import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database & Login State
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25 08:00", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "MEDIUM", "Harga": 7500000, "Status": "🟢 AKTIF", "Jatuh_Tempo": "2026-04-25", "Log": "System Initialized"}
    ]

# FITUR: Login hanya sekali
if 'admin_authenticated' not in st.session_state:
    st.session_state.admin_authenticated = False

# 2. CSS CUSTOM (Alarm & Styling)
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .fraud-alert { background: #f8d7da; color: #721c24; padding: 20px; border-radius: 10px; border-left: 10px solid #dc3545; font-weight: bold; animation: blinker 1s linear infinite; margin-bottom: 15px; }
    .piutang-box { background: #fff3cd; color: #856404; padding: 15px; border-radius: 10px; border-left: 10px solid #ffc107; margin-bottom: 10px; font-weight: bold; }
    @keyframes blinker { 50% { opacity: 0.2; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi Utama:", ["1. 👤 Profil Founder", "2. 🎯 Visi & ROI", "3. 📦 Paket Unggulan", "4. 📝 Registrasi & Capture", "5. 🔐 Admin Control Center", "6. 📜 Laporan Audit Klien"])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- MENU 5: ADMIN CONTROL CENTER ---
if menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Control")

    # LOGIKA: Tampilkan input password hanya jika belum login
    if not st.session_state.admin_authenticated:
        pw = st.text_input("Sandi Otoritas:", type="password")
        if pw == "w1nbju8282":
            st.session_state.admin_authenticated = True
            st.rerun() # Refresh untuk menghilangkan kolom password
        elif pw != "":
            st.error("Akses Ditolak: Sandi Salah.")
    
    # JIKA SUDAH LOGIN, TAMPILKAN DASHBOARD (TANPA KOLOM PASSWORD)
    else:
        # Tombol Logout (Opsional, di pojok kanan)
        if st.button("🔓 Logout Admin"):
            st.session_state.admin_authenticated = False
            st.rerun()

        df = pd.DataFrame(st.session_state.db_nasabah)
        
        # A. TAMBAH AKUN KLIEN
        with st.expander("➕ TAMBAH AKUN KLIEN BARU"):
            with st.form("admin_add"):
                c1, c2 = st.columns(2)
                new_pic = c1.text_input("Nama PIC:")
                new_bis = c1.text_input("Nama Bisnis:")
                new_pkt = c2.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
                new_hrg = c2.number_input("Harga (Rp):", value=2500000)
                if st.form_submit_button("Daftarkan Klien"):
                    new_id = st.session_state.db_nasabah[-1]["ID"] + 1
                    st.session_state.db_nasabah.append({
                        "ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"), "Pelanggan": new_
