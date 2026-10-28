import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="AI Coding Tutor", page_icon="🐍", layout="wide")
DATA = json.loads(Path(__file__).with_name("programs.json").read_text(encoding="utf-8"))

st.title("🐍 AI Coding Tutor")
st.caption("A beginner-friendly Python code explainer • Capstone 6")
st.info("Learning note: the built-in explanations are prepared examples, not a live AI model. Use the Prompt Builder to ask ChatGPT, Gemini, or Claude for a second explanation, then verify every claim by running the code.")

titles = [item["title"] for item in DATA]
selected = st.sidebar.selectbox("Choose a Python example", titles)
item = next(p for p in DATA if p["title"] == selected)

tab1, tab2, tab3, tab4 = st.tabs(["📘 Learn", "🧪 Practice", "🧠 Prompt Builder", "✅ Verification"])
with tab1:
    left, right = st.columns([1, 1])
    with left:
        st.subheader(item["title"])
        st.code(item["code"], language="python")
        st.markdown("**Expected output**")
        st.code(item["output"], language="text")
    with right:
        st.subheader("Line-by-line explanation")
        for i, explanation in enumerate(item["explanation"], 1):
            st.markdown(f"{i}. {explanation}")
        st.caption("Topic: " + item["topic"])
with tab2:
    st.subheader("Try it yourself")
    st.write(item["practice"])
    response = st.text_area("Write your answer or modified code here", height=140, key="practice")
    if st.button("Show learning reminder"):
        st.success("Run your modified code in Google Colab or Python. Compare the actual output with what you expected.")
with tab3:
    st.subheader("Prompt Builder")
    prompt = f"""Act as a patient Python tutor for a beginner. Explain this program accurately.
1. Explain every line in simple language.
2. Trace the variable values step by step.
3. State the exact output and why.
4. Identify likely beginner mistakes and any safety or file-handling concerns.
5. Give one similar practice problem without immediately solving it.
If uncertain, say so. Do not invent Python syntax.

Code:
{item['code']}"""
    st.text_area("Copy this prompt into ChatGPT, Gemini, or Claude", prompt, height=260)
    st.caption("This app does not send code to an AI service automatically. Paste the prompt into the tool you choose.")
with tab4:
    st.subheader("Verification checklist")
    st.write("Use this checklist for every example before submitting.")
    checks = [
        "I ran the code in Google Colab or a local Python interpreter.",
        "The actual output matches the expected output.",
        "I checked each explanation against Python's behaviour.",
        "I recorded any incorrect or unclear AI claim.",
        "I rewrote the explanation in my own words."
    ]
    for c in checks:
        st.checkbox(c, key=selected + c)
    st.warning("File example note: writing with mode 'w' overwrites an existing file named sample.txt. Use a test folder and avoid important files.")
st.sidebar.markdown("---")
st.sidebar.markdown("**Capstone deliverables**")
st.sidebar.markdown("10 examples • prompts • quiz • verification log • report • presentation")
