import streamlit as st
import datetime

# --- Page Config ---
st.set_page_config(
    page_title="CourtVision AI",
    layout="centered",
    page_icon="🏀"
)

# --- Colors ---
BG = "#A7FFEB"       # turquoise light background
TEXT = "#000000"     # black text
CARD_BG = "#FFFFFF"  # white cards
ACCENT = "#00838F"   # teal blue
ACCENT2 = "#004D40"  # dark teal green

# --- Custom CSS ---
st.markdown(f"""
    <style>
        body {{
            background-color: {BG};
            color: {TEXT};
            font-family: 'Arial', sans-serif;
        }}

        .title {{
            font-size: 42px;
            font-weight: bold;
            color: {TEXT};
            text-align: center;
            margin-bottom: 5px;
        }}

        .subtitle {{
            text-align: center;
            color: {ACCENT2};
            margin-bottom: 25px;
            font-size: 22px;
            font-weight: bold;
        }}

        .card {{
            background: {CARD_BG};
            padding: 25px;
            border-radius: 18px;
            margin-bottom: 25px;
            border: 3px solid {ACCENT};
            box-shadow: 0 4px 18px rgba(0,0,0,0.12);
        }}

        .league {{
            font-size: 23px;
            font-weight: bold;
            color: {ACCENT2};
        }}

        .match {{
            font-size: 28px;
            font-weight: bold;
            color: {TEXT};
            margin-top: 8px;
        }}

        .label {{
            font-size: 21px;
            font-weight: bold;
            color: {ACCENT};
        }}

        .confidence {{
            font-size: 23px;
            font-weight: bold;
            color: {ACCENT2};
            margin-top: 12px;
            display: block;
        }}

        .stDateInput > div > input {{
            font-size: 20px !important;
            padding: 10px !important;
        }}
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<div class='title'>🏀 CourtVision AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>NBA & EuroLeague • High Accuracy AI Predictions</div>", unsafe_allow_html=True)

# --- Date Picker ---
selected_date = st.date_input(
    "📅 Select Date",
    datetime.date.today()
)

st.write("")
st.write(f"### 📌 Predictions for: **{selected_date.strftime('%Y/%m/%d')}**")
st.write("")

# --- AI Prediction Data ---
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

# --- Render Cards ---
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
