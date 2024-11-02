from fastapi import FastAPI

# Start Python App #

# Create Python virtual environment
# python3 -m venv venv
# source venv/bin/activate
# .\venv\Scripts\activate

# Install dependencies 
# pip3 install -r requirements.txt

# run app with "fastapi dev app.py"

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
