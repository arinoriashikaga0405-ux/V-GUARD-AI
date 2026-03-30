import streamlit as st
import os
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS CUSTOM UNTUK TAMPILAN PREMIUM & FOOTER
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 18px; }
    .package-box {
        height: 500px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        background-color: #ffffff;
        margin-bottom: 10px;
    }
    .footer-container {
        position: fixed;
        left: 0; bottom: 0; width: 100%;
        background-color: #f8f9fa; color: #31333F;
        text-align: center; padding: 15px 0px;
        font-weight: bold; border-top: 1px solid #dee2e6;
        z-index: 9999;
    }
    .stApp { margin-bottom: 100px; }
    .profile-text { text-align: justify; line-height: 1.8; }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.write("---")
    menu = st.radio("Folder Menu:", [
        "1. 👤 Profil & Filosofi", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Layanan", 
        "4. 🔐 Admin Dashboard"
    ])
    st.write("---")
    st.subheader("📡 Sistem Status")
    st.markdown('<p class="status-connected">● Connected</p>', unsafe_allow_html=True)
    st.write("---")
    st.link_button("📞 Konsultasi Langsung", wa_url, use_container_width=True)

# --- MENU 1: PROFIL & FILOSOFI ---
if menu == "1. 👤 Profil & Filosofi":
    st.header("👤 Strategic Leadership")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.subheader("Erwin Sinaga")
        st.markdown("""
        <div class="profile-text">
        Bapak Erwin Sinaga adalah seorang profesional dan Pemimpin Bisnis Senior dengan pengalaman lebih dari sepuluh tahun di perbankan dan manajemen aset. Beliau memiliki keahlian strategis dalam manajemen risiko dan perlindungan aset korporasi. Filosofi beliau berakar pada integritas dan transparansi data, meyakini bahwa teknologi AI dapat menutup celah fraud secara holistik.<br><br>
        V-Guard AI lahir dari visi beliau untuk membawa standar audit perbankan ke sektor UMKM dan korporasi melalui teknologi cerdas. Bapak Erwin berkomitmen menciptakan lingkungan bisnis yang aman dari kebocoran dana melalui deteksi anomali real-time.
        </div>
        """, unsafe_allow_html=True)

# --- MENU 2: VISI, MISI & ROI (ROI DI BAWAH) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Analisis Strategi")
    st.info("### 🎯 Visi 2026\nMenjadi standar utama keamanan audit AI di Indonesia.")
    st.
