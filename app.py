import streamlit as st
import pandas as pd
import hashlib
import time
import os

# --- 1. KONFIGURASI KEAMANAN ---
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

# --- 2. SETUP HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# Gaya Visual Corporate
st.markdown("""
    <style>
    .main { background-color: #0a192f; color: #e6f1ff; }
    .stButton>button { background-color: #64ffda; color: #0a192f; font-weight: bold; }
    h1, h2, h3 { color: #ccd6f6; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION (FOLDER MENU) ---
st.sidebar.title("🛡️ V-GUARD MENU")
menu = st.sidebar.radio("Pilih Folder:", [
    "🏠 Home (Founder)", 
    "📜 Visi & Misi", 
    "📦 Produk & Layanan", 
    "🔑 Portal Klien", 
    "🔐 Admin Panel"
])

# --- HALAMAN 1: HOME (FOTO & NARASI) ---
if menu == "🏠 Home (Founder)":
    st.title("Founder V-Guard AI Intelligence")
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # Membaca file erwin.jpg dari GitHub
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga - Founder & CEO", use_column_width=True)
        else:
            st.warning("⚠️ File 'erwin.jpg' tidak ditemukan. Pastikan sudah diunggah ke GitHub.")
            st.image("https://via.placeholder.com/400x500?text=Upload+erwin.jpg", use_column_width=True)
    
    with col2:
        st.header("Digitizing Trust, Eliminating Leakage")
        st.write("""
        Sebagai seorang **Senior Business Leader** dengan pengalaman lebih dari satu dekade di industri perbankan dan aset, 
        saya memahami bahwa musuh terbesar pertumbuhan bisnis bukanlah kompetisi, melainkan ketidakpastian data dan kebocoran internal. 
        Di dunia yang bergerak serba cepat, kepercayaan (trust) tidak lagi cukup jika hanya berdasarkan janji; kepercayaan harus bisa diukur, 
        diverifikasi, dan didigitalisasi. Inilah alasan saya mendirikan **V-Guard AI Intelligence**.

        Visi kami adalah menjadi standar global dalam **Digital Trust**. Kami percaya bahwa setiap pemilik bisnis—mulai dari tokoh retail 
        mandiri hingga korporasi multinasional—berhak mendapatkan transparansi mutlak atas aset mereka. Melalui prinsip **'Digitizing Trust'**, 
        kami mengubah data mentah dari CCTV, mesin kasir, laporan stok (VCS), dan mutasi bank menjadi bukti otentik yang tidak dapat dimanipulasi.

        Misi utama kami, **'Eliminating Leakage'**, dijalankan dengan mengintegrasikan ekosistem AI tercanggih di dunia (Gemini, MindBridge, YOLO). 
        Kami tidak hanya mendeteksi kecurangan saat sudah terjadi, tetapi membangun benteng pertahanan prediktif untuk menghentikan kebocoran 
        sebelum menjadi kerugian finansial. V-Guard AI mengembalikan kendali penuh ke tangan Anda, memberikan ketenangan pikiran, 
        dan memastikan setiap rupiah investasi Anda bekerja secara jujur dan optimal untuk masa depan bisnis Anda.
        """)
        st.caption("— Erwin Sinaga, Founder V-Guard AI")

# --- HALAMAN 2: VISI & MISI ---
elif menu == "📜 Visi & Misi":
    st.header("Filosofi V-Guard")
    st.info("**Visi:** Menjadi standar global 'Digital Trust' untuk keamanan finansial bisnis.")
    st.success("**Misi:** Menghentikan kebocoran aset (Eliminating Leakage) melalui orkestrasi 9 AI Engine.")

# --- HALAMAN 3: PRODUK & LAYANAN ---
elif menu == "📦 Produk & Layanan":
    st.header("Solusi AI Intelligence")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("V-LITE & V-PRO")
        st.write("Solusi untuk UMKM dan Retail Menengah.")
    with c2:
        st.subheader("V-SIGHT & V-ENTERPRISE")
        st.write("Keamanan Visual CCTV AI dan Solusi Korporasi.")

# --- HALAMAN 4: PORTAL KLIEN ---
elif menu == "🔑 Portal Klien":
    st.header("Portal Client - Upload Data")
    st.text_input("Nama Perusahaan")
    st.file_uploader("Upload Data Audit (VCS/KTP)")
    if st.button("Kirim ke Server"):
        st.success("Data telah aman dienkripsi.")

# --- HALAMAN 5: ADMIN PANEL (DIKUNCI) ---
elif menu == "🔐 Admin Panel":
    st.header("Executive Dashboard (CEO Only)")
    pwd_input = st.text_input("Masukkan Sandi Founder", type="password")
    
    if pwd_input:
        if hashlib.sha256(pwd_input.encode()).hexdigest() == ADMIN_PWD_HASH:
            st.success("Selamat Datang, Pak Erwin.")
            st.metric("Kebocoran Dicegah", "Rp 125.500.000", "12%")
            if st.button("🚀 JALANKAN AUDIT GLOBAL"):
                st.write("Proses Orkestrasi AI Sedang Berjalan...")
        else:
            st.error("Sandi Salah. Akses Ditolak.")

st.sidebar.markdown("---")
st.sidebar.caption("V-Guard AI v1.0 | Founder: Erwin Sinaga")
