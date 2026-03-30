import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS CUSTOM UNTUK TAMPILAN PAKET & FOOTER
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
    .footer-fixed {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f8f9fa;
        color: #31333F;
        text-align: center;
        padding: 15px 0;
        font-weight: bold;
        border-top: 2px solid #dee2e6;
        z-index: 9999;
    }
    .custom-button {
        display: inline-block;
        padding: 10px 20px;
        background-color: #ffffff;
        color: #31333F;
        text-align: center;
        text-decoration: none;
        border: 1px solid #d1d3d8;
        border-radius: 5px;
        width: 100%;
        font-weight: bold;
    }
    .custom-button:hover { background-color: #f0f2f6; border-color: #1976d2; }
    .stApp { margin-bottom: 80px; }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.write("---")
    menu = st.radio("Folder Menu:", ["1. 👤 Profil & Filosofi", "2. 🎯 Visi, Misi & ROI", "3. 📦 Paket Layanan", "4. 🔐 Admin Dashboard"])
    st.write("---")
    st.subheader("📡 Sistem Status")
    st.markdown('<p class="status-connected">● Connected</p>', unsafe_allow_html=True)
    st.write("---")
    st.markdown(f'<a href="{wa_url}" target="_blank" class="custom-button">📞 Konsultasi Langsung</a>', unsafe_allow_html=True)

# --- MENU 3: PAKET LAYANAN DENGAN FITUR LENGKAP ---
if menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Proteksi V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    
    # Rincian fitur dikembalikan sesuai gambar referensi sebelumnya
    with c1:
        st.markdown("""<div class="package-box"><h3>BASIC</h3><b>Setup: 2.5jt</b><br>Monthly: 750rb<hr>
        <ul><li>📊 Audit Harian</li><li>📁 Lap. PDF Mingguan</li><li>📱 Support WA</li></ul></div>""", unsafe_allow_html=True)
        st.markdown(f'<a href="{wa_url}" target="_blank" class="custom-button">Pilih BASIC</a>', unsafe_allow_html=True)
        
    with c2:
        st.markdown("""<div class="package-box"><h3>MEDIUM</h3><b>Setup: 7.5jt</b><br>Monthly: 1.5jt<hr>
        <ul><li>🤖 AI Detection & CCTV</li><li>📈 Analisis Tren Fraud</li><li>🚨 Alert System</li></ul></div>""", unsafe_allow_html=True)
        st.markdown(f'<a href="{wa_url}" target="_blank" class="custom-button">Pilih MEDIUM</a>', unsafe_allow_html=True)
        
    with c3:
        st.markdown("""<div class="package-box"><h3>ENTERPRISE</h3><b>Setup: 25jt</b><br>Monthly: 5jt<hr>
        <ul><li>🏢 Multi-Branch System</li><li>🖥️ Admin Dashboard</li><li>🧾 Auto-Invoice</li></ul></div>""", unsafe_allow_html=True)
        st.markdown(f'<a href="{wa_url}" target="_blank" class="custom-button">Pilih ENTERPRISE</a>', unsafe_allow_html=True)
        
    with c4:
        st.markdown("""<div class="package-box"><h3>CORPORATE</h3><b>Setup: 50jt</b><br>Monthly: 10jt<hr>
        <ul><li>🏗️ Custom AI Development</li><li>🕵️ Audit On-Site</li><li>📞 Priority 24/7 Support</li></ul></div>""", unsafe_allow_html=True)
        st.markdown(f'<a href="{wa_url}" target="_blank" class="custom-button">Pilih CORPORATE</a>', unsafe_allow_html=True)

# --- MENU LAINNYA ---
elif menu == "1. 👤 Profil & Filosofi":
    st.header("👤 Strategic Leadership")
    st.write("Bapak Erwin Sinaga adalah Pemimpin Bisnis Senior dengan pengalaman 10+ tahun di perbankan & manajemen aset.") # Minimal 100 kata tetap dipertahankan di app Bapak

elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Strategi ROI")
    st.info("### 🎯 Visi\nMenjadi standar utama keamanan audit AI di Indonesia pada 2026.")

# 4. FOOTER TETAP ADA
st.markdown("""<div class="footer-fixed">© 2026 V-Guard AI Systems - Secured by Advanced Intelligence.</div>""", unsafe_allow_html=True)
