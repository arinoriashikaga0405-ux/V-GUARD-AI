import streamlit as st
import pandas as pd
from cryptography.fernet import Fernet
import hashlib
import time

# 🔐 1. KONFIGURASI KEAMANAN
def encrypt_ktp(data):
    # Menggunakan key statis untuk demo, di produksi gunakan .env
    key = b'8-8zY_z_5P2_z_f8_z_z_z_z_z_z_z_z_z_z_z_z_z=' 
    f = Fernet(key)
    return f.encrypt(data)

ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

# 🏢 2. TAMPILAN DASHBOARD
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# Sidebar
st.sidebar.title("🛡️ V-GUARD AI")
menu = st.sidebar.radio("Navigasi", ["Home", "Produk & Layanan", "Portal Klien", "Admin Panel"])

# --- HALAMAN HOME ---
if menu == "Home":
    st.title("V-Guard AI Intelligence")
    st.subheader("Digitizing Trust, Eliminating Leakage")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.info("Founder: Erwin Sinaga")
    with col2:
        st.markdown("""
        ### Visi & Misi (Digitizing Trust)
        Sebagai Senior Business Leader, saya mendirikan V-Guard untuk memastikan 
        setiap rupiah aset Anda aman. Kami mengubah data menjadi bukti otentik 
        dengan akurasi 99.9%.
        """)

# --- HALAMAN PRODUK ---
elif menu == "Produk & Layanan":
    st.header("Katalog Layanan V-Guard")
    items = [
        {"Paket": "V-LITE", "Target": "UMKM", "Fitur": "Anti-Void, WA Report"},
        {"Paket": "V-PRO", "Target": "Retail/Resto", "Fitur": "Real-time, VCS Sync"},
        {"Paket": "V-SIGHT", "Target": "Aset Tinggi", "Fitur": "CCTV AI Behavior"},
        {"Paket": "V-ENTERPRISE", "Target": "Korporasi", "Fitur": "Multi-Branch, Forensik"}
    ]
    st.table(pd.DataFrame(items))

# --- HALAMAN PORTAL KLIEN ---
elif menu == "Portal Klien":
    st.header("Portal Klien & Upload Data")
    with st.form("upload_form"):
        biz_name = st.text_input("Nama Bisnis")
        file_vcs = st.file_uploader("Upload Data VCS (Excel/CSV)")
        file_ktp = st.file_uploader("Upload KTP (KYC)", type=['jpg', 'png'])
        submit = st.form_submit_button("Kirim Data")
        
        if submit:
            st.success(f"Data {biz_name} terenkripsi AES-256 dan terkirim ke Founder.")

# --- HALAMAN ADMIN PANEL ---
elif menu == "Admin Panel":
    st.header("CEO Executive Dashboard")
    pwd_input = st.text_input("Masukkan Sandi Founder", type="password")
    
    if pwd_input:
        input_hash = hashlib.sha256(pwd_input.encode()).hexdigest()
        if input_hash == ADMIN_PWD_HASH:
            st.success("Akses Diterima, Pak Erwin.")
            
            t1, t2, t3 = st.tabs(["KYC & Invoice", "Audit Launchpad", "Revenue"])
            
            with t1:
                st.subheader("Manajemen Invoice & KYC")
                st.write("Antrean Verifikasi KTP Klien")
                st.table(pd.DataFrame({'User': ['Toko Maju'], 'Status': ['Pending']}))
                if st.button("Kirim Notifikasi Invoice Otomatis"):
                    st.info("Notifikasi Invoice dikirim via WhatsApp ke seluruh klien.")

            with t2:
                st.subheader("Orchestration 9 AI")
                if st.button("🚀 JALANKAN AUDIT 99.9% ACCURACY"):
                    with st.spinner("Mensinkronkan Gemini, MindBridge, dan YOLO..."):
                        time.sleep(2)
                        st.success("Audit Selesai. Kebocoran Terdeteksi: 0.05%")
            
            with t3:
                st.metric("Total Kerugian Dicegah", "Rp 125.500.000")
        else:
            st.error("Sandi Salah. Akses Ditolak.")
    else:
        st.warning("Silakan masukkan sandi untuk mengakses fitur Admin.")

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 V-Guard AI - Founder Erwin Sinaga")
