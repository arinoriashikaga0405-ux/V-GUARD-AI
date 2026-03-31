import streamlit as st
import os
import pandas as pd
import numpy as np
from datetime import datetime
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"Waktu": "2026-03-31", "Pelanggan": "Admin", "Bisnis": "V-Guard Core", "Paket": "CORPORATE", "Harga": 50000000, "Status": "🟢 AKTIF"}
    ]

# 2. CSS CUSTOM PREMIUM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; margin-top: 5px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; font-size: 16px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 8px rgba(0,0,0,0.02); }
    .security-info { color: #666; font-size: 12px; font-weight: bold; margin-top: 10px; text-align: center; border: 1px dashed #ccc; padding: 8px; border-radius: 8px; background: #fafafa; }
    .invoice-output { background: #f8f9fa; padding: 20px; border-left: 8px solid #007bff; border-radius: 5px; font-family: monospace; white-space: pre-wrap; font-size: 14px; margin-top: 15px; }
    .stat-card { background: linear-gradient(135deg, #007bff 0%, #0056b3 100%); color: white; padding: 25px; border-radius: 15px; text-align: center; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,123,255,0.3); }
    .package-item { background: #fff; padding: 15px; border-radius: 10px; border: 1px solid #eee; margin-bottom: 10px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● Intelligence Active</p>', unsafe_allow_html=True)
    menu = st.radio("Navigasi Utama:", ["1. 👤 Profil Founder", "2. 🎯 Visi & ROI", "3. 📦 Paket Layanan", "4. 📝 Registrasi & Invoice", "5. 🔐 Admin Dashboard"])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")
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

# --- FOLDER 2: VISI & ROI ---
elif menu == "2. 🎯 Visi & ROI":
    st.header("🎯 Analisis Strategis & ROI")
    st.info("Visi: Menjamin transparansi operasional total melalui inovasi AI.")
    omzet = st.number_input("Input Omzet Bulanan Bisnis (Rp):", value=500000000)
    st.success(f"🛡️ Potensi Penyelamatan Aset: **Rp {omzet * 0.045:,.0f}** / bulan.")

# --- FOLDER 3: PAKET LAYANAN ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Layanan V-Guard AI")
    p_cols = st.columns(4)
    pkgs = [("BASIC", "2.5jt"), ("MEDIUM", "7.5jt"), ("ENTERPRISE", "25jt"), ("CORPORATE", "50jt")]
    for i, p in enumerate(pkgs):
        with p_cols[i]:
            st.markdown(f'<div class="package-item"><h3>{p[0]}</h3><p>Investasi:<br><b>{p[1]}</b></p></div>', unsafe_allow_html=True)
            st.write("✅ AI Audit\n✅ Deteksi Fraud")

# --- FOLDER 4: REGISTRASI & INVOICE (REKENING BCA ERWIN SINAGA) ---
elif menu == "4. 📝 Registrasi & Invoice":
    st.header("📝 Registrasi & Penawaran Klien")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        n_pel = c1.text_input("Nama Pelanggan (PIC):")
        n_bis = c1.text_input("Nama Bisnis:")
        p_pil = c2.selectbox("Pilih Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h_pen = c2.number_input("Harga Penawaran (Rp):", value=2500000)
        wa_no = c2.text_input("No. WA Klien (Gunakan 62...):")
        btn_reg = st.form_submit_button("Simpan & Buat Invoice")
        
        if btn_reg and n_pel:
            st.session_state.db_nasabah.append({
                "Waktu": datetime.now().strftime("%Y-%m-%d"), 
                "Pelanggan": n_pel, "Bisnis": n_bis, 
                "Paket": p_pil, "Harga": h_pen, "Status": "🔴 Menunggu"
            })
            st.success("✅ Data Berhasil Disimpan!")
            
            # Invoice Formal dengan Rekening BCA Bapak
            inv_msg = f"""*INVOICE V-GUARD AI SYSTEMS*
            
Yth. {n_pel} ({n_bis}),

Berikut rincian biaya aktivasi sistem:
- Paket: {p_pil} Intelligence
- Nilai Investasi: Rp {h_pen:,.0f}

*INSTRUKSI PEMBAYARAN:*
Transfer ke Rekening Resmi Founder:
🏦 *Bank:* BCA
💳 *No. Rekening:* 3450074658
👤 *Atas Nama:* ERWIN SINAGA

Mohon lampirkan bukti transfer untuk aktivasi sistem.
Salam, Erwin Sinaga (Founder)."""
            
            st.markdown(f'<div class="invoice-output">{inv_msg}</div>', unsafe_allow_html=True)
            
            # Tombol Kirim WA Otomatis
            wa_encoded = urllib.parse.quote(inv_msg)
            st.link_button("🚀 KIRIM KE WHATSAPP KLIEN", f"https://wa.me/{wa_no}?text={wa_encoded}")

# --- FOLDER 5: ADMIN & TOTAL ASSET ---
elif menu == "5. 🔐 Admin Dashboard":
    st.header("🔐 Admin Intelligence Control")
    pw = st.text_input("Password Admin:", type="password")
    if pw == "w1nbju8282":
        df = pd.DataFrame(st.session_state.db_nasabah)
        
        # Dashboard Akumulasi Penyelamatan Aset
        total_terlindungi = df['Harga'].sum() * 15 
        st.markdown(f"""<div class="stat-card">
            <p style="margin:0; font-size:16px; opacity:0.8;">ESTIMASI TOTAL ASET TERLINDUNGI</p>
            <h1 style="margin:0; font-size:42px;">Rp {total_terlindungi:,.0f}</h1>
        </div>""", unsafe_allow_html=True)
        
        st.subheader("📋 Database Nasabah Terdaftar")
        st.table(df)
        st.line_chart(np.random.randn(10, 2))

# 4. FOOTER
st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
