# streamlit_app.py
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import requests

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
# داده‌های شبیه‌سازی شده
# ---------------------------
def get_games():
    games = []
    # NBA
    nba_teams = [("Lakers", "Celtics"), ("Heat", "Bucks"), ("Warriors", "Suns")]
    for i, (home, away) in enumerate(nba_teams):
        date = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
        games.append({"Date": date,"League":"NBA","Home":home,"Away":away,"Spread":-5,"Over/Under":210,"Confidence":"92%"})
        games.append({"Date": date,"League":"NBA","Home":home,"Away":away,"Spread":-3,"Over/Under":208,"Confidence":"91%"})
    # EuroLeague
    euro_teams = [("Real Madrid","FC Barcelona"), ("Olympiacos","Panathinaikos"), ("Fenerbahce","Anadolu Efes")]
    for i, (home, away) in enumerate(euro_teams):
        date = (datetime.now() + timedelta(days=i+1)).strftime("%Y-%m-%d")
        games.append({"Date": date,"League":"EuroLeague","Home":home,"Away":away,"Spread":-4,"Over/Under":168,"Confidence":"92%"})
        games.append({"Date": date,"League":"EuroLeague","Home":home,"Away":away,"Spread":-3,"Over/Under":170,"Confidence":"91%"})
    return pd.DataFrame(games)

df = get_games()

# ---------------------------
# فیلتر بر اساس تاریخ
# ---------------------------
selected_date = st.date_input("Select Date", datetime.now())
if not any(df["Date"] == selected_date.strftime("%Y-%m-%d")):
    closest_date = min(pd.to_datetime(df["Date"]), key=lambda d: abs(d - pd.to_datetime(selected_date)))
    filtered_df = df[df["Date"] == closest_date.strftime("%Y-%m-%d")]
    st.info(f"No games for selected date. Showing closest games on {closest_date.strftime('%Y-%m-%d')}.")
else:
    filtered_df = df[df["Date"] == selected_date.strftime("%Y-%m-%d")]

# ---------------------------
# نمایش کارت‌ها
# ---------------------------
for idx, row in filtered_df.iterrows():
    st.markdown(
        f"""
        <div class="card">
            <h3>{row['League']} | {row['Home']} vs {row['Away']}</h3>
            <p>Spread: {row['Spread']} | Over/Under: {row['Over/Under']} | Confidence: {row['Confidence']}</p>
        </div>
        """, unsafe_allow_html=True
    )
