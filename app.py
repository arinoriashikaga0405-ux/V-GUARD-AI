import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database Sederhana
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = []

# 2. CSS CUSTOM UNTUK TAMPILAN PREMIUM
st.markdown("""
<style>
    .main { background-color: #f5f7f9; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .package-card { 
        background: white; padding: 25px; border-radius: 15px; border: 1px solid #e0e0e0; 
        height: 600px; transition: transform 0.3s; box-shadow: 2px 2px 12px rgba(0,0,0,0.05);
    }
    .package-card:hover { transform: translateY(-5px); border-color: #007bff; }
    .profile-box { text-align: justify; line-height: 1.8; padding: 20px; background: white; border-radius: 15px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    # Menampilkan Foto Founder
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.image("https://www.w3schools.com/howto/img_avatar.png", caption="Foto Founder", use_container_width=True)
    
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Folder Navigasi:", 
                    ["1. 👤 Profil Founder", 
                     "2. 🎯 Visi, Misi & ROI", 
                     "3. 📦 Paket Layanan", 
                     "4. 📝 Registrasi Klien",
                     "5. 🔐 Admin Dashboard"])
    st.write("---")
    st.link_button("📞 Hubungi Erwin Sinaga", "https://wa.me/628212190885")

# --- FOLDER 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("👤 Strategic Leadership")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.subheader("Erwin Sinaga")
        st.markdown("""<div class="profile-box">
        Bapak Erwin Sinaga adalah seorang profesional dan Pemimpin Bisnis Senior dengan pengalaman lebih dari sepuluh tahun di industri perbankan serta manajemen aset nasional. 
        Keahlian beliau mencakup manajemen risiko strategis, kepatuhan operasional (compliance), hingga pengawasan aset korporasi yang sangat kompleks. 
        V-Guard AI lahir dari visi beliau untuk membawa standar keamanan audit perbankan yang ketat ke ekosistem bisnis UMKM dan perusahaan menengah di Indonesia. 
        Beliau meyakini bahwa teknologi AI adalah solusi mutlak untuk menutup celah kebocoran finansial dan memastikan transparansi aset bagi pemilik bisnis.
        </div>""", unsafe_allow_html=True)

# --- FOLDER 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Analisis Strategi V-Guard")
    v1, v2 = st.columns(2)
    with v1:
        st.info("### 🎯 Visi 2026\nMenjadi standar utama keamanan audit berbasis AI di seluruh ekosistem bisnis Indonesia.")
    with v2:
        st.success("### 🚀 Misi Utama\n1. Otomasi Audit 24/7 secara presisi.\n2. Deteksi Fraud Instan sebelum kerugian meluas.\n3. Transparansi Aset Mutlak bagi pemilik bisnis.\n4. Integrasi Teknologi AI untuk efisiensi.")
    
    st.write("---")
    st.subheader("📈 Analisis ROI (Penyelamatan Aset)")
    omzet = st.number_input("Input Omzet Bulanan (Rp):", value=500000000, step=10000000)
    leakage = omzet * 0.05
    st.error(f"🚨 Estimasi Kebocoran (5%): Rp {leakage:,.0f}")
    st.success(f"🛡️ Target Penyelamatan V-Guard (90%): Rp {leakage * 0.9:,.0f}")

# --- FOLDER 3: PAKET LAYANAN (CUSTOM DESIGN) ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Layanan Premium")
    p_cols = st.columns(4)
    pkgs = [
        {"n": "BASIC", "s": "2.5jt", "m": "750rb", "c": "#f8f9fa", "f": ["Audit Harian", "Laporan Mingguan", "Standard Fraud Alarm (Email)"]},
        {"n": "MEDIUM", "s": "7.5jt", "m": "1.5jt", "c": "#e3f2fd", "f": ["Semua Fitur BASIC", "AI CCTV Integration", "Instant Fraud Alarm (WA)", "Monthly Trend Analysis"]},
        {"n": "ENTERPRISE", "s": "25jt", "m": "5jt", "c": "#e8f5e9", "f": ["Semua Fitur MEDIUM", "Multi-Branch Dashboard", "Advanced AI Fraud Alarm", "Dedicated Cloud Server"]},
        {"n": "CORPORATE", "s": "50jt", "m": "10jt", "c": "#fff3e0", "f": ["Semua Fitur ENTERPRISE", "Custom AI Model", "Real-time Sirene Alarm", "Audit On-site Bulanan"]}
    ]
    
    for i, p in enumerate(pkgs):
        with p_cols[i]:
            st.markdown(f"""<div class="package-card" style="background-color: {p['c']};">
                <h3 style="text-align:center;">{p['n']}</h3>
                <p style="text-align:center;">Setup: <b>{p['s']}</b><br>Bulanan: <b>{p['m']}</b></p><hr>
                <ul style="font-size: 14px;">{''.join([f'<li>{item}</li>' for item in p['f']])}</ul>
            </div>""", unsafe_allow_html=True)
            wa_link = f"https://wa.me/628212190885?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20{p['n']}"
            st.link_button(f"Pilih Paket {p['n']}", wa_link, use_container_width=True)

# --- FOLDER 4: REGISTRASI ---
elif menu == "4. 📝 Registrasi Klien":
    st.header("📝 Registrasi Nasabah Baru")
    with st.form("form_reg"):
        nama = st.text_input("Nama Bisnis/Toko:")
        bidang = st.selectbox("Bidang Usaha:", ["Retail", "F&B", "Distribusi", "Jasa", "Lainnya"])
        harga = st.text_input("Harga Kesepakatan (Rp):")
        paket = st.selectbox("Paket Dipilih:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        if st.form_submit_button("Kirim Pendaftaran"):
            st.session_state.db_nasabah.append({"Waktu": datetime.now(), "Nama": nama, "Paket": paket, "Harga": harga, "Status": "Menunggu"})
            st.success("✅ Data terkirim! Admin akan segera memproses.")

# --- FOLDER 5: ADMIN DASHBOARD (FITUR HASIL AUDIT) ---
elif menu == "5. 🔐 Admin Dashboard":
    st.header("🔐 Intelligence Center Admin")
    pw = st.text_input("Password Admin:", type="password")
    if pw == "w1nbju8282":
        t1, t2, t3 = st.tabs(["📊 Database Klien", "📤 Kelola Transaksi", "📝 Hasil Audit AI"])
        
        with t1:
            st.subheader("Daftar Nasabah")
            if st.session_state.db_nasabah: st.table(pd.DataFrame(st.session_state.db_nasabah))
            else: st.info("Belum ada nasabah terdaftar.")
            
        with t2:
            st.subheader("Upload Data Transaksi Masuk")
            st.file_uploader("Upload File Nota/CSV Nasabah", type=["csv", "xlsx"])
            st.button("Tarik Laporan Mentah")
            
        with t3:
            st.subheader("📤 Kirim Hasil Audit AI")
            st.write("Gunakan bagian ini untuk mengirimkan hasil analisa akhir ke nasabah.")
            nasabah_target = st.selectbox("Pilih Nasabah:", ["Toko Jaya", "Sentosa Corp", "Nasabah Baru"])
            file_audit = st.file_uploader("Upload Hasil Audit Final (.pdf/.xlsx)", key="audit_up")
            if st.button("Kirim Hasil Audit"):
                st.success(f"Berhasil mengirimkan hasil audit ke {nasabah_target}")

# 4. FOOTER
st.markdown('<div class="footer">© 2026 V-Guard AI Systems - Secured by Advanced Intelligence</div>', unsafe_allow_html=True)
