import sys
import os
from map import Map
from data import Crop
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
import uvicorn


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    map = Map() 
    with open(os.path.join("static", "index.html"), "r") as file:
        return HTMLResponse(content=file.read())

@app.get("/map", response_class=HTMLResponse)
async def read_map(crop: str, year: str):
    map = Map()
    Crop(crop, year)
    map.heat_map(crop)
    with open(os.path.join("static", "index.html"), "r") as file:
        return HTMLResponse(content=file.read())