import streamlit as st
import os
import pandas as pd
from datetime import datetime
import google.generativeai as genai

# --- 1. CONFIG & ENGINE AI ---
K_V = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=K_V)
    v_ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE & SESSION STATE (Struktur Data Lengkap) ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "p", "Level": "Eksekutif", "Paket": "MASTER"},
        {"User ID": "siska", "Password": "p", "Level": "Klien", "Paket": "SMART"},
        {"User ID": "jaya", "Password": "p", "Level": "Klien", "Paket": "BASIC"}
    ]

if 'db_n' not in st.session_state:
    st.session_state.db_n = [
        {"ID": "CL-101", "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": "CL-102", "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Usaha": "Otomotif", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]

if 'current_user' not in st.session_state:
    st.session_state.current_user = None

if 'auth_vguard' not in st.session_state:
    st.session_state.auth_vguard = False

if 'client_logged_in' not in st.session_state:
    st.session_state.client_logged_in = False

# --- 3. CSS PREMIUM (UKURAN & TAMPILAN) ---
st.markdown("""
<style>
    .fraud-header { background-color: #ff7675; color: white; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 15px; }
    .status-box { background-color: #e3f2fd; padding: 15px; border-radius: 8px; color: #1e3a8a; font-weight: bold; margin-bottom: 5px; }
    .package-box { background-color: #fff3e0; padding: 8px 15px; border-radius: 8px; color: #e65100; font-weight: bold; display: inline-block; margin-bottom: 20px; border: 1px solid #ffe0b2; font-size: 14px; }
    .service-card { background-color: #ffffff; padding: 15px; border-radius: 12px; border: 1px solid #e0e0e0; text-align: center; height: 400px; }
    .client-box { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #1e3a8a; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR (NAVIGASI TETAP 1-5) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.markdown("**Erwin Sinaga - Senior Business Leader**")
    st.write("---")
    nav = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 💎 Layanan Produk", 
        "4. 📝 Registrasi & Upload", 
        "5. 🔐 Akses Terbatas"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI Intelligence")

# --- 5. LOGIKA HALAMAN ---

# MENU 1: PROFIL
if nav == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2.5])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.write("""Bapak **Erwin Sinaga** adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Beliau memahami bahwa di era digital saat ini, integritas data dan keamanan aset adalah fondasi utama bagi setiap unit bisnis untuk dapat tumbuh secara berkelanjutan.

Melalui dedikasi yang tinggi terhadap transparansi, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan mendesak para pengusaha akan sistem perlindungan aset yang berbasis teknologi kecerdasan buatan mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif dan efisien. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit real-time yang mampu meminimalisir risiko kerugian modal secara signifikan.""")

# MENU 2: VISI MISI ROI
elif nav == "2. 🎯 Visi, Misi & ROI":
    st.header("Visi, Misi & Analisis Kerugian")
    st.info("**Visi:** Menjadi pelopor global dalam penyediaan infrastruktur audit digital berbasis AI.")
    st.success("**Misi:** Mengintegrasikan AI untuk deteksi fraud real-time.")
    st.write("---")
    st.subheader("📊 Simulasi ROI & Penyelamatan Aset")
    oz = st.number_input("Input Total Omzet Bulanan (Rp):", value=100000000)
    leakage = oz * 0.07
    st.error(f"Potensi Kerugian Akibat Kebocoran (7%): Rp {leakage:,.0f}")
    st.success(f"Estimasi Penyelamatan: Rp {leakage - 2500000:,.0f}")

# MENU 3: LAYANAN PRODUK
elif nav == "3. 💎 Layanan Produk":
    st.header("Paket Layanan Unggulan V-Guard AI")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="service-card"><h3>📦 BASIC</h3><div class="price-tag">Rp 1.5jt</div>• AI Monitor Dasar<br>• Laporan Bulanan<br
