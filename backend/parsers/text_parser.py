# backend/parsers/text_parser.py

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_API_TOKEN")
client = InferenceClient(model="google/flan-t5-base", token=HF_TOKEN)

def extract_job_info(raw_description: str) -> str:
    prompt = f"""
You are an intelligent HR assistant. Given the following job description, return a structured summary in strict JSON format with the following fields:
- title
- company
- location
- responsibilities
- skills
- required_experience
- contract_type
- languages
- salary

Example of output (JSON format):
{{
    "title": "Python Developer",
    "company": "TechCorp",
    "location": "Paris",
    "responsibilities": "Develop backend systems.",
    "skills": ["Python", "Django", "REST API"],
    "required_experience": "2+ years",
    "contract_type": "Full-time",
    "languages": ["English", "French"],
    "salary": "€50,000"
}}

Now, here is a job offer:
{raw_description}

Please respond with **only** the JSON structure. Do **not** include any other text, explanations, or remarks. The response must **not** contain anything outside the JSON format.
"""

    try:
        # Max token limit for flan-t5-base is generally fine under 250 tokens.
        result = client.text_generation(prompt, max_new_tokens=200, temperature=0.3)
        return result
    except Exception as e:
        print("Error calling Hugging Face inference:", e)
        return {"error": "Could not process job description"}
