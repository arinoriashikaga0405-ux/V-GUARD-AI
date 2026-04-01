import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database dengan Logika Jatuh Tempo
if 'db_nasabah' not in st.session_state:
    today = datetime.now().date()
    st.session_state.db_nasabah = [
        {
            "ID": 101, "Tgl_Daftar": "2026-03-01", "Pelanggan": "Siska", 
            "Bisnis": "Cafe Maju", "Paket": "SMART", "Harga": 2500000, 
            "Jatuh_Tempo": (today + timedelta(days=5)).strftime("%Y-%m-%d"),
            "Status": "🟢 AKTIF", "Audit_Score": 98
        },
        {
            "ID": 102, "Tgl_Daftar": "2026-03-10", "Pelanggan": "Jaya", 
            "Bisnis": "Bengkel Berkah", "Paket": "BASIC", "Harga": 1500000, 
            "Jatuh_Tempo": (today + timedelta(days=15)).strftime("%Y-%m-%d"), 
            "Status": "🟢 AKTIF", "Audit_Score": 95
        }
    ]
if 'admin_akses_terbuka' not in st.session_state:
    st.session_state.admin_akses_terbuka = False

WA_NUMBER = "628212190885"
ADMIN_PASSWORD = "w1nbju8282"

def format_rp(angka):
    try:
        return f"Rp {float(angka):,.0f}".replace(",", ".")
    except:
        return str(angka)

# 2. CSS CUSTOM (FIXED UI)
st.markdown("""
<style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; font-size: 12px; }
    .fraud-alarm { background-color: #ff4b4b; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; animation: blinker 1.5s linear infinite; margin-bottom: 10px; border: 2px solid yellow; }
    @keyframes blinker { 50% { opacity: 0.6; } }
    .invoice-notif { background-color: #fff3cd; color: #856404; padding: 10px; border-radius: 5px; border-left: 5px solid #ffc107; margin-bottom: 5px; font-size: 14px; }
    .vcs-card { background: #f0f7ff; padding: 20px; border-radius: 10px; border: 1px solid #1E3A8A; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (NAVIGASI TERKUNCI)
with st.sidebar:
    st.markdown("<h1 style='color: #1E3A8A; text-align: center;'>🛡️ V-GUARD AI</h1>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", use_container_width=True)
        st.markdown(f"<p style='text-align:center;'><b>Erwin Sinaga</b><br>Senior Business Leader</p>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("Menu Utama:", ["1. 👤 Profil", "2. 🎯 Visi & ROI", "3. 📦 Paket", "4. 📝 Registrasi", "5. 🔐 Admin"])
    st.write("---")
    st.link_button("💬 Chat Support", f"https://wa.me/{WA_NUMBER}")
