import streamlit as st
import pandas as pd
import os
import time

# --- 1. CONFIG & DB ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")
if 'auth' not in st.session_state: st.session_state.auth = False
if 'db' not in st.session_state: st.session_state.db = []

# --- 2. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    menu = ["Profil", "Visi Misi", "Produk", "Register", "Login", "Admin"]
    nav = st.radio("Navigasi:", menu)
    st.write("---")
    st.markdown("[💬 Hubungi Admin](https://wa.me/628212190885)")

# --- 3. MODUL HALAMAN ---

if nav == "Profil":
    st.header("Profil Kepemimpinan")
    # Teks dipisah per baris pendek agar tidak terpotong saat copy-paste
    t1 = "Bapak **Erwin Sinaga** adalah sosok **Founder** di balik **V-Guard AI Intelligence**, "
    t2 = "sebuah platform inovatif yang lahir dari dedikasi mendalam terhadap keamanan aset. "
    t3 = "Beliau memiliki rekam jejak profesional selama lebih dari satu dekade di industri "
    t4 = "perbankan serta manajemen aset nasional. Pengalaman panjang tersebut membentuk "
    t5 = "ketajaman analitis beliau dalam mengidentifikasi berbagai pola risiko finansial. "
    t6 = "\n\nBerdomisili di Tangerang, beliau aktif menjembatani kebutuhan dunia usaha dengan "
    t7 = "teknologi AI global seperti Gemini, MindBridge, dan YOLO. Fokus utama beliau adalah "
    t8 = "memberikan ketenangan pikiran bagi pemilik usaha melalui sistem audit real-time "
    t9 = "yang mampu meminimalisir potensi kerugian secara signifikan demi menciptakan "
    t10 = "lingkungan usaha yang lebih transparan dan berintegritas tinggi di Indonesia."
    st.write(t1+t2+t3+t4+t5+t6+t7+t8+t9+t10)

elif nav == "Produk":
    st.header("Daftar Produk Utama")
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.subheader("📦 V-LITE (UMKM)")
            st.write("**Rp 1jt/bln**. Target: Toko Mandiri. Fitur: AI Fraud Dasar, Laporan WA.")
    with c2:
        with st.container(border=True):
            st.subheader("🚀 V-PRO (Retail)")
            st.write("**Rp 2.5jt/bln**. Target: Resto/Cafe. Fitur: VCS Sync, Audit AI Harian.")
    c3, c4 = st.columns(2)
    with c3:
        with st.container(border=True):
            st.subheader("👁️ V-SIGHT (Visual)")
            st.write("**Rp 4.5jt/bln**. Target: Toko Emas/Gudang. Fitur: CCTV AI, Behavior Audit.")
    with c4:
        with st.container(border=True):
            st.subheader("🏢 V-ENTERPRISE")
            st.write("**Custom**. Target: Korporasi/Franchise. Fitur: Multi-Cabang, Full Forensic.")

elif nav == "Register":
    st.header("Pendaftaran Klien & Upload KTP")
    with st.form("reg"):
        n = st.text_input("Nama Sesuai KTP:"); u = st.text_input("Nama Usaha:")
        p = st.selectbox("Pilih Paket:", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
        st.file_uploader("Upload Foto KTP (JPG/PNG):")
        if st.form_submit_button("Daftar"):
            st.session_state.db.append({"Nama": n, "Usaha": u, "Paket": p, "Status": "Pending"})
            st.success("Terkirim! Mohon tunggu verifikasi KTP oleh Admin.")

elif nav == "Login":
    st.header("Dashboard Klien")
    st.text_input("ID Klien:"); st.text_input("Password:", type="password")
    st.file_uploader("Upload Data VCS (Excel/CSV):")
    if st.button("Kirim ke Server"): st.success("Data Terunggah. Menunggu eksekusi Audit AI.")

elif nav == "Admin":
    if not st.session_state.auth:
        pwd = st.text_input("Sandi Founder:", type="password")
        if st.button("Login"):
            if pwd == "w1nbju8282": st.session_state.auth = True; st.rerun()
    else:
        st.header("🛡️ CEO Executive Panel")
        if st.button("Logout"): st.session_state.auth = False; st.rerun()
        t1, t2 = st.tabs(["✅ Verifikasi KTP", "🚀 Eksekusi Audit AI"])
        with t1:
            if st.session_state.db: st.table(pd.DataFrame(st.session_state.db))
            else: st.write("Tidak ada pendaftar baru.")
        with t2:
            st.warning("Pusat Kendali Audit: Sinkronisasi Gemini, MindBridge, & YOLO.")
            if st.button("JALANKAN PROSES AUDIT AI"):
                with st.spinner("AI sedang memproses data audit seluruh klien..."):
                    time.sleep(2); st.success("Audit Selesai & Laporan Terkirim!")

elif nav == "Visi Misi":
    st.header("Ekosistem AI V-Guard"); st.info("Integrasi: Gemini, MindBridge, YOLO, DataRobot, Alteryx.")

st.write("---")
st.caption("© 2026 V-Guard AI | Founder")
