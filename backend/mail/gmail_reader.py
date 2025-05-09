from imap_tools import MailBox, AND
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER")


def fetch_latest_emails(limit=1):
    emails = []

    with MailBox(IMAP_SERVER).login(EMAIL, PASSWORD, initial_folder="INBOX") as mailbox:
        for msg in mailbox.fetch(AND(all=True), limit=limit, reverse=True):
            emails.append({
                "subject": msg.subject,
                "from": msg.from_,
                "date": msg.date.isoformat(),
                "body": msg.text or msg.html or ""
            })
    return emails
