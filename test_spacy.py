import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Tharun Lokesh is a Python developer with resume parsing experience.")
for ent in doc.ents:
    print(ent.text, ent.label_)
