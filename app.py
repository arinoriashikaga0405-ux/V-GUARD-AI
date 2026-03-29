import streamlit as st
import pandas as pd
import numpy as np

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 2. CSS CUSTOM UNTUK TAMPILAN PREMIUM (DARK MODE LUXURY) ---
st.markdown("""
    <style>
    /* Background Utama */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    
    /* Header Container */
    .header-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        margin-bottom: 30px;
    }
    
    .big-title {
        font-size: 4rem !important;
        font-weight: 800;
        background: -webkit-linear-gradient(#38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }

    /* Misi Box Modern */
    .mission-container {
        border-top: 2px solid #38bdf8;
        border-bottom: 2px solid #38bdf8;
        padding: 20px 0;
        margin: 30px 0;
        text-align: center;
    }
    .mission-text {
        font-size: 1.8rem;
        font-weight: 300;
        letter-spacing: 2px;
        color: #e2e8f0;
    }

    /* Card Paket Harga Premium */
    .price-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 30px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: 0.4s;
        text-align: center;
        height: 100%;
    }
    .price-card:hover {
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid #38bdf8;
        transform: translateY(-10px);
    }

    /* Menyesuaikan Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0f172a !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Tombol Utama */
    .stButton>button {
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        font-size: 1.2rem;
        font-weight: bold;
        border-radius: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    try:
        st.image("erwin.jpg", width=220)
    except:
        st.write("👤 CEO PROFILE")
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI Systems")
    st.write("---")
    menu = st.radio("SISTEM NAVIGASI", ["BERANDA EKSEKUTIF", "ANALISIS REAL-TIME", "DATA AUDIT"])

# --- 4. LOGIKA MENU ---
if menu == "BERANDA EKSEKUTIF":
    # Header Section
    st.markdown('<div class="header-box">', unsafe_allow_html=True)
    st.markdown('<p class="big-title">VGUARD AI SYSTEMS</p>', unsafe_allow_html=True)
    st.write("NEXT GENERATION OPERATIONAL SECURITY")
    st.markdown('</div>', unsafe_allow_html=True)

    # Misi Section
    st.markdown('<div class="mission-container"><p class="mission-text">DIGITIZING TRUST, ELIMINATING LEAKAGE</p></div>', unsafe_allow_html=True)

    # Profil Section
    col1, col2 = st.columns([1, 1.5])
    with col1:
        try:
            st.image("erwin.jpg", use_container_width=True)
        except:
            st.info("Upload foto erwin.jpg ke GitHub")
    with col2:
        st.markdown("## VISI PEMIMPIN")
        st.write("Saya Erwin, memimpin VGUARD AI Systems untuk menghapus kebocoran operasional di Indonesia melalui integrasi teknologi kecerdasan buatan yang tak tertandingi.")
        st.markdown("## FILOSO
