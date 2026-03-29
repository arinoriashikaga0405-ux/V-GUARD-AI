import streamlit as st
import pandas as pd
import numpy as np

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# PERBAIKAN: Menggunakan unsafe_allow_html agar tidak error
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR NAVIGASI ---
st.sidebar.title("VGUARD AI")
menu = st.sidebar.radio("Navigasi Sistem", ["Dashboard Performa", "AI Scanner Audit", "Paket Layanan", "Kontak Admin"])

# --- 3. LOGIKA MENU (CONTOH) ---
if menu == "Dashboard Performa":
    st.title("🛡️ VGUARD AI Systems")
    st.subheader("Intelligence for Your Business Security")
    st.metric("Efisiensi Sistem", "98.2%", "+2.1%")
    st.line_chart(pd.DataFrame(np.random.randn(20, 2), columns=['Retail', 'Gudang']))

elif menu == "AI Scanner Audit":
    st.title("🔍 AI Scanner Audit")
    input_data = st.text_area("Masukkan Data untuk Diaudit:")
    if st.button("Jalankan Analisis"):
        st.info("Sedang menganalisis data melalui VGUARD Engine...")

elif menu == "Paket Layanan":
    st.title("📦 Paket VGUARD AI Systems")
    col1, col2 = st.columns(2)
    col1.info("### V-START\n**Rp 2,5 Juta**")
    col2.warning("### V-GROW\n**Rp 5 Juta**")

elif menu == "Kontak Admin":
    st.title("📞 Kontak CEO")
    st.write("Founder: Pak Erwin - Tangerang")
