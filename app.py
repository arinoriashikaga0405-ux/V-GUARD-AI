import streamlit as st
import pandas as pd

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. CSS MASTER: CLEAN & PROFESSIONAL PC LOOK ---
st.markdown("""
<style>
    /* Background Utama & Reset */
    .stApp { background-color: #001529 !important; }
    
    /* MENGHILANGKAN SEMUA BENTUK KURUNG & GARIS TEPI */
    div.row-widget.stImage > div { border: none !important; box-shadow: none !important; }
    [data-testid="stMetricValue"] { border: none !important; }
    [data-testid="stVerticalBlock"] { gap: 0rem !important; }

    /* STYLE LANDING PAGE PROMOSI */
    .main-hero {
        padding: 50px;
        background: radial-gradient(circle, #002140 0%, #001529 100%);
        border-radius: 25px;
        border: 1px solid rgba(0, 242, 255, 0.3);
        margin-top: 20px;
    }
    
    .promo-title { color: #00f2ff; font-size: 3rem; font-weight: 800; margin-bottom: 15px; text-shadow: 0 0 10px rgba(0,242,255,0.5); }
    .promo-sub { color: #ffffff; font-size: 1.2rem; line-height: 1.7; margin-bottom: 30px; opacity: 0.9; }

    /* LOGIN BOX DENGAN EFEK KEREN */
    .login-container {
        background-color: #001c36;
        padding: 35px;
        border-radius: 20px;
        border: 2px solid #00f2ff;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.15);
    }

    /* TOMBOL LOGIN GLOW */
    .stButton>button[kind="primary"] {
        background: linear-gradient(90deg, #00f2ff, #00d4ff) !important;
        color: #001529 !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
        width: 100% !important;
        border: none !important;
        transition: 0.3s;
    }
    .stButton>button[kind="primary"]:hover {
        box-shadow: 0 0 20px #00f2ff !important;
        transform: scale(1.02);
    }

    /* DASHBOARD SIDEBAR & METRIK (DIKUNCI) */
    [data-testid="stSidebar"] { background-color: #000c17 !important; border-right: 2px solid #FFD700; }
    [data-testid="stMetric"] { background-color: #002140 !important; border: 2px solid #004a99 !important; border-radius: 15px !important; }
    .stButton>button[kind="secondary"] { background-color: #ff4b4b !important; color: white !important; width: 100% !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA NAVIGASI ---
if 'page' not in st.session_state:
    st.session_state['page'] = 'promo'

# --- 4. TAMPILAN LANDING PAGE ---
if st.session_state['page'] == 'promo':
    
    # Menampilkan Banner (Lebar PC Proporsional)
    try:
        st.image("VGUARD-AI-BANNER.png", use_container_width=True)
    except:
        st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200", use_container_width=True)

    # Konten Promosi & Login
    st.markdown("<div class='main-hero'>", unsafe_allow_html=True)
    col_desc, col_log = st.columns([1.8, 1], gap="large")
    
    with col_desc:
        st.markdown("<div class='promo-title'>🛡️ V-GUARD AI SOLUTIONS</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='promo-sub'>
        <b>Evolusi Keamanan Bisnis Anda Dimulai di Sini.</b><br>
        Kami menyediakan sistem audit pintar berbasis AI yang bekerja secara otonom untuk mendeteksi setiap sen kebocoran operasional.
        <br><br>
        💎 <b>Proteksi Aset:</b> Monitoring real-time 24 jam.<br>
        💎 <b>Audit Otomatis:</b> Tanpa perlu input manual yang melelahkan.<br>
        💎 <b>Decision Support:</b> Data akurat untuk keputusan investor cepat.
        </div>
        """, unsafe_allow_html=True)

    with col_log:
        st.markdown("<div class='login-container'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: white; text-align: center; margin-bottom: 20px;'>🔑 Portal Klien</h3>", unsafe_allow_html=True)
        uid = st.text_input("Username", placeholder="admin", key="l_user")
        pwd = st.text_input("Password", type="password", placeholder="vguard2026", key="l_pass")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("MASUK KE DASHBOARD", type="primary"):
            if uid == "admin" and pwd == "vguard2026":
                st.session_state['page'] = 'dashboard'
                st.rerun()
            else:
                st.error("Akses ditolak. Cek kredensial Anda.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- 5. TAMPILAN DASHBOARD (DIKUNCI - JANGAN RUBAH) ---
elif st.session_state['page'] == 'dashboard':
    with st.sidebar:
        st.markdown("<div style='text-align: center;'><img src='https://cdn-icons-png.flaticon.com/512/1055/1055644.png' width='80'><h2 style='color: #FFD700;'>V-GUARD AI</h2></div>", unsafe_allow_html=True)
        st.divider()
        st.markdown("### ⚙️ Pengaturan AI")
        st.selectbox("Mulai Operasional", ["10:00"])
        st.selectbox("Selesai Operasional", ["22:00"])
        st.success("🟢 Monitoring Aktif")
        st.divider()
        menu = st.radio("Navigasi:", ["🔴 Executive Dashboard", "📊 Laporan Mingguan", "⚫ Audit Engine", "⚫ Finance", "⚫ HR Monitoring"])
        st.divider()
        if st.button("KELUAR (LOGOUT)", type="secondary"):
            st.session_state['page'] = 'promo'
            st.rerun()

    if menu == "🔴 Executive Dashboard":
        st.markdown("<h1 style='color: white;'>🔴 Executive Dashboard</h1>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        c1.metric("Audit Bulan Ini", "1,284", "12%")
        c2.metric("Anomali Terdeteksi", "42", "-5%", delta_color="inverse")
        c3.metric("Revenue Terproteksi", "IDR 8.2B", "8%")
        
        st.markdown("<h3 style='color: #00f2ff; border-bottom: 2px solid #00f2ff; padding-bottom: 10px;'>🔔 Monitor Invoice</h3>", unsafe_allow_html=True)
        cinv, cwa = st.columns([4, 1])
        with cinv: st.markdown("<div style='background: rgba(255,255,255,0.05); padding: 12px; border-radius: 8px; color: white;'>👤 Ko Shandy Vertigo | 💰 Rp 5.000.000 | 📅 30 Mar 2026</div>", unsafe_allow_html=True)
        with cwa: st.button("🚀 Kirim WA", key="wa_main")
        
        st.markdown("<h3 style='color: #00f2ff; margin-top: 20px;'>📽️ Live CCTV Audit</h3>", unsafe_allow_html=True)
        st.image("https://via.placeholder.com/1000x400.png?text=V-Guard+Live+Audit+Active", use_container_width=True)
