from ocr_utils import extract_text_from_image, extract_schedule
from calendar_utils import get_calendar_service, convert_to_datetime_range, add_event
from datetime import datetime

def main():
    name = input("Enter the name (e.g., LUU, M): ").strip()
    image_path = "timetable.jpg"
    text = extract_text_from_image(image_path)
    print("OCR text printed:\n", text)
    schedule = extract_schedule(text, name)

    if not schedule:
        print("No schedule found for this name.")
        return

    print(f"Schedule for {name}:")
    for day, hours in schedule.items():
        print(f"{day}: {hours}")

    service = get_calendar_service()
    base_date = datetime.strptime("2025-04-07", "%Y-%m-%d")

    for day, time_str in schedule.items():
        start, end = convert_to_datetime_range(day, time_str, base_date)
        add_event(service, start, end, summary=f"{name} - {day} Shift")
    print("✅ Calendar events added.")

if __name__ == "__main__":
    main()
