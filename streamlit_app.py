import streamlit as st
import datetime
import random
import time

# --- Page Config ---
st.set_page_config(page_title="CourtVision AI Live", layout="centered", page_icon="🏀")

# --- Colors ---
BG = "#E0F7FA"
TEXT = "#000000"
CARD_BG = "#FFFFFF"
ACCENT = "#00796B"
HANDICAP_COLOR = "#FF7043"
OVERUNDER_COLOR = "#42A5F5"
CONFIDENCE_COLOR = "#FFD700"

# --- Custom CSS ---
st.markdown(f"""
<style>
body {{ background-color: {BG}; color: {TEXT}; font-family: 'Arial', sans-serif; }}
.title {{ font-size:36px; font-weight:bold; text-align:center; margin-bottom:10px; }}
.subtitle {{ text-align:center; color:{ACCENT}; font-size:18px; margin-bottom:20px; }}
.card {{ background:{CARD_BG}; padding:20px; border-radius:15px; margin-bottom:20px;
         border:2px solid {ACCENT}; box-shadow:0 4px 10px rgba(0,0,0,0.12); }}
.league {{ font-size:20px; font-weight:bold; color:{ACCENT}; margin-bottom:5px; }}
.match {{ font-size:22px; font-weight:bold; color:{TEXT}; margin-bottom:5px; }}
.label {{ font-size:16px; font-weight:bold; }}
.handicap {{ color:{HANDICAP_COLOR}; font-weight:bold; }}
.overunder {{ color:{OVERUNDER_COLOR}; font-weight:bold; }}
.confidence {{ font-size:16px; font-weight:bold; color:{CONFIDENCE_COLOR}; margin-top:5px; }}
.date {{ font-size:14px; color:gray; margin-bottom:5px; }}
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<div class='title'>🏀 CourtVision AI Live</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>NBA & EuroLeague • Live AI Predictions</div>", unsafe_allow_html=True)

# --- Date Picker ---
selected_date = st.date_input("📅 Select Date", datetime.date.today())

# --- Game Data (Live Simulation) ---
teams = [
    ("Lakers","Celtics"), ("Heat","Bucks"), ("Suns","Thunder"),
    ("Fenerbahce","Anadolu Efes"), ("Real Madrid","Barcelona"), ("Maccabi Tel Aviv","Valencia Basket")
]
leagues = ["NBA"]*3 + ["EuroLeague"]*3

def generate_live_games():
    games = []
    for idx, (home, away) in enumerate(teams):
        league = leagues[idx]
        # simulate dynamic score
        home_score = random.randint(70, 120)
        away_score = random.randint(70, 120)
        # random time
        game_time = datetime.datetime.combine(selected_date, datetime.time(random.randint(12,22), random.choice([0,30])))
        # random handicap & over/under
        handicap_val = random.randint(-5,5)
        handicap = f"{home} {f'+{handicap_val}' if handicap_val>=0 else f'{handicap_val}'}" if random.choice([True,False]) else f"{away} {f'+{handicap_val}' if handicap_val>=0 else f'{handicap_val}'}"
        overunder_val = random.randint(160,220)
        over_under = f"{random.choice(['Over','Under'])} {overunder_val}"
        confidence = random.randint(90,98)
        # status
        status = random.choice(["Live", "Upcoming", "Finished"])
        games.append({
            "league": league,
            "match": f"{home} vs {away}",
            "date": game_time.strftime("%Y-%m-%d %H:%M"),
            "score": f"{home_score} - {away_score}" if status!="Upcoming" else "? - ?",
            "status": status,
            "handicap": handicap,
            "over_under": over_under,
            "confidence": f"{confidence}%"
        })
    return games

# --- Live Refresh ---
st.markdown("### 🔄 Live Updates (simulated) every 30 seconds")
placeholder = st.empty()

while True:
    live_games = generate_live_games()
    with placeholder.container():
        for g in live_games:
            st.markdown(f"""
            <div class='card'>
                <div class='league'>{g['league']}</div>
                <div class='match'>{g['match']}</div>
                <div class='date'>🕒 {g['date']} | Status: {g['status']}</div>
                <div><span class='handicap'>Handicap:</span> {g['handicap']}</div>
                <div><span class='overunder'>Over/Under:</span> {g['over_under']}</div>
                <div class='confidence'>Confidence: {g['confidence']}</div>
                <div><span class='label'>Score:</span> {g['score']}</div>
            </div>
            """, unsafe_allow_html=True)
    time.sleep(30)  # refresh every 30 seconds
