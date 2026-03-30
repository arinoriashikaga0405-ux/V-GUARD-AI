import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# CSS UNTUK TAMPILAN PREMIUM
st.markdown("""
<style>
    .tech-card {
        background: #fdfdfd; border-radius: 10px; padding: 12px;
        border-left: 5px solid #ff4b4b; margin-bottom: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .tech-title { font-weight: bold; color: #1f1f1f; font-size: 15px; }
    .tech-desc { font-size: 12px; color: #555; }
    .alarm-box {
        background: #fff5f5; border: 1px solid #ff4b4b;
        padding: 15px; border-radius: 10px; color: #a51d1d; font-size: 14px;
    }
    .invoice-box {
        background: #f0fff4; border: 1px solid #38a169;
        padding: 15px; border-radius: 10px; color: #276749; font-size: 14px;
    }
    .vision-mission-box {
        background: #ffffff; border-radius: 12px; padding: 20px;
        border-left: 5px solid #ff4b4b; box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .price-card {
        background: white; border-radius: 15px; padding: 0px; border: 1px solid #eee;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); height: 420px;
        display: flex; flex-direction: column; overflow: hidden;
    }
    .card-header {
        background: linear-gradient(135deg, #ff4b4b 0%, #a51d1d 100%);
        color: white; padding: 15px; text-align: center; font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 2. SIDEBAR DENGAN FOTO FOUNDER DI ATAS LOGO (MENU NOMOR 1)
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.error("Unggah foto 'erwin.jpg' ke folder GitHub.")
    
    st.title("🛡️ V-Guard AI")
    st.write("---")
    menu = st.radio("Pilih Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🏠 Home: Ekosistem AI", 
        "3. 📦 Paket Solusi", 
        "4. 🔐 Admin Panel"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI Systems")

# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with r:
        st.subheader("Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        st.write("""
        Bapak Erwin Sinaga adalah seorang Senior Business Leader visioner dengan rekam jejak impresif selama lebih dari sepuluh tahun 
        menduduki posisi strategis sebagai CEO dan CSO dalam industri perbankan serta manajemen aset. Pengalaman mendalam beliau 
        dalam memitigasi fraud finansial menjadi pondasi utama berdirinya V-Guard AI Systems.
        """)

# --- MENU 2: HOME & EKOSISTEM TEKNOLOGI ---
elif menu == "2. 🏠 Home: Ekosistem AI":
    st.title("🛡️ Keamanan Masa Depan dengan AI")
    
    # VISI & MISI
    col_v, col
