import streamlit as st
import pandas as pd

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. CSS FIX: KONTRAST TINGGI (MEMPERJELAS TEKS) ---
st.markdown("""
<style>
    .stApp { background-color: #001529 !important; }
    [data-testid="stSidebar"] { background-color: #000c17 !important; border-right: 1px solid #002140; }

    /* MEMAKSA TEKS SIDEBAR PUTIH TERANG & TEBAL */
    [data-testid="stSidebar"] * { color: #ffffff !important; }
    [data-testid="stSidebar"] label { font-weight: bold !important; padding-bottom: 15px !important; }
    
    /* Perbaikan Menu Navigasi agar Tidak Berantakan */
    div.row-widget.stRadio > div { background: rgba(255, 255, 255, 0.05); padding: 15px; border-radius: 10px; }
    div[data-testid="stMarkdownContainer"] p { font-size: 1.1rem !important; font-weight: bold !important; }

    /* Header Cyan Menyala */
    .cyan-header {
        color: #00f2ff !important; font-size: 1.6rem !important; font-weight: bold !important;
        margin-top: 25px !important; border-bottom: 2px solid #00f2ff; padding-bottom: 5px;
    }

    /* KOTAK METRIK DENGAN LABEL DIPERJELAS (FINAL FIX) */
    [data-testid="stMetric"] { background-color: #002140 !important; border: 2px solid #004a99 !important; border-radius: 12px !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; font-weight: bold !important; }
    
    /* INI ADALAH PERBAIKAN UNTUK MEMPERJELAS TEKS LABEL (Audit Bulan Ini, dst) */
    [data-testid="stMetricLabel"] > div {
        color: #ffffff !important; /* Diubah menjadi Putih Terang */
        font-weight: bold !important; /* Dibuat Tebal */
        font-size: 1.1rem !important; /* Ukuran diperbesar sedikit */
        opacity: 1 !important; /* Kontras maksimal */
    }

    /* Baris Invoice Minimalis */
    .minimalis-invoice { border-bottom: 1px solid #004a99; padding: 12px 0; }
    .minimalis-invoice-text { color: white !important; font-size: 1rem; font-weight: bold !important;}

    /* Tombol Logout Merah Standar */
    .stButton>button[kind="secondary"] { 
        background-color: #ff4b4b !important; 
        color: white !important; 
        border: none !important; 
        width: 100% !important;
        font-weight: bold !important;
    }
    
    /* Tombol WA Merah */
    .stButton>button[kind="primary"] { background-color: #ff4b4b !important; color: white !important; font-weight: bold !important; }

    /* Perbaikan Input Text CCTV */
    .stTextInput>div>div>input { background-color: #002140 !important; color: white !important; border: 1px solid #00f2ff !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA LOGIN ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align: center; color: white;'>🛡️ V-GUARD AI LOGIN</h1>", unsafe_allow_html=True)
    with st.container():
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("Masuk Ke Dashboard"):
            if u == "admin" and p == "vguard2026":
                st.session_state.update({'logged_in': True, 'role': 'admin'})
                st.rerun()
    st.stop()

# --- 4. DASHBOARD UTAMA (SEMUA FITUR DIKUNCI & DIPERTAHANKAN) ---
if st.session_state['logged_in']:
    
    with st.sidebar:
        # LOGO & IDENTITAS
        st.markdown("<div style='text-align: center;'><img src='https://cdn-icons-png.flaticon.com/512/1055/1055644.png' width='80'><h2 style='color: white;'>V-GUARD AI</h2></div>", unsafe_allow_html=True)
        st.divider()
        
        # PENGATURAN AI (JAM OPERASIONAL)
        st.markdown("### ⚙️ Pengaturan AI")
        st.selectbox("Mulai Operasional", ["08:00", "09:00", "10:00"], index=2, key="start_time")
        st.selectbox("Selesai Operasional", ["20:00", "21:00", "22:00"], index=2, key="end_time")
        st.success("🟢 Monitoring Aktif")
        
        st.divider()
        
        # MENU NAVIGASI (LENGKAP & PUTIH TERANG)
        st.markdown("### Menu Navigasi")
        menu = st.radio("Pilih Halaman:", [
            "🔴 Executive Dashboard", 
            "📊 Laporan Mingguan",
            "⚫ Audit Engine", 
            "⚫ Finance & Payment",
            "⚫ HR & Payroll Monitoring"
        ], key="main_nav")
        
        st.divider()
        
        # INFO SESI & LOGOUT
        st.write(f"Sesi: **{st.session_state['role'].upper()}**")
        if st.button("Logout", type="secondary", key="logout_btn"):
            st.session_state['logged_in'] = False
            st.rerun()

    # --- KONTEN HALAMAN ---
    if menu == "🔴 Executive Dashboard":
        st.markdown("<h1 style='color: white;'>🔴 Executive Dashboard</h1>", unsafe_allow_html=True)
        
        # Kolom Metrik dengan Label yang Diperjelas oleh CSS
        col1, col2, col3 = st.columns(3)
        col1.metric("Audit Bulan Ini", "1,284", "12%")
        col2.metric("Anomali Terdeteksi", "42", "-5%", delta_color="inverse")
        col3.metric("Revenue Terproteksi", "IDR 8.2B", "8%")

        # MONITOR INVOICE
