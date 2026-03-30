import streamlit as st
import pandas as pd
import plotly.express as px
import os
import uuid
from datetime import datetime
import time

# 1. KONFIGURASI HALAMAN PREMIUM
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")
wa_url = "https://wa.me/6282122190885"

# 2. INISIALISASI DATA & SESSION
if 'client_queue' not in st.session_state: 
    st.session_state.client_queue = []
if 'auth' not in st.session_state: 
    st.session_state.auth = False

pkgs = {
    "MIKRO": {"N": "Basic Guard", "S": 2500000, "M": 500000},
    "MENENGAH": {"N": "Premium Shield", "S": 7500000, "M": 1500000},
    "ENTERPRISE": {"N": "Enterprise Vault", "S": 50000000, "M": 5000000},
    "CORPORATE": {"N": "Elite Managed", "S": 85000000, "M": 10000000}
}

# 3. SIDEBAR NAVIGASI
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Menu Utama:", ["🏠 Home & ROI", "📦 Produk & Antrean", "👤 Profil", "🔐 Admin Panel"])
    st.write("---")
    st.caption("v1.2 Stable | © 2026")

# --- HALAMAN 1: HOME & ROI ---
if menu == "🏠 Home & ROI":
    st.title("🛡️ V-Guard AI: Strategic Security")
    st.markdown("### Kalkulator ROI & Penyelamatan Kerugian")
    st.write("Gunakan simulasi ini untuk melihat potensi penghematan bisnis Anda.")
    
    col_roi1, col_roi2 = st.columns([1, 1.5])
    with col_roi1:
        st.subheader("Input Data")
        num_trans = st.number_input("Transaksi/Bulan:", value=1000)
        avg_val = st.number_input("Rata-rata Nilai (Rp):", value=500000)
        fraud_p = st.slider("Asumsi Fraud (%):", 0.0, 5.0, 1.2)
        
        pot_loss = (num_trans * avg_val) * (fraud_p / 100)
        
    with col_roi2:
        st.subheader("Hasil Analisis")
        st.error(f"Potensi Kerugian/Bulan: Rp {pot_loss:,.0f}")
        st.success(f"Penyelamatan V-Guard (99%): Rp {pot_loss * 0.99:,.0f}")
        st.info("Investasi V-Guard jauh lebih kecil dibanding risiko kehilangan aset.")

# --- HALAMAN 2: PRODUK & INPUT ANTREAN ---
elif menu == "📦 Produk & Antrean":
    st.title("📦 Paket Solusi & Pengiriman Data")
    
    cols = st.columns(4)
    for i, (tier, data) in enumerate(pkgs.items()):
        with cols[i]:
            st.warning(f"**{tier}**")
            st.write(f"Setup: Rp {data['S']:,}")
