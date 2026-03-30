import streamlit as st
import os
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS CUSTOM PREMIUM
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
    .footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: white; color: #757575; text-align: center;
        padding: 10px; font-size: 12px; border-top: 1px solid #eee;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 3. SIDEBAR NAVIGASI
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.write("---")
    menu = st.radio("Folder Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Layanan", 
        "4. 🔐 Admin Dashboard"
    ])
    st.write("---")
    st.subheader("📡 Sistem Status")
    st.markdown('<p class="status-connected">● Connected</p>', unsafe_allow_html=True)
    st.write("---")
    # TAMBAHAN: TOMBOL KONSULTASI CEPAT
    st.link_button("📞 Konsultasi Langsung", wa_url, use_container_width=True)
    st.caption("Lokasi: Tangerang")

# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("👤 Strategic Leadership")
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col_txt:
        st.subheader("Erwin Sinaga")
        st.write("Bapak Erwin Sinaga merupakan seorang profesional dan Pemimpin Bisnis Senior dengan rekam jejak prestisius selama lebih dari sepuluh tahun di industri perbankan serta manajemen aset nasional. Beliau menguasai manajemen risiko kredit, kepatuhan operasional, hingga strategi perlindungan aset korporasi.")
        st.write("Di bawah kepemimpinan beliau, V-Guard AI mengintegrasikan standar audit perbankan yang ketat dengan kecanggihan teknologi Artificial Intelligence untuk memberikan perlindungan finansial yang holistik dan transparan.")

# --- MENU 2: VISI, MISI & ROI + FAQ ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Strategi & Analisis Risiko")
    v, m = st.columns(2)
    with v:
        st.info("### 🎯 Visi\nMenjadi pemimpin pasar solusi keamanan audit berbasis AI di Indonesia pada tahun 2026.")
    with m:
        st.info("### 🚀 Misi\n1. Integrasi AI otomatis.\n2. Laporan transparan.\n3. Pengawasan aset 24/7.")
    
    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Aset (ROI)")
    omzet = st.number_input("Input Omzet Bulanan Klien (Rp):", value=500000000, step=10000000)
    potensi_rugi = omzet * 0.05
    st.error(f"🚨 Estimasi Kebocoran Aset: Rp {potensi_rugi:,.0f} / Bulan")
    st.success(f"🛡️ Target Penyelamatan V-Guard: Rp {potensi_rugi * 0.9:,.0f} / Bulan")
    
    # TAMBAHAN: FAQ SINGKAT
    with st.expander("❓ FAQ - Pertanyaan Umum"):
        st.write("**Bagaimana AI bekerja?** AI kami memindai anomali data transaksi dan visual CCTV secara real-time.")
        st.write("**Apakah aman?** Data dienkripsi dengan standar keamanan perbankan tinggi.")

# --- MENU 3: PAKET LAYANAN ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Proteksi V-Guard AI")
    st.markdown("---")
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown("""<div class="package-box"><h3>BASIC</h3><b>Setup: Rp 2.5 Juta</b><br><span style="color:#d32f2f">Monthly: Rp 750rb</span><hr><ul><li>📊 Audit Harian</li><li>📁 Lap. PDF</li><li>📱 Support WA</li><li>🔍 Cek Manual</li></ul></div>""", unsafe_allow_html=True)
        st.link_button("Pilih BASIC", wa_url, use_container_width=True)
    with c2:
        st.markdown("""<div class="package-box"><h3>MEDIUM</h3><b>Setup: Rp 7.5 Juta</b><br>Monthly: Rp 1.5jt<hr><b>BASIC +</b><ul><li>🤖 AI Detection</li><li>👁️ Integrasi CCTV</li><li>🚨 Alarm Fraud</li><li>📉 Analisis Tren</li></ul></div>""", unsafe_allow_html=True)
        st.link_button("Pilih MEDIUM", wa_url, use_container_width=True)
    with c3:
        st.markdown("""<div class="package-box"><h3>ENTERPRISE</h3><b>Setup: Rp 25 Juta</b><br>Monthly: Rp 5jt<hr><b>MEDIUM +</b><ul><li>🏢 Multi-Cabang</li><li>🖥️ Dashboard Admin</li><li>🧾 Auto-Invoice</li><li>🛡️ Proteksi Aset</li></ul></div>""", unsafe_allow_html=True)
        st.link_button("Pilih ENTERPRISE", wa_url, use_container_width=True)
    with c4:
        st.markdown("""<div class="package-box"><h3>CORPORATE</h3><b>Setup: Rp 50 Juta</b><br>Monthly: Rp 10jt<hr><b>ENTERPRISE +</b><ul><li>🏗️ Custom AI Dev</li><li>🕵️ Audit On-Site</li><li>📑 Laporan Pajak</li><li>📞 Priority 24/7</li></ul></div>""", unsafe_allow_html=True)
        st.link_button("Pilih CORPORATE", wa_url, use_container_width=True)

# --- MENU 4: ADMIN DASHBOARD ---
elif menu == "4. 🔐 Admin Dashboard":
    st.header("🔐 Intelligence Center")
    pwd = st.text_input("Password:", type="password")
    if pwd == "admin123":
        st.success("Akses Diterima.")
        m1, m2, m3 = st.columns(3)
        m1.metric("Klien Aktif", "12 Cabang")
        m2.metric("Omzet", "Rp 6.2 Miliar")
        m3.metric("Diselamatkan", "Rp 310 Juta")
