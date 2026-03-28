import streamlit as st
import pandas as pd

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. CSS MASTER (DIKUNCI) ---
st.markdown("""
<style>
    .stApp { background-color: #001529 !important; font-family: 'Segoe UI', sans-serif; }
    
    /* STYLE LANDING PAGE PROMOSI */
    .hero-section {
        background: linear-gradient(45deg, #001529 30%, #002140 100%);
        padding: 60px 20px;
        border-radius: 20px;
        border: 1px solid #00f2ff;
        text-align: center;
        margin-bottom: 40px;
    }
    .promo-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 25px;
        border-radius: 15px;
        border-left: 4px solid #00f2ff;
        margin-bottom: 20px;
    }
    .feature-title { color: #00f2ff; font-weight: bold; font-size: 1.3rem; margin-bottom: 10px; }
    .feature-desc { color: #e0e0e0; font-size: 1rem; line-height: 1.6; }

    /* STYLE DASHBOARD (DIKUNCI) */
    [data-testid="stSidebar"] { background-color: #000c17 !important; border-right: 2px solid #FFD700; }
    [data-testid="stMetric"] { background-color: #002140 !important; border: 2px solid #004a99 !important; border-radius: 12px !important; }
    [data-testid="stMetricLabel"] > div { color: #ffffff !important; font-weight: bold !important; font-size: 1.1rem !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; font-weight: bold !important; }
    .cyan-header { color: #00f2ff !important; font-size: 1.5rem !important; font-weight: bold !important; border-bottom: 2px solid #00f2ff; padding-bottom: 10px; margin-top: 30px; }
    .btn-login>div>button { background-color: #00f2ff !important; color: #001529 !important; width: 100% !important; font-weight: bold !important; }
    .btn-logout>div>button { background-color: #ff4b4b !important; color: white !important; width: 100% !important; font-weight: bold !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA NAVIGASI ---
if 'page' not in st.session_state:
    st.session_state['page'] = 'promo'

# --- 4. TAMPILAN LANDING PAGE (DENGAN DESKRIPSI MENDALAM) ---
if st.session_state['page'] == 'promo':
    # Hero Visual
    st.image("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1350&q=80")
    
    st.markdown("<div class='hero-section'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: #00f2ff;'>V-GUARD AI SOLUTIONS</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>The Future of Loss Detection & Business Protection</h3>", unsafe_allow_html=True)
    st.markdown("""
        <p style='color: #aaa; max-width: 800px; margin: auto;'>
        V-Guard hadir sebagai solusi mutakhir bagi pemilik bisnis dan investor untuk mengeliminasi kebocoran operasional secara real-time. 
        Kami menggabungkan kecerdasan buatan (AI) dengan sistem monitoring yang presisi untuk menjaga aset dan memaksimalkan profit Anda.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Deskripsi Fitur Mendalam
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("<div class='promo-card'>", unsafe_allow_html=True)
        st.markdown("<div class='feature-title'>🛡️ AI-Driven Loss Detection</div>", unsafe_allow_html=True)
        st.markdown("<div class='feature-desc'>Algoritma V-Guard mampu mendeteksi anomali transaksi dan perilaku operasional yang mencurigakan dalam hitungan detik. Lindungi bisnis Anda dari fraud internal maupun eksternal secara otomatis.</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='promo-card'>", unsafe_allow_html=True)
        st.markdown("<div class='feature-title'>📊 Real-Time Financial Audit</div>", unsafe_allow_html=True)
        st.markdown("<div class='feature-desc'>Lupakan laporan manual yang lambat. V
