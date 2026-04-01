import streamlit as st
import pandas as pd
import os

# --- 1. SETTING ---
st.set_page_config(page_title="V-Guard AI", layout="wide")

# --- 2. DATA STORAGE ---
if 'admin_authed' not in st.session_state:
    st.session_state.admin_authed = False
if 'db_reg' not in st.session_state:
    st.session_state.db_reg = []

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    menu = ["Profil Kepemimpinan", "Visi dan Misi", "Daftar Produk Utama", 
            "Register Pelanggan", "Dashboard Login", "Admin Panel"]
    nav = st.radio("Menu:", menu)
    st.write("---")
    wa = "https://wa.me/628212190885"
    st.markdown(f'[💬 Hubungi Admin]({wa})')

# --- 4. LOGIKA MENU ---

if nav == "Profil Kepemimpinan":
    st.header("Profil Kepemimpinan")
    st.write("""
    Bapak **Erwin Sinaga** adalah sosok **Founder** V-Guard AI Intelligence. 
    Dengan pengalaman lebih dari satu dekade di perbankan dan aset manajemen, 
    beliau membangun V-Guard AI untuk memastikan transparansi mutlak bagi pengusaha 
    melalui audit real-time berbasis kecerdasan buatan. Beliau berkomitmen membantu 
    UMKM dan Korporasi di Indonesia mengamankan aset dari risiko kebocoran finansial.
    """)

elif nav == "Daftar Produk Utama":
    st.header("Solusi V-Guard AI")
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.subheader("📦 V-LITE")
            st.write("Pasang: 1jt | Bulan: 1jt")
            st.write("- AI Fraud Dasar\n- Laporan Bulanan WA")
    with c2:
        with st.container(border=True):
            st.subheader("🚀 V-PRO")
            st.write("Pasang: 2jt | Bulan: 2.5jt")
            st.write("- VCS Integrasi\n- Audit AI Harian")

elif nav == "Register Pelanggan":
    st.header("Pendaftaran Klien Baru")
    with st.form("f_reg"):
        n_p = st.text_input("Nama Pemilik:")
        n_u = st.text_input("Nama Usaha:")
        u_t = st.selectbox("Usaha:", ["Retail", "Resto", "Jasa"])
        if st.form_submit_button("Daftar Sekarang"):
            st.session_state.db_reg.append({"Nama": n_p, "Usaha": n_u, "Tipe": u_t})
            st.success("Terkirim! Tunggu Aktivasi Admin.")

elif nav == "Dashboard Login":
    st.header("Portal Klien & VCS")
    st.info("Input Data VCS untuk Audit AI")
    st.text_input("User ID:")
    f_vcs = st.file_uploader("Upload Data (CSV/Excel):")
    if st.button("Proses Data"):
        st.success("AI sedang memproses Audit & Laba Rugi...")

elif nav == "Admin Panel":
    if not st.session_state.admin_authed:
        st.header("🛡️ Restricted Access")
        pwd = st.text_input("Sandi:", type="password")
        if st.button("Login"):
            if pwd == "w1nbju8282":
                st.session_state.admin_authed = True
                st.rerun()
            else: st.error("Salah!")
    else:
        st.header("🛡️ Central Management")
        if st.button("Logout"):
            st.session_
