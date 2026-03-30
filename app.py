import streamlit as st
import os
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS CUSTOM UNTUK TAMPILAN PREMIUM
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
        height: 420px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        background-color: #ffffff;
        margin-bottom: 10px;
    }
    .footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: #f8f9fa; color: #6c757d; text-align: center;
        padding: 10px; font-size: 13px; border-top: 1px solid #dee2e6;
        z-index: 999;
    }
    .profile-text { text-align: justify; line-height: 1.8; }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 3. SIDEBAR (STATUS SEDERHANA, TANPA CEK API)
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

# --- MENU 1: PROFIL & FILOSOFI (MINIMAL 100 KATA) ---
if menu == "1. 👤 Profil & Filosofi":
    st.header("👤 Strategic Leadership & Philosophy")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.subheader("Erwin Sinaga")
        st.markdown("""
        <div class="profile-text">
        Bapak Erwin Sinaga adalah seorang profesional dan Pemimpin Bisnis Senior yang memiliki dedikasi tinggi selama lebih dari sepuluh tahun dalam dunia perbankan serta manajemen aset nasional. Melalui perjalanan karier yang panjang di sektor keuangan formal, beliau telah mengasah keahlian strategis dalam manajemen risiko kredit, pengawasan kepatuhan operasional (compliance), hingga perancangan sistem perlindungan aset korporasi skala besar. Filosofi kepemimpinan beliau berakar pada integritas mutlak dan transparansi data, di mana beliau percaya bahwa setiap celah fraud dapat ditutup dengan sinergi antara ketelitian manusia dan kecanggihan teknologi.<br><br>
        V-Guard AI lahir dari visi beliau untuk membawa standar keamanan audit perbankan yang sangat ketat ke dalam ekosistem bisnis UMKM dan perusahaan menengah. Beliau memandang bahwa Artificial Intelligence bukan sekadar alat otomatisasi, melainkan benteng pertahanan utama dalam menjaga keberlangsungan finansial klien. Dengan mengintegrasikan algoritma deteksi anomali secara real-time, Bapak Erwin berkomitmen untuk menciptakan lingkungan bisnis yang bersih dari kebocoran dana, memastikan setiap rupiah aset klien terlindungi secara holistik dan terukur di bawah pengawasan sistem yang cerdas dan jujur.
        </div>
        """, unsafe_allow_html=True)

# --- MENU 2: VISI, MISI, ROI & FAQ ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Strategi Proteksi & ROI")
    v, m = st.columns(2)
    with v:
        st.info("### 🎯 Visi\nMenjadi pemimpin pasar dalam solusi keamanan audit berbasis AI di Indonesia pada tahun 2026.")
    with m:
        st.info("### 🚀 Misi\n1. Integrasi AI untuk deteksi fraud otomatis.\n2. Laporan audit transparan & real-time.\n3. Otomasi pengawasan aset 24/7.")
    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Aset (ROI)")
    omzet = st.number_input("Input Omzet Bulanan (Rp):", value=500000000, step=10000000)
    potensi_rugi = omzet * 0.05
    st.error(f"🚨 Estimasi Kebocoran Aset Tanpa V-Guard: Rp {potensi_rugi:,.0f} / Bulan")
    st.success(f"🛡️ Target Penyelamatan Aset (90%): Rp {potensi_rugi * 0.9:,.0f} / Bulan")
    
    st.write("---")
    with st.expander("❓ FAQ - Pertanyaan Umum"):
        st.write("**Bagaimana V-Guard AI mendeteksi kecurangan?** Sistem kami menggunakan algoritma khusus untuk memindai pola transaksi yang tidak wajar secara otomatis.")
        st.write("**Apakah data bisnis saya aman?** Keamanan data adalah prioritas kami. Semua data dienkripsi dengan standar protokol perbankan.")
        st.write("**Apakah sistem ini bisa dipantau dari HP?** Ya, laporan dikirim secara real-time melalui Dashboard atau notifikasi WhatsApp.")

# --- MENU 3: PAKET LAYANAN ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Proteksi V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""<div class="package-box"><h3>BASIC</h3><b>Setup: 2.5jt</b><br><span style="color:#d32f2f">Monthly: 750rb</span><hr><ul><li>📊 Audit Harian</li><li>📁 Lap. PDF Mingguan</li><li>📱 Support WA</li></ul></div>""", unsafe_allow_html=True)
        st.link_
