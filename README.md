# Document Processing and Data Extraction using OCR Computer Vision

## Project Overview
This project builds an automated system to process corporate documents such as invoices and contracts using Computer Vision, OCR, and NLP techniques. The system extracts meaningful structured information from unstructured scanned documents.

## Features
- Image preprocessing using OpenCV
- OCR text extraction using Tesseract OCR
- Text normalization and field extraction using Regex and spaCy NLP
- Evaluation using Accuracy, Precision, Recall, F1-score, Confusion Matrix
- Streamlit frontend for real-time document upload and extraction

## Folder Structure
data/
  invoices/
  contracts/

preprocessing.py  
ocr_engine.py  
classifier.py  
evaluation.py  
app.py  

## How to Run

### Step 1
Activate virtual environment (Python 3.11)

### Step 2
Install requirements:
pip install -r requirements.txt

### Step 3
Run the app:
streamlit run app.py

## Output
Upload an invoice image → View OCR text → View extracted fields.

## Technologies Used
Python, OpenCV, Tesseract OCR, spaCy NLP, Scikit-learn, Streamlit
