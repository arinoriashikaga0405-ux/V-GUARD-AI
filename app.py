import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Executive Platform", page_icon="🛡️", layout="wide")

# Inisialisasi State untuk Navigasi Demo
if 'demo_mode' not in st.session_state:
    st.session_state.demo_mode = "Home"

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
    .feature-box {
        background-color: #f8fafc; padding: 15px; border-radius: 10px;
        border-left: 4px solid #1e3a8a; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .roi-calc-box {
        background-color: #f1f5f9; padding: 25px; border-radius: 15px;
        border: 2px solid #1e3a8a; margin-top: 20px;
    }
    .stButton>button { background-color: #1e3a8a; color: white; border-radius: 8px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    try:
        st.image("erwin.jpg", width=70) 
    except:
        st.write("👤 PROFILE CEO")
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI Systems")
    st.write("---")
    if st.button("🏠 Kembali ke Beranda"):
        st.session_state.demo_mode = "Home"

# --- 4. LOGIKA HALAMAN ---

# A. HALAMAN DEMO ADMIN
if st.session_state.demo_mode == "Admin":
    st.title("💻 Portal Dashboard Admin (Simulasi)")
    st.warning("Mode Audit Aktif: AI sedang memindai transaksi mencurigakan...")
    
    # Simulasi Data Audit
    df_audit = pd.DataFrame({
        'Waktu': ['10:05', '10:12', '10:45', '11:02'],
        'User': ['Kasir_01', 'Admin_02', 'Kasir_01', 'Kasir_03'],
        'Aktivitas': ['Void Transaksi', 'Edit Harga', 'Input Manual', 'Void Transaksi'],
        'Status AI': ['⚠️ Mencurigakan', '✅ Normal', '⚠️ Anomali', '✅ Normal']
    })
    st.table(df_audit)
    st.button("Jalankan Rekonsiliasi Stok", type="primary")

# B. HALAMAN DEMO KLIEN
elif st.session_state.demo_mode == "Klien":
    st.title("📱 Portal Dashboard Owner (Simulasi)")
    st.success("Koneksi WhatsApp Aktif: Anda akan menerima alert jika terjadi leakage.")
    
    col_stat1, col_stat2, col_stat3 = st.columns(3)
    col_stat1.metric("Total Omzet Hari Ini", "Rp 12.500.000", "+5%")
    col_stat2.metric("Potensi Leakage Dicegah", "Rp 450.000", "Safe", delta_color="normal")
    col_stat3.metric("Efisiensi Sistem", "98.2%", "+1.2%")
    
    st.write("### Grafik Performa Real-time")
    chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Sales', 'Loss Prevention'])
    st.line_chart(chart_data)

# C. HALAMAN UTAMA (HOME)
else:
    st.markdown('<div class="header-box"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="mission-box"><p style="font-size:1.4rem; font-style:italic; color:#1e3a8a; margin:0;">"Digitizing Trust, Eliminating Leakage"</p></div>', unsafe_allow_html=True)

    # Profil & Filosofi (Terkunci)
    st.write("---")
    col_img, col_txt = st.columns([1, 4])
    with col_img:
        try:
            st.image("erwin.jpg", width=130) 
        except:
            st.info("Upload foto erwin.jpg")
    with col_txt:
        st.markdown("### PROFIL & VISI STRATEGIS")
        st.write("Saya **Erwin**, membawa lebih dari **10 tahun pengalaman profesional di industri perbankan** dalam membangun fondasi VGUARD AI. Kami mentransformasikan standar keamanan perbankan ke bisnis Anda.")

    # --- EKOSISTEM DENGAN TOMBOL AKTIF ---
    st.write("---")
    st.markdown("### 🌐 EKOSISTEM FITUR VGUARD AI")
    t_admin, t_client = st.tabs(["💻 PORTAL ADMIN", "📱 PORTAL KLIEN"])

    with t_admin:
        st.write("#### Alat Kerja Tim Audit & Admin")
        st.markdown('<div class="feature-box"><b>🔍 AI Audit Scanner</b>: Mendeteksi anomali pada data transaksi.</div>', unsafe_allow_html=True)
        if st.button("MASUK KE DASHBOARD ADMIN"):
            st.session_state.demo_mode = "Admin"
            st.rerun()

    with t_client:
        st.write("#### Kontrol Eksklusif Pemilik Bisnis")
        st.markdown('<div class="feature-box"><b>📊 Executive Dashboard</b>: Visualisasi laba-rugi secara real-time.</div>', unsafe_allow_html=True)
        if st.button("MASUK KE PORTAL OWNER"):
            st.session_state.demo_mode = "Klien"
            st.rerun()

    # ROI & PRODUK (Terkunci)
    st.write("---")
    st.markdown("### 📊 KALKULATOR ESTIMASI KERUGIAN & ROI")
    omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
    leakage_rate = st.slider("Estimasi Kebocoran (%)", 1.0, 20.0, 5.0)
    total_loss = omzet * (leakage_rate / 100)
    st.error(f"Potensi Kerugian: Rp {total_loss:,.0f}")

    st.write("---")
    st.write("### LAYANAN PRODUK")
    st.columns(4)[1].markdown('**V-GROW**<br>5 JT / Bulan', unsafe_allow_html=True)

# Footer
st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Tangerang")
