from fastapi import FastAPI, Query
import json

from fastapi.middleware.cors import CORSMiddleware


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET"],  # Only allow GET requests
    allow_headers=["*"],  # Allows all headers
)




app = FastAPI()

# Load data from JSON file
def load_data():
    with open("q-vercel-python.json", "r") as file:
        return json.load(file)

data = load_data()

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    result = {n: next((item['marks'] for item in data if item['name'] == n), None) for n in name}
    return result