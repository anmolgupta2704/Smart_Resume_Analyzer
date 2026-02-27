# 📄 Smart Resume Analyzer (Domain Based ATS):-

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-1.26.1-orange)](https://streamlit.io/)  
[![ATS Score](https://img.shields.io/badge/ATS-Ready-green)](https://en.wikipedia.org/wiki/Applicant_tracking_system)  

**Smart Resume Analyzer** is a **Streamlit-based AI-powered resume tool** that helps users:

- Improve resumes
- Match domain-specific skills
- Generate professional PDFs with selectable templates

---

## 🚀 Key Features

- **Domain Selection:** Data Science, Web Development, Machine Learning, DevOps, Android Development, Software Engineering  
- **Resume Upload:** PDF or TXT files  
- **Skill Matching:** Fuzzy logic matches your resume against trending skills in your domain  
- **ATS Score:** Calculates a percentage showing resume optimization  
- **Resume Enhancement:** AI-enhanced experience bullet points  
- **Template Selection & PDF Download:** Choose from ATS, Modern, or Creative templates  
- **Downloadable Reports:** CSV of matched/missing skills and PDF resume  

---   


## 🧠 How It Works

1. User selects their **career domain**  
2. Uploads their **resume (PDF or TXT)**  
3. The app **extracts text** from the resume  
4. **Matches skills** against domain-specific trending skills  
5. Calculates **ATS Score**  
6. Displays **matched and missing skills**, with AI-enhanced improvement suggestions  
7. User can **preview the resume** in a selected template and download it as PDF  

---

<!--## 🖼 App Preview

**1️⃣ Dashboard with Domain Selection & File Upload**  
![Dashboard](screenshots/dashboard.png)  

**2️⃣ Skills Analysis & ATS Score**  
![ATS Score](screenshots/ats_score.png)  

**3️⃣ Template Preview & Download**  
![Template Preview](screenshots/template_preview.png)  

---
-->   


## 📂 File Structure

```bash
PROJECT_RESUME_DETECTION/
├── app.py                  # Streamlit app
├── utils.py                # Helper functions (PDF parsing, AI enhancement, PDF rendering)
├── templates/              # HTML templates
│   ├── template_ats.html
│   ├── template_modern.html
│   └── template_creative.html
├── requirements.txt        # Python dependencies
├── screenshots/            # Placeholder for app screenshots
└── README.md               # This file
```


## 📁 How to Run

1. **Clone or download** this repository
2. Create a virtual environment (optional but recommended)

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # For Windows
👨‍💻 Author

Made with ❤️ for academic/project use.


---
## Install dependencies
```bash
pip install -r requirements.txt

```
## Run the app
```bash
streamlit run app.py
```
```bash
Open browser at http://localhost:8501
```
