import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="CourtVision AI",
    layout="centered",
    page_icon="🏀"
)

# --- Color Palette ---
ACCENT = "#1DE9B6"     # turquoise
SECOND = "#2979FF"     # blue
LIME = "#C6FF00"       # lime green
DARK = "#1A1A1A"       # blackish
LIGHT = "#F5F5F5"      # light white

# --- Custom CSS ---
st.markdown(f"""
    <style>
        body {{
            background-color: {LIGHT};
            color: {DARK};
            font-family: 'Arial', sans-serif;
        }}

        .title {{
            font-size: 34px;
            font-weight: bold;
            color: {SECOND};
            text-align: center;
            margin-bottom: 25px;
        }}

        .card {{
            background: white;
            padding: 22px;
            border-radius: 14px;
            margin-bottom: 25px;
            border-left: 6px solid {ACCENT};
            box-shadow: 0 0 15px rgba(0,0,0,0.10);
        }}

        .league {{
            font-size: 20px;
            font-weight: bold;
            color: {SECOND};
        }}

        .match {{
            font-size: 22px;
            font-weight: bold;
            color: {DARK};
            margin-top: 6px;
        }}

        .label {{
            font-size: 17px;
            font-weight: bold;
            color: {ACCENT};
        }}

        .confidence {{
            font-size: 18px;
            font-weight: bold;
            color: {LIME};
            margin-top: 8px;
            display: block;
        }}
    </style>
""", unsafe_allow_html=True)

# --- Page Title ---
st.markdown("<div class='title'>🏀 CourtVision AI – Smart Predictions</div>", unsafe_allow_html=True)


# --- Prediction Data ---
games = [
    {
        "league": "EuroLeague",
        "match": "Fenerbahce vs Anadolu Efes",
        "handicap": "Fenerbahce -2",
        "over_under": "Under 172",
        "confidence": "95%"
    },
    {
        "league": "NBA",
        "match": "Heat vs Bucks",
        "handicap": "Heat +4",
        "over_under": "Under 214",
        "confidence": "93%"
    },
    {
        "league": "NBA",
        "match": "Lakers vs Celtics",
        "handicap": "Lakers +4",
        "over_under": "Under 170",
        "confidence": "96%"
    }
]

# --- Display Predictions ---
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
