# streamlit_app.py
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import requests

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
# 1) Fetch NBA Data
# ---------------------------
def fetch_nba_games(days=3):
    games = []
    url_base = "https://www.balldontlie.io/api/v1/games?dates[]="
    for i in range(days):
        date_str = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
        try:
            r = requests.get(url_base + date_str).json()
            for g in r.get("data", []):
                games.append({
                    "Date": date_str,
                    "League": "NBA",
                    "Home": g["home_team"]["full_name"],
                    "Away": g["visitor_team"]["full_name"],
                    "Spread": -5,
                    "Over/Under": 210,
                    "Confidence": "92%"
                })
        except Exception as e:
            print(f"Error fetching NBA: {e}")
    return games

# ---------------------------
# 2) EuroLeague Data (Simulated)
# ---------------------------
def fetch_euroleague_games():
    euro_games = [
        ("Real Madrid", "FC Barcelona"),
        ("Olympiacos", "Panathinaikos"),
        ("Fenerbahce", "Anadolu Efes"),
        ("Maccabi Tel Aviv", "Valencia Basket"),
        ("EA7 Milan", "Panathinaikos"),
        ("Paris Basketball", "Zalgiris Kaunas")
    ]
    games = []
    for i, (home, away) in enumerate(euro_games):
        date_str = (datetime.now() + timedelta(days=i+1)).strftime("%Y-%m-%d")
        games.append({
            "Date": date_str,
            "League": "EuroLeague",
            "Home": home,
            "Away": away,
            "Spread": -4,
            "Over/Under": 168,
            "Confidence": "92%"
        })
    return games

# ---------------------------
# 3) Combine & DataFrame
# ---------------------------
all_games = fetch_nba_games() + fetch_euroleague_games()
df = pd.DataFrame(all_games)

# ---------------------------
# 4) Date Filter
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
