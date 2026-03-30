import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database
if 'db_nasabah' not in st.session_state or len(st.session_state.db_nasabah) == 0:
    st.session_state.db_nasabah = [
        {"Waktu": "2026-03-31", "Nama Personal": "Admin", "Nama Bisnis": "Contoh Corp", "Paket": "BASIC", "Harga": "2.500.000", "Status": "🔴 Menunggu Aktivasi"}
    ]

# 2. CSS CUSTOM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 16px; margin-top: 10px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .package-card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #e0e0e0; height: 580px; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .profile-box { text-align: justify; line-height: 1.8; padding: 20px; background: white; border-radius: 15px; font-size: 16px; }
    .vision-box { background: #fdfdfd; padding: 25px; border-left: 5px solid #007bff; border-radius: 10px; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● System Online / Connected</p>', unsafe_allow_html=True)
    menu = st.radio("Folder Navigasi:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 📦 Paket Layanan", "4. 📝 Registrasi Klien", "5. 🔐 Admin Dashboard"])
    st.write("---")
    st.link_button("📞 Hubungi Erwin Sinaga", "https://wa.me/628212190885")

# --- FOLDER 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.markdown(f"""<div class="profile-box">
        <b>Bapak Erwin Sinaga</b> merupakan seorang profesional dan Pemimpin Bisnis Senior dengan pengalaman lebih dari sepuluh tahun di industri perbankan dan manajemen aset. <br><br>
        V-Guard AI adalah wujud dedikasi beliau untuk menghadirkan sistem pengawasan aset berbasis AI yang mampu mendeteksi kecurangan secara real-time, memberikan rasa aman bagi para pemilik usaha di Indonesia.
        </div>""", unsafe_allow_html=True)

# --- FOLDER 2: VISI, MISI & ROI (VISI MISI DITAMPILKAN KEMBALI) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Strategi & Analisis ROI")
    
    # Bagian Visi & Misi
    st.markdown("""<div class="vision-box">
    <h3>Visi</h3>
    <p>Menjadi benteng pertahanan digital terdepan di Indonesia yang mengeliminasi kebocoran aset bisnis melalui kecerdasan buatan.</p>
    <h3>Misi</h3>
    <ul>
        <li>Mengintegrasikan AI dalam sistem audit harian UMKM dan Korporasi.</li>
        <li>Menyediakan alarm deteksi dini terhadap segala bentuk anomali transaksi.</li>
        <li>Memastikan transparansi penuh antara operasional lapangan dan pemilik bisnis.</li>
    </ul>
    </div>""", unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("📊 Kalkulator Potensi Penyelamatan Aset")
    omzet = st.number_input("Omzet Bulanan Bisnis Anda (Rp):", value=500000000, step=10000000)
    st.success(f"🛡️ Estimasi kebocoran yang bisa dicegah V-Guard AI: **Rp {omzet * 0.045:,.0f}** per bulan.")

# --- FOLDER 3: PAKET LAYANAN ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Layanan V-Guard AI")
    p_cols = st.columns(4)
    pkgs = [
        {"n": "BASIC", "s": "2.5jt", "m": "750rb", "c": "#f8f9fa", "f": ["Audit Harian", "Laporan Mingguan"]},
        {"n": "MEDIUM", "s": "7.5jt", "m": "1.5jt", "c": "#e3f2fd", "f": ["Semua Fitur BASIC", "AI CCTV Integration"]},
        {"n": "ENTERPRISE", "s": "25jt", "m": "5jt", "c": "#e8f5e9", "f": ["Semua Fitur MEDIUM", "Multi-Branch Dashboard"]},
        {"n": "CORPORATE", "s": "50jt", "m": "10jt", "c": "#fff3e0", "f": ["Semua Fitur ENTERPRISE", "Custom AI Model"]}
    ]
    for i, p in enumerate(pkgs):
        with p_cols[i]:
            st.markdown(f'<div class="package-card" style="background-color: {p["c"]};"><h3>{p["n"]}</h3><p>Setup: {p["s"]}<br>Bulanan: {p["m"]}</p><hr><ul>{"".join([f"<li>{item}</li>" for item in p["f"]])}</ul></div>', unsafe_allow_html=True)
            st.link_button(f"Pilih {p['n']}", f"
