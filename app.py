import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
from PIL import Image

# 1. KONFIGURASI HALAMAN UTAMA
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

# Fungsi Foto Profil
def get_foto(lebar):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try: return st.image(Image.open('erwin.jpg'), width=lebar)
        except: return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# 2. DESIGN CSS (SEMUA KOTAK PUTIH & PROPORSIONAL)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    [data-testid="stSidebar"] .stMarkdown b { color: white !important; }
    
    .hero-bg { background: #0e1117; padding: 25px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 25px; }
    
    /* DESAIN KOTAK LAYANAN (WARNA PUTIH & UKURAN PAS) */
    .card-v { 
        background: white; 
        padding: 18px; 
        border-radius: 12px; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); 
        border-top: 5px solid #FFD700; 
        height: 550px; 
        display: flex; 
        flex-direction: column; 
        justify-content: space-between;
    }
    
    .card-v h4 { font-size: 18px; font-weight: 800; color: #111; text-align: center; margin: 0; }
    .card-v .price { font-size: 22px; color: #d42f2f; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .card-v .section-label { font-size: 11px; font-weight: bold; color: #888; text-transform: uppercase; margin-top: 8px; border-bottom: 1px solid #eee; }
    .card-v p { font-size: 13px; color: #444; margin: 4px 0; line-height: 1.4; text-align: left; }
    .card-v ul { font-size: 13px; color: #444; margin: 4px 0; padding-left: 15px; text-align: left; }
    
    .stLinkButton button { width: 100%; background-color: #FFD700 !important; color: #000 !important; font-weight: bold; border-radius: 8px; border: none; height: 38px; font-size: 13px !important; }
    .fraud-card { background: #fff5f5; border-left: 5px solid #d42f2f; padding: 15px; border-radius: 8px; margin-bottom: 10px; color: #111; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (PROFIL & NAVIGASI)
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(65)
    with col_n: st.markdown("<b>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    nav_list = ["🌐 Beranda", "📝 Meeting Lab"]
    if st.session_state.role == "admin": nav_list.append("🤖 Panel Admin")
    elif st.session_state.role == "klien": nav_list.append("📊 Laporan Klien")
    else: nav_list.append("🔑 Masuk Ke Sistem")
    menu = st.radio("NAVIGASI:", nav_list)
    if st.session_state.role:
        if st.button("🚪 Logout"):
            st.session_state.role = None
            st.rerun()

# 4. LOGIKA HALAMAN
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(300)
    with c2:
        st.subheader("📊 Kalkulator Potensi Kerugian Operasional")
        omset = st.number_input("Omset Bulanan Bisnis (Rp):", value=100000000, step=10000000)
