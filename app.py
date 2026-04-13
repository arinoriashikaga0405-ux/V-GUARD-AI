"""
🛡️ V-GUARD AI INTELLIGENCE - FULL ENTERPRISE SYSTEM
Optimized for Railway.app | SOP Compliance v3.1
Founder & CEO: Erwin Sinaga
"""

import streamlit as st
import google.generativeai as genai
import pandas as pd
import numpy as np
import os
from datetime import datetime

# ============================================================================
# 1. ENTERPRISE CONFIGURATION (RAILWAY FRIENDLY)
# ============================================================================
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")
WA_TOKEN = os.environ.get("WA_TOKEN") or st.secrets.get("WA_TOKEN")
WA_PHONE_ID = os.environ.get("WA_PHONE_ID") or st.secrets.get("WA_PHONE_ID")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Data Produk Sesuai SOP
PRODUCTS = {
    "V-LITE": {"install": "750.000", "monthly": "350.000", "color": "#10b981"},
    "V-PRO": {"install": "1.500.000", "monthly": "850.000", "color": "#3b82f6"},
    "V-SIGHT": {"install": "7.500.000", "monthly": "3.500.000", "color": "#f59e0b"},
    "V-ENTERPRISE": {"install": "15.000.000", "monthly": "10.000.000", "color": "#8b5cf6"}
}

# ============================================================================
# 2. DATABASE INITIALIZATION
# ============================================================================
if "db_klien" not in st.session_state:
    st.session_state.db_klien = pd.DataFrame(columns=[
        "Nama", "Usaha", "Paket", "Username", "Password", "Status", "Tgl_Daftar"
    ])

# ============================================================================
# 3. SIDEBAR NAVIGATION
# ============================================================================
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center;'><p style='color:#00d4aa; font-weight:bold;'>Erwin Sinaga</p><p style='color:gray;'>Founder & CEO</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Logic Navigasi
    if "admin_logged_in" not in st.session_state: st.session_state.admin_logged_in = False
    if "klien_auth" not in st.session_state: st.session_state.klien_auth = False

    if st.session_state.admin_logged_in:
        menu = st.radio("EXECUTIVE MENU", ["Admin Control Center"])
    elif st.session_state.klien_auth:
        menu = st.radio("CLIENT MENU", ["Dashboard Klien"])
    else:
        menu = st.radio("NAVIGASI", [
            "🏢 Visi & Misi", 
            "📦 Produk & Layanan", 
            "📊 ROI Kerugian Klien", 
            "🔐 Portal Klien",
            "🔒 Admin Control Center"
        ])

    st.markdown("---")
    if st.session_state.admin_logged_in or st.session_state.klien_auth:
        if st.button("🚪 Log Out"):
            st.session_state.admin_logged_in = False
            st.session_state.klien_auth = False
            st.rerun()

# ============================================================================
# 4. HALAMAN: ROI KERUGIAN KLIEN
# ============================================================================
if menu == "📊 ROI Kerugian Klien":
    st.header("📊 Analisis Potensi Kerugian vs ROI")
    with st.container(border=True):
        col_a, col_b = st.columns(2)
        with col_a:
            st.subheader("💰 Kalkulator Kerugian")
            omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000, step=1000000)
            leak = st.slider("Estimasi Kebocoran (%)", 1, 20, 5)
            loss = omzet * (leak / 100)
            st.error(f"**Potensi Kerugian: Rp {loss:,.0f} / bulan**")
        with col_b:
            st.subheader("🛡️ Proteksi V-Guard AI")
            saved_min = loss * 0.25
            saved_max = loss * 0.40
            st.success(f"**Estimasi Penghematan: Rp {saved_min:,.0f} - Rp {saved_max:,.0f}**")

# ============================================================================
# 5. HALAMAN: ADMIN CONTROL CENTER (PASSED 20%)
# ============================================================================
elif menu == "🔒 Admin Control Center":
    if not st.session_state.admin_logged_in:
        st.subheader("Akses Administrator")
        pwd = st.text_input("Masukkan Password Eksklusif", type="password")
        if pwd == "w1nbju8282":
            st.session_state.admin_logged_in = True
            st.rerun()
    else:
        st.success("✅ Akses Eksekutif Aktif")
        st.markdown("### 📊 Ringkasan Eksekutif & AI Squad")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Anggaran API Bulanan", "Rp 10.000.000")
        c2.metric("Biaya API Terpakai", "Rp 2.000.000", delta="20%", delta_color="inverse")
        c3.metric("Efisiensi Sistem", "88%", delta="SOP Compliance")
        
        st.progress(0.20, text="Penggunaan Kuota API Cloud: 20%") # Update ke 20%
        
        st.divider()
        # Tab Menu Admin (Aktivasi Klien, dll)
        t1, t2 = st.tabs(["👤 Aktivasi Klien", "🖥️ Ekosistem AI"])
        with t1:
            st.subheader("Aktivasi Akun Paid")
            st.info("Gunakan menu ini untuk memverifikasi pembayaran klien.")

# ============================================================================
# 6. HALAMAN: PORTAL KLIEN (DAFTAR & LOGIN)
# ============================================================================
elif menu == "🔐 Portal Klien":
    tab1, tab2 = st.tabs(["📝 Daftar Klien Baru", "🔑 Login Klien"])
    with tab1:
        with st.form("pendaftaran"):
            st.subheader("Form Registrasi Klien Baru")
            n_pel = st.text_input("Nama Lengkap (KTP)")
            n_usa = st.text_input("Nama Usaha")
            ktp = st.file_uploader("Upload KTP")
            pkt = st.selectbox("Pilih Paket", list(PRODUCTS.keys()))
            u_reg = st.text_input("Buat Username")
            p_reg = st.text_input("Buat Password", type="password")
            if st.form_submit_button("Daftar Sekarang"):
                st.success("✅ Pendaftaran Terkirim. Menunggu Aktivasi Admin.")

# ============================================================================
# 7. DASHBOARD KLIEN (88% EFFICIENCY)
# ============================================================================
elif menu == "Dashboard Klien":
    st.header(f"🛡️ V-Guard Dashboard")
    st.metric("Efisiensi AI", "88%", delta="SOP Protected")

st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | CEO Erwin Sinaga | ©2026</small></center>", unsafe_allow_html=True)
