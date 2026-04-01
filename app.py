import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database Klien
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {
            "ID": 101, 
            "Waktu": "2026-03-25 08:00", 
            "Pelanggan": "Siska", 
            "Bisnis": "Cafe Maju", 
            "Paket": "MEDIUM", 
            "Harga": 7500000, 
            "Status": "🟢 AKTIF", 
            "Jatuh_Tempo": "2026-04-25",
            "Log": "System Initialized"
        }
    ]

# 2. CSS CUSTOM PREMIUM (Tampilan Bersih & Rapi)
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .finance-card { background: #f8f9fa; padding: 20px; border-radius: 12px; border: 1px solid #dee2e6; text-align: center; }
    .audit-card { background: #ffffff; padding: 15px; border-radius: 10px; border-left: 5px solid #6c757d; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .fraud-alert { background: #f8d7da; color: #721c24; padding: 15px; border-radius: 8px; border-left: 5px solid #dc3545; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0.5; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● System Online</p>', unsafe_allow_html=True)
    menu = st.radio("Navigasi:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Capture", 
        "5. 🔐 Admin Control Center",
        "6. 📜 Laporan Audit Klien"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.markdown("""<div class="profile-box">
        <b>B
