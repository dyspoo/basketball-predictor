import streamlit as st
import random  # pour générer des nombres aléatoires

st.title("Jeux NBA & EuroLeague du jour avec prédictions aléatoires")

# Données d'exemple
games = [
    {"Ligue": "NBA", "Équipe à domicile": "Lakers", "Équipe visiteuse": "Celtics"},
    {"Ligue": "EuroLeague", "Équipe à domicile": "Real Madrid", "Équipe visiteuse": "FC Barcelona"}
]

# Fonction simple de prédiction aléatoire
def prediction(game):
    over_under = random.randint(190, 220)  # Over/Under entre 190 et 220
    handicap = random.randint(-10, 10)     # Handicap entre -10 et +10
    confiance = random.randint(60, 95)     # Confiance entre 60% et 95%
    return {
        "Over/Under": f"Over {over_under}",
        "Handicap": f"{handicap:+}",  # affiche + ou -
        "Confiance": f"{confiance}%"
    }

# Affichage du tableau avec prédictions aléatoires
st.subheader("Jeux et prédictions d'aujourd'hui")
for game in games:
    pred = prediction(game)
    st.write(f"{game['Ligue']} : {game['Équipe à domicile']} vs {game['Équipe visiteuse']} - "
             f"Over/Under : {pred['Over/Under']}, Handicap : {pred['Handicap']}, Confiance : {pred['Confiance']}")
