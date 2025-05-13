import streamlit as st
import pandas as pd
import plotly.express as px


mock_emails = [
    {
        "subject": "🎉 Congratulations! You've been selected",
        "from": "hr@dreamcompany.com",
        "date": "2025-05-12T10:34:00",
        "status": "offer"
    },
    {
        "subject": "❌ Unfortunately, we have decided to move forward with other candidates",
        "from": "jobs@anotherco.io",
        "date": "2025-05-10T15:22:00",
        "status": "rejection"
    },
    {
        "subject": "🤔 Your application has been received",
        "from": "noreply@startupmail.com",
        "date": "2025-05-09T09:12:00",
        "status": "other"
    }
]

df = pd.DataFrame(mock_emails)
df["date"] = pd.to_datetime(df["date"])


status_colors = {
    "offer": "#ccf5d3",      # vert clair
    "rejection": "#ffd6d6",  # rouge clair
    "other": "#fffacc"       # jaune clair
}

def highlight_row(row):
    color = status_colors.get(row["status"], "#f0f0f0")
    return [f"background-color: {color}"] * len(row)

styled_df = df.style.apply(highlight_row, axis=1)

st.set_page_config(page_title="📬 Email Classifier", layout="centered")
st.title("📬 Emails Classifiés")
st.caption("Analyse visuelle des statuts d'emails (mock data)")

# 📊 Graphe par statut
st.subheader("📊 Répartition des statuts")
status_counts = df["status"].value_counts()
st.bar_chart(status_counts)

# 📄 Tableau 
st.subheader("📋 Détails des emails")
st.dataframe(styled_df, use_container_width=True)

with st.expander("📦 Données brutes JSON"):
    st.json(mock_emails)

 # streamlit run frontend/dashboard.py