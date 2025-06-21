import streamlit as st
import time

# --- Set page and load Google Fonts ---
st.set_page_config(page_title="Vida – Multimodal AI Intake", layout="wide")
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
        background-color: #f8f9fb;
    }

    .header-container {
        display: flex;
        align-items: center;
        background: linear-gradient(90deg, #e6f0ff, #f9fbff);
        padding: 20px;
        border-radius: 10px;
    }

    .header-container img {
        margin-right: 15px;
    }

    .header-container h1 {
        font-size: 28px;
        margin-bottom: 0;
    }

    .subtext {
        font-size: 16px;
        color: #5c5c5c;
    }

    .question {
        font-size: 20px;
        font-weight: 600;
        color: #003366;
        margin-top: 25px;
        margin-bottom: 10px;
    }

    .transcription {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #dce0e6;
        font-style: italic;
        color: #333;
    }

    .summary-box {
        background-color: #ffffff;
        border: 1px solid #ccc;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.03);
    }
    </style>
""", unsafe_allow_html=True)

# --- Custom Header with Logo ---
st.markdown(
    """
    <div class="header-container">
        <img src='https://raw.githubusercontent.com/indranimazumdar/vida-livedemo/main/static/avatar.png' width='60'>
        <div>
            <h1>Vida – Multimodal Emotion Analysis for Mental Health Triage</h1>
            <p class="subtext">AI-powered intake assistant analyzing patient speech, facial cues, and emotional state.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Welcome Message ---
st.markdown("---")
st.markdown("### Welcome")
st.markdown(
    "This brief session guides the patient through two intake questions. "
    "Vida will analyze the video, transcribe the audio, and provide insights into emotional well-being."
)

# --- Clip 1 ---
st.markdown("<div class='question'>Question 1: I’d like to start by checking in, how have you been feeling lately, both physically and emotionally?</div>", unsafe_allow_html=True)
st.video("static/my_video_clip_1.mp4")

with st.expander("Transcribed Response – Clip 1"):
    st.markdown(
        "<div class='transcription'>Lately, I just feel empty. I don't have the energy to get out of bed some days. I'm not really sleeping very well. I'm always tired. It's like nothing really matters anymore.</div>",
        unsafe_allow_html=True,
    )

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
st.markdown("<div class='question'>Question 2: Do you ever find yourself going through the motions in your daily life, even with things you used to love?</div>", unsafe_allow_html=True)
st.video("static/my_video_clip_2.mp4")

with st.expander("Transcribed Response – Clip 2"):
    st.markdown(
        "<div class='transcription'>I just feel very stuck. I used to enjoy a lot of things such as gymming and cooking but I just go through the motions now. People keep asking if I'm okay. I say I'm fine but I'm not really fine.</div>",
        unsafe_allow_html=True,
    )

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
st.markdown(
    "<div class='summary-box'>"
    "Patient expresses emotional fatigue and detachment. Verbal and visual cues suggest depressive affect. "
    "There is a notable decline in motivation and interest in previously enjoyed activities. "
    "Speech is low-energy, posture is slouched, and expressivity is minimal. Recommend follow-up screening."
    "</div>",
    unsafe_allow_html=True
)

# Optional editable text
summary = (
    "Patient expresses emotional fatigue and detachment. Verbal and visual cues suggest depressive affect. "
    "There is a notable decline in motivation and interest in previously enjoyed activities. "
    "Speech is low-energy, posture is slouched, and expressivity is minimal. Recommend follow-up screening."
)
st.download_button("Download Summary", summary, file_name="vida_summary.txt")
