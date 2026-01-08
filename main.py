from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI(
    title="Forge City Global Backend",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")


@app.get("/srishtisteam", response_class=HTMLResponse)
async def srishti_team(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
