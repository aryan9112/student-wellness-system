import streamlit as st

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Student Wellness System",
    page_icon="🧠",
    layout="centered"
)

# ---------------- Header ----------------
st.title("🧠 Student Wellness System")
st.subheader("AI & Cloud Based Mental Wellness Analyzer")

st.info(
    "This system uses AI-based decision logic to analyze student stress levels "
    "and provide personalized wellness suggestions. "
    "The application is cloud-deployable and accessible via a web browser."
)

st.markdown("---")

# ---------------- User Input ----------------
st.header("📋 Student Self-Assessment Questionnaire")

academic_stress = st.slider(
    "📚 Academic Stress Level", 0, 10, 5
)

sleep_quality = st.slider(
    "😴 Sleep Quality", 0, 10, 5
)

anxiety_level = st.slider(
    "😟 Anxiety / Overthinking Level", 0, 10, 5
)

social_support = st.slider(
    "🤝 Social Support Level", 0, 10, 5
)

st.markdown("---")

# ---------------- AI Decision Logic ----------------
if st.button("🔍 Analyze My Wellness"):

    score = academic_stress + anxiety_level + (10 - sleep_quality) + (10 - social_support)

    st.markdown("### 📊 Analysis Result")
    st.write(f"**Stress Score:** `{score} / 40`")

    # Progress bar for visualization
    st.progress(score / 40)

    st.markdown("---")

    if score <= 10:
        st.success("🟢 Wellness Status: GOOD")
        st.write("""
        **AI Suggestions:**
        • Maintain your healthy routine  
        • Stay physically active  
        • Continue good sleep habits  
        """)

    elif score <= 25:
        st.warning("🟡 Wellness Status: MODERATE")
        st.write("""
        **AI Suggestions:**
        • Take regular study breaks  
        • Improve sleep schedule  
        • Practice meditation or breathing exercises  
        """)

    else:
        st.error("🔴 Wellness Status: NEEDS ATTENTION")
        st.write("""
        **AI Suggestions:**
        • Reduce stress triggers  
        • Talk to friends or family  
        • Maintain proper sleep routine  
        • Seek professional counseling if required  
        """)

# ---------------- Footer ----------------
st.markdown("---")
st.caption(
    "⚠ Educational Project | Demonstrates AI-based decision logic and Cloud deployment "
    "| Not a replacement for professional medical advice."
)
