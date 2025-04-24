# backend/parsers/text_parser.py

import openai
import os 
from dotenv import load_dotenv
load_dotenv()

# Load your API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_job_info(raw_description: str) -> dict:
    prompt = f"""
Tu es un assistant RH intelligent.

Voici une offre d'emploi à analyser :
---
{raw_description}
---

Donne-moi un résumé structuré sous forme JSON avec les champs suivants :
- titre
- entreprise
- localisation
- missions
- compétences
- expérience_requise
- type_contrat
- langues
- salaire

Réponds uniquement avec du JSON, pas de texte autour.
"""

    try:
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # Specify the GPT model
            prompt=prompt,
            max_tokens=500,  # Adjust depending on job description size
            temperature=0.3,
        )
        # Extract and return the parsed JSON from the response
        result = response["choices"][0]["text"]
        return result
    except Exception as e:
        print("Error parsing job description:", e)
        return {"error": "Could not parse the job description"}
