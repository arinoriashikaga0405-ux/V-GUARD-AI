import streamlit as st

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. STYLE KONTRAS MAKSIMAL & MINIMALIS (CSS) ---
st.markdown("""
<style>
    .stApp { background-color: #001529 !important; }
    [data-testid="stSidebar"] { background-color: #000c17 !important; border-right: 1px solid #002140; }

    /* Memaksa Teks Sidebar Putih Terang */
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] h3 {
        color: #ffffff !important; font-weight: bold !important;
    }

    /* Header Cyan Menyala */
    .cyan-header {
        color: #00f2ff !important; font-size: 1.6rem !important; font-weight: bold !important;
        margin-top: 25px !important; border-bottom: 2px solid #00f2ff; padding-bottom: 5px;
    }

    /* Kotak Metrik */
    [data-testid="stMetric"] { background-color: #002140 !important; border: 2px solid #004a99 !important; border-radius: 12px !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; font-weight: bold !important; }
    [data-testid="stMetricLabel"] > div { color: #f0c04a !important; font-weight: bold !important; }

    /* Style Baris Invoice Minimalis */
    .minimalis-invoice {
        background-color: transparent !important;
        padding: 10px 0 !important;
        border-bottom: 1px solid #004a99 !important;
    }
    .minimalis-invoice-text { color: #ffffff !important; font-size: 1.05rem !important; }

    /* Tombol Logout & Kirim WA Merah */
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

# --- 4. DASHBOARD UTAMA (SEMUA FITUR KEMBALI) ---
if st.session_state['logged_in']:
    
    with st.sidebar:
        # LOGO & NAMA
        st.markdown("<div style='text-align: center;'><img src='https://cdn-icons-png.flaticon.com/512/1055/1055644.png' width='80'><h2 style='color: white;'>V-GUARD AI</h2></div>", unsafe_allow_html=True)
        st.divider()
        
        # FITUR YANG TADI HILANG: PENGATURAN AI
        st.markdown("### ⚙️ Pengaturan AI")
        st.selectbox("Mulai Operasional", ["08:00", "09:00", "10:00"], index=2)
        st.selectbox("Selesai Operasional", ["20:00", "21:00", "22:00"], index=2)
        st.success("🟢 Monitoring Aktif")
        
        st.divider()
        
        # FITUR YANG TADI HILANG: NAVIGASI LENGKAP
        st.markdown("### Menu Navigasi")
        menu = st.radio("Nav", [
            "🔴 Executive Dashboard", 
            "📊 Laporan Mingguan",
            "⚫ Audit Engine", 
            "⚫ Finance & Payment",
            "⚫ HR & Payroll Monitoring"
        ], label_visibility="collapsed")
        
        st.divider()
        
        # INFO SESI & LOGOUT
        st.markdown(f"<p style='color: white;'>Sesi: {st.session_state['role'].upper()}</p>", unsafe_allow_html=True)
        if st.button("Logout", key="out", type="secondary"):
            st.session_state['logged_in'] = False
            st.rerun()

    # --- LOGIKA ISI HALAMAN ---
    
    if menu == "🔴 Executive Dashboard":
        st.markdown("<h1 style='color: white;'>🔴 Executive Dashboard</h1>", unsafe_allow_html=True)
        m1, m2, m3 = st.columns(3)
        with m1: st.metric("Audit Bulan Ini", "1,284", "12%")
        with m2: st.metric("Anomali Terdeteksi", "42", "-5%", delta_color="inverse")
        with m3: st.metric("Revenue Terproteksi", "IDR 8.2B", "8%")

        # MONITOR INVOICE (KEMBALI KE MINIMALIS)
        st.markdown("<div class='cyan-header'>🔔 Monitor Invoice & Tagihan</div>", unsafe_allow_html=True)
        
        def minimalis_row(nama, uang, tempo, key):
            c1, c2 = st.columns([4, 1])
            with c1:
                st.markdown(f"<div class='minimalis-invoice'><span class='minimalis-invoice-text'>👤 {nama} | 💰 {uang} | 📅 {tempo}</span></div>", unsafe_allow_html=True)
            with c2:
                st.button("📩 Kirim WA", key=key, type="primary", use_container_width=True)

        minimalis_row("Ko Shandy Vertigo", "Rp 5.000.000", "30 Mar 2026", "wa1")
        minimalis_row("Client SME B", "Rp 1.250.000", "02 Apr 2026", "wa2")

        st.divider()
        
        # LIVE CCTV
        st.markdown("<div class='cyan-header'>📽️ Live CCTV Audit</div>", unsafe_allow_html=True)
        st.text_input("Link RTSP:", "rtsp://admin:password@192.168.1.100:554/live")
        st.image("https://via.placeholder.com/1000x400.png?text=Live+Audit+Active+Stream", use_column_width=True)

    elif menu == "📊 Laporan Mingguan":
        st.markdown("<h1 style='color: white;'>📊 Laporan Mingguan</h1>", unsafe_allow_html=True)
        st.info("Fitur simulasi pengiriman laporan mingguan ke klien.")
        st.bar_chart({"Data": [10, 25, 15, 30]})
    
    else:
        st.markdown(f"<h1 style='color: white;'>{menu}</h1>", unsafe_allow_html=True)
        st.warning("Halaman ini dalam tahap sinkronisasi data.")
