import streamlit as st
import os
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS CUSTOM TERBARU (DIPERBAIKI UNTUK FOOTER & PAKET)
st.markdown("""
<style>
    /* Status Hijau */
    .status-connected { color: #28a745; font-weight: bold; font-size: 18px; }
    
    /* Box Paket Layanan Sejajar */
    .package-box {
        height: 480px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        background-color: #ffffff;
        margin-bottom: 10px;
    }
    
    /* PERBAIKAN FOOTER AGAR PASTI MUNCUL */
    .footer-container {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f0f2f6; /* Warna abu muda agar kontras */
        color: #31333F;
        text-align: center;
        padding: 15px 0px;
        font-weight: bold;
        border-top: 2px solid #d1d3d8;
        z-index: 9999;
    }
    
    /* Memberi ruang di bawah agar konten tidak tertutup footer */
    .main-content {
        margin-bottom: 80px;
    }
    
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

# Membungkus konten utama agar tidak tertabrak footer
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# --- MENU 1: PROFIL & FILOSOFI ---
if menu == "1. 👤 Profil & Filosofi":
    st.header("👤 Strategic Leadership & Philosophy")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.subheader("Erwin Sinaga")
        st.markdown("""
        <div class="profile-text">
        Bapak Erwin Sinaga adalah seorang profesional dan Pemimpin Bisnis Senior dengan pengalaman lebih dari sepuluh tahun di perbankan dan manajemen aset. Beliau ahli dalam manajemen risiko, kepatuhan operasional, dan perlindungan aset korporasi. Filosofinya berakar pada integritas dan transparansi, percaya bahwa teknologi AI adalah benteng utama melawan fraud.<br><br>
        V-Guard AI lahir dari visi beliau untuk membawa standar audit bank yang ketat ke UMKM dan perusahaan menengah. Beliau berkomitmen menciptakan lingkungan bisnis yang bersih dari kebocoran dana melalui sistem cerdas yang memantau aset secara holistik dan terukur, memastikan setiap rupiah klien terlindungi.
        </div>
        """, unsafe_allow_html=True)

# --- MENU 2: VISI, MISI, ROI & FAQ ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Strategi Proteksi & ROI")
    v, m = st.columns(2)
    with v: st.info("### 🎯 Visi\nMenjadi standar utama keamanan audit AI di Indonesia pada 2026.")
    with m: st.info("### 🚀 Misi\nIntegrasi AI otomatis, laporan real-time, dan pengawasan aset 24/7.")
    st.write("---")
    st.subheader("📈 Kalkulator ROI")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=500000000)
    st.error(f"🚨 Estimasi Kebocoran: Rp {omzet*0.05:,.0f}")
    st.success(f"🛡️ Penyelamatan V-Guard: Rp {omzet*0.05*0.9:,.0f}")
    st.write("---")
    with st.expander("❓ FAQ"):
        st.write("**Aman?** Ya, data dienkripsi standar perbankan.")

# --- MENU 3: PAKET LAYANAN ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Proteksi V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="package-box"><h3>BASIC</h3><b>Setup: 2.5jt</b><br>Monthly: 750rb<hr>Audit Harian & PDF</div>', unsafe_allow_html=True)
        st.link_button("Pilih", wa_url, key="b1")
    with c2:
        st.markdown('<div class="package-box"><h3>MEDIUM</h3><b>Setup: 7.5jt</b><br>Monthly: 1.5jt<hr>AI & CCTV Integration</div>', unsafe_allow_html=True)
        st.link_button("Pilih", wa_url, key="b2")
    with c3:
        st.markdown('<div class="package-box"><h3>ENTERPRISE</h3><b>Setup: 25jt</b><br>Monthly: 5jt<hr>Multi-Branch & Auto-Invoice</div>', unsafe_allow_html=True)
        st.link_button("Pilih", wa_url, key="b3")
    with c4:
        st.markdown('<div class="package-box"><h3>CORPORATE</h3><b>Setup: 50jt</b><br>Monthly: 10jt<hr>Custom AI & Priority Support</div>', unsafe_allow_html=True)
        st.link_button("Pilih", wa_url, key="b4")

# --- MENU 4: ADMIN ---
elif menu == "4. 🔐 Admin Dashboard":
    st.header("🔐 Intelligence Center")
    pwd = st.text_input("Password Admin:", type="password")
    if pwd == "admin123":
        st.success("Sistem AI Aktif.")
        st.metric("Total Aset Terproteksi", "Rp 6.2 Miliar")

st.markdown('</div>', unsafe_allow_html=True)

# 4. FOOTER (MENGGUNAKAN DIV CONTAINER AGAR TIDAK HILANG)
st.markdown("""
<div class="footer-container">
    © 2026 V-Guard AI Systems - Secured by Advanced Intelligence.
</div>
""", unsafe_allow_html=True)
