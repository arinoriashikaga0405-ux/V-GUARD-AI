import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI UTAMA
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# Inisialisasi Database (Session State)
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = []

# 2. CSS CUSTOM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 18px; }
    .package-box { height: 680px; padding: 25px; border: 2px solid #f0f0f0; border-radius: 15px; background-color: #ffffff; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .footer-container { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #f8f9fa; text-align: center; padding: 15px 0px; font-weight: bold; border-top: 1px solid #dee2e6; z-index: 9999; }
    .stApp { margin-bottom: 120px; }
    .profile-text { text-align: justify; line-height: 1.8; font-size: 16px; }
</style>
""", unsafe_allow_html=True)

my_wa = "https://wa.me/628212190885"

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Folder Navigasi:", 
                    ["1. 👤 Profil Founder", 
                     "2. 🎯 Visi, Misi & ROI", 
                     "3. 📦 Produk & Paket", 
                     "4. 📝 Registrasi Klien",
                     "5. 🔐 Admin Dashboard"])
    st.markdown('<p class="status-connected">● System Online</p>', unsafe_allow_html=True)
    st.link_button("📞 Hubungi Erwin Sinaga", my_wa, use_container_width=True)

# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("👤 Strategic Leadership & Founder Philosophy")
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.subheader("Erwin Sinaga")
        st.markdown(f"""<div class="profile-text">
        Bapak Erwin Sinaga adalah seorang profesional dan Pemimpin Bisnis Senior dengan pengalaman lebih dari sepuluh tahun di dunia perbankan serta manajemen aset nasional. Beliau memiliki keahlian strategis dalam manajemen risiko kredit dan pengawasan kepatuhan operasional. V-Guard AI lahir dari visi beliau untuk membawa standar keamanan audit perbankan ke ekosistem UMKM dan perusahaan menengah. Beliau berkomitmen menciptakan lingkungan bisnis yang bersih dari kebocoran dana melalui teknologi cerdas.
        </div>""", unsafe_allow_html=True)

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Analisis Strategi Bisnis")
    c1, c2 = st.columns(2)
    with c1:
        st.info("### 🎯 Visi 2026\nMenjadi standar utama keamanan audit berbasis AI di seluruh ekosistem bisnis Indonesia.")
