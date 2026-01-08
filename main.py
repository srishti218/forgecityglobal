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
