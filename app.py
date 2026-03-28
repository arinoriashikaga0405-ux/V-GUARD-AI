import streamlit as st

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. STYLE KONTRAS TINGGI (MEMAKSA TEKS PUTIH) ---
st.markdown("""
<style>
    /* Latar Belakang Utama & Sidebar */
    .stApp { background-color: #001529 !important; }
    [data-testid="stSidebar"] { background-color: #000c17 !important; border-right: 1px solid #002140; }

    /* MEMAKSA SEMUA TEKS DI SIDEBAR MENJADI PUTIH TERANG */
    [data-testid="stSidebar"] .stText, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] .stMarkdown p {
        color: #ffffff !important;
        font-weight: bold !important;
        opacity: 1 !important;
    }

    /* Memperbaiki Logo agar Rapi di Tengah */
    .sidebar-logo-container {
        text-align: center;
        padding: 20px 0;
    }
    .sidebar-logo-container img {
        width: 100px;
        border-radius: 10px;
        margin-bottom: 10px;
    }

    /* Judul Header (Biru Muda/Cyan Menyala) */
    .cyan-header {
        color: #00f2ff !important;
        font-size: 1.6rem !important;
        font-weight: bold !important;
        margin-top: 25px !important;
        border-bottom: 2px solid #00f2ff;
        padding-bottom: 5px;
    }

    /* Kartu Metrik dengan Angka Putih */
    [data-testid="stMetric"] {
        background-color: #002140 !important;
        border: 2px solid #004a99 !important;
        border-radius: 12px !important;
    }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; font-weight: bold !important; }
    [data-testid="stMetricLabel"] > div { color: #f0c04a !important; font-weight: bold !important; }

    /* Baris Data Invoice (Teks Putih di atas Biru) */
    .invoice-card {
        background: #002b55;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 1px solid #00f2ff;
    }
    .invoice-card b, .invoice-card span { color: white !important; }

    /* Tombol Logout Merah Terang */
    .stButton>button[kind="secondary"] {
        background-color: #ff4b4b !important;
        color: white !important;
        border: none !important;
        width: 100% !important;
        font-size: 1.1rem !important;
        height: 3em !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA AKSES ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align: center; color: white;'>🛡️ V-GUARD AI LOGIN</h1>", unsafe_allow_html=True)
    with st.container():
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("Masuk"):
            if u == "admin" and p == "vguard2026":
                st.session_state.update({'logged_in': True, 'role': 'admin'})
                st.rerun()
            elif u == "shandy" and p == "vertigo123":
                st.session_state.update({'logged_in': True, 'role': 'client'})
                st.rerun()
    st.stop()

# --- 4. DASHBOARD UTAMA ---
if st.session_state['logged_in']:
    
    with st.sidebar:
        # LOGO RAPI
        st.markdown("""
        <div class="sidebar-logo-container">
            <img src="https://cdn-icons-png.flaticon.com/512/1055/1055644.png">
            <h2 style="color: white !important;">V-GUARD AI</h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # PENGATURAN AI (Teks dipaksa putih)
        st.markdown("<h3 style='color: white !important;'>⚙️ Pengaturan AI</h3>", unsafe_allow_html=True)
        st.selectbox("Mulai Operasional", ["08:00", "09:00", "10:00"], index=2)
        st.selectbox("Selesai Operasional", ["20:00", "21:00", "22:00"], index=2)
        st.success("🟢 Monitoring Aktif")
        
        st.divider()
        
        # NAVIGASI (Teks dipaksa putih)
        st.markdown("<h3 style='color: white !important;'>Menu Navigasi</h3>", unsafe_allow_html=True)
        menu = st.radio("Nav", [
            "🔴 Executive Dashboard", 
            "⚫ Audit Engine", 
            "⚫ Finance & Payment", 
            "⚫ HR & Payroll Monitoring"
        ], label_visibility="collapsed")
        
        st.divider()
        
        # LOGOUT (Hadir Kembali & Jelas)
        st.markdown(f"<p style='color: white !important;'>Sesi: {st.session_state['role'].upper()}</p>", unsafe_allow_html=True)
        if st.button("Logout", key="out", use_container_width=True, type="secondary"):
            st.session_state['logged_in'] = False
            st.rerun()

    # KONTEN UTAMA
    st.markdown(f"<h1 style='color: white;'>{menu}</h1>", unsafe_allow_html=True)
    
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Audit Bulan Ini", "1,284", "12%")
    with m2: st.metric("Anomali Terdeteksi", "42", "-5%", delta_color="inverse")
    with m3: st.metric("Revenue Terproteksi", "IDR 8.2B", "8%")

    # Monitor Invoice dengan Teks Putih & Judul Cyan
    st.markdown("<div class='cyan-header'>🔔 Monitor Invoice & Tagihan</div>", unsafe_allow_html=True)
    
    def baris_invoice(nama, uang, tgl, key):
        c1, c2 = st.columns([4, 1])
        with c1:
            st.markdown(f"""
            <div class="invoice-card">
                <b>👤 {nama}</b> | 💰 {uang} | 📅 {tgl}
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.button("📩 Kirim WA", key=key, use_container_width=True)

    baris_invoice("Ko Shandy Vertigo", "Rp 5.000.000", "30 Mar 2026", "wa1")
    baris_invoice("Client SME B", "Rp 1.250.000", "02 Apr 2026", "wa2")

    # CCTV Section
    st.markdown("<div class='cyan-header'>📽️ Live CCTV Audit</div>", unsafe_allow_html=True)
    st.text_input("Link RTSP Camera:", "rtsp://admin:password@192.168.1.100:554/live")
    st.image("https://via.placeholder.com/1000x400.png?text=V-Guard+Live+Stream+Active", use_column_width=True)
