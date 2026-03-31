import streamlit as st
import os
import pandas as pd
import numpy as np
from datetime import datetime
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database (Session State)
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-04-01", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "MEDIUM", "Harga": 7500000, "Status": "🟢 AKTIF"}
    ]

# 2. CSS CUSTOM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; border: 1px solid #f0f0f0; }
    .stat-card { background: linear-gradient(135deg, #007bff 0%, #0056b3 100%); color: white; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    .admin-box { background: #f8f9fa; padding: 20px; border-radius: 10px; border: 1px solid #dee2e6; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● Intelligence Active</p>', unsafe_allow_html=True)
    menu = st.radio("Navigasi:", ["1. 👤 Profil Founder", "2. 🎯 Visi & ROI", "3. 📦 Paket Produk", "4. 📝 Registrasi & Invoice", "5. 🔐 Admin Control Center"])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- FOLDER 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.markdown("""<div class="profile-box">
        <b>Bapak Erwin Sinaga</b> merupakan seorang Pemimpin Bisnis Senior dengan rekam jejak profesional lebih dari sepuluh tahun di industri perbankan dan manajemen aset nasional. Sebagai CEO dan CSO, beliau sangat memahami risiko operasional dan pentingnya perlindungan aset korporasi. V-Guard AI lahir dari visi beliau untuk menghadirkan audit cerdas 24/7 yang menjamin transparansi total bagi pemilik bisnis di Indonesia.
        </div>""", unsafe_allow_html=True)

# --- FOLDER 2: VISI & ROI ---
elif menu == "2. 🎯 Visi & ROI":
    st.header("🎯 Analisis ROI")
    omzet = st.number_input("Input Omzet Bulanan Klien (Rp):", value=500000000)
    st.success(f"🛡️ Estimasi Kebocoran Terdeteksi: **Rp {omzet * 0.045:,.0f}** / bulan.")

# --- FOLDER 3: PAKET PRODUK ---
elif menu == "3. 📦 Paket Produk":
    st.header("📦 Paket V-Guard AI")
    p_cols = st.columns(4)
    pkgs = [("BASIC", "2.5jt"), ("MEDIUM", "7.5jt"), ("ENTERPRISE", "25jt"), ("CORPORATE", "50jt")]
    for i, p in enumerate(p_cols):
        with p:
            st.info(f"**{pkgs[i][0]}**")
            st.write(f"Investasi: {pkgs[i][1]}")

# --- FOLDER 4: REGISTRASI & INVOICE ---
elif menu == "4. 📝 Registrasi & Invoice":
    st.header("📝 Form Registrasi Klien")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        n_pel = c1.text_input("Nama Pelanggan:")
        n_bis = c1.text_input("Nama Bisnis:")
        p_pil = c2.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h_pen = c2.number_input("Harga (Rp):", value=2500000)
        wa_no = st.text_input("WhatsApp Klien (62...):")
        
        if st.form_submit_button("Generate & Simpan"):
            new_id = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
            st.session_state.db_nasabah.append({"ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d"), "Pelanggan": n_pel, "Bisnis": n_bis, "Paket": p_pil, "Harga": h_pen, "Status": "🔴 Menunggu"})
            st.success("Data Tersimpan!")
            
            msg = f"INVOICE V-GUARD AI\nYth. {n_pel}\nPaket: {p_pil}\nNilai: Rp {h_pen:,.0f}\n\nTransfer ke BCA 3450074658 a/n ERWIN SINAGA"
            st.code(msg)
            st.link_button("🚀 Kirim WA", f"https://wa.me/{wa_no}?text={urllib.parse.quote(msg)}")

# --- FOLDER 5: ADMIN CONTROL CENTER (FITUR LENGKAP) ---
elif menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Control")
    pw = st.text_input("Sandi Admin:", type="password")
    
    if pw == "w1nbju8282":
        # 1. Statistik Dashboard
        df = pd.DataFrame(st.session_state.db_nasabah)
        col_stat1, col_stat2 = st.columns(2)
        with col_stat1:
            st.markdown(f'<div class="stat-card"><p>TOTAL OMZET V-GUARD</p><h2>Rp {df["Harga"].sum():,.0f}</h2></div>', unsafe_allow_html=True)
        with col_stat2:
            st.markdown(f'<div class="stat-card"><p>ASET TERLINDUNGI (SIMULASI)</p><h2>Rp {df["Harga"].sum()*12:,.0f}</h2></div>', unsafe_allow_html=True)

        # 2. Fitur Input Cepat (Admin Work)
        with st.expander("➕ Tambah Nasabah Baru (Input Cepat Admin)"):
            with st.form("admin_input"):
                ac1, ac2 = st.columns(2)
                a_pel = ac1.text_input("Nama Pelanggan:")
                a_bis = ac1.text_input("Bisnis:")
                a_pak = ac2.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
                a_harg = ac2.number_input("Harga:", value=2500000)
                if st.form_submit_button("Input ke Database"):
                    nid = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
                    st.session_state.db_nasabah.append({"ID": nid, "Waktu": datetime.now().strftime("%Y-%m-%d"), "Pelanggan": a_pel, "Bisnis": a_bis, "Paket": a_pak, "Harga": a_harg, "Status": "🔴 Menunggu"})
                    st.rerun()

        # 3. Manajemen Database (Edit/Hapus/Aktifkan)
        st.subheader("📋 Manajemen Database Nasabah")
        if not df.empty:
            for i, row in df.iterrows():
                with st.container():
                    c_id, c_name, c_bis, c_stat, c_act = st.columns([0.5, 1.5, 1.5, 1.5, 2])
                    c_id.write(f"#{row['ID']}")
                    c_name.write(row['Pelanggan'])
                    c_bis.write(row['Bisnis'])
                    c_stat.write(row['Status'])
                    
                    # Tombol Aksi
                    col_btn1, col_btn2 = c_act.columns(2)
                    if row['Status'] == "🔴 Menunggu":
                        if col_btn1.button("🟢 Aktifkan", key=f"akt_{i}"):
                            st.session_state.db_nasabah[i]['Status'] = "🟢 AKTIF"
                            st.rerun()
                    if col_btn2.button("🗑️ Hapus", key=f"del_{i}"):
                        st.session_state.db_nasabah.pop(i)
                        st.rerun()
                st.write("---")
        else:
            st.info("Database Kosong.")

        # 4. Audit Visual
        st.subheader("📉 Grafik Performa Audit AI")
        st.line_chart(np.random.randn(20, 2))

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
