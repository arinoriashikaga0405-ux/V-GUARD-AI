import streamlit as st
import pandas as pd
import hashlib
import time
import os
from datetime import datetime

# --- 1. CONFIG: KEAMANAN (CEO ONLY) ---
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

# --- 2. SETUP TEMA & LAYOUT ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# Custom CSS Premium Corporate
st.markdown("""
    <style>
    .main { background-color: #0a192f; color: #e6f1ff; }
    .stButton>button { background-color: #64ffda; color: #0a192f; font-weight: bold; border-radius: 8px; }
    .stMetric { background-color: #112240; padding: 15px; border-radius: 10px; border: 1px solid #233554; }
    h1, h2, h3 { color: #ccd6f6; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
st.sidebar.title("🛡️ V-GUARD MENU")
menu = st.sidebar.radio("Folder Navigasi:", [
    "🏠 Home (Founder Profil)", 
    "📜 Visi & Misi", 
    "📦 Produk & Layanan", 
    "🔑 Portal Klien (Upload Data)", 
    "🔐 Admin Panel (Restricted)"
])

# --- 📂 FOLDER 1: HOME ---
if menu == "🏠 Home (Founder Profil)":
    st.title("V-Guard AI Intelligence")
    st.divider()
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga - Founder & CEO", use_column_width=True)
        else:
            st.warning("⚠️ File 'erwin.jpg' tidak ditemukan di GitHub.")
            st.image("https://via.placeholder.com/400x500.png?text=Upload+erwin.jpg", use_column_width=True)
    with col2:
        st.header("Digitizing Trust, Eliminating Leakage")
        st.markdown("""
        Sebagai seorang **Senior Business Leader** dengan pengalaman lebih dari satu dekade di industri perbankan dan aset, 
        saya memahami bahwa musuh terbesar pertumbuhan bisnis bukanlah kompetisi, melainkan **ketidakpastian data dan kebocoran internal**. 

        Visi kami adalah menjadi standar global dalam **Digital Trust**. Melalui prinsip **'Digitizing Trust'**, 
        kami mengubah data mentah dari CCTV, mesin kasir, laporan stok (VCS), dan mutasi bank menjadi bukti otentik yang tidak dapat dimanipulasi.

        Misi utama kami, **'Eliminating Leakage'**, dijalankan dengan mengintegrasikan ekosistem AI tercanggih di dunia (Gemini, MindBridge, YOLO). 
        V-Guard AI mengembalikan kendali penuh ke tangan Anda, memberikan ketenangan pikiran, 
        dan memastikan setiap rupiah investasi Anda bekerja secara jujur dan optimal untuk masa depan bisnis Anda.
        """)
        st.caption("— **Erwin Sinaga**, Founder V-Guard AI Intelligence")

# --- 📂 FOLDER 2: VISI & MISI ---
elif menu == "📜 Visi & Misi":
    st.header("Filosofi & Strategi V-Guard")
    st.divider()
    st.subheader("🎯 Visi")
    st.info("Menjadi standar global dalam **Digital Trust** melalui transparansi data mutlak.")
    st.subheader("🚀 Misi")
    st.success("1. **Digitizing Trust:** Mengubah laporan manual menjadi data digital terverifikasi.\n\n2. **Eliminating Leakage:** Menghentikan kebocoran finansial dengan orkestrasi 9 AI Engine.")

# --- 📂 FOLDER 3: PRODUK & LAYANAN ---
elif menu == "📦 Produk & Layanan":
    st.header("4 Pilar Solusi V-Guard AI")
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        with st.expander("🟢 V-LITE (UMKM / Toko Mandiri)", expanded=True):
            st.markdown("- **AI Fraud Dasar:** Deteksi void mencurigakan.\n- **Laporan WA:** PDF setiap tanggal 1.\n- **Akses:** 1 User Pemilik.")
        with st.expander("🔵 V-PRO (Retail / Resto Menengah)", expanded=True):
            st.markdown("- **Real-Time Monitoring:** Notifikasi instan ke HP.\n- **VCS Integrasi:** Sinkronisasi Stok-Kasir-Bank.\n- **Audit Harian:** Laporan closing otomatis.")
    with c2:
        with st.expander("🟡 V-SIGHT (Keamanan Visual AI)", expanded=True):
            st.markdown("- **AI Behavior:** Baca gerak mencurigakan di CCTV.\n- **Visual Audit:** Cocokkan struk dengan rekaman video.\n- **Cloud Storage:** Rekaman aman tidak bisa dihapus.")
        with st.expander("🔴 V-ENTERPRISE (Korporasi / Franchise)", expanded=True):
            st.markdown("- **Centralized Dashboard:** Pantau ratusan cabang.\n- **Digital Forensics:** Investigasi indikasi korupsi.\n- **Custom API:** Terhubung ke ERP internal.")

# --- 📂 F
