import requests
import json
from typing import cast
from ics import Calendar 

#example url
ICAL_URL = "https://umamherst.instructure.com/feeds/calendars/user_aWBDrDP7GhNr2laHFoa8cY7oIeKZ7uZm7GaClJVO.ics"

def fetch_calendar_events():
    response = requests.get(ICAL_URL)
    if response.status_code != 200:
        print("failed to fetch calendar")
        return []
    
    calendar = cast(Calendar, Calendar(response.text))
    events = []
    
    for event in calendar.events:
        event_data = {
            "title": event.name,
            "due_date": event.begin.format("YYYY-MM-DD")
        }
        events.append(event_data)
    return events

if __name__ == "__main__":
    assignments = fetch_calendar_events()
    print(json.dumps(assignments, indent=2, ensure_ascii=False))