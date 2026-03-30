import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

# 1. KONFIGURASI HALAMAN & UI PREMIUM
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

st.markdown("""
<style>
    .main-title { font-size: 32px; font-weight: 800; color: #1f1f1f; margin-bottom: 5px; }
    .sub-title { font-size: 16px; color: #666; margin-bottom: 25px; }
    .vision-mission-box {
        background: #ffffff;
        border-radius: 12px;
        padding: 20px;
        border-left: 5px solid #ff4b4b;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .price-card {
        background: white; border-radius: 15px; padding: 0px; border: 1px solid #eee;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); height: 420px;
        display: flex; flex-direction: column; overflow: hidden; transition: 0.3s;
    }
    .price-card:hover { transform: translateY(-8px); box-shadow: 0 12px 30px rgba(0,0,0,0.12); }
    .card-header {
        background: linear-gradient(135.2deg, #ff4b4b 0%, #a51d1d 100%);
        color: white; padding: 15px; text-align: center; font-weight: bold; font-size: 18px;
    }
    .card-content { padding: 20px; flex-grow: 1; }
    .price-tag { font-size: 22px; font-weight: 800; color: #1f1f1f; }
    .monthly-tag { font-size: 14px; color: #ff4b4b; font-weight: 600; margin-bottom: 15px; }
    .feature-item { font-size: 13px; color: #444; margin-bottom: 8px; display: flex; align-items: center; }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 2. DATA MASTER PAKET
pkgs = {
    "MIKRO": {"N": "Basic Guard", "S": "2.5jt", "M": "500rb", "F": ["🛡️ AI Fraud Detection", "📩 Email Support", "📊 Laporan Mingguan"]},
    "MENENGAH": {"N": "Premium Shield", "S": "7.5jt", "M": "1.5jt", "F": ["🔍 Anomaly Detection", "🚨 Real-time Alarm", "🧾 Auto Invoice Pro", "📱 WA Priority Support"]},
    "ENTERPRISE": {"N": "Enterprise Vault", "S": "50jt", "M": "5jt", "F": ["⚙️ Full AI Integration", "🚨 Smart Alarm System", "🧾 Auto Invoice Pro", "📹 CCTV AI Integration"]},
    "CORPORATE": {"N": "Elite Managed", "S": "85jt", "M": "10jt", "F": ["🧠 Custom AI Training", "🚨 Executive Alarm", "🧾 Auto Invoice Pro", "📹 CCTV AI 24/7", "👤 Dedicated Engineer"]}
}

# 3. SIDEBAR
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Pilih Menu:", ["1. 🏠 Home & ROI", "2. 📦 Paket Solusi", "3. 👤 Profil Founder", "4. 🔐 Admin Panel"])
    st.write("---")

# --- 1. HOME: VISI, MISI & ROI ---
if menu == "1. 🏠 Home & ROI":
    st.markdown('<div class="main-title">🛡️ Keamanan Masa Depan dengan AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">V-Guard AI Systems hadir untuk melindungi aset bisnis Anda secara otomatis dan cerdas.</div>', unsafe_allow_html=True)
    
    # BAGIAN VISI & MISI
    col_v, col_m = st.columns(2)
    with col_v:
        st.markdown("""
        <div class="vision-mission-box">
            <h4 style="color:#ff4b4b; margin-top:0;">🎯 Visi</h4>
            <p style="font-size:14px; color:#444;">Menjadi <b>Intermediary Keamanan AI Global Nomor 1</b> yang mendemokratisasi teknologi proteksi finansial tingkat tinggi untuk semua skala bisnis di Indonesia pada tahun 2026.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_m:
        st.markdown("""
        <div class="vision-mission-box">
            <h4 style="color:#ff4b4b; margin-top:0;">🚀 Misi</h4>
            <ul style="font-size:14px; color:#444; padding-left:20px;">
                <li>Mengintegrasikan AI adaptif untuk deteksi fraud dini.</li>
                <li>Menyediakan solusi keamanan end-to-end yang terjangkau bagi UMKM.</li>
                <li>Menjamin integritas aset klien melalui monitoring CCTV AI 24/7.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Aset")
    nt = st.number_input("Transaksi/Bulan:", value=1000)
    vt = st.number_input("Rata-rata Nilai (Rp):", value=500000)
    loss = (nt * vt) * 0.012
    st.error(f"Potensi Kerugian Tanpa AI: Rp {loss:,.0f}")
    st.success(f"Penyelamatan V-Guard AI (99%): Rp {loss * 0.99:,.0f}")

# --- 2. PAKET SOLUSI ---
elif menu == "2. 📦 Paket Solusi":
    st.title("📦 Investasi Keamanan Bisnis")
    def draw_premium_card(key):
        item = pkgs[key]
        features_html = "".join([f'<div class="feature-item">{f}</div>' for f in item['F']])
        st.markdown(f"""
        <div class="price-card">
            <div class="card-header">🛡️ {item['N']}</div>
            <div class="card-content">
                <div class="price-tag">Setup: Rp {item['S']}</div>
                <div class="monthly-tag">Langanan: Rp {item['M']} / Bulan</div>
                <hr>
                {features_html}
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(f"PILIH PAKET {key}", wa_url, use_container_width=True)

    c1, c2 = st.columns(2)
    with c1: draw_premium_card("MIKRO")
    with c2: draw_premium_card("MENENGAH")
    st.write("#")
    c3, c4 = st.columns(2)
    with c3: draw_premium_card("ENTERPRISE")
    with c4: draw_premium_card("CORPORATE")

# --- 3. PROFIL FOUNDER ---
elif menu == "3. 👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
        else: st.error("Silakan unggah 'erwin.jpg'")
    with r:
        st.subheader("Erwin Sinaga")
        st.write("Bapak Erwin Sinaga adalah Senior Business Leader visioner dengan pengalaman lebih dari 10 tahun sebagai CEO/CSO di industri perbankan.")

# --- 4. ADMIN PANEL ---
elif menu == "4. 🔐 Admin Panel":
    st.title("🔐 Admin Dashboard")
    # ... (Fitur Admin tetap sama seperti sebelumnya)

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia | Strategically Led by Erwin Sinaga")
