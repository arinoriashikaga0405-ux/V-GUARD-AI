import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems - CEO Erwin Sinaga", page_icon="🛡️", layout="wide")

# --- 2. BAKU & PERMANEN CSS (ESTETIKA EKSEKUTIF) ---
# Saya kunci CSS ini agarvisual Beranda Utama tidak berubah tanpa persetujuan Bapak.
st.markdown("""
<style>
    .stApp { background-color: white; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; height: 45px; }
    
    /* Header Baku (Tengah) */
    .header-container { display: flex; align-items: center; justify-content: center; gap: 15px; margin-bottom: 30px; }
    .main-title { color: #1e3a8a; font-size: 2.5em; font-weight: bold; margin: 0; }
    
    /* Profil Section Baku */
    .profile-box { background: #f8fafc; padding: 25px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    
    /* Paket Layanan Strategis - Ramping & Baku (4 Kolom) */
    .package-card { 
        background: white; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; 
        text-align: center; height: 100%; display: flex; flex-direction: column; 
    }
    .pkg-name { color: #1e3a8a; font-size: 1.5em; font-weight: bold; margin-bottom: 10px; }
    .pkg-price { color: #1e3a8a; font-size: 1.8em; font-weight: bold; margin: 10px 0; }
    .pkg-feat { text-align: left; font-size: 0.9em; margin: 15px 0; min-height: 120px; flex-grow: 1; list-style-type: disc; padding-left: 20px;}
</style>
""", unsafe_allow_html=True)

wa_number = "62821221190885"

# --- 3. LOGIKA HALAMAN & STATE ---
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 4. HEADER & PROFIL (KONSEP BAKU) ---
if st.session_state.page == "Home":
    # Header Logo & Judul (Tengah)
    st.markdown("""
    <div class="header-container">
        <img src="https://cdn-icons-png.flaticon.com/512/1004/1004666.png" width="40">
        <h1 class="main-title">VGUARD AI SYSTEMS</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Kolom Profil
    with st.container():
        c1, c2 = st.columns([1, 2.5])
        with c1:
            # Foto Profil (Aset baku Bapak)
            st.image("https://cdn-icons
