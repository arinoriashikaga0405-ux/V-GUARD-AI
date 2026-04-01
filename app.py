import streamlit as st
import pandas as pd
import os
import time

# 1. SETUP & DB
st.set_page_config(page_title="V-Guard AI", layout="wide")
if 'auth' not in st.session_state: st.session_state.auth = False
if 'db' not in st.session_state: st.session_state.db = []

# 2. SIDEBAR
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    menu = ["Profil", "Produk", "Register", "Login", "Admin"]
    nav = st.radio("Navigasi:", menu)
    st.write("---")
    st.markdown("[💬 Hubungi Admin](https://wa.me/628212190885)")

# 3. MODUL HALAMAN
if nav == "Profil":
    st.header("Profil Kepemimpinan")
    st.write("""
    Bapak **Erwin Sinaga** adalah Founder V-Guard AI Intelligence. 
    Dengan pengalaman 10+ tahun di perbankan, beliau membangun ekosistem 
    AI global (Gemini, MindBridge, YOLO) untuk transparansi bisnis total. 
    Berdomisili di Tangerang, beliau berkomitmen melindungi aset pengusaha 
    melalui audit real-time guna mencegah kebocoran finansial.
    """)

elif nav == "Produk":
    st.header("Daftar Produk & Harga")
    c1, c2 = st.columns(2)
    with c1:
        st.info("**📦 V-LITE (UMKM)**\n\nRp 1jt/bln. Target: Toko Mandiri.")
    with c2:
        st.success("**🚀 V-PRO (Retail)**\n\nRp 2.5jt/bln. Target: Resto/Cafe.")

elif nav == "Register":
    st.header("Pendaftaran & Upload KTP")
    with st.form("f_reg"):
        n = st.text_input("Nama Sesuai KTP:")
        u = st.text_input("Nama Usaha:")
        p = st.selectbox("Paket:", ["V-LITE", "V-PRO", "V-SIGHT"])
        st.file_uploader("Upload Foto KTP:")
        if st.form_submit_button("Daftar & Kirim"):
            st.session_state.db.append({"Nama": n, "Usaha": u, "Paket": p})
            st.success("Data Terkirim! Mohon tunggu verifikasi Admin.")

elif nav == "Login":
    st.header("Dashboard Klien")
    st.text_input("ID Klien:"); st.text_input("Password:", type="password")
    st.file_uploader("Upload Data VCS (Excel/CSV):")
    if st.button("Kirim ke Server"): st.success("Data Terunggah ke Admin.")

elif nav == "Admin":
    if not st.session_state.auth:
        pwd = st.text_input("Sandi Founder:", type="password")
        if st.button("Login"):
            if pwd == "w1nbju8282": st.session_state.auth = True; st.rerun()
            else: st.error("Salah!")
    else:
        st.header("🛡️ CEO Executive Panel")
        if st.button("Logout"): st.session_state.auth = False; st.rerun()
        t1, t2 = st.tabs(["✅ Verifikasi KTP", "🚀 Eksekusi Audit AI"])
        with t1:
            if st.session_state.db: st.table(pd.DataFrame(st.session_state.db))
            else: st.write("Kosong.")
        with t2:
            if st.button("JALANKAN PROSES AUDIT AI"):
                with st.spinner("AI sedang memproses data audit..."):
                    time.sleep(2); st.success("Audit Selesai!")

st.write("---")
st.caption("© 2026 V-Guard AI | Founder")
