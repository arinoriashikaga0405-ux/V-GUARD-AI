import streamlit as st
import pandas as pd
import plotly.express as px
import os
import uuid
from datetime import datetime

# 1. KONFIGURASI HALAMAN & CSS BIAR RINGKAS & SEJAJAR
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

st.markdown("""
<style>
    .price-card {
        background-color: #f8f9fa;
        border-radius: 15px;
        padding: 15px; /* Padding diperkecil */
        border: 1px solid #e0e0e0;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        height: 400px; /* Tinggi kotak diperkecil dari 520px */
        display: flex;
        flex-direction: column;
        transition: 0.2s;
    }
    .price-card:hover {
        transform: translateY(-3px); /* Efek melayang diperkecil */
        border-color: #ff4b4b;
    }
    .package-title { font-size: 18px; font-weight: bold; color: #1f1f1f; margin-bottom: 2px; }
    .price-text { font-size: 20px; font-weight: bold; color: #ff4b4b; margin-bottom: 0px; }
    .monthly-text { font-size: 13px; color: #666; margin-bottom: 10px; }
    .feature-text { font-size: 12px; color: #444; flex-grow: 1; line-height: 1.4; }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 2. DATA MASTER PAKET (Fitur Disingkat)
pkgs = {
    "MIKRO": {
        "N": "Basic Guard", "S": "2.5jt", "M": "500rb",
        "F": ["✅ AI Fraud Dasar", "✅ Email Support", "✅ Laporan Mingguan", "✅ Dashboard Standar"]
    },
    "MENENGAH": {
        "N": "Premium Shield", "S": "7.5jt", "M": "1.5jt",
        "F": ["✅ AI Anomaly Detection", "✅ 🚨 Fitur Alarm", "✅ 🧾 Auto Invoice", "✅ WA Priority Support", "✅ Analisis Risiko Live"]
    },
    "ENTERPRISE": {
        "N": "Enterprise Vault", "S": "50jt", "M": "5jt",
        "F": ["✅ Full AI Integration", "✅ 🚨 Fitur Alarm", "✅ 🧾 Auto Invoice", "✅ 📹 CCTV AI", "✅ Audit Bulanan"]
    },
    "CORPORATE": {
        "N": "Elite Managed", "S": "85jt", "M": "10jt",
        "F": ["✅ Custom AI Training", "✅ 🚨 Fitur Alarm", "✅ 🧾 Auto Invoice", "✅ 📹 CCTV AI 24/7", "✅ Dedicated Engineer"]
    }
}

# 3. SIDEBAR NAVIGASI
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Pilih Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🏠 Home: Visi & Misi", 
        "3. 📦 Paket Solusi", 
        "4. 🔐 Admin Panel"
    ])
    st.write("---")

# --- 1. PROFIL FOUNDER (PERBAIKAN FOTO) ---
if menu == "1. 👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        # Menampilkan foto profil JIKA ada file erwin.jpg
        if os.path.exists("erwin.jpg"): 
            st.image("erwin.jpg", use_container_width=True)
        else: 
            # Menampilkan pesan error JIKA file foto tidak ditemukan
            st.error("Gagal memuat foto. Harap upload file 'erwin.
