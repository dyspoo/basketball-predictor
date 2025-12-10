import requests
import csv
from datetime import datetime, timedelta

# -------------------------------
# 1) NBA DATA (FREE API)
# -------------------------------
def fetch_nba_games(days=7):
    all_games = []
    base_url = "https://www.balldontlie.io/api/v1/games?dates[]="

    for i in range(days):
        date = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
        r = requests.get(base_url + date).json()
        for g in r.get("data", []):
            home = g["home_team"]["full_name"]
            away = g["visitor_team"]["full_name"]

            # Fake simple odds (for AI training)
            spread = -5
            ou = 210

            all_games.append([
                date, "NBA", home, away, spread, ou
            ])
    return all_games

# -------------------------------
# 2) EUROLEAGUE DATA (SIMULATED)
# -------------------------------
def fetch_euroleague_games():
    fake_games = [
        ["2025-12-10", "EuroLeague", "Real Madrid", "FC Barcelona", -4, 168],
        ["2025-12-11", "EuroLeague", "Olympiacos", "Panathinaikos", -3, 162],
        ["2025-12-12", "EuroLeague", "Fenerbahce", "Anadolu Efes", -2, 164]
    ]
    return fake_games

# -------------------------------
# 3) SAVE DATASET
# -------------------------------
all_data = []
all_data.extend(fetch_nba_games())
all_data.extend(fetch_euroleague_games())

with open("dataset.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "League", "Home", "Away", "Spread", "OverUnder"])
    writer.writerows(all_data)

print("dataset.csv generated ✔")
