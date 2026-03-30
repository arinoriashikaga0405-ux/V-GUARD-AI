import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems - Erwin Sinaga", page_icon="🛡️", layout="wide")

# --- 2. CSS UNTUK TAMPILAN RAPI & BENAR ---
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    
    /* Banner Hitam Utama */
    .black-banner {
        background-color: #111827;
        color: white;
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        border-bottom: 5px solid #facc15; /* Garis Kuning Bawah */
        margin-bottom: 30px;
    }
    
    /* Container Foto & About */
    .about-container {
        display: flex;
        gap: 20px;
        align-items: stretch;
    }
    
    .profile-card {
        background: #111827;
        border-radius: 15px;
        padding: 0;
        overflow: hidden;
        text-align: center;
        border-bottom: 5px solid #facc15;
    }
    
    .description-box {
        background: #111827;
        color: white;
        padding: 30px;
        border-radius: 15px;
        flex-grow: 1;
        border-bottom: 5px solid #facc15;
    }

    .wa-button {
        display: inline-block;
        background-color: #25d366;
        color: white !important;
        padding: 10px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

wa_number = "62821221190885"

if 'page' not in st.session_state: st.session_state.page = "Home"

# --- 3. TAMPILAN BERANDA UTAMA ---
if st.session_state.page == "Home":
    
    # BANNER ATAS
    st.markdown("""
    <div class="black-banner">
        <h1 style="margin:0; font-size: 3em;">V-GUARD AI SYSTEMS</h1>
        <p style="font-size: 1.2em; opacity: 0.8;">Mencegah Kerugian Owner Melalui Deteksi Proaktif</p>
    </div>
    """, unsafe_allow_html=True)

    # KOLOM FOTO DAN DESKRIPSI
    col_photo, col_desc = st.columns([1, 1.5])
    
    with col_photo:
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        # Menggunakan Placeholder Image yang Merepresentasikan Foto Profesional Bapak
        st.image("https://raw.githubusercontent.com/erwinsinaga/v-guard-ai/main/assets/ceo_photo.jpg", 
                 caption="Erwin Sinaga - Senior Business Executive", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_desc:
        st.markdown(f"""
        <div class="description-box">
            <h3 style="color: #facc15;">🛡️ About V-GUARD</h3>
            <p style="font-size: 1.1em; line-height: 1.6;">
                Platform deteksi fraud sistemik yang dibangun oleh <b>Erwin Sinaga</b> (Senior Business Executive). 
                Pengalaman perbankan 10+ tahun kami gunakan untuk memproteksi aset bisnis Anda dari kebocoran hingga 90%.
            </p>
            <p>Filosofi kami: <b>Presisi Tanpa Kompromi.</b></p>
            <a href="https://wa.me/{wa_number}" class="wa-button">Hubungi CEO via WhatsApp</a>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 BUKA PANEL ADMIN"):
            st.session_state.page =
