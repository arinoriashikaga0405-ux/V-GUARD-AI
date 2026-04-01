import streamlit as st
import os
import pandas as pd
from datetime import datetime
import google.generativeai as genai

# 1. KONFIGURASI AI
try:
    genai.configure(api_key="AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA")
    model = genai.GenerativeModel('gemini-pro')
    ai_ok = True
except:
    ai_ok = False

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database & Login Session
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": 102, "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]
if 'admin_akses_terbuka' not in st.session_state:
    st.session_state.admin_akses_terbuka = False

WA_NUMBER = "628212190885"

# 2. CSS CUSTOM (STABIL)
st.markdown(f"""
<style>
    .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; }}
    .product-card {{ 
        background-color: #f8f9fa; 
        border: 1px solid #e0e0e0; 
        border-radius: 15px; 
        padding: 20px; 
        text-align: center; 
        min-height: 520px; 
        border-top: 8px solid #1E3A8A; 
    }}
    .pkg-title {{ font-size: 24px; font-weight: bold; color: #1E3A8A; margin-bottom: 10px; }}
    .feature-text {{ text-align: left; font-size: 14px; line-height: 1.6; margin-top: 15px; color: #444; }}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGASI
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🛡️ V-GUARD AI</h1>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.write("---")
    menu = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Upload", 
        "5. 🔐 Akses Terbatas"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", f"https://wa.me/{WA_NUMBER}")

# --- MENU 1: PROFIL FOUNDER (NARASI BARU >150 KATA, TANPA CEO/CSO) ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2.2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("""
        Bapak Erwin Sinaga adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir.

        Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel. Dengan visi besar untuk mendemokrasikan keamanan bisnis bagi semua kalangan, mulai dari tingkat UMKM hingga skala korporasi, beliau terus berinovasi dalam mengembangkan instrumen pengawasan yang adaptif terhadap tantangan ekonomi masa depan, memastikan setiap investasi klien terjaga dengan standar perlindungan berlapis dan efisiensi yang terukur secara nyata.
        """)

# --- MENU 2: VISI, MISI & ROI (TAMPILAN BARU) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("Analisis Strategis & Proteksi Kerugian")
    st.info("**Visi:** Menjadi standar emas dalam teknologi pengawasan bisnis digital di Indonesia.")
    st.success("**Misi:** Menyediakan instrumen audit AI untuk mendeteksi indikasi kecurangan secara real-time.")
    
    st.write("---")
    st.markdown("### 📉 Kalkulator Potensi Kerugian & ROI")
    omzet = st.number_input("Omzet Bulanan Bisnis (Rp):", value=100000000, step=1000000)
    
    c_roi1, c_roi2 = st.columns(2)
    with c_roi1:
        pot_bocor = omzet * 0.07
        st.error(f"**Estimasi Kebocoran (7%):** Rp {pot_bocor:,.0f}")
    with c_roi2:
        biaya_v = 2500000
        hasil_roi = pot_bocor - biaya_v
        st.metric("Dana Berhasil Diselamatkan", f"Rp {hasil_roi:,.0f}", delta="ROI Positif")

# --- MENU 3: PAKET (STABIL - TIDAK BERUBAH) ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("Layanan V-Guard AI")
    cols = st.columns(4)
    p_data = [
        ("BASIC", "1.5jt", "• Monitor Transaksi Harian<br>• Laporan Mingguan Manual<br>• Alarm Indikasi Fraud Dasar<br>• Support Layanan Jam Kerja"), 
        ("SMART", "2.5jt", "• Fraud AI Detection
