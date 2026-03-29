import streamlit as st
import pandas as pd
import numpy as np

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 2. CSS PREMIUM (DARK MODE LUXURY) ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    .header-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    .big-title {
        font-size: 3.5rem !important;
        font-weight: 800;
        background: -webkit-linear-gradient(#38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .mission-container {
        border-top: 1px solid #38bdf8;
        border-bottom: 1px solid #38bdf8;
        padding: 15px 0;
        margin: 20px 0;
        text-align: center;
    }
    .price-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
    }
    section[data-testid="stSidebar"] {
        background-color: #0f172a !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    try:
        st.image("erwin.jpg", width=200)
    except:
        st.write("👤 CEO PROFILE")
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI Systems")
    st.write("---")
    menu = st.sidebar.radio("NAVIGASI", ["BERANDA", "DASHBOARD", "AI SCANNER"])

# --- 4. LOGIKA MENU ---
if menu == "BERANDA":
    st.markdown('<div class="header-box">', unsafe_allow_html=True)
    st.markdown('<p class="big-title">VGUARD AI SYSTEMS</p>', unsafe_allow_html=True)
    st.write("NEXT GENERATION OPERATIONAL SECURITY")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="mission-container"><h3>DIGITIZING TRUST, ELIMINATING LEAKAGE</h3></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.5])
    with col1:
        try:
            st.image("erwin.jpg", use_container_width=True)
        except:
            st.info("Foto Erwin")
    with col2:
        st.write("### VISI PEMIMPIN")
        st.write("Saya Erwin, memimpin VGUARD AI Systems untuk menghapus kebocoran operasional di Indonesia melalui integrasi teknologi kecerdasan buatan.")
        st.write("### FILOSOFI")
        st.write("VGUARD AI adalah perisai digital yang bekerja tanpa henti untuk mengamankan aset bisnis Anda.")

    st.write("---")
    st.write("### SOLUSI STRATEGIS")
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.markdown('<div class="price-card"><h4>V-START</h4><h3 style="color:#38bdf8">2.5 JT</h3><p>Audit Harian</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="price-card"><h4>V-GROW</h4><h3 style="color:#38bdf8">5 JT</h3><p>Fraud Detection</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="price-card"><h4>V-PRIME</h4><h3 style="color:#38bdf8">10 JT</h3><p>Multi Cabang</p></div>', unsafe_allow_html=True)
    with p4:
        st.markdown('<div class="price-card"><h4>V-CUSTOM</h4><h3 style="color:#38bdf8">NEGO</h3><p>Tailor Made</p></div>', unsafe_allow_html=True)

elif menu == "DASHBOARD":
    st.title("📊 Dashboard Performa")
    st.line_chart(np.random.randn(20, 2))

elif menu == "AI SCANNER":
    st.title("🔍 AI Scanner Audit")
    st.button("Jalankan Audit AI")

# --- 5. FOOTER ---
st.write("---")
st.caption("2026 VGUARD AI Systems | Tangerang")
