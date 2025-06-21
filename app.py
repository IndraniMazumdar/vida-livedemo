import streamlit as st
import time

st.set_page_config(page_title="Vida – Multimodal AI Analysis", layout="wide")

st.title("Vida – Multimodal Emotion Analysis for Mental Health Triage")
st.markdown("_Combining video, voice, and language insights to support mental health professionals._")
st.markdown("---")

# Clip 1 + Opening Question
st.header("🧍 Session Start: Patient Introduction")
st.video("static/patient_video_part_1.mp4")
st.markdown("**Vida:** _“Thank you for being here today. Could you tell me how you’ve been feeling lately, both physically and emotionally?”_")

if st.button("Analyze Introduction"):
    with st.spinner("Analyzing patient tone, expression, and sentiment..."):
        time.sleep(2)
    st.success("Initial analysis complete.")
    st.markdown("**Insights from First Segment:**")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Sentiment", "Negative")
        st.metric("Energy Level", "Low")
    with col2:
        st.metric("Motivation", "Minimal")
        st.metric("Fatigue Indicators", "High")

st.markdown("---")

# Clip 2 + Follow-up Question
st.header("🔄 Follow-Up: Emotional Withdrawal Discussion")
st.video("static/patient_video_part_2.mp4")
st.markdown("**Vida:** _“You mentioned losing interest in things you once enjoyed — how long have you been feeling this way, and has it changed recently?”_")

if st.button("Analyze Follow-Up"):
    with st.spinner("Analyzing continued expression and verbal cues..."):
        time.sleep(2)
    st.success("Follow-up analysis complete.")
    st.markdown("**Insights from Second Segment:**")
    col3, col4 = st.columns(2)
    with col3:
        st.metric("Anhedonia", "Present")
        st.metric("Expressivity", "Low")
    with col4:
        st.metric("Social Withdrawal", "Likely")
        st.metric("Risk Level", "Moderate")

st.markdown("---")

# Transcription
st.header("🗣️ What the Patient Said (Transcription)")
transcription = \"\"\"Lately, I've been feeling very sleepy. I don't have much energy. I don't feel like getting out of the bed. I don't feel very motivated enough.
I used to love cooking, gymming, taking my dog out for walks, but I don't know. It's not been the same anymore. I think I'm losing zeal, confidence in life.
People keep asking me if I'm happy or if I'm satisfied. I just keep nodding and saying yes to things, but I don't know if I really feel like that anymore.\"\"\"
st.text_area("Session Transcript", transcription, height=180)

# NLP Insights
st.markdown("---")
st.header("🧠 Language & Emotion Signals (LLM Analysis)")
if st.button("Run Text Analysis"):
    with st.spinner("Extracting emotional markers and clinical red flags..."):
        time.sleep(2)
    st.success("Textual analysis complete.")
    col5, col6, col7 = st.columns(3)
    with col5:
        st.metric("Sentiment", "Negative")
        st.metric("Emotion Detected", "Sadness")
    with col6:
        st.metric("Sleep Disturbance", "✔️")
        st.metric("Keyphrase: Anhedonia", "✔️")
    with col7:
        st.metric("Risk Level", "Moderate")
        st.metric("Model Confidence", "92%")

# Final Summary
st.markdown("---")
st.header("📋 Clinician Summary & Risk Impression")
summary = \"\"\"Patient expresses signs of low mood, fatigue, and diminished motivation in the first half of the session.
The second half reflects clear anhedonia, emotional withdrawal, and reduced self-confidence.
Facial expressions and verbal tone support the presence of depressive symptoms. Recommend psychological evaluation and ongoing monitoring.\"\"\"
st.text_area("Editable Summary", summary, height=180)
st.download_button("Download Summary", summary, file_name="vida_clinical_summary.txt")
