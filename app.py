from fastapi import FastAPI

# Start Python App #

# Create Python virtual environment
# python3 -m venv venv
# source venv/bin/activate

# Install dependencies 
# pip3 install -r requirements.txt
# May have to restart venv after installing fastapi

# run app with "fastapi dev app.py"

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}