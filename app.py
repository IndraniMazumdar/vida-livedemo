import streamlit as st
import time
from pathlib import Path

st.set_page_config(page_title="Vida – Multimodal AI Analysis", layout="wide")

st.title("Vida – Multimodal Emotion Analysis for Mental Health Triage")
st.markdown("---")

# 1. Display Video
st.header("Patient Video Session")
video_path = "static/my_video.mp4"
st.video(video_path)

# 2. Simulated Transcription (Whisper output)
st.markdown("---")
st.header("Voice Transcription")
if st.button("Run Transcription"):
    with st.spinner("Transcribing audio using Whisper..."):
        time.sleep(2)
    st.success("Transcription complete!")
    transcription = (
        Lately, I just feel empty. I don't have the energy to get out of the bed some days. I'm
not really sleeping very well. I'm always tired. It's like nothing really matters anymore.
I just feel very stuck. I used to enjoy a lot of things such as gymming and cooking but I just go
through the motions now. People keep asking if I'm okay. I see I'm fine but I'm not really fine.
    )
    st.text_area("Transcribed Text", transcription, height=180)

# 3. NLP Risk & Sentiment Analysis
st.markdown("---")
st.header("NLP-Based Risk & Sentiment Insights")
if st.button("Run Text Risk Analysis"):
    with st.spinner("Analyzing text for affective and risk cues..."):
        time.sleep(2)
    st.success("Analysis complete.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Sentiment", "Negative")
        st.metric("Emotion Detected", "Sadness")
    with col2:
        st.metric("Keyphrase: Anhedonia", "✔️")
        st.metric("Sleep Disturbance", "✔️")
    with col3:
        st.metric("Risk Level", "Moderate")
        st.metric("LLM Confidence", "92%")

# 4. Facial Emotion & Gaze (Simulated MediaPipe output)
st.markdown("---")
st.header("Facial Emotion & Gaze Tracking")
if st.button("Run Video Emotion Analysis"):
    with st.spinner("Detecting gaze, facial emotion, and micro-expressions..."):
        time.sleep(2)
    st.success("Facial analysis complete.")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.metric("Facial Emotion", "Low Energy")
        st.metric("Mouth Movement", "Minimal")
    with col5:
        st.metric("Gaze Direction", "Downward")
        st.metric("Blink Rate", "Reduced")
    with col6:
        st.metric("Posture", "Slouched")
        st.metric("Expressivity", "Low")

# 5. Final Summary Panel
st.markdown("---")
st.header("📋 Clinician Review Summary")
summary = (
    "Patient exhibits signs of emotional exhaustion and detachment. Voice tone is flat with low variation. Facial features including gaze and expressivity suggest depressive affect. "
    "Transcribed content supports symptoms of anhedonia, fatigue, and social withdrawal. Risk level moderate. Recommend follow-up psychological evaluation."
)
st.text_area("Editable Summary", summary, height=180)
st.download_button("Download Summary", summary, file_name="vida_clinical_summary.txt")
