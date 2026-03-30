import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# Inisialisasi Database Penampung Data Nasabah (Session State)
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = []

# 2. CSS CUSTOM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 18px; }
    .package-box { height: 500px; padding: 20px; border: 1px solid #e0e0e0; border-radius: 10px; background-color: #ffffff; margin-bottom: 10px; }
    .footer-container { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #f8f9fa; text-align: center; padding: 15px 0px; font-weight: bold; border-top: 1px solid #dee2e6; z-index: 9999; }
    .stApp { margin-bottom: 100px; }
    .profile-text { text-align: justify; line-height: 1.8; }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/628212190885"

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Folder Menu:", ["1. 👤 Profil & Filosofi", "2. 🎯 Visi, Misi & ROI", "3. 📦 Pendaftaran & Paket", "4. 🔐 Admin Dashboard"])
    st.markdown('<p class="status-connected">● System Online</p>', unsafe_allow_html=True)
    st.link_button("📞 Konsultasi Langsung", wa_url, use_container_width=True)

# --- MENU 1: PROFIL ---
if menu == "1. 👤 Profil & Filosofi":
    st.header("👤 Strategic Leadership & Philosophy")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.subheader("Erwin Sinaga")
        st.markdown('<div class="profile-text">Bapak Erwin Sinaga adalah seorang profesional dan Pemimpin Bisnis Senior yang memiliki dedikasi tinggi selama lebih dari sepuluh tahun dalam dunia perbankan serta manajemen aset nasional. Melalui perjalanan karier yang panjang di sektor keuangan formal, beliau telah mengasah keahlian strategis dalam manajemen risiko kredit, pengawasan kepatuhan operasional (compliance), hingga perancangan sistem perlindungan aset korporasi skala besar. Pengalaman mendalam beliau dalam menangani struktur keuangan yang kompleks memberikan landasan kuat bagi pengembangan sistem keamanan audit berbasis teknologi tinggi.<br><br>Filosofi kepemimpinan beliau berakar pada integritas mutlak dan transparansi data, di mana beliau percaya bahwa setiap celah fraud dapat ditutup dengan sinergi antara ketelitian manusia dan kecanggihan teknologi digital. V-Guard AI lahir dari visi beliau untuk membawa standar keamanan audit perbankan yang sangat ketat ke dalam ekosistem bisnis UMKM dan perusahaan menengah.</div>', unsafe_allow_html=True)

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Analisis Strategi & ROI")
    st.info("### 🎯 Visi 2026\nMenjadi standar utama keamanan audit AI di Indonesia.")
    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Aset (ROI)")
    omzet = st.number_input("Input Omzet Bulanan Bisnis (Rp):", value=500000000, step=10000000)
    potensi_rugi = omzet * 0.05
    st.error(f"🚨 Estimasi Kebocoran Aset (5%): Rp {potensi_rugi:,.0f}")
    st.success(f"🛡️ Target Penyelamatan V-Guard (90%): Rp {potensi_rugi * 0.9:,.0f}")

# --- MENU 3: PENDAFTARAN (TEMPAT NASABAH KIRIM DATA) ---
elif menu == "3. 📦 Pendaftaran & Paket":
    st.header("📦 Pilih Paket & Kirim Data Nasabah")
    st.write("Calon nasabah mengisi formulir ini untuk mengirimkan permintaan aktivasi ke Admin.")
    
    with st.form("form_nasabah"):
        nama_nasabah = st.text_input("Nama Lengkap / Nama Bisnis:")
        jenis_usaha = st.selectbox("Jenis Usaha:", ["Retail", "F&B", "Jasa", "Corporate"])
        paket_dipilih = st.selectbox("Pilih Paket Layanan:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        kontak = st.text_input("Nomor WA / Email:")
        submit_btn = st.form_submit_button("Kirim Data Pendaftaran")
        
        if submit_btn:
            if nama_nasabah and kontak:
                # DATA DITERIMA DAN DISIMPAN
                data_baru = {
                    "Waktu": datetime.now().strftime("%H:%M"),
                    "Nasabah": nama_nasabah,
                    "Usaha": jenis_usaha,
                    "Paket": paket_dipilih,
                    "Kontak": kontak
                }
                st.session_state.db_nasabah.append(data_baru)
                st.success("✅ Data Anda telah terkirim! Admin V-Guard akan menghubungi Anda untuk aktivasi modul.")
            else:
                st.warning("Mohon lengkapi Nama dan Kontak Bapak.")

# --- MENU 4: ADMIN DASHBOARD (TEMPAT BAPAK TERIMA DATA) ---
elif menu == "4. 🔐 Admin Dashboard":
    st.header("🔐 Intelligence Center")
    u_id = st.text_input("Username Admin:")
    p_id = st.text_input("Password Admin:", type="password")
    
    if u_id == "erwin_admin" and p_id == "w1nbju8282": 
        st.success("Welcome, Super Admin.")
        t1, t2, t3 = st.tabs(["📩 Antrean Data Nasabah", "🕒 Jadwal & Load", "📊 Database Aktif"])
        
        with t1:
            st.subheader("Data Pendaftaran Masuk (Real-time)")
            if st.session_state.db_nasabah:
                # MENAMPILKAN DATA YANG DIKIRIM DARI MENU 3
                st.table(pd.DataFrame(st.session_state.db_nasabah))
                st.info("Bapak bisa segera menghubungi kontak di atas untuk proses aktivasi.")
            else:
                st.write("Belum ada data nasabah baru yang masuk.")
        
        with t2:
            st.subheader("Pengaturan Jadwal Kirim Data")
            st.write("Pembagian waktu agar server tidak overload:")
            df_j = pd.DataFrame({"Kategori":["Retail","F&B","Corporate"],"Jam Audit":["21:00 WIB","23:00 WIB","Real-time"]})
            st.table(df_j)
            
        with t3:
            st.subheader("Klien Terdaftar")
            df_k = pd.DataFrame({"Nama":["Toko Jaya","Sentosa Corp"],"Paket":["BASIC","CORP"],"Aktif":["Ya","Ya"]})
            st.table(df_k)

    elif p_id != "":
        st.error("Akses Ditolak.")

# 4. FOOTER
st.markdown('<div class="footer-container">© 2026 V-Guard AI Systems - Secured by Advanced Intelligence.</div>', unsafe_allow_html=True)
