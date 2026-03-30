import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIG & STATE ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. SIDEBAR ---
with st.sidebar:
    st.markdown("### 👤 CEO: ERWIN SINAGA")
    if st.button("🏠 Halaman Beranda"):
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.auth:
        if st.button("🔓 Keluar Admin"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()

# --- 3. BERANDA ---
if st.session_state.page == "Home":
    st.markdown("<h1 style='text-align: center; color: #1e3a8a;'>🛡️ VGUARD AI SYSTEMS</h1>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2.5])
    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=200)
        st.info("Erwin Sinaga - Founder & CEO")
        
    with c2:
        st.subheader("👤 Profil & Filosofi")
        st.write("""
        **Erwin Sinaga** adalah pemimpin strategis dengan pengalaman lebih dari sepuluh tahun sebagai eksekutif senior di perbankan nasional. 
        VGUARD AI Systems hadir sebagai solusi presisi tinggi untuk mengamankan aset bisnis Anda dari risiko kebocoran data dan kecurangan sistemik.
        """)
        if st.button("🚀 MASUK KE COMMAND CENTER"):
            st.session_state.page = "Admin"
            st.rerun()

    st.divider()
    st.markdown("#### 📊 ANALISIS PROTEKSI PROFIT")
    ca, cb = st.columns(2)
    with ca: 
        oz = st.number_input("Omzet Bulanan (Rp)", value=250000000)
    with cb: 
        kb = st.slider("Estimasi Kebocoran (%)", 1, 15, 3)
    
    st.success(f"Potensi Profit Diselamatkan: Rp {(oz * (kb/100) * 0.95):,.0f} / bln")

    st.divider()
    st.subheader("🏷️ PAKET LAYANAN")
    p1, p2, p3, p4 = st.columns(4)
    wa = "
