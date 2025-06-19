from pathlib import Path

# Revised app.py with distinct emotion labels and clinician interpretations
revised_app_code = """
import streamlit as st
import time

st.set_page_config(page_title="VIDA – Per-Segment Emotion Analysis", layout="wide")
st.title("🎬 VIDA – Analyze Emotional Segments Separately")
st.markdown("_Play and analyze each clip individually for high-resolution emotional insight._")
st.markdown("---")

# Segment 1
st.header("🎥 Segment 1 – Initial Response")
st.video("static/CREMA_sample_1.mp4")
if st.button("Analyze Segment 1"):
    with st.spinner("Analyzing Segment 1..."):
        time.sleep(2)
    st.success("Analysis Complete!")
    st.json({
        "Detected Emotion": "Subdued or Thoughtful",
        "Confidence": 0.72,
        "Observations": [
            "Low expressiveness",
            "Inward-focused affect",
            "Subtle hesitation"
        ]
    })
    seg1_notes = st.text_area("Clinician Notes – Segment 1", 
        "Patient appears reflective and internally focused. May be processing thoughts before responding.")
else:
    seg1_notes = ""

# Segment 2
st.header("🎥 Segment 2 – Emotional Guarding")
st.video("static/CREMA_sample_2.mp4")
if st.button("Analyze Segment 2"):
    with st.spinner("Analyzing Segment 2..."):
        time.sleep(2)
    st.success("Analysis Complete!")
    st.json({
        "Detected Emotion": "Controlled or Guarded",
        "Confidence": 0.72,
        "Observations": [
            "Intentional affect regulation",
            "Minimal spontaneous expression",
            "Patient may be emotionally present but cautious"
        ]
    })
    seg2_notes = st.text_area("Clinician Notes – Segment 2", 
        "Patient displays controlled demeanor, potentially signaling caution or guarded emotional sharing.")
else:
    seg2_notes = ""

# Segment 3
st.header("🎥 Segment 3 – Conversational Neutrality")
st.video("static/CREMA_sample_3.mp4")
if st.button("Analyze Segment 3"):
    with st.spinner("Analyzing Segment 3..."):
        time.sleep(2)
    st.success("Analysis Complete!")
    st.json({
        "Detected Emotion": "Calm Neutrality",
        "Confidence": 0.72,
        "Observations": [
            "Balanced emotional tone",
            "Low but present engagement",
            "Relaxed and conversational state"
        ]
    })
    seg3_notes = st.text_area("Clinician Notes – Segment 3", 
        "Patient demonstrates calm, neutral tone. No signs of distress; likely in a steady state of engagement.")
else:
    seg3_notes = ""

# Final Combined Summary
st.markdown("---")
st.header("📋 Combined Clinician Summary")
final_summary = f\"\"\"
Segment 1: Subdued or Thoughtful
{seg1_notes}

Segment 2: Controlled or Guarded
{seg2_notes}

Segment 3: Calm Neutrality
{seg3_notes}
\"\"\"

st.text_area("Full Summary (Editable):", final_summary, height=300)
st.download_button("📥 Download Combined Summary", data=final_summary, file_name="vida_segmented_summary.txt")
"""

# Save to file
revised_app_path = Path("/mnt/data/app_segment_refined.py")
revised_app_path.write_text(revised_app_code)
revised_app_path.name
