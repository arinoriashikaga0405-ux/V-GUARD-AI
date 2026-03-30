import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS UNTUK TAMPILAN PREMIUM & TINGGI KARTU SERAGAM
st.markdown("""
<style>
    .main-header { font-size: 24px; font-weight: bold; color: #1f1f1f; margin-bottom: 20px; }
    .price-card {
        background: white; border-radius: 12px; border: 1px solid #eee;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); height: 480px;
        padding: 20px; display: flex; flex-direction: column;
    }
    .card-header {
        background: #ff4b4b; color: white; padding: 10px;
        text-align: center; font-weight: bold; border-radius: 8px;
        margin-bottom: 15px;
    }
    .vision-card {
        background: #f8f9fa; padding: 20px; border-radius: 12px;
        border-left: 5px solid #ff4b4b; height: 220px;
    }
    .tech-item {
        background: #fff; padding: 10px; border-radius: 8px;
        border: 1px solid #ddd; margin-bottom: 8px; font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 3. SIDEBAR NAVIGASI (URUTAN BARU)
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Pilih Folder Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Layanan", 
        "4. 🔐 Admin Panel"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI Systems | Tangerang")

# --- MENU 1: PROFIL FOUNDER (PINDAH KE NOMOR 1) ---
if menu == "1. 👤 Profil Founder":
    st.header("👤 Strategic Leadership")
    col_img, col_txt = st.columns([1, 2])
    with col_txt:
        st.subheader("Erwin Sinaga")
        st.write("""
        Bapak Erwin Sinaga adalah Senior Business Leader dengan pengalaman lebih dari 10 tahun 
        di industri perbankan dan manajemen aset nasional. Beliau menginisiasi V-Guard AI 
        sebagai solusi deteksi kebocoran aset berbasis teknologi mutlak.
        """)

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.markdown('<div class="main-header">Strategi & Analisis Risiko</div>', unsafe_allow_html=True)
    v, m = st.columns(2)
    with v:
        st.markdown('<div class="vision-card"><h3>🎯 Visi</h3><p>Menjadi pemimpin pasar solusi audit AI di Indonesia pada 2026.</p></div>', unsafe_allow_html=True)
    with m:
        st.
