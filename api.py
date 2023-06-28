from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from routeData import obtainRouteData
from fastapi.templating import Jinja2Templates

class RequestModel(BaseModel):
    origin: str
    destination: str
    unit: str = "k"

Api = FastAPI()
templates = Jinja2Templates(directory="UI\\templates")
Api.mount("/UI", StaticFiles(directory="UI"), name="UI")

@Api.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@Api.post("/routeData")
def route(model: RequestModel):
    data = obtainRouteData(model.origin, model.destination, model.unit)
    if data != False:
        return data
    else:
        raise HTTPException(500)