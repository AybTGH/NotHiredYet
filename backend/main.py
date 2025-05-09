from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

# Job parsing
from .parsers.text_parser import extract_job_info
from .parsers.url_parser import extract_text_from_url

# CV optimization
from .ai.cv_optimizer import optimize_latex_cv
from .utils.latex_handler import (
    read_latex_file,
    write_latex_file,
    compile_latex_to_pdf
)
from .mail.status_classifier import classify_email
from .mail.gmail_reader import fetch_latest_emails

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.get("/")
def read_root():
    return {"message": "Hello, I'm your AI agent that will help you manage applications for your job."}

# ---------------------------
# 📌 Endpoint 1: Parse Job Offer
# ---------------------------
@app.post("/parse-job")
def parse_job(data: dict = Body(...)):
    url = data.get("url")
    description = data.get("description", "")

    if url:
        print(f"[INFO] Scraping job offer from URL: {url}")
        description = extract_text_from_url(url)

    if not description.strip():
        return {"error": "No job description provided or extracted."}

    job_data = extract_job_info(description)
    return {"job_offer": job_data}


# ---------------------------
# 📌 Endpoint 2: Generate Optimized CV
# ---------------------------
@app.post("/generate-cv")
def generate_cv(job_data: dict = Body(...)):
    job_offer = job_data.get("job_offer")
    if not job_offer:
        return {"error": "Missing 'job_offer' field in request body."}

    # Load base LaTeX CV
    base_cv_path = "./data/my_cv.tex"
    try:
        original_cv = read_latex_file(base_cv_path)
    except FileNotFoundError:
        return {"error": f"Base LaTeX CV not found at {base_cv_path}"}

    # Ask AI to optimize CV
    updated_latex = optimize_latex_cv(original_cv, job_offer)
    if not updated_latex.strip():
        return {"error": "Failed to generate updated LaTeX CV."}

    # Save and compile
    tex_path = write_latex_file(updated_latex, filename="optimized_cv")
    pdf_path = compile_latex_to_pdf(tex_path)

    if not pdf_path:
        return {"error": "Failed to compile LaTeX to PDF."}

    return {
        "status": "success",
        "pdf_path": pdf_path
    }
    
@app.get("/email/status")
def get_email_status():
    emails = fetch_latest_emails()
    results = []

    for email in emails:
        status = classify_email(email["subject"], email["body"])
        results.append({
            "subject": email["subject"],
            "from": email["from"],
            "date": email["date"],
            "status": status
        })

    return results

# uvicorn backend.main:app --reload
# ### myenv\Scripts\activate
# # {
#   "description": "We are looking for a backend Python developer..."
# }
# {
#   "job_offer": {
#     "title": "Backend Python Developer",
#     "entreprise": "Tech Corp",
#     "localisation": "Paris",
#     "missions": "Develop APIs, maintain microservices",
#     "compétences": ["Python", "Docker", "FastAPI"],
#     "expérience_requise": "3+ years",
#     "type_contrat": "CDI",
#     "langues": ["French", "English"],
#     "salaire": "€50,000"
#   }
# }
