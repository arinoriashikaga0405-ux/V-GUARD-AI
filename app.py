import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Executive Platform", page_icon="🛡️", layout="wide")

# Inisialisasi State Navigasi
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM EKSEKUTIF (DENGAN EFEK ALARM) ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .header-box { text-align: center; padding: 20px 0; }
    .main-title { font-size: 3rem !important; font-weight: 800; color: #1e3a8a; margin-bottom: 0; }
    .mission-box { 
        background-color: #ffffff; padding: 20px; border-radius: 12px; 
        border-left: 8px solid #1e3a8a; box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
        text-align: center; margin: 20px auto; max-width: 900px;
    }
    .card-paket {
        background-color: #ffffff; padding: 25px; border-radius: 15px; 
        border: 1px solid #e2e8f0; height: 420px; transition: 0.3s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02); text-align: center;
    }
    .card-paket:hover { transform: translateY(-5px); box-shadow: 0 10px 15px rgba(0,0,0,0.1); border-color: #ef4444; }
    .alarm-text { color: #ef4444; font-weight: bold; font-size: 0.9rem; }
    .feature-card {
        background-color: #ffffff; padding: 15px; border-radius: 10px;
        border-top: 4px solid #1e3a8a; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .roi-calc-box {
        background-color: #f1f5f9; padding: 25px; border-radius: 15px;
        border: 2px solid #1e3a8a; margin-top: 20px;
    }
    .stButton>button { background-color: #1e3a8a; color: white; border-radius: 8px; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    try:
        st.image("erwin.jpg", width=80) 
    except:
        st.write("👤 CEO PROFILE")
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI")
    st.write("---")
    if st.button("🏠 Beranda Utama"):
        st.session_state.page = "Home"
    st.write("---")
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 4. LOGIKA NAVIGASI ---

# A. PORTAL ADMIN (DENGAN FITUR ALARM)
if st.session_state.page == "Admin":
    st.title("💻 Command Center - Admin Audit")
    pwd = st.text_input("Kode Otoritas Admin", type="password")
    
    if pwd == "vguard2026":
        st.success("Akses Otoritas Diterima.")
        col_1, col_2 = st.columns([2, 1])
        with col_1:
            st.subheader("🔍 Scan Temuan")
            st.warning("🚨 [ALARM] Terdeteksi Selisih Kasir di Cabang Tangerang!")
            st.table(pd.DataFrame({'ID': ['TX-88'], 'Tipe': ['Void Massal'], 'Risiko': ['KRITIS']}))
        with col_2:
            st.subheader("🛠️ Quick Action")
            if st.button("🔔 Bunyikan Alarm Owner"):
                st.error("Notifikasi Darurat Terkirim!")

# B. PORTAL KLIEN
elif st.session_state.page == "Klien":
    st.title("📱 Owner Dashboard")
    st.metric("Total Profit Aman", "Rp 125M", "Protected by V-Guard")
    st.subheader("🔥 Log Fire Alarm (Temuan Mencurigakan)")
    st.info("Pesan Terakhir: [02:15 AM] Alarm Berbunyi - Void Manual Tanpa Otorisasi di Store 02.")

# C. BERANDA UTAMA
else:
    st.markdown('<div class="header-box"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)
    st.
