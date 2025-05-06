from calendar_auth import get_calendar_service

def add_event_to_calendar(event):
    service = get_calendar_service()

    event_body = {
        'summary': event['summary'],
        'start': {'dateTime': event['start_time'], 'timeZone': 'Australia/Melbourne'},
        'end': {'dateTime': event['end_time'], 'timeZone': 'Australia/Melbourne'},
    }

    event_result = service.events().insert(calendarId='primary', body=event_body).execute()
    print(f"Event created: {event_result['summary']}")

def process_timetable(events):
    for event in events:
        add_event_to_calendar(event)