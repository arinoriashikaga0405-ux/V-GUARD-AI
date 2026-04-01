import streamlit as st
import os
import pandas as pd
from datetime import datetime
import google.generativeai as genai

# 1. KONFIGURASI AI
try:
    genai.configure(api_key="AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA")
    model = genai.GenerativeModel('gemini-pro')
    ai_ok = True
except:
    ai_ok = False

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Database Sesi
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": 102, "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]
if 'admin_akses_terbuka' not in st.session_state:
    st.session_state.admin_akses_terbuka = False

WA_NUMBER = "628212190885"

# 2. CSS CUSTOM (STABIL)
st.markdown(f"""
<style>
    .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; }}
    .product-card {{ 
        background-color: #f8f9fa; 
        border: 1px solid #e0e0e0; 
        border-radius: 15px; 
        padding: 20px; 
        text-align: center; 
        min-height: 500px; 
        border-top: 8px solid #1E3A8A; 
    }}
    .pkg-title {{ font-size: 24px; font-weight: bold; color: #1E3A8A; margin-bottom: 10px; }}
    .feature-text {{ text-align: left; font-size: 14px; line-height: 1.6; margin-top: 15px; color: #444; }}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGASI
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🛡️ V-GUARD AI</h1>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
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

# --- MENU 1: PROFIL FOUNDER (TETAP) ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2.2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("""Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang telah mengabdikan lebih dari satu dekade karir profesionalnya untuk mendalami seluk-beluk operasional bisnis dan efisiensi organisasi di skala nasional. Dengan keahlian mendalam dalam navigasi industri finansial, beliau memiliki kemampuan analitis yang tajam dalam mengidentifikasi titik-titik rawan kebocoran aset yang seringkali luput dari pengawasan manajemen konvensional. Dedikasi beliau terhadap prinsip integritas dan akuntabilitas menjadi pilar utama di balik berdirinya V-Guard AI, sebuah platform yang mengintegrasikan kecerdasan buatan untuk memberikan perlindungan berlapis bagi para pengusaha di Indonesia.""")

# --- MENU 2: ROI (TETAP) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("Analisis Strategis")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    st.metric("Potensi Efisiensi (7%)", f"Rp {omzet * 0.07:,.0f}")

# --- MENU 3: PAKET UNGGULAN (DENGAN DETAIL FITUR) ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("Layanan V-Guard AI")
    cols = st.columns(4)
    p_data = [
        ("BASIC", "1.5jt", "• Monitor Transaksi Harian<br>• Laporan Mingguan Manual<br>• Alarm Indikasi Fraud Dasar<br>• Support Layanan Jam Kerja"), 
        ("SMART", "2.5jt", "• Fraud AI Detection Aktif<br>• Notifikasi WA Real-time<br>• Alarm Indikasi Fraud Pintar<br>• Dashboard Pantauan Mobile"), 
        ("PRO", "5jt", "• VCS (Visual Control System)<br>• Integrasi CCTV AI<br>• Notifikasi Invoice Otomatis<br>• Laporan Audit PDF AI"), 
        ("ELITE", "Custom", "• Full System V-Guard AI<br>• On-site Audit Berkala<br>• Kustomisasi Alarm Khusus<br>• Prioritas Layanan 24/7")
    ]
    for i, (n, p, f) in enumerate(p_data):
        with cols[i]:
            st.markdown(f"""
            <div class="product-card">
                <div class="pkg-title">{n}</div>
                <p style="color: #d32f2f; font-size: 20px;"><b>Rp {p}</b></p>
                <div class="feature-text">{f}</div>
            </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Pilih {n}", f"https://wa.me/{WA_NUMBER}?text=Saya%20tertarik%20Paket%20{n}")

# --- MENU 4: REGISTRASI (NAMA, PAKET, HARGA) ---
elif menu == "4. 📝 Registrasi & Upload":
    st.header("Formulir Pendaftaran Klien")
    with st.form("reg_klien"):
        col1, col2 = st.columns(2)
        with col1:
            nama_user = st.text_input("Nama Lengkap Pelanggan:")
            nama_toko = st.text_input("Nama Bisnis/Usaha:")
        with col2:
            pkt_pilih = st.selectbox("Pilih Jenis Paket:", ["BASIC (1.5jt)", "SMART (2.5jt)", "PRO (5jt)", "ELITE (Custom)"])
            harga_pkt = st.text_input("Konfirmasi Harga (Rp):")
        
        st.file_uploader("Upload KTP (JPG/PNG):", type=['jpg', 'png'])
        st.file_uploader("Upload Bukti Pembayaran:", type=['jpg', 'png'])
        
        if st.form_submit_button("Kirim Pendaftaran"):
            st.success(f"Pendaftaran {nama_user} untuk paket {pkt_pilih} berhasil dikirim!")

# --- MENU 5: AKSES TERBATAS (DENGAN FITUR VCS, ALARM, INVOICE, CCTV & LOGOUT) ---
elif menu == "5. 🔐 Akses Terbatas":
    if not st.session_state.admin_akses_terbuka:
        st.markdown("<h2 style='text-align: center;'>🔐 Verifikasi Otoritas Admin</h2>", unsafe_allow_html=True)
        cols_l = st.columns([1, 2, 1])
        with cols_l[1]:
            sandi = st.text_input("Masukkan Sandi Keamanan:", type="password", key="sandi_admin")
            if st.button("Buka Panel Admin"):
                if sandi == "w1nbju8282":
                    st.session_state.admin_akses_terbuka = True
                    st.rerun()
                else:
                    st.error("Sandi Salah!")
    else:
        # LOGOUT DI POJOK KANAN ATAS
        h1, h2 = st.columns([5, 1])
        with h1: st.header("⚙️ Operasional V-Guard AI")
        with h2:
            if st.button("🔒 LOGOUT"):
                st.session_state.admin_akses_terbuka = False
                st.rerun()
        
        st.write("---")
        t1, t2, t3 = st.tabs(["📊 Kelola Akun", "🚨 Monitoring (VCS/Alarm/CCTV)", "🧾 Invoice & Billing"])
        
        with t1:
            st.dataframe(pd.DataFrame(st.session_state.db_nasabah), use_container_width=True)

        with t2:
            st.subheader("Pantauan Lapangan")
            c_a, c_b, c_c = st.columns(3)
            with c_a: st.info("🖥️ **VCS System**"); st.button("Aktifkan Visual Control")
            with c_b: st.error("🔔 **Alarm Fraud**"); st.button("Lihat Indikasi Fraud")
            with c_c: st.warning("📹 **CCTV Monitor**"); st.button("Buka Kamera")

        with t3:
            st.subheader("🧾 Invoice Management")
            st.info("Kirim Notifikasi Tagihan ke Pelanggan")
            if st.button("Kirim Notifikasi Invoice via WA"):
                st.success("Notifikasi sedang dikirim ke database pelanggan.")

st.markdown('<div class="footer">© 2026 V-Guard AI | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
