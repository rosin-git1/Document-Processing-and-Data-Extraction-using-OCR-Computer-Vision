import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_invoice_fields(text):
    data = {}

    # -------- Regex (reliable for numbers) --------
    invoice_no = re.search(r'\d{3,5}', text)
    if invoice_no:
        data["Invoice Number"] = invoice_no.group()

    numbers = re.findall(r'\d{5,8}', text)
    if numbers:
        data["Probable Amount"] = max([int(n) for n in numbers])

    # -------- NLP (good for names) --------
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "ORG":
            data["Organization"] = ent.text

    return data
