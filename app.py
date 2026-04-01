import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database Klien (Session State)
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

# 2. CSS CUSTOM (Alarm Fraud & Notifikasi Piutang)
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    
    /* ALARM FRAUD BERKEDIP (> 1 JUTA) */
    .fraud-alert { 
        background: #f8d7da; color: #721c24; padding: 20px; border-radius: 10px; 
        border-left: 10px solid #dc3545; font-weight: bold; 
        animation: blinker 1s linear infinite; margin-bottom: 15px;
    }
    
    /* NOTIFIKASI PIUTANG */
    .piutang-box {
        background: #fff3cd; color: #856404; padding: 15px; border-radius: 10px;
        border-left: 10px solid #ffc107; margin-bottom: 10px; font-weight: bold;
    }
    
    @keyframes blinker { 50% { opacity: 0.2; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Capture", 
        "5. 🔐 Admin Control Center",
        "6. 📜 Laporan Audit Klien"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- MENU 5: ADMIN CONTROL CENTER (FITUR LENGKAP) ---
if menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Control")
    pw = st.text_input("Sandi Otoritas:", type="password")
    
    if pw == "w1nbju8282":
        df = pd.DataFrame(st.session_state.db_nasabah)
        
        # A. FITUR TAMBAH AKUN KLIEN BARU (INPUT MANUAL ADMIN)
        with st.expander("➕ TAMBAH AKUN KLIEN BARU (Input Langsung)"):
            with st.form("admin_add_client"):
                col1, col2 = st.columns(2)
                new_pic = col1.text_input("Nama PIC:")
                new_bisnis = col1.text_input("Nama Bisnis/Perusahaan:")
                new_paket = col2.selectbox("Paket Layanan:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
                new_harga = col2.number_input("Nilai Investasi (Rp):", value
