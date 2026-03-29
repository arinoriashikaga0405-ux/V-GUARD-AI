import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - ROI Calculator", page_icon="🛡️", layout="wide")

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
        border: 1px solid #e2e8f0; height: 380px; transition: 0.3s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .card-paket:hover { transform: translateY(-5px); box-shadow: 0 10px 15px rgba(0,0,0,0.1); }
    .roi-calc-box {
        background-color: #f1f5f9; padding: 25px; border-radius: 15px;
        border: 2px solid #1e3a8a; margin-top: 20px;
    }
    .stButton>button { background-color: #1e3a8a; color: white; border-radius: 8px; width: 100%; font-weight: bold; height: 3.5em; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (Foto Diperkecil Maksimal) ---
with st.sidebar:
    try:
        # Foto diperkecil ke 100px agar sangat rapi di navigasi
        st.image("erwin.jpg", width=100)
    except:
        st.write("👤 CEO PROFILE")
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI Systems")
    st.write("---")
    menu = st.radio("NAVIGASI", ["Beranda Eksekutif", "Dashboard Performa", "AI Scanner"])

# --- 4. LOGIKA MENU ---
if menu == "Beranda Eksekutif":
    # Header & Misi
    st.markdown('<div class="header-box"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="mission-box"><p style="font-size:1.4rem; font-style:italic; color:#1e3a8a; margin:0;">Digitizing Trust, Eliminating Leakage</p></div>', unsafe_allow_html=True)

    # Profil & Strategi
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
        st.write("VGUARD AI adalah perisai digital yang bekerja 24 jam untuk mengamankan aset dan mencegah kerugian sistemik bagi bisnis UMKM maupun korporasi.")

    # --- FITUR BARU: KALKULATOR ROI INTERAKTIF ---
    st.write("---")
    st.markdown("### 📊 KALKULATOR ESTIMASI KERUGIAN & ROI")
    st.write("Gunakan alat ini untuk melihat potensi dana yang dapat diselamatkan oleh VGUARD AI setiap bulannya.")
    
    with st.container():
        st.markdown('<div class="roi-calc-box">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            omzet = st.number_input("Masukkan Omzet Bulanan Bisnis Anda (Rp)", min_value=0, value=100000000, step=1000000)
            leakage_rate = st.slider("Estimasi Persentase Kebocoran (%)", 1.0, 20.0, 5.0)
        
        with c2:
            # Hitung estimasi
            total_loss = omzet * (leakage_rate / 100)
            saved_by_ai = total_loss * 0.90 # AI mengasumsikan efisiensi 90%
            
            st.write("#### Hasil Analisis Strategis:")
            st.error(f"Potensi Kerugian/Bocor: Rp {total_loss:,.0f}")
            st.success(f"Dana Diselamatkan VGUARD AI: Rp {saved_by_ai:,.0f}")
            
            roi_times = saved_by_ai / 5000000 # Asumsi ambil paket V-GROW (5jt)
            st.info(f"Efisiensi Investasi: {roi_times:.1f}x lipat dari biaya sistem")
        st.markdown('</div>', unsafe_allow_html=True)

    # LAYANAN PRODUK
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
        st.markdown('<div class="card-paket"><b>V-CUSTOM</b><h3 style="color:#1e3a8a">NEGO</h3><hr><p style="font-size:0.85rem; text-align:left;">• Solusi Tailor-made<br>• Integrasi ERP/SAP<br>• Support Strategis 24/7</p></div>', unsafe_allow_html=True)

    st.write("---")
    if st.button("🛡️ KONSULTASI STRATEGIS SEKARANG"):
        st.success("Permintaan telah diterima. Admin VGUARD AI akan segera menghubungi Bapak Erwin.")

elif menu == "Dashboard Performa":
    st.title("📊 Dashboard Performa")
    st.line_chart(np.random.randn(20, 2))

elif menu == "AI Scanner":
    st.title("🔍 AI Scanner Audit")
    st.button("Jalankan Analisis Engine")

# --- 5. FOOTER ---
st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Tangerang, Indonesia")
