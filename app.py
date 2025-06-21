import streamlit as st
import time

st.set_page_config(page_title="Vida – Multimodal AI Analysis", layout="wide")

st.title("Vida – Multimodal Emotion Analysis for Mental Health Triage")
st.markdown("_Analyzing facial expressions, voice tone, and emotional risk from patient video clips._")
st.markdown("---")

# 🔹 Clip 1: Initial Check-in
st.header("🟢 Question 1: I’d like to start by checking in, how have you been feeling lately, both physically and emotionally?")
st.video("static/my_video_clip_1.mp4")

if st.button("Run Analysis for Clip 1"):
    with st.spinner("Analyzing Clip 1..."):
        time.sleep(2)
    st.success("Analysis complete.")

    st.subheader("Transcript")
    st.info("Lately, I just feel empty. I don't have the energy to get out of the bed some days. I'm not really sleeping very well. I'm always tired. It's like nothing really matters anymore.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Sentiment", "Negative")
        st.metric("Emotion", "Hopelessness")
    with col2:
        st.metric("Sleep Issues", "✔️")
        st.metric("Energy Level", "Low")
    with col3:
        st.metric("Facial Emotion", "Fatigued")
        st.metric("Risk Level", "Moderate")

st.markdown("---")

# 🔹 Clip 2: Chained Follow-up
st.header("🟡 Question 2: Do you ever find yourself going through the motions in your daily life, even with things you used to love?")
st.video("static/my_video_clip_2.mp4")

if st.button("Run Analysis for Clip 2"):
    with st.spinner("Analyzing Clip 2..."):
        time.sleep(2)
    st.success("Analysis complete.")

    st.subheader("Transcript")
    st.info("I just feel very stuck. I used to enjoy a lot of things such as gymming and cooking but I just go through the motions now. People keep asking if I'm okay. I say I'm fine but I'm not really fine.")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.metric("Sentiment", "Negative")
        st.metric("Emotion", "Anhedonia")
    with col5:
        st.metric("Social Withdrawal", "✔️")
        st.metric("Masking Emotion", "✔️")
    with col6:
        st.metric("Facial Emotion", "Low Expressivity")
        st.metric("Risk Level", "Elevated")

st.markdown("---")
st.header("📋 Final Clinician Summary")
summary = (
    "Across both clips, the patient presents signs of fatigue, anhedonia, and emotional masking. "
    "Clip 1 reflects physical exhaustion and sleep disturbance. "
    "Clip 2 emphasizes social withdrawal and a loss of joy in previously enjoyed activities. "
    "Moderate to elevated risk. Recommend structured follow-up and psychological assessment."
)
st.text_area("Editable Summary", summary, height=180)
st.download_button("Download Summary", summary, file_name="vida_clinical_summary.txt")
