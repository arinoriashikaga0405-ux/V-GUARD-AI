import streamlit as st
import pandas as pd
import numpy as np

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Founder Erwin", page_icon="🛡️", layout="wide")

# --- 2. CSS CUSTOM ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .big-title { font-size: 3rem !important; font-weight: bold; color: #1a237e; margin-bottom: 0px;}
    .mission-box { background-color: #ffffff; padding: 20px; border-radius: 10px; border-left: 10px solid #1a237e; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin: 20px 0;}
    .stInfo, .stWarning, .stError, .stSuccess { border-radius: 10px; padding: 20px !important; color: black; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    try:
        st.image("erwin.jpg", width=200, caption="Erwin - Founder & CEO")
    except:
        st.write("Profil CEO")
    st.title("VGUARD AI")
    st.write("---")
    menu = st.radio("Navigasi", ["Beranda", "Dashboard", "AI Scanner"])

# --- 4. LOGIKA MENU ---
if menu == "Beranda":
    # HEADER
    st.markdown('<p class="big-title">VGUARD AI Systems</p>', unsafe_allow_html=True)
    st.write("Next Generation Operational Security and Revenue Optimization")
    st.write("---")

    # MISI (Tanpa tanda petik/bintang)
    st.write("MISI KAMI")
    st.markdown('<div class="mission-box">Digitizing Trust, Eliminating Leakage</div>', unsafe_allow_html=True)

    # PROFIL & FILOSOFI
    st.write("---")
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("erwin.jpg", width=250)
        except:
            st.write("Foto Founder")
    with col2:
        st.write("PROFIL FOUNDER DAN CEO")
        st.write("Saya Erwin, Founder dan CEO VGUARD AI Systems. VGUARD AI lahir dari visi untuk menghapus kebocoran operasional dan mengoptimalkan keuntungan bisnis di Indonesia.")
        
        st.write("FILOSOFI KEAMANAN")
        st.write("VGUARD AI adalah Audit Officer pribadi Anda yang bekerja 24 jam. Kami menghadirkan teknologi AI masa depan untuk mengamankan aset Anda dan mencegah kerugian secara sistemik.")

    # 4 PAKET HARGA (Bersih)
    st.write("---")
    st.write("PILIH SOLUSI KEAMANAN ANDA")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.info("V-START \n\n Rp 2,5 Juta \n\n Audit Harian")
    with c2:
        st.warning("V-GROW \n\n Rp 5 Juta \n\n Fraud Detection")
    with c3:
        st.error("V-PRIME \n\n Rp 10 Juta \n\n Multi Cabang")
    with c4:
        st.success("V-CUSTOM \n\n Negotiable \n\n Tailor Made")

elif menu == "Dashboard":
    st.title("Dashboard Performa")
    st.line_chart(pd.DataFrame(np.random.randn(20, 2), columns=['Aset', 'Keamanan']))

elif menu == "AI Scanner":
    st.title("AI Scanner Audit")
    st.write("Sistem VGUARD AI Online")
    if st.button("Jalankan Analisis"):
        st.info("Menganalisis data...")

# --- 5. FOOTER ---
st.write("---")
st.caption("2026 VGUARD AI Systems | Tangerang Indonesia")
