import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")
wa_url = "https://wa.me/6282122190885"

# DATA PAKET
pkgs = {
    "MIKRO": {"N": "Basic Guard", "S": "2.500.000", "M": "500.000"},
    "MENENGAH": {"N": "Premium Shield", "S": "7.500.000", "M": "1.500.000"},
    "ENTERPRISE": {"N": "Enterprise Vault", "S": "50.000.000", "M": "5.000.000"},
    "CORPORATE": {"N": "Elite Managed", "S": "85.000.000", "M": "10.000.000"}
}

# 2. SIDEBAR NAVIGASI (URUTAN 1-4)
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Pilih Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🏠 Home: Visi & Misi", 
        "3. 📦 Paket Solusi", 
        "4. 🔐 Admin Panel"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI")

# --- NOMOR 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): 
            st.image("erwin.jpg", use_container_width=True)
        else: 
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250)
    with r:
        st.subheader("Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        st.write("Senior Business Leader dengan pengalaman 10+ tahun sebagai CEO/CSO di industri perbankan.")

# --- NOMOR 2: HOME (VISI, MISI & ROI) ---
elif menu == "2. 🏠 Home: Visi & Misi":
    st.title("🛡️ Visi & Misi V-Guard AI")
    cv, cm = st.columns(2)
    with cv:
        st.subheader("🎯 Visi")
        st.write("Menjadi perantara keamanan AI terdepan yang mendemokratisasi proteksi aset untuk semua skala bisnis.")
    with cm:
        st.subheader("🚀 Misi")
        st.write("Memberikan kepastian keamanan finansial kelas dunia melalui teknologi adaptif.")
    
    st.write("---")
    st.subheader("📈 Kalkulator ROI")
    nt = st.number_input("Transaksi/Bulan:", value=1000)
    vt = st.number_input("Rata-rata Nilai (Rp):", value=500000)
    fp = st.slider("Asumsi Fraud (%):", 0.0, 5.0, 1.2)
    loss = (nt * vt) * (fp / 100)
    st.error(f"Potensi Kerugian: Rp {loss:,.0f}")
    st.success(f"Penyelamatan AI: Rp {loss * 0.99:,.0f}")

# --- NOMOR 3: PAKET SOLUSI ---
elif menu == "3. 📦 Paket Solusi":
    st.title("📦 Paket Solusi & Layanan")
    st.write("Silakan pilih paket investasi keamanan yang sesuai.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.warning("**MIKRO - Basic Guard**")
        st.write(f"Setup: Rp {pkgs['MIKRO']['S']}")
        st.link_button("Pesan via WA", wa_url, use_container_width=True)
    with c2:
        st.warning("**MENENGAH - Premium Shield**")
        st.write(f"Setup: Rp {pkgs['MENENGAH']['S']}")
        st.link_button("Pesan via WA", wa_url, use_container_width=True)
    
    c3, c4 = st.columns(2)
    with c3:
        st.warning("**ENTERPRISE - Enterprise Vault**")
        st.write(f"Setup: Rp {pkgs['ENTERPRISE']['S']}")
        st.link_button("Pesan via WA", wa_url, use_container_width=True)
    with c4:
        st.warning("**CORPORATE - Elite Managed**")
        st.write(f"Setup: Rp {pkgs['CORPORATE']['S']}")
        st.link_button("Pesan via WA", wa_url, use_container_width=True)

# --- NOMOR 4: ADMIN PANEL ---
elif menu == "4. 🔐 Admin Panel":
    st.title("🔐 Admin Dashboard")
    if 'auth' not in st.session_state: st.session_state.auth = False
    
    if not st.session_state.auth:
        pwd = st.text_input("Password Admin:", type="password")
        if st.button("Authorize"):
            if pwd == st.secrets["ADMIN_PASSWORD"]:
                st.session_state.auth = True
                st.rerun()
            else: st.error("Salah!")
    else:
        st.success("Selamat Datang, Pak Erwin.")
        if st.button("Logout"):
            st.session_state.auth = False
            st.rerun()
        st.write("Monitoring internal aktif.")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
