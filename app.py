import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database, Log & Riwayat Audit
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-01", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "MEDIUM", "Harga": 7500000, "Status": "🟢 AKTIF", "Jatuh_Tempo": "2026-04-01"}
    ]
if 'audit_logs' not in st.session_state:
    st.session_state.audit_logs = [f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - System Initialized"]

def add_log(msg):
    st.session_state.audit_logs.insert(0, f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - {msg}")

# 2. CSS CUSTOM PREMIUM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .stat-card { background: linear-gradient(135deg, #0d6efd 0%, #003d99 100%); color: white; padding: 20px; border-radius: 12px; text-align: center; margin-bottom: 10px; }
    .finance-card { background: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; }
    .due-alert { background: #fff3cd; color: #856404; padding: 15px; border-radius: 8px; border-left: 5px solid #ffc107; margin-bottom: 10px; font-weight: bold; }
    .log-container { background: #1e1e1e; color: #00ff00; padding: 15px; border-radius: 8px; font-family: 'Courier New', monospace; font-size: 12px; height: 200px; overflow-y: scroll; }
    .audit-note { font-size: 11px; color: #666; font-style: italic; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● Intelligence Active</p>', unsafe_allow_html=True)
    menu = st.radio("Navigasi Utama:", ["1. 👤 Profil Founder", "2. 🎯 Visi & ROI", "3. 📦 Paket Unggulan", "4. 📝 Registrasi & Invoice", "5. 🔐 Admin Control Center"])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- FOLDER 1: PROFIL FOUNDER (MIN 150 KATA) ---
if menu == "1. 👤 Profil Founder":
    st.markdown(f"""<div class="profile-box">
    <b>Bapak Erwin Sinaga</b> merupakan seorang Pemimpin Bisnis Senior (Senior Business Leader) yang telah mengabdikan dedikasi dan keahlian strategisnya selama lebih dari sepuluh tahun di pusat industri perbankan serta sektor manajemen aset berskala nasional. Sepanjang perjalanan karier profesionalnya yang gemilang, beliau dikenal sebagai figur yang memiliki ketajaman luar biasa dalam memetakan dinamika pasar serta memahami kompleksitas tata kelola finansial modern. Pengalaman panjang beliau di garis depan industri keuangan tidak hanya membentuk karakter kepemimpinan yang tangguh, tetapi juga melahirkan intuisi yang mendalam dalam mendeteksi ancaman terhadap keberlanjutan bisnis dari sudut pandang keamanan data dan integritas operasional. <br><br>
    V-Guard AI didirikan oleh Bapak Erwin Sinaga sebagai wujud nyata dari visi beliau untuk membawa standar keamanan tingkat tinggi ke tangan para pelaku usaha di seluruh Indonesia. Beliau sangat meyakini bahwa di era digital saat ini, setiap pemilik bisnis—tanpa memandang skala operasionalnya—berhak mendapatkan perlindungan aset yang berbasis teknologi masa depan. Melalui kepemimpinan strategisnya, V-Guard AI bertransformasi menjadi benteng pertahanan digital yang tidak hanya berfungsi sebagai alat pengawasan, melainkan sebagai mitra terpercaya yang menjamin akurasi audit serta transparansi data secara mutlak. Dedikasi Bapak Erwin dalam mengawal setiap fase pengembangan produk bertujuan untuk memastikan bahwa setiap inovasi yang dihadirkan mampu memberikan nilai ekonomi nyata, efisiensi jangka panjang, serta ketenangan pikiran bagi para pengusaha dalam mengelola aset berharga mereka secara profesional, modern, dan aman dari segala bentuk manipulasi sistemik.
    </div>""", unsafe_allow_html=True)

# --- FOLDER 4: REGISTRASI ---
elif menu == "4. 📝 Registrasi & Invoice":
    st.header("📝 Registrasi Klien Baru")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        n_pel = c1.text_input("Nama PIC:")
        n_bis = c1.text_input("Nama Bisnis:")
        p_pil = c2.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h_pen = c2.number_input("Harga (Rp):", value=2500000)
        wa_no = st.text_input("WhatsApp (62...):")
        if st.form_submit_button("Generate Invoice"):
            new_id = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
            due = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
            st.session_state.db_nasabah.append({"ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"), "Pelanggan": n_pel, "Bisnis": n_bis, "Paket": p_pil, "Harga": h_pen, "Status": "🔴 Menunggu", "Jatuh_Tempo": due})
            add_log(f"Invoice Terbit: {n_bis} (ID: {new_id})")
            st.code(f"INVOICE V-GUARD AI\nYth.
