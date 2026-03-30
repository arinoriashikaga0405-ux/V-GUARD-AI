import streamlit as st
import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime

# --- 1. LOAD CONFIG & SECURITY ---
load_dotenv()
ADMIN_PWD = os.getenv("ADMIN_PASSWORD")

st.set_page_config(page_title="V-Guard AI | Secure", layout="wide")

# Inisialisasi Session State
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- 2. LOGIKA LOGIN (SECURITY GUARD) ---
if not st.session_state.auth:
    st.markdown("<div style='text-align:center; padding-top:100px;'>", unsafe_allow_html=True)
    st.title("🛡️ V-GUARD AI SECURE LOGIN")
    pwd_input = st.text_input("Masukkan Password Admin:", type="password")
    
    if st.button("Masuk"):
        if pwd_input == ADMIN_PWD:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Password Salah. Akses Ditolak.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop() # Berhenti di sini jika belum login

# --- 3. KONTEN UTAMA (HANYA JIKA SUDAH LOGIN) ---
try:
    st.sidebar.title("V-Guard AI")
    st.sidebar.write(f"👤 User: **Erwin Sinaga**")
    
    if st.sidebar.button("🔓 Logout"):
        st.session_state.auth = False
        st.rerun()

    st.success("Selamat Datang di Command Center, Pak Erwin Sinaga.")
    
    # Area Simulasi Dashboard
    st.header("Financial Integrity Monitoring")
    data = pd.DataFrame({
        'Status': ['Safe', 'Flagged', 'Critical'],
        'Jumlah': [85, 12, 3]
    })
    st.bar_chart(data.set_index('Status'))

except Exception as e:
    # Baris 94+: Indentasi harus menjorok ke dalam (4 spasi)
    st.error(f"⚠️ Terjadi gangguan pada sistem: {str(e)}")
    st.write("Silakan cek koneksi database atau variabel di file .env Anda.")

# --- 4. FOOTER ---
st.write("---")
st.caption("© 2026 V-Guard AI Systems | Secured Environment")
