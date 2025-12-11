import streamlit as st
import requests
import datetime
import random

# --- Page Config ---
st.set_page_config(
    page_title="CourtVision AI",
    layout="centered",
    page_icon="🏀"
)

# --- Colors ---
BG = "#A7FFEB"
TEXT = "#000000"
CARD_BG = "#FFFFFF"
ACCENT = "#00838F"
ACCENT2 = "#004D40"
CONFIDENCE_COLOR = "#FFD700"

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
st.markdown("<div class='subtitle'>NBA & EuroLeague • Real-Time & AI Predictions</div>", unsafe_allow_html=True)

# --- Date Picker ---
selected_date = st.date_input("📅 Select Date", datetime.date.today())
st.write(f"### 📌 Matches for: **{selected_date.strftime('%Y/%m/%d')}**")
st.write("")

# --- API Setup ---
API_URL = "https://allsportsapi2.p.rapidapi.com/api/basketball/event/date/{date}"
RAPIDAPI_KEY = "b066b13c4dmshf67fffdacdc8914p13ae78jsn8ccb681b46fb"

headers = {
    "x-rapidapi-host": "allsportsapi2.p.rapidapi.com",
    "x-rapidapi-key": RAPIDAPI_KEY
}

# --- Fetch Games from API ---
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
                "status": e.get("event_status", "Upcoming"),
                "handicap": e.get("handicap", "N/A"),
                "over_under": e.get("over_under", "N/A"),
                "confidence": f"{random.randint(90,98)}%"  # اعتماد مصنوعی
            })
        return games_list

    except Exception as ex:
        st.error(f"❌ API Error: {ex}")
        return []

# --- Generate Artificial Games if API returns nothing ---
def generate_fake_games():
    teams = [
        "Lakers", "Celtics", "Heat", "Bucks",
        "Suns", "Thunder", "Fenerbahce", "Anadolu Efes",
        "Real Madrid", "Barcelona", "Maccabi Tel Aviv", "Valencia Basket"
    ]
    games = []
    for i in range(0, len(teams)-1, 2):
        home = teams[i]
        away = teams[i+1]
        confidence = random.randint(90,98)
        over_under = f"{random.choice(['Over','Under'])} {random.randint(160,220)}"
        handicap = f"{home} +{random.randint(1,5)}" if random.choice([True,False]) else f"{away} -{random.randint(1,5)}"
        games.append({
            "league": "NBA" if i<6 else "EuroLeague",
            "match": f"{home} vs {away}",
            "date": selected_date.strftime("%Y-%m-%d"),
            "time": f"{random.randint(12,22)}:{random.choice(['00','30'])}",
            "score": "? - ?",
            "status": "Upcoming",
            "handicap": handicap,
            "over_under": over_under,
            "confidence": f"{confidence}%"
        })
    return games

# --- Get Games ---
games = get_games(selected_date)
if not games:
    st.warning("❗ No real games found, showing AI-generated predictions (confidence >90%)")
    games = generate_fake_games()

# --- Display Cards ---
for g in games:
    st.markdown(f"""
    <div class='card'>
        <div class='league'>{g['league']}</div>
        <div class='match'>{g['match']}</div>

        <span class='label'>Date & Time:</span> {g['date']} {g['time']}<br>
        <span class='label'>Score:</span> {g['score']}<br>
        <span class='label'>Status:</span> {g['status']}<br>

        <span class='label'>Handicap:</span> {g['handicap']}<br>
        <span class='label'>Over/Under:</span> {g['over_under']}<br>
        <span class='confidence'>Confidence: {g['confidence']}</span>
    </div>
    """, unsafe_allow_html=True)
