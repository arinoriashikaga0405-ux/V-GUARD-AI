import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS UNTUK TAMPILAN PREMIUM & SEJAJAR SEMPURNA
st.markdown("""
<style>
    .main-header { font-size: 26px; font-weight: bold; color: #1f1f1f; margin-bottom: 20px; }
    .price-card {
        background: white; border-radius: 12px; border: 1px solid #eee;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); height: 500px;
        display: flex; flex-direction: column; justify-content: space-between;
        padding: 15px; margin-bottom: 5px;
    }
    .card-header {
        background: linear-gradient(135deg, #ff4b4b 0%, #a51d1d 100%);
        color: white; padding: 10px; text-align: center; font-weight: bold;
        border-radius: 8px; margin-bottom: 10px;
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

# --- FUNGSI RENDER PAKET (ANTI ERROR) ---
def render_box(title, setup, monthly, features):
    f_html = "".join([f"<div style='margin-bottom:8px;'>✅ {f}</div>" for f in features])
    st.markdown(f"""
    <div class="price-card">
        <div>
            <div class="card-header">{title}</div>
            <h4 style="margin:0;">Setup: Rp {setup}</h4>
            <p style="color:#ff4b4b; font-weight:bold;">Rp {monthly}/Bln</p>
            <hr>
            <div style="font-size:13px; color:#444;">{f_html}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button(f"Pilih {title}", wa_url, use_container_width=True)

# --- LOGIKA TAMPILAN MENU ---
if menu == "1. 🎯 Visi, Misi & ROI":
    st.markdown('<div class="main-header">Strategi & Analisis Risiko Bisnis</div>', unsafe_allow_html=True)
    v, m = st.columns(2)
    with v:
        st.markdown('<div class="vision-card"><h3>🎯 Visi</h3><p>Menjadi pemimpin pasar dalam solusi keamanan audit berbasis AI di Indonesia pada 2026.</p></div>', unsafe_allow_html=True)
    with m:
        st.markdown('<div class="vision-card"><h3>🚀 Misi</h3><ul><li>Deteksi fraud otomatis.</li><li>Laporan audit transparan.</li><li>Otomasi pengawasan aset 24/7.</li></ul></div>', unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Aset")
    omzet = st.number_input("Input Omzet Bulanan (Rp):", value=500000000, step=10000000)
    st.error(f"Potensi Kerugian Tanpa V-Guard: Rp {omzet * 0.05:,.0f} / Bulan")

elif menu == "2. 📦 Paket Layanan":
    st.markdown('<div class="main-header
