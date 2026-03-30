import streamlit as st
import os
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS CUSTOM UNTUK TAMPILAN PREMIUM & FOOTER
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 18px; }
    .package-box {
        height: 480px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        background-color: #ffffff;
        margin-bottom: 10px;
    }
    /* PERBAIKAN FOOTER: Menggunakan padding bawah pada body agar konten tidak tertutup */
    .stApp { margin-bottom: 100px; }
    
    .footer-fixed {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f8f9fa;
        color: #31333F;
        text-align: center;
        padding: 20px 0;
        font-weight: bold;
        border-top: 2px solid #dee2e6;
        z-index: 9999;
    }
    /* Style Tombol Manual (Pengganti link_button yang error) */
    .custom-button {
        display: inline-block;
        padding: 10px 20px;
        background-color: #ffffff;
        color: #31333F;
        text-align: center;
        text-decoration: none;
        border: 1px solid #d1d3d8;
        border-radius: 5px;
        width: 100%;
        font-weight: bold;
    }
    .custom-button:hover { background-color: #f0f2f6; border-color: #1976d2; }
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
    # Tombol Konsultasi (HTML version)
    st.markdown(f'<a href="{wa_url}" target="_blank" class="custom-button">📞 Konsultasi Langsung</a>', unsafe_allow_html=True)

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
        Bapak Erwin Sinaga adalah seorang profesional dan Pemimpin Bisnis Senior yang memiliki dedikasi tinggi selama lebih dari sepuluh tahun dalam dunia perbankan serta manajemen aset nasional. Melalui perjalanan karier yang panjang di sektor keuangan formal, beliau telah mengasah keahlian strategis dalam manajemen risiko kredit, pengawasan kepatuhan operasional (compliance), hingga perancangan sistem perlindungan aset korporasi skala besar. Filosofi kepemimpinan beliau berakar pada integritas mutlak dan transparansi data, di mana beliau percaya bahwa setiap celah fraud dapat ditutup dengan sinergi antara ketelitian manusia dan kecanggihan teknologi.<br><br>
        V-Guard AI lahir dari visi beliau untuk membawa standar keamanan audit perbankan yang sangat ketat ke dalam ekosistem bisnis UMKM dan perusahaan menengah. Beliau memandang bahwa Artificial Intelligence bukan sekadar alat otomatisasi, melainkan benteng pertahanan utama dalam menjaga keberlangsungan finansial klien. Dengan mengintegrasikan algoritma deteksi anomali secara real-time, Bapak Erwin berkomitmen untuk menciptakan lingkungan bisnis yang bersih dari kebocoran dana, memastikan setiap rupiah aset klien terlindungi secara holistik dan terukur di bawah pengawasan sistem yang cerdas dan jujur.
        </div>
        """, unsafe_allow_html=True)

# --- MENU 2: VISI, MISI, ROI & FAQ ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Strategi Proteksi & ROI")
    v, m = st.columns(2)
    with v: st.info("### 🎯 Visi\nMenjadi standar utama keamanan audit AI di Indonesia pada 2026.")
    with m: st.info("### 🚀 Misi\n1. Integrasi AI otomatis.\n2. Laporan real-time.\n3. Pengawasan aset 24/7.")
    st.write("---")
    st.subheader("📈 Kalkulator ROI")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=500000000, step=10000000)
    st.error(f"🚨 Estimasi Kebocoran: Rp {omzet*0.05:,.0f}")
    st.success(f"🛡️ Penyelamatan V-Guard: Rp {omzet*0.05*0.9:,.0f}")
    st.write("---")
    with st.expander("❓ FAQ"):
        st.write("**Apakah aman?** Ya, semua data dienkripsi dengan standar protokol perbankan.")

# --- MENU 3: PAKET LAYANAN ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Proteksi V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    packages = [
        ("BASIC", "2.5jt", "750rb", "Audit Harian & PDF"),
        ("MEDIUM", "7.5jt", "1.5jt", "AI & CCTV Detection"),
        ("ENTERPRISE", "25jt", "5jt", "Multi-Branch & Admin"),
        ("CORPORATE", "50jt", "10jt", "Custom Dev & On-Site")
    ]
    cols = [c1, c2, c3, c4]
    for i, col in enumerate(cols):
        name, setup, monthly, desc = packages[i]
        with col:
            st.markdown(f"""<div class="package-box"><h3>{name}</h3><b>Setup: {setup}</b><br>Monthly: {monthly}<hr>{desc}</div>""", unsafe_allow_html=True)
            st.markdown(f'<a href="{wa_url}" target="_blank" class="custom-button">Pilih {name}</a>', unsafe_allow_html=True)

# --- MENU 4: ADMIN ---
elif menu == "4. 🔐 Admin Dashboard":
    st.header("🔐 Intelligence Center")
    pwd = st.text_input("Password Admin:", type="password")
    if pwd == "admin123":
        st.success("Sistem AI Aktif.")
        st.metric("Total Aset Terproteksi", "Rp 6.2 Miliar")

# 4. FOOTER (DIPASTIKAN MUNCUL)
st.markdown("""
<div class="footer-fixed">
    © 2026 V-Guard AI Systems - Secured by Advanced Intelligence.
</div>
""", unsafe_allow_html=True)
