# Timetable to Google Calendar

Convert a weekly work schedule image into Google Calendar events for a selected person.

## 🔧 Setup

1. Clone or download this project.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Get your Google Calendar API `credentials.json` from [Google Developers Console](https://developers.google.com/calendar/quickstart/python).
4. Place your timetable image as `timetable.jpeg`.
5. Run:
   ```
   python main.py
   ```

## 🧠 What it Does
- OCR reads your roster
- Parses hours for selected name
- Converts into Calendar events
