import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
# Menggunakan VGUARD AI Systems sebagai judul tab
st.set_page_config(page_title="VGUARD AI Systems - Solusi Keamanan Strategis", page_icon="🛡️", layout="wide")

# --- 2. CSS CUSTOM UNTUK TAMPILAN GAGAH & DETAIL ---
st.markdown("""
    <style>
    /* Mengubah warna background halaman */
    .main { background-color: #f5f7f9; }
    
    /* Menyesuaikan Title agar lebih besar dan berbayang */
    .big-title { font-size: 3.5rem !important; font-weight: bold; color: #1a237e; text-shadow: 2px 2px 4px rgba(0,0,0,0.1); margin-bottom: 0px;}
    
    /* Mendesain Misi Box agar menonjol */
    .mission-box { background-color: #e8eaf6; padding: 20px; border-radius: 10px; border-left: 10px solid #1a237e; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin: 20px 0;}
    
    /* Mendesain 4 Kotak Paket Harga agar modern dan terukur */
    div.stInfo, div.stWarning, div.stError, div.stSuccess { border-radius: 10px; padding: 25px !important; box-shadow: 0 10px 15px rgba(0,0,0,0.05); transition: 0.3s; margin-bottom: 20px; text-align: center; color: black; }
    div.stInfo:hover, div.stWarning:hover, div.stError:hover, div.stSuccess:hover { box-shadow: 0 15px 20px rgba(0,0,0,0.1); transform: translateY(-5px); }
    
    /* List Fitur agar rapi */
    .feature-list { text-align: left; margin-top: 15px; font-size: 1rem; color: #333; line-height: 1.6;}
    
    /* Section ROI Modern */
    .roi-section { background-color: #ffffff; padding: 30px; border-radius: 15px; border: 1px solid #e0e0e0; margin-top: 40px; box-shadow: 0 4px 6px rgba(0,0,0,0.03);}
    .roi-title { font-size: 2rem !important; font-weight: bold; color: #1a237e; margin-bottom: 20px;}
    
    /* Tombol Kontak Kami di bagian bawah */
    .stButton>button { width: 100%; border-radius: 5px; height: 3.5em; background-color: #1a237e; color: white; font-weight: bold; font-size: 1.2rem;}
    .stButton>button:hover { background-color: #3949ab; color: white; border: none; }
    
    /* Menghilangkan margin atas agar foto profil tidak terlalu jauh */
    .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGASI (Fitur Tetap Lengkap) ---
with st.sidebar:
    # PERBAIKAN: Perkecil ukuran foto di sidebar (misal ke 150px)
    try:
        # PENTING: File 'erwin.jpg' harus ada di folder yang sama di GitHub
        st.image("erwin.jpg", width=150, caption="Erwin - Founder & CEO")
    except:
        st.write("👤 [Foto Erwin Belum Diupload]")

    st.title("🛡️ VGUARD AI")
    st.write("---")
    
    menu = st.sidebar.radio("Navigasi Sistem", [
        "Beranda Eksekutif", 
        "Dashboard Performa (Demo)", 
        "AI Scanner Audit (Fitur Utama)"
    ])

# --- 4. LOGIKA MENU (Edisi CEO yang Lebih Menjual) ---

if menu == "Beranda Eksekutif":
    # HEADER BRANDING
    st.markdown('<p class="big-title">🛡️ VGUARD AI Systems</p>', unsafe_allow_html=True)
    st.markdown("### *Intelligence for Your Business Security*")
    st.write("---")

    # BAGIAN 1: MISI BAPAK
    st.write("#### MISI KAMI")
    # Menampilkan Misi di kotak biru yang mencolok
    st.markdown('<div class="mission-box"><p style="font-size:1.5rem; font-style:italic; color:#1a237e; margin:0;">👉 "Digitizing Trust, Eliminating Leakage"</p></div>', unsafe_allow_html=True)

    # BAGIAN 2: PROFIL & FILOSOFI BAPAK (Mempertahankan 2 Kolom)
    st.write("---")
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            # PENTING: File 'erwin.jpg' harus ada di folder yang sama di GitHub
            # Gunakan use_container_width agar foto menyesuaikan kolom
            st.image("erwin.jpg", use_container_width=True)
        except:
            st.error("Gagal memuat foto erwin.jpg. Pastikan file ada di GitHub.")
    
    with col2:
        st.write("#### PROFIL FOUNDER & CEO")
        st.write("""
        Halo, saya **Erwin**, Founder dan CEO VGUARD AI Systems.
        Didirikan pada 2026, VGUARD AI lahir dari visi strategi untuk menghapus kebocoran operasional yang seringkali tidak terdeteksi 
        dan menggerogoti keuntungan bisnis di Indonesia. Kami tidak sekadar merekam, kami menganalisis dan menghadirkan intelijen 
        kepada Anda, para pemilik bisnis, agar dapat fokus pada ekspansi tanpa keraguan.
        """)
        
        st.write("#### FILOSOFI PERISAI")
        st.write("""
        Kami adalah Audit Officer pribadi Anda yang bekerja tanpa henti.
        Filosofi kami adalah menghadirkan teknologi AI masa depan yang mudah digunakan, untuk mengamankan aset Anda dan mencegah 
        kerugian secara sistemik. Kami mentransformasikan data menjadi ketenangan pikiran Anda.
        """)

    # BAGIAN 3: BARU - FITUR ROI & ESTIMASI KERUGIAN (The "Wow" Section)
    st.write("---")
    st.markdown('<div class="roi-section">', unsafe_allow_html=True)
    st.markdown('<p class="roi-title">🛡️ Mengapa Bisnis Anda Membutuhkan VGUARD AI?</p>', unsafe_allow_html=True)
    
    r1, r2 = st.columns(2)
    with r1:
        st.write("#### Estimasi Kerugian Tanpa AI Audit")
        st.error("""
        Tanpa sistem audit cerdas 24/7, bisnis Bapak rentan terhadap:
        - 💸 **Kerugian Transaksi Manual**: 5-8% revenue hilang karena *human error* atau fraud kecil tak terdeteksi.
        - 📦 **Kebocoran Stok (Inventory Leakage)**: 10-15% margin hilang karena mismatch stok yang tidak terlacak real-time.
        - 🛑 **Anomali Sistemik**: Kerugian tak terduga yang dapat mencapai puluhan juta per tahun.
        """)
        
    with r2:
        st.write("#### Jaminan ROI VGUARD AI Systems")
        st.success("""
        **Sistem Kami Dijamin Membayar Dirinya Sendiri**
        Dalam 3-6 Bulan pertama, VGUARD AI ditargetkan mengembalikan investasi Bapak:
        - 🚀 **Penghematan Langsung**: AI Audit kami memotong 90% kebocoran transaksi di paket V-GROW/V-PRIME.
        -
