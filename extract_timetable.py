import cv2
import pytesseract

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    text = pytesseract.image_to_string(thresh, config="--psm 6")  # OCR text extraction
    return text

def parse_timetable(text):
    lines = text.strip().split("\n")
    timetable = []

    for line in lines:
        parts = line.split()
        if len(parts) >= 4:
            subject = parts[0]
            date = parts[1]
            start_time = parts[2]
            end_time = parts[3]
            timetable.append({"subject": subject, "date": date, "start_time": start_time, "end_time": end_time})

    return timetable

# Example usage
image_path = "timetable.jpg"
text = extract_text_from_image(image_path)
timetable = parse_timetable(text)
print(timetable)