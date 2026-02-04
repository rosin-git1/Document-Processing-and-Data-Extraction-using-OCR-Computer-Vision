import cv2
import numpy as np

def preprocess_image(image_path):
    # Read image
    img = cv2.imread(image_path)

    # Resize for consistency
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Remove noise
    denoised = cv2.medianBlur(gray, 3)

    # Thresholding (binarization)
    _, thresh = cv2.threshold(denoised, 150, 255, cv2.THRESH_BINARY)

    return thresh
