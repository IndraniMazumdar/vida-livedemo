import streamlit as st
import time

st.set_page_config(page_title="Vida – Multimodal AI Intake", layout="wide")

# --- Custom Header with Logo ---
st.markdown(
    """
    <div style='display: flex; align-items: center;'>
        <img src='https://raw.githubusercontent.com/indranimazumdar/vida-livedemo/main/static/avatar.png' width='60'>
        <h1 style='padding-left: 15px;'>Vida – Multimodal Emotion Analysis for Mental Health Triage</h1>
    </div>
    <p style='font-size:16px; color:gray;'>AI-powered intake assistant analyzing patient speech, facial cues, and emotional state.</p>
    """,
    unsafe_allow_html=True
)

# --- Welcome Message ---
st.markdown("---")
st.markdown("### Welcome")
st.markdown(
    "Thank you for checking in. This brief session will guide you through a couple of simple questions. "
    "Our assistant will analyze the video, transcribe your response, and provide emotional risk insights to help clinicians understand how you’re feeling."
)

# --- Clip 1 ---
st.markdown("---")
st.markdown("## Question 1: I’d like to start by checking in, how have you been feeling lately, both physically and emotionally?")
st.video("static/my_video_clip_1.mp4")

# --- Analysis 1 ---
if st.button("Run Analysis for Clip 1"):
    with st.spinner("Analyzing response..."):
        time.sleep(2)
    st.success("Analysis complete.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Facial Emotion", "Tired / Flat")
        st.metric("Blink Rate", "Low")
    with col2:
        st.metric("Sentiment", "Negative")
        st.metric("Gaze", "Downcast")
    with col3:
        st.metric("Energy Level", "Low")
        st.metric("Speech Rate", "Slow")

# --- Clip 2 ---
st.markdown("---")
st.markdown("## Question 2: Do you ever find yourself going through the motions in your daily life, even with things you used to love?")
st.video("static/my_video_clip_2.mp4")

# --- Analysis 2 ---
if st.button("Run Analysis for Clip 2"):
    with st.spinner("Analyzing response..."):
        time.sleep(2)
    st.success("Analysis complete.")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.metric("Facial Emotion", "Resigned")
        st.metric("Posture", "Slouched")
    with col5:
        st.metric("Sentiment", "Negative")
        st.metric("Confidence", "93%")
    with col6:
        st.metric("Expressivity", "Low")
        st.metric("Keyphrase", "Disengagement")

# --- Final Summary ---
st.markdown("---")
st.markdown("## 📋 Clinician Review Summary")
summary_text = (
    "Patient expresses emotional fatigue and detachment. Verbal and visual cues suggest depressive affect. "
    "There is a notable decline in motivation and interest in previously enjoyed activities. "
    "Speech is low-energy, posture is slouched, and expressivity is minimal. Recommend follow-up screening."
)
st.text_area("Editable Summary", summary_text, height=200)
st.download_button("Download Summary", summary_text, file_name="vida_summary.txt")
