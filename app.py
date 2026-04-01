import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE USER & PAKET ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "p", "Level": "Eksekutif", "Paket": "MASTER"},
        {"User ID": "siska", "Password": "p", "Level": "Klien", "Paket": "SMART"},
        {"User ID": "jaya", "Password": "p", "Level": "Klien", "Paket": "BASIC"}
    ]

if 'client_logged_in' not in st.session_state:
    st.session_state.client_logged_in = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None
if 'auth_admin' not in st.session_state:
    st.session_state.auth_admin = False

# --- 3. CSS TAMPILAN PREMIUM ---
st.markdown("""
<style>
    .status-box { background-color: #e3f2fd; padding: 15px; border-radius: 8px; color: #1e3a8a; font-weight: bold; margin-bottom: 5px; }
    .package-box { background-color: #fff3e0; padding: 8px 15px; border-radius: 8px; color: #e65100; font-weight: bold; display: inline-block; margin-bottom: 20px; border: 1px solid #ffe0b2; }
    .service-card { background-color: #ffffff; padding: 15px; border-radius: 12px; border: 1px solid #e0e0e0; text-align: center; height: 350px; }
    .fraud-header { background-color: #ff7675; color: white; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR NAVIGASI (TETAP 1-5) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.markdown("**Erwin Sinaga - Senior Business Leader**")
    st.write("---")
    nav = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 💎 Layanan Produk", 
        "4. 📝 Registrasi & Upload", 
        "5. 🔐 Akses Terbatas"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI Intelligence")

# --- 5. LOGIKA MENU ---

# MENU 1: PROFIL FOUNDER (UTUH)
if nav == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2.5])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.write("""Bapak **Erwin Sinaga** adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Beliau memahami bahwa di era digital saat ini, integritas data dan keamanan aset adalah fondasi utama bagi setiap unit bisnis untuk dapat tumbuh secara berkelanjutan.

Melalui dedikasi yang tinggi terhadap transparansi, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan mendesak para pengusaha akan sistem perlindungan aset yang berbasis teknologi kecerdasan buatan mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif dan efisien. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit real-time yang mampu meminimalisir risiko kerugian modal secara signifikan.""")

# MENU 2: VISI, MISI & ROI (UTUH)
elif nav == "2. 🎯 Visi, Misi & ROI":
    st.header("Visi, Misi & Analisis Kerugian")
    st.info("**Visi:** Menjadi pelopor global dalam penyediaan infrastruktur audit digital berbasis AI.")
    st.success("**Misi:** Mengintegrasikan AI untuk deteksi fraud real-time.")
    st.write("---")
    st.subheader("📊 Simulasi ROI & Penyelamatan Aset")
    oz = st.number_input("Input Total Omzet Bulanan (Rp):", value=100000000)
    leakage = oz * 0.07
    st.error(f"Potensi Kerugian Akibat Kebocoran (7%): Rp {leakage:,.0f}")
    st.success(f"Estimasi Dana yang Diselamatkan: Rp {leakage - 2500000:,.0f}")

# MENU 3: LAYANAN PRODUK (UTUH)
elif nav == "3. 💎 Layanan Produk":
    st.header("Paket Layanan Unggulan V-Guard AI")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="service-card"><h3>📦 BASIC</h3>Rp 1.5jt<br><br>• AI Monitor Dasar<br>• Laporan Bulanan<br>• Alarm Fraud</div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="service-card" style="border: 2px solid #1e3a8a;"><h3>🚀 SMART</h3>Rp 2.5jt<br><br>• Monitoring Pro<br>• VCS System<br>• Audit Real-Time</div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="service-card"><h3>🛡️ PRO</h3>Rp 5.0jt<br><br>• Forensik Digital<br>• Multi-Cabang<br>• Support 24/7</div>', unsafe_allow_html=True)

# MENU 4: REGISTRASI & DASHBOARD KLIEN (DITAMBAH INFO PAKET)
elif nav == "4. 📝 Registrasi & Upload":
    if not st.session_state.client_logged_in:
        t1, t2 = st.tabs(["📝 Form Pendaftaran", "🔑 Dashboard Akun Klien"])
        with t1:
            with st.form("reg"):
                st.text_input("Nama Pelanggan:")
                st.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO"])
                st.form_submit_button("Kirim Pendaftaran")
        with t2:
            u = st.text_input("User ID:")
            p = st.text_input("Password:", type="password")
            if st.button("LOGIN KLIEN"):
                user = next((c for c in st.session_state.user_creds if c["User ID"] == u and c["Password"] == p), None)
                if user:
                    st.session_state.client_logged_in = True
                    st.session_state.current_user = user
                    st.rerun()
                else: st.error("Akses ditolak.")
    else:
        st.header("Selamat Datang di Ekosistem V-Guard AI")
        # MENAMPILKAN PAKET YANG DIAMBIL
        pkg = st.session_state.current_user.get("Paket", "N/A")
        st.markdown('<div class="status-box">Status Akun: ✅ AKTIF & TERPROTEKSI</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="package-box">📦 Paket Layanan: {pkg}</div>', unsafe_allow_html=True)
        
        st.subheader("📋 Tugas Harian Anda")
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.markdown("**✅ Data Transaksi**\n\nKirim laporan harian pukul 23:59.")
            st.markdown("**✅ Absensi Karyawan**\n\nUpdate shift kasir.")
        with col_t2:
            st.markdown("**✅ Update Stok**\n\nCatat sisa stok fisik.")
            st.markdown("**✅ Koneksi CCTV**\n\nPastikan feed visual terhubung.")
        
        if st.sidebar.button("🚪 Keluar Dashboard"):
            st.session_state.client_logged_in = False
            st.session_state.current_user = None
            st.rerun()

# MENU 5: AKSES TERBATAS ADMIN (UTUH)
elif nav == "5. 🔐 Akses Terbatas":
    if not st.session_state.auth_admin:
        st.subheader("🔐 Akses Khusus Admin")
        pw_admin = st.text_input("Masukkan Password Admin:", type="password")
        if st.button("BUKA PANEL ADMIN"):
            # Password Admin: p atau w1nbju8282
            if pw_admin == "w1nbju8282" or pw_admin == "p":
                st.session_state.auth_admin = True
                st.rerun()
            else: st.error("Password Salah!")
    else:
        st.markdown('<div class="fraud-header">🚨 PANEL KONTROL EKSEKUTIF V-GUARD</div>', unsafe_allow_html=True)
        t_a, t_b = st.tabs(["👤 Aktivasi Akun Klien", "📊 Database Keseluruhan"])
        with t_a:
            with st.form("add_user"):
                new_u = st.text_input("User ID Baru:")
                new_p = st.text_input("Password Baru:")
                new_k = st.selectbox("Tentukan Paket:", ["BASIC", "SMART", "PRO"])
                if st.form_submit_button("AKTIFKAN AKUN"):
                    st.session_state.user_creds.append({"User ID": new_u, "Password": new_p, "Level": "Klien", "Paket": new_k})
                    st.success(f"Akun {new_u} berhasil diaktifkan!")
        with t_b:
            st.table(pd.DataFrame(st.session_state.user_creds))
        
        if st.sidebar.button("🔐 Keluar Admin"):
            st.session_state.auth_admin = False
            st.rerun()

st.write("---")
st.caption("© 2026 V-Guard AI | Secured by Erwin Sinaga")
