import streamlit as st
import os
import pandas as pd
import tempfile
from parser.extractor import extract_text, extract_info

st.set_page_config(page_title="Smart Resume Parser", layout="centered")
st.title("📄 Smart Resume Parser")

st.markdown("""
Upload a resume in **PDF** or **DOCX** format.  
The app will extract:
- Name
- Email
- Phone Number
- Skills
- Summary snippet
""")

uploaded_file = st.file_uploader("📤 Upload your resume", type=["pdf", "docx"])

if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1].lower()
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_ext}") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Extract and parse resume
    text = extract_text(tmp_path, file_ext)
    info = extract_info(text)
    df = pd.DataFrame([info])

    # Display results
    st.success("✅ Resume Parsed Successfully!")
    st.write("### 🧾 Extracted Data:")
    st.json(info)

    # Save to CSV
    output_dir = "data/outputs"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, uploaded_file.name.split('.')[0] + ".csv")
    df.to_csv(output_file, index=False)

    # Download button
    with open(output_file, "rb") as f:
        st.download_button(
            label="⬇️ Download CSV",
            data=f,
            file_name=os.path.basename(output_file),
            mime="text/csv"
        )
