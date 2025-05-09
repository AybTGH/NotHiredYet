
def classify_email(subject: str, body: str):
    content = f"{subject.lower()} {body.lower()}"

    if "job offer" in content or "we are pleased" in content or "congratulations" in content:
        return "offer"
    elif "unfortunately" in content or "we regret" in content or "not selected" in content:
        return "rejection"
    else:
        return "other"
