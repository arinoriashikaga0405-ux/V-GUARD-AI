import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Executive Platform", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .header-box { text-align: center; padding: 20px 0; }
    .main-title { font-size: 3rem !important; font-weight: 800; color: #1e3a8a; margin-bottom: 0; }
    .mission-box { 
        background-color: #ffffff; padding: 20px; border-radius: 12px; 
        border-left: 8px solid #1e3a8a; box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
        text-align: center; margin: 20px auto; max-width: 900px;
    }
    .card-paket {
        background-color: #ffffff; padding: 25px; border-radius: 15px; 
        border: 1px solid #e2e8f0; height: 460px; transition: 0.3s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02); text-align: center;
    }
    .alarm-tag { 
        background-color: #fee2e2; color: #ef4444; padding: 5px 12px; 
        border-radius: 20px; font-size: 0.8rem; font-weight: bold; border: 1px solid #fecaca;
        display: inline-block; margin-top: 15px;
    }
    .stButton>button { background-color: #1e3a8a; color: white; border-radius: 8px; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI")
    st.write("---")
    if st.button("🏠 Beranda Utama"):
        st.session_state.page = "Home"
        st.rerun()
    st.write("---")
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 4. LOGIKA NAVIGASI ---

if st.session_state.page == "Admin":
    st.title("💻 Admin Portal")
    pwd = st.text_input("Kode Otoritas", type="password")
    if pwd == "vguard2026":
        st.success("Otoritas Diterima.")
        st.warning("🚨 [ALARM] Anomali Transaksi Terdeteksi!")
        if st.button("🔔 Kirim Fire Alarm"):
            st.error("Alarm Terkirim ke Owner!")
    elif pwd != "":
        st.error("Kode Salah!")

elif st.session_state.page == "Klien":
    st.title("📱 Owner Dashboard")
    st.metric("Total Profit Aman", "Rp 125.000.000")
    st.info("Log: [ALARM] Terdeteksi Manipulasi Data di Store 01.")

else:
    # --- BERANDA ---
    st.markdown('<div class="header-box"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="mission-box"><p style="font-size:1.4rem; font-style:italic; color:#1e3a8a; margin:0;">"Digitizing Trust, Eliminating Leakage"</p></div>', unsafe_allow_html=True)

    st.write("---")
    c_img, c_txt = st.columns([1, 4])
    with c_txt:
        st.markdown("### FOUNDER PROFILE & FILOSOFI")
        # Teks Profil dalam satu baris untuk menghindari SyntaxError
        txt = "Saya **Erwin**, Founder VGUARD AI Systems, mengintegrasikan standar keamanan **10 tahun pengalaman profesional di industri perbankan** ke dalam operasional bisnis Anda. Filosofi kami, **Perisai Digital**, memastikan integritas aset Anda melalui teknologi **V-Guard Fire Alarm** yang bekerja tanpa henti mendeteksi setiap indikasi kecurangan."
        st.write(txt)

    st.write("---")
    col_adm, col_cli = st.columns(2)
    with col_adm:
        if st.button("Masuk Admin Portal"):
            st.session_state.page = "Admin"
            st.rerun()
    with col_cli:
        if st.button("Masuk Client Portal"):
            st.session_state.page = "Klien"
            st.rerun()

    st.write("---")
    st.markdown("### 🏷️ LAYANAN PRODUK & PAKET")
    p1, p2, p3, p4 = st.columns(4)
    
    # Template HTML Paket
    p_start = '<div class="card-paket"><b>V-START</b><h3 style="color:#1e3a8a">2.5 JT</h3><hr><p style="text-align:left; font-size:0.9rem;">• Audit Harian Retail<br>• Notifikasi WA Aktif<br>• Laporan Mingguan Dasar<br><span class="alarm-tag">🔥 V-Guard Fire Alarm</span></p></div>'
    p_grow = '<div class="card-paket"><b>V-GROW</b><h3 style="color:#1e3a8a">5 JT</h3><hr><p style="text-align:left; font-size:0.9rem;">• Fitur V-START<br>• AI Fraud Detection<br>• Sinkron Stok Otomatis<br><span class="alarm-tag">🔥 V-Guard Fire Alarm</span></p></div>'
    p_prime = '<div class="card-paket"><b>V-PRIME</b><h3 style="color:#1e3a8a">10 JT</h3><hr><p style="text-align:left; font-size:0.9rem;">• Fitur V-GROW<br>• Audit Multi-Cabang<br>• Predictive AI Analytics<br><span class="alarm-tag">🔥 V-Guard Fire Alarm</span></p></div>'
    p_custom = '<div class="card-paket"><b>V-CUSTOM</b><h3 style="color:#1e3a8a">NEGO</h3><hr><p style="text-align:left; font-size:0.9rem;">• Solusi Enterprise
