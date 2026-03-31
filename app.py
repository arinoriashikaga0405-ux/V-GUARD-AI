import streamlit as st
import os
import pandas as pd
import numpy as np
from datetime import datetime
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database (Session State agar data tidak hilang saat refresh di satu sesi)
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"Waktu": "2026-04-01", "Pelanggan": "Admin System", "Bisnis": "V-Guard Core", "Paket": "CORPORATE", "Harga": 50000000, "Status": "🟢 AKTIF"}
    ]

# 2. CSS CUSTOM PREMIUM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; margin-top: 5px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; font-size: 16px; border: 1px solid #f0f0f0; box-shadow: 2px 2px 8px rgba(0,0,0,0.02); }
    .vision-box { background: #fdfdfd; padding: 25px; border-left: 5px solid #007bff; border-radius: 10px; margin-bottom: 25px; }
    .security-info { color: #666; font-size: 12px; font-weight: bold; margin-top: 10px; text-align: center; border: 1px dashed #ccc; padding: 8px; border-radius: 8px; background: #fafafa; }
    .package-card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #eee; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 300px; }
    .invoice-output { background: #f8f9fa; padding: 20px; border-left: 8px solid #28a745; border-radius: 5px; font-family: monospace; white-space: pre-wrap; font-size: 14px; margin-top: 15px; }
    .stat-card { background: linear-gradient(135deg, #007bff 0%, #0056b3 100%); color: white; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (PENGEMBALIAN NAVIGASI LENGKAP)
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● System Online</p>', unsafe_allow_html=True)
    
    menu = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi & ROI", 
        "3. 📦 Paket Produk", 
        "4. 📝 Registrasi & Invoice", 
        "5. 🔐 Admin Dashboard"
    ])
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
    st.markdown("""<div class="vision-box">
        <h3>Visi</h3><p>Menjamin transparansi operasional total melalui inovasi AI.</p>
        <h3>Misi</h3><ul><li>Deteksi fraud real-time.</li><li>Audit otomatis transparan.</li><li>Eliminasi kebocoran aset bisnis.</li></ul>
    </div>""", unsafe_allow_html=True)
    omzet = st.number_input("Input Omzet Bulanan Bisnis (Rp):", value=500000000)
    st.success(f"🛡️ Estimasi Kebocoran yang Dicegah: **Rp {omzet * 0.045:,.0f}** / bulan.")

# --- FOLDER 3: PAKET PRODUK (DIKEMBALIKAN) ---
elif menu == "3. 📦 Paket Produk":
    st.header("📦 Pilihan Paket V-Guard AI")
    p_cols = st.columns(4)
    pkgs = [
        {"n": "BASIC", "p": "2.5jt", "f": "Audit Harian & Laporan Mingguan"},
        {"n": "MEDIUM", "p": "7.5jt", "f": "AI CCTV & Deteksi Antrean"},
        {"n": "ENTERPRISE", "p": "25jt", "f": "Multi-Branch & AI Fraud Analytics"},
        {"n": "CORPORATE", "p": "50jt", "f": "Custom AI Model & 24/7 Support"}
    ]
    for i, p in enumerate(pkgs):
        with p_cols[i]:
            st.markdown(f"""<div class="package-card">
                <h3>{p['n']}</h3>
                <h2 style="color:#007bff;">{p['p']}</h2>
                <hr><p>{p['f']}</p>
            </div>""", unsafe_allow_html=True)
            st.link_button(f"Pilih {p['n']}", f"https://wa.me/628212190885?text=Saya%20minat%20paket%20{p['n']}")

# --- FOLDER 4: REGISTRASI & INVOICE ---
elif menu == "4. 📝 Registrasi & Invoice":
    st.header("📝 Registrasi & Penawaran Klien")
    with st.form("reg_form"):
        c1, c2 = st.columns(2)
        n_pel = c1.text_input("Nama Pelanggan (PIC):")
        n_bis = c1.text_input("Nama Bisnis/Perusahaan:")
        p_pil = c2.selectbox("Pilih Paket Produk:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        h_pen = c2.number_input("Harga Penawaran Disepakati (Rp):", value=2500000)
        wa_no = c2.text_input("No. WhatsApp Klien (Contoh: 62812...):")
        
        btn_reg = st.form_submit_button("Simpan & Generate Invoice")
        
        if btn_reg and n_pel:
            st.session_state.db_nasabah.append({
                "Waktu": datetime.now().strftime("%Y-%m-%d"), 
                "Pelanggan": n_pel, "Bisnis": n_bis, 
                "Paket": p_pil, "Harga": h_pen, "Status": "🔴 Menunggu"
            })
            st.success("✅ Data Tersimpan di Database Admin!")
            
            # Pesan WA dengan Rekening Bapak
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

Mohon konfirmasi bukti transfer untuk aktivasi. 
Salam, Erwin Sinaga (Founder)."""
            
            st.markdown(f'<div class="invoice-output">{inv_msg}</div>', unsafe_allow_html=True)
            wa_encoded = urllib.parse.quote(inv_msg)
            st.link_button("🚀 KIRIM KE WHATSAPP KLIEN", f"https://wa.me/{wa_no}?text={wa_encoded}")

# --- FOLDER 5: ADMIN DASHBOARD (DIKEMBALIKAN) ---
elif menu == "5. 🔐 Admin Dashboard":
    st.header("🔐 Admin Intelligence Control")
    pw = st.text_input("Masukkan Sandi Admin:", type="password")
    if pw == "w1nbju8282":
        df = pd.DataFrame(st.session_state.db_nasabah)
        
        # Statistik Penyelamatan Aset
        total_aset = df['Harga'].sum() * 10
        st.markdown(f"""<div class="stat-card">
            <p style="margin:0;">ESTIMASI TOTAL ASET TERLINDUNGI</p>
            <h1 style="margin:0;">Rp {total_aset:,.0f}</h1>
        </div>""", unsafe_allow_html=True)
        
        st.subheader("📋 Daftar Nasabah Terdaftar")
        st.table(df)
        st.line_chart(np.random.randn(10, 2))
    elif pw != "":
        st.error("Sandi Salah!")

# 4. FOOTER
st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Intelligence by Erwin Sinaga</div>', unsafe_allow_html=True)
