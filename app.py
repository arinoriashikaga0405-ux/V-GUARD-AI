import streamlit as st
import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime

# --- 1. LOAD CONFIG & SECURITY ---
load_dotenv()
import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. AMBIL PASSWORD DARI SECRETS ---
try:
    ADMIN_PWD = st.secrets["ADMIN_PASSWORD"]
except Exception:
    st.error("⚠️ Password belum diatur di menu Secrets Streamlit Cloud!")
    st.stop()

# --- 2. LOGIKA LOGIN ---
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI SECURE LOGIN")
    st.write("Founder: Erwin Sinaga")
    pwd_input = st.text_input("Masukkan Password Admin:", type="password")
    
    if st.button("Masuk"):
        if pwd_input == ADMIN_PWD:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Password Salah!")
    st.stop()

# --- 3. KONTEN UTAMA (Hanya muncul jika sudah login) ---
st.sidebar.title("V-Guard AI")
st.sidebar.write(f"👤 User: **Erwin Sinaga**")
if st.sidebar.button("Logout"):
    st.session_state.auth = False
    st.rerun()

st.header("Financial Integrity Dashboard")
st.success("Sistem Online & Terproteksi.")

# Visualisasi Plotly yang tadi error, sekarang sudah aktif
df = pd.DataFrame({'Kategori': ['Aman', 'Risiko'], 'Nilai': [92, 8]})
fig = px.bar(df, x='Kategori', y='Nilai', color='Kategori', title="Status Transaksi Real-time")
st.plotly_chart(fig)
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
