import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI ---
st.set_page_config(page_title="V-Guard AI", layout="wide")
if 'auth' not in st.session_state: st.session_state.auth = False
if 'db' not in st.session_state: st.session_state.db = []

# --- 2. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    m = ["Profil", "Visi Misi", "Produk", "Register", "Login", "Admin"]
    nav = st.radio("Menu:", m)
    st.write("---")
    st.markdown("[💬 Hubungi Admin](https://wa.me/628212190885)")

# --- 3. LOGIKA HALAMAN ---

if nav == "Profil":
    st.header("Profil Kepemimpinan")
    # Teks dipecah agar tidak terpotong saat copy-paste
    p1 = "Bapak **Erwin Sinaga** adalah Founder V-Guard AI Intelligence. "
    p2 = "Beliau memiliki pengalaman 10+ tahun di perbankan dan aset manajemen. "
    p3 = "Berdomisili di Tangerang, beliau membangun ekosistem AI global "
    p4 = "untuk proteksi aset UMKM dan Korporasi dari kebocoran finansial."
    st.write(p1 + p2 + p3 + p4)

elif nav == "Visi Misi":
    st.header("Visi & Misi")
    st.info("Pelopor Global Audit AI dengan Akurasi 99.9%")

elif nav == "Produk":
    st.header("Daftar Produk & Harga")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📦 V-LITE (UMKM)")
        st.write("Pasang: 1jt | Bulanan: 1jt")
    with c2:
        st.subheader("🚀 V-PRO (Retail)")
        st.write("Pasang: 2jt | Bulanan: 2.5jt")

elif nav == "Register":
    st.header("Register & Upload KTP")
    with st.form("f_reg"):
        n = st.text_input("Nama Sesuai KTP:")
        u = st.text_input("Nama Usaha:")
        pkt = st.selectbox("Pilih Paket:", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
        st.file_uploader("Upload KTP (JPG/PNG):")
        if st.form_submit_button("Daftar & Aktivasi"):
            st.session_state.db.append({"Nama": n, "Usaha": u, "Paket": pkt})
            st.success("Data Terkirim ke Folder Admin!")

elif nav == "Login":
    st.header("Dashboard Login Klien")
    st.text_input("Client ID:")
    st.text_input("Password:", type="password")
    st.file_uploader("Upload Data VCS (Excel/CSV):")
    if st.button("Jalankan Audit AI"):
        st.info("AI sedang memproses data...")

elif nav == "Admin":
    if not st.session_state.auth:
        pwd = st.text_input("Sandi Founder:", type="password")
        if st.button("Buka Panel"):
            if pwd == "w1nbju8282":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        st.header("🛡️ CEO Executive Panel")
        if st.button("Logout"):
            st.session_state.auth = False
            st.rerun()
        t1, t2 = st.tabs(["👥 Verifikasi & KTP", "🚨 AI Monitor"])
        with t1:
            if st.session_state.db: st.table(pd.DataFrame(st.session_state.db))
            else: st.write("Tidak ada pendaftar baru.")
        with t2:
            st.metric("Fraud Alert", "Aman")

st.write("---")
st.caption("© 2026 V-Guard AI | Founder")
