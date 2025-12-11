import streamlit as st
import requests
import pandas as pd
import datetime

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
st.markdown("<div class='subtitle'>NBA & EuroLeague • Real-Time Data</div>", unsafe_allow_html=True)

# --- Date Picker ---
selected_date = st.date_input("📅 Select Date", datetime.date.today())
st.write(f"### 📌 Matches for: **{selected_date.strftime('%Y/%m/%d')}**")
st.write("")

# --- API Setup ---
API_URL = "https://allsportsapi2.p.rapidapi.com/api/basketball/event/date/{date}"
RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY"  # <-- اینجا کلید خودت رو بذار

headers = {
    "x-rapidapi-host": "allsportsapi2.p.rapidapi.com",
    "x-rapidapi-key": RAPIDAPI_KEY
}

# --- Fetch Data from API ---
def get_games(date):
    url = API_URL.format(date=date.strftime("%Y-%m-%d"))
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        events = data.get("result", [])
        games_list = []
        for e in events:
            games_list.append({
                "league": e.get("league_name", "Unknown"),
                "match": f"{e.get('home_team', '')} vs {e.get('away_team', '')}",
                "date": e.get("event_date", ""),
                "time": e.get("event_time", ""),
                "score": f"{e.get('home_score', '?')} - {e.get('away_score', '?')}",
                "status": e.get("event_status", "Upcoming")
            })
        return games_list
    except Exception as ex:
        st.error(f"Error fetching data: {ex}")
        return []

# --- Get Games ---
games = get_games(selected_date)

# --- Display Cards ---
for g in games:
    st.markdown(f"""
    <div class='card'>
        <div class='league'>{g['league']}</div>
        <div class='match'>{g['match']}</div>
        <span class='label'>Date & Time:</span> {g['date']} {g['time']}<br>
        <span class='label'>Score:</span> {g['score']}<br>
        <span class='label'>Status:</span> {g['status']}<br>
    </div>
    """, unsafe_allow_html=True)
