import streamlit as st
from rapidfuzz import fuzz
from utils import extract_text_from_pdf, render_resume_pdf, enhance_experience_with_ai
from web_scraper import get_latest_skills, get_all_domains
import streamlit.components.v1 as components
from auth import require_login_if_needed, google_login_button, register_user, login_user, logout
from db import init_db
from history import save_resume_history, get_resume_history
import pandas as pd
import io
import re

# ---------------- Init DB ----------------
init_db()

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Smart Resume Analyzer",
    layout="wide",
    page_icon="📄",
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
    .skill-badge-green  { background:#d1fae5; color:#065f46; padding:4px 10px; border-radius:12px; margin:3px; display:inline-block; font-size:0.82rem; }
    .skill-badge-red    { background:#fee2e2; color:#991b1b; padding:4px 10px; border-radius:12px; margin:3px; display:inline-block; font-size:0.82rem; }
    .skill-badge-blue   { background:#e1ecf4; color:#0366d6; padding:4px 10px; border-radius:12px; margin:3px; display:inline-block; font-size:0.82rem; }
    .skill-badge-yellow { background:#fef9c3; color:#78350f; padding:4px 10px; border-radius:12px; margin:3px; display:inline-block; font-size:0.82rem; }
    .score-box { padding:16px; border-radius:12px; text-align:center; }
</style>
""", unsafe_allow_html=True)

# ---------------- Login Gate ----------------
if not require_login_if_needed():
    st.title("🔐 Login Required")
    tab1, tab2 = st.tabs(["Google Login", "Email Login / Register"])
    with tab1:
        google_login_button()
    with tab2:
        email_inp = st.text_input("Email")
        password_inp = st.text_input("Password", type="password")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Register"):
                if not email_inp or not password_inp:
                    st.error("Email and password required")
                else:
                    ok, msg = register_user(email_inp, password_inp)
                    st.success(msg) if ok else st.error(msg)
        with col2:
            if st.button("Login"):
                if login_user(email_inp, password_inp):
                    st.session_state.user = email_inp
                    st.success("Logged in!")
                    st.rerun()
                else:
                    st.error("Invalid credentials")
    st.stop()

# ---------------- Sidebar ----------------
st.sidebar.title("⚙️ Settings")

if "user" in st.session_state:
    st.sidebar.markdown(f"👤 **{st.session_state.user}**")
    if st.sidebar.button("🚪 Logout"):
        logout()

# All domains from web_scraper
all_domains = get_all_domains()

domain = st.sidebar.selectbox("Choose Domain", all_domains, index=all_domains.index("Software Engineering") if "Software Engineering" in all_domains else 0)
threshold = st.sidebar.slider("Skill Match Sensitivity (%)", 60, 100, 80, step=5)
show_tips = st.sidebar.checkbox("💡 AI Resume Tips", value=True)

# Fetch skills for selected domain
live_skills = get_latest_skills(domain)

st.sidebar.markdown("### 📌 Trending Skills")
st.sidebar.markdown(
    " ".join([f"<span class='skill-badge-blue'>{s}</span>" for s in live_skills]),
    unsafe_allow_html=True,
)

# Navigation
tab = st.sidebar.radio("Go To", ["🧠 Skill Analyzer", "🎯 JD Matcher", "📄 Resume Builder", "👤 Profile"])


# ─────────────────────────── HELPERS ────────────────────────────────────────

def fuzzy_match(skill, text, threshold=80):
    return fuzz.partial_ratio(skill.lower(), text.lower()) >= threshold

def match_resume_with_skills(text, skills, threshold=80):
    matched = [s for s in skills if fuzzy_match(s, text, threshold)]
    missing = [s for s in skills if s not in matched]
    return matched, missing

def calculate_score(matched, total):
    return round((len(matched) / len(total)) * 100, 2) if total else 0

def badges(skill_list, css_class):
    return " ".join([f"<span class='{css_class}'>{s}</span>" for s in skill_list])

def ai_suggestions(missing_skills, domain):
    if not missing_skills:
        return "🎉 Your resume already covers all important skills!"
    prompt = f"""You are a resume expert. The user is applying for {domain} roles.
Their resume is missing: {', '.join(missing_skills)}.

Provide 5 concise bullet points covering:
- How to add these skills to the resume
- Quick ways to learn them
- Project ideas to demonstrate them
Keep each bullet under 2 lines."""
    try:
        return enhance_experience_with_ai(prompt)
    except Exception as e:
        return f"⚠️ AI Error: {str(e)}"

def make_csv(matched, missing, domain):
    rows = (
        [{"Skill": s, "Status": "✅ Matched", "Domain": domain} for s in matched] +
        [{"Skill": s, "Status": "❌ Missing",  "Domain": domain} for s in missing]
    )
    df = pd.DataFrame(rows)
    buf = io.StringIO()
    df.to_csv(buf, index=False)
    return buf.getvalue().encode("utf-8")

def extract_skills_from_jd(jd_text):
    """Return words/phrases likely to be skills from JD text."""
    # Split on common delimiters and clean
    tokens = re.split(r"[,•\n\-–|/]", jd_text)
    skills = []
    for t in tokens:
        t = t.strip()
        # Keep tokens that look like skill names (2–40 chars, not pure stopwords)
        if 4 <= len(t) <= 40 and not t.lower().startswith(("the ", "and ", "or ", "with ", "must ", "should ")):
            skills.append(t)
    return list(dict.fromkeys(skills))  # deduplicate preserving order


# ══════════════════════════════════════════════════════════════════════════════
# TAB 1: SKILL ANALYZER
# ══════════════════════════════════════════════════════════════════════════════
if tab == "🧠 Skill Analyzer":
    st.title("🧠 Resume Skill Analyzer")
    st.caption(f"Domain: **{domain}**  |  Skills checked: **{len(live_skills)}**  |  Match sensitivity: **{threshold}%**")

    uploaded = st.file_uploader("Upload Your Resume (PDF or TXT)", type=["pdf", "txt"])

    if uploaded:
        resume_text = (
            extract_text_from_pdf(uploaded)
            if uploaded.type == "application/pdf"
            else uploaded.read().decode("utf-8")
        )
        matched, missing = match_resume_with_skills(resume_text, live_skills, threshold)
        score = calculate_score(matched, live_skills)

        # ── Score Section ────────────────────────────────────────────────────
        st.markdown("---")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("🎯 ATS Score",        f"{score}%")
        c2.metric("✅ Skills Matched",   len(matched))
        c3.metric("❌ Skills Missing",   len(missing))
        c4.metric("📋 Total Skills",     len(live_skills))

        # Score bar
        st.progress(int(score))
        if score >= 80:
            st.success("🟢 Excellent! Your resume is well-optimized for this domain.")
        elif score >= 60:
            st.warning("🟡 Good start — add a few more skills to improve.")
        else:
            st.error("🔴 Your resume needs significant skill additions for this domain.")

        # ── Skill Breakdown ──────────────────────────────────────────────────
        st.markdown("---")
        col_m, col_miss = st.columns(2)
        with col_m:
            st.markdown("### ✅ Matched Skills")
            st.markdown(badges(matched, "skill-badge-green"), unsafe_allow_html=True)

        with col_miss:
            st.markdown("### ❌ Missing Skills")
            st.markdown(badges(missing, "skill-badge-red"), unsafe_allow_html=True)

        # ── AI Tips ─────────────────────────────────────────────────────────
        if show_tips and missing:
            st.markdown("---")
            with st.expander("💡 AI-Based Resume Improvement Tips", expanded=False):
                with st.spinner("Generating tips…"):
                    st.markdown(ai_suggestions(missing, domain))

        # ── Score Breakdown Chart ────────────────────────────────────────────
        st.markdown("---")
        st.markdown("### 📊 Skill Coverage Breakdown")
        breakdown_df = pd.DataFrame({
            "Category": ["Matched", "Missing"],
            "Count":    [len(matched), len(missing)],
        })
        st.bar_chart(breakdown_df.set_index("Category"))

        # ── Download CSV ─────────────────────────────────────────────────────
        st.download_button(
            "📥 Download Skill Report (CSV)",
            data=make_csv(matched, missing, domain),
            file_name=f"skill_report_{domain.replace(' ','_')}.csv",
            mime="text/csv",
        )

        # ── Save History ─────────────────────────────────────────────────────
        if "user" in st.session_state:
            save_resume_history(st.session_state.user, domain, score)

        st.session_state.usage_count = st.session_state.get("usage_count", 0) + 1


# ══════════════════════════════════════════════════════════════════════════════
# TAB 2: JD MATCHER (NEW!)
# ══════════════════════════════════════════════════════════════════════════════
elif tab == "🎯 JD Matcher":
    st.title("🎯 Job Description Matcher")
    st.caption("Paste any job description — we'll compare your resume against its required skills.")

    col_l, col_r = st.columns(2)

    with col_l:
        st.subheader("📋 Paste Job Description")
        jd_text = st.text_area("Job Description", height=300, placeholder="Paste the full JD here…")

    with col_r:
        st.subheader("📄 Upload Your Resume")
        jd_resume = st.file_uploader("Resume (PDF or TXT)", type=["pdf", "txt"], key="jd_resume")

    if st.button("🔍 Analyze Match", use_container_width=True):
        if not jd_text.strip():
            st.error("Please paste a Job Description.")
        elif jd_resume is None:
            st.error("Please upload your resume.")
        else:
            resume_text = (
                extract_text_from_pdf(jd_resume)
                if jd_resume.type == "application/pdf"
                else jd_resume.read().decode("utf-8")
            )

            # Extract skills from JD
            jd_skills = extract_skills_from_jd(jd_text)

            if not jd_skills:
                st.warning("Could not extract skills from the JD. Make sure it lists requirements.")
            else:
                matched_jd, missing_jd = match_resume_with_skills(resume_text, jd_skills, threshold)
                jd_score = calculate_score(matched_jd, jd_skills)

                st.markdown("---")
                c1, c2, c3 = st.columns(3)
                c1.metric("🎯 JD Match Score", f"{jd_score}%")
                c2.metric("✅ Matched",         len(matched_jd))
                c3.metric("❌ Missing",          len(missing_jd))

                st.progress(int(jd_score))

                if jd_score >= 75:
                    st.success("🟢 Strong match! You're a good fit for this JD.")
                elif jd_score >= 50:
                    st.warning("🟡 Decent match — address the missing skills in your resume.")
                else:
                    st.error("🔴 Low match — consider tailoring your resume for this role.")

                c_m, c_miss = st.columns(2)
                with c_m:
                    st.markdown("### ✅ Skills You Have")
                    st.markdown(badges(matched_jd, "skill-badge-green"), unsafe_allow_html=True)
                with c_miss:
                    st.markdown("### ❌ Skills to Add / Highlight")
                    st.markdown(badges(missing_jd, "skill-badge-yellow"), unsafe_allow_html=True)

                # AI gap analysis
                if show_tips and missing_jd:
                    with st.expander("💡 How to Close the Skill Gap", expanded=False):
                        with st.spinner("Generating tips…"):
                            st.markdown(ai_suggestions(missing_jd[:10], domain))

                st.download_button(
                    "📥 Download JD Match Report (CSV)",
                    data=make_csv(matched_jd, missing_jd, "JD Match"),
                    file_name="jd_match_report.csv",
                    mime="text/csv",
                )

                if "user" in st.session_state:
                    save_resume_history(st.session_state.user, f"JD Match ({domain})", jd_score)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 3: RESUME BUILDER
# ══════════════════════════════════════════════════════════════════════════════
elif tab == "📄 Resume Builder":
    st.title("📄 ATS Resume Builder")
    left, right = st.columns([1, 1.2])

    with left:
        with st.form("resume_form"):
            st.subheader("👤 Personal Info")
            name     = st.text_input("Full Name")
            email    = st.text_input("Email")
            phone    = st.text_input("Phone")
            linkedin = st.text_input("LinkedIn URL (optional)")
            github   = st.text_input("GitHub URL (optional)")

            st.subheader("📝 Professional Summary")
            summary = st.text_area("Summary")

            st.subheader("💡 Skills")
            skills = st.text_area("Skills (comma separated)")

            st.subheader("🎓 Education")
            education = st.text_area("Education (one per line)")

            st.subheader("💼 Experience")
            experience = st.text_area("Experience (one per line)")

            st.subheader("🛠 Projects")
            projects = st.text_area("Projects (one per line)")

            st.subheader("🏆 Certifications (optional)")
            certifications = st.text_area("Certifications (one per line)")

            st.subheader("✨ AI Enhancer")
            enhance = st.checkbox("Enhance Experience with AI")

            template_choice = st.selectbox("Choose Template", ["ats", "modern", "creative"])
            submitted = st.form_submit_button("Generate Resume")

    if submitted:
        exp_text = enhance_experience_with_ai(experience) if enhance else experience
        resume_data = {
            "name":           name,
            "email":          email,
            "phone":          phone,
            "linkedin":       linkedin,
            "github":         github,
            "summary":        summary,
            "skills":         [s.strip() for s in skills.split(",")       if s.strip()],
            "education":      [e.strip() for e in education.split("\n")   if e.strip()],
            "experience":     [e.strip() for e in exp_text.split("\n")    if e.strip()],
            "projects":       [p.strip() for p in projects.split("\n")    if p.strip()],
            "certifications": [c.strip() for c in certifications.split("\n") if c.strip()],
        }

        with right:
            st.subheader("📄 Resume Preview")
            html_preview = render_resume_pdf(resume_data, template_choice, preview=True)
            components.html(html_preview, height=800, scrolling=True)
            pdf_bytes = render_resume_pdf(resume_data, template_choice, preview=False)
            st.download_button(
                "📥 Download PDF",
                pdf_bytes,
                file_name=f"{name.replace(' ', '_')}_resume.pdf",
                mime="application/pdf",
            )


# ══════════════════════════════════════════════════════════════════════════════
# TAB 4: PROFILE
# ══════════════════════════════════════════════════════════════════════════════
elif tab == "👤 Profile":
    st.title("👤 My Profile")
    st.markdown(f"**Email:** {st.session_state.get('user')}")

    rows = get_resume_history(st.session_state.get("user"))
    st.subheader("📜 Resume Check History")

    if not rows:
        st.info("No resume checks yet. Upload a resume to get started!")
    else:
        df = pd.DataFrame(rows, columns=["Domain", "ATS Score (%)", "Checked At"])
        st.dataframe(df, use_container_width=True)

        # Quick stats
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Checks",  len(rows))
        c2.metric("Best Score",    f"{max(r[1] for r in rows)}%")
        c3.metric("Avg Score",     f"{round(sum(r[1] for r in rows)/len(rows), 1)}%")

        # Score trend
        st.subheader("📈 Score Trend")
        trend_df = pd.DataFrame({"Check #": range(1, len(rows)+1), "Score": [r[1] for r in rows][::-1]})
        st.line_chart(trend_df.set_index("Check #"))