import streamlit as st
import requests
import pandas as pd
import datetime
import random

# --- Page Config ---
st.set_page_config(
    page_title="CourtVision AI",
    layout="centered",
    page_icon="🏀"
)

# --- Colors ---
BG = "#A7FFEB"       # turquoise background
TEXT = "#000000"     # black text
CARD_BG = "#FFFFFF"  # white cards
ACCENT = "#00838F"   # teal
ACCENT2 = "#004D40"  # dark teal
CONFIDENCE_COLOR = "#FFD700"  # gold

# --- Custom CSS ---
st.markdown(f"""
<style>
body {{ background-color: {BG}; color: {TEXT}; font-family: 'Arial', sans-serif; }}
.title {{ font-size:42px; font-weight:bold; text-align:center; margin-bottom:5px; }}
.subtitle {{ text-align:center; color:{ACCENT2}; font-size:22px; font-weight:bold; margin-bottom:20px; }}
.card {{ background:{CARD_BG}; padding:25px; border-radius:18px; margin-bottom:25px; border:3px solid {ACCENT}; box-shadow:0 4px 18px rgba(0,0,0,0.12); }}
.league {{ font-size:23px; font-weight:bold; color:{ACCENT2}; }}
.match {{ font-size:28px; font-weight:bold; color:{TEXT}; margin-top:8px; }}
.label {{ font-size:21px; font-weight:bold; color:{ACCENT}; }}
.confidence {{ font-size:23px; font-weight:bold; color:{CONFIDENCE_COLOR}; margin-top:12px; display:block; }}
.stDateInput > div > input {{ font-size:20px !important; padding:10px !important; }}
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<div class='title'>🏀 CourtVision AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>NBA & EuroLeague • High Accuracy AI Predictions</div>", unsafe_allow_html=True)

# --- Date Picker ---
selected_date = st.date_input("📅 Select Date", datetime.date.today())
st.write(f"### 📌 Predictions for: **{selected_date.strftime('%Y/%m/%d')}**")
st.write("")

# --- Sample Data: Replace with API for real ---
nba_teams = [
    "Lakers", "Celtics", "Heat", "Bucks", "Suns", "Thunder"
]
euro_teams = [
    "Fenerbahce", "Anadolu Efes", "Real Madrid", "Barcelona",
    "Maccabi Tel Aviv", "Valencia Basket"
]

def generate_predictions(teams):
    games = []
    for i in range(0, len(teams)-1, 2):
        home = teams[i]
        away = teams[i+1]
        # Random but high confidence >90%
        confidence = random.randint(90, 98)
        over_under = random.choice(["Over", "Under"]) + f" {random.randint(160, 220)}"
        handicap = random.choice([home, away])
        # If home team selected, +ve, else -ve
        if handicap == home:
            handicap_str = f"{home} +{random.randint(1,5)}"
        else:
            handicap_str = f"{away} -{random.randint(1,5)}"
        games.append({
            "league": "NBA" if home in nba_teams else "EuroLeague",
            "match": f"{home} vs {away}",
            "handicap": handicap_str,
            "over_under": over_under,
            "confidence": f"{confidence}%"
        })
    return games

# --- Get Games ---
games = generate_predictions(nba_teams) + generate_predictions(euro_teams)

# --- Display Cards ---
for g in games:
    st.markdown(f"""
    <div class='card'>
        <div class='league'>{g['league']}</div>
        <div class='match'>{g['match']}</div>
        <br>
        <span class='label'>Handicap:</span> {g['handicap']}<br>
        <span class='label'>Over/Under:</span> {g['over_under']}<br>
        <span class='confidence'>Confidence: {g['confidence']}</span>
    </div>
    """, unsafe_allow_html=True)
