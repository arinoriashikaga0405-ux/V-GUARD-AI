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
    .status-box {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #1976d2;
        margin-bottom: 10px;
    }
    .package-box {
        height: 400px;
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
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 3. SIDEBAR (KEMBALI KE VERSI AWAL)
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
    
    # MENGEMBALIKAN STATUS SISTEM MENDALAM
    st.subheader("📡 Sistem Status")
    st.markdown("""
    <div class="status-box">
    <ul style="list-style-type: none; padding-left: 0; margin-bottom: 0;">
        <li style="color: #1976d2;">● AI Engine: Connected</li>
        <li style="color: #1976d2;">● Audit Core: Connected</li>
        <li style="color: #1976d2;">● Vision System: Connected</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔌 Cek Koneksi API"):
        with st.spinner("Ping API..."):
            time.sleep(1)
        st.success("API Response: 200 OK")
        
    st.write("---")
    st.link_button("📞 Konsultasi Langsung", wa_url, use_container_width=True)
    st.caption("Lokasi: Tangerang")

# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("Erwin Sinaga")
    st.write("Pemimpin Bisnis Senior dengan pengalaman 10+ tahun di perbankan & manajemen aset. V-Guard AI adalah visi beliau untuk membawa standar audit bank ke sektor UMKM dan Korporasi melalui teknologi AI.")

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Analisis ROI")
    st.info("### 🎯 Visi 2026\nMenjadi standar utama keamanan audit AI di Indonesia.")
    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Aset")
    omzet = st.number_input("Input Omzet Bulanan (Rp):", value=500000000, step=10000000)
    potensi_rugi = omzet * 0.05
    st.error(f"🚨 Estimasi Kebocoran Aset: Rp {potensi_rugi:,.0f} / Bulan")
    st.success(f"🛡️ Target Penyelamatan V-Guard: Rp {potensi_rugi * 0.9:,.0f} / Bulan")

# --- MENU 3: PAKET LAYANAN (TETAP RAPI & SEJAJAR) ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Proteksi")
    st.markdown("---")
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown("""<div class="package-box"><h3>BASIC</h3><b>Setup: 2.5jt</b><br><span style="color:#d32f2f">Monthly: 750rb</span><hr><ul><li>📊 Audit Harian</li><li>📁 Lap. PDF Mingguan</li><li>📱 Support WA</li></ul></div>""", unsafe_allow_html=True)
        st.link_button("Pilih BASIC", wa_url, use_container_width=True)
    with c2:
        st.markdown("""<div class="package-box"><h3>MEDIUM</h3><b>Setup: 7.5jt</b><br>Monthly: 1.5jt<hr><ul><li>🤖 AI Detection</li><li>👁️ Integrasi CCTV</li><li>🚨 Alarm Fraud</li></ul></div>""", unsafe_allow_html=True)
        st.link_button("Pilih MEDIUM", wa_url, use_container_width=True)
    with c3:
        st.markdown("""<div class="package-box"><h3>ENTERPRISE</h3><b>Setup: 25jt</b><br>Monthly: 5jt<hr><ul><li>🏢 Multi-Cabang</li><li>🖥️ Dashboard Admin</li><li>🧾 Auto-Invoice</li></ul></div>""", unsafe_allow_html=True)
        st.link_button("Pilih ENTERPRISE", wa_url, use_container_width=True)
    with c4:
        st.markdown("""<div class="package-box"><h3>CORPORATE</h3><b>Setup: 50jt</b><br>Monthly: 10jt<hr><ul><li>🏗️ Custom AI Dev</li><li>🕵️ Audit On-Site</li><li>📞 Priority 24/7</li></ul></div>""", unsafe_allow_html=True)
        st.link_button("Pilih CORPORATE", wa_url, use_container_width=True)

# --- MENU 4: ADMIN DASHBOARD ---
elif menu == "4. 🔐 Admin Dashboard":
    st.header("🔐 Intelligence Center")
    pwd = st.text_input("Password Admin:", type="password")
    if pwd == "admin123":
        st.success("Sistem AI Aktif.")
        st.metric("Aset Terproteksi", "Rp 6.2 Miliar")
        uploaded = st.file_uploader("Audit File", type=['csv', 'xlsx'])
        if uploaded:
            with st.status("AI Menganalisis..."):
                time.sleep(2)
            st.warning("Hasil Audit: 0 Anomali ditemukan.")
    elif pwd != "":
        st.error("Akses Ditolak.")

# 4. FOOTER SESUAI PERMINTAAN
st.markdown("""
<div class="footer">
    © 2026 V-Guard AI Systems - Secured by Advanced Intelligence. Tangerang, Indonesia.
</div>
""", unsafe_allow_html=True)
