import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

# 1. KONFIGURASI HALAMAN & CSS RINGKAS
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

st.markdown("""
<style>
    .price-card {
        background-color: #f8f9fa;
        border-radius: 12px;
        padding: 15px;
        border: 1px solid #e0e0e0;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        height: 380px; /* Ukuran diperkecil sesuai permintaan */
        display: flex;
        flex-direction: column;
        transition: 0.2s;
    }
    .price-card:hover {
        transform: translateY(-3px);
        border-color: #ff4b4b;
    }
    .package-title { font-size: 17px; font-weight: bold; color: #1f1f1f; }
    .price-text { font-size: 19px; font-weight: bold; color: #ff4b4b; }
    .feature-text { font-size: 12px; color: #444; flex-grow: 1; line-height: 1.3; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 2. DATA MASTER PAKET (DIPERPADAT)
pkgs = {
    "MIKRO": {
        "N": "Basic Guard", "S": "2.5jt", "M": "500rb",
        "F": ["✅ AI Fraud Dasar", "✅ Email Support", "✅ Laporan Mingguan"]
    },
    "MENENGAH": {
        "N": "Premium Shield", "S": "7.5jt", "M": "1.5jt",
        "F": ["✅ AI Anomaly Detection", "✅ 🚨 Fitur Alarm", "✅ 🧾 Auto Invoice Pro", "✅ WA Priority Support"]
    },
    "ENTERPRISE": {
        "N": "Enterprise Vault", "S": "50jt", "M": "5jt",
        "F": ["✅ Full AI Integration", "✅ 🚨 Fitur Alarm", "✅ 🧾 Auto Invoice Pro", "✅ 📹 CCTV AI Integration"]
    },
    "CORPORATE": {
        "N": "Elite Managed", "S": "85jt", "M": "10jt",
        "F": ["✅ Custom AI Training", "✅ 🚨 Fitur Alarm", "✅ 🧾 Auto Invoice Pro", "✅ 📹 CCTV AI 24/7", "✅ Dedicated Engineer"]
    }
}

# 3. SIDEBAR
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Pilih Menu:", ["1. 👤 Profil Founder", "2. 🏠 Home: Visi & Misi", "3. 📦 Paket Solusi", "4. 🔐 Admin Panel"])

# --- 1. PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): 
            st.image("erwin.jpg", use_container_width=True)
        else: 
            st.error("Foto 'erwin.jpg' tidak ditemukan di folder.")
    with r:
        st.subheader("Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        st.write("Bapak Erwin Sinaga adalah seorang Senior Business Leader visioner dengan rekam jejak impresif selama lebih dari sepuluh tahun menduduki posisi strategis sebagai CEO dan CSO dalam industri perbankan serta manajemen aset. Pengalaman mendalam beliau dalam mengelola risiko operasional, memitigasi fraud finansial, dan menjaga integritas aset bernilai tinggi menjadi pondasi utama berdirinya V-Guard AI Systems. Beliau berdedikasi penuh untuk mendemokratisasi akses terhadap teknologi keamanan finansial berbasis kecerdasan buatan tingkat tinggi bagi pelaku UMKM maupun korporasi global di tahun 2026. Melalui kepemimpinan strategisnya, V-Guard AI hadir sebagai perantara cerdas yang memberikan standar proteksi aset kelas dunia, memastikan ekosistem bisnis klien tumbuh aman, adaptif, dan berkelanjutan.")

# --- 2. HOME ---
elif menu == "2. 🏠 Home: Visi & Misi":
    st.title("🛡️ Visi & Misi V-Guard AI")
    st.write("Visi: Menjadi perantara keamanan AI global nomor 1 untuk semua skala bisnis di tahun 2026.")
    st.write("---")
    st.subheader("📈 Kalkulator ROI")
    nt = st.number_input("Transaksi/Bulan:", value=1000)
    vt = st.number_input("Rata-rata Nilai (Rp):", value=500000)
    loss = (nt * vt) * 0.012
    st.error(f"Potensi Kerugian: Rp {loss:,.0f}")
    st.success(f"Penyelamatan AI: Rp {loss * 0.99:,.0f}")

# --- 3. PAKET SOLUSI (RINGKAS & SEJAJAR) ---
elif menu == "3. 📦 Paket Solusi":
    st.title("📦 Solusi Keamanan Terintegrasi")
    
    def draw_card(key):
        item = pkgs[key]
        st.markdown(f"""
        <div class="price-card">
            <div class="package-title">🛡️ {item['N']}</div>
            <div class="price-text">Setup: Rp {item['S']}</div>
            <div style="font-size:12px; color:#666;">Bulanan: Rp {item['M']}</div>
            <div class="feature-text">{'<br>'.join(item['F'])}</div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(f"Pesan {key}", wa_url, use_container_width=True)

    c1, c2 = st.columns(2)
    with c1: draw_card("MIKRO")
    with c2: draw_card("MENENGAH")
    st.write("#")
    c3, c4 = st.columns(2)
    with c3: draw_card("ENTERPRISE")
    with c4: draw_card("CORPORATE")

# --- 4. ADMIN PANEL ---
elif menu == "4. 🔐 Admin Panel":
    st.title("🔐 Admin Dashboard")
    if 'auth' not in st.session_state: st.session_state.auth = False
    if not st.session_state.auth:
        pwd = st.text_input("Password:", type="password")
        if st.button("Login"):
            if pwd == st.secrets.get("ADMIN_PASSWORD", "admin123"):
                st.session_state.auth = True
                st.rerun()
    else:
        t1, t2, t3, t4 = st.tabs(["📊 Stats", "🚨 Alarm", "📲 Antrean", "🧾 Invoice"])
        with t1: st.plotly_chart(px.pie(values=[94, 6], names=['Aman', 'Anomali'], hole=0.4))
        with t2: st.error("🚨 ANOMALI: Massive Withdrawal Detected")
        with t3: st.info("Antrean: PT Digital Vision (18:55)")
        with t4: st.success("Invoice Generator Aktif.")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Strategically Led by Erwin Sinaga")
