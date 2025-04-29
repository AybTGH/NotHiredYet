# backend/parsers/cv_optimizer.py

from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(
    model="google/flan-t5-base",
    token=os.getenv("HF_API_TOKEN")
)

def optimize_latex_cv(cv_latex: str, job_offer: dict) -> str:
    prompt = f"""
You are a professional resume optimizer.

Here is a LaTeX resume document:
{cv_latex}

Here is a job offer the candidate wants to apply for:
{job_offer}

Update the LaTeX code to:
- Add missing keywords and relevant experience
- Emphasize matching skills
- Keep the LaTeX formatting valid
- Do NOT add explanations or comments, return ONLY updated LaTeX code
"""

    try:
        response = client.text_generation(
            prompt=prompt,
            max_new_tokens=200,  # Adjusted to stay within model limit
            temperature=0.4
        )
        return response
    except Exception as e:
        print("Error optimizing LaTeX CV:", e)
        return ""
