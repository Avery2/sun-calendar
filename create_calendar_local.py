import requests
from ics import Calendar, Event
from datetime import datetime, timezone, timedelta
import pytz

def get_sun_events(current_date):
    # API call for sunrise and sunset times in San Francisco, CA
    sun_times_url = f"https://api.sunrise-sunset.org/json?lat=37.7749000&lng=-122.4194000&date={current_date}&formatted=0"
    print(f"sun_times_url: {sun_times_url}")

    response = requests.get(sun_times_url)

    response_json = None

    if response.status_code == 200:
        data = response.json()  # Assuming the response is in JSON format
        print(f"response json: {data}")
        response_json = data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

    # Convert the strings to datetime objects
    datetime_objects = {
        key: datetime.fromisoformat(value)  # full UTC timestamp, e.g. 2026-10-26T01:19:12+00:00
        for key, value in response_json['results'].items()
        if key != 'day_length'  # 'day_length' is a number of seconds
    }

    calendar_time_format = "%Y-%m-%d %H:%M:%S"

    events = []

    # Create an event for today's sunrise
    e = Event()
    e.name = "🌅 Sunrise"
    e.begin = datetime_objects['sunrise'].strftime(calendar_time_format)
    e.duration = {'seconds': 15*60}
    events.append(e)

    # Create an event for today's sunset
    e = Event()
    e.name = "🌇 Sunset"
    e.begin = datetime_objects['sunset'].strftime(calendar_time_format)
    e.duration = {'seconds': 15*60}
    events.append(e)

    return events

c = Calendar()

current_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')

# get dates for today and next 6 days
dates = [current_date]
for i in range(1, 7):
    dates.append((datetime.now(timezone.utc) + timedelta(days=i)).strftime('%Y-%m-%d'))

for date in dates:
    for event in get_sun_events(date):
        c.events.add(event)

with open('sun.ics', 'w') as f:
    f.writelines(c.serialize_iter())
