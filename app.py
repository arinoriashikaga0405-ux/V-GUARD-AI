import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. INITIALIZE SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems - CEO Erwin Sinaga", page_icon="🛡️", layout="wide")

# --- 3. CLEAN CSS (FIX SYNTAX ERROR) ---
st.markdown("""
<style>
    .stApp { background-color: white; }
    
    /* Header Tengah Baku */
    .header-center {
        display: flex; align-items: center; justify-content: center;
        gap: 15px; padding: 30px 0;
    }
    .main-title {
        color: #1e3a8a; font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 2.8em; font-weight: 800; margin: 0;
    }
    
    /* Profil Section */
    .profile-box { background: #f8fafc; padding: 25px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    
    /* Paket Layanan Strategis - 4 Kolom */
    .package-card { 
        background: white; padding: 25px; border-radius: 12px; border: 1px solid #e2e8f0; 
        text-align: center; height: 100%; display: flex; flex-direction: column; 
    }
    .pkg-name { color: #1e3a8a; font-size: 1.6em; font-weight: bold; margin-bottom: 5px; }
    .pkg-price { color: #1e3a8a; font-size: 2em; font-weight: bold; margin: 20px 0; }
    .wa-button { 
        display: block; background: #25d366; color: white !important; text-decoration: none !important; 
        padding: 12px; border-radius: 8px; font-weight: bold; text-align: center; margin-top: auto;
    }
</style>
""", unsafe_allow_html=True)

wa_number = "62821221190885"

# --- 4. BERANDA ---
if st.session_state.page == "Home":
    # HEADER TENGAH
    st.markdown("""
    <div class="header-center">
        <img src="https://cdn-icons-png.flaticon.com/512/1004/1004666.png" width="55">
        <h1 class="main-title">VGUARD AI SYSTEMS</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # SEKSI PROFIL
