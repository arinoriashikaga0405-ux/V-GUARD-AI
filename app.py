import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
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

# 2. CSS - METODE BARU (MENCEGAH ERROR TANDA PETIK)
st.markdown('<style>.stApp { background-color: #f4f6f9; }</style>', unsafe_allow_html=True)
st.markdown('<style>[data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }</style>', unsafe_allow_html=True)
st.markdown('<style>.hero-bg { background: #0e1117; padding: 30px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 30px; }</style>', unsafe_allow_html=True)
st.markdown('<style>.card-v { background: white !important; padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #FFD700; min-height: 520px; display: flex; flex-direction: column; justify-content: space-between; }</style>', unsafe_allow_html=True)
st.markdown('<style>.card-v h4 { color: #111; text-align: center; font-weight: 800; } .card-v .price { color: #d42f2f; font-weight: bold; text-align: center; font-size: 20px; }</style>', unsafe_allow_html=True)
st.markdown('<style>.stLinkButton button { width: 100%; background-color: #FFD700 !important; color: #000 !important; font-weight: bold; }</style>', unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    f_col, n_col = st.columns([1, 2])
    with f_col: get_foto(65)
    with n_col: st.markdown("<b style='color:white;'>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    nav = ["🌐 Beranda", "📝 Meeting Lab"]
    if st.session_state.role == "admin": nav.append("🤖 Panel Admin")
    elif st.session_state.role == "klien": nav.append("📊 Laporan Klien")
    else: nav.append("🔑 Masuk Ke Sistem")
    menu = st.radio("MENU UTAMA:", nav)
    if st.session_state.role:
        if st.button("🚪 Keluar"):
            st.session_state.role = None
            st.rerun()

# 4. HALAMAN UTAMA
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(300)
    with c2:
        st.subheader("📊 Analisis Potensi Penyelamatan")
        omset = st.number_input("Omset Bulanan (Rp):", value=100000000, step=10000000)
        leak = st.slider("Kebocoran (%):", 1,
