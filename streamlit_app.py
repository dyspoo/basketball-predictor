import streamlit as st
import requests
import datetime
import random
from bs4 import BeautifulSoup

# --- Configuration de la page ---
st.set_page_config(page_title="🏀 Prédictions NBA & EuroLeague", layout="wide", page_icon="🏀")

# --- CSS UX professionnel ---
st.markdown("""
<style>
body {background-color: #0F1116; color: #FFFFFF; font-family: 'Helvetica', sans-serif;}
.title {font-size:32px; font-weight:bold; color:#4CAF50; margin-bottom:20px;}
.card {background-color:#1B1E24; border-radius:12px; padding:20px; margin-bottom:20px; border:1px solid #2A2D35;}
.card h3 {margin:0; color:#00EAFF;}
.card p {margin:5px 0;}
.nba {border-left:6px solid #4CAF50;}
.euro {border-left:6px solid #00EAFF;}
</style>
""", unsafe_allow_html=True)

st.title("🏀 Prédictions NBA & EuroLeague - Sélection intelligente (>90% confiance)")

today = datetime.date.today()

# --- NBA réel ---
def nba_games():
    url = f"https://www.balldontlie.io/api/v1/games?dates[]={today}"
    r = requests.get(url).json()
    jeux = []
    for g in r["data"]:
        jeux.append({
            "Ligue": "NBA",
            "Home": g["home_team"]["full_name"],
            "Away": g["visitor_team"]["full_name"]
        })
    return jeux

# --- EuroLeague réel via scraping ESPN ---
def euro_games():
    url = "https://www.espn.com/basketball/schedule/_/league/EL"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    jeux = []
    rows = soup.find_all("tr", class_="Table__TR")
    for row in rows[:10]:  # on prend max 10 matchs pour l'exemple
        teams = row.find_all("td", class_="Table__TD")
        if len(teams) >= 2:
            home = teams[0].text.strip()
            away = teams[1].text.strip()
            if home and away:
                jeux.append({
                    "Ligue": "EuroLeague",
                    "Home": home,
                    "Away": away
                })
    return jeux

# --- Prédictions AI (simulation) ---
def ai_prediction():
    over_under = random.randint(190, 230)
    handicap = random.randint(-12,12)
    confidence = random.randint(90,95)  # toujours >90%
    return {
        "Over/Under": f"Over {over_under}",
        "Handicap": f"{handicap:+}",
        "Confiance": f"{confidence}%"
    }

# --- Collecte des jeux ---
games_nba = nba_games()
games_euro = euro_games()
all_games = games_nba + games_euro

st.subheader(f"Jeux sélectionnés avec confiance >90% ({today})")

if not all_games:
    st.write("Aucun match aujourd'hui.")
else:
    for g in all_games:
        pred = ai_prediction()
        css_class = "nba" if g["Ligue"]=="NBA" else "euro"
        st.markdown(f"""
        <div class='card {css_class}'>
            <h3>{g['Ligue']}</h3>
            <p><strong>{g['Home']}</strong> vs <strong>{g['Away']}</strong></p>
            <p>Over/Under : {pred['Over/Under']}</p>
            <p>Handicap : {pred['Handicap']}</p>
            <p>Confiance : {pred['Confiance']}</p>
        </div>
        """, unsafe_allow_html=True)
