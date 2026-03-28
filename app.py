import streamlit as st

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. STYLE KONTRAS MAKSIMAL & INVOICE MINIMALIS (CSS) ---
st.markdown("""
<style>
    /* Latar Belakang & Sidebar */
    .stApp { background-color: #001529 !important; }
    [data-testid="stSidebar"] { background-color: #000c17 !important; border-right: 1px solid #002140; }

    /* Memastikan Semua Teks Sidebar Putih */
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] h3 {
        color: #ffffff !important; font-weight: bold !important;
    }

    /* Judul Header Cyan Menyala */
    .cyan-header {
        color: #00f2ff !important; font-size: 1.6rem !important; font-weight: bold !important;
        margin-top: 25px !important; border-bottom: 2px solid #00f2ff; padding-bottom: 5px;
    }

    /* Kartu Metrik */
    [data-testid="stMetric"] { background-color: #002140 !important; border: 2px solid #004a99 !important; border-radius: 12px !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; font-weight: bold !important; }
    [data-testid="stMetricLabel"] > div { color: #f0c04a !important; font-weight: bold !important; }

    /* --- GAYA MINIMALIS INVOICE (SESUAI KEINGINAN BAPAK) --- */
    .minimalis-invoice {
        background-color: transparent !important;
        padding: 8px 0 !important;
        border-bottom: 1px solid #004a99 !important; /* Garis tipis pemisah */
        margin-bottom: 5px !important;
    }
    .minimalis-invoice-text {
        color: #e0e0e0 !important;
        font-size: 1.1rem !important;
    }

    /* Tombol Logout & Kirim Laporan Merah */
    .stButton>button[kind="secondary"] { background-color: #ff4b4b !important; color: white !important; border: none !important; width: 100% !important; }
    .stButton>button[kind="primary"] { background-color: #ff4b4b !important; color: white !important; font-weight: bold !important; }
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
        st.markdown("### Menu Navigasi")
        menu = st.radio("Nav", [
            "🔴 Executive Dashboard", 
            "📊 Laporan Mingguan"
        ], label_visibility="collapsed")
        st.divider()
        st.markdown(f"<p style='color: white;'>Sesi: {st.session_state['role'].upper()}</p>", unsafe_allow_html=True)
        if st.button("Logout", key="out", type="secondary"):
            st.session_state['logged_in'] = False
            st.rerun()

    # --- LOGIKA TAMPILAN HALAMAN ---
    
    if menu == "🔴 Executive Dashboard":
        st.markdown("<h1 style='color: white;'>🔴 Executive Dashboard</h1>", unsafe_allow_html=True)
        m1, m2, m3 = st.columns(3)
        with m1: st.metric("Audit Bulan Ini", "1,284", "12%")
        with m2: st.metric("Anomali Terdeteksi", "42", "-5%", delta_color="inverse")
        with m3: st.metric("Revenue Terproteksi", "IDR 8.2B", "8%")

        # --- JUDUL JUDUL (CYAN & MENYALA) ---
        st.markdown("<div class='cyan-header'>🔔 Monitor Invoice & Tagihan</div>", unsafe_allow_html=True)
        
        # --- PERBAIKAN: INVOICE MINIMALIS (SESUAI image_10.png) ---
        def minimalis_row(nama, uang, tempo, key):
            c1, c2 = st.columns([4, 1])
            with c1:
                # Menggunakan teks baris tunggal dengan garis bawah tipis
                st.markdown(f"<div class='minimalis-invoice'><span class='minimalis-invoice-text'>👤 {nama} | 💰 {uang} | 📅 {tempo}</span></div>", unsafe_allow_html=True)
            with c2:
                # Tombol merah di sebelahnya
                st.button("📩 Kirim WA", key=key, type="primary")

        minimalis_row("Ko Shandy Vertigo", "Rp 5.000.000", "30 Mar 2026", "wa1")
        minimalis_row("Client SME B", "Rp 1.250.000", "02 Apr 2026", "wa2")

        st.divider()
        st.markdown("<div class='cyan-header'>📽️ Live CCTV Audit</div>", unsafe_allow_html=True)
        st.image("https://via.placeholder.com/1000x400.png?text=Live+Audit+Active+Stream", use_column_width=True)

    elif menu == "📊 Laporan Mingguan":
        st.markdown("<h1 style='color: white;'>📊 Laporan Mingguan Klien</h1>", unsafe_allow_html=True)
        st.info("Halaman simulasi pengiriman laporan mingguan.")
        st.bar_chart({"Kebocoran Dana": [10, 15], "Audit Sukses": [100, 120]})
