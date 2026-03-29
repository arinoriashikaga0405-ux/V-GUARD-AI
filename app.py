import streamlit as st
import google.generativeai as genai
import os
import pandas as pd
from PIL import Image
from datetime import datetime, timedelta

# 1. KONFIGURASI HALAMAN UTAMA
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# API KEY GEMINI
GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Koneksi AI Terputus.")

# INITIAL DATABASE SIMULATION
if 'role' not in st.session_state: st.session_state.role = None
if 'user_name' not in st.session_state: st.session_state.user_name = "Visitor"
if 'user_id' not in st.session_state: st.session_state.user_id = None
if 'db_klien' not in st.session_state:
    st.session_state.db_klien = {
        "klien_demo": {"paket": "V-LITE", "tagihan": 7500000, "due": "2026-04-05"}
    }

def get_foto(lebar):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    # Mengutamakan foto Bapak jika ada di folder
    if os.path.exists('erwin.jpg'):
        try: return st.image(Image.open('erwin.jpg'), width=lebar)
        except: return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# 2. CSS STYLING EXECUTIVE (BLACK & GOLD)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .hero-bg { background: #0e1117; padding: 40px; border-radius: 12px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px; }
    .bio-section { background: #1a1c23; color: white; padding: 30px; border-radius: 15px; border-left: 8px solid #FFD700; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    .red-alert { background: #ff4b4b; color: white; padding: 20px; border-radius: 10px; border: 3px solid black; text-align: center; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0.3; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    f_col, n_col = st.columns([1, 2])
    with f_col: get_foto(70)
    with n_col: 
        st.markdown(f"<b style='color:white;'>{st.session_state.user_name}</b><br><small style='color:#FFD700;'>V-GUARD Ecosystem</small>", unsafe_allow_html=True)
    st.divider()
    
    # Navigasi Dinamis
    if st.session_state.role == "admin":
        menu = st.radio("FOUNDER MENU:", ["🌐 Beranda", "👥 Management Klien", "🤖 AI Fraud Scanner"])
    elif st.session_state.role == "klien":
        menu = st.radio("CLIENT DASHBOARD:", ["🌐 Beranda", "📅 Invoice & Payment"])
    else:
        menu = st.radio("VISITOR MENU:", ["🌐 Beranda", "🔑 Masuk Ke Sistem"])

    if st.session_state.role and st.button("🚪 Logout"):
        st.session_state.role = None
        st.session_state.user_name = "Visitor"
        st.session_state.user_id = None
        st.rerun()

# 4. HALAMAN BERANDA (PROFIL & FILOSOFI)
if menu == "🌐 Beranda":
    # Header Utama
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p style="font-size: 1.2em; color: #FFD700;">Mencegah Kerugian Owner Melalui Deteksi Proaktif</p></div>', unsafe_allow_html=True)
    
    # Section Profil & About
    c_img, c_txt = st.columns([1, 2])
    with c_img:
        # Menampilkan foto Bapak yang ada di screenshot
        get_foto(380)
    with c_txt:
        st.markdown(f"""
        <div class="bio-section">
            <h2 style="color:#FFD700;">🛡️ About V-GUARD</h2>
            <p style="font-size: 1.1em; line-height: 1.6;">
                <b>V-GUARD</b> adalah platform deteksi fraud dan tata kelola AI bertanggung jawab. 
                Dibangun oleh <b>Erwin Sinaga</b> dengan pengalaman perbankan 10+ tahun untuk mencegah kerugian owner hingga 90%.
            </p>
            <hr style="border-color: #444;">
            <h3 style="color:#FFD700;">Filosofi V-GUARD</h3>
            <p>
                Dengan pengalaman perbankan lebih dari 10 tahun, kami memastikan setiap rupiah aset Anda terlindungi. 
                Sistem kami dirancang untuk memberikan <b>Alarm Merah</b> seketika saat kecurangan terdeteksi.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Kalkulator ROI
    st.subheader("📈 Kalkulator ROI Fraud")
    col_1, col_2 = st.columns(2)
    with col_1:
        omset = st.number_input("Omset Bulanan Bisnis (Rp):", value=100000000, step=10000000)
    with col_2:
        saved = omset * 0.027 # Estimasi 2.7%
        st.metric("Pot
