import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Strategic Security", page_icon="🛡️", layout="wide")

# --- 2. CSS CUSTOM EKSEKUTIF ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stApp { color: #1e293b; }
    .header-box { text-align: center; padding: 20px 0; }
    .main-title { font-size: 3rem !important; font-weight: 800; color: #1e3a8a; margin-bottom: 0; }
    .mission-box { 
        background-color: #ffffff; padding: 20px; border-radius: 12px; 
        border-left: 8px solid #1e3a8a; box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
        margin: 20px auto; max-width: 900px; text-align: center;
    }
    .card-paket {
        background-color: #ffffff; padding: 20px; border-radius: 15px; 
        border: 1px solid #e2e8f0; height: 100%; transition: 0.3s;
    }
    .card-paket:hover { transform: translateY(-5px); box-shadow: 0 10px 15px rgba(0,0,0,0.1); }
    .stButton>button { background-color: #1e3a8a; color: white; border-radius: 8px; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (Foto Perkecil) ---
with st.sidebar:
    try:
        # Foto diperkecil ke 150px sesuai instruksi
        st.image("erwin.jpg", width=150)
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
    st.markdown('<div class="mission-box"><p style="font-size:1.4rem; font-style:italic; color:#1e3a8a; margin:0;">Digitizing Trust, Eliminating Leakage</p></div>', unsafe_allow_html=True)

    # Profil (Ukuran Foto Lebih Proporsional)
    st.write("---")
    col_img, col_txt = st.columns([1, 2.5])
    with col_img:
        try:
            st.image("erwin.jpg", use_container_width=True)
        except:
            st.info("Upload foto erwin.jpg")
    with col_txt:
        st.markdown("### STRATEGI PEMIMPIN")
        st.write("Saya **Erwin**, memimpin VGUARD AI untuk menghapus kebocoran operasional di Indonesia melalui integrasi kecerdasan buatan.")
        st.markdown("### FILOSOFI PERISAI")
        st.write("VGUARD AI adalah Audit Officer pribadi Anda yang bekerja 24 jam untuk mengamankan aset dan mencegah kerugian sistemik.")
