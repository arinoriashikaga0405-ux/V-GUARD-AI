import streamlit as st
import os
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS CUSTOM UNTUK TAMPILAN PREMIUM & SEJAJAR
st.markdown("""
<style>
    .alarm-banner {
        background-color: #ff4b4b; color: white; padding: 15px;
        border-radius: 10px; text-align: center; font-weight: bold;
        border: 2px solid white; animation: blinker 1s linear infinite;
        margin-bottom: 20px;
    }
    @keyframes blinker { 50% { opacity: 0.2; } }
    .invoice-box {
        background: #e3f2fd; border-left: 8px solid #1976d2;
        padding: 20px; border-radius: 10px; margin-top: 15px;
    }
    .founder-text {
        font-size: 16px; line-height: 1.8; text-align: justify;
    }
    .status-connected {
        color: #28a745; font-weight: bold; font-size: 18px;
    }
    .package-box {
        height: 420px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        background-color: #ffffff;
        margin-bottom: 10px;
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
        st.markdown("""
        <div class="founder-text">
        Bapak Erwin Sinaga merupakan seorang profesional dan Pemimpin Bisnis Senior yang memiliki rekam jejak prestisius selama lebih dari sepuluh tahun di industri perbankan serta manajemen aset nasional. Melalui dedikasi panjang di sektor keuangan formal, beliau telah menguasai secara mendalam berbagai aspek krusial seperti manajemen risiko kredit, pengawasan kepatuhan operasional (compliance), hingga perancangan strategi perlindungan aset korporasi dalam skala besar. <br><br>
        Pemahaman komprehensif beliau terhadap celah-celah fraud dan dinamika kebocoran dana yang sering terjadi pada sistem keuangan konvensional menjadi batu pijakan utama dalam mendirikan ekosistem V-Guard AI. Di bawah kepemimpinan strategisnya, Bapak Erwin berhasil mengintegrasikan standar audit perbankan yang sangat ketat dengan kecanggihan teknologi Artificial Intelligence modern. Sinergi teknologi ini dirancang khusus untuk memberikan perlindungan finansial yang holistik, transparan, dan mampu mencegah segala bentuk anomali transaksi bisnis klien secara mutlak dan real-time.
        </div>
        """, unsafe_allow_html=True)

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Strategi & Analisis Risiko")
    v, m = st.columns(2)
    with v:
        st.info("### 🎯 Visi\nMenjadi pemimpin pasar dalam solusi keamanan audit berbasis AI di Indonesia pada tahun 2026.")
    with m:
        st.info("### 🚀 Misi\n1. Integrasi AI untuk deteksi fraud otomatis.\n2. Laporan audit transparan & real-time.\n3. Otomasi pengawasan aset 24/7.")
    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Aset (ROI)")
    omzet = st.number_input("Input Omzet Bulanan Klien (Rp):", value=500000000, step=10000000)
    potensi_rugi = omzet * 0.05
    st.error(f"🚨 Estimasi Kebocoran Aset Tanpa V-Guard: Rp {potensi_rugi:,.0f} / Bulan")
    st.success(f"🛡️ Target Penyelamatan Aset (90%): Rp {potensi_rugi * 0.9:,.0f} / Bulan")

# --- MENU 3: PAKET LAYANAN ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Proteksi V-Guard AI")
    st.markdown("---")
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown("""<div class="package-box">
        <h3 style="color:#1976d2">BASIC</h3>
        <b>Setup: Rp 2.5 Juta</b><br>
        <span style="color:#d32f2f">Monthly: Rp 750rb</span><hr>
        <b>Fitur:</b><ul>
        <li>📊 Audit Harian</li>
        <li>📁 Lap. PDF Mingguan</li>
        <li>📱 Support WA</li>
        <li>🔍 Cek Kasir Manual</li></ul></div>""", unsafe_allow_html=True)
        st.link_button("Pilih BASIC", wa_url, use_container_width=True)

    with c2:
        st.markdown("""<div class="package-box">
        <h3 style="color:#1976d2">MEDIUM</h3>
        <b>Setup: Rp 7.5 Juta</b><br>
        Monthly: Rp 1.5jt<hr>
        <b>Fitur BASIC +</b><ul>
        <li>🤖 <b>AI Detection</b></li>
        <li>👁️ Integrasi CCTV</li>
        <li>🚨 Alarm Fraud</li>
        <li>📉 Analisis Tren</li></ul></div>""", unsafe_allow_html=True)
        st.link_button("Pilih MEDIUM", wa_url, use_container_width=True)

    with c3:
        st.markdown("""<div class="package-box">
        <h3 style="color:#1976d2">ENTERPRISE</h3>
        <b>Setup: Rp 25 Juta</b><br>
        Monthly: Rp 5jt<hr>
        <b>Fitur MEDIUM +</b><ul>
        <li>🏢 Multi-Cabang</li>
        <li>🖥️ Dashboard Khusus</li>
        <li>🧾 <b>Auto-Invoice</b></li>
        <li>🛡️ Proteksi Aset</li></ul></div>""", unsafe_allow_html=True)
        st.link_button("Pilih ENTERPRISE", wa_url, use_container_width=True)

    with c4:
        st.markdown("""<div class="package-box">
        <h3 style="color:#1976d2">CORPORATE</h3>
        <b>Setup: Rp 50 Juta</b><br>
        Monthly: Rp 10jt<hr>
        <b>Fitur ENTERPRISE +</b><ul>
        <li>🏗️ <b>Custom AI Dev</b></li>
        <li>🕵️ Audit On-Site</li>
        <li>📑 Laporan Pajak</li>
        <li>📞 Priority 24/7</li></ul></div>""", unsafe_allow_html=True)
        st.link_button("Pilih CORPORATE", wa_url, use_container_width=True)

# --- MENU 4: ADMIN DASHBOARD ---
elif menu == "4. 🔐 Admin Dashboard":
    st.header("🔐 Intelligence Center")
    pwd = st.text_input("Masukkan Password Admin:", type="password")
    if pwd == "admin123":
        st.success("Akses Diterima.")
        m1, m2, m3 = st.columns(3)
        m1.metric("Klien Aktif", "12 Cabang")
        m2.metric("Omzet Terpantau", "Rp 6.2 Miliar")
        m3.metric("Aset Diselamatkan", "Rp 310 Juta")
        st.write("---")
        uploaded = st.file_uploader("Unggah Laporan Transaksi untuk Audit AI", type=['csv', 'xlsx'])
        if uploaded:
            with st.status("V-Guard AI memproses data...", expanded=True) as status:
                st.write("🤖 Menganalisis integritas data...")
                time.sleep(2)
                status.update(label="Audit Selesai!", state="complete")
            st.markdown('<div class="alarm-banner">🚨 FRAUD DETECTED: Anomali ditemukan!</div>', unsafe_allow_html=True)
            st.download_button("📥 Unduh Laporan PDF", "Data Audit V-Guard", file_name="Audit_VGuard.pdf", use_container_width=True)
    elif pwd != "":
        st.error("Password Salah!")
