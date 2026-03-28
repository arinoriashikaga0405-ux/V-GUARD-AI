import streamlit as st
import pandas as pd

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. CSS MASTER (IDENTITAS VISUAL V-GUARD) ---
st.markdown("""
<style>
    .stApp { background-color: #001529 !important; font-family: 'Segoe UI', sans-serif; }
    
    /* STYLE LANDING PAGE PROMOSI */
    .hero-section {
        background: linear-gradient(45deg, #001529 30%, #002140 100%);
        padding: 40px 20px;
        border-radius: 20px;
        border: 1px solid #00f2ff;
        text-align: center;
        margin-bottom: 30px;
    }
    .promo-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 20px;
        border-radius: 12px;
        border-left: 4px solid #00f2ff;
        margin-bottom: 20px;
    }
    .feature-title { color: #00f2ff; font-weight: bold; font-size: 1.2rem; margin-bottom: 8px; }
    .feature-desc { color: #e0e0e0; font-size: 0.95rem; line-height: 1.5; }

    /* STYLE DASHBOARD (DIKUNCI) */
    [data-testid="stSidebar"] { background-color: #000c17 !important; border-right: 2px solid #FFD700; }
    [data-testid="stMetric"] { background-color: #002140 !important; border: 2px solid #004a99 !important; border-radius: 12px !important; }
    .cyan-header { color: #00f2ff !important; font-size: 1.5rem !important; font-weight: bold !important; border-bottom: 2px solid #00f2ff; padding-bottom: 10px; margin-top: 30px; }
    .btn-login>div>button { background-color: #00f2ff !important; color: #001529 !important; width: 100% !important; font-weight: bold !important; }
    .btn-logout>div>button { background-color: #ff4b4b !important; color: white !important; width: 100% !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA NAVIGASI ---
if 'page' not in st.session_state:
    st.session_state['page'] = 'promo'

# --- 4. TAMPILAN LANDING PAGE (DENGAN DESKRIPSI FIX) ---
if st.session_state['page'] == 'promo':
    # Banner Sirkuit dari gambar Screenshot 2026-03-28 171652.jpg
    st.image("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1350&q=80")
    
    st.markdown("<div class='hero-section'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: #00f2ff;'>🛡️ V-GUARD AI SOLUTIONS</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>Proteksi Bisnis Berbasis AI Generasi Terbaru</h3>", unsafe_allow_html=True)
    st.markdown("""
        <p style='color: #aaa; max-width: 850px; margin: auto;'>
        V-Guard hadir untuk mengatasi tantangan terbesar pemilik bisnis: kebocoran operasional. 
        Kami menyatukan kecerdasan buatan dengan audit finansial presisi tinggi untuk memastikan setiap rupiah aset Anda terlindungi.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("<div class='promo-card'>", unsafe_allow_html=True)
        st.markdown("<div class='feature-title'>🛡️ Deteksi Anomali Otomatis</div>", unsafe_allow_html=True)
        st.markdown("<div class='feature-desc'>Algoritma kami bekerja 24/7 mendeteksi ketidakwajaran transaksi dan pola operasional mencurigakan, mencegah fraud sebelum kerugian membengkak.</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='promo-card'>", unsafe_allow_html=True)
        st.markdown("<div class='feature-title'>📊 Audit Finansial Real-Time</div>", unsafe_allow_html=True)
        st.markdown("<div class='feature-desc'>Lupakan laporan manual. V-Guard memproses data arus kas dan tagihan secara instan, memberikan visualisasi 'Revenue Terproteksi' langsung di layar Anda.</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_b:
        st.markdown("<div class='promo-card'>", unsafe_allow_html=True)
        st.markdown("<div class='feature-title'>📽️ Intelligent Surveillance System</div>", unsafe_allow_html=True)
        st.markdown("<div class='feature-desc'>Integrasi stream CCTV pintar yang dapat diakses di mana saja melalui protokol RTSP, memudahkan pengawasan visual audit secara langsung.</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Login Box
        st.markdown("<div style='background: #002140; padding: 20px; border-radius: 15px; border: 1px solid #00f2ff;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='color: white; text-align: center;'>🔐 Akses Dashboard</h4>", unsafe_allow_html=True)
        u = st.text_input("Username", key="u_login")
        p = st.text_input("Password", type="password", key="p_login")
        st.markdown("<div class='btn-login'>", unsafe_allow_html=True)
        if st.button("MASUK KE SISTEM"):
            if u == "admin" and p == "vguard2026":
                st.session_state['page'] = 'dashboard'
                st.rerun()
            else: st.error("Kredensial salah.")
        st.markdown("</div></div>", unsafe_allow_html=True)

# --- 5. TAMPILAN DASHBOARD (DIKUNCI - SESUAI GAMBAR) ---
elif st.session_state['page'] == 'dashboard':
    with st.sidebar:
        st.markdown("<div style='text-align: center;'><img src='https://cdn-icons-png.flaticon.com/512/1055/1055644.png' width='80'><h2 style='color: #FFD700;'>V-GUARD AI</h2></div>", unsafe_allow_html=True)
        st.divider()
        st.markdown("### ⚙️ Pengaturan AI")
        st.selectbox("Mulai Operasional", ["10:00"], index=0)
        st.selectbox("Selesai Operasional", ["22:00"], index=0)
        st.success("🟢 Monitoring Aktif")
        st.divider()
        menu = st.radio("Menu Navigasi:", ["🔴 Executive Dashboard", "📊 Laporan Mingguan", "⚫ Audit Engine", "⚫ Finance", "⚫ HR Monitoring"])
        st.divider()
        st.markdown("<div class='btn-logout'>", unsafe_allow_html=True)
        if st.button("LOGOUT"):
            st.session_state['page'] = 'promo'
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    if menu == "🔴 Executive Dashboard":
        st.markdown("<h1 style='color: white;'>Executive Dashboard</h1>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        c1.metric("Audit Bulan Ini", "1,284", "12%")
        c2.metric("Anomali Terdeteksi", "42", "-5%", delta_color="inverse")
        c3.metric("Revenue Terproteksi", "IDR 8.2B", "8%")
        
        st.markdown("<div class='cyan-header'>🔔 Monitor Invoice & Tagihan</div>", unsafe_allow_html=True)
        col_inv, col_wa = st.columns([4, 1])
        with col_inv: 
            st.markdown("<div style='background: rgba(255,255,255,0.05); padding: 12px; border-radius: 8px; color: white;'>👤 Ko Shandy Vertigo | 💰 Rp 5.000.000 | 📅 30 Mar 2026</div>", unsafe_allow_html=True)
        with col_wa: st.button("🚀 Kirim WA", key="wa1")
        
        st.markdown("<div class='cyan-header'>📽️ Live CCTV Audit</div>", unsafe_allow_html=True)
        st.text_input("Link RTSP Cam:", "rtsp://admin:password@192.168.1.100:554/live")
        st.image("https://via.placeholder.com/1000x400.png?text=V-Guard+Live+Audit+Active")

    elif menu == "📊 Laporan Mingguan":
        st.markdown("<h1 style='color: white;'>📊 Laporan Mingguan</h1>", unsafe_allow_html=True)
        st.bar_chart(pd.DataFrame({"Data": [10, 25, 15, 30]}), color="#00f2ff")
