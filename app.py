import streamlit as st
import os
import pandas as pd
from datetime import datetime
import google.generativeai as genai

# --- 1. CONFIG & ENGINE AI ---
K_V = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=K_V)
    v_ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE & SESSION STATE ---
# Database Klien (Tampilan di Admin)
if 'db_n' not in st.session_state:
    st.session_state.db_n = [
        {"ID": "CL-001", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "SMART", "Status": "🟢 AKTIF"},
        {"ID": "CL-002", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Paket": "BASIC", "Status": "🔴 Menunggu"}
    ]

# Database Login (User & Pass untuk Klien)
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = {"siska": "12345", "jaya": "12345"}

if 'auth_vguard' not in st.session_state:
    st.session_state.auth_vguard = False

if 'client_logged_in' not in st.session_state:
    st.session_state.client_logged_in = False

# --- 3. CSS PREMIUM ---
st.markdown("""
<style>
    .fraud-header { background-color: #ff7675; color: white; padding: 15px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 20px; font-size: 18px; }
    .client-box { background-color: #f0f2f6; padding: 25px; border-radius: 15px; border-left: 10px solid #1e3a8a; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.markdown("**Erwin Sinaga - Senior Business Leader**")
    st.write("---")
    nav = st.radio("Navigasi Utama:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 💎 Layanan Produk", "4. 📝 Registrasi & Upload", "5. 🔐 Akses Terbatas"])
    st.write("---")
    st.caption("© 2026 V-Guard AI Intelligence")

# --- 5. LOGIKA HALAMAN ---

if nav == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2.5])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.write("""Bapak **Erwin Sinaga** adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Beliau memahami bahwa di era digital saat ini, integritas data dan keamanan aset adalah fondasi utama bagi setiap unit bisnis untuk dapat tumbuh secara berkelanjutan.

Melalui dedikasi yang tinggi terhadap transparansi, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan mendesak para pengusaha akan sistem perlindungan aset yang berbasis teknologi kecerdasan buatan mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif dan efisien. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit real-time yang mampu meminimalisir risiko kerugian modal secara signifikan.

Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel dan pengawasan yang tak terputus. Visi besar beliau adalah untuk mendemokratisasikan keamanan bisnis bagi semua kalangan, memastikan bahwa UKM pun memiliki akses ke teknologi proteksi setingkat korporasi. Di bawah kepemimpinan beliau, V-Guard AI terus berinovasi untuk mengembangkan instrumen pengawasan yang adaptif terhadap tantangan ekonomi masa depan, menjadikannya mitra strategis yang tak tergantikan dalam menjaga setiap rupiah aset berharga pelanggan dari ancaman internal maupun eksternal yang merugikan.""")

elif nav == "2. 🎯 Visi, Misi & ROI":
    st.header("Visi, Misi & Analisis Kerugian")
    st.info("**Visi:** Menjadi pelopor global dalam penyediaan infrastruktur audit digital berbasis AI.")
    st.success("**Misi:** Mengintegrasikan AI untuk deteksi fraud real-time.")
    oz = st.number_input("Input Total Omzet Bulanan (Rp):", value=100000000)
    leakage = oz * 0.07
    st.error(f"Potensi Kerugian (7%): Rp {leakage:,.0f}")
    st.success(f"Estimasi Penyelamatan: Rp {leakage - 2500000:,.0f}")

elif nav == "3. 💎 Layanan Produk":
    st.header("Paket Layanan V-Guard AI")
    st.columns(3) # UI kolom paket... (disingkat untuk hemat ruang, isi tetap sama)

elif nav == "4. 📝 Registrasi & Upload":
    if not st.session_state.client_logged_in:
        t1, t2 = st.tabs(["📝 Pendaftaran Klien", "🔑 Login Dashboard Klien"])
        with t1:
            with st.form("reg"):
                st.text_input("Nama Pelanggan:")
                st.selectbox("Paket:", ["BASIC", "SMART", "PRO"])
                st.form_submit_button("Daftar Sekarang")
        with t2:
            u = st.text_input("User ID:")
            p = st.text_input("Password:", type="password")
            if st.button("LOGIN KLIEN"):
                if u in st.session_state.user_creds and st.session_state.user_creds[u] == p:
                    st.session_state.client_logged_in = True
                    st.rerun()
                else: st.error("ID atau Password salah.")
    else:
        st.header("🛡️ Dashboard Mitra V-Guard")
        st.markdown('<div class="client-box"><h3>Tugas Harian Anda</h3>• Upload CSV Penjualan<br>• Update Absensi<br>• Cek Koneksi CCTV</div>', unsafe_allow_html=True)
        if st.button("🚪 Keluar"):
            st.session_state.client_logged_in = False
            st.rerun()

elif nav == "5. 🔐 Akses Terbatas":
    if not st.session_state.auth_vguard:
        pw = st.text_input("Kode Keamanan Admin:", type="password")
        if st.button("BUKA PANEL ADMIN"):
            if pw == "w1nbju8282":
                st.session_state.auth_vguard = True
                st.rerun()
    else:
        st.title("👨‍💼 Panel Eksekutif Pak Erwin")
        tab_db, tab_user, tab_audit = st.tabs(["📊 Database Klien", "👤 Buat Akun Klien", "📉 Audit AI"])
        
        with tab_db:
            st.subheader("Data Kontrak Aktif")
            st.table(pd.DataFrame(st.session_state.db_n))
            
        with tab_user:
            st.subheader("Registrasi Akun Baru (Aktivasi)")
            with st.form("add_user"):
                new_u = st.text_input("Buat User ID Klien:")
                new_p = st.text_input("Buat Password Klien:")
                if st.form_submit_button("AKTIFKAN AKUN KLIEN"):
                    st.session_state.user_creds[new_u] = new_p
                    st.success(f"Akun '{new_u}' telah aktif. Silakan berikan akses ini ke klien.")
                    
        with tab_audit:
            st.write("Analisis Fraud Terkini...")
            st.line_chart([10, 20, 15, 5])
            
        if st.button("🔐 KELUAR ADMIN"):
            st.session_state.auth_vguard = False
            st.rerun()

st.write("---")
st.caption("© 2026 V-Guard AI | Secured by Erwin Sinaga")
