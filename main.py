from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from pydantic import BaseModel
from datetime import datetime
import csv
import os

app = FastAPI(title="Forge City Global Backend")

# =============================
# Templates
# =============================
templates = Jinja2Templates(directory="templates")

# =============================
# CSV Config
# =============================
CSV_FILE = "karya_log.csv"

# =============================
# Data Model
# =============================
class KaryaLog(BaseModel):
    name: str
    task: str
    status: str = "in-progress"

# =============================
# Ensure CSV exists
# =============================
def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp",
                "name",
                "task",
                "status"
            ])

init_csv()

# =============================
# Routes
# =============================

@app.get("/srishtisteam", response_class=HTMLResponse)
async def srishti_team(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

# =============================
# API: Log Karya
# =============================
@app.post("/karya/log")
def log_karya(karya: KaryaLog):
    timestamp = datetime.utcnow().isoformat()

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            timestamp,
            karya.name,
            karya.task,
            karya.status
        ])

    return {
        "message": "Karya logged successfully",
        "timestamp": timestamp
    }

@app.get("/karya/all")
def get_all_karyas():
    rows = []
    # print(os.path.exists(CSV_FILE))
    if not os.path.exists(CSV_FILE):
        return rows

    with open("karya_log.csv", mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row:  # skip empty rows
                rows.append(row)
    # print(rows)
    return rows

TODAY_KARYA_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "today_karya.csv"
)

@app.get("/karya/todayskarya")
def get_all_todayskaryas():
    rows = []

    # print("Today CSV exists:", os.path.exists(TODAY_KARYA_FILE))

    if not os.path.exists(TODAY_KARYA_FILE):
        return rows

    with open(TODAY_KARYA_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row:
                rows.append(row)

    # print("Today's Karyas:", rows)
    return rows
