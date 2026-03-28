import streamlit as st
import pandas as pd

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. CSS MASTER: TAMPILAN PC PROFESIONAL ---
st.markdown("""
<style>
    /* Background Utama */
    .stApp { background-color: #001529 !important; }

    /* MENGHILANGKAN GARIS TEPI / KURUNG DI GAMBAR */
    div.row-widget.stImage { text-align: center; border: none !important; }
    [data-testid="stMetricValue"] { border: none !important; }

    /* STYLE LANDING PAGE */
    .hero-container {
        padding: 40px;
        background: linear-gradient(180deg, #002140 0%, #001529 100%);
        border-radius: 20px;
        border: 1px solid #00f2ff;
        text-align: center;
        margin-top: 20px;
    }
    
    /* Box Login */
    .login-box {
        background-color: #001c36;
        padding: 30px;
        border-radius: 15px;
        border: 2px solid #00f2ff;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.2);
    }

    /* Teks Promosi */
    .promo-header { color: #00f2ff; font-size: 2.8rem; font-weight: bold; margin-bottom: 10px; }
    .promo-text { color: #ffffff; font-size: 1.1rem; line-height: 1.6; margin-bottom: 25px; }

    /* DASHBOARD SIDEBAR (DIKUNCI) */
    [data-testid="stSidebar"] { background-color: #000c17 !important; border-right: 2px solid #FFD700; }
    [data-testid="stSidebar"] * { color: #ffffff !important; }
    
    /* Metrik Dashboard */
    [data-testid="stMetric"] { background-color: #002140 !important; border: 2px solid #004a99 !important; border-radius: 12px !important; }
    [data-testid="stMetricLabel"] > div { color: #ffffff !important; font-weight: bold !important; font-size: 1.1rem !important; }
    
    /* Tombol Login (Cyan) & Logout (Merah) */
    .stButton>button[kind="primary"] { background-color: #00f2ff !important; color: #001529 !important; font-weight: bold !important; width: 100% !important; }
    .stButton>button[kind="secondary"] { background-color: #ff4b4b !important; color: white !important; font-weight: bold !important; width: 100% !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA NAVIGASI ---
if 'page' not in st.session_state:
    st.session_state['page'] = 'promo'

# --- 4. TAMPILAN LANDING PAGE (PROMOSI & LOGIN) ---
if st.session_state['page'] == 'promo':
    
    # 1. Gambar Banner (Auto Width PC)
    try:
        st.image("VGUARD-AI-BANNER.png", use_container_width=True)
    except:
        st.image("https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200", use_container_width=True)

    # 2. Deskripsi Promosi & Login Box
    st.markdown("<div class='hero-container'>", unsafe_allow_html=True)
    
    col_text, col_login = st.columns([2, 1], gap="large")
    
    with col_text:
        st.markdown("<div class='promo-header'>🛡️ V-GUARD AI SOLUTIONS</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='promo-text'>
        <b>V-Guard AI</b> adalah platform proteksi bisnis masa kini yang dirancang khusus untuk pemilik usaha dan investor. 
        Menggunakan teknologi audit cerdas untuk mengidentifikasi kebocoran operasional secara instan.
        <br><br>
        ✅ <b>Audit 24/7:</b> Monitoring otomatis tanpa henti.<br>
        ✅ <b>Loss Prevention:</b> Mencegah kebocoran dana operasional.<br>
        ✅ <b>Executive Reporting:</b> Laporan langsung ke genggaman Anda.
        </div>
        """, unsafe_allow_html=True)

    with col_login:
        st.markdown("<div class='login-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: white; text-align: center;'>🔑 Klien Login</h3>", unsafe_allow_html=True)
        user_input = st.text_input("Username", placeholder="admin", key="user_login")
        pass_input = st.text_input("Password", type="password", placeholder="vguard2026", key="pass_login")
        
        # TOMBOL LOGIN (DIKEMBALIKAN & DIPERJELAS)
        if st.button("MASUK KE DASHBOARD", type="primary"):
            if user_input == "admin" and pass_input == "vguard2026":
                st.session_state['page'] = 'dashboard'
                st.rerun()
            else:
                st.error("Username atau Password salah.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- 5. TAMPILAN DASHBOARD (ADMIN & KLIEN - TETAP DIKUNCI) ---
elif st.session_state['page'] == 'dashboard':
    with st.sidebar:
        st.markdown("<div style='text-align: center;'><img src='https://cdn-icons-png.flaticon.com/512/1055/1055644.png' width='80'><h2 style='color: #FFD700;'>V-GUARD AI</h2></div>", unsafe_allow_html=True)
        st.divider()
        st.markdown("### ⚙️ Pengaturan AI")
        st.selectbox("Mulai Operasional", ["10:00"], index=0)
        st.selectbox("Selesai Operasional", ["22:00"], index=0)
        st.success("🟢 Monitoring Aktif")
        st.divider()
        menu = st.radio("Navigasi:", ["🔴 Executive Dashboard", "📊 Laporan Mingguan", "⚫ Audit Engine", "⚫ Finance", "⚫ HR Monitoring"])
        st.divider()
        if st.button("KELUAR (LOGOUT)", type="secondary"):
            st.session_state['page'] = 'promo'
            st.rerun()

    if menu == "🔴 Executive Dashboard":
        st.markdown("<h1 style='color: white;'>🔴 Executive Dashboard</h1>", unsafe_allow_html=True)
        
        # Metrik Kontras Tinggi
        c1, c2, c3 = st.columns(3)
        c1.metric("Audit Bulan Ini", "1,284", "12%")
        c2.metric("Anomali Terdeteksi", "42", "-5%", delta_color="inverse")
        c3.metric("Revenue Terproteksi", "IDR 8.2B", "8%")
        
        # Tagihan
        st.markdown("<h3 style='color: #00f2ff; border-bottom: 2px solid #00f2ff; padding-bottom: 10px;'>🔔 Monitor Invoice</h3>", unsafe_allow_html=True)
        col_inv, col_wa = st.columns([4, 1])
        with col_inv: 
            st.markdown("<div style='background: rgba(255,255,255,0.05); padding: 12px; border-radius: 8px; color: white;'>👤 Ko Shandy Vertigo | 💰 Rp 5.000.000 | 📅 30 Mar 2026</div>", unsafe_allow_html=True)
        with col_wa: st.button("🚀 Kirim WA", key="wa_dashboard")
        
        # CCTV
        st.markdown("<h3 style='color: #00f2ff; margin-top: 20px;'>📽️ Live CCTV Audit</h3>", unsafe_allow_html=True)
        st.image("https://via.placeholder.com/1000x400.png?text=V-Guard+Live+Audit+Active", use_container_width=True)

    elif menu == "📊 Laporan Mingguan":
        st.markdown("<h1 style='color: white;'>📊 Laporan Mingguan</h1>", unsafe_allow_html=True)
        st.bar_chart(pd.DataFrame({"Data": [10, 25, 15, 30]}), color="#00f2ff")
