import streamlit as st
import os
import pandas as pd
import numpy as np
from datetime import datetime
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database Sesi untuk Akun Klien
if 'db_akun' not in st.session_state:
    st.session_state.db_akun = []

# 2. CSS CUSTOM PREMIUM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 8px rgba(0,0,0,0.02); }
    .vision-box { background: #fdfdfd; padding: 25px; border-left: 5px solid #007bff; border-radius: 10px; margin-bottom: 25px; }
    .package-card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #eee; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 250px; }
    .invoice-output { background: #f8f9fa; padding: 20px; border-left: 8px solid #007bff; border-radius: 5px; font-family: monospace; white-space: pre-wrap; font-size: 14px; margin-top: 15px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● Intelligence Active</p>', unsafe_allow_html=True)
    menu = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Invoice",
        "5. 🔐 Admin: Buat Akun Klien"
    ])
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
        <b>Bapak Erwin Sinaga</b> merupakan seorang Pemimpin Bisnis Senior (Senior Business Leader) yang telah mengukir rekam jejak profesional impresif selama lebih dari sepuluh tahun di industri perbankan dan manajemen aset nasional. Sepanjang perjalanan kariernya, beliau telah dipercaya memegang berbagai tanggung jawab strategis, termasuk peran krusial sebagai Chief Executive Officer (CEO) dan Chief Sales Officer (CSO). Dalam kapasitas tersebut, beliau bertanggung jawab penuh atas mitigasi risiko operasional, kepatuhan sistem, serta perlindungan aset korporasi dalam skala besar. Pengalaman mendalam di sektor finansial ini memberikan beliau perspektif unik dan tajam dalam mengidentifikasi titik-titik lemah sistem manajemen konvensional yang sering kali menjadi celah terjadinya inefisiensi finansial. <br><br>
        V-Guard AI didirikan berdasarkan dedikasi beliau untuk menghadirkan teknologi pengawasan berbasis Artificial Intelligence yang mampu bekerja secara otonom dan presisi selama 24 jam penuh. Beliau sangat meyakini bahwa integritas dan transparansi data adalah fondasi utama bagi pertumbuhan bisnis yang berkelanjutan. Oleh karena itu, melalui kepemimpinan beliau, V-Guard AI berkomitmen untuk mendemokratisasi standar keamanan tingkat tinggi agar dapat diakses oleh pemilik bisnis dari berbagai skala di Indonesia. Dengan visi untuk membangun benteng pertahanan digital yang tangguh, Bapak Erwin Sinaga terus memastikan bahwa setiap inovasi yang dihadirkan mampu memberikan nilai ekonomi nyata serta ketenangan pikiran (peace of mind) bagi para pengusaha dalam mengelola aset berharga mereka secara profesional dan aman.
        </div>""", unsafe_allow_html=True)

# --- FOLDER 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Strategi & Analisis ROI")
    st.markdown("""<div class="vision-box">
        <h3>Visi Perusahaan</h3>
        <p>Menjadi mitra pertahanan digital terdepan di Indonesia yang menjamin transparansi operasional total melalui inovasi kecerdasan buatan.</p>
        <h3>Misi Strategis</h3>
        <ul>
            <li>Mengeliminasi potensi kebocoran aset bisnis secara sistemik melalui AI Audit.</li>
            <li>Menyediakan laporan transparansi real-time bagi pemilik bisnis.</li>
            <li>Memberikan rasa aman melalui deteksi fraud otomatis 24/7.</li>
        </ul>
    </div>""", unsafe_allow_html=True)
    st.subheader("📊 Simulasi Penghematan (ROI)")
    omzet = st.number_input("Input Omzet Bulanan Bisnis (Rp):", value=500000000, step=10000000)
    st.success(f"🛡️ Estimasi Kebocoran yang Dicegah: **Rp {omzet * 0.045:,.0f}** / bulan.")

# --- FOLDER 3: PAKET UNGGULAN ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("📦 4 Paket Produk Unggulan V-Guard AI")
    p_cols = st.columns(4)
    pkgs = [
        {"n": "BASIC", "p": "2.5jt", "f": "AI Audit Harian & Laporan Mingguan"},
        {"n": "MEDIUM", "p": "7.5jt", "f": "AI CCTV Cloud & Deteksi Antrean"},
        {"n": "ENTERPRISE", "p": "25jt", "f": "Multi-Branch Support & Fraud Analytics"},
        {"n": "CORPORATE", "p": "50jt", "f": "Custom AI Model & Dedicated Manager"}
    ]
    for i, p in enumerate(pkgs):
        with p_cols[i]:
            st.markdown(f"""<div class="package-card">
                <h3>{p['n']}</h3>
                <h2 style="color:#007bff;">{p['p']}</h2>
                <p style="font-size:14px; color:#666;">{p['f']}</p>
            </div>""", unsafe_allow_html=True)

# --- FOLDER 4: REGISTRASI & INVOICE ---
elif menu == "4. 📝 Registrasi & Invoice":
    st.header("📝 Registrasi & Penawaran")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        n_pel = c1.text_input("Nama Pelanggan (PIC):")
        n_bis = c1.text_input("Nama Bisnis:")
        p_pil = c2.selectbox("Pilih Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h_pen = c2.number_input("Harga Investasi (Rp):", value=2500000)
        wa_no = st.text_input("Nomor WhatsApp Klien (Contoh: 62812...):")
        
        if st.form_submit_button("Generate Invoice"):
            if n_pel and wa_no:
                inv_msg = f"*INVOICE V-GUARD AI*\n\nYth. {n_pel} ({n_bis}),\n\nBiaya aktivasi sistem:\n- Paket: {p_pil}\n- Nilai: Rp {h_pen:,.0f}\n\n*PEMBAYARAN:* \nBCA: 3450074658\nA/n: ERWIN SINAGA"
                st.markdown(f'<div class="invoice-output">{inv_msg}</div>', unsafe_allow_html=True)
                st.link_button("🚀 Kirim Invoice via WhatsApp", f"https://wa.me/{wa_no}?text={urllib.parse.quote(inv_msg)}")
            else:
                st.warning("Mohon lengkapi Nama Pelanggan dan Nomor WhatsApp.")

# --- FOLDER 5: ADMIN BUAT AKUN ---
elif menu == "5. 🔐 Admin: Buat Akun Klien":
    st.header("🔐 Panel Aktivasi Akun Klien")
    pw = st.text_input("Sandi Otoritas Admin:", type="password")
    
    if pw == "w1nbju8282":
        with st.form("buat_akun"):
            st.subheader("➕ Buat Akun & Siapkan Undangan")
            ca1, ca2 = st.columns(2)
            k_nama = ca1.text_input("Nama PIC Klien:")
            k_bisnis = ca1.text_input("Nama Bisnis Klien:")
            k_wa = ca2.text_input("Nomor WA (Contoh: 62812...):")
            k_paket = ca2.selectbox("Paket Aktivasi:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
            
            submit_akun = st.form_submit_button("Buat Akun & Siapkan Undangan")
            
            if submit_akun and k_nama and k_wa:
                st.session_state.db_akun.append({
                    "Nama": k_nama, "Bisnis": k_bisnis, "WA": k_wa, "Paket": k_paket
                })
                st.success(f"Akun untuk {k_bisnis} berhasil didaftarkan!")
                
                undangan = f"""*UNDANGAN AKTIVASI V-GUARD AI*
                
Selamat! Akun V-Guard AI untuk *{k_bisnis}* telah disiapkan.

Detail Akun:
- PIC: {k_nama}
- Paket: {k_paket} Intelligence

Silakan login melalui link akses yang telah kami sediakan untuk mulai mengamankan aset bisnis Anda secara real-time.

Terima kasih atas kepercayaan Anda.
Salam, 
*Erwin Sinaga (Founder V-Guard AI)*"""
                
                st.info("Klik tombol di bawah untuk mengirim undangan:")
                st.link_button("🚀 KIRIM UNDANGAN KE WHATSAPP KLIEN", f"https://wa.me/{k_wa}?text={urllib.parse.quote(undangan)}")
    elif pw != "":
        st.error("Kata sandi salah.")

# 4. FOOTER
st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
