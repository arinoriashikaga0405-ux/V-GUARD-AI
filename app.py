import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI UTAMA
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# Inisialisasi Database (Session State)
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = []

# 2. CSS CUSTOM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 18px; }
    .package-box { height: 650px; padding: 25px; border: 2px solid #f0f0f0; border-radius: 15px; background-color: #ffffff; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .footer-container { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #f8f9fa; text-align: center; padding: 15px 0px; font-weight: bold; border-top: 1px solid #dee2e6; z-index: 9999; }
    .stApp { margin-bottom: 120px; }
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
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.subheader("Erwin Sinaga")
        st.markdown(f"""<div class="profile-text">
        Bapak Erwin Sinaga adalah seorang profesional dan Pemimpin Bisnis Senior yang memiliki dedikasi tinggi selama lebih dari sepuluh tahun dalam dunia perbankan serta manajemen aset nasional. Melalui perjalanan karier yang panjang di sektor keuangan formal, beliau telah mengasah keahlian strategis dalam manajemen risiko kredit, pengawasan kepatuhan operasional (compliance), hingga perancangan sistem perlindungan aset korporasi skala besar. Pengalaman mendalam beliau dalam menangani struktur keuangan yang kompleks memberikan landasan kuat bagi pengembangan sistem keamanan audit berbasis teknologi tinggi.<br><br>
        Filosofi kepemimpinan beliau berakar pada integritas mutlak dan transparansi data, di mana beliau percaya bahwa setiap celah fraud dapat ditutup dengan sinergi antara ketelitian manusia dan kecanggihan teknologi digital. V-Guard AI lahir dari visi beliau untuk membawa standar keamanan audit perbankan yang sangat ketat ke dalam ekosistem bisnis UMKM dan perusahaan menengah. Beliau memandang bahwa Artificial Intelligence bukan sekadar alat otomatisasi, melainkan benteng pertahanan utama dalam menjaga keberlangsungan finansial klien.
        </div>""", unsafe_allow_html=True)

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Analisis Strategi Bisnis")
    st.info("### 🎯 Visi 2026\nMenjadi standar utama keamanan audit berbasis AI di seluruh ekosistem bisnis Indonesia.")
    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Aset (ROI)")
    omzet = st.number_input("Input Omzet Bulanan Bisnis (Rp):", value=500000000, step=10000000)
    leakage = omzet * 0.05
    st.error(f"🚨 Estimasi Kebocoran (5%): Rp {leakage:,.0f}")
    st.success(f"🛡️ Target Penyelamatan (90%): Rp {leakage * 0.9:,.0f}")

# --- MENU 3: PRODUK & PAKET (FITUR DITAMBAHKAN SESUAI TINGKATAN) ---
elif menu == "3. 📦 Produk & Paket":
    st.header("📦 Paket Layanan V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    packages = [
        {
            "name": "BASIC", "setup": "2.5jt", "monthly": "750rb", 
            "feat": ["Audit Transaksi Harian", "Laporan Mingguan", "Deteksi Anomali Standar", "Support Chat WA"]
        },
        {
            "name": "MEDIUM", "setup": "7.5jt", "monthly": "1.5jt", 
            "feat": ["Semua Fitur BASIC", "Integrasi AI CCTV", "Analisa Tren Fraud", "Real-time Alert System", "Audit Stok Digital"]
        },
        {
            "name": "ENTERPRISE", "setup": "25jt", "monthly": "5jt", 
            "feat": ["Semua Fitur MEDIUM", "Multi-Branch Dashboard", "Dedicated Cloud Server", "Auto-Invoice Validation", "Forensik Digital Lanjutan"]
        },
        {
            "name": "CORPORATE", "setup": "50jt", "monthly": "10jt", 
            "feat": ["Semua Fitur ENTERPRISE", "Custom AI Model Development", "Audit On-Site Bulanan", "Priority 24/7 Hotline", "Sistem Proteksi Aset Global"]
        }
    ]
    cols = [c1, c2, c3, c4]
    for i, p in enumerate(packages):
        with cols[i]:
            st.markdown(f"""<div class="package-box">
                <h3 style="text-align:center; color:#1f77b4;">{p['name']}</h3>
                <p style="font-size:14px;"><b>Setup:</b> {p['setup']}<br><b>Monthly:</b> {p['monthly']}</p><hr>
                <ul style="font-size:13px;">{"".join([f"<li>{f}</li>" for f in p['feat']])}</ul>
            </div>""", unsafe_allow_html=True)
            st.link_button(f"Pesan {p['name']}", my_wa, use_container_width=True)

# --- MENU 4: REGISTRASI KLIEN ---
elif menu == "4. 📝 Registrasi Klien":
    st.header("📝 Formulir Registrasi Klien")
    with st.form("reg_form"):
        n_bisnis = st.text_input("Nama Bisnis / Nasabah:")
        j_usaha = st.selectbox("Jenis Usaha:", ["Retail", "F&B / Restoran", "Jasa", "Distribusi", "Corporate"])
        p_pilihan = st.selectbox("Pilih Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        file_data = st.file_uploader("Upload Laporan Transaksi (CSV/XLSX)", type=['csv', 'xlsx'])
        if st.form_submit_button("Kirim Data Pendaftaran"):
            if n_bisnis:
                st.session_state.db_nasabah.append({
                    "Waktu": datetime.now().strftime("%d/%m %H:%M"), 
                    "Nasabah": n_bisnis, 
                    "Usaha": j_usaha, 
                    "Paket": p_pilihan, 
                    "File": file_data.name if file_data else "No File"
                })
                st.success("✅ Berhasil! Data telah terkirim ke Intelligence Center Admin.")
            else:
                st.error("Mohon isi Nama Bisnis.")

# --- MENU 5: ADMIN DASHBOARD (FITUR ANALISA DI SINI) ---
elif menu == "5. 🔐 Admin Dashboard":
    st.header("🔐 Intelligence Center (Super Admin)")
    u_id = st.text_input("Username Admin:")
    p_id = st.text_input("Password Admin:", type="password")
    
    if u_id == "erwin_admin" and p_id == "w1nbju8282":
        st.success("Welcome, Super Admin Erwin Sinaga")
        t1, t2, t3 = st.tabs(["📊 Analisa Data Klien", "🧾 Database Registrasi", "🕒 Log Server"])
        
        with t1:
            st.subheader("🔍 Analisa Distribusi Paket")
            if st.session_state.db_nasabah:
                df = pd.DataFrame(st.session_state.db_nasabah)
                st.bar_chart(df['Paket'].value_counts())
                st.write("Visualisasi ini memudahkan Bapak memantau paket yang paling banyak diminati klien.")
            else:
                st.info("Menunggu data nasabah masuk untuk dianalisa.")
        
        with t2:
            st.subheader("Database Pendaftaran Masuk")
            if st.session_state.db_nasabah:
                st.table(pd.DataFrame(st.session_state.db_nasabah))
            else:
                st.write("Belum ada data pendaftaran.")
        
        with t3:
            st.subheader("Status & Jadwal Audit")
            st.table(pd.DataFrame({"Kategori":["Retail","F&B","Corp"],"Jam Kirim":["21:00","23:00","Realtime"]}))
    elif p_id != "":
        st.error("Akses Ditolak.")

# 4. FOOTER (KEMBALIKAN TANDA AIR SPESIFIK)
st.markdown(f'<div class="footer-container">© 2026 V-Guard AI Systems - Secured by Advanced Intelligence</div>', unsafe_allow_html=True)
