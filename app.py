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
        {"Waktu": "2026-03-31", "Pelanggan": "Budi Santoso", "Bisnis": "Retailindo", "Paket": "MEDIUM", "Harga": "7.500.000", "Status": "🟢 AKTIF"}
    ]

# 2. CSS CUSTOM UNTUK TAMPILAN PREMIUM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; margin-top: 5px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; font-size: 16px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 8px rgba(0,0,0,0.02); }
    .vision-box { background: #fdfdfd; padding: 25px; border-left: 5px solid #007bff; border-radius: 10px; margin-bottom: 25px; }
    .security-info { color: #666; font-size: 12px; font-weight: bold; margin-top: 10px; text-align: center; border: 1px dashed #ccc; padding: 8px; border-radius: 8px; background: #fafafa; }
    
    /* Style Card Paket */
    .package-card { 
        background: white; 
        padding: 30px 20px; 
        border-radius: 20px; 
        border: 1px solid #eef2f6; 
        text-align: center; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
        height: 580px;
    }
    .package-card:hover { transform: translateY(-10px); border-color: #007bff; }
    .feature-list { text-align: left; font-size: 13px; color: #555; margin-top: 15px; height: 250px; }
    .price-tag { font-size: 24px; font-weight: bold; color: #007bff; margin: 15px 0; }
    
    /* Style Invoice */
    .invoice-output { 
        background: #f1f3f5; 
        padding: 25px; 
        border-left: 10px solid #007bff; 
        border-radius: 5px; 
        font-family: 'Courier New', Courier, monospace; 
        white-space: pre-wrap;
        font-size: 14px;
        line-height: 1.4;
    }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● System Online & Secured</p>', unsafe_allow_html=True)
    
    menu = st.radio("Navigasi Utama:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 📦 Paket Layanan", "4. 📝 Registrasi & Invoice", "5. 🔐 Admin & Audit AI"])
    st.write("---")
    
    st.markdown("### Support Center")
    st.link_button("💬 Chat Customer Service", "https://wa.me/628212190885")
    st.markdown('<div class="security-info">🔐 End-to-End Encrypted System</div>', unsafe_allow_html=True)

# --- FOLDER 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.markdown(f"""<div class="profile-box">
        <b>Bapak Erwin Sinaga</b> merupakan seorang Pemimpin Bisnis Senior (Senior Business Leader) dengan rekam jejak profesional lebih dari sepuluh tahun di industri perbankan dan manajemen aset nasional. Sepanjang kariernya, beliau telah menduduki berbagai posisi strategis sebagai Chief Executive Officer (CEO) dan Chief Sales Officer (CSO), di mana fokus utama beliau adalah pada mitigasi risiko, efisiensi operasional, serta perlindungan aset dalam skala korporasi besar. Pengalaman mendalam ini memberikan beliau wawasan tajam mengenai celah-celah sistem konvensional yang sering kali menjadi pintu masuk bagi inefisiensi finansial dan tindakan kecurangan (fraud). <br><br>
        V-Guard AI lahir dari visi besar Bapak Erwin untuk menghadirkan teknologi pengawasan berbasis Artificial Intelligence yang otonom dan presisi. Beliau percaya bahwa keamanan aset adalah fondasi utama dari pertumbuhan bisnis yang sehat. Oleh karena itu, beliau berkomitmen untuk menyediakan solusi audit cerdas yang bekerja 24/7 demi memastikan setiap transaksi dan aktivitas bisnis berjalan sesuai koridor integritas. <br><br>
        Di bawah kepemimpinan beliau, V-Guard AI bertransformasi menjadi mitra strategis bagi para pengusaha di Indonesia untuk mengamankan operasional mereka secara digital. Dengan dedikasi tinggi terhadap transparansi dan akurasi, Bapak Erwin Sinaga terus mengawal setiap inovasi produk demi memberikan ketenangan pikiran (peace of mind) bagi para mitra bisnis dalam menjaga aset paling berharga mereka.
        </div>""", unsafe_allow_html=True)

# --- FOLDER 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Analisis Strategis & ROI")
    st.markdown("""<div class="vision-box">
        <h3>Visi</h3>
        <p>Menjadi benteng pertahanan digital terpercaya di Indonesia melalui inovasi AI yang menjamin transparansi operasional total.</p>
        <h3>Misi</h3>
        <ul>
            <li>Mengintegrasikan deteksi fraud cerdas ke dalam sistem operasional UMKM hingga Korporasi.</li>
            <li>Memberikan laporan audit otomatis yang akurat dan tidak dapat dimanipulasi.</li>
            <li>Memaksimalkan profitabilitas mitra dengan mengeliminasi kebocoran aset secara sistemik.</li>
        </ul>
    </div>""", unsafe_allow_html=True)
    st.write("---")
    st.subheader("📊 Simulasi Pengembalian Investasi (ROI)")
    omzet = st.number_input("Input Omzet Bulanan (Rp):", value=500000000, step=10000000)
    st.success(f"🛡️ Estimasi Kebocoran yang Dicegah: **Rp {omzet * 0.045:,.0f}** / bulan.")

# --- FOLDER 3: PAKET LAYANAN (VISUAL BEAUTIFICATION) ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Layanan Unggulan V-Guard AI")
    p_cols = st.columns(4)
    pkgs = [
        {"n": "BASIC", "p": "2.5jt", "m": "750rb", "f": ["✅ Audit Harian Dasar", "✅ Laporan Mingguan", "✅ Notifikasi E-mail", "✅ Support Chat"]},
        {"n": "MEDIUM", "p": "7.5jt", "m": "1.5jt", "f": ["✅ Semua Fitur BASIC", "✅ AI CCTV Integration", "✅ Deteksi Antrean", "✅ Laporan Harian"]},
        {"n": "ENTERPRISE", "p": "25jt", "m": "5jt", "f": ["✅ Semua Fitur MEDIUM", "✅ Multi-Branch Sync", "✅ AI Fraud Analytics", "✅ Dashboard Pemilik"]},
        {"n": "CORPORATE", "p": "50jt", "m": "10jt", "f": ["✅ Semua Fitur ENTERPRISE", "✅ Custom AI Model", "✅ 24/7 Priority Call", "✅ On-site Training"]}
    ]
    for i, p in enumerate(pkgs):
        with p_cols[i]:
            f_html = "".join([f"<p>{item}</p>" for item in p['f']])
            st.markdown(f"""
            <div class="package-card">
                <h3>{p['n']}</h3>
                <div class="price-tag">{p['p']}</div>
                <p style="font-size:12px; color:#999;">Setup Fee</p>
                <hr>
                <div class="feature-list">{f_html}</div>
                <p style="font-size:12px;">Maint: {p['m']}/bln</p>
            </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Pilih {p['n']}", f"https://wa.me/628212190885?text=Minat%20Paket%20{p['n']}")

# --- FOLDER 4: REGISTRASI & OTOMATISASI INVOICE ---
elif menu == "4. 📝 Registrasi & Invoice":
    st.header("📝 Registrasi Klien & Generate Invoice")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        n_pel = c1.text_input("Nama Pelanggan (PIC):")
        n_bis = c1.text_input("Nama Bisnis/Perusahaan:")
        p_pil = c2.selectbox("Pilih Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h_pen = c2.text_input("Harga Penawaran (Rp):", value="2.500.000")
        
        btn_reg = st.form_submit_button("Simpan Data & Generate Invoice")
        
        if btn_reg:
            if n_pel and n_bis:
                st.session_state.db_nasabah.append({
                    "Waktu": datetime.now().strftime("%Y-%m-%d"), 
                    "Pelanggan": n_pel, "Bisnis": n_bis, 
                    "Paket": p_pil, "Harga": h_pen, "Status": "🔴 Menunggu"
                })
                st.success("✅ Data berhasil disimpan!")
                
                # --- FITUR OTOMATISASI INVOICE ---
                st.markdown("### 📄 Invoice Professional (Siap Copy)")
                invoice_text = f"""
