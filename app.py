import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems - CEO Erwin Sinaga", page_icon="🛡️", layout="wide")

# --- 2. BAKU & PERMANEN CSS (ESTETIKA EKSEKUTIF) ---
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; height: 45px; }
    
    /* Header Baku */
    .header-container { display: flex; align-items: center; justify-content: center; gap: 15px; margin-bottom: 30px; }
    .main-title { color: #1e3a8a; font-size: 2.5em; font-weight: bold; margin: 0; }
    
    /* Profil Section */
    .profile-box { background: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    
    /* Paket Layanan - Ramping & Tanpa HPP */
    .package-card { 
        background: white; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; 
        text-align: center; height: 100%; display: flex; flex-direction: column; 
    }
    .pkg-name { color: #1e3a8a; font-size: 1.5em; font-weight: bold; margin-bottom: 10px; }
    .pkg-price { color: #1e3a8a; font-size: 1.8em; font-weight: bold; margin: 10px 0; }
    .pkg-feat { text-align: left; font-size: 0.9em; margin: 15px 0; min-height: 120px; flex-grow: 1; }
</style>
""", unsafe_allow_html=True)

wa_number = "62821221190885"

# --- 3. LOGIKA HALAMAN ---
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 4. HEADER & PROFIL (KONSEP BAKU) ---
if st.session_state.page == "Home":
    st.markdown("""
    <div class="header-container">
        <img src="https://cdn-icons-png.flaticon.com/512/1004/1004666.png" width="40">
        <h1 class="main-title">VGUARD AI SYSTEMS</h1>
    </div>
    """, unsafe_allow_html=True)
    
    with st.container():
        c1, c2 = st.columns([1, 2.5])
        with c1:
            # Foto Profil (Aset baku Bapak)
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", caption="Erwin Sinaga - Founder & CEO")
        with c2:
            st.markdown('<div class="profile-box">', unsafe_allow_html=True)
            st.markdown("### 👤 Profil & Filosofi: Erwin Sinaga")
            st.write("""
            Pemimpin strategis dengan rekam jejak prestisius selama lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan nasional**. 
            **VGUARD AI** hadir sebagai perisai pertahanan bisnis Bapak untuk menjaga aset dengan presisi tinggi melalui teknologi AI.
            """)
            st.write("")
            if st.button("🚀 BUKA COMMAND CENTER (ADMIN)"): 
                st.session_state.page = "Admin"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")
    
    # --- CALCULATOR ROI ---
    st.markdown("#### 📊 ANALISIS PROTEKSI PROFIT & RESIKO FRAUD")
    ca, cb = st.columns(2)
    with ca: oz = st.number_input("Omzet Bulanan (Rp)", value=250000000)
    with cb: kb = st.slider("Estimasi Kebocoran (%)", 1, 15, 3)
    st.success(f"Potensi Profit Diselamatkan V-GUARD: Rp {(oz * (kb/100) * 0.95):,.0f} / bln")

    # --- PAKET LAYANAN STRATEGIS (KONSEP BAKU 4 KOLOM) ---
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
