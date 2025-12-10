# streamlit_app.py
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="CourtVision AI", layout="wide", page_icon="🏀")

# ---------------------------
# CSS برای رنگ‌ها و فونت‌ها
# ---------------------------
st.markdown(
    """
    <style>
    .stApp { background-color: #f0f4f8; color: #000000; font-family: 'Segoe UI', sans-serif;}
    .card { background-color: #ffffff; padding: 20px; border-radius: 12px; margin-bottom: 15px; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.2); border-left: 6px solid #00bcd4;}
    .card h3 { color: #007bff; margin:0; font-weight: 700; }
    .card p { color: #333333; margin:0; font-weight: 500;}
    .stDateInput>div>div>input { background-color: #e0f7fa; color: #000; border-radius: 8px; padding: 5px;}
    </style>
    """, unsafe_allow_html=True
)

st.title("CourtVision AI 🏀")
st.subheader("Smart Predictions • NBA & EuroLeague")

# ---------------------------
# 1) داده‌های شبیه‌سازی شده با Over/Under و Spread مشخص
# ---------------------------
def generate_games():
    games = []
    # NBA نمونه
    nba_teams = [("Lakers", "Celtics"), ("Heat", "Bucks"), ("Warriors", "Suns")]
    for i, (home, away) in enumerate(nba_teams):
        date = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
        for _ in range(2):  # هر تیم 2-3 پیش‌بینی
            spread = random.choice([-5, -3, 4])
            over_under_val = random.choice([208, 210, 212])
            over_under_type = random.choice(["Over", "Under"])
            confidence = random.choice(["91%", "92%", "95%"])
            games.append({
                "Date": date,
                "League": "NBA",
                "Home": home,
                "Away": away,
                "Spread": spread,
                "OverUnder": f"{over_under_type} {over_under_val}",
                "Confidence": confidence
            })
    # EuroLeague نمونه
    euro_teams = [("Real Madrid","FC Barcelona"), ("Olympiacos","Panathinaikos"), ("Fenerbahce","Anadolu Efes")]
    for i, (home, away) in enumerate(euro_teams):
        date = (datetime.now() + timedelta(days=i+1)).strftime("%Y-%m-%d")
        for _ in range(2):
            spread = random.choice([-4, -3, 5])
            over_under_val = random.choice([168, 170, 172])
            over_under_type = random.choice(["Over", "Under"])
            confidence = random.choice(["91%", "92%", "94%"])
            games.append({
                "Date": date,
                "League": "EuroLeague",
                "Home": home,
                "Away": away,
                "Spread": spread,
                "OverUnder": f"{over_under_type} {over_under_val}",
                "Confidence": confidence
            })
    return pd.DataFrame(games)

df = generate_games()

# ---------------------------
# 2) فیلتر تاریخ (امروز یا نزدیک‌ترین)
# ---------------------------
selected_date = st.date_input("Select Date", datetime.now())
if not any(df["Date"] == selected_date.strftime("%Y-%m-%d")):
    closest_date = min(pd.to_datetime(df["Date"]), key=lambda d: abs(d - pd.to_datetime(selected_date)))
    filtered_df = df[df["Date"] == closest_date.strftime("%Y-%m-%d")]
    st.info(f"No games for selected date. Showing closest games on {closest_date.strftime('%Y-%m-%d')}.")
else:
    filtered_df = df[df["Date"] == selected_date.strftime("%Y-%m-%d")]

# ---------------------------
# 3) نمایش کارت‌ها
# ---------------------------
for idx, row in filtered_df.iterrows():
    st.markdown(
        f"""
        <div class="card">
            <h3>{row['League']} | {row['Home']} vs {row['Away']}</h3>
            <p>Handicap: {row['Home']} {row['Spread']}</p>
            <p>Over/Under: {row['OverUnder']}</p>
            <p>Confidence: {row['Confidence']}</p>
        </div>
        """, unsafe_allow_html=True
    )
