import streamlit as st
import pandas as pd
import os
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. SESSION STATE (Database Simulasi & Auth) ---
if 'admin_authed' not in st.session_state:
    st.session_state.admin_authed = False
if 'klien_db' not in st.session_state:
    st.session_state.klien_db = [] # Database klien baru

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    menu = ["Profil Kepemimpinan", "Visi dan Misi", "Daftar Produk Utama", 
            "Register Pelanggan", "Dashboard Login", "Admin Panel"]
    nav = st.radio("Navigasi Utama:", menu)
    st.write("---")
    st.markdown('<a href="https://wa.me/628212190885" target="_blank" style="background-color:#25d366;color:white;padding:10px;border-radius:8px;text-decoration:none;display:block;text-align:center;font-weight:bold;">💬 Hubungi Admin</a>', unsafe_allow_html=True)

# --- 4. LOGIKA MENU ---

if nav == "Profil Kepemimpinan":
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga — Founder")
    with col2:
        st.write("""
        Bapak **Erwin Sinaga** adalah sosok **Founder** V-Guard AI Intelligence. 
        Dengan pengalaman lebih dari satu dekade di perbankan dan aset manajemen, 
        beliau membangun V-Guard AI untuk memastikan transparansi mutlak bagi pengusaha 
        melalui audit real-time berbasis kecerdasan buatan.
        """)

elif nav == "Daftar Produk Utama":
    st.header("Solusi V-Guard AI")
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.subheader("📦 V-LITE")
            st.write("Pasang: 1jt | Bulan: 1jt\n- AI Fraud Dasar\n- Laporan WA")
    with c2:
        with st.container(border=True):
            st.subheader("🚀 V-PRO")
            st.write("Pasang: 2jt | Bulan: 2.5jt\n- VCS Integrasi\n- Audit AI Harian")

elif nav == "Register Pelanggan":
    st.header("Formulir Pendaftaran Klien Baru")
    with st.form("reg_klien"):
        nama_p = st.text_input("Nama Pemilik:")
        nama_u = st.text_input("Nama Usaha:")
        u_type = st.selectbox("Bidang Usaha:", ["Retail", "Restoran", "Jasa"])
        paket = st.selectbox("Paket:", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
        
        # Smart Scheduling
        jam = "22:00" if u_type == "Retail" else "23:00" if u_type == "Restoran" else "00:00"
        st.info(f"Slot Sinkronisasi Data: Jam {jam} WIB")
        
        if st.form_submit_button("Daftar Sekarang"):
            new_client = {"Nama": nama_p, "Usaha": nama_u, "Bidang": u_type, "Paket": paket, "Status": "Menunggu Aktivasi", "Jam": jam}
            st.session_state.klien_db.append(new_client)
            st.success("Data terkirim ke Admin. Silakan tunggu aktivasi.")

elif nav == "Dashboard Login":
    st.header("Portal Klien & VCS Input")
    st.info("Upload data harian Anda di bawah ini sesuai jadwal.")
    with st.container(border=True):
        st.text_input("ID Klien:")
        file_vcs = st.file_uploader("Upload Data Penjualan/Stok (CSV/Excel):", type=['csv', 'xlsx'])
        if st.button("Kirim ke VCS AI"):
            if file_vcs:
                st.success("Data diterima! AI sedang memproses Audit & Laba Rugi...")
                st.balloons()
            else: st.warning("Pilih file terlebih dahulu.")

elif nav == "Admin Panel":
    if not st.session_state.admin_authed:
        st.header("🛡️ Restricted Access")
        pwd = st.text_input("Sandi Otoritas:", type="password")
        if st.button("Verifikasi"):
            if pwd == "w1nbju8282":
                st.session_state.admin_authed = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        st.header("🛡️ Central Management")
        if st.button("Logout"):
            st.session_state.admin_authed = False
            st.rerun()
        
        t1, t2, t3 = st.tabs(["✅ Aktivasi Klien", "🚨 Monitoring AI", "⚙️ Database VCS"])
        
        with t1:
            st.subheader("Persetujuan Klien Baru")
            if st.session_state.klien_db:
                df = pd.DataFrame(st.session_state.
