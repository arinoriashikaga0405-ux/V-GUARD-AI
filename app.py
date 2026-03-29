import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Executive Platform", page_icon="🛡️", layout="wide")

# Inisialisasi State Navigasi
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM EKSEKUTIF ---
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
        border: 1px solid #e2e8f0; height: 440px; transition: 0.3s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02); text-align: center;
    }
    .card-paket:hover { transform: translateY(-5px); box-shadow: 0 10px 15px rgba(0,0,0,0.1); border-color: #ef4444; }
    .alarm-tag { 
        background-color: #fee2e2; color: #ef4444; padding: 5px 12px; 
        border-radius: 20px; font-size: 0.8rem; font-weight: bold; border: 1px solid #fecaca;
        display: inline-block; margin-top: 15px;
    }
    .feature-card {
        background-color: #ffffff; padding: 15px; border-radius: 10px;
        border-top: 4px solid #1e3a8a; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
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
        st.rerun()
    st.write("---")
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 4. LOGIKA NAVIGASI ---

if st.session_state.page == "Admin":
    st.title("💻 Command Center - Admin Audit")
    pwd = st.text_input("Kode Otoritas Admin", type="password")
    if pwd == "vguard2026":
        st.success("Akses Otoritas Diterima.")
        st.subheader("🔍 Scan Temuan Mencurigakan")
        st.warning("🚨 [ALARM] Deteksi Anomali Transaksi di Store 01!")
        if st.button("🔔 Kirim Fire Alarm ke Owner"):
            st.error("Alarm Berhasil Dikirim!")
    elif pwd != "":
        st.error("Kode Salah!")

elif st.session_state.page == "Klien":
    st.title("📱 Owner Dashboard")
    st.metric("Total Profit Aman", "Rp 125.000.000", "Protected")
    st.subheader("🔥 Log V-Guard Fire Alarm")
    st.info("Log: [02:15 AM] Alarm Berbunyi - Upaya Manipulasi Void Terdeteksi.")

else:
    # --- HALAMAN UTAMA ---
    st.markdown('<div class="header-box"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="mission-box"><p style="font-size:1.4rem; font-style:italic; color:#1e3a8a; margin:0;">"Digitizing Trust, Eliminating Leakage"</p></div>', unsafe_allow_html=True)

    # Profil (10 Tahun Bank)
    st.write("---")
    c_img, c_txt = st.columns([1, 4])
    with c_img:
        try: st.image("erwin.jpg", width=140)
        except: st.info("CEO Photo")
    with c_txt:
        st.markdown("### FOUNDER PROFILE & FILOSOFI")
        st.write("""
        Saya **
