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
    h1, h2, h3 { color: #ccd6f6; font-family: 'Inter', sans-serif; }
    .sidebar .sidebar-content { background-image: linear-gradient(#0a192f, #112240); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION (FOLDER SISTEM) ---
st.sidebar.title("🛡️ V-GUARD MENU")
menu = st.sidebar.radio("Folder Navigasi:", [
    "🏠 Home (Founder Profil)", 
    "📜 Visi & Misi", 
    "📦 Produk & Layanan", 
    "🔑 Portal Klien (Upload Data)", 
    "🔐 Admin Panel (Restricted)"
])

# --- 📂 FOLDER 1: HOME (HALAMAN DEPAN) ---
if menu == "🏠 Home (Founder Profil)":
    st.title("V-Guard AI Intelligence")
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # Mencoba membaca file erwin.jpg dari repository GitHub
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga - Founder & CEO", use_column_width=True)
        else:
            st.warning("⚠️ File 'erwin.jpg' belum terdeteksi di GitHub.")
            st.image("https://via.placeholder.com/400x500.png?text=Unggah+erwin.jpg+ke+GitHub", use_column_width=True)
        
        st.info("📍 Berdomisili: Tangerang, Indonesia")

    with col2:
        st.header("Digitizing Trust, Eliminating Leakage")
        st.markdown(f"""
        Sebagai seorang **Senior Business Leader** dengan pengalaman lebih dari satu dekade di industri perbankan dan aset, 
        saya memahami bahwa musuh terbesar pertumbuhan bisnis bukanlah kompetisi, melainkan **ketidakpastian data dan kebocoran internal**. 
        Di dunia yang bergerak serba cepat, kepercayaan (trust) tidak lagi cukup jika hanya berdasarkan janji; kepercayaan harus bisa diukur, 
        diverifikasi, dan didigitalisasi. Inilah alasan saya mendirikan **V-Guard AI Intelligence**.

        Visi kami adalah menjadi standar global dalam **Digital Trust**. Kami percaya bahwa setiap pemilik bisnis—mulai dari tokoh retail 
        mandiri hingga korporasi multinasional—berhak mendapatkan transparansi mutlak atas aset mereka. Melalui prinsip **'Digitizing Trust'**, 
        kami mengubah data mentah dari CCTV, mesin kasir, laporan stok (VCS), dan mutasi bank menjadi bukti otentik yang tidak dapat dimanipulasi.

        Misi utama kami, **'Eliminating Leakage'**, dijalankan dengan mengintegrasikan ekosistem AI tercanggih di dunia (Gemini, MindBridge, YOLO). 
        Kami tidak hanya mendeteksi kecurangan saat sudah terjadi, tetapi membangun benteng pertahanan prediktif untuk menghentikan kebocoran 
        sebelum menjadi kerugian finansial. V-Guard AI mengembalikan kendali penuh ke tangan Anda, memberikan ketenangan pikiran (*peace of mind*), 
        dan memastikan setiap rupiah investasi Anda bekerja secara jujur dan optimal untuk masa depan bisnis Anda.
        """)
        st.caption("— **Erwin Sinaga**, Founder V-Guard AI Intelligence")

# --- 📂 FOLDER 2: VISI & MISI ---
elif menu == "📜 Visi & Misi":
    st.header("Filosofi & Strategi V-Guard")
    st.divider()
    st.subheader("🎯 Visi")
    st.info("Menjadi standar global dalam **Digital Trust** melalui transparansi data yang tidak dapat dimanipulasi.")
    
    st.subheader("🚀 Misi")
    st.success("1. **Digitizing Trust:** Mengubah aset fisik dan laporan manual menjadi data digital terverifikasi.\n"
               "2. **Eliminating Leakage:** Meng
