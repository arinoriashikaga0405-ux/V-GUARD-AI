import streamlit as st
import pandas as pd
import numpy as np

# --- 1. KONFIGURASI HALAMAN ---
# Menggunakan VGUARD AI Systems sebagai judul tab
st.set_page_config(page_title="VGUARD AI Systems - Founder Erwin", page_icon="🛡️", layout="wide")

# --- 2. CSS CUSTOM UNTUK TAMPILAN EKSEKUTIF ---
st.markdown("""
    <style>
    /* Mengubah warna background halaman */
    .main { background-color: #f5f7f9; }
    
    /* Membuat kotak paket harga lebih menonjol */
    .stInfo, .stWarning, .stError, .stSuccess { border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    
    /* Tombol Kontak Kami di bagian bawah */
    .stButton>button { width: 100%; border-radius: 5px; height: 3.5em; background-color: #007bff; color: white; font-weight: bold;}
    
    /* Menghilangkan margin atas agar foto profil tidak terlalu jauh */
    .block-container { padding-top: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGASI (Fitur Tetap Lengkap) ---
# Sidebar dengan profil Bapak
with st.sidebar:
    try:
        # PENTING: Pastikan file 'erwin.jpg' ada di folder yang sama di GitHub
        st.image("erwin.jpg", width=200, caption="Erwin - Founder & CEO")
    except:
        st.write("👤 [Foto Erwin Belum Diupload]")

    st.title("🛡️ VGUARD AI")
    st.write("---")
    
    menu = st.sidebar.radio("Navigasi Sistem", [
        "Beranda & Profil CEO", 
        "Dashboard Performa (Demo)", 
        "AI Scanner Audit (Fitur Utama)", 
        "Laporan Audit (Demo)"
    ])

# --- 4. LOGIKA MENU (MENYATUKAN SEMUA KEINGINAN BAPAK) ---

if menu == "Beranda & Profil CEO":
    # HEADER BRANDING (Modern & Gagah)
    st.title("🛡️ VGUARD AI Systems")
    st.markdown("### *Intelligence for Your Business Security*")
    st.write("---")

    # BAGIAN 1: MISI BAPAK (Posisikan Paling Atas agar Klien Langsung Tahu)
    st.write("#### MISI KAMI")
    # Menampilkan Misi di kotak biru yang mencolok
    st.info('👉 "Digitizing Trust, Eliminating Leakage"')

    # BAGIAN 2: PROFIL & FILOSOFI BAPAK
    st.write("---")
    # Menggunakan layout kolom: Foto kiri, Profil kanan
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            # PENTING: File 'erwin.jpg' harus ada di folder yang sama di GitHub
            st.image("erwin.jpg", width=300)
        except:
            st.error("Gagal memuat foto erwin.jpg. Pastikan file ada di GitHub.")
    
    with col2:
        st.write("#### PROFIL FOUNDER & CEO")
        st.write("""
        Halo, saya **Erwin**, Founder dan CEO dari VGUARD AI Systems.
        Saya percaya bahwa fondasi utama dari pertumbuhan bisnis adalah kepercayaan dan keamanan operasional.
        """)
        
        st.write("#### FILOSOFI VGUARD AI Systems")
        st.write("""
        Kami bukan sekadar sistem keamanan, kami adalah **"Otak Digital"** yang bekerja 24 jam untuk melindungi aset Bapak.
        Filosofi kami adalah menghadirkan teknologi AI masa depan yang mudah digunakan, untuk mengamankan keuntungan dan mencegah kerugian secara sistemik.
        """)

    # BAGIAN 3: KATALOG 4 PAKET LANGGANAN (Mempertahankan 4 Kotak)
    st.write("---")
    st.write("### Pilih Solusi Keamanan Anda:")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.info("### V-START")
        st.write("**Investasi: Rp 2,5 Juta**")
        st.write("Maintenance: Rp 1 Juta/Bulan")
        st.write("🔹 Audit Harian Retail\n🔹 Notifikasi WA Bot\n🔹 Laporan Mingguan")
        # Bapak bisa tambahkan tombol Kontak di sini juga jika perlu
        # st.button("Pilih V-START", key="btn1")

    with c2:
