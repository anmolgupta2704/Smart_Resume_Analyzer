import os
import json
from PyPDF2 import PdfReader
from jinja2 import Environment, FileSystemLoader
import pdfkit
from dotenv import load_dotenv
from google import genai

# ------------------ CONFIGURATION ------------------

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

client = genai.Client(api_key=GOOGLE_API_KEY)

env = Environment(loader=FileSystemLoader("templates"))

WKHTML_PATH = os.getenv("WKHTMLTOPDF_PATH")
if not WKHTML_PATH:
    if os.name == "nt":
        WKHTML_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    else:
        WKHTML_PATH = "/usr/bin/wkhtmltopdf"

config = pdfkit.configuration(wkhtmltopdf=WKHTML_PATH)

# ---------------------------------------------------


def extract_text_from_pdf(file) -> str:
    """Extract readable text from PDF."""
    try:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {str(e)}"


def enhance_experience_with_ai(experience_text: str) -> str:
    """Enhance resume experience / run any prompt using Gemini AI."""
    if not experience_text.strip():
        return ""
    try:
        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=experience_text
        )
        return response.text
    except Exception as e:
        return f"⚠️ AI Enhancement Error: {str(e)}"


def extract_jd_skills_with_ai(jd_text: str) -> list[str]:
    """
    Use Gemini to extract ONLY technical/domain skills and tools from a JD.
    Returns a clean list — NOT raw sentences — so ATS matching is accurate.
    """
    if not jd_text.strip():
        return []

    prompt = f"""You are an expert technical recruiter and ATS specialist.

From the job description below, extract ONLY the technical skills, tools, technologies,
programming languages, frameworks, methodologies, and domain-specific keywords
that a candidate must or should have.

Rules:
- Return ONLY a valid JSON array of short skill strings (1-4 words each)
- Do NOT include soft skills like "communication", "teamwork", "problem solving"
- Do NOT include years of experience, education, or company names
- Do NOT include job titles, locations, or salary details
- Remove duplicates
- Each skill must be a specific, matchable keyword (e.g. "React", "Python", "Docker", "REST API")

Job Description:
\"\"\"
{jd_text[:4000]}
\"\"\"

Return ONLY valid JSON like: ["Python", "Django", "PostgreSQL", "REST API", "Docker"]
No explanation, no markdown, no extra text."""

    try:
        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=prompt
        )
        raw = response.text.strip()

        # Strip markdown code blocks if present
        raw = raw.replace("```json", "").replace("```", "").strip()

        skills = json.loads(raw)
        if isinstance(skills, list):
            # Clean and deduplicate
            return list(dict.fromkeys(
                s.strip() for s in skills if isinstance(s, str) and 1 < len(s.strip()) <= 50
            ))
        return []
    except Exception as e:
        # Fallback: simple regex-based extraction if AI fails
        import re
        tokens = re.split(r"[,•\n\-–|/()]", jd_text)
        skills = []
        stopwords = {"the", "and", "or", "with", "must", "should", "will", "have",
                     "this", "that", "for", "from", "are", "our", "you", "your",
                     "able", "team", "work", "role", "join", "help", "also",
                     "experience", "years", "strong", "good", "knowledge", "ability"}
        for t in tokens:
            t = t.strip()
            words = t.split()
            if 1 <= len(words) <= 4 and 2 <= len(t) <= 40:
                lower_t = t.lower()
                if not any(lower_t.startswith(sw) for sw in stopwords):
                    skills.append(t)
        return list(dict.fromkeys(skills))[:40]  # cap at 40


def render_resume_pdf(resume_data, template_choice="ats", preview=False):
    """Render resume HTML or convert to PDF using wkhtmltopdf."""
    try:
        template = env.get_template(f"template_{template_choice}.html")
        html_content = template.render(**resume_data)

        if preview:
            return html_content

        options = {
            "page-size": "A4",
            "encoding": "UTF-8",
            "enable-local-file-access": "",
            "margin-top": "10mm",
            "margin-bottom": "10mm",
            "margin-left": "10mm",
            "margin-right": "10mm",
        }

        pdf_bytes = pdfkit.from_string(
            html_content, False, options=options, configuration=config
        )
        return pdf_bytes

    except Exception as e:
        return f"Error generating PDF: {str(e)}"


# ------------------------ DOMAIN SKILLS ------------------------

domain_skill_map = {
    "Data Science": ["Python", "Pandas", "NumPy", "Scikit-learn", "Matplotlib", "SQL", "Jupyter"],
    "Web Development": ["HTML", "CSS", "JavaScript", "React", "Node.js", "Bootstrap", "Git"],
    "Machine Learning": ["TensorFlow", "PyTorch", "ML Algorithms", "Scikit-learn", "Python"],
    "DevOps": ["Docker", "Kubernetes", "AWS", "CI/CD", "Linux"],
    "Android Development": ["Java", "Kotlin", "XML", "Firebase", "Android Studio"],
    "Software Engineering": ["OOP", "Data Structures", "Algorithms", "Git", "C++", "Java"],
}

def get_latest_skills(domain: str):
    return domain_skill_map.get(domain, [])