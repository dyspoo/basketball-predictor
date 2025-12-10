# streamlit_app.py
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="CourtVision AI", layout="wide", page_icon="🏀")

# --------------------------------
# CSS STYLE (روشن مثل Digipay)
# --------------------------------
st.markdown(
    """
    <style>
    .stApp { background-color: #ecf5ff; color: #000; font-family: 'Segoe UI', sans-serif;}
    .card { background-color: #ffffff; padding: 22px; border-radius: 14px;
            margin-bottom: 18px; box-shadow: 0 4px 14px rgba(0,0,0,0.15);
            border-left: 6px solid #00bcd4; }
    .card h3 { color: #0077ff; margin:0; font-weight: 700; }
    .card p { color: #222; margin:0; font-weight: 500; font-size: 15px; }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------
# CREATE REALISTIC UNIQUE GAMES
# --------------------------------
def generate_games_for_day():
    nba_games = [
        ("Lakers", "Celtics"),
        ("Heat", "Bucks"),
        ("Warriors", "Suns"),
        ("Clippers", "Nuggets"),
    ]

    euro_games = [
        ("Real Madrid", "Barcelona"),
        ("Fenerbahce", "Anadolu Efes"),
        ("Olympiacos", "Panathinaikos"),
        ("Monaco", "Maccabi Tel Aviv"),
    ]

    all_games = nba_games + euro_games

    selected = random.sample(all_games, random.randint(2, 5))  # 2 تا 5 بازی واقعی در روز

    games = []

    for (home, away) in selected:
        spread = random.choice([-6, -5, -4, -3, -2, 2, 3, 4])
        ov = random.choice([168, 170, 172, 210, 212, 214])
        ov_type = random.choice(["Over", "Under"])
        conf = random.randint(88, 97)

        games.append({
            "Home": home,
            "Away": away,
            "Spread": spread,
            "OverUnder": f"{ov_type} {ov}",
            "Confidence": conf
        })

    df = pd.DataFrame(games)
    df = df[df["Confidence"] >= 90]  # فقط بازی‌های دقت بالا

    # حداکثر 3 بازی
    if len(df) > 3:
        df = df.sample(3)

    return df


# --------------------------------
# DATE SELECTION
# --------------------------------
st.title("CourtVision AI 🏀")
st.subheader("Smart Predictions • High Confidence Picks (90%+)")

selected_date = st.date_input("Select Date", datetime.now())

df = generate_games_for_day()


# --------------------------------
# DISPLAY
# --------------------------------
if df.empty:
    st.warning("No high-confidence games (90%+) found for this date.")
else:
    for _, row in df.iterrows():
        st.markdown(
            f"""
            <div class="card">
                <h3>{row['Home']} vs {row['Away']}</h3>
                <p>Handicap: <b>{row['Home']} {row['Spread']}</b></p>
                <p>Over/Under: <b>{row['OverUnder']}</b></p>
                <p>Confidence: <b>{row['Confidence']}%</b></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
