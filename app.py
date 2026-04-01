import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE USER & PENDAFTARAN ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "Eksekutif", "Paket": "MASTER"},
        {"User ID": "siska", "Password": "p", "Level": "Klien", "Paket": "SMART"},
        {"User ID": "jaya", "Password": "p", "Level": "Klien", "Paket": "BASIC"}
    ]

if 'client_logged_in' not in st.session_state: st.session_state.client_logged_in = False
if 'current_user' not in st.session_state: st.session_state.current_user = None
if 'auth_admin' not in st.session_state: st.session_state.auth_admin = False

# --- 3. CSS TAMPILAN ---
st.markdown("""
<style>
    .status-box { background-color: #e3f2fd; padding: 15px; border-radius: 8px; color: #1e3a8a; font-weight: bold; margin-bottom: 5px; }
    .package-box { background-color: #fff3e0; padding: 8px 15px; border-radius: 8px; color: #e65100; font-weight: bold; display: inline-block; margin-bottom: 20px; border: 1px solid #ffe0b2; }
    .fraud-header { background-color: #ff7675; color: white; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR NAVIGASI (1-5 TETAP) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    st.markdown("**Erwin Sinaga - Senior Business Leader**")
    st.write("---")
    nav = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 💎 Layanan Produk", 
        "4. 📝 Registrasi & Dashboard", 
        "5. 🔐 Akses Terbatas"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI Intelligence")

# --- 5. LOGIKA MENU ---

if nav == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    st.write("""Bapak **Erwin Sinaga** adalah seorang Senior Business Leader yang memimpin transformasi operasional dengan keahlian analitis tajam dalam mengidentifikasi celah kebocoran finansial.""")

elif nav == "2. 🎯 Visi, Misi & ROI":
    st.header("Visi, Misi & Analisis Kerugian")
    oz = st.number_input("Input Omzet Bulanan (Rp):", value=100000000)
    leakage = oz * 0.07
    st.error(f"Potensi Kerugian (7%): Rp {leakage:,.0f}")

elif nav == "3. 💎 Layanan Produk":
    st.header("Paket Layanan V-Guard AI")
    st.write("Silakan pilih paket sesuai kebutuhan bisnis Anda.")

elif nav == "4. 📝 Registrasi & Dashboard":
    t1, t2 = st.tabs(["📝 Form Pendaftaran Baru", "🔑 Dashboard Akun Klien"])
    
    with t1:
        st.subheader("Form Pendaftaran Pelanggan")
        with st.form("pendaftaran_baru"):
            c1, c2 = st.columns(2)
            with c1:
                nama = st.text_input("Nama Pelanggan:")
                usaha = st.text_input("Jenis Usaha (e.g. Cafe, Retail):")
            with c2:
                paket_pilih = st.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO"])
                harga_paket = st.text_input("Harga Kesepakatan (Rp):", value="1,500,000")
            
            uploaded_ktp = st.file_uploader("Upload Foto KTP (JPG/PNG):", type=["jpg", "png", "jpeg"])
            
            if st.form_submit_button("KIRIM PEN
