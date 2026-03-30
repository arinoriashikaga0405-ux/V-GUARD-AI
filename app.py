import streamlit as st
import pandas as pd
import plotly.express as px
import os
import uuid
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")
wa_url = "https://wa.me/6282122190885"

# 2. DATA MASTER PAKET LENGKAP
pkgs = {
    "MIKRO": {
        "N": "Basic Guard", "S": "2.500.000", "M": "500.000",
        "F": ["AI Fraud Detection Dasar", "Email Support", "Laporan Mingguan"]
    },
    "MENENGAH": {
        "N": "Premium Shield", "S": "7.500.000", "M": "1.500.000",
        "F": ["AI Anomaly Detection", "🚨 Fitur Alarm", "🧾 Auto Invoice", "WA Priority Support"]
    },
    "ENTERPRISE": {
        "N": "Enterprise Vault", "S": "50.000.000", "M": "5.000.000",
        "F": ["Full AI Integration", "🚨 Fitur Alarm", "🧾 Auto Invoice", "📹 Integrasi CCTV AI", "Audit Bulanan"]
    },
    "CORPORATE": {
        "N": "Elite Managed", "S": "85.000.000", "M": "10.000.000",
        "F": ["Custom AI Training", "🚨 Fitur Alarm", "🧾 Auto Invoice", "📹 CCTV AI 24/7", "Dedicated Engineer"]
    }
}

# 3. SIDEBAR NAVIGASI
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🏠 Home: Visi & Misi", 
        "3. 📦 Paket Solusi & Layanan", 
        "4. 🔐 Admin Panel (Full Feature)"
    ])
    st.write("---")

