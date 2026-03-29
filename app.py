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

# INITIAL DATABASE SIMULATION
if 'role' not in st.session_state: st.session_state.role = None
if 'db_klien' not in st.session_state:
    st.session_state.db_klien = {
        "klien": {"paket": "V-LITE", "tagihan": 7500000, "due": "2026-04-05"}
    }

def get_foto(lebar):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try: return st.image(Image.open('erwin.jpg'), width=lebar)
        except: return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# 2. CSS STYLING EXECUTIVE
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .hero-bg { background: #0e1117; padding: 35px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 30px; }
    .bio-section { background: #0e1117; color: white; padding: 25px; border-radius: 15px; border-left: 6px solid #FFD700; }
    .card-v { background: white !important; padding: 22px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #FFD700; min-height: 400px; display: flex; flex-direction: column; justify-content: space-between; }
    .price { font-size: 1.2em; color: #FFD700; font-weight: bold; margin: 10px 0; }
    .red-alert { background: #ff4b4b; color: white; padding: 20px; border-radius: 10px; border: 3px solid black; text-align: center; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0.3; } }
    .invoice-warning { background: #fff3cd; color: #856404; padding: 15px; border-radius: 8px; border-left: 8px solid #ffcc00; margin-bottom: 15px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    f_col, n_col = st.columns([1, 2])
    with f_col: get_foto(65)
    with n_col: st.markdown(f"<b style='color:white;'>{st.session_state.get('user_name', 'Visitor')}</b><br><small style='color:#FFD700;'>V-GUARD Ecosystem</small>", unsafe_allow_html=True)
    st.divider()
    
    # DINAMIS MENU BERDASARKAN ROLE
    if st.session_state.role == "admin":
        menu = st.radio("FOUNDER MENU:", ["🌐 Beranda", "👥 Management Klien", "🤖 AI Fraud Scanner", "📝 Meeting Lab"])
    elif st.session_state.role == "klien":
        menu = st.radio("CLIENT DASHBOARD:", ["🌐 Beranda", "📊 Laporan Keamanan", "📅 Invoice & Payment"])
    else:
        menu = st.radio("VISITOR MENU:", ["🌐 Beranda", "🔑 Masuk Ke Sistem"])

    if st.session_state.role and st.button("🚪 Logout"):
        st.session_state.role = None
        st.session_state.user_name = "Visitor"
        st.rerun()

# 4. HALAMAN BERANDA (PROFIL & ROI)
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Mencegah Kerugian Owner Melalui Deteksi Proaktif</p></div>', unsafe_allow_html=True)
    c_img, c_txt = st.columns([1, 2])
    with c_img: get_foto(350)
    with c_txt:
        st.markdown('<div class="bio-section"><h3 style="color:#FFD700;">🛡️ About V-GUARD</h3><p>Platform deteksi fraud sistemik yang dibangun oleh <b>Erwin Sinaga</b> (Senior Business Executive). Pengalaman perbankan 10+ tahun kami gunakan untuk memproteksi aset bisnis Anda dari kebocoran hingga 90%.</p></div>', unsafe_allow_html=True)
    
    st.divider()
    st.subheader("📈 Kalkulator ROI Fraud")
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        omset = st.number_input("Omset Bulanan Bisnis (Rp):", value=100000000)
    with col_r2:
        saved = omset * 0.03 * 0.9 # Estimasi 3% kebocoran, 90% tertangani
        st.metric("Potensi Aset Terselamatkan /Bln", f"Rp {saved:,.0f}", "90% Proteksi AI")

# 5. HALAMAN MANAGEMENT KLIEN (KHUSUS PAK ERWIN/ADMIN)
elif menu == "👥 Management Klien":
    st.title("👥 Control Panel: Aktivasi Klien")
    with st.expander("➕ Tambah/Update Klien Baru"):
        new_
