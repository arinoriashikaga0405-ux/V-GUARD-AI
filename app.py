import streamlit as st
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25 08:00", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "MEDIUM", "Harga": 7500000, "Status": "🟢 AKTIF", "Jatuh_Tempo": "2026-04-25"}
    ]

# 2. CSS CUSTOM PREMIUM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .finance-card { background: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; }
    .due-alert { background: #fff3cd; color: #856404; padding: 15px; border-radius: 8px; border-left: 5px solid #ffc107; margin-bottom: 10px; font-weight: bold; }
    .fraud-alert { background: #f8d7da; color: #721c24; padding: 15px; border-radius: 8px; border-left: 5px solid #dc3545; margin-bottom: 10px; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0.5; } }
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

# --- FOLDER 1: PROFIL FOUNDER ---
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
            inv_text = f"""INVOICE V-GUARD AI
Yth. {n_pel}
Bisnis: {n_bis}
Total Investasi: Rp {h_pen:,.0f}

BCA: 3450074658
A/n: ERWIN SINAGA"""
            st.code(inv_text)
            st.link_button("🚀 Kirim WA", f"https://wa.me/{wa_no}?text={urllib.parse.quote(inv_text)}")

# --- FOLDER 5: ADMIN CONTROL CENTER ---
elif menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Control & Weekly Finance")
    pw = st.text_input("Sandi Otoritas Admin:", type="password")
    if pw == "w1nbju8282":
        df = pd.DataFrame(st.session_state.db_nasabah)
        
        # 1. LAPORAN LABA RUGI PER MINGGU
        st.subheader("📊 Laporan Laba Rugi (Per Minggu)")
        c_fin1, c_fin2, c_fin3 = st.columns(3)
        total_rev = df["Harga"].sum()
        ops_cost = total_rev * 0.15 # Estimasi biaya operasional
        net_profit = total_rev - ops_cost
        
        c_fin1.markdown(f'<div class="finance-card"><p>Omzet Mingguan</p><h3 style="color:#0d6efd;">Rp {total_rev:,.0f}</h3></div>', unsafe_allow_html=True)
        c_fin2.markdown(f'<div class="finance-card"><p>Biaya Ops (Server/AI)</p><h3 style="color:#dc3545;">-Rp {ops_cost:,.0f}</h3></div>', unsafe_allow_html=True)
        c_fin3.markdown(f'<div class="finance-card"><p><b>LABA BERSIH MINGGUAN</b></p><h3 style="color:#28a745;">Rp {net_profit:,.0f}</h3></div>', unsafe_allow_html=True)

        # 2. ALARM INDIKASI FRAUD & BILLING
        st.write("---")
        col_warn1, col_warn2 = st.columns(2)
        
        with col_warn1:
            st.subheader("🚨 Alarm Indikasi Fraud")
            # Logika Fraud: Jika ada transaksi di atas 10jt atau ID ganjil (Simulasi)
            fraud_hits = df[df['Harga'] > 10000000]
            if not fraud_hits.empty:
                for _, r in fraud_hits.iterrows():
                    st.markdown(f'<div class="fraud-alert">🚩 FRAUD DETECTED: Transaksi Tak Wajar di {r["Bisnis"]}!</div>', unsafe_allow_html=True)
            else: st.success("✅ Tidak ada indikasi fraud sistem.")

        with col_warn2:
            st.subheader("📅 Billing Alert")
            today = datetime.now().strftime("%Y-%m-%d")
            due_df = df[df['Jatuh_Tempo'] <= today]
            if not due_df.empty:
                for _, r in due_df.iterrows():
                    st.markdown(f'<div class="due-alert">⚠️ {r["Bisnis"]} JATUH TEMPO!</div>', unsafe_allow_html=True)
            else: st.success("✅ Semua tagihan lancar.")

        # 3. TAMBAH AKUN MANUAL
        st.write("---")
        with st.expander("➕ Tambah Akun & Aktivasi Manual"):
            with st.form("manual_add"):
                m1, m2 = st.columns(2)
                m_pic = m1.text_input("PIC Klien:")
                m_bis = m1.text_input("Nama Bisnis:")
                m_pkt = m2.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
                m_hrg = m2.number_input("Harga (Rp):", value=2500000)
                if st.form_submit_button("Simpan & Aktifkan"):
                    nid = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
                    due_m = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
                    st.session_state.db_nasabah.append({"ID": nid, "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"), "Pelanggan": m_pic, "Bisnis": m_bis, "Paket": m_pkt, "Harga": m_hrg, "Status": "🟢 AKTIF", "Jatuh_Tempo": due_m})
                    st.rerun()

        # 4. MANAJEMEN DATABASE
        st.write("---")
        s_query = st.text_input("🔍 Cari Klien:")
        f_df = df[df['Pelanggan'].str.contains(s_query, case=False) | df['Bisnis'].str.contains(s_query, case=False)]
        st.dataframe(f_df, use_container_width=True)
        
    elif pw != "": st.error("Sandi Salah!")

# --- LAINNYA ---
elif menu == "2. 🎯 Visi & ROI":
    st.header("🎯 Strategi ROI")
    omzet = st.number_input("Omzet (Rp):", value=500000000)
    st.success(f"Pencegahan Kebocoran: Rp {omzet * 0.045:,.0f}/bln")
elif menu == "3. 📦 Paket Unggulan":
    st.header("📦 Paket Produk")
    st.write("BASIC | MEDIUM | ENTERPRISE | CORPORATE")

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
