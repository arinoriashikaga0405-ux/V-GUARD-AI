import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Strategic Security", page_icon="🛡️", layout="wide")

# --- 2. CSS CUSTOM EKSEKUTIF ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stApp { color: #1e293b; }
    .header-box { text-align: center; padding: 15px 0; }
    .main-title { font-size: 3rem !important; font-weight: 800; color: #1e3a8a; margin-bottom: 0; }
    .mission-box { 
        background-color: #ffffff; padding: 20px; border-radius: 12px; 
        border-left: 8px solid #1e3a8a; box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
        text-align: center; margin: 20px auto; max-width: 900px;
    }
    .card-paket {
        background-color: #ffffff; padding: 20px; border-radius: 15px; 
        border: 1px solid #e2e8f0; height: 350px; transition: 0.3s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .card-paket:hover { transform: translateY(-5px); box-shadow: 0 10px 15px rgba(0,0,0,0.1); }
    .stButton>button { background-color: #1e3a8a; color: white; border-radius: 8px; width: 100%; font-weight: bold; height: 3.5em; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (Foto Diperkecil) ---
with st.sidebar:
    try:
        # Foto diperkecil ke 120px sesuai instruksi agar proporsional
        st.image("erwin.jpg", width=120)
    except:
        st.write("👤 PROFILE CEO")
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI Systems")
    st.write("---")
    menu = st.radio("NAVIGASI", ["Beranda Eksekutif", "Dashboard Performa", "AI Scanner"])

# --- 4. LOGIKA MENU ---
if menu == "Beranda Eksekutif":
    # Header & Misi
    st.markdown('<div class="header-box"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="mission-box"><p style="font-size:1.4rem; font-style:italic; color:#1e3a8a; margin:0;">Digitizing Trust, Eliminating Leakage</p></div>', unsafe_allow_html=True)

    # Profil & Strategi (2 Kolom Rapi)
    st.write("---")
    col_img, col_txt = st.columns([1, 2.5])
    with col_img:
        try:
            st.image("erwin.jpg", use_container_width=True)
        except:
            st.info("Upload foto erwin.jpg")
    with col_txt:
        st.markdown("### STRATEGI PEMIMPIN")
        st.write("Saya Erwin, memimpin VGUARD AI untuk menghapus kebocoran operasional di Indonesia melalui integrasi kecerdasan buatan.")
        st.markdown("### FILOSOFI PERISAI")
        st.write("VGUARD AI adalah Audit Officer pribadi Anda yang bekerja 24 jam untuk mengamankan aset dan mencegah kerugian sistemik.")

    # ANALISIS ROI & ESTIMASI KERUGIAN
    st.write("---")
    st.markdown("### 🛡️ ANALISIS STRATEGIS & ROI")
    r1, r2 = st.columns(2)
    with r1:
        st.error("#### Estimasi Kerugian Tanpa AI")
        st.write("- **Kebocoran Transaksi**: 5-8% revenue hilang karena error manual.")
        st.write("- **Mismatch Stok**: 10-15% margin hilang akibat data tidak real-time.")
    with r2:
        st.success("#### Jaminan ROI VGUARD AI")
        st.write("- **Break Even Point**: Estimasi kembali modal dalam 3-6 bulan.")
        st.write("- **Efisiensi**: Memotong hingga 90% potensi fraud transaksi.")

    # LAYANAN PRODUK (4 Paket dengan Detail Fitur)
    st.write("---")
    st.write("### LAYANAN PRODUK & FITUR")
    p1, p2, p3, p4 = st.columns(4)
    
    with p1:
        st.markdown('<div class="card-paket"><b>V-START</b><h3 style="color:#1e3a8a">2.5 JT</h3><hr><p style="font-size:0.85rem; text-align:left;">• Audit Harian Retail<br>• Notifikasi WA Aktif<br>• Laporan Mingguan Dasar</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="card-paket"><b>V-GROW</b><h3 style="color:#1e3a8a">5 JT</h3><hr><p style="font-size:0.85rem; text-align:left;">• Semua Fitur V-START<br>• <b>AI Fraud Detection</b><br>• Integrasi Stok Otomatis</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="card-paket"><b>V-PRIME</b><h3 style="color:#1e3a8a">10 JT</h3><hr><p style="font-size:0.85rem; text-align:left;">• Semua Fitur V-GROW<br>• Audit Multi-Cabang<br>• <b>Prediksi Kerugian AI</b></p></div>', unsafe_allow_html=True)
    with p4:
        st.markdown('<div class="card-paket"><b>V-CUSTOM</b><h3 style="color:#1e3a8a">NE
