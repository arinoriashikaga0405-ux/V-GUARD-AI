import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")
wa_url = "https://wa.me/6282122190885"

# DATA PAKET (FORMAT RAPI)
pkgs = {
    "MIKRO": {"N": "Basic Guard", "S": "2.500.000", "M": "500.000"},
    "MENENGAH": {"N": "Premium Shield", "S": "7.500.000", "M": "1.500.000"},
    "ENTERPRISE": {"N": "Enterprise Vault", "S": "50.000.000", "M": "5.000.000"},
    "CORPORATE": {"N": "Elite Managed", "S": "85.000.000", "M": "10.000.000"}
}

# 2. SIDEBAR NAVIGASI (URUTAN SESUAI PERMINTAAN)
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Pilih Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🏠 Home: Visi & Misi", 
        "3. 📦 Paket Solusi", 
        "4. 🔐 Admin Panel"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI")

# --- NOMOR 1: PROFIL FOUNDER (CLEAN - TANPA WA) ---
if menu == "1. 👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): 
            st.image("erwin.jpg", use_container_width=True)
        else: 
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250)
    with r:
        st.subheader("Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        st.write("""
        Bapak Erwin Sinaga adalah Senior Business Leader visioner dengan pengalaman 10+ tahun sebagai CEO/CSO 
        di industri perbankan dan aset manajemen. Fokus beliau adalah membangun V-Guard AI sebagai 
        solusi 'End-to-End Intermediary' yang cerdas untuk melindungi bisnis dari fraud di pasar global 2026.
        """)

# --- NOMOR 2: HOME (VISI, MISI & ROI) ---
elif menu == "2. 🏠 Home: Visi & Misi":
    st.title("🛡️ Visi & Misi V-Guard AI")
    c_v, c_m = st.columns(2)
    with c_v:
        st.subheader("🎯 Visi")
        st.write("Menjadi perantara keamanan finansial berbasis AI terdepan yang mendemokratisasi proteksi aset untuk semua skala bisnis.")
    with c_m:
        st.subheader("🚀 Misi")
        st.write("Memberikan kepastian keamanan finansial kelas dunia bagi UMKM maupun Korporat melalui teknologi adaptif.")
    
    st.write("---")
    st.subheader("📈 Kalkulator ROI Penyelamatan Kerugian")
    n_tr = st.number_input("Total Transaksi/Bulan:", value=1000)
    v_tr = st.number_input("Rata-rata Nilai (Rp):", value=500000)
    f_p = st.slider("Asumsi Fraud (%):", 0.0, 5.0, 1.2)
    loss = (n_tr * v_tr) * (f_p / 100)
    st.error(f"Potensi Kerugian: Rp {loss:,.0f}")
    st.success(f"Penyelamatan V-Guard AI: Rp {loss * 0.99:,.0f}")

# --- NOMOR 3: PAKET SOLUSI (LAYOUT 2x2 AGAR RAPI) ---
elif menu == "3. 📦 Paket Solusi":
    st.title("📦 Paket Solusi & Layanan")
    st.write("Silakan pilih paket investasi keamanan yang sesuai.
