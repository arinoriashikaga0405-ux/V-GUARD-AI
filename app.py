import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. SETUP & STYLE
st.set_page_config(page_title="V-Guard AI Systems", layout="wide")
st.markdown("""<style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #f8f9fa; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 9999; }
    .package-box { padding: 20px; border: 1px solid #eee; border-radius: 10px; background: #fff; height: 500px; }
</style>""", unsafe_allow_html=True)

# 2. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Folder:", ["1. 👤 Profil", "2. 🎯 Visi & Misi", "3. 📦 Paket", "4. 📝 Registrasi", "5. 🔐 Admin"])

# 3. FOLDER 1: PROFIL
if menu == "1. 👤 Profil":
    st.header("👤 Profil Founder")
    st.write("Bapak Erwin Sinaga adalah Pemimpin Bisnis Senior dengan 10+ tahun pengalaman di perbankan. V-Guard AI adalah visinya untuk mengamankan aset UMKM dengan standar audit perbankan menggunakan teknologi AI.")

# 4. FOLDER 2: VISI, MISI & ROI
elif menu == "2. 🎯 Visi & Misi":
    st.info("### 🎯 Visi 2026\nMenjadi standar utama keamanan audit berbasis AI di Indonesia.")
    st.success("### 🚀 Misi Utama\n1. Otomasi Audit 24/7\n2. Deteksi Fraud Instan\n3. Transparansi Aset\n4. Efisiensi Teknologi AI")
    st.write("---")
    st.subheader("📈 Kalkulator ROI (Penyelamatan Aset)")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=500000000)
    st.error(f"🚨 Estimasi Kebocoran (5%): Rp {omzet * 0.05:,.0f}")
    st.success(f"🛡️ Target Penyelamatan V-Guard: Rp {omzet * 0.05 * 0.9:,.0f}")

# 5. FOLDER 3: PRODUK & PAKET
elif menu == "3. 📦 Paket":
    cols = st.columns(4)
    pkgs = [("BASIC", "2.5jt", "750rb"), ("MEDIUM", "7.5jt", "1.5jt"), ("ENTERPRISE", "25jt", "5jt"), ("CORPORATE", "50jt", "10jt")]
    for i, (n, s, m) in enumerate(pkgs):
        with cols[i]:
            st.markdown(f"<div class='package-box'><h3>{n}</h3><p>Setup: {s}<br>Bulanan: {m}</p><hr><ul><li>Audit Harian</li><li>AI Detection</li></ul></div>", unsafe_allow_html=True)

# 6. FOLDER 4: REGISTRASI
elif menu == "4. 📝 Registrasi":
    st.header("📝 Registrasi Nasabah")
    with st.form("reg"):
        st.text_input("Nama Bisnis:")
        st.selectbox("Jenis Usaha:", ["Retail", "F&B", "Jasa", "Corporate"])
        st.text_input("Harga (Sesuai Paket):")
        st.selectbox("Pilih Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        if st.form_submit_button("Kirim"): st.success("Data Terkirim!")

# 7. FOLDER 5: ADMIN (FITUR UNGGAH/TARIK DI SINI)
elif menu == "5. 🔐 Admin":
    st.header("🔐 Admin Dashboard")
    pw = st.text_input("Password Admin:", type="password")
    if pw == "w1nbju8282":
        t1, t2 = st.tabs(["📊 Database", "📤 Kelola File"])
        with t1: st.write("Daftar Nasabah Aktif")
        with t2:
            st.file_uploader("Upload Data Transaksi (.csv/.xlsx)")
            st.button("Tarik Laporan Audit Terakhir")

# 8. FOOTER
st.markdown('<div class="footer">© 2026 V-Guard AI Systems - Secured by Advanced Intelligence</div>', unsafe_allow_html=True)
