# ☀️ Sun Calendar

A simple ICS calendar that shows daily sunrise & sunset times in **San Francisco**.  

## 🗓️ Usage

Subscribe to this link ("by URL") in your calendar app: 

```
webcal://www.averychan.site/sun-calendar/sun.ics
```

Sunrise and Sunset times for the current week should appear in your calendar like this:

<img src="https://github.com/user-attachments/assets/b74367bc-9a3c-44dd-b00d-57a810d2285f" style="height: 50vh" alt="example calendar view">

<details>
    <summary>Google Calendar instructions</summary>
    <div>
        <img src="https://github.com/user-attachments/assets/508cacad-239e-49fa-8e87-ab9bdcb27abb" style="height: 50vh" />
        <img src="https://github.com/user-attachments/assets/e9da2a43-cf50-4b93-9950-995eed520b97" style="height: 50vh" />
    </div>
</details>


## 💻 Dev Usage + Notes

- To generate the isc file, run `create_calendar_local.py`
    - Uses this awesome free sun API: https://sunrise-sunset.org/api
    - Uses isc python library https://icspy.readthedocs.io/en/stable/
- The isc file is exposed by hosting on GH pages
- If you want to use a different location, just change the lat and long coords in `create_calendar_local.py`
    - (if you want it to auto-update, you'll have to fork this and host it on your own github pages)

