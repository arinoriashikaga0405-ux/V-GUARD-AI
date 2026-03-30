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

# 2. CSS CUSTOM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; margin-top: 5px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; font-size: 16px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 8px rgba(0,0,0,0.02); }
    .vision-box { background: #fdfdfd; padding: 25px; border-left: 5px solid #007bff; border-radius: 10px; margin-bottom: 25px; }
    .security-info { color: #666; font-size: 12px; font-weight: bold; margin-top: 10px; text-align: center; border: 1px dashed #ccc; padding: 8px; border-radius: 8px; background: #fafafa; }
    .package-card { background: white; padding: 30px 20px; border-radius: 20px; border: 1px solid #eef2f6; text-align: center; box-shadow: 0 10px 20px rgba(0,0,0,0.05); height: 550px; }
    .feature-list { text-align: left; font-size: 13px; color: #555; margin-top: 15px; height: 220px; }
    .price-tag { font-size: 24px; font-weight: bold; color: #007bff; margin: 15px 0; }
    .invoice-output { background: #f1f3f5; padding: 25px; border-left: 10px solid #007bff; border-radius: 5px; font-family: monospace; white-space: pre-wrap; font-size: 14px; }
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
    st.link_button("💬 Chat Customer Service", "https://wa.me/628212190885")
    st.markdown('<div class="security-info">🔐 End-to-End Encrypted System</div>', unsafe_allow_html=True)

# --- FOLDER 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.markdown("""<div class="profile-box">
        <b>Bapak Erwin Sinaga</b> merupakan seorang Pemimpin Bisnis Senior (Senior Business Leader) dengan rekam jejak profesional lebih dari sepuluh tahun di industri perbankan dan manajemen aset nasional. Sepanjang kariernya, beliau telah menduduki berbagai posisi strategis sebagai Chief Executive Officer (CEO) dan Chief Sales Officer (CSO), di mana fokus utama beliau adalah pada mitigasi risiko, efisiensi operasional, serta perlindungan aset dalam skala korporasi besar. Pengalaman mendalam ini memberikan beliau wawasan tajam mengenai celah-celah sistem konvensional yang sering kali menjadi pintu masuk bagi inefisiensi finansial dan tindakan kecurangan (fraud). <br><br>
        V-Guard AI lahir dari visi besar Bapak Erwin untuk menghadirkan teknologi pengawasan berbasis Artificial Intelligence yang otonom dan presisi. Beliau percaya bahwa keamanan aset adalah fondasi utama dari pertumbuhan bisnis yang sehat. Oleh karena itu, beliau berkomitmen untuk menyediakan solusi audit cerdas yang bekerja 24/7 demi memastikan setiap transaksi dan aktivitas bisnis berjalan sesuai koridor integritas. <br><br>
        Di bawah kepemimpinan beliau, V-Guard AI bertransformasi menjadi mitra strategis bagi para pengusaha di Indonesia untuk mengamankan operasional mereka secara digital. Dengan dedikasi tinggi terhadap transparansi dan akurasi, Bapak Erwin Sinaga terus mengawal setiap inovasi produk demi memberikan ketenangan pikiran (peace of mind) bagi para mitra bisnis dalam menjaga aset paling berharga mereka.
        </div>""", unsafe_allow_html=True)

# --- FOLDER 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Analisis Strategis & ROI")
    st.markdown("""<div class="vision-box">
        <h3>Visi</h3><p>Menjadi benteng pertahanan digital terpercaya di Indonesia melalui inovasi AI yang menjamin transparansi operasional total.</p>
        <h3>Misi</h3><ul><li>Mengintegrasikan deteksi fraud cerdas ke operasional bisnis.</li><li>Memberikan laporan audit otomatis yang akurat.</li><li>Memaksimalkan profitabilitas mitra dengan eliminasi kebocoran aset.</li></ul>
    </div>""", unsafe_allow_html=True)
    st.write("---")
    omzet = st.number_input("Input Omzet Bulanan (Rp):", value=500000000)
    st.success(f"🛡️ Estimasi Kebocoran yang Dicegah: **Rp {omzet * 0.045:,.0f}** / bulan.")

# --- FOLDER 3: PAKET LAYANAN ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Layanan V-Guard AI")
    p_cols = st.columns(4)
    pkgs = [
        {"n": "BASIC", "p": "2.5jt", "f": ["✅ Audit Dasar", "✅ Laporan Mingguan", "✅ Support Chat"]},
        {"n": "MEDIUM", "p": "7.5jt", "f": ["✅ Fitur BASIC", "✅ AI CCTV Integration", "✅ Deteksi Antrean"]},
        {"n": "ENTERPRISE", "p": "25jt", "f": ["✅ Fitur MEDIUM", "✅ Multi-Branch Sync", "✅ AI Fraud Analytics"]},
        {"n": "CORPORATE", "p": "50jt", "f": ["✅ Fitur ENTERPRISE", "✅ Custom AI Model", "✅ 24/7 Priority"]}
    ]
    for i, p in enumerate(pkgs):
        with p_cols[i]:
            f_html = "".join([f"<p>{item}</p>" for item in p['f']])
            st.markdown(f'<div class="package-card"><h3>{p["n"]}</h3><div class="price-tag">{p["p"]}</div><hr><div class="feature-list">{f_html}</div></div>', unsafe_allow_html=True)
            st.link_button(f"Pilih {p['n']}", "https://wa.me/628212190885")

# --- FOLDER 4: REGISTRASI & INVOICE ---
elif menu == "4. 📝 Registrasi & Invoice":
    st.header("📝 Registrasi & Generate Invoice")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        n_pel = c1.text_input("Nama Pelanggan (PIC):")
        n_bis = c1.text_input("Nama Bisnis:")
        p_pil = c2.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h_pen = c2.text_input("Harga Penawaran (Rp):", value="2.500.000")
        btn_reg = st.form_submit_button("Simpan & Buat Invoice")
        
        if btn_reg and n_pel:
            st.session_state.db_nasabah.append({"Waktu": datetime.now().strftime("%Y-%m-%d"), "Pelanggan": n_pel, "Bisnis": n_bis, "Paket": p_pil, "Harga": h_pen, "Status": "🔴 Menunggu"})
            st.success("✅ Data Tersimpan!")
            
            # Invoice dibuat tanpa f-string rumit agar tidak error
            inv_header = f"NOMOR: INV/VG-AI/{datetime.now().strftime('%Y%m%d')}\n"
            inv_body = f"Kepada Yth. {n_pel} ({n_bis})\n\nDetail Paket: {p_pil}\nNilai Investasi: Rp {h_pen},-\n\nSalam, Erwin Sinaga (V-Guard AI)"
            st.markdown(f'<div class="invoice-output">{inv_header}{inv_body}</div>', unsafe_allow_html=True)

# --- FOLDER 5: ADMIN & AUDIT ---
elif menu == "5. 🔐 Admin & Audit AI":
    st.header("🔐 Admin Dashboard")
    pw = st.text_input("Password:", type="password")
    if pw == "w1nbju8282":
        st.table(pd.DataFrame(st.session_state.db_nasabah))
        st.line_chart(np.random.randn(20, 2))

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
