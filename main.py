import os
from timetable_reader import read_timetable
from format_timetable import process_timetable
from add_to_calendar import add_events_to_calendar

def main():
    """
    Main function to process a timetable and add it to Google Calendar.
    """
    # Prompt user to enter a file path
    file_path = input("Enter the path of your timetable (CSV or image): ").strip()

    # Validate file existence
    if not os.path.exists(file_path):
        print("Error: File not found!")
        return

    # Step 1: Read the timetable (CSV or Image)
    raw_timetable = read_timetable(file_path)

    if raw_timetable is None:
        print("Error: Could not read timetable.")
        return

    # Step 2: Process and format timetable
    formatted_timetable = process_timetable(raw_timetable)

    if formatted_timetable is None or len(formatted_timetable) == 0:
        print("Error: No valid events found in the timetable.")
        return

    # Step 3: Add events to Google Calendar
    success = add_events_to_calendar(formatted_timetable)

    if success:
        print("✅ Timetable successfully added to Google Calendar!")
    else:
        print("❌ Failed to add events to Google Calendar.")

if __name__ == "__main__":
    main()