# --- NOMOR 1: PROFIL FOUNDER (100 KATA) ---
if menu == "1. 👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
        else: st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250)
    with r:
        st.subheader("Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        st.write("""
        Bapak Erwin Sinaga adalah seorang Senior Business Leader visioner dengan rekam jejak impresif selama lebih dari sepuluh tahun 
        menduduki posisi strategis sebagai CEO dan CSO dalam industri perbankan serta manajemen aset. Pengalaman mendalam beliau dalam 
        mengelola risiko operasional, memitigasi fraud finansial, dan menjaga integritas aset bernilai tinggi menjadi pondasi utama 
        berdirinya V-Guard AI Systems. Beliau berdedikasi penuh untuk mendemokratisasi akses terhadap teknologi keamanan finansial 
        berbasis kecerdasan buatan tingkat tinggi bagi pelaku UMKM maupun korporasi global di tahun 2026. Melalui kepemimpinan strategisnya, 
        V-Guard AI hadir sebagai perantara cerdas yang memberikan standar proteksi aset kelas dunia, memastikan ekosistem bisnis klien 
        tumbuh aman, adaptif, dan berkelanjutan.
        """)

# --- NOMOR 2: HOME (VISI MISI & ROI) ---
elif menu == "2. 🏠 Home: Visi & Misi":
    st.title("🛡️ Visi & Misi V-Guard AI")
    cv, cm = st.columns(2)
    with cv:
        st.subheader("🎯 Visi")
        st.write("Menjadi intermediary keamanan AI global yang mendemokratisasi proteksi finansial untuk semua skala bisnis.")
    with cm:
        st.subheader("🚀 Misi")
        st.write("Menghadirkan teknologi deteksi fraud adaptif dan integrasi CCTV AI guna menjamin keamanan aset klien secara end-to-end.")
    
    st.write("---")
    st.subheader("📈 Kalkulator ROI Penyelamatan")
    nt = st.number_input("Transaksi/Bulan:", value=1000)
    vt = st.number_input("Rata-rata Nilai (Rp):", value=500000)
    fp = st.slider("Asumsi Fraud (%):", 0.0, 5.0, 1.2)
    loss = (nt * vt) * (fp / 100)
    st.error(f"Potensi Kerugian: Rp {loss:,.0f}")
    st.success(f"Penyelamatan AI (99%): Rp {loss * 0.99:,.0f}")

# --- NOMOR 3: PAKET SOLUSI (LENGKAP DENGAN FITUR) ---
elif menu == "3. 📦 Paket Solusi & Layanan":
    st.title("📦 Investasi Keamanan & Layanan")
    
    # Baris 1
    c1, c2 = st.columns(2)
    with c1:
        st.warning(f"**{pkgs['MIKRO']['N']} (MIKRO)**")
        st.write(f"💰 Setup: Rp {pkgs['MIKRO']['S']}")
        st.write(f"📅 Bulanan: Rp {pkgs['MIKRO']['M']}")
        for f in pkgs['MIKRO']['F']: st.write(f"- {f}")
        st.link_button("Pesan Mikro", wa_url, use_container_width=True)
    with c2:
        st.warning(f"**{pkgs['MENENGAH']['N']} (MENENGAH)**")
        st.write(f"💰 Setup: Rp {pkgs['MENENGAH']['S']}")
        st.write(f"📅 Bulanan: Rp {pkgs['MENENGAH']['M']}")
        for f in pkgs['MENENGAH']['F']: st.write(f"- {f}")
        st.link_button("Pesan Menengah", wa_url, use_container_width=True)
    
    st.write("---")
    # Baris 2
    c3, c4 = st.columns(2)
    with c3:
        st.warning(f"**{pkgs['ENTERPRISE']['N']} (ENTERPRISE)**")
        st.write(f"💰 Setup: Rp {pkgs['ENTERPRISE']['S']}")
        st.write(f"📅 Bulanan: Rp {pkgs['ENTERPRISE']['M']}")
        for f in pkgs['ENTERPRISE']['F']: st.write(f"- {f}")
        st.link_button("Pesan Enterprise", wa_url, use_container_width=True)
    with c4:
        st.warning(f"**{pkgs['CORPORATE']['N']} (CORPORATE)**")
        st.write(f"💰 Setup: Rp {pkgs['CORPORATE']['S']}")
        st.write(f"📅 Bulanan: Rp {pkgs['CORPORATE']['M']}")
        for f in pkgs['CORPORATE']['F']: st.write(f"- {f}")
        st.link_button("Pesan Corporate", wa_url, use_container_width=True)

# --- NOMOR 4: ADMIN PANEL (FULL FEATURE) ---
elif menu == "4. 🔐 Admin Panel (Full Feature)":
    st.title("🔐 Dashboard Kendali Admin")
    if 'auth' not in st.session_state: st.session_state.auth = False
    
    if not st.session_state.auth:
        pwd = st.text_input("Password Admin:", type="password")
        if st.button("Authorize Access"):
            if pwd == st.secrets["ADMIN_PASSWORD"]:
                st.session_state.auth = True
                st.rerun()
    else:
        if st.button("Logout Admin"):
            st.session_state.auth = False
            st.rerun()
        
        t1, t2, t3, t4 = st.tabs(["📊 Monitoring", "🚨 Alarm Log", "📲 Antrean Data", "🧾 Invoice"])
        
        with t1:
            st.subheader("Grafik Keamanan Real-time")
            fig = px.pie(values=[94, 6], names=['Aman', 'Anomali'], hole=0.4)
            st.plotly_chart(fig, use_container_width=True)
            
        with t2:
            st.subheader("🚨 Security Alarm Center")
            st.error(f"{datetime.now().strftime('%H:%M')} | 🚨 ANOMALI: Massive Withdrawal Detected | Origin: Proxy-X")
            st.write("14:20 | Login Successful | User: Staff_01")
            
        with t3:
            st.subheader("📲 Antrean Masuk (Overload Control)")
            st.info("Jam: 18:45 | Klien: PT Maju Jaya | Status: ⏳ Menunggu Analisis AI")
            
        with t4:
            st.subheader("🧾 Invoice System")
            inv_c = st.text_input("Nama Perusahaan:")
            inv_p = st.selectbox("Paket:", list(pkgs.keys()))
            if st.button("Generate Invoice"):
                st.success(f"Invoice Berhasil Dibuat untuk {inv_c} Paket {inv_p}")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
