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
        {"Waktu": "2026-03-31", "Nama Personal": "Admin", "Nama Bisnis": "V-Guard Core", "Paket": "CORPORATE", "Harga": "50.000.000", "Status": "🟢 AKTIF"}
    ]

# 2. CSS CUSTOM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 16px; margin-top: 10px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; font-size: 16px; border: 1px solid #f0f0f0; }
    .security-tag { background: #e8f5e9; color: #2e7d32; padding: 5px 15px; border-radius: 20px; font-size: 12px; font-weight: bold; display: inline-block; margin-top: 10px; }
    .invoice-box { background: #f8f9fa; padding: 20px; border: 1px dashed #007bff; border-radius: 10px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● System Online / Secured</p>', unsafe_allow_html=True)
    menu = st.radio("Navigasi Sistem:", ["1. 👤 Profil Founder", "2. 🎯 Visi & ROI", "3. 📦 Paket Layanan", "4. 📝 Registrasi & Invoice", "5. 🔐 Admin & Audit AI"])
    st.write("---")
    st.link_button("💬 Chat Customer Service", "https://wa.me/628212190885")

# --- FOLDER 1: PROFIL & SECURITY ---
if menu == "1. 👤 Profil Founder":
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.markdown(f"""<div class="profile-box">
        <b>Bapak Erwin Sinaga</b> merupakan Pemimpin Bisnis Senior dengan pengalaman lebih dari 10 tahun di industri perbankan dan manajemen aset. <br><br>
        V-Guard AI hadir dengan standar keamanan tinggi. Kami menjamin kerahasiaan data nasabah melalui enkripsi tingkat lanjut.<br>
        <span class="security-tag">🛡️ ISO 27001 Certified Simulation</span> 
        <span class="security-tag">🔐 End-to-End Encrypted</span>
        </div>""", unsafe_allow_html=True)

# --- FOLDER 2: VISI & ROI ---
elif menu == "2. 🎯 Visi & ROI":
    st.header("🎯 Strategi ROI")
    omzet = st.number_input("Input Omzet Bulanan (Rp):", value=500000000)
    st.success(f"Estimasi Penyelamatan Aset: **Rp {omzet * 0.045:,.0f}** / bulan")

# --- FOLDER 3: PAKET LAYANAN ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Layanan")
    p_cols = st.columns(4)
    pkgs = [{"n": "BASIC", "c": "#f8f9fa"}, {"n": "MEDIUM", "c": "#e3f2fd"}, {"n": "ENTERPRISE", "c": "#e8f5e9"}, {"n": "CORPORATE", "c": "#fff3e0"}]
    for i, p in enumerate(pkgs):
        with p_cols[i]:
            st.info(f"**{p['n']} PACKAGE**")
            st.write("Audit AI harian & Deteksi Fraud Otomatis.")
            st.link_button("Pilih", "https://wa.me/628212190885")

# --- FOLDER 4: REGISTRASI & INVOICE (PROFESSIONALISM) ---
elif menu == "4. 📝 Registrasi & Invoice":
    st.header("📝 Registrasi & Otomatisasi Invoice")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        u = c1.text_input("Nama Pendaftar:")
        b = c1.text_input("Nama Bisnis:")
        p = c2.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h = c2.text_input("Harga Kesepakatan (Rp):", value="2.500.000")
        sub = st.form_submit_button("Simpan & Buat Penawaran")
        
        if sub:
            st.session_state.db_nasabah.append({"Waktu": datetime.now().strftime("%Y-%m-%d"), "Nama Personal": u, "Nama Bisnis": b, "Paket": p, "Harga": h, "Status": "🔴 Menunggu"})
            st.markdown("### 📄 Draft Invoice / Penawaran")
            inv_text = f"""
            Kepada Yth. {u} ({b}),
            Berikut adalah detail penawaran V-Guard AI:
            - Paket: {p}
            - Biaya: Rp {h}
            - Status: Menunggu Aktivasi
            Silakan lakukan pembayaran ke rekening perusahaan untuk aktivasi sistem.
            """
            st.code(inv_text, language="text")
            st.info("Bapak bisa copy teks di atas untuk dikirim ke WhatsApp klien.")

# --- FOLDER 5: ADMIN & AUDIT AI (DASHBOARD & LAPORAN) ---
elif menu == "5. 🔐 Admin & Audit AI":
    st.header("🔐 Intelligence Dashboard")
    pw = st.text_input("Password Admin:", type="password")
    if pw == "w1nbju8282":
        t1, t2 = st.tabs(["📊 Database Nasabah", "📉 Laporan Audit AI"])
        
        with t1:
            st.table(pd.DataFrame(st.session_state.db_nasabah))
            
        with t2:
            st.subheader("Simulasi Deteksi Kebocoran Aset (Real-time)")
            chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Audit Normal', 'Anomali Fraud'])
            st.line_chart(chart_data)
            st.warning("⚠️ AI Detection: Ditemukan 2 anomali pada transaksi di Cabang Tangerang hari ini.")
            st.button("Unduh Laporan Audit (.pdf)")

# 4. FOOTER
st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
