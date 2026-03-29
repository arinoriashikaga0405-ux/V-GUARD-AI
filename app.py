import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from PIL import Image

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# API KEY BAPAK
GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"

if GOOGLE_API_KEY:
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except:
        st.error("Koneksi AI Terputus.")

def get_foto(lebar):
    try:
        if os.path.exists('erwin.jpg'):
            return st.image(Image.open('erwin.jpg'), width=lebar)
        else:
            return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)
    except:
        st.write("📸")

# 2. STATUS LOGIN
if 'role' not in st.session_state:
    st.session_state.role = None

def login_vguard():
    st.sidebar.markdown("---")
    with st.sidebar.form("login_form"):
        u = st.text_input("Username").strip().lower()
        p = st.text_input("Password", type="password").strip()
        if st.form_submit_button("Masuk"):
            if u == "admin" and p == "Vguard2026":
                st.session_state.role = "admin"
                st.rerun()
            elif u == "klien" and p == "User2026":
                st.session_state.role = "klien"
                st.rerun()

# 3. CSS UNTUK TAMPILAN PROFESIONAL (UKURAN KOTAK PAS)
st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    .hero-bg { background: #0e1117; padding: 25px; border-radius: 15px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 30px; }
    
    .card-v { 
        background: white; padding: 20px; border-radius: 12px; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 6px solid #FFD700; 
        height: 520px; display: flex; flex-direction: column; justify-content: space-between;
    }
    .card-v h4 { font-size: 20px; color: #1a1a1a; margin-bottom: 5px; font-weight: 800; text-align: center; }
    .card-v .price { font-size: 26px; color: #d42f2f; font-weight: bold; text-align: center; margin-bottom: 10px; }
    .card-v .section-title { font-size: 13px; font-weight: bold; color: #888; text-transform: uppercase; margin-top: 10px; border-bottom: 1px solid #eee; }
    .card-v p { font-size: 14px; color: #444; margin: 5px 0; line-height: 1.4; }
    .card-v ul { font-size: 13px; color: #555; padding-left: 15px; margin: 5px 0; }
    
    .stLinkButton button { width: 100%; height: 45px; font-size: 15px !important; font-weight: bold; background-color: #FFD700 !important; color: #000 !important; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

# 4. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    col_x, col_y = st.columns([1, 2])
    with col_x: get_foto(65)
    with col_y: st.markdown("<b>Erwin Sinaga</b><br><small>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    menu = st.radio("NAVIGASI:", ["🌐 Beranda", "📝 Meeting Lab", "📊 Dashboard", "🤖 Admin"])
    if not st.session_state.role: login_vguard()
    else:
        if st.button("🚪 Keluar"):
            st.session_state.role = None
            st.rerun()

# 5. HALAMAN BERANDA
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence for SMEs</p></div>', unsafe_allow_html=True)
    
    WA = "https://wa.me/6282122190885"
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown(f"""<div class="card-v">
            <h4>🌱 V-START</h4>
            <div class="price">3,5 Jt /Bln</div>
            <div class="section-title">Deskripsi</div>
            <p>Sistem audit otomatis mandiri untuk validasi kas harian.</p>
            <div class="section-title">Fitur Utama</div>
            <ul><li>Cek Stok & Kas</li><li>Laporan Mingguan</li><li>AI Basic Fraud Scan</li></ul>
            <div class="section-title">Target Market</div>
            <p>UMKM Mikro, Toko Tunggal, Kedai Kopi Kecil.</p>
        </div>""", unsafe_allow_html=True)
        st.link_button("PILIH PAKET", WA)

    with c2:
        st.markdown(f"""<div class="card-v">
            <h4>📦 V-LITE</h4>
            <div class="price">7,5 Jt /Bln</div>
            <div class="section-title">Deskripsi</div>
            <p>Monitoring aktif untuk pemilik bisnis yang tidak di lokasi.</p>
            <div class="section-title">Fitur Utama</div>
            <ul><li>Laporan Real-time WA</li><li>Integrasi POS</li><li>1 Outlet Premium</li></ul>
            <div class="section-title">Target Market</div>
            <p>Retailer, Cafe Mandiri, Restoran Keluarga.</p>
        </div>""", unsafe_allow_html=True)
        st.link_button("PILIH PAKET", WA)

    with c3:
        st.markdown(f"""<div class="card-v" style="border: 2px solid #FFD700;">
            <h4>🚀 V-PRO</h4>
            <div class="price">15 Jt /Bln</div>
            <div class="section-title">Deskripsi</div>
            <p>Solusi komprehensif untuk mendeteksi pola kecurangan sistemik.</p>
            <div class="section-title">Fitur Utama</div>
            <ul><li>Deep Fraud Audit AI</li><li>Hingga 5 Outlet</li><li>Analisis Perilaku Kasir</li></ul>
            <div class="section-title">Target Market</div>
            <p>Franchise, Bisnis Multi-cabang, Restoran Besar
