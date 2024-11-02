import sys
import os
from PyQt5 import QtWidgets
from map import Map
from data import Crop
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    map = Map()
    choice = ''
    Crop(choice)
    while(choice is False):
        map.heat_map(choice)
    
    with open(os.path.join("static", "map.html"), "r") as file:
        return HTMLResponse(content=file.read())


# def main():
#     

# if __name__ == "__main__":
#     main()
