import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")

        # Remove scripts and styles
        for tag in soup(["script", "style"]):
            tag.decompose()

        # Get clean visible text
        text = soup.get_text(separator=" ", strip=True)
        print(text)
        return text
    except Exception as e:
        print(f"Error scraping URL: {e}")
        return ""
