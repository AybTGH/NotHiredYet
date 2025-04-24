# NotHiredYet
"NotHiredYet is an AI-driven job application assistant that helps you discover offers, craft tailored CVs and cover letters, track applications, monitor email replies, and send follow-ups — all from one platform.

# Architecture 

NOTHIREDYET/
│
├── frontend/                         # Streamlit app
│   └── dashboard.py                  # Main UI (add job, view apps, etc.)
│
├── backend/                          # FastAPI backend
│   ├── main.py                       # Launch API server
│   ├── parsers/                      # Parsing logic
│   │   ├── url_parser.py             # Extract info from job URLs
│   │   ├── text_parser.py            # Extract info from pasted job description
│   │   └── extractor.py              # Extract missions, location, years XP, etc.
│   ├── ai/                           
│   │   ├── cv_optimizer.py           # Modify CV based on offer
│   │   └── summarizer.py             # Summarize job offers
│   ├── mail/                         # Gmail integration (later)
│   │   ├── gmail_reader.py
│   │   └── status_classifier.py      # Classify email as interview/reject/etc.
│   ├── tracker/                      # Application tracker logic
│   │   ├── db.py                     # DB access (SQLite/Postgres)
│   │   └── application_manager.py    # CRUD for job applications
│   └── utils/                        # Embeddings, helper funcs
│       └── openai_client.py
│
├── docs/                             # Example resumes, letters
├── data/                             # Static or seed job data
├── requirements.txt
├── README.md
└── .env                              # For API keys, Gmail secrets

### myenv\Scripts\activate
