import streamlit as st
import os
import pandas as pd
import numpy as np
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"Waktu": "2026-03-31", "Nama Pelanggan": "Budi Santoso", "Bisnis": "Toko Berkah", "Paket": "BASIC", "Harga": "2.500.000", "Status": "🟢 AKTIF"}
    ]

# 2. CSS CUSTOM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; margin-top: 5px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; font-size: 16px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 8px rgba(0,0,0,0.02); }
    .vision-box { background: #fdfdfd; padding: 25px; border-left: 5px solid #007bff; border-radius: 10px; margin-bottom: 25px; }
    .security-info { color: #666; font-size: 12px; font-weight: bold; margin-top: 10px; text-align: center; border: 1px dashed #ccc; padding: 5px; border-radius: 5px; }
    .package-card { background: white; padding: 20px; border-radius: 12px; border: 1px solid #eee; height: 450px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● System Online</p>', unsafe_allow_html=True)
    
    menu = st.radio("Navigasi Utama:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 📦 Paket Layanan", "4. 📝 Registrasi & Invoice", "5. 🔐 Admin & Audit AI"])
    st.write("---")
    
    # Customer Service & Security Info
    st.markdown("### Support Center")
    st.link_button("💬 Chat Customer Service", "https://wa.me/628212190885")
    st.markdown('<div class="security-info">🔐 End-to-End Encrypted System</div>', unsafe_allow_html=True)

# --- FOLDER 1: PROFIL FOUNDER (MINIMAL 100 KATA) ---
if menu == "1. 👤 Profil Founder":
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col2:
        profil_html = """
        <div class="profile-box">
        <b>Bapak Erwin Sinaga</b> merupakan seorang Pemimpin Bisnis Senior (Senior Business Leader) yang telah memiliki pengalaman profesional lebih dari sepuluh tahun di industri perbankan dan manajemen aset nasional. Sepanjang perjalanan kariernya, beliau telah menduduki berbagai posisi strategis, mulai dari Chief Executive Officer (CEO) hingga Chief Sales Officer (CSO), di mana fokus utamanya adalah pada manajemen risiko operasional dan pengawasan aset korporasi dalam skala besar. Pengalaman luas ini memberikan beliau pemahaman mendalam mengenai titik-titik kritis di mana inefisiensi dan potensi kecurangan (fraud) sering terjadi dalam sistem bisnis konvensional. <br><br>
        Melalui V-Guard AI, Bapak Erwin Sinaga berkomitmen untuk menghadirkan teknologi pengawasan berbasis Artificial Intelligence yang mampu bekerja secara mandiri selama 24 jam penuh tanpa henti. Visi beliau adalah mendemokratisasi standar keamanan tingkat tinggi yang biasanya hanya dimiliki oleh bank besar, agar kini dapat dinikmati oleh pemilik bisnis UMKM dan perusahaan menengah di seluruh Indonesia. <br><br>
        Di bawah kepemimpinan strategis beliau, V-Guard AI tidak hanya menawarkan sekadar alat pemantau, melainkan sebuah solusi komprehensif yang menjamin transparansi data dan akurasi audit. Beliau percaya bahwa dengan teknologi deteksi dini yang tepat, setiap pemilik bisnis dapat memiliki ketenangan pikiran (peace of mind) dalam mengembangkan usaha mereka tanpa perlu khawatir akan kebocoran aset yang tidak terdeteksi. Bapak Erwin terus berinovasi untuk memastikan V-Guard AI tetap menjadi benteng pertahanan digital terdepan bagi ekonomi Indonesia.
        </div>
        """
        st.markdown(profil_html, unsafe_allow_html=True)

# --- FOLDER 2: VISI, MISI & ROI (KEMBALI DITAMPILKAN) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Visi, Misi & Analisis Strategis")
    st.markdown("""
    <div class="vision-box">
        <h3>Visi Perusahaan</h3>
        <p>Menjadi pelopor utama dalam perlindungan aset digital dan fisik melalui integrasi kecerdasan buatan demi menciptakan ekosistem bisnis yang transparan dan bebas dari kecurangan.</p>
        <h3>Misi Perusahaan</h3>
        <ul>
            <li>Mengembangkan teknologi AI mutakhir yang mampu mendeteksi anomali transaksi secara real-time.</li>
            <li>Memberikan akses keamanan standar perbankan bagi pelaku usaha di semua tingkatan.</li>
            <li>Mengurangi risiko kerugian operasional hingga ke titik terendah bagi mitra bisnis V-Guard AI.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.write("---")
    st.subheader("📊 Simulasi Penghematan Aset")
    omzet = st.number_input("Omzet Bulanan Bisnis (Rp):", value=500000000, step=10000000)
    st.success(f"🛡️ Estimasi kebocoran yang dapat dicegah oleh V-Guard AI: **Rp {omzet * 0.045:,.0f}** per bulan.")

# --- FOLDER 3: PAKET LAYANAN (DIPERBAIKI) ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Layanan V-Guard AI")
    p_cols = st.columns(4)
    pkgs = [
        {"n": "BASIC", "s": "2.5jt", "m": "750rb", "c": "#f8f9fa", "f": "Audit Harian & Laporan Mingguan"},
        {"n": "MEDIUM", "s": "7.5jt", "m": "1.5jt", "c": "#e3f2fd", "f": "AI CCTV & Deteksi Fraud Dasar"},
        {"n": "ENTERPRISE", "s": "25jt", "m": "5jt", "c": "#e8f5e9", "f": "Multi-Branch & Dashboard Real-time"},
        {"n": "CORPORATE", "s": "50jt", "m": "10jt", "c": "#fff3e0", "f": "Custom AI Model & Prioritas Support"}
    ]
    for i, p in enumerate(pkgs):
        with p_cols[i]:
            st.markdown(f"""
            <div class="package-card" style="border-top: 5px solid {p['c']};">
                <h3 style="color: #333;">{p['n']}</h3>
                <p style="font-size: 14px; color: #666;">Setup Fee: <b>{p['s']}</b><br>Maintenance: <b>{p['m']}</b></p>
                <hr>
                <p style="font-size: 13px;">{p['f']}</p>
            </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Pilih {p['n']}", f"https://wa.me/628212190885?text=Tertarik%20Paket%20{p['n']}")

# --- FOLDER 4: REGISTRASI (TAMBAH KOLOM NAMA PELANGGAN) ---
elif menu == "4. 📝 Registrasi & Invoice":
    st.header("📝 Registrasi Klien & Penawaran")
    with st.form("reg_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            nama_pelanggan = st.text_input("Nama Pelanggan (Individu):")
            nama_bisnis = st.text_input("Nama Bisnis/Perusahaan:")
        with col_b:
            paket_pilihan = st.selectbox("Pilih Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
            harga_input = st.text_input("Harga Penawaran (Rp):", value="2.500.000")
            
        if st.form_submit_button("Simpan & Buat Penawaran"):
            if nama_pelanggan and nama_bisnis:
                st.session_state.db_nasabah.append({
                    "Waktu": datetime.now().strftime("%Y-%m-%d"), 
                    "Nama Pelanggan": nama_pelanggan,
                    "Bisnis": nama_bisnis, 
                    "Paket": paket_pilihan, 
                    "Harga": harga_input, 
                    "Status": "🔴 Menunggu"
                })
                st.success(f"Data {nama_pelanggan} telah tersimpan.")
                st.info(f"DRAFT PENAWARAN:\n\nYth. {nama_pelanggan}, paket {paket_pilihan} untuk {nama_bisnis} telah kami siapkan dengan nilai Rp {harga_input}.")

# --- FOLDER 5: ADMIN & AUDIT ---
elif menu == "5. 🔐 Admin & Audit AI":
    st.header("🔐 Intel Dashboard")
    pw = st.text_input("Password Admin:", type="password")
    if pw == "w1nbju8282":
        tab1, tab2 = st.tabs(["Database", "Audit AI"])
        with tab1:
            st.table(pd.DataFrame(st.session_state.db_nasabah))
        with tab2:
            st.line_chart(np.random.randn(20, 2))
            st.warning("AI mendeteksi aktivitas operasional berjalan normal.")

# 4. FOOTER
st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
