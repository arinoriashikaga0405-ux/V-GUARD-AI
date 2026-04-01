import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE AI ---
K_V = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=K_V)
    v_ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE SESSION ---
if 'db_o' not in st.session_state: st.session_state.db_o = []
if 'db_n' not in st.session_state:
    st.session_state.db_n = [
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Usaha": "F&B", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": 102, "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Usaha": "Otomotif", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 3. CSS CUSTOM (Sesuai Foto Dashboard) ---
st.markdown("""
<style>
    .main { background-color: #ffffff; }
    .stAlert { border-radius: 10px; }
    .fraud-alert { background-color: #ff7675; color: white; padding: 15px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 20px; }
    .photo-frame { border-radius: 10px; border: 2px solid #1e3a8a; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Erwin Sinaga | Senior Business Leader")
    else:
        st.info("Unggah erwin.jpg")
    
    st.write("---")
    nav = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Upload", 
        "5. 🔐 Akses Terbatas"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- 5. LOGIKA HALAMAN ---

if nav == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2]) # Baris 61 Fixed
    with c1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("""Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel.""")

elif nav == "2. 🎯 Visi, Misi & ROI":
    st.header("Strategi & Analisis Proteksi")
    st.info("**Visi:** Menjadi standar emas dalam teknologi pengawasan bisnis digital di Indonesia.")
    st.success("**Misi:** Menyediakan instrumen audit AI untuk mendeteksi indikasi kecurangan secara real-time.")
    st.write("---")
    oz = st.number_input("Omzet Bulanan Bisnis (Rp):", value=100000000)
    bc = oz * 0.07
    st.markdown(f"<p style='color:red;'>Estimasi Kebocoran (7%): Rp {bc:,.0f}</p>", unsafe_allow_html=True)
    st.subheader(f"Dana Berhasil Diselamatkan: Rp {bc - 2500000:,.0f}")
    st.caption("🟢 ROI Positif")

elif nav == "3. 📦 Paket Unggulan":
    st.header("Layanan V-Guard AI")
    cols = st.columns(4)
    pkts = [
        ("BASIC", "Rp 1.5jt", "Monitoring AI, VCS System, Weekly Audit"),
        ("SMART", "Rp 2.5jt", "Monitoring AI, VCS System, Weekly Audit"),
        ("PRO", "Rp 5jt", "Monitoring AI, VCS System, Weekly Audit"),
        ("ELITE", "Rp Custom", "Monitoring AI, VCS System, Weekly Audit")
    ]
    for i, (nama, harga, fitur) in enumerate(pkts):
        with cols[i]:
            st.markdown(f"### {nama}\n**{harga}**\n\n{fitur}")
            st.button(f"Pesan {nama}", key=nama)

elif nav == "4. 📝 Registrasi & Upload":
    st.header("Formulir Pendaftaran Klien")
    with st.form("reg"):
        c1, c2 = st.columns(2)
        n = c1.text_input("Nama Pelanggan:")
        b = c1.text_input("Nama Bisnis:")
        u = c2.text_input("Jenis Usaha:")
        p = c2.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO", "ELITE"])
        st.file_uploader("Upload KTP / Dokumen Pendukung:")
        if st.form_submit_button("Kirim Pendaftaran Ke V-Guard"):
            st.success("Data berhasil dikirim!")

elif nav == "5. 🔐 Akses Terbatas":
    if not st.session_state.auth:
        pw = st.text_input("Security Code:", type="password")
        if st.button("LOGIN"):
            if pw == "w1nbju8282":
                st.session_state.auth = True
                st.rerun()
    else:
        col_h1, col_h2 = st.columns([10, 1])
        col_h1.header("⚙️ Operasional V-Guard AI")
        if col_h2.button("LOGOUT"):
            st.session_state.auth = False
            st.rerun()
            
        st.markdown('<div class="fraud-alert">🚨 PERINGATAN: INDIKASI FRAUD TERDETEKSI PADA TITIK TRANSAKSI HARIAN</div>', unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Database Klien", "📉 Audit Gemini Studio", "📹 Monitoring CCTV", "🧾 Billing"])
        
        with tab1:
            st.subheader("Database Klien Aktif")
            st.table(pd.DataFrame(st.session_state.db_n))
        with tab2:
            st.subheader("Google Studio Gemini Audit")
            st.write("- Skor Integritas Bisnis: **98.5%**")
            st.write("- Efisiensi Penyelamatan Modal: **Tinggi**")
            st.line_chart([1.5, 2.0, 3.0, 2.8])
            if st.button("Tarik Laporan Full"):
                st.write("Generating report...")
        with tab3:
            st.info("Koneksi CCTV/CVV aktif. AI sedang memantau pergerakan kasir.")
        with tab4:
            st.subheader("Estimasi Laba Bersih (60%)")
            total = sum([x['Harga'] for x in st.session_state.db_n])
            st.metric("Total Revenue", f"Rp {total:,.0f}")
            st.metric("Profit Sharing (V-Guard)", f"Rp {total * 0.6:,.0f}")

st.write("---")
st.caption("© 2026 V-Guard AI | Secured by Erwin Sinaga")
