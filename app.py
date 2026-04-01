import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database & Login State
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25 08:00", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "MEDIUM", "Harga": 7500000, "Status": "🟢 AKTIF", "Jatuh_Tempo": "2026-04-25", "Log": "System Initialized"}
    ]

if 'admin_authenticated' not in st.session_state:
    st.session_state.admin_authenticated = False

# 2. CSS CUSTOM
st.markdown("""
<style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .fraud-alert { background: #f8d7da; color: #721c24; padding: 15px; border-radius: 10px; border-left: 10px solid #dc3545; font-weight: bold; animation: blinker 1s linear infinite; margin-bottom: 10px; }
    .piutang-box { background: #fff3cd; color: #856404; padding: 15px; border-radius: 10px; border-left: 10px solid #ffc107; margin-bottom: 10px; font-weight: bold; }
    .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); border-top: 5px solid #1E3A8A; height: 100%; }
    @keyframes blinker { 50% { opacity: 0.2; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 📦 Produk Unggulan", "4. 📝 Registrasi & Capture", "5. 🔐 Admin Control Center", "6. 📜 Laporan Audit Klien"])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- MENU 1: PROFIL FOUNDER (150 KATA) ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Founder")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("""
        Bapak Erwin Sinaga adalah seorang Senior Business Leader yang memiliki rekam jejak profesional selama lebih dari 10 tahun di sektor Perbankan dan Manajemen Aset. Sebagai mantan CEO dan CSO, beliau memahami secara mendalam tantangan kebocoran finansial yang sering dihadapi oleh pemilik bisnis. Dedikasi beliau terhadap integritas dan transparansi melahirkan V-Guard AI, sebuah platform cerdas yang dirancang untuk melindungi aset pelaku usaha melalui teknologi kecerdasan buatan. 
        
        Melalui kepemimpinannya, V-Guard AI tidak hanya menjadi alat monitor transaksi, tetapi menjadi mitra strategis dalam pengambilan keputusan bisnis berbasis data. Berdomisili di Tangerang, beliau aktif mengedukasi komunitas digital mengenai pentingnya pengawasan berlapis untuk mencegah fraud.
