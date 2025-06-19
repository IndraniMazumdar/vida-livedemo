import streamlit as st
import time

st.set_page_config(page_title="VIDA – Per-Segment Emotion Analysis", layout="wide")
st.title("🎬 VIDA – Analyze Emotional Segments Separately")
st.markdown("_Play and analyze each clip individually for high-resolution emotional insight._")
st.markdown("---")

# Segment 1
st.header("🎥 Segment 1 – Sad Clip")
st.video("static/CREMA_sample_1.mp4")
if st.button("Analyze Segment 1"):
    with st.spinner("Analyzing Segment 1..."):
        time.sleep(2)
    st.success("Analysis Complete!")
    st.json({
        "Detected Emotion": "Sad",
        "Confidence": 0.84,
        "Observations": ["Downturned mouth", "Low eye contact", "Low vocal tone"]
    })
    seg1_notes = st.text_area("Clinician Notes – Segment 1", height=100)
else:
    seg1_notes = ""

# Segment 2
st.header("🎥 Segment 2 – Happy Clip")
st.video("static/CREMA_sample_2.mp4")
if st.button("Analyze Segment 2"):
    with st.spinner("Analyzing Segment 2..."):
        time.sleep(2)
    st.success("Analysis Complete!")
    st.json({
        "Detected Emotion": "Happy",
        "Confidence": 0.78,
        "Observations": ["Smiling", "Raised eyebrows", "Positive vocal tone"]
    })
    seg2_notes = st.text_area("Clinician Notes – Segment 2", height=100)
else:
    seg2_notes = ""

# Segment 3
st.header("🎥 Segment 3 – Neutral Clip")
st.video("static/CREMA_sample_3.mp4")
if st.button("Analyze Segment 3"):
    with st.spinner("Analyzing Segment 3..."):
        time.sleep(2)
    st.success("Analysis Complete!")
    st.json({
        "Detected Emotion": "Neutral",
        "Confidence": 0.69,
        "Observations": ["Still gaze", "Flat affect", "Emotionally stable"]
    })
    seg3_notes = st.text_area("Clinician Notes – Segment 3", height=100)
else:
    seg3_notes = ""

# Final Combined Summary
st.markdown("---")
st.header("📋 Combined Clinician Summary")
final_summary = f"""
Segment 1 Notes:
{seg1_notes}

Segment 2 Notes:
{seg2_notes}

Segment 3 Notes:
{seg3_notes}
"""

st.text_area("Full Summary (Editable):", final_summary, height=300)
st.download_button("📥 Download Combined Summary", data=final_summary, file_name="vida_segmented_summary.txt")
