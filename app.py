import streamlit as st
import time

st.set_page_config(page_title="Vida – Video Emotion Analysis", layout="wide")

# Header
st.title("🎥 VIDA – Video-Based Emotion Analysis")
st.markdown("_Using patient video input to simulate facial emotion recognition from the CREMA-D dataset._")
st.markdown("---")

# Play sample patient video
st.header("📼 Sample Patient Video")
st.video("static/CREMA_sample.mp4")

# Simulated analysis
st.markdown("---")
st.header("🧠 Emotion Analysis (Simulated)")
st.markdown("Click the button below to simulate analysis of facial expressions from the video.")

if st.button("Run Emotion Analysis"):
    with st.spinner("Analyzing video for emotional expressions..."):
        time.sleep(2)
    st.success("Analysis complete!")
    st.json({
        "Detected Emotion": "Sad",
        "Confidence": 0.84,
        "Key Observations": [
            "Lowered eyebrows",
            "Downturned mouth",
            "Lack of eye contact"
        ]
    })

# Clinician summary
st.markdown("---")
st.header("📋 Clinician Summary")
default_summary = "Patient appears sad and emotionally withdrawn based on facial expressions."
editable_summary = st.text_area("Edit Summary Below:", default_summary, height=150)
st.download_button("📥 Download Summary", editable_summary, file_name="vida_video_summary.txt")
