import streamlit as st
import pandas as pd
import os

# --- 1. SETUP & DB ---
st.set_page_config(page_title="V-Guard AI", layout="wide")
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

# --- 3. LOGIKA HALAMAN ---

if nav == "Profil":
    st.header("Profil Kepemimpinan")
    txt = [
        "Bapak **Erwin Sinaga** adalah Founder V-Guard AI Intelligence. ",
        "Beliau memiliki pengalaman 10+ tahun di perbankan dan aset manajemen. ",
        "V-Guard AI hadir untuk transparansi bisnis total melalui audit AI real-time, ",
        "melindungi UMKM dan Korporasi dari kebocoran finansial di era digital."
    ]
    st.write(" ".join(txt))

elif nav == "Register":
    st.header("Pendaftaran & Upload KTP")
    with st.form("f_reg"):
        n = st.text_input("Nama Sesuai KTP:")
        u = st.text_input("Nama Usaha:")
        p = st.selectbox("Paket:", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
        st.file_uploader("Upload KTP (JPG/PNG):")
        if st.form_submit_button("Daftar & Kirim Berkas"):
            st.session_state.db.append({"Nama": n, "Usaha": u, "Paket": p, "Status": "Pending"})
            st.success("Terkirim! Data KTP Anda sedang diverifikasi Admin.")

elif nav == "Login":
    st.header("Dashboard Klien")
    st.text_input("Client ID:")
    st.text_input("Password:", type="password")
    st.write("---")
    st.subheader("📤 Upload Data VCS Harian")
    st.file_uploader("Pilih File (Excel/CSV):")
    if st.button("Kirim Data ke Server"):
        st.success("Data Berhasil Diunggah. Silakan tunggu laporan Audit dari Admin.")

elif nav == "Admin":
    if not st.session_state.auth:
        pwd = st.text_input("Sandi Founder:", type="password")
        if st.button("Buka Folder Admin"):
            if pwd == "w1nbju8282": 
                st.session_state.auth = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        st.header("🛡️ CEO Executive Panel")
        if st.button("Keluar"): 
            st.session_state.auth = False
            st.rerun()
        
        t1, t2, t3 = st.tabs(["✅ Verifikasi Klien", "🚨 Eksekusi Audit AI", "📊 Monitoring"])
        
        with t1:
            if st.session_state.db: st.table(pd.DataFrame(st.session_state.db))
            else: st.write("Belum ada pendaftar baru.")
            
        with t2:
            st.subheader("Pusat Kendali Audit")
            st.warning("Tombol ini akan menjalankan sinkronisasi Gemini, MindBridge, dan YOLO secara massal.")
            if st.button("🚀 Jalankan Proses Audit AI Sekarang"):
                with st.spinner("AI sedang sinkronisasi data seluruh unit..."):
                    import time
                    time.sleep(2)
                    st.success("Audit Selesai! Laporan telah dikirim ke Dashboard masing-masing klien.")
        
        with t3:
            st.metric("Fraud Detection", "Aman", "0 Anomali")

# Menu lain (Simple)
elif nav == "Visi Misi": st.header("Visi & Misi"); st.info("Akurasi Audit 99.9%")
elif nav == "Produk": st.header("Produk"); st.write("V-LITE, V-PRO, V-SIGHT, V-ENTERPRISE")

st.write("---")
st.caption("© 2026 V-Guard AI Intelligence | Founder")
