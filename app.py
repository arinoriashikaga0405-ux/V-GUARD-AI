import streamlit as st
import google.generativeai as genai
import os
import pandas as pd
import numpy as np
from PIL import Image
from datetime import datetime, timedelta

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

# 2. CSS STYLING EXECUTIVE (PROFIL + ALARM)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .hero-bg { background: #0e1117; padding: 35px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 30px; }
    .card-v { background: white !important; padding: 22px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #FFD700; min-height: 400px; display: flex; flex-direction: column; justify-content: space-between; }
    .bio-section { background: #0e1117; color: white; padding: 25px; border-radius: 15px; border-left: 6px solid #FFD700; }
    .price { font-size: 1.2em; color: #FFD700; font-weight: bold; margin: 10px 0; }
    .red-alert-box { background-color: #ff4b4b; color: white; padding: 20px; border-radius: 10px; border: 3px solid black; text-align: center; font-weight: bold; animation: blinker 1.2s linear infinite; margin-top: 20px; }
    @keyframes blinker { 50% { opacity: 0.3; } }
    .invoice-warning { background-color: #fff3cd; color: #856404; padding: 15px; border-radius: 8px; border-left: 8px solid #ffcc00; margin-bottom: 15px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    f_col, n_col = st.columns([1, 2])
    with f_col: get_foto(65)
    with n_col: st.markdown("<b style='color:white;'>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    nav_options = ["🌐 Beranda", "🤖 Panel Admin (Fraud Scan)", "📊 Monitoring Invoice", "📝 Meeting Lab"]
    if not st.session_state.role: nav_options.append("🔑 Masuk Ke Sistem")
    menu = st.radio("MENU UTAMA:", nav_options)
    if st.session_state.role and st.button("🚪 Logout"):
        st.session_state.role = None
        st.rerun()

# 4. HALAMAN BERANDA (DESAIN AWAL FULL)
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Mencegah Kerugian Owner Melalui Deteksi Proaktif</p></div>', unsafe_allow_html=True)
    c_img, c_txt = st.columns([1, 2])
    with c_img: get_foto(350)
    with c_txt:
        st.markdown('<div class="bio-section"><h3 style="color:#FFD700;">🛡️ About V-GUARD</h3><p>Didirikan pada 2026, <b>V-GUARD</b> berfokus pada deteksi fraud dan tata kelola AI bertanggung jawab. Dibangun oleh <b>Erwin Sinaga</b> dengan pengalaman perbankan 10+ tahun untuk mencegah kerugian owner hingga 90%.</p></div>', unsafe_allow_html=True)
    st.divider()
    p1, p2, p3, p4 = st.columns(4)
    WA = "https://
