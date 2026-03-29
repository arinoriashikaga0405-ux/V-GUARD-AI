import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Executive Profile", page_icon="🛡️", layout="wide")

# --- 2. CSS CUSTOM EKSEKUTIF ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stApp { color: #1e293b; }
    .header-box { text-align: center; padding: 15px 0; }
    .main-title { font-size: 3rem !important; font-weight: 800; color: #1e3a8a; margin-bottom: 0; }
    .mission-box { 
        background-color: #ffffff; padding: 20px; border-radius: 12px; 
        border-left: 8px solid #1e3a8a; box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
        text-align: center; margin: 20px auto; max-width: 900px;
    }
    .card-paket {
        background-color: #ffffff; padding: 20px; border-radius: 15px; 
        border: 1px solid #e2e8f0; height: 380px; transition: 0.3s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .card-paket:hover { transform: translateY(-5px); box-shadow: 0 10px 15px rgba(0,0,0,0.1); }
    .roi-calc-box {
        background-color: #f1f5f9; padding: 25px; border-radius: 15px;
        border: 2px solid #1e3a8a; margin-top: 20px;
    }
    .stButton>button { background-color: #1e3a8a; color: white; border-radius: 8px; width: 100%; font-weight: bold; height: 3.5em; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (Foto Tetap Kecil 70px) ---
with st.sidebar:
    try:
        st.image("erwin.jpg", width=70) 
    except:
        st.write("👤 PROFILE CEO")
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI Systems")
    st.write("---")
    menu = st.radio("NAVIGASI", ["Beranda Eksekutif", "Dashboard Performa", "AI Scanner"])

# --- 4. LOGIKA MENU ---
if menu == "Beranda Eksekutif":
    # Header & Misi
    st.markdown('<div class="header-box"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="mission-box"><p style="font-size:1.4rem; font-style:italic; color:#1e3a8a; margin:0;">"Digitizing Trust, Eliminating Leakage"</p></div>', unsafe_allow_html=True)

    # Profil & Filosofi (Narasi Ekspansif dengan Pengalaman 10 Tahun Perbankan)
    st.write("---")
    col_img, col_txt = st.columns([1, 4])
    with col_img:
        try:
            st.image("erwin.jpg", width=130) 
        except:
            st.info("Upload foto erwin.jpg")
    with col_txt:
        st.markdown("### PROFIL & VISI STRATEGIS")
        st.write("""
        Saya **Erwin**, Founder dan CEO VGUARD AI Systems, membawa lebih dari **10 tahun pengalaman profesional di industri perbankan** dalam membangun fondasi sistem keamanan ini. Dedikasi satu dekade di sektor finansial telah membentuk keahlian saya dalam manajemen risiko, kepatuhan, dan pengawasan aset yang ketat. Kini, visi saya adalah mentransformasikan standar keamanan perbankan tersebut ke dalam ekosistem bisnis Anda. Melalui integrasi teknologi AI masa depan, kami memastikan setiap transaksi terpantau dan setiap potensi kebocoran dapat dimitigasi secara instan sebelum berdampak pada profitabilitas Anda.
        """)
        st.markdown("### FILOSOFI PERISAI DIGITAL")
        st.write("""
        Filosofi VGUARD AI berakar pada prinsip integritas mutlak dan perlindungan aset total. Kami percaya bahwa kepercayaan bisnis dibangun di atas transparansi data. Terinspirasi dari ketatnya standar audit perbankan, kami hadir sebagai "Perisai Digital" yang bekerja 24/7 tanpa henti untuk mengawal integritas operasional bisnis Anda. Misi kami bukan sekadar menyediakan perangkat lunak, melainkan memberikan ketenangan pikiran (*peace of mind*) bagi para pimpinan perusahaan dalam mengelola ekspansi tanpa harus khawatir akan kebocoran finansial yang tersembunyi.
        """)

    # FITUR TETAP: KALKULATOR ROI INTERAKTIF (PERBAIKAN SINTAKS)
    st.write("---")
    st.markdown("### 📊 KALKULATOR ESTIMASI KERUGIAN & ROI")
    st.write("Gunakan alat analisis ini untuk melihat potensi dana yang dapat diselamatkan oleh VGUARD AI.")
    
    with st.container():
        st.markdown('<div class="roi-calc-box">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            omzet = st.number_input("Masukkan Omzet Bulanan Bisnis Anda (Rp)", min_value=0, value=100000000, step=1000000)
            leakage_rate = st.slider("Estimasi Persentase Kebocoran (%)", 1.0, 20.
