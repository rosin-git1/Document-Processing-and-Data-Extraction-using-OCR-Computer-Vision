import pytesseract
from preprocessing import preprocess_image

def extract_text(image_path):
    processed_img = preprocess_image(image_path)
    text = pytesseract.image_to_string(processed_img)
    return text
