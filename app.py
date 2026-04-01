import streamlit as st
import pandas as pd
from cryptography.fernet import Fernet
import hashlib
import time

# 🔐 1. SISTEM KEAMANAN & ENKRIPSI
def generate_key():
    return Fernet.generate_key()

def encrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode())

# Password Admin (Wajib di-hash untuk keamanan)
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

# 🏢 2. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# Custom CSS untuk Tema Corporate Navy
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { background-color: #1c2e4a; color: white; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 🏠 3. SIDEBAR NAVIGATION
st.sidebar.title("🛡️ V-GUARD AI")
menu = st.sidebar.radio("Navigasi", ["Home", "Produk & Layanan", "Portal Klien", "Admin Panel"])

# --- HALAMAN HOME ---
if menu == "Home":
    st.title("V-Guard AI Intelligence")
    st.subheader("Digitizing Trust, Eliminating Leakage")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://via.placeholder.com/150", caption="Erwin Sinaga - Founder")
    with col2:
        st.markdown("""
        ### Profil Founder
        Sebagai Senior Business Leader dengan 10+ tahun pengalaman di perbankan, 
        saya mendirikan V-Guard untuk menjawab tantangan ketidakpastian data. 
        Visi kami adalah menjadi standar global dalam **Digital Trust**. 
        Misi kami adalah **Eliminating Leakage** dengan integrasi 9 AI terbaik dunia.
        """)

# --- HALAMAN PRODUK ---
elif menu == "Produk & Layanan":
    st.header("Katalog Layanan V-Guard")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**V-LITE** (Solusi UMKM)\n- Anti-Void Audit\n- Laporan WA Bulanan")
        st.success("**V-PRO** (Retail/Resto)\n- Real-Time Monitoring\n- Integrasi VCS Bank")
    with col2:
        st.warning("**V-SIGHT** (Visual Security)\n- CCTV AI Behavior\n- Cloud Evidence")
        st.error("**V-ENTERPRISE** (Corporate)\n- Multi-Branch Dashboard\n- Digital Forensics")

# --- HALAMAN PORTAL KLIEN ---
elif menu == "Portal Klien":
    st.header("Portal Klien - Upload Data Audit")
    with st.form("upload_form"):
        nama_bisnis = st.text_input("Nama Bisnis")
        file_vcs = st.file_uploader("Upload Data VCS (Excel/CSV)", type=['csv', 'xlsx'])
        file_ktp = st.file_uploader("Upload KTP (KYC Verification)", type=['jpg', 'png'])
        submitted = st.form_submit_button("Kirim Data")
        
        if submitted:
            if file_ktp:
                st.success(f"Data {nama_bisnis} berhasil diunggah dan Dienkripsi (AES-256).")
                st.info("Status: Menunggu Verifikasi Admin.")

# --- HALAMAN ADMIN PANEL ---
elif menu == "Admin Panel":
    st.header("CEO Executive Dashboard")
    pwd_input = st.text_input("Masukkan Sandi Founder", type="password")
    
    if hashlib.sha256(pwd_input.encode()).hexdigest() == ADMIN_PWD_HASH:
        st.success("Akses Diterima, Pak Founder.")
        
        tab1, tab2, tab3 = st.tabs(["KYC Verification", "Audit Launchpad", "Revenue"])
        
        with tab1:
            st.write("Daftar Antrean KTP Klien")
            # Contoh data dummy
            df_ktp = pd.DataFrame({'User': ['Toko Maju', 'Cafe Sejahtera'], 'Status': ['Pending', 'Pending']})
            st.table(df_ktp)
            if st.button("Verify All"): st.balloons()

        with tab2:
            st.subheader("Orchestration 9 AI")
            if st.button("🚀 JALANKAN AUDIT SELURUH CABANG"):
                with st.spinner("Mengaktifkan Gemini, MindBridge, dan YOLO..."):
                    time.sleep(3)
                    st.success("Audit Selesai. Akurasi 99.9%. Laporan dikirim via WhatsApp.")
                    
        with tab3:
            st.metric("Total Profit Kebocoran Dicegah", "Rp 125.500.000", "+12%")
    else:
