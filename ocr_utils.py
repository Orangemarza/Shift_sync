import pytesseract
import cv2
import re

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    cv2.imshow("Otsu", thresh)
    return pytesseract.image_to_string(gray)


def extract_schedule(text, name):
    lines = text.splitlines()
    schedule = {}
    for line in lines:
        if name.upper() in line:
            times = re.findall(r'\d{1,2}\.\d{2}-\d{1,2}\.\d{2}', line)
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            for i, time in enumerate(times):
                if i < len(days):
                    schedule[days[i]] = time
    return schedule
