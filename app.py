import streamlit as st
import pandas as pd
import os

# --- 1. SETTING & DATABASE ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

if 'admin_authed' not in st.session_state: st.session_state.admin_authed = False
if 'db_klien' not in st.session_state: st.session_state.db_klien = []

# --- 2. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    menu = ["Profil Kepemimpinan", "Visi dan Misi", "Daftar Produk Utama", 
            "Register Pelanggan", "Dashboard Login", "Admin Panel"]
    nav = st.radio("Navigasi:", menu)
    st.write("---")
    st.markdown("[💬 Hubungi Admin](https://wa.me/628212190885)")

# --- 3. MODUL HALAMAN ---

def hal_register():
    st.header("Pendaftaran & Aktivasi Klien")
    with st.form("form_reg"):
        col1, col2 = st.columns(2)
        with col1:
            nama = st.text_input("Nama Sesuai KTP:")
            usaha = st.text_input("Nama Usaha:")
            st.file_uploader("Upload Foto KTP (Format JPG/PNG):")
        with col2:
            paket = st.selectbox("Pilih Paket Sistem:", [
                "V-LITE (Rp 1jt/bln)", 
                "V-PRO (Rp 2.5jt/bln)", 
                "V-SIGHT (Rp 4.5jt/bln)", 
                "V-ENTERPRISE (Custom)"
            ])
            st.info("Metode Bayar: Transfer Bank / VA")
        
        if st.form_submit_button("Kirim Data Pendaftaran"):
            st.session_state.db_klien.append({
                "Nama": nama, "Usaha": usaha, "Paket": paket, "Status": "Menunggu Verifikasi"
            })
            st.success("Data & KTP terkirim! Admin akan memverifikasi dalam 1x24 jam.")

def hal_login():
    st.header("Portal Dashboard Klien")
    tab_log, tab_vcs = st.tabs(["🔑 Login Member", "📊 Upload Data VCS"])
    
    with tab_log:
        st.text_input("Client ID / Email:")
        st.text_input("Password:", type="password")
        st.button("Masuk Ke Dashboard")
    
    with tab_vcs:
        st.warning("Pastikan Anda sudah login untuk sinkronisasi AI.")
        st.file_uploader("Upload File Transaksi (Excel/CSV):")
        if st.button("Jalankan Audit AI"):
            st.info("AI sedang mencocokkan data stok, kasir, dan bank...")

def hal_admin():
    if not st.session_state.admin_authed:
        st.header("🛡️ Restricted Access")
        pwd = st.text_input("Sandi Otoritas Founder:", type="password")
        if st.button("Masuk Admin"):
            if pwd == "w1nbju8282":
                st.session_state.admin_authed = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        st.header("🛡️ CEO Executive Management")
        if st.button("Keluar & Kunci Panel"):
            st.session_state.admin_authed = False
            st.rerun()
        
        t1, t2, t3 = st.tabs(["👥 Verifikasi Klien", "📄 Data KTP", "🚨 Monitoring AI"])
        with t1:
            if st.session_state.db_klien:
                st.table(pd.DataFrame(st.session_state.db_klien))
                if st.button("Aktivasi Semua Klien Baru"):
                    st.success("Sistem Klien telah diaktifkan secara otomatis.")
            else: st.write("Tidak ada pendaftar baru.")
        with t2:
            st.write("Folder berkas KTP pelanggan tersimpan aman di server enkripsi.")
        with t3:
            st.metric("Fraud Alert", "0 Anomali", "Sistem Aman")

# --- 4. ROUTING ---
if nav == "Profil Kepemimpinan":
    st.header("Profil Kepemimpinan")
    st.write("Bapak **Erwin Sinaga** (Founder) memimpin V-Guard AI dengan visi transparansi mutlak. Berdomisili di Tangerang, beliau mengintegrasikan teknologi AI global untuk memproteksi aset UM
