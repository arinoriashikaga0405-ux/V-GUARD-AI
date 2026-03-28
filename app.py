import streamlit as st
import pandas as pd

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. STYLE PERBAIKAN TATA LETAK (CSS) ---
st.markdown("""
<style>
    .stApp { background-color: #001529 !important; }
    [data-testid="stSidebar"] { background-color: #000c17 !important; border-right: 1px solid #002140; }

    /* MEMBERI JARAK AGAR TIDAK MENINDIH DI SIDEBAR */
    .stSelectbox { margin-bottom: 20px !important; }
    [data-testid="stSidebar"] label { 
        color: #ffffff !important; 
        font-weight: bold !important; 
        padding-bottom: 10px !important; 
        display: block !important;
    }

    /* Header Cyan Menyala */
    .cyan-header {
        color: #00f2ff !important; font-size: 1.6rem !important; font-weight: bold !important;
        margin-top: 25px !important; border-bottom: 2px solid #00f2ff; padding-bottom: 5px;
    }

    /* Baris Invoice Minimalis */
    .minimalis-invoice { border-bottom: 1px solid #004a99; padding: 12px 0; }
    .minimalis-invoice-text { color: white !important; font-size: 1rem; }

    /* Perbaikan Input Text agar Terlihat di Tema Gelap */
    .stTextInput>div>div>input {
        background-color: #002140 !important;
        color: white !important;
        border: 1px solid #00f2ff !important;
    }
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

# --- 4. DASHBOARD UTAMA ---
if st.session_state['logged_in']:
    
    with st.sidebar:
        st.markdown("<div style='text-align: center;'><img src='https://cdn-icons-png.flaticon.com/512/1055/1055644.png' width='80'><h2 style='color: white;'>V-GUARD AI</h2></div>", unsafe_allow_html=True)
        st.divider()
        
        # PENGATURAN AI DENGAN JARAK AMAN
        st.markdown("### ⚙️ Pengaturan AI")
        st.selectbox("Jam Mulai Operasional", ["08:00", "09:00", "10:00"], index=2, key="start_time")
        st.selectbox("Jam Selesai Operasional", ["20:00", "21:00", "22:00"], index=2, key="end_time")
        st.success("🟢 Monitoring Aktif")
        
        st.divider()
        st.markdown("### Menu Navigasi")
        menu = st.radio("Nav", ["🔴 Executive Dashboard", "📊 Laporan Mingguan", "⚫ Audit Engine", "⚫ Finance", "⚫ HR Monitoring"], label_visibility="collapsed")
        
        st.divider()
        if st.button("Logout", type="secondary", use_container_width=True):
            st.session_state['logged_in'] = False
            st.rerun()

    # --- ISI KONTEN ---
    if menu == "🔴 Executive Dashboard":
        st.markdown("<h1 style='color: white;'>🔴 Executive Dashboard</h1>", unsafe_allow_html=True)
        
        # Kolom Metrik
        col1, col2, col3 = st.columns(3)
        col1.metric("Audit Bulan Ini", "1,284", "12%")
        col2.metric("Anomali Terdeteksi", "42", "-5%", delta_color="inverse")
        col3.metric("Revenue Terproteksi", "IDR 8.2B", "8%")

        # MONITOR INVOICE
        st.markdown("<div class='cyan-header'>🔔 Monitor Invoice & Tagihan</div>", unsafe_allow_html=True)
        
        def row_inv(nama, uang, tgl, k):
            c1, c2 = st.columns([4, 1])
            with c1: st.markdown(f"<div class='minimalis-invoice'><span class='minimalis-invoice-text'>👤 {nama} | 💰 {uang} | 📅 {tgl}</span></div>", unsafe_allow_html=True)
            with c2: st.button("🚀 Kirim WA", key=k, type="primary", use_container_width=True)

        row_inv("Ko Shandy Vertigo", "Rp 5.000.000", "30 Mar 2026", "wa1")
        row_inv("Client SME B", "Rp 1.250.000", "02 Apr 2026", "wa2")

        # LIVE CCTV (KOLOM INPUT DIKEMBALIKAN)
        st.markdown("<div class='cyan-header'>📽️ Live CCTV Audit</div>", unsafe_allow_html=True)
        url_cctv = st.text_input("Masukkan URL CCTV (RTSP/IP Cam):", "rtsp://admin:password@192.168.1.100:554/live")
        st.image("https://via.placeholder.com/1000x400.png?text=V-Guard+Live+Stream+Active", use_column_width=True)

    elif menu == "📊 Laporan Mingguan":
        st.markdown("<h1 style='color: white;'>📊 Laporan Mingguan</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color: white;'>Grafik pencegahan kebocoran dana (dalam jutaan Rupiah):</p>", unsafe_allow_html=True)
        
        chart_data = pd.DataFrame({
            "Hari": ["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"],
            "Kebocoran Dicegah": [12, 18, 5, 8, 4, 22, 15]
        })
        # Menggunakan warna cyan agar menyala di background gelap
        st.bar_chart(chart_data.set_index("Hari"), color="#00f2ff")
