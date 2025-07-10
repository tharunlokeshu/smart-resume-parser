import fitz  # PyMuPDF
import docx
import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_text(file_path, ext):
    """
    Extract text from PDF or DOCX.
    """
    text = ""
    if ext == "pdf":
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()
    elif ext == "docx":
        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format")
    return text

def extract_info(text):
    """
    Extract email, phone, skills, and short summary using regex + NLP.
    """
    email = re.findall(r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+", text)
    phone = re.findall(r"\+?\d[\d\s\-]{8,}\d", text)

    # Simple skill section extraction
    skills_section = re.findall(r"(skills|technologies)[:\-]?\s*(.*)", text, re.IGNORECASE)

    # Use spaCy for named entity recognition (you can expand this later)
    doc = nlp(text)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

    return {
        "name": names[0] if names else "",
        "email": email[0] if email else "",
        "phone": phone[0] if phone else "",
        "skills": skills_section[0][1] if skills_section else "",
        "summary": text[:300] + "..."
    }

