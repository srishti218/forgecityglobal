🚀 Forge City Global Backend
Srishti’s Team – Today’s Work Dashboard

An internal FastAPI-powered work-tracking system for Srishti’s Team.
It separates today’s planning, work logging, and completed/history view using a clean tab-based UI.

✨ Key Features

🧭 Today’s Karya (table view from today_karya.csv)

✍️ Log Karya (name, task, status)

📜 All Karyas Done (history from karya_log.csv)

🗂 CSV-based persistence (no database required)

🖥 Clean tab-based UI

👤 External avatars for team members

⚡ FastAPI backend with auto docs

🏗 Project Structure
srishti-team/
│
├── main.py                  # FastAPI backend
├── karya_log.csv            # All logged karyas (auto-created)
├── today_karya.csv          # Today's planned karyas
├── requirements.txt
│
├── templates/
│   └── index.html           # Dashboard UI
│
└── static/                  # (optional) CSS / JS / images

⚙️ Requirements

Python 3.9+

pip

📦 Installation
git clone <your-repo-url>
cd srishti-team
pip install -r requirements.txt

▶️ Run the Server
uvicorn main:app --reload


Open in browser:

http://127.0.0.1:8000/srishtisteam

🧭 Dashboard Tabs
1️⃣ Today’s Karya

Data source: today_karya.csv

Display: Table

Purpose: Daily planning & focus

2️⃣ Log & All Karyas Done

Log new work

View all previously logged karyas

Stored in karya_log.csv

🔌 API Endpoints
📋 Get Today’s Karyas

GET /karya/todayskarya

[
  {
    "timestamp": "2026-01-08T09:00:00Z",
    "name": "Vision-Team",
    "task": "Define the core problem",
    "status": "in-progress"
  }
]

➕ Log Karya

POST /karya/log

{
  "name": "Amit",
  "task": "API Integration",
  "status": "completed"
}


Response:

{
  "message": "Karya logged successfully",
  "timestamp": "2026-01-08T10:15:30Z"
}

📜 Get All Karyas Done

GET /karya/all

Returns all historical karyas from karya_log.csv.

🗃 CSV Formats
today_karya.csv
timestamp,name,task,status

karya_log.csv
timestamp,name,task,status


Files are UTF-8 encoded.
karya_log.csv is auto-created if missing.

🧠 Status Values

Allowed:

in-progress

completed

pending

🔐 Security Notes

Designed for internal use

No authentication yet

Recommended behind VPN or private network

🚀 Future Enhancements

Auto-move completed tasks → Done

Date-based filtering

Role-based access

Database migration

CSV / PDF export

Analytics dashboard

👤 Maintained By

Srishti’s Team
Forge City Global Backend

📜 License

Internal use only