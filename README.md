# 📄 Smart Resume Parser

A Streamlit-based Python application that extracts structured information from resumes (PDF/DOCX) using **Natural Language Processing** (spaCy), **regex**, and **file parsing**.

---

## 🚀 Features

- Upload resumes in `.pdf` or `.docx` format
- Extracts:
  - ✅ Name
  - ✅ Email
  - ✅ Phone Number
  - ✅ Skills
  - ✅ Summary snippet
- Exports results to `.csv`
- Streamlit-powered UI

---

## 🛠 Tech Stack

- **Python 3.11**
- **spaCy** — for NLP and entity extraction
- **PyMuPDF** — to extract text from PDFs
- **python-docx** — to extract text from Word files
- **pandas** — for data handling and CSV export
- **Streamlit** — for frontend web interface
- **Regex** — for email & phone pattern matching

---

## 📂 Project Structure

```
smart_resume_parser/
├── app.py
├── requirements.txt
├── README.md
├── Smart_Resume_Parser_Project_Report.docx
├── parser/
│   └── extractor.py
├── data/
│   ├── sample_resumes/
│   │   ├── resume_1.docx ...
│   └── outputs/
│       ├── resume_1.csv ...
```

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/tharunlokeshu/smart-resume-parser.git
cd smart-resume-parser
python -m venv venv
venv\Scripts\activate         # On Windows
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
```

---

## 📁 Sample Resumes

Test files are located in `data/sample_resumes/`.

---

## 📤 Output Format

Parsed resume data will be saved as `.csv` inside `data/outputs/`.

---

## 📝 Report

📄 `Smart_Resume_Parser_Project_Report.docx` is included in the repository.

---

## 🙌 Acknowledgements

This project was created as part of an internship phase to demonstrate practical NLP, file handling, and frontend/backend integration using Python.
