import streamlit as st
import os
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS CUSTOM UNTUK FOOTER & TAMPILAN
st.markdown("""
<style>
    .alarm-banner {
        background-color: #ff4b4b; color: white; padding: 15px;
        border-radius: 10px; text-align: center; font-weight: bold;
        border: 2px solid white; animation: blinker 1s linear infinite;
        margin-bottom: 20px;
    }
    @keyframes blinker { 50% { opacity: 0.2; } }
    .status-connected { color: #28a745; font-weight: bold; font-size: 18px; }
    .package-box {
        height: 430px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        background-color: #ffffff;
        margin-bottom: 10px;
    }
    /* STYLE UNTUK FOOTER PESANAN BAPAK */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f8f9fa;
        color: #6c757d;
        text-align: center;
        padding: 10px;
        font-size: 13px;
        border-top: 1px solid #dee2e6;
        z-index: 999;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.write("---")
    menu = st.radio("Folder Menu:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 📦 Paket Layanan", "4. 🔐 Admin Dashboard"])
    st.write("---")
    st.subheader("📡 Sistem Status")
    st.markdown('<p class="status-connected">● Connected</p>', unsafe_allow_html=True)
    st.link_button("📞 Konsultasi Langsung", wa_url, use_container_width=True)

# --- MENU 1: PROFIL ---
if menu == "1. 👤 Profil Founder":
    st.header("👤 Strategic Leadership")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
    with col2:
        st.subheader("Erwin Sinaga")
        st.write("Pemimpin Bisnis Senior dengan pengalaman 10+ tahun di perbankan & manajemen aset. V-Guard AI adalah visi beliau untuk membawa standar audit bank ke sektor UMKM dan Korporasi melalui teknologi AI.")

# --- MENU 2: ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Analisis ROI")
    st.info("### 🎯 Visi 2026\nMenjadi standar utama keamanan audit AI di Indonesia.")
    st.write("---")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=500000000)
    st.error(f"Potensi Kebocoran (5%): Rp {omzet*0.05:,.0f}")
    st.success(f"Penyelamatan V-Guard: Rp {omzet*0.05*0.9:,.0f}")

# --- MENU 3: PAKET ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Proteksi")
    c1, c2, c3, c4 = st.columns(4)
    # List paket sudah sejajar dengan harga Basic 750rb
    with c1:
        st.markdown('<div class="package-box"><h3>BASIC</h3><b>Setup: 2.5jt</b><br>Monthly: 750rb<hr>Audit harian & Lap. PDF</div>', unsafe_allow_html=True)
        st.link_button("Pilih", wa_url)
    with c2:
        st.markdown('<div class="package-box"><h3>MEDIUM</h3><b>Setup: 7.5jt</b><br>Monthly: 1.5jt<hr>AI Detection & CCTV</div>', unsafe_allow_html=True)
        st.link_button("Pilih", wa_url)
    with c3:
        st.markdown('<div class="package-box"><h3>ENTERPRISE</h3><b>Setup: 25jt</b><br>Monthly: 5jt<hr>Multi-Branch & Auto-Invoice</div>', unsafe_allow_html=True)
        st.link_button("Pilih", wa_url)
    with c4:
        st.markdown('<div class="package-box"><h3>CORPORATE</h3><b>Setup: 50jt</b><br>Monthly: 10jt<hr>Custom Dev & Audit On-Site</div>', unsafe_allow_html=True)
        st.link_button("Pilih", wa_url)

# --- MENU 4: ADMIN (AI PENDUKUNG ADA DI SINI) ---
elif menu == "4. 🔐 Admin Dashboard":
    st.header("🔐 Intelligence Center")
    pwd = st.text_input("Password Admin:", type="password")
    if pwd == "admin123":
        st.success("Sistem AI Aktif & Terkoneksi.")
        st.metric("Aset Terproteksi", "Rp 6.2 Miliar")
        uploaded = st.file_uploader("Unggah Data untuk Audit AI", type=['csv', 'xlsx'])
        if uploaded:
            with st.status("AI Sedang Menganalisis..."):
                time.sleep(2)
            st.warning("Hasil Audit: Data Bersih dari Anomali.")
    elif pwd != "":
        st.error("Akses Ditolak.")

# 4. FOOTER PESANAN BAPAK
st.markdown("""
<div class="footer">
    © 2026 V-Guard AI Systems - Secured by Advanced Intelligence. Tangerang, Indonesia.
</div>
""", unsafe_allow_html=True)
