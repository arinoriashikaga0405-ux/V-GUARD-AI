import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 2. CSS CUSTOM (VERSI STABIL & RAPI) ---
st.markdown("""
    <style>
    .stApp { background-color: #fcfcfc; color: #1a1a1a; }
    .header-container { text-align: center; margin-bottom: 30px; }
    .main-title { font-size: 3.5rem !important; font-weight: 800; color: #1a237e; margin-bottom: 0px; }
    .mission-box { 
        background-color: #ffffff; padding: 25px; border-radius: 10px; 
        border-left: 10px solid #1a237e; box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
        text-align: center; margin: 20px auto; max-width: 850px;
    }
    .pricing-card {
        background-color: #ffffff; padding: 25px; border-radius: 12px; 
        border: 1px solid #e0e0e0; text-align: center; height: 100%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .stButton>button {
        background-color: #1a237e; color: white; border-radius: 5px; 
        width: 100%; font-weight: bold; height: 3em;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    try:
        st.image("erwin.jpg", width=200)
    except:
        st.write("👤 PROFILE CEO")
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI Systems")
    st.write("---")
    menu = st.radio("NAVIGASI", ["Beranda Eksekutif", "Dashboard Performa", "AI Scanner"])

# --- 4. LOGIKA MENU ---
if menu == "Beranda Eksekutif":
    # Header
    st.markdown('<div class="header-container"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p><p style="color:#5c6bc0; letter-spacing:2px;">INTELLIGENCE FOR YOUR BUSINESS SECURITY</p></div>', unsafe_allow_html=True)

    # Misi
    st.markdown('<div class="mission-box"><p style="font-size:1.5rem; font-style:italic; color:#1a237e; margin:0;">Digitizing Trust, Eliminating Leakage</p></div>', unsafe_allow_html=True)

    st.write("---")
    # Profil
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("erwin.jpg", use_container_width=True)
        except:
            st.info("Foto Erwin")
    with col2:
        st.markdown("### PROFIL FOUNDER & CEO")
        st.write("Saya **Erwin**, Founder dan CEO VGUARD AI Systems. VGUARD AI lahir dari visi strategi untuk menghapus kebocoran operasional yang menggerogoti keuntungan bisnis di Indonesia.")
        st.markdown("### FILOSOFI PERISAI")
        st.write("VGUARD AI adalah Audit Officer pribadi Anda yang bekerja tanpa henti. Kami menghadirkan teknologi AI masa depan untuk mengamankan aset Anda dan mencegah kerugian secara sistemik.")

    st.write("---")
    st.write("### SOLUSI STRATEGIS KAMI")
    # 4 Paket
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.markdown('<div class="pricing-card"><b style="color:#1a237e">V-START</b><br><h2>2.5 JT</h2><p>Audit Harian Retail</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="pricing-card"><b style="color:#1a237e">V-GROW</b><br><h2>5 JT</h2><p>AI Fraud Detection</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="pricing-card"><b style="color:#1a237e">V-PRIME</b><br><h2>10 JT</h2><p>Multi Cabang</p></div>', unsafe_allow_html=True)
    with p4:
        st.markdown('<div class="pricing-card"><b style="color:#1a237e">V-CUSTOM</b><br><h2>NEGO</h2><p>Tailor Made</p></div>', unsafe_allow_html=True)

    st.write("---")
    if st.button("🛡️ HUBUNGI VGUARD AI SYSTEMS SEKARANG"):
        st.success("Admin kami akan segera menghubungi Anda.")

elif menu == "Dashboard Performa":
    st.title("📊 Dashboard Performa")
    st.line_chart(np.random.randn(20, 2))

elif menu == "AI Scanner":
    st.title("🔍 AI Scanner Audit")
    st.text_area("Input data log:")
    st.button("Jalankan Audit AI")

# --- 5. FOOTER ---
st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Tangerang, Indonesia")
