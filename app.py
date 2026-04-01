import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI DASAR ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# Inisialisasi Database Internal (Agar Data Tidak Hilang saat Refresh)
if 'admin_authed' not in st.session_state: st.session_state.admin_authed = False
if 'db_klien' not in st.session_state: st.session_state.db_klien = []

# --- 2. SIDEBAR (NAVIGASI STATIS) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    # Urutan Navigasi Sesuai SOP
    menu = ["Profil", "Visi Misi", "Produk", "Register", "Login", "Admin"]
    nav = st.radio("Navigasi:", menu)
    st.write("---")
    st.markdown("[💬 Hubungi Admin](https://wa.me/628212190885)")

# --- 3. MODUL HALAMAN (Pemisah Fitur) ---

def hal_profil():
    st.header("Profil Kepemimpinan")
    st.write("""
    Bapak **Erwin Sinaga** adalah Founder V-Guard AI Intelligence. 
    Dengan pengalaman 10+ tahun di perbankan dan aset manajemen, 
    beliau membangun V-Guard AI untuk transparansi bisnis total 
    melalui audit AI real-time, melindungi UMKM dan Korporasi 
    dari kebocoran finansial di era digital secara menyeluruh.
    """)

def hal_produk():
    st.header("Solusi V-Guard AI")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📦 V-LITE")
        st.write("Pasang: 1jt | Bulan: 1jt\n- AI Fraud Dasar\n- Laporan WA")
    with c2:
        st.subheader("🚀 V-PRO")
        st.write("Pasang: 2jt | Bulan: 2.5jt\n- VCS Stok/Bank\n- Audit AI Harian")

def hal_register():
    st.header("Pendaftaran Klien Baru")
    with st.form("f_reg"):
        n_p = st.text_input("Nama Pemilik:")
        n_u = st.text_input("Nama Usaha:")
        u_t = st.selectbox("Usaha:", ["Retail", "Resto", "Jasa"])
        if st.form_submit_button("Daftar"):
            st.session_state.db_klien.append({"Nama": n_p, "Usaha": n_u, "Tipe": u_t})
            st.success("Terkirim! Mohon tunggu aktivasi Admin.")

def hal_admin():
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
            st.session_state.admin_authed = False
            st.rerun()
        t1, t2 = st.tabs(["✅ Aktivasi Klien", "📊 AI Monitor"])
        with t1:
            if st.session_state.db_klien:
                st.table(pd.DataFrame(st.session_state.db_klien))
                if st.button("Aktifkan"): st.success("Klien Aktif!")
            else: st.write("Belum ada pendaftar.")
        with t2:
            st.metric("Fraud Alert", "Aman")
            st.metric("VCS Accuracy", "99.8%")

# --- 4. ROUTING UTAMA ---
if nav == "Profil": hal_profil()
elif nav == "Visi Misi": st.header("Visi & Misi"); st.info("Pelopor Audit AI.")
elif nav == "Produk": hal_produk()
elif nav == "Register": hal_register()
elif nav == "Login": st.header("Portal VCS"); st.file_uploader("Upload Data:"); st.button("Proses AI")
elif nav == "Admin": hal_admin()

st.write("---")
st.caption("© 2026 V-Guard AI | Founder")
