# backend/main.py

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from .parsers.text_parser import extract_job_info

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.post("/parse-job")
def parse_job(data: dict = Body(...)):
    description = data.get("description", "")
    result = extract_job_info(description)
    return result

# uvicorn backend.main:app --reload
