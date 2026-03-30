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
        height: 520px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        background-color: #ffffff;
        margin-bottom: 10px;
    }
    .footer-container {
        position: fixed;
        left: 0; bottom: 0; width: 100%;
        background-color: #f8f9fa; color: #31333F;
        text-align: center; padding: 15px 0px;
        font-weight: bold; border-top: 1px solid #dee2e6;
        z-index: 9999;
    }
    .stApp { margin-bottom: 100px; }
    .profile-text { text-align: justify; line-height: 1.6; }
</style>
""", unsafe_allow_html=True)

# Nomor WA diperbarui sesuai permintaan
wa_url = "https://wa.me/628212190885"

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

# --- MENU 1: PROFIL & FILOSOFI (RINGKAS < 100 KATA) ---
if menu == "1. 👤 Profil & Filosofi":
    st.header("👤 Strategic Leadership")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.subheader("Erwin Sinaga")
        st.markdown("""
        <div class="profile-text">
        Bapak Erwin Sinaga adalah Pemimpin Bisnis Senior dengan pengalaman 10+ tahun di sektor perbankan dan manajemen aset. 
        Keahliannya fokus pada manajemen risiko dan kepatuhan operasional. <br><br>
        <b>Filosofi:</b> Beliau memegang teguh prinsip integritas dan transparansi. 
        Melalui V-Guard AI, beliau berkomitmen melindungi aset pelaku usaha dari risiko fraud menggunakan 
        teknologi audit cerdas yang presisi dan real-time.
        </div>
        """, unsafe_allow_html=True)

# --- MENU 2: VISI, MISI & ROI (ROI DI BAWAH MISI) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Analisis Strategi")
    st.info("### 🎯 Visi\nMenjadi standar utama keamanan audit AI di Indonesia pada tahun 2026.")
    
    st.subheader("🚀 Misi Utama")
    st.markdown("""
    * **Otomasi**: Sistem audit AI yang bekerja non-stop 24/7.
    * **Transparansi**: Laporan akurat untuk mencegah manipulasi data.
    * **Akurasi**: Deteksi instan terhadap setiap anomali transaksi.
    """)
    
    st.write("---")
    
    # ROI dikembalikan dan diletakkan di bawah Misi
    st.subheader("📈 Kalkulator Penyelamatan Aset (ROI)")
    omzet = st.number_input("Input Omzet Bulanan Bisnis (Rp):", value=500000000, step=10000000)
    potensi_rugi = omzet * 0.05
    st.error(f"🚨 Estimasi Kebocoran Aset (5%): Rp {potensi_rugi:,.0f} / Bulan")
    st.success(f"🛡️ Target Penyelamatan V-Guard (90%): Rp {potensi_rugi * 0.9:,.0f} / Bulan")

# --- MENU 3: PAKET LAYANAN (LENGKAP 4 PAKET) ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Proteksi V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown("""<div class="package-box"><h3>BASIC</h3><b>Setup: 2.5jt</b><br>Monthly: 750rb<hr>
        <b>Manfaat:</b><ul><li>📊 Audit Harian</li><li>📁 Laporan Mingguan</li><li>📱 Support WA</li></ul></div>""", unsafe_allow_html=True)
        st.link_button("Pilih BASIC", wa_url, use_container_width=True)
    with c2:
        st.markdown("""<div class="package-box"><h3>MEDIUM</h3><b>Setup: 7.5jt</b><br>Monthly: 1.5jt<hr>
        <b>Manfaat:</b><ul><li>🤖 AI CCTV Integration</li><li>📈 Analisis Tren Fraud</li><li>🚨 Alert System</li></ul></div>""", unsafe_allow_html=True)
        st.link_button("Pilih MEDIUM", wa_url, use_container_width=True)
    with c3:
        st.markdown("""<div class="package-box"><h3>ENTERPRISE</h3><b>Setup: 25jt</b><br>Monthly: 5jt<hr>
        <b>Manfaat:</b><ul><li>🏢 Multi-Branch System</li><li>🖥️ Dashboard Admin</li><li>🧾 Auto-Invoice</li></ul></div>""", unsafe_allow_html=True)
        st.link_button("Pilih ENTERPRISE", wa_url, use_container_width=True)
    with c4:
        st.markdown("""<div class="package-box"><h3>CORPORATE</h3><b>Setup: 50jt</b><br>Monthly: 10jt<hr>
        <b>Manfaat:</b><ul><li>🏗️ Custom AI Dev</li><li>🕵️ Audit On-Site</li><li>📞 Priority 24/7</li></ul></div>""", unsafe_allow_html=True)
        st.link_button("Pilih CORPORATE", wa_url, use_container_width=True)

# --- MENU 4: ADMIN DASHBOARD (KEMBALI) ---
elif menu == "4. 🔐 Admin Dashboard":
    st.header("🔐 Intelligence Center")
    pwd = st.text_input("Password Admin:", type="password")
    if pwd == "w1nbju8282": 
        st.success("Sistem AI Aktif. Selamat Datang, Pak Erwin.")
        st.metric("Total Aset Terproteksi", "Rp 6.2 Miliar")
        st.write("---")
        st.file_uploader("Unggah File Log Transaksi untuk Audit AI", type=['csv', 'xlsx'])
    elif pwd != "":
        st.error("Akses Ditolak. Password Salah.")

# 4. FOOTER (DITAMPILKAN @2026)
st.markdown("""<div class="footer-container">© 2026 V-Guard AI Systems - Secured by Advanced Intelligence.</div>""", unsafe_allow_html=True)
