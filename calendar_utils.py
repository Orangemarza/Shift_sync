from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, timedelta

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'credentials.json'

def get_calendar_service():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('calendar', 'v3', credentials=creds)

def convert_to_datetime_range(day_str, time_str, base_date):
    start_str, end_str = time_str.split('-')
    start_time = datetime.strptime(start_str.replace('.', ':'), "%H:%M")
    end_time = datetime.strptime(end_str.replace('.', ':'), "%H:%M")
    day_index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].index(day_str)
    work_day = base_date + timedelta(days=day_index)
    start = work_day.replace(hour=start_time.hour, minute=start_time.minute)
    end = work_day.replace(hour=end_time.hour, minute=end_time.minute)
    return start, end

def add_event(service, start, end, summary="Work Shift"):
    event = {
        'summary': summary,
        'start': {'dateTime': start.isoformat(), 'timeZone': 'Australia/Sydney'},
        'end': {'dateTime': end.isoformat(), 'timeZone': 'Australia/Sydney'},
    }
    service.events().insert(calendarId='primary', body=event).execute()
