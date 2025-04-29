# 🚀 NotHiredYet

> ⚠️ **Work in Progress**: This project is still under development and not fully complete. Features are being added and refined regularly.

**NotHiredYet** is an AI-powered job application assistant that streamlines your entire job hunt — from discovering offers to following up. It helps you apply smarter and faster using automation and AI.

> Discover jobs, tailor CVs and cover letters, track applications, monitor replies, and follow up — all from one platform.

---

## 🧠 Features

- 🔍 Parse job descriptions from URLs or plain text
- 📝 Generate AI-optimized CVs and cover letters
- 📊 Track your job applications with ease
- 📬 Monitor Gmail for replies and classify outcomes (interview, rejected, etc.)
- 🔁 Send follow-ups and automate your outreach

---

## 🏗️ Architecture Overview

```
NOTHIREDYET/
│
├── frontend/                         # Frontend (Streamlit app)
│   └── dashboard.py                  # Main UI for managing job applications
│
├── backend/                          # Backend (FastAPI server)
│   ├── main.py                       # API server entry point
│
│   ├── parsers/                      # Job parsing modules
│   │   ├── url_parser.py             # Scrape data from job listing URLs
│   │   ├── text_parser.py            # Handle raw pasted job descriptions
│   │   └── extractor.py              # Extract structured fields like experience, location
│
│   ├── ai/                           # AI features
│   │   ├── cv_optimizer.py           # Tailor CVs to job descriptions
│   │   └── summarizer.py             # Summarize job descriptions
│
│   ├── mail/                         # Gmail integration (in progress)
│   │   ├── gmail_reader.py           # Reads and filters job-related emails
│   │   └── status_classifier.py      # Labels emails: interview, rejection, etc.
│
│   ├── tracker/                      # Application tracking logic
│   │   ├── db.py                     # Database interface (SQLite/PostgreSQL)
│   │   └── application_manager.py    # CRUD operations for job apps
│
│   └── utils/                        # Utilities and OpenAI helpers
│       └── openai_client.py          # Handles OpenAI API requests
│
├── docs/                             # Sample CVs, cover letters, documentation
├── data/                             # Static or seed job data
├── requirements.txt                  # Python dependencies
├── README.md                         # This file
└── .env                              # API keys, secrets, and Gmail config
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/AybTGH/nothiredyet.git
cd nothiredyet
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_key
GMAIL_USER=your_email@gmail.com
GMAIL_APP_PASSWORD=your_app_password
```

---

## ▶️ Running the App

### Run backend (FastAPI)

```bash
uvicorn backend.main:app --reload
```

### Run frontend (Streamlit)

```bash
streamlit run frontend/dashboard.py
```

---

## 📦 Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **AI Engine:** OpenAI GPT
- **Database:** SQLite (optionally PostgreSQL)
- **Email:** Gmail API integration (in progress)

---

## 📈 Roadmap

- [ ] OAuth2 login and multi-user support
- [ ] Full Gmail API integration with real-time monitoring
- [ ] Chrome extension to parse job offers in-browser
- [ ] PDF CV editor
- [ ] Job board integrations (Indeed, LinkedIn, etc.)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create your feature branch: `git checkout -b feat/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feat/amazing-feature`
5. Open a pull request

---

## 🪪 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [OpenAI](https://openai.com)
- [FastAPI](https://fastapi.tiangolo.com)
- [Streamlit](https://streamlit.io)
- All job seekers everywhere — this one's for you.
