import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# CSS UNTUK TAMPILAN PREMIUM & TINGGI KARTU SERAGAM
st.markdown("""
<style>
    .main-header { font-size: 28px; font-weight: bold; color: #1f1f1f; margin-bottom: 20px; }
    .price-card {
        background: white; border-radius: 12px; border: 1px solid #eee;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); height: 500px;
        display: flex; flex-direction: column; justify-content: space-between;
        padding: 20px; margin-bottom: 10px;
    }
    .card-header {
        background: #ff4b4b; color: white; padding: 10px;
        text-align: center; font-weight: bold; border-radius: 8px;
        margin-bottom: 15px;
    }
    .vision-card {
        background: #f8f9fa; padding: 20px; border-radius: 12px;
        border-left: 5px solid #ff4b4b; height: 260px;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 2. SIDEBAR NAVIGASI
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    # Menu navigasi yang simpel agar folder tidak macet
    menu = st.selectbox("Pilih Folder Menu:", [
        "1. 🎯 Visi, Misi & ROI", 
        "2. 📦 Paket Layanan", 
        "3. 👤 Profil Founder", 
        "4. 🔐 Admin Panel"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI Systems | Tangerang")

# --- FUNGSI TAMPILAN PAKET (SOLUSI ANTI-ERROR) ---
def render_paket(title, setup, monthly, features):
    f_html = "".join([f"<div style='margin-bottom:8px;'>✅ {f}</div>" for f in features])
    st.markdown(f"""
    <div class="price-card">
        <div>
            <div class="card-header">{title}</div>
            <h4 style="margin-bottom:5px;">Setup: Rp {setup}</h4>
            <p style="color:#ff4b4b; font-weight:bold;">Bulan: Rp
