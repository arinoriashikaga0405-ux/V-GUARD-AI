import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS TAMPILAN PREMIUM (SEMUA TANDA PETIK DIKUNCI RAPID)
st.markdown("""
<style>
    .main-header { font-size: 26px; font-weight: bold; color: #1f1f1f; margin-bottom: 20px; }
    .price-card {
        background: white; border-radius: 12px; border: 1px solid #eee;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); height: 500px;
        padding: 15px; display: flex; flex-direction: column;
    }
    .card-header {
        background: #ff4b4b; color: white; padding: 10px;
        text-align: center; font-weight: bold; border-radius: 8px;
        margin-bottom: 15px;
    }
    .vision-card {
        background: #f8f9fa; padding: 20px; border-radius: 12px;
        border-left: 5px solid #ff4b4b; height: 250px;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 3. SIDEBAR NAVIGASI
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.selectbox("Pilih Menu:", [
        "1. 🎯 Visi, Misi & ROI", 
        "2. 📦 Paket Layanan", 
        "3. 👤 Profil Founder", 
        "4. 🔐 Admin Panel"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI Systems | Tangerang")

# --- LOGIKA TAMPILAN MENU ---

if menu == "1. 🎯 Visi, Misi & ROI":
    st.markdown('<div class="main-header">Strategi & Analisis Risiko Bisnis</div>', unsafe_allow_html=True)
    v, m = st.columns(2)
    with v:
        st.markdown('<div class="vision-card"><h3>🎯 Visi</h3><p>Menjadi pemimpin pasar solusi audit AI di Indonesia pada 2026.</p></div>', unsafe_allow_html=True)
    with m:
        st.markdown('<div class="vision-card"><h3>🚀 Misi</h3><ul><li>Deteksi fraud otomatis.</li><li>Laporan audit transparan.</li><li>Otomasi pengawasan aset 24/7.</li></ul></div>', unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("📈 Kalkulator ROI")
    omzet = st.number_input("Input Omzet Bulanan (Rp):", value=500000000, step=10000000)
    st.error(f"Potensi Kerugian: Rp {omzet * 0.05:,.0f} / Bulan")

elif menu == "2. 📦 Paket Layanan":
    st.markdown('<div class="main-header">📦 Paket Proteksi V-Guard AI</div>', unsafe_allow_html=True)
    c1
