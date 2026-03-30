import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS CUSTOM UNTUK TAMPILAN KEREN & SEJAJAR
st.markdown("""
<style>
    /* Mengatur kotak paket agar tinggi seragam dan tombol sejajar di bawah */
    .price-card {
        background-color: #f8f9fa;
        border-radius: 15px;
        padding: 25px;
        border: 1px solid #e0e0e0;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.05);
        transition: 0.3s;
        height: 520px; /* Tinggi tetap agar sejajar */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .price-card:hover {
        transform: translateY(-10px);
        box-shadow: 5px 5px 25px rgba(0,0,0,0.1);
        border-color: #ff4b4b;
    }
    .package-name { color: #1f1f1f; font-weight: bold; font-size: 20px; margin-bottom: 10px; }
    .price-tag { color: #ff4b4b; font-size: 24px; font-weight: bold; }
    .feature-list { font-size: 14px; color: #555; flex-grow: 1; }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# DATA PAKET
pkgs = {
    "MIKRO": {
        "N": "Basic Guard", "S": "2.5jt", "M": "500rb",
        "F": ["• AI Fraud Detection Dasar", "• Email Support", "• Laporan Mingguan", "• Dashboard Standar"]
    },
    "MENENGAH": {
        "N": "Premium Shield", "S": "7.5jt", "M": "1.5jt",
        "F": ["• AI Anomaly Detection", "• 🚨 Fitur Alarm System", "• 🧾 Auto Invoice Pro", "• WA Priority Support", "• Analisis Risiko Live"]
    },
    "ENTERPRISE": {
        "N": "Enterprise Vault", "S": "50jt", "M": "5jt",
        "F": ["• Full AI Integration", "• 🚨 Fitur Alarm System", "• 🧾 Auto Invoice Pro", "• 📹 Integrasi CCTV AI", "• Audit Keamanan Bulanan"]
    },
    "CORPORATE": {
        "N": "Elite Managed", "S": "85jt", "M": "10jt",
        "F": ["• Custom AI Training", "• 🚨 Fitur Alarm System", "• 🧾 Auto Invoice Pro", "• 📹 CCTV AI 24/7", "• Dedicated Security Engineer"]
    }
}

# 3. SIDEBAR
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi:", ["1. 👤 Profil Founder", "2. 🏠 Home: Visi & Misi", "3. 📦 Paket Solusi", "4. 🔐 Admin Panel"])
    st.write("---")

# --- NOMOR 1: PROFIL ---
if menu == "1. 👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250)
    with r:
        st.subheader("Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        st.write("Bapak Erwin Sinaga adalah seorang Senior Business Leader visioner dengan rekam jejak impresif selama lebih dari sepuluh tahun menduduki posisi strategis sebagai CEO dan CSO dalam industri perbankan serta manajemen aset. Pengalaman mendalam beliau dalam mengelola risiko operasional, memitigasi fraud finansial, dan menjaga integritas aset bernilai tinggi menjadi pondasi utama berdirinya V-Guard AI Systems. Beliau berdedikasi penuh untuk mendemokratisasi akses terhadap teknologi keamanan finansial berbasis kecerdasan buatan tingkat tinggi bagi pelaku UMKM maupun korporasi global di tahun 2026. Melalui kepemimpinan strategisnya, V-Guard AI hadir sebagai perantara cerdas yang memberikan standar proteksi aset kelas dunia, memastikan ekosistem bisnis klien tumbuh aman, adaptif, dan berkelanjutan.")

# --- NOMOR 2: HOME ---
elif menu == "2. 🏠 Home: Visi & Misi":
    st.title("🛡️ Keamanan Finansial Masa Depan")
    st.markdown("### Visi: Menjadi Intermediary Keamanan AI Global Nomor 1.")
    st.write("---")
    st.subheader("📈 Kalkulator ROI Penyelamatan")
    nt = st.number_input("Transaksi Bulanan:", value=1000)
    vt = st.number_input("Nilai Rata-rata (Rp):", value=500000)
    loss = (nt * vt) * 0.012
    st.error(f"Potensi Fraud Tanpa V-Guard: Rp {loss:,.0f}")
    st.success(f"Penyelamatan V-Guard AI: Rp {loss * 0.99:,.0f}")

# --- NOMOR 3: PAKET SOLUSI (DENGAN TAMPILAN KEREN & SEJAJAR) ---
elif menu == "3. 📦 Paket Solusi":
    st.title("📦 Solusi Keamanan Terintegrasi")
    st.write("Pilih paket yang sesuai dengan skala bisnis Anda. Seluruh tombol telah disejajarkan secara presisi.")
    
    # BARIS 1
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div class="price-card">
            <div>
                <div class="package-name">🛡️ {pkgs['MIKRO']['N']} (MIKRO)</div>
                <div class="price-tag">Setup: Rp {pkgs['MIKRO']['S']}</div>
                <p>Bulan: Rp {pkgs['MIKRO']['M']}</p>
                <div class="feature-list">{'<br>'.join(pkgs['MIKRO']['F'])}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Pesan Mikro Sekarang", wa_url, use
