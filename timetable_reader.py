import pandas as pd
import cv2
import pytesseract
import os

def read_timetable(file_path):
    """
    Reads a timetable from a CSV file or an image (JPG/PNG) using OCR.
    :param file_path: Path to the timetable file.
    :return: Extracted text (if image) or DataFrame (if CSV).
    """
    if not os.path.exists(file_path):
        print("Error: File not found!")
        return None

    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext == ".csv":
        return read_csv_timetable(file_path)
    elif file_ext in [".jpg", ".png", ".jpeg"]:
        return read_image_timetable(file_path)
    else:
        print("Unsupported file type! Use CSV or an image format.")
        return None

def read_csv_timetable(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None

def read_image_timetable(image_path):
    try:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        extracted_text = pytesseract.image_to_string(gray)
        return extracted_text
    except Exception as e:
        print(f"Error reading image: {e}")
        return None