import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database (Pertahankan Data)
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25 08:00", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "MEDIUM", "Harga": 7500000, "Status": "🟢 AKTIF", "Jatuh_Tempo": "2026-04-25"}
    ]

# 2. CSS CUSTOM PREMIUM (MODERN & CLEAN)
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: #ffffff; border-radius: 15px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 12px rgba(0,0,0,0.05); }
    .vision-card { background: linear-gradient(135deg, #f8f9fa 0%, #e9cece 100%); padding: 20px; border-radius: 12px; border-left: 5px solid #0d6efd; height: 100%; }
    .finance-card { background: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; }
    .fraud-alert { background: #f8d7da; color: #721c24; padding: 15px; border-radius: 8px; border-left: 5px solid #dc3545; margin-bottom: 10px; font-weight: bold; animation: blinker 1.5s linear infinite; }
    .due-alert { background: #fff3cd; color: #856404; padding: 15px; border-radius: 8px; border-left: 5px solid #ffc107; margin-bottom: 10px; font-weight: bold; }
    @keyframes blinker { 50% { opacity: 0.5; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● Intelligence Active</p>', unsafe_allow_html=True)
    menu = st.radio("Menu Navigasi:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Invoice", 
        "5. 🔐 Admin Control Center"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- NAVIGASI 1: PROFIL FOUNDER (PERBAIKAN FOTO & NARASI) ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
        else:
            st.info("Unggah foto 'erwin.jpg' untuk melihat profil visual.")
    with col2:
        st.markdown(f"""<div class="profile-box">
        <b>Bapak Erwin Sinaga</b> merupakan seorang Pemimpin Bisnis Senior (Senior Business Leader) yang telah mengabdikan dedikasi dan keahlian strategisnya selama lebih dari sepuluh tahun di pusat industri perbankan serta sektor manajemen aset berskala nasional. Sepanjang perjalanan karier profesionalnya yang gemilang, beliau dikenal sebagai figur yang memiliki ketajaman luar biasa dalam memetakan dinamika pasar serta memahami kompleksitas tata kelola finansial modern. Pengalaman panjang beliau di garis depan industri keuangan tidak hanya membentuk karakter kepemimpinan yang tangguh, tetapi juga melahirkan intuisi yang mendalam dalam mendeteksi ancaman terhadap keberlanjutan bisnis dari sudut pandang keamanan data dan integritas operasional. <br><br>
        V-Guard AI didirikan oleh Bapak Erwin Sinaga sebagai wujud nyata dari visi beliau untuk membawa standar keamanan tingkat tinggi ke tangan para pelaku usaha di seluruh Indonesia. Beliau sangat meyakini bahwa di era digital saat ini, setiap pemilik bisnis—tanpa memandang skala operasionalnya—berhak mendapatkan perlindungan aset yang berbasis teknologi masa depan. Melalui kepemimpinan strategisnya, V-Guard AI bertransformasi menjadi benteng pertahanan digital yang tidak hanya berfungsi sebagai alat pengawasan, melainkan sebagai mitra terpercaya yang menjamin akurasi audit serta transparansi data secara mutlak. Dedikasi Bapak Erwin dalam mengawal setiap fase pengembangan produk bertujuan untuk memastikan bahwa setiap inovasi yang dihadirkan mampu memberikan nilai ekonomi nyata, efisiensi jangka panjang, serta ketenangan pikiran bagi para pengusaha dalam mengelola aset berharga mereka secara profesional, modern, dan aman dari segala bentuk manipulasi sistemik.
        </div>""", unsafe_allow_html=True)

# --- NAVIGASI 2: VISI, MISI & ROI (PERBAIKAN VISUAL) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Strategi Bisnis & Analisis ROI")
    cv1, cv2 = st.columns(2)
    with cv1:
        st.markdown("""<div class="vision-card"><h3>Visi Utama</h3><p>Menjadi standar emas pertahanan digital nasional yang mengintegrasikan kecerdasan buatan untuk mengeliminasi segala bentuk kebocoran finansial dan operasional pada bisnis modern.</p></div>""", unsafe_allow_html=True)
    with cv2:
        st.markdown("""<div class="vision-card"><h3>Misi Strategis</h3><p>1. Menghadirkan pengawasan otonom 24/7.<br>2. Menjamin transparansi audit data klien.<br>3. Mendemokratisasi teknologi AI tingkat tinggi untuk UKM hingga Korporasi.</p></div>""", unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("📊 Kalkulator Pengembalian Investasi (ROI)")
    omzet = st.number_input("Estimasi Omzet Bulanan Klien (Rp):", value=500000000, step=10000000)
    leakage = omzet * 0.045
    st.success(f"🛡️ **V-Guard AI** berpotensi menyelamatkan aset sebesar **Rp {leakage:,.0f}** setiap bulannya melalui deteksi fraud dini.")

# --- NAVIGASI 3: PAKET UNGGULAN (PERBAIKAN TAMPILAN) ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("📦 Solusi Keamanan V-Guard AI")
    st.markdown("""
    | Paket | Harga Investasi | Fitur Utama | Target Bisnis |
    | :--- | :--- | :--- | :--- |
    | **BASIC** | Rp 2.500.000 | Audit Harian & Alarm Dasar | Toko/Retail Kecil |
    | **MEDIUM** | Rp 7.500.000 | AI CCTV & Notifikasi Cloud | Cafe & Restoran |
    | **ENTERPRISE** | Rp 25.000.000 | Full Fraud Analytics | Distributor & Pabrik |
    | **CORPORATE** | Rp 50.000.000 | Custom AI & 24/7 Support | Perusahaan Nasional |
    """)
    st.info("Semua paket sudah termasuk instalasi sistem dan pelatihan admin.")

# --- NAVIGASI 4: REGISTRASI & INVOICE (LOCK) ---
elif menu == "4. 📝 Registrasi & Invoice":
    st.header("📝 Registrasi & Penagihan")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        n_pel = c1.text_input("Nama PIC:")
        n_bis = c1.text_input("Nama Bisnis:")
        p_pil = c2.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h_pen = c2.number_input("Harga (Rp):", value=2500000)
        wa_no = st.text_input("WhatsApp (62...):")
        if st.form_submit_button("Buat Invoice"):
            new_id = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
            due = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
            st.session_state.db_nasabah.append({"ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"), "Pelanggan": n_pel, "Bisnis": n_bis, "Paket": p_pil, "Harga": h_pen, "Status": "🔴 Menunggu", "Jatuh_Tempo": due})
            inv_text = f"""INVOICE V-GUARD AI\nYth. {n_pel}\nBisnis: {n_bis}\nTotal: Rp {h_pen:,.0f}\n\nBCA: 3450074658\nA/n: ERWIN SINAGA"""
            st.code(inv_text)
            st.link_button("🚀 Kirim WA", f"https://wa.me/{wa_no}?text={urllib.parse.quote(inv_text)}")

# --- NAVIGASI 5: ADMIN CONTROL CENTER (LOCK - SEMUA FITUR ADA) ---
elif menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Control")
    pw = st.text_input("Sandi Otoritas:", type="password")
    if pw == "w1nbju8282":
        df = pd.DataFrame(st.session_state.db_nasabah)
        
        # 1. LABA RUGI MINGGUAN
        st.subheader("📊 Laporan Laba Rugi Mingguan")
        c_fin1, c_fin2, c_fin3 = st.columns(3)
        rev = df["Harga"].sum()
        ops = rev * 0.15
        profit = rev - ops
        c_fin1.markdown(f'<div class="finance-card"><p>Omzet</p><h3 style="color:#0d6efd;">Rp {rev:,.0f}</h3></div>', unsafe_allow_html=True)
        c_fin2.markdown(f'<div class="finance-card"><p>Ops Cost (15%)</p><h3 style="color:#dc3545;">-Rp {ops:,.0f}</h3></div>', unsafe_allow_html=True)
        c_fin3.markdown(f'<div class="finance-card"><p><b>NET PROFIT</b></p><h3 style="color:#28a745;">Rp {profit:,.0f}</h3></div>', unsafe_allow_html=True)

        # 2. ALARM FRAUD & BILLING
        st.write("---")
        ca1, ca2 = st.columns(2)
        with ca1:
            st.subheader("🚨 Alarm Fraud Detection")
            if not df[df['Harga'] > 10000000].empty:
                st.markdown('<div class="fraud-alert">🚩 PERINGATAN: Deteksi Transaksi Anomali (>10jt)!</div>', unsafe_allow_html=True)
            else: st.success("Sistem Aman.")
        with ca2:
            st.subheader("📅 Billing Alert")
            today = datetime.now().strftime("%Y-%m-%d")
            if not df[df['Jatuh_Tempo'] <= today].empty:
                st.markdown('<div class="due-alert">⚠️ Perhatian: Ada Invoice Jatuh Tempo!</div>', unsafe_allow_html=True)
            else: st.success("Penagihan Lancar.")

        # 3. TAMBAH AKUN MANUAL & DATABASE
        st.write("---")
        with st
