import streamlit as st
import pandas as pd
import hashlib
import time
import os
from datetime import datetime

# --- 1. CONFIG: KEAMANAN (CEO ONLY) ---
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

# --- 2. SETUP TEMA & LAYOUT ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# Custom CSS Premium Corporate
st.markdown("""
    <style>
    .main { background-color: #0a192f; color: #e6f1ff; }
    .stButton>button { background-color: #64ffda; color: #0a192f; font-weight: bold; border-radius: 8px; }
    .stMetric { background-color: #112240; padding: 15px; border-radius: 10px; border: 1px solid #233554; }
    h1, h2, h3 { color: #ccd6f6; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
st.sidebar.title("🛡️ V-GUARD MENU")
menu = st.sidebar.radio("Folder Navigasi:", [
    "🏠 Home (Founder Profil)", 
    "📜 Visi & Misi", 
    "📦 Produk & Layanan", 
    "🔑 Portal Klien (Upload Data)", 
    "🔐 Admin Panel (Restricted)"
])

# --- 📂 FOLDER 1: HOME ---
if menu == "🏠 Home (Founder Profil)":
    st.title("V-Guard AI Intelligence")
    st.divider()
    col1, col2 = st.columns([1, 2])
    with col1:
        if os
