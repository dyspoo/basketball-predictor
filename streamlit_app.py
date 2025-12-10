# streamlit_app.py
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="CourtVision AI", layout="wide", page_icon="🏀")

st.markdown(
    """
    <style>
    .stApp { background-color: #1a1a2e; color: white; }
    .card { background-color: #162447; padding: 15px; border-radius: 12px; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);}
    .card h3 { color: #e43f5a; margin:0; }
    .card p { color: #ffffff; margin:0; }
    </style>
    """, unsafe_allow_html=True
)

st.title("CourtVision AI 🏀")
st.subheader("Smart Predictions • NBA & EuroLeague")

# ---------------------------
# 1) Shabihe-sazi Data (Offline)
# ---------------------------
def get_games():
    games = []
    # NBA 3 days
    nba_teams = [("Lakers", "Celtics"), ("Heat", "Bucks"), ("Warriors", "Suns")]
    for i, (home, away) in enumerate(nba_teams):
        date = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
        games.append({
            "Date": date,
            "League": "NBA",
            "Home": home,
            "Away": away,
            "Spread": -5 + i,
            "Over/Under": 210 - i*2,
            "Confidence": f"{92-i}%"
        })
    # EuroLeague 3 days
    euro_teams = [("Real Madrid","FC Barcelona"), ("Olympiacos","Panathinaikos"), ("Fenerbahce","Anadolu Efes")]
    for i, (home, away) in enumerate(euro_teams):
        date = (datetime.now() + timedelta(days=i+1)).strftime("%Y-%m-%d")
        games.append({
            "Date": date,
            "League": "EuroLeague",
            "Home": home,
            "Away": away,
            "Spread": -4 + i,
            "Over/Under": 168 + i*2,
            "Confidence": f"{91-i}%"
        })
    return pd.DataFrame(games)

df = get_games()

# ---------------------------
# 2) Filter by Date
# ---------------------------
selected_date = st.date_input("Select Date", datetime.now())
filtered_df = df[df["Date"] == selected_date.strftime("%Y-%m-%d")]

if filtered_df.empty:
    st.info("No games found for this date. Try another day.")
else:
    for idx, row in filtered_df.iterrows():
        st.markdown(
            f"""
            <div class="card">
                <h3>{row['League']} | {row['Home']} vs {row['Away']}</h3>
                <p>Spread: {row['Spread']} | Over/Under: {row['Over/Under']} | Confidence: {row['Confidence']}</p>
            </div>
            """, unsafe_allow_html=True
        )
