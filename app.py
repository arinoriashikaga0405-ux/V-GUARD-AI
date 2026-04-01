import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI HALAMAN & STATE (LOCKED SOP)
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": 102, "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]
if 'admin_akses_terbuka' not in st.session_state:
    st.session_state.admin_akses_terbuka = False

WA_NUMBER = "628212190885"

# FUNGSI FORMAT RUPIAH SESUAI SOP
def format_rp(angka):
    try:
        return f"Rp {float(angka):,.0f}".replace(",", ".")
    except:
        return str(angka)

# 2. CSS CUSTOM (STABIL)
st.markdown("""
<style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; }
    .product-card { 
        background-color: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 15px; 
        padding: 20px; text-align: center; min-height: 520px; border-top: 8px solid #1E3A8A; 
    }
    .pkg-title { font-size: 24px; font-weight: bold; color: #1E3A8A; margin-bottom: 10px; }
    .feature-text { text-align: left; font-size: 14px; line-height: 1.6; margin-top: 15px; color: #444; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGASI (LOCK SOP)
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🛡️ V-GUARD AI</h1>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", caption="Erwin Sinaga | Senior Business Leader", use_container_width=True)
    st.write("---")
    menu = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Upload", 
        "5. 🔐 Akses Terbatas"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", f"https://wa.me/{WA_NUMBER}")

# --- MENU 1: PROFIL FOUNDER (SOP: >150 KATA, NO CEO/CSO) ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2.2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("""
        Bapak Erwin Sinaga adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir.

        Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel. Dengan visi besar untuk mendemokrasikan keamanan bisnis bagi semua kalangan, mulai dari tingkat UMKM hingga skala korporasi, beliau terus berinovasi dalam mengembangkan instrumen pengawasan yang adaptif terhadap tantangan ekonomi masa depan, memastikan setiap investasi klien terjaga dengan standar perlindungan berlapis dan efisiensi yang terukur secara nyata.
        """)

# --- MENU 2: ROI (LOCK SOP 7%) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("Analisis Strategis & Proteksi Kerugian")
    omzet = st.number_input("Omzet Bulanan Bisnis (Rp):", value=100000000, step=1000000)
    c_roi1, c_roi2 = st.columns(2)
    with c_roi1:
        pot_bocor = omzet * 0.07
        st.error(f"**Estimasi Kebocoran (7%):** {format_rp(pot_bocor)}")
    with c_roi2:
        hasil_roi = pot_bocor - 2500000
        st.metric("Dana Berhasil Diselamatkan", format_rp(hasil_roi), delta="ROI Positif")

# --- MENU 3: PAKET (LOCK SOP) ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("Layanan V-Guard AI")
    cols = st.columns(4)
    p_data = [
        ("BASIC", "1.5jt", "• Monitor Transaksi Harian<br>• Laporan Mingguan Manual<br>• Alarm Indikasi Fraud Dasar"), 
        ("SMART", "2.5jt", "• Fraud AI Detection Aktif<br>• Notifikasi WA Real-time<br>• Dashboard Pantauan Mobile"), 
        ("PRO", "5jt", "• VCS (Visual Control System)<br>• Integrasi CCTV AI<br>• Notifikasi Invoice Otomatis"), 
        ("ELITE", "Custom", "• Full System V-Guard AI<br>• On-site Audit Berkala<br>• Prioritas Layanan 24/7")
    ]
    for i, (n, p, f) in enumerate(p_data):
        with cols[i]:
            st.markdown(f'<div class="product-card"><div class="pkg-title">{n}</div><p style="color: #d32f2f; font-size: 20px;"><b>Rp {p}</b></p><div class="feature-text">{f}</div></div>', unsafe_allow_html=True)

# --- MENU 4: REGISTRASI (LOCK SOP) ---
elif menu == "4. 📝 Registrasi & Upload":
    st.header("Formulir Pendaftaran Klien")
    with st.form("reg_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Nama Lengkap Pelanggan:")
            st.text_input("Nama Bisnis/Usaha:")
        with col2:
            st.selectbox("Pilih Jenis Paket:", ["BASIC (1.5jt)", "SMART (2.5jt)", "PRO (5jt)", "ELITE (Custom)"])
            st.text_input("Konfirmasi Harga (Rp):")
        st.file_uploader("Upload KTP (JPG/PNG):", type=['jpg', 'png'])
        st.file_uploader("Upload Bukti Pembayaran:", type=['jpg', 'png'])
        st.form_submit_button("Kirim Pendaftaran")

# --- MENU 5: AKSES TERBATAS (FIXED ERROR) ---
elif menu == "5. 🔐 Akses Terbatas":
    if not st.session_state.admin_akses_terbuka:
        st.markdown("<h2 style='text-align: center;'>🔐 Verifikasi Otoritas Admin</h2>", unsafe_allow_html=True)
        cols_l = st.columns([1, 2, 1])
        with cols_l[1]:
            sandi = st.text_input("Masukkan Sandi Keamanan:", type="password")
            if st.button("Buka Panel Admin"):
                if sandi == "w1nbju8282":
                    st.session_state.admin_akses_terbuka = True
                    st.rerun()
                else:
                    st.error("Sandi Salah!")
    else:
        # HEADER & LOGOUT (SOP)
        h1, h2 = st.columns([5, 1])
        with h1: st.header("⚙️ Operasional V-Guard AI")
        with h2:
            if st.button("🔒 LOGOUT"):
                st.session_state.admin_akses_terbuka = False
                st.rerun()
        
        st.write("---")
        t1, t2, t3 = st.tabs(["📊 Database & Tamb
