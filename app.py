import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - CEO Erwin Sinaga", page_icon="🛡️", layout="wide")

# --- 2. CSS BAKU (PUTIH BERSIH & RAPI) ---
st.markdown("""
<style>
    .stApp { background-color: white; }
    
    /* Header Tengah */
    .header-container {
        display: flex; align-items: center; justify-content: center;
        gap: 15px; padding: 30px 0;
    }
    .main-title {
        color: #1e3a8a; font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 2.5em; font-weight: 800; margin: 0;
    }
    
    /* Box Profil */
    .profile-box { 
        background: #f8fafc; padding: 25px; border-radius: 15px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-left: 5px solid #1e3a8a;
    }
    
    /* Paket Layanan (4 Kolom Ramping) */
    .package-card { 
        background: white; padding: 20px; border-radius: 12px; 
        border: 1px solid #e2e8f0; text-align: center; height: 100%;
        display: flex; flex-direction: column; 
    }
    .pkg-name { color: #1e3a8a; font-size: 1.5em; font-weight: bold; }
    .pkg-price { color: #1e3a8a; font-size: 1.8em; font-weight: bold; margin: 15px 0; }
    .wa-button { 
        display: block; background: #25d366; color: white !important; 
        text-decoration: none !important; padding: 12px; border-radius: 8px; 
        font-weight: bold; margin-top: auto;
    }
</style>
""", unsafe_allow_html=True)

wa_number = "62821221190885"

if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 3. BERANDA UTAMA (KEMBALI RAPI) ---
if st.session_state.page == "Home":
    # HEADER TENGAH
    st.markdown("""
    <div class="header-container">
        <img src="https://cdn-icons-png.flaticon.com/512/1004/1004666.png" width="50">
        <h1 class="main-title">VGUARD AI SYSTEMS</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # SEKSI PROFIL
    c1, c2 = st.columns([1, 2.5])
    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", use_container_width=True)
        st.info("Founder & CEO: Erwin Sinaga")
    with c2:
        st.markdown('<div class="profile-box">', unsafe_allow_html=True)
        st.markdown("### 👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        Pemimpin strategis dengan pengalaman lebih dari sepuluh tahun sebagai eksekutif senior di perbankan nasional. 
        **VGUARD AI Systems** hadir sebagai solusi presisi tinggi untuk mengamankan aset bisnis Anda dari risiko kebocoran data dan kecurangan sistemik.

        Filosofi Kami: **Presisi Tanpa Kompromi.**
        """)
        if st.button("🚀 MASUK KE COMMAND CENTER"):
            st.session_state.page = "Admin"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")
    
    # FITUR ANALISIS (YANG SEMPAT HILANG)
