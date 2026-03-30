import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. SETUP & STYLE
st.set_page_config(page_title="V-Guard AI Systems", layout="wide")
st.markdown("""<style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #f8f9fa; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 9999; }
    .package-box { padding: 20px; border: 1px solid #eee; border-radius: 10px; background: #fff; height: 650px; }
    .profile-text { text-align: justify; line-height: 1.8; font-size: 16px; }
</style>""", unsafe_allow_html=True)

# 2. SIDEBAR
with st.sidebar:
    # Logika Foto: Cek file lokal, jika tidak ada gunakan link gambar online sementara
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.image("https://www.w3schools.com/howto/img_avatar.png", caption="Foto Founder (erwin.jpg tidak ditemukan)", use_container_width=True)
        
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Folder:", ["1. 👤 Profil Founder", "2. 🎯 Visi & Misi", "3. 📦 Paket", "4. 📝 Registrasi", "5. 🔐 Admin"])
    st.write("---")
    st.link_button("📞 Layanan Pelanggan (WA)", "https://wa.me/628212190885")

# 3. FOLDER 1: PROFIL FOUNDER (>100 KATA)
if menu == "1. 👤 Profil Founder":
    st.header("👤 Profil Founder: Erwin Sinaga")
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
        else:
            st.markdown("### [Foto Erwin Sinaga]")
    with col2:
        st.markdown("""<div class="profile-text">
        Bapak Erwin Sinaga merupakan seorang profesional dan Pemimpin Bisnis Senior yang telah mendedikasikan lebih dari sepuluh tahun kariernya dalam industri perbankan serta manajemen aset nasional. Melalui perjalanan panjang di sektor keuangan formal, beliau telah membangun keahlian mendalam dalam manajemen risiko strategis, kepatuhan operasional (compliance), hingga pengawasan aset korporasi yang sangat kompleks. Pengalaman ini membentuk pemahaman beliau bahwa celah kecurangan atau fraud sering kali muncul dari kelemahan sistem pengawasan manual yang tidak mampu bekerja secara real-time. <br><br>
        V-Guard AI didirikan berdasarkan visi besar Bapak Erwin Sinaga untuk membawa standar keamanan audit perbankan yang sangat ketat ke dalam ekosistem bisnis UMKM dan perusahaan menengah di Indonesia. Beliau sangat meyakini bahwa pemanfaatan teknologi Artificial Intelligence adalah solusi mutlak untuk menutup celah kebocoran finansial dan memastikan transparansi aset bagi para pemilik bisnis. Melalui V-Guard AI, beliau berkomitmen untuk menyediakan benteng pertahanan digital cerdas yang mampu melakukan deteksi dini terhadap setiap anomali transaksi, sehingga setiap rupiah aset milik klien dapat terlindungi dengan akurasi maksimal dan sistem alarm otomatis yang responsif.
        </div>""", unsafe_allow_html=True)

# 4. FOLDER 2: VISI, MISI & ROI
elif menu == "2. 🎯 Visi & Misi":
    st.header("🎯 Strategi & Analisis ROI")
    c1, c2 = st.columns(2)
    with c1:
        st.info("### 🎯 Visi 2026\nMenjadi standar utama keamanan audit berbasis AI di seluruh ekosistem bisnis Indonesia.")
    with c2:
        st.success("### 🚀 Misi Utama\n1. Otomasi Audit 24/7 secara presisi.\n2. Deteksi Fraud Instan sebelum kerugian meluas.\n3. Transparansi Aset Mutlak bagi pemilik bisnis.\n4. Integrasi Teknologi AI untuk efisiensi operasional.")
    
    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Aset (ROI)")
    omzet = st.number_input("Input Omzet Bulanan Bisnis (Rp):", value=500000000, step=10000000)
    leakage = omzet * 0.05
    st.error(f"🚨 Estimasi Kebocoran (5%): Rp {leakage:,.0f}")
    st.success(f"🛡️ Target Penyelamatan (90%): Rp {leakage * 0.9:,.0f}")

# 5. FOLDER 3: PAKET LAYANAN
elif menu == "3. 📦 Paket":
    st.header("📦 Paket Layanan V-Guard AI")
    cols = st.columns(4)
    pkgs = [
        ("BASIC", "2.5jt", "750rb", ["Audit Harian", "Laporan Mingguan", "Standard Fraud Alarm (Email)"]),
        ("MEDIUM", "7.5jt", "1.5jt", ["Semua Fitur BASIC", "AI CCTV Integration", "Instant Fraud Alarm (WA)", "Monthly Trend Analysis"]),
        ("ENTERPRISE", "25jt", "5jt", ["Semua Fitur MEDIUM", "Multi-Branch Dashboard", "Advanced AI Fraud Alarm", "Dedicated Cloud Server"]),
        ("CORPORATE", "50jt", "10jt", ["Semua Fitur ENTERPRISE", "Custom AI Model", "Real-time Sirene Alarm", "Audit On-site Bulanan", "Priority 24/7 Support"])
    ]
    for i, (n, s, m, f) in enumerate(pkgs):
        with cols[i]:
            st.markdown(f"""<div class='package-box'>
                <h3 style='text-align:center;'>{n}</h3>
                <p><b>Setup:</b> {s}<br><b>Bulanan:</b> {m}</p><hr>
                <ul>{"".join([f"<li>{item}</li>" for item in f])}</ul>
            </div>""", unsafe_allow_html=True)

# 6. FOLDER 4: REGISTRASI
elif menu == "4. 📝 Registrasi":
    st.header("📝 Registrasi Nasabah Baru")
    with st.form("reg"):
        st.text_input("Nama Bisnis:")
        st.selectbox("Jenis Usaha:", ["Retail", "F&B", "Jasa", "Corporate"])
        st.text_input("Harga (Sesuai Paket):")
        st.selectbox("Pilih Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        if st.form_submit_button("Kirim Data Pendaftaran"):
            st.success("✅ Berhasil! Data terkirim ke Admin.")

# 7. FOLDER 5: ADMIN
elif menu == "5. 🔐 Admin":
    st.header("🔐 Intelligence Center Admin")
    pw = st.text_input("Password Admin:", type="password")
    if pw == "w1nbju8282":
        t1, t2 = st.tabs(["📊 Database Klien", "📤 Kelola Data Transaksi"])
        with t1: 
            st.write("Daftar Nasabah Aktif")
            st.table(pd.DataFrame({"Nama": ["Toko Jaya", "Sentosa Corp"], "Paket": ["BASIC", "CORP"], "Status": ["Aktif", "Aktif"]})) #
        with t2:
            st.file_uploader("Upload Laporan Transaksi (.csv/.xlsx)") #
            st.button("Tarik Laporan Audit Terakhir")

# 8. FOOTER
st.markdown('<div class="footer">© 2026 V-Guard AI Systems - Secured by Advanced Intelligence</div>', unsafe_allow_html=True)
