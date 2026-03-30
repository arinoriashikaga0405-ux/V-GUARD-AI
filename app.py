import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI UTAMA
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# Inisialisasi Database (Session State)
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = []
if 'db_transaksi' not in st.session_state:
    st.session_state.db_transaksi = []

# 2. CSS CUSTOM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 18px; }
    .package-box { height: 580px; padding: 25px; border: 2px solid #f0f0f0; border-radius: 15px; background-color: #ffffff; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .footer-container { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #f8f9fa; text-align: center; padding: 15px 0px; font-weight: bold; border-top: 1px solid #dee2e6; z-index: 9999; }
    .stApp { margin-bottom: 100px; }
    .profile-text { text-align: justify; line-height: 1.8; font-size: 16px; }
</style>
""", unsafe_allow_html=True)

my_wa = "https://wa.me/628212190885"

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Folder Navigasi:", 
                    ["1. 👤 Profil Founder", 
                     "2. 🎯 Visi, Misi & ROI", 
                     "3. 📦 Produk & Paket", 
                     "4. 📝 Registrasi Klien",
                     "5. 🔐 Admin Dashboard"])
    st.markdown('<p class="status-connected">● System Online</p>', unsafe_allow_html=True)
    st.link_button("📞 Hubungi Erwin Sinaga", my_wa, use_container_width=True)

# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("👤 Strategic Leadership & Founder Philosophy")
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"): 
            st.image("erwin.jpg", use_container_width=True, caption="Erwin Sinaga")
    with col2:
        st.subheader("Erwin Sinaga")
        st.markdown(f"""<div class="profile-text">
        Bapak Erwin Sinaga adalah seorang profesional dan Pemimpin Bisnis Senior yang memiliki dedikasi tinggi selama lebih dari sepuluh tahun dalam dunia perbankan serta manajemen aset nasional. Melalui perjalanan karier yang panjang di sektor keuangan formal, beliau telah mengasah keahlian strategis dalam manajemen risiko kredit, pengawasan kepatuhan operasional (compliance), hingga perancangan sistem perlindungan aset korporasi skala besar. Pengalaman mendalam beliau dalam menangani struktur keuangan yang kompleks memberikan landasan kuat bagi pengembangan sistem keamanan audit berbasis teknologi tinggi.<br><br>
        Filosofi kepemimpinan beliau berakar pada integritas mutlak dan transparansi data, di mana beliau percaya bahwa setiap celah fraud dapat ditutup dengan sinergi antara ketelitian manusia dan kecanggihan teknologi digital. V-Guard AI lahir dari visi beliau untuk membawa standar keamanan audit perbankan yang sangat ketat ke dalam ekosistem bisnis UMKM dan perusahaan menengah. Beliau memandang bahwa Artificial Intelligence bukan sekadar alat otomatisasi, melainkan benteng pertahanan utama dalam menjaga keberlangsungan finansial klien. Dengan mengintegrasikan algoritma deteksi anomali secara real-time, Bapak Erwin berkomitmen untuk menciptakan lingkungan bisnis yang bersih dari kebocoran dana, memastikan setiap rupiah aset klien terlindungi secara holistik dan terukur di bawah pengawasan sistem yang cerdas dan jujur.
        </div>""", unsafe_allow_html=True)

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Analisis Strategi Bisnis")
    c1, c2 = st.columns(2)
    with c1:
        st.info("### 🎯 Visi 2026\nMenjadi standar utama keamanan audit berbasis AI di seluruh ekosistem bisnis Indonesia.")
    with c2:
        st.success("### 🚀 Misi Utama\n1. Otomasi Audit 24/7\n2. Deteksi Fraud Instan\n3. Transparansi Aset Mutlak")
    
    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Aset (ROI)")
    omzet = st.number_input("Input Omzet Bulanan Bisnis (Rp):", value=500000000, step=10000000)
    leakage = omzet * 0.05
    recovery = leakage * 0.9
    
    col_a, col_b = st.columns(2)
    col_a.error(f"🚨 Estimasi Kebocoran (5%): Rp {leakage:,.0f}")
    col_b.success(f"🛡️ Target Penyelamatan (90%): Rp {recovery:,.0f}")
    st.caption("Analisis ini didasarkan pada rata-rata kerugian operasional akibat fraud internal yang tidak terdeteksi.")

# --- MENU 3: PRODUK & PAKET ---
elif menu == "3. 📦 Produk & Paket":
    st.header("📦 Paket Layanan V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    
    packages = [
        {"name": "BASIC", "setup": "2.5jt", "monthly": "750rb", "features": ["Audit Transaksi Harian", "Laporan Mingguan", "Support Chat"]},
        {"name": "MEDIUM", "setup": "7.5jt", "monthly": "1.5jt", "features": ["AI CCTV Integration", "Deteksi Tren Fraud", "Alert System"]},
        {"name": "ENTERPRISE", "setup": "25jt", "monthly": "5jt", "features": ["Multi-Branch Dashboard", "Auto-Invoice Audit", "Dedicated Server"]},
        {"name": "CORPORATE", "setup": "50jt", "monthly": "10jt", "features": ["Custom AI Model", "On-Site Audit", "Priority 24/7 Support"]}
    ]
    
    cols = [c1, c2, c3, c4]
    for i, p in enumerate(packages):
        with cols[i]:
            st.markdown(f"""<div class="package-box">
                <h3 style="text-align:center;">{p['name']}</h3>
                <p><b>Pemasangan:</b> {p['setup']}<br><b>Bulanan:</b> {p['monthly']}</p><hr>
                <ul>{"".join([f"<li>{f}</li>" for f in p['features']])}</ul>
            </div>""", unsafe_allow_html=True)
            st.link_button(f"Pesan {p['name']}", my_wa, use_container_width=True)

# --- MENU 4: REGISTRASI KLIEN ---
elif menu == "4. 📝 Registrasi Klien":
    st.header("📝 Formulir Registrasi & Pengiriman Data")
    with st.form("reg_form"):
        st.subheader("Data Bisnis")
        n_bisnis = st.text_input("Nama Bisnis / Nasabah:")
        j_usaha = st.selectbox("Jenis Usaha:", ["Retail", "F&B / Restoran", "Jasa", "Distribusi", "Corporate"])
        p_pilihan = st.selectbox("Pilih Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        harga_pilih = st.text_input("Konfirmasi Biaya (Sesuai Paket):")
        
        st.subheader("File Transaksi (Untuk Analisa)")
        file_data = st.file_uploader("Upload Nota/Laporan (.csv, .xlsx)", type=['csv', 'xlsx'])
        
        submit = st.form_submit_button("Kirim Data ke Admin")
        if submit:
            if n_bisnis and p_pilihan:
                new_data = {
                    "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "Nasabah": n_bisnis,
                    "Usaha": j_usaha,
                    "Paket": p_pilihan,
                    "File": file_data.name if file_data else "No File",
                    "Status": "Pending Review"
                }
                st.session_state.db_nasabah.append(new_data)
                st.success("✅ Data berhasil dikirim. Admin akan segera menganalisa data Anda.")
            else:
                st.error("Mohon lengkapi Nama Bisnis dan Paket.")

# --- MENU 5: ADMIN DASHBOARD ---
elif menu == "5. 🔐 Admin Dashboard":
    st.header("🔐 Intelligence Center (Super Admin)")
    u_id = st.text_input("Username:")
    p_id = st.text_input("Password:", type="password")
    
    if u_id == "erwin_admin" and p_id == "w1nbju8282":
        st.success("Akses Diterima: Super Admin Erwin Sinaga")
        t1, t2, t3 = st.tabs(["📊 Analisa Data Masuk", "🕒 Jadwal Server", "⚙️ Status Sistem"])
        
        with t1:
            st.subheader("Pusat Analisa Data Nasabah")
            if st.session_state.db_nasabah:
                df = pd.DataFrame(st.session_state.db_nasabah)
                st.dataframe(df, use_container_width=True)
                
                # Fitur Analisa Tambahan
                st.write("---")
                st.subheader("🔍 Analisa Beban Paket")
                st
