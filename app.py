import streamlit as st
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG & KEAMANAN (LOCKED) ---
WHATSAPP_NUMBER = "6282122190885" 
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

if 'auth_vguard' not in st.session_state:
    st.session_state['auth_vguard'] = False

# --- 2. PREMIUM UI DESIGN (LOCKED) ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #1e293b; border-right: 1px solid #334155; }
    .product-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 20px; border-radius: 20px; border: 1px solid #334155;
        height: 100%; display: flex; flex-direction: column; justify-content: space-between;
    }
    .price-tag { color: #34d399; font-size: 24px; font-weight: bold; margin: 5px 0; }
    .feature-list { font-size: 12px; color: #cbd5e1; text-align: left; line-height: 1.5; }
    .wa-btn {
        display: block; text-align: center; background-color: #059669; color: white !important;
        padding: 10px; border-radius: 10px; text-decoration: none; font-weight: bold; margin-top: 15px;
    }
    .roi-container {
        background: #1e293b; padding: 30px; border-radius: 20px; 
        border: 1px solid #334155; margin-top: 40px;
    }
    .loss-alert { background-color: #fee2e2; color: #991b1b; padding: 15px; border-radius: 10px; font-weight: bold; margin-bottom: 10px; }
    .save-alert { background-color: #d1fae5; color: #065f46; padding: 15px; border-radius: 10px; font-weight: bold; }
    .visi-teks { line-height: 1.8; text-align: justify; color: #cbd5e1; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (LOCKED: NO ICON) ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg",
