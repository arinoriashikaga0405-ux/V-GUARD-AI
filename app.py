import streamlit as st
import os

# 1. KONFIGURASI DASAR
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# CSS UNTUK TAMPILAN PRESTIGE & SEJAJAR
st.markdown("""
<style>
    .price-card {
        background: white; border-radius: 15px; border: 1px solid #eee;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); height: 500px;
        display: flex; flex-direction: column; justify-content: space-between;
        padding-bottom: 20px;
    }
    .card-header {
        background: #ff4b4b; color: white; padding: 15px;
        text-align: center; font-weight: bold; border-radius: 15px 15px 0 0;
    }
    .card-body { padding: 20px; flex-grow: 1; font-size: 14px; }
    .vision-card {
        background: #f8f9fa; padding: 20px; border-radius: 15px;
        border-left: 5px solid #ff4b4b; height: 250px;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 2. NAVIGASI SIDEBAR
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi:", ["🏠 Home & ROI", "📦 Paket Solusi", "👤 Profil Founder", "🔐 Admin Panel"])
    st.write("---")
    st.caption("© 2026 V-Guard AI Systems | Tangerang")

# --- FUNGSI MODULAR (ANTI ERROR) ---
def tampilkan_paket(title, setup, monthly, features, key):
    f_html = "".join([f"<div style='margin-bottom:8px;'>✅ {f}</div>" for f in features])
    st.markdown(f"""
    <div class="price-card">
        <div class="card-header">{title}</div>
        <div class="card-body">
            <h4 style="margin:0;">Setup: Rp {setup}</h4>
            <p style="color:#ff4b4b; font-weight:bold;">Bulan: Rp {monthly}</p>
            <hr>
            {f_html}
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button(f"Pilih {title}", wa_url, use_container_width=True, key=key)

# --- LOGIKA MENU ---
if menu == "🏠 Home & ROI":
    st.header("🛡️ Keamanan Masa Depan dengan AI")
    
    # Visi & Misi Sejajar
    v, m = st.columns(2)
    with v:
        st.markdown('<div class="vision-card"><h3>🎯 Visi</h3><p>Menjadi pemimpin pasar solusi audit AI di Indonesia pada 2026.</p></div>', unsafe_allow_html=True)
    with m:
        st.markdown('<div class="vision-card"><h3>🚀 Misi</h3><ul><li>Deteksi fraud otomatis.</li><li>Audit transparan 24/7.</li></ul></div>', unsafe_allow_html=True)

    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Aset")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=500000000)
    st.error(f"Potensi Kerugian Tanpa V-Guard: Rp {omzet * 0.05:,.0f}")

elif menu == "📦 Paket Solusi":
    st.header("📦 Pilih Paket Proteksi Anda")
    # MENGGUNAKAN 4 KOLOM LANGSUNG (SOLUSI AGAR SEJAJAR)
    c1, c2, c3, c4 = st.columns(4)
    
    with c1: tampilkan_paket("BASIC (MIKRO)", "2.5jt", "500rb", ["Gemini AI", "Audit Harian"], "b1")
    with c2: tampilkan_paket("MEDIUM (SME)", "7.5jt", "1.5jt", ["MindBridge", "Alarm System"], "b2")
    with c3: tampilkan_paket("ENTERPRISE", "25jt", "5jt", ["YOLO CCTV", "Forecasting"], "b3")
    with c4: tampilkan_paket("CORPORATE", "50jt", "10jt", ["Custom AI", "Full Ops"], "b4")

elif menu == "👤 Profil Founder":
    st.header("Strategic Leadership")
    st.subheader("Erwin Sinaga")
    st.write("Senior Business Leader dengan 10+ tahun pengalaman di perbankan & asset management.")

elif menu == "🔐 Admin Panel":
    st.header("🔐 Intelligence Center")
    st.info("Status Sistem: Lancar (12 Data dalam antrean)")
    st.error("🚨 Deteksi Anomali: Cabang Tangerang")
