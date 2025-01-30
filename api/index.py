from fastapi import FastAPI, Query
import json

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