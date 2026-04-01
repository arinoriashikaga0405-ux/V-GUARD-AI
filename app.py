import streamlit as st
import pandas as pd
import os
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. SESSION STATE (Penyimpanan Data & Auth) ---
if 'admin_authed' not in st.session_state:
    st.session_state.admin_authed = False

# --- 3. SIDEBAR (Urutan Navigasi Statis) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    menu = [
        "Profil Kepemimpinan", "Visi dan Misi", "Daftar Produk Utama", 
        "Register Pelanggan", "Dashboard Login", "Admin Panel"
    ]
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
        with st.container(border=True):
            st.write("""
            Bapak **Erwin Sinaga** adalah sosok **Founder** di balik **V-Guard AI Intelligence**. 
            Beliau memiliki rekam jejak profesional selama lebih dari satu dekade di industri perbankan 
            dan manajemen aset nasional. V-Guard AI dibangun untuk memberikan transparansi total 
            bagi pemilik bisnis melalui sistem audit real-time berbasis AI guna meminimalisir risiko kerugian.
            """)

elif nav == "Visi dan Misi":
    st.header("Visi dan Misi Perusahaan")
    v1, v2 = st.columns(2)
    with v1:
        st.info("### 🎯 Visi\nMenjadi pelopor global teknologi audit digital berbasis AI.")
    with v2:
        st.success("### 🚀 Misi\n1. Proteksi aset via Fraud Detection.\n2. Efisiensi operasional.\n3. Bisnis bebas kebocoran.")

elif nav == "Daftar Produk Utama":
    st.header("Daftar Produk & Analisis ROI")
    with st.expander("📊 Simulasi ROI (Return on Investment)", expanded=True):
        oz = st.number_input("Omzet Bulanan (Rp):", value=100000000)
        rugi = oz * 0.07
        st.metric("Potensi Rugi Tanpa AI (7%)", f"Rp {rugi:,.0f}")
        st.metric("Aset Aman V-Guard AI", f"Rp {rugi*0.9:,.0f}")
    
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.subheader("📦 V-LITE")
            st.write("- **Alarm Fraud:** WA\n- **Invoice:** Digital\n- **Audit:** Laporan Bulanan")
            st.write("**Pasang: 1jt | Bulan: 1jt**")
    with c2:
        with st.container(border=True):
            st.subheader("🚀 V-PRO")
            st.write("- **VCS:** Sync Stok & Kasir\n- **CCTV:** Behavior AI\n- **Audit:** AI Otomatis")
            st.write("**Pasang: 2jt | Bulan: 2.5jt**")

elif nav == "Register Pelanggan":
    st.header("Pendaftaran Pelanggan Baru")
    with st.form("reg_form"):
        st.text_input("Nama Lengkap Pemilik:")
        st.text_input("Nama Usaha:")
        # Penentuan Waktu Upload Berdasarkan Jenis Usaha
        usaha_type = st.selectbox("Jenis Usaha:", ["Retail/Minimarket", "Restoran/Cafe", "Laundry/Jasa", "Gudang/Distribusi"])
        st.selectbox("Pilih Paket:", ["V-LITE (1jt)", "V-PRO (2.5jt)", "V-SIGHT (4.5jt)", "V-ENTERPRISE"])
        
        # Penjelasan Jam Upload
        if usaha_type == "Retail/Minimarket": jam = "22:00 - 23:00 WIB"
        elif usaha_type == "Restoran/Cafe": jam = "23:00 - 00:00 WIB"
        else: jam = "00:00 - 01:00 WIB"
        
        st.warning(f"Slot Jam Upload Data Anda: {jam} (Untuk mencegah overload server)")
        st.file_uploader("Upload KTP:", type=["jpg", "png", "jpeg"])
        if st.form_submit_button("Kirim Pendaftaran"):
            st.success(f"Berhasil! Jadwal sinkronisasi data Anda disetel pada {jam}.")

elif nav == "Dashboard Login":
    st.header("Portal Klien V-Guard AI")
    st.info("Fitur: VCS, CCTV Live, & Laporan Audit")
    u = st.text_input("User ID:")
    p = st.text_input("Password:", type="password")
    if st.button("Masuk Dashboard"):
        st.write("### 📊 Laporan Rugi Laba Terkini")
        st.write("### 🚨 Hasil Audit AI: 1 Anomali Ditemukan")
        st.write("### 📹 CCTV Cloud Monitoring Aktif")

elif nav == "Admin Panel":
    st.header("🛡️ CEO Executive Panel (Pak Erwin)")
    if not st
