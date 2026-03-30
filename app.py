import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. SETUP & STYLE
st.set_page_config(page_title="V-Guard AI Systems", layout="wide")
st.markdown("""<style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #f8f9fa; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 9999; }
    .package-box { padding: 20px; border: 1px solid #eee; border-radius: 10px; background: #fff; height: 620px; }
    .profile-text { text-align: justify; line-height: 1.8; font-size: 16px; }
</style>""", unsafe_allow_html=True)

# 2. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.warning("Foto 'erwin.jpg' tidak ditemukan. Pastikan file foto ada di folder yang sama.")
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Folder:", ["1. 👤 Profil Founder", "2. 🎯 Visi & Misi", "3. 📦 Paket", "4. 📝 Registrasi", "5. 🔐 Admin"])
    st.write("---")
    st.link_button("📞 Layanan Pelanggan (WA)", "https://wa.me/628212190885")

# 3. FOLDER 1: PROFIL FOUNDER (MINIMAL 100 KATA)
if menu == "1. 👤 Profil Founder":
    st.header("👤 Profil Founder: Erwin Sinaga")
    st.markdown("""<div class="profile-text">
    Bapak Erwin Sinaga adalah seorang Pemimpin Bisnis Senior yang memiliki rekam jejak impresif selama lebih dari sepuluh tahun di industri perbankan dan manajemen aset nasional. Sepanjang kariernya, beliau telah menguasai berbagai aspek strategis mulai dari manajemen risiko, kepatuhan operasional, hingga pengawasan aset korporasi skala besar. Pengalaman mendalam ini memberikan beliau perspektif unik mengenai betapa rentannya operasional bisnis terhadap celah kecurangan atau fraud yang sering kali tidak terdeteksi oleh sistem konvensional. <br><br>
    V-Guard AI lahir dari visi besar Bapak Erwin Sinaga untuk mendemokrasikan standar keamanan audit perbankan yang ketat agar dapat diimplementasikan oleh pelaku UMKM dan perusahaan menengah di Indonesia. Beliau meyakini bahwa teknologi Artificial Intelligence adalah kunci utama untuk menciptakan ekosistem bisnis yang transparan dan bebas dari kebocoran finansial. Melalui V-Guard AI, beliau berkomitmen untuk menyediakan benteng pertahanan digital yang bekerja secara nonstop selama 24 jam, memastikan setiap rupiah aset klien terlindungi dengan presisi tinggi dan teknologi audit yang cerdas serta adaptif.
    </div>""", unsafe_allow_html=True)

# 4. FOLDER 2: VISI, MISI & ROI (TIDAK BERUBAH)
elif menu == "2. 🎯 Visi & Misi":
    st.info("### 🎯 Visi 2026\nMenjadi standar utama keamanan audit berbasis AI di Indonesia.")
    st.success("### 🚀 Misi Utama\n1. Otomasi Audit 24/7\n2. Deteksi Fraud Instan\n3. Transparansi Aset\n4. Efisiensi Teknologi AI")
    st.write("---")
    st.subheader("📈 Kalkulator ROI (Penyelamatan Aset)")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=500000000)
    st.error(f"🚨 Estimasi Kebocoran (5%): Rp {omzet * 0.05:,.0f}")
    st.success(f"🛡️ Target Penyelamatan V-Guard: Rp {omzet * 0.05 * 0.9:,.0f}")

# 5. FOLDER 3: PAKET LAYANAN (DENGAN FITUR ALARM FRAUD BERTINGKAT)
elif menu == "3. 📦 Paket":
    st.header("📦 Paket Layanan V-Guard AI")
    cols = st.columns(4)
    # Fitur bertingkat: Semakin mahal, semakin banyak fitur
    pkgs = [
        ("BASIC", "2.5jt", "750rb", ["Audit Transaksi Harian", "Laporan Mingguan", "Standard Fraud Alarm (Email)"]),
        ("MEDIUM", "7.5jt", "1.5jt", ["Semua Fitur BASIC", "Integrasi AI CCTV", "Fraud Alarm Instan (WA)", "Analisa Tren Bulanan"]),
        ("ENTERPRISE", "25jt", "5jt", ["Semua Fitur MEDIUM", "Multi-Branch Support", "Advanced AI Fraud Alarm", "Dedicated Cloud Server"]),
        ("CORPORATE", "50jt", "10jt", ["Semua Fitur ENTERPRISE", "Custom AI Model", "Real-time Sirene Fraud Alarm", "Audit On-site Bulanan", "Priority 24/7 Support"])
    ]
    for i, (n, s, m, f) in enumerate(pkgs):
        with cols[i]:
            st.markdown(f"""<div class='package-box'>
                <h3 style='text-align:center;'>{n}</h3>
                <p><b>Setup:</b> {s}<br><b>Bulanan:</b> {m}</p><hr>
                <ul>{"".join([f"<li>{item}</li>" for item in f])}</ul>
            </div>""", unsafe_allow_html=True)

# 6. FOLDER 4: REGISTRASI (TIDAK BERUBAH)
elif menu == "4. 📝 Registrasi":
    st.header("📝 Registrasi Nasabah Baru")
    with st.form("reg"):
        st.text_input("Nama Bisnis:")
        st.selectbox("Jenis Usaha:", ["Retail", "F&B", "Jasa", "Corporate"])
        st.text_input("Harga (Sesuai Paket):")
        st.selectbox("Pilih Paket:", ["BASIC
