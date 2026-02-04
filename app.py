import streamlit as st
from ocr_engine import extract_text
from classifier import extract_invoice_fields
from PIL import Image
import tempfile

st.title("Document Processing and Data Extraction using OCR Computer Vision")

uploaded_file = st.file_uploader("Upload an Invoice Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Show image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Document", width=600)

    # Save temp image
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        image.save(tmp.name)
        temp_path = tmp.name

    # OCR
    text = extract_text(temp_path)
    st.subheader("Extracted OCR Text")
    st.text(text)

    # Field Extraction
    data = extract_invoice_fields(text)
    st.subheader("Extracted Fields")
    st.json(data)
