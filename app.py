import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Erwin Sinaga", page_icon="🛡️", layout="wide")

# --- 2. CSS TAMPILAN RAPI (HITAM & KUNING) ---
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    
    /* Banner Hitam Atas */
    .black-banner {
        background-color: #111827;
        color: white;
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        border-bottom: 5px solid #facc15;
        margin-bottom: 30px;
    }
    
    /* Box Deskripsi Hitam */
    .description-box {
        background: #111827;
        color: white;
        padding: 30px;
        border-radius: 15px;
        height: 100%;
        border-bottom: 5px solid #facc15;
    }

    .wa-button {
        display: inline-block;
        background-color: #25d366;
        color: white !important;
        padding: 12px 25px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = "Home"

# --- 3. LOGIKA HALAMAN ---
if st.session_state.page == "Home":
    
    # BANNER UTAMA
    st.markdown("""
    <div class="black-banner">
        <h1 style="margin:0; font-size: 3em;">V-GUARD AI SYSTEMS</h1>
        <p style="font-size: 1.2em; opacity: 0.8;">Mencegah Kerugian Owner Melalui Deteksi Proaktif</p>
    </div>
    """, unsafe_allow_html=True)

    # KONTEN PROFIL (FOTO & ABOUT)
    col_photo, col_desc = st.columns([1, 1.5])
    
    with col_photo:
        # Foto Profil Strategis
        st.image("https://raw.githubusercontent.com/erwinsinaga/v-guard-ai/main/assets/ceo_photo.jpg", 
                 caption="Erwin Sinaga - Senior Business Executive", use_container_width=True)
        
    with col_desc:
        st.markdown(f"""
        <div class="description-box">
            <h3 style="color: #facc15;">🛡️ About V-GUARD</h3>
            <p style="font-size: 1.1em; line-height: 1.6;">
                Platform deteksi fraud sistemik yang dibangun oleh <b>Erwin Sinaga</b> (Senior Business Executive). 
                Pengalaman perbankan 10+ tahun kami gunakan untuk memproteksi aset bisnis Anda dari kebocoran hingga 90%.
            </p>
            <p>Filosofi Kami: <b>Presisi Tanpa Kompromi</b>.</p>
            <a href="https://wa.me/62821221190885" class="wa-button">💬 Hubungi CEO via WhatsApp</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        if st.button("🚀 MASUK KE COMMAND CENTER"):
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    
    # 4 PAKET LAYANAN STRATE
