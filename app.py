import streamlit as st

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. STYLE PREMIUM DARK BLUE (CSS) ---
st.markdown("""
<style>
    /* Background Utama Navy Gelap */
    .stApp { background-color: #001529 !important; }
    
    /* Sidebar Lebih Gelap agar Logo Menonjol */
    [data-testid="stSidebar"] {
        background-color: #000c17 !important;
        border-right: 1px solid #002140;
    }

    /* Styling Logo di Sidebar */
    .sidebar-logo {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 10px 0;
    }
    .sidebar-logo img { width: 80px; margin-bottom: 10px; }
    .sidebar-logo h2 { color: #ffffff !important; font-size: 1.2rem; margin: 0; }

    /* Paksa Judul Header menjadi Biru Muda (Cyan) agar Terbaca */
    .cyan-header {
        color: #00f2ff !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        margin-top: 20px !important;
        margin-bottom: 15px !important;
        border-bottom: 2px solid #00f2ff33;
    }

    /* Kotak Metrik (Card) */
    [data-testid="stMetric"] {
        background-color: #002140 !important;
        border: 1px solid #004a99 !important;
        border-radius: 12px !important;
        border-left: 6px solid #f0c04a !important;
    }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; }
    [data-testid="stMetricLabel"] > div { color: #ced4da !important; }

    /* Styling Baris Invoice */
    .invoice-row {
        background: rgba(255,255,255,0.05);
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 8px;
        border: 1px solid #004a99;
    }
    .invoice-text { color: white !important; font-size: 1rem; }

    /* Tombol Logout Merah di Sidebar */
    .stButton>button[kind="secondary"] {
        background-color: #ff4b4b !important;
        color: white !important;
        border: none !important;
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA LOGIN ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align: center; color: white;'>🛡️ V-GUARD AI LOGIN</h1>", unsafe_allow_html=True)
    with st.container():
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        if st.button("Masuk"):
            if user == "admin" and pwd == "vguard2026":
                st.session_state.update({'logged_in': True, 'role': 'admin'})
                st.rerun()
            elif user == "shandy" and pwd == "vertigo123":
                st.session_state.update({'logged_in': True, 'role': 'client'})
                st.rerun()
    st.stop()

# --- 4. DASHBOARD UTAMA ---
if st.session_state['logged_in']:
    
    # --- SIDEBAR (KEMBALIKAN SEMUA FITUR) ---
    with st.sidebar:
        # Perbaikan Logo & Nama
        st.markdown("""
        <div class="sidebar-logo">
            <img src="https://cdn-icons-png.flaticon.com/512/1055/1055644.png">
            <h2>V-GUARD AI</h2>
        </div>
        """, unsafe_allow_html=True)
        st.divider()
        
        # Fitur Jam Operasional
        st.subheader("⚙️ Pengaturan AI")
        st.selectbox("Mulai Operasional", ["08:00", "09:00", "10:00"], index=2)
        st.selectbox("Selesai Operasional", ["20:00", "21:00", "22:00"], index=2)
        st.success("🟢 Monitoring Aktif")
        
        st.divider()
        
        # Navigasi Menu
        st.subheader("Menu Navigasi")
        menu = st.radio("Pilih:", [
            "🔴 Executive Dashboard", 
            "⚫ Audit Engine", 
            "⚫ Finance & Payment", 
            "⚫ HR & Payroll Monitoring"
        ], label_visibility="collapsed")
        
        st.divider()
        
        # TOMBOL LOGOUT (Hadir Kembali)
        st.write(f"Sesi: **{st.session_state['role'].upper()}**")
        if st.button("Logout", key="logout_sidebar", use_container_width=True, type="secondary"):
            st.session_state['logged_in'] = False
            st.rerun()

    # --- ISI KONTEN ---
    st.markdown(f"<h1 style='color: white;'>{menu}</h1>", unsafe_allow_html=True)
    
    # Metrik
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Audit Bulan Ini", "1,284", "12%")
    with m2: st.metric("Anomali Terdeteksi", "42", "-5%", delta_color="inverse")
    with m3: st.metric("Revenue Terproteksi", "IDR 8.2B", "8%")

    st.divider()
    
    # Judul Biru Muda (Monitor Invoice)
    st.markdown("<div class='cyan-header'>🔔 Monitor Invoice & Tagihan</div>", unsafe_allow_html=True)
    
    def baris_data(nama, info, tempo, k):
        c1, c2 = st.columns([4, 1])
        with c1:
            st.markdown(f"<div class='invoice-row'><span class='invoice-text'><b>{nama}</b> | {info} | {tempo}</span></div>", unsafe_allow_html=True)
        with c2:
            st.button("📩 Kirim WA", key=k, use_container_width=True)

    baris_data("Ko Shandy Vertigo", "Rp 5,000,000", "Tempo: 30 Mar 2026", "wa1")
    baris_data("Client SME B", "Rp 1,250,000", "Tempo: 02 Apr 2026", "wa2")

    st.divider()
    
    # Judul Biru Muda (CCTV)
    st.markdown("<div class='cyan-header'>📽️ Live CCTV Audit</div>", unsafe_allow_html=True)
    st.text_input("Link RTSP/IP Cam:", "rtsp://admin:password@192.168.1.100:554/live")
    st.image("https://via.placeholder.com/1000x400.png?text=Live+Audit+Active+Stream", use_column_width=True)
