def format_timetable(timetable):
    formatted_events = []

    for event in timetable:
        start_dt = f"{event['date']}T{event['start_time']}:00"
        end_dt = f"{event['date']}T{event['end_time']}:00"

        formatted_events.append({
            'summary': event['subject'],
            'start_time': start_dt,
            'end_time': end_dt
        })

    return formatted_events