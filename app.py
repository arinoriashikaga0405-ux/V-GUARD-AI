import streamlit as st
import google.generativeai as genai
import os
import pandas as pd
import numpy as np
from PIL import Image

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# API KEY GEMINI
GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Koneksi AI Terputus.")

if 'role' not in st.session_state:
    st.session_state.role = None

def get_foto(lebar):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try: return st.image(Image.open('erwin.jpg'), width=lebar)
        except: return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# 2. CSS STYLING (VERSI STABIL)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .hero-bg { background: #0e1117; padding: 35px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 30px; }
    .card-v { background: white !important; padding: 22px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #FFD700; min-height: 400px; display: flex; flex-direction: column; justify-content: space-between; }
    .bio-section { background: #0e1117; color: white; padding: 25px; border-radius: 15px; border-left: 6px solid #FFD700; }
    .fraud-panel { background: #ffffff; padding: 25px; border-radius: 12px; border: 2px solid #d42f2f; margin-top: 20px; color: #111; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    f_col, n_col = st.columns([1, 2])
    with f_col: get_foto(65)
    with n_col: st.markdown("<b style='color:white;'>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    nav = ["🌐 Beranda", "🤖 Panel Admin (Fraud Detection)", "📊 Laporan Klien", "📝 Meeting Lab"]
    if not st.session_state.role: nav.append("🔑 Masuk Ke Sistem")
    menu = st.radio("MENU UTAMA:", nav)
    if st.session_state.role:
        if st.button("🚪 Logout"):
            st.session_state.role = None
            st.rerun()

# 4. HALAMAN BERANDA
if menu == "
