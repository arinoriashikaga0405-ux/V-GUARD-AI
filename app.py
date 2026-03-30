import streamlit as st
import pandas as pd
import plotly.express as px
import os
import uuid
from datetime import datetime

# 1. KONFIGURASI HALAMAN & CSS BIAR KEREN & SEJAJAR
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

st.markdown("""
<style>
    .price-card {
        background-color: #f8f9fa;
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        height: 520px; /* Tinggi seragam agar tombol sejajar */
        display: flex;
        flex-direction: column;
        transition: 0.3s;
    }
    .price-card:hover {
        transform: translateY(-5px);
        border-color: #ff4b4b;
    }
    .package-title { font-size: 20px; font-weight: bold; color: #1f1f1f; margin-bottom: 5px; }
    .price-text { font-size: 22px; font-weight: bold; color: #ff4b4b; }
    .feature-text { font-size: 14px; color: #444; margin-top: 10px; flex-grow: 1; }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 2. DATA MASTER PAKET
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

# 3. SIDEBAR NAVIGASI
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Pilih Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🏠 Home: Visi & Misi", 
        "3. 📦 Paket Solusi", 
        "4. 🔐 Admin Panel"
    ])
    st.write("---")

# --- 1. PROFIL FOUNDER (100 KATA) ---
if menu == "1. 👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250)
    with r:
        st.subheader("Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        st.write("""
        Bapak Erwin Sinaga adalah seorang Senior Business Leader visioner dengan rekam jejak impresif selama lebih dari sepuluh tahun menduduki posisi strategis sebagai CEO dan CSO dalam industri perbankan serta manajemen aset. Pengalaman mendalam beliau dalam mengelola risiko operasional, memitigasi fraud finansial, dan menjaga integritas aset bernilai tinggi menjadi pondasi utama berdirinya V-Guard AI Systems. Beliau berdedikasi penuh untuk mendemokratisasi akses terhadap teknologi keamanan finansial berbasis kecerdasan buatan tingkat tinggi bagi pelaku UMKM maupun korporasi global di tahun 2026. Melalui kepemimpinan strategisnya, V-Guard AI hadir sebagai perantara cerdas yang memberikan standar proteksi aset kelas dunia, memastikan ekosistem bisnis klien tumbuh aman, adaptif, dan berkelanjutan.
        """)

# --- 2. HOME: VISI MISI & ROI ---
elif menu == "2. 🏠 Home: Visi & Misi":
    st.title("🛡️ Visi & Misi V-Guard AI")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("🎯 Visi")
        st.write("Menjadi perantara keamanan AI global yang mendemokratisasi proteksi finansial untuk semua skala bisnis di tahun 2026.")
    with c2:
        st.subheader("🚀 Misi")
        st.write("Memberikan kepastian keamanan kelas dunia melalui deteksi fraud adaptif dan integrasi CCTV AI yang presisi.")
    
    st.write("---")
    st.subheader("📈 Kalkulator ROI Penyelamatan")
    nt = st.number_input("Transaksi/Bulan:", value=1000)
    vt = st.number_input("Rata-rata Nilai (Rp):", value=500000)
    loss = (nt * vt) * 0.012
    st.error(f"Potensi Kerugian: Rp {loss:,.0f}")
    st.success(f"Penyelamatan AI: Rp {loss * 0.99:,.0f}")

# --- 3. PAKET SOLUSI (SEJAJAR & RAPI) ---
elif menu == "3. 📦 Paket Solusi":
    st.title("📦 Solusi Keamanan Terintegrasi")
    
    def draw_card(key):
        item = pkgs[key]
        st.markdown(f"""
        <div class="price-card">
            <div class="package-title">🛡️ {item['N']}</div>
            <div class="price-text">Setup: Rp {item['S']}</div>
            <div style="color: #666;">Bulanan: Rp {item['M']}</div>
            <div class="feature-text">{'<br>'.join(item['F'])}</div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(f"Pesan {key}", wa_url, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1: draw_card("MIKRO")
    with col2: draw_card("MENENGAH")
    
    st.write("#")
    
    col3, col4 = st.columns(2)
    with col3: draw_card("ENTERPRISE")
    with col4: draw_card("CORPORATE")

# --- 4. ADMIN PANEL (FITUR LENGKAP) ---
elif menu == "4. 🔐 Admin Panel":
    st.title("🔐 Admin Dashboard")
    if 'auth' not in st.session_state: st.session_state.auth = False
    
    if not st.session_state.auth:
        pwd = st.text_input("Password Admin:", type="password")
        if st.button("Masuk"):
            if pwd == st.secrets["ADMIN_PASSWORD"]:
                st.session_state.auth = True
                st.rerun()
    else:
        if st.button("Logout Admin"):
            st.session_state.auth = False
            st.rerun()
            
        t1, t2, t3, t4 = st.tabs(["📊 Statistik", "🚨 Alarm Real-time", "📲 Antrean Data", "🧾 Invoice"])
        
        with t1:
            st.subheader("Laporan Keamanan")
            fig = px.pie(values=[94, 6], names=['Aman', 'Anomali'], hole=0.4)
            st.plotly_chart(fig, use_container_width=True)
            
        with t2:
            st.subheader("🚨 Log Alarm Aktif")
            st.error(f"{datetime.now().strftime('%H:%M')} | 🚨 ANOMALI: Percobaan Akses dari IP Asing")
            st.write("15:30 | System Scan | Status: Aman")
            
        with t3:
            st.subheader("📲 Antrean Server (Overload Control)")
            st.info("Jam: 18:55 | Klien: PT Digital Vision | Status: ⏳ Dalam Proses AI")
            
        with t4:
            st.subheader("🧾 Invoice Generator")
            inv_name = st.text_input("Klien:")
            if st.button("Buat Invoice"):
                st.success(f"Invoice untuk {inv_name} berhasil dibuat!")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
