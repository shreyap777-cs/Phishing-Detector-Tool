import streamlit as st
from main import analyze_email


# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Phishing Detector",
    page_icon="🔐",
    layout="centered"
)

# -------------------------------
# Title & Description
# -------------------------------
st.title("🔐 AI-Powered Phishing Detection System")

st.markdown("""
This tool analyzes email content using:
- 🤖 AI-based phishing detection  
- 🌐 URL security analysis  
- ⚠️ Risk scoring system  
""")

st.markdown("---")

# -------------------------------
# User Input
# -------------------------------
user_input = st.text_area(
    "📩 Enter Email Content:",
    height=200,
    placeholder="Paste suspicious email text here..."
)

# -------------------------------
# Analyze Button
# -------------------------------
if st.button("🔍 Analyze Email"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter some email content.")
    else:
        result = analyze_email(user_input)

        st.markdown("### 🔍 Analysis Result")
        
        # Display result nicely
        st.code(result)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Python, Machine Learning, and Cybersecurity concepts")