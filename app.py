import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE SEDERHANA ---
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 3. SIDEBAR (Tanpa Angka) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    menu = [
        "Profil Kepemimpinan & ROI", 
        "Daftar 4 Produk Utama", 
        "Register Pelanggan", 
        "Dashboard Login", 
        "Admin Panel"
    ]
    nav = st.radio("Navigasi Utama:", menu)
    st.write("---")
    st.markdown('<a href="https://wa.me/628212190885" target="_blank" style="background-color:#25d366;color:white;padding:10px;border-radius:8px;text-decoration:none;display:block;text-align:center;font-weight:bold;">💬 Hubungi Admin</a>', unsafe_allow_html=True)

# --- 4. LOGIKA MENU (Struktur IF-ELIF Lengkap) ---

if nav == "Profil Kepemimpinan & ROI":
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
            dan manajemen aset nasional. Pengalaman ini membentuk ketajaman analitis beliau dalam 
            mendeteksi kebocoran finansial yang luput dari sistem konvensional. 
            
            V-Guard AI dibangun sebagai benteng pertahanan digital untuk memberikan ketenangan 
            pikiran bagi pemilik usaha melalui audit real-time berbasis AI yang transparan dan disiplin.
            """)
    
    st.write("---")
    st.subheader("Visi, Misi & Analisis ROI")
    v1, v2 = st.columns(2)
    with v1: st.info("**Visi:** Pelopor audit digital AI global.")
    with v2: st.success("**Misi:** Proteksi aset UMKM & Fraud Detection.")
    
    oz = st.number_input("Input Omzet Bulanan (Rp):", value=100000000)
    rugi = oz * 0.07
    st.metric("Potensi Rugi Tanpa AI (7%)", f"Rp {rugi:,.0f}")
    st.metric("Aset Aman Dengan V-Guard AI", f"Rp {rugi*0.9:,.0f}")

elif nav == "Daftar 4 Produk Utama":
    st.header("Solusi Keamanan Aset V-Guard AI")
    st.info("Fitur Utama: Alarm Fraud, Invoice Notif, Laba-Rugi, & Audit Otomatis")
    
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.subheader("📦 V-LITE (Basic)")
            st.write("**Fitur Utama:**\n- Alarm Fraud: Notif WA\n- Invoice: Digital Notif\n- Laporan: Laba Rugi Bulanan\n- Audit: Laporan Self-Audit")
            st.write("💰 **Pasang:** 1jt | **Bulan:** 1jt")
            st.link_button("Pesan V-LITE", "https://wa.me/628212190885?text=Pesan%20V-LITE")

        with st.container(border=True):
            st.subheader("👁️ V-SIGHT (Visual)")
            st.write("**Fitur Utama:**\n- Alarm Fraud: Real-Time + Foto\n- Invoice: Sync Struk & Video\n- Laporan: Analisis ROI Aset\n- Audit: Perilaku Visual AI")
            st.write("💰 **Pasang:** 3.5jt | **Bulan:** 4.5jt")
            st.link_button("Pesan V-SIGHT", "https://wa.me/628212190885?text=Pesan%20V-SIGHT")

    with c2:
        with st.container(border=True):
            st.subheader("🚀 V-PRO (Standard)")
            st.write("**Fitur Utama:**\n- Alarm Fraud: Real-Time Push\n- Invoice: Auto-Invoice & Stok\n- Laporan: Laba Rugi Harian\n- Audit: Audit AI Otomatis")
            st.write("💰 **Pasang:** 2jt | **Bulan:** 2.5jt")
            st.link_button("Pesan V-PRO", "https://wa.me/628212190885?text=Pesan%20V-PRO")

        with st.container(border=True):
            st.subheader("🏢 V-ENTERPRISE")
            st.write("**Fitur Utama:**\n- Alarm Fraud: Investigasi Tim\n- Invoice: Custom Billing API\n- Laporan: Konsolidasi Cabang\n- Audit: Forensik Digital")
            st.write("💰 **Pasang:** Custom | **Bulan:** 10jt++")
            st.link_button("Hubungi Admin", "https://wa.me/628212190885?text=Pesan%20ENTERPRISE")

elif nav == "Register Pelanggan":
    st.header("Form Pendaftaran")
    with st.form("f_reg"):
        st.text_input("Nama Pemilik:")
        st.text_input("Nama Usaha:")
        st.selectbox("Pilih Produk:", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
        st.file_uploader("Upload KTP:", type=["jpg", "png", "jpeg"])
        if st.form_submit_button("Daftar Sekarang"):
            st.success("Terkirim ke Admin!")

elif nav == "Dashboard Login":
    st.header("Portal Klien")
    st.text_input("User ID:")
    st.text_input("Password:", type="password")
    st.button("Masuk")

elif nav == "Admin Panel":
    st.header("Executive Panel")
    pwd = st.text_input("Sandi Otoritas:", type="password")
    if st.button("Buka Data"):
        if pwd == "w1nbju8282":
            st.success("Akses Diterima, Selamat Datang Founder.")
        else: st.error("Sandi Salah")

st.write("---")
st.caption("© 2026 V-Guard AI Intelligence | Erwin Sinaga — Founder")
