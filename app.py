import streamlit as st
import os
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE AI ---
# Inisialisasi Google Gemini Pro
# API Key: AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA
GEMINI_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
genai.configure(api_key=GEMINI_API_KEY)
model_gemini = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Kustom untuk Tampilan Putih/Abu-abu Muda (Sidebar & Kartu)
# Berdasarkan desain kustom profil Erwin Sinaga (Gambar 1, 2)
# Menghapus semua referensi warna hijau dan menggunakan warna putih saja
st.markdown("""
    <style>
    /* Styling Sidebar Erwin Sinaga Kustom */
    [data-testid="stSidebar"] {
        background-color: #f8fafc;
        border-right: 1px solid #e2e8f0;
    }
    .main {
        background-color: #ffffff;
    }

    /* Styling Menu Utama (Tombol Radio Putih Kustom) */
    div.stRadio > div {
        background-color: transparent;
    }
    label[data-testid="stWidgetLabel"] > div > p {
        color: #1e3a8a;
        font-weight: bold;
    }
    div.stRadio > div > label {
        color: #475569;
        font-weight: bold;
    }

    /* Styling Kartu Produk Putih & Tombol Pilih Putih */
    .product-card {
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        padding: 24px;
        text-align: center;
        background-color: #ffffff;
        min-height: 480px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .product-title {
        color: #1e3a8a;
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 16px;
    }
    .product-details {
        color: #64748b;
        font-size: 14px;
        text-align: left;
    }
    .pilih-button {
        background-color: #ffffff;
        color: #1e3a8a;
        border: 2px solid #1e3a8a;
        border-radius: 8px;
        padding: 10px;
        width: 100%;
        margin-top: 16px;
        font-weight: bold;
    }

    /* Styling Metrik & Bagian Admin */
    div[data-testid="stMetricValue"] > div {
        color: #1e3a8a;
        font-size: 24px;
        font-weight: bold;
    }
    .edge-box {
        border: 2px dashed #22c55e;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        background-color: #f0fdf4;
    }

    /* Styling Bagian Admin (Executive Control) */
    .admin-header {
        color: #1e3a8a;
        font-size: 24px;
        font-weight: bold;
    }
    div.stTextInput > div > div > input {
        color: #ffffff;
        background-color: #1e293b;
        border: none;
        border-radius: 4px;
    }

    /* Styling Status Agen AI */
    .status-online { color: #22c55e; font-weight: bold; }
    .status-active { color: #f59e0b; font-weight: bold; }
    .status-processing { color: #3b82f6; font-weight: bold; }
    .status-idle { color: #94a3b8; font-weight: bold; }

    /* Metrik Dasbor Pemasaran */
    div[data-testid="stMetricValue"] {
        font-size: 22px;
    }
    div.stSelectbox > div > div > div > div {
        background-color: transparent;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION (KUSTOM ERWIN SINAGA) ---
with st.sidebar:
    # Logo kustom V-Guard AI (biru muda)
    col_logo, col_vguard = st.columns([1, 4])
    with col_logo:
        # Placeholder untuk logo perisai biru (misal, Gambar 0/1)
        st.markdown("<h1 style='color: #1e3a8a; margin: 0;'>🛡️</h1>", unsafe_allow_html=True)
    with col_vguard:
        st.markdown("<h2 style='color: #1e3a8a; font-weight: 800; margin: 0; padding-top: 10px;'>V-Guard AI</h2>", unsafe_allow_html=True)

    # Foto profil Erwin Sinaga (memegang perisai holografik "Cyber Security Tech" di sirkuit - Gambar 1, 2)
    st.image("path/to/erwin_sinaga_cyber_photo.jpg", caption="Erwin Sinaga - Founder V-Guard AI", use_column_width=True) # Ganti path sesuai kebutuhan

    # Daftar Navigasi Utama (Tombol Radio Putih Kustom - Gambar 1, 2)
    # Diperbarui untuk menampilkan "Portal Klien" dan membuang menu OPEX utama
    st.markdown("### NAVIGASI UTAMA")
    menu = st.radio("", ["Visi & Misi", "Produk & Layanan", "Portal Klien", "Admin Control Center"], key="main_nav")

    # Ikon radio default merah kustom untuk Admin (Gambar 1, 2)
    st.markdown("<h2 style='color: #ef4444; font-size: 20px; font-weight: bold; padding-left: 20px;'>🛑 Admin Control Center</h2>", unsafe_allow_html=True)

    # Informasi SOP ACTIVE di bawah
    st.markdown("<div class='edge-box' style='background-color: #f1f5f9; border-color: #cbd5e1; border-style: solid; margin-top: 20px;'>\
        <h3 style='color: #1e3a8a; font-weight: bold;'>SOP Status: ACTIVE</h3></div>", unsafe_allow_html=True)

# --- 4. LOGIKA MENU DAN KONTEN UTAMA ---

if menu == "Visi & Misi":
    st.header("Visi & Misi V-Guard AI Intelligence")
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        # Gunakan foto profil kustom Erwin Sinaga (Gambar 1, 2)
        st.image("path/to/erwin_sinaga_cyber_photo.jpg", use_column_width=True) # Ganti path sesuai kebutuhan
    with col_txt:
        st.markdown("""
        ### VISI
        Menjadi pilar utama global dalam pengamanan aset digital dan integritas finansial, menciptakan lingkungan bisnis yang sepenuhnya bersih dari fraud melalui Digital Trust.

        ### MISI
        1.  **Dukungan Audit Cerdas:** Memberikan platform AI audit cerdas berbasis Digital Trust untuk memverifikasi data dan audit kasir/bank secara presisi.
        2.  **Edge Filtering:** Membangun deteksi anomali real-time di titik transaksi (Edge) untuk mengeliminasi potensi kebocoran sebelum data mencapai cloud.
        3.  **V-SIGHT Global:** Mengimplementasikan solusi vision AI V-SIGHT untuk pemantauan perilaku visual di kasir dan gudang guna mencegah kecurangan fisik.
        4.  **Forensic AI:** Memberikan insight forensik mendalam berbasis data jangka panjang untuk kepatuhan SOP dan investigasi.
        5.  **Perlindungan ROI:** Berinvestasi dalam teknologi yang mengamankan ROI (Potensi Dana Aman) klien sebagai benteng pertahanan terakhir.
        """)

elif menu == "Produk & Layanan":
    st.header("🛡️ Portofolio Layanan Strategis V-Guard")
    st.write("V-Guard AI Intelligence menghadirkan perlindungan aset digital dan fisik dengan lima paket layanan strategis.")

    # Spanduk Potensi Dana Aman (Gambar 0)
    st.markdown("<div class='roi-box' style='background-color: #1e3a8a; color: white; padding: 20px; border-radius: 12px; margin-bottom: 24px;'>\
        <h2 style='text-align: center; color: white; margin-bottom: 8px;'>Potensi Dana Aman: Rp 20,000,000</h2>\
        <p style='text-align: center; color: white; margin: 0;'>Kebocoran yang berhasil dihentikan oleh sistem V-Guard AI</p></div>", unsafe_allow_html=True)

    # 1. Kartu Produk (Putih dengan Tombol Putih Kustom - Gambar 0, 8)
    # Menggunakan lima paket produk: V-LITE, V-PRO, V-SIGHT, V-ENTERPRISE, V-ULTRA
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Paket V-LITE
    with col1:
        st.markdown("<div class='product-card'>\
            <div class='product-title'>V-LITE</div>\
            <div class='product-details'>🎯 Mikro / 1 Kasir<br>• Fraud Detection<br>• Real-time Alert</div>\
            <button class='pilih-button'>Pilih V-LITE</button></div>", unsafe_allow_html=True)

    # Paket V-PRO
    with col2:
        st.markdown("<div class='product-card'>\
            <div class='product-title'>V-PRO</div>\
            <div class='product-details'>🎯 Retail & Kafe<br>• Fraud Detection<br>• Real-time Alert</div>\
            <button class='pilih-button'>Pilih V-PRO</button></div>", unsafe_allow_html=True)

    # Paket V-SIGHT
    with col3:
        st.markdown("<div class='product-card'>\
            <div class='product-title'>V-SIGHT</div>\
            <div class='product-details'>🎯 Gudang & Toko<br>• Fraud Detection<br>• Real-time Alert</div>\
            <button class='pilih-button'>Pilih V-SIGHT</button></div>", unsafe_allow_html=True)

    # Paket V-ENTERPRISE
    with col4:
        st.markdown("<div class='product-card'>\
            <div class='product-title'>V-ENTERPRISE</div>\
            <div class='product-details'>🎯 Korporasi<br>• Fraud Detection<br>• Real-time Alert</div>\
            <button class='pilih-button'>Pilih V-ENTERPRISE</button></div>", unsafe_allow_html=True)

    # Paket V-ULTRA
    with col5:
        st.markdown("<div class='product-card'>\
            <div class='product-title'>V-ULTRA</div>\
            <div class='product-details'>🎯 Investor & VIP<br>• Fraud Detection<br>• Real-time Alert</div>\
            <button class='pilih-button'>Pilih V-ULTRA</button></div>", unsafe_allow_html=True)

    # 2. Tabel Perbandingan Eksekutif Kustom
    st.markdown("---")
    st.subheader("📊 Tabel Perbandingan Eksekutif V-Guard AI")
    
    tabel_data = {
        "Fitur Utama": ["Metode Audit", "Data Integrity", "Vision AI (Visual)", "Jangkauan Data", "Keamanan Server"],
        "V-LITE": ["Cerdas (API Kasir)", "Cek Void Harian", "-", "1 Kasir", "Shared"],
        "V-PRO": ["Cerdas (API Kasir/Bank)", "Cek Split Harian", "-", "Retail Kafe", "Shared"],
        "V-SIGHT": ["Visual (Vision AI)", "Cek Void Harian", "Pemantauan CCTV", "Gudang/Toko", "Dedicated"],
        "V-ENTERPRISE": ["Forensik (Deep AI)", "Audit SOP Forensik", "-", "Korporasi Nasional", "Dedicated"],
        "V-ULTRA": ["Forensik (Deep AI)", "Audit SOP Forensik", "Pemantauan CCTV", "VIP/Investor", "Dedicated Server"]
    }
    st.table(tabel_data)

elif menu == "Portal Klien":
    st.header("📱 Portal Klien V-Guard AI")
    st.write("Akses Registrasi dan Dasbor Klien V-Guard.")

    # Bagian Registrasi Klien Baru
    st.subheader("📝 Registrasi Klien Baru")
    with st.container(border=True):
        st.text_input("Nama Lengkap Owner")
        st.text_input("Nama Perusahaan / Bisnis")
        st.text_input("Harga Paket Investasi (Rp)")
        st.selectbox("Pilih Paket V-Guard", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE", "V-ULTRA"])
        st.file_uploader("Upload Bukti Transfer Pemasangan")
        st.file_uploader("Upload KTP")
        
        # Tombol Kirim Registrasi Putih Kustom
        st.markdown("<button class='pilih-button' style='width: 320px; margin-top: 10px;'>Kirim Registrasi Baru</button>", unsafe_allow_html=True)

    # Bagian Akses Dasbor Klien Aktif
    st.markdown("---")
    st.subheader("🔑 Akses Dasbor Klien Aktif")
    with st.container(border=True):
        st.text_input("Username Klien")
        st.text_input("Password", type="password")
        
        # Tombol Masuk Putih Kustom
        st.markdown("<button class='pilih-button' style='width: 200px; margin-top: 10px;'>Masuk ke Dasbor</button>", unsafe_allow_html=True)

elif menu == "Admin Control Center":
    # --- 1. Alur Login Admin (Gambar 3) ---
    # Password Admin: w1nbju8282
    ADMIN_PASSWORD = "w1nbju8282"
    
    # Periksa status login admin
    if 'admin_logged_in' not in st.session_state:
        st.session_state.admin_logged_in = False

    if not st.session_state.admin_logged_in:
        # Halaman Login Admin Kustom
        st.markdown("<div class='admin-header' style='text-align: center; margin-bottom: 24px;'>\
            🛡️ V-Guard AI Intelligence | ©2026</div>", unsafe_allow_html=True)
        st.markdown("<h2 class='admin-header'><center>Akses Executive Control</center></h2>", unsafe_allow_html=True)
        
        # Form Login
        with st.container(border=True, key="login_container"):
            # Gunakan kotak teks password gelap kustom (Gambar 3)
            col_icon, col_title = st.columns([1, 10])
            with col_icon:
                st.markdown("### 🔐")
            with col_title:
                st.markdown("<h3 style='margin: 0; padding-top: 5px;'>Executive Admin Control</h3>", unsafe_allow_html=True)
            
            # Input Password
            admin_input_pass = st.text_input("Password", type="password", key="admin_pwd", label_visibility="collapsed")
            
            col_login, col_placeholder = st.columns([1, 4])
            with col_login:
                if st.button("Masuk"):
                    if admin_input_pass == ADMIN_PASSWORD:
                        st.session_state.admin_logged_in = True
                        st.rerun()
                    elif admin_input_pass != "":
                        st.error("Password Salah. Akses Ditolak.")

    else:
        # --- 2. Dashboard Admin (Gambar 1, 5, 6, 7 - Tanpa Warna Hijau!) ---
        # Judul: Executive Admin Dashboard
        st.header("🔒 Executive Admin Dashboard")
        
        # Section Utama: Dasbor Squad Agent Kustom
        # Tampilkan status agen (Visionary, Concierge, dst. - Gambar 1, 5, 6)
        st.markdown("## 👥 Squad AI AGENT Status")
        col_v, col_c, col_g, col_l, col_a = st.columns(5)
        
        with col_v:
            st.markdown("<b>👁️ Visionary</b><br><span class='status-online'>Online</span>", unsafe_allow_html=True)
        with col_c:
            st.markdown("<b>🔑 Concierge</b><br><span class='status-active'>Active</span>", unsafe_allow_html=True)
        with col_g:
            st.markdown("<b>📈 Growth</b><br><span class='status-online'>Online</span>", unsafe_allow_html=True)
        with col_l:
            st.markdown("<b>🤝 Liaison</b><br><span class='status-online'>Online</span>", unsafe_allow_html=True)
        with col_a:
            st.markdown("<b>🧠 Analyst</b><br><span class='status-processing'>Processing</span>", unsafe_allow_html=True)

        # Bagian Pertumbuhan & Pemasaran Kustom
        st.divider()
        st.markdown("### 📈 GROWTH & MARKETING CENTER")
        st.markdown("#### Dasbor Multi-Channel Marketing Control")
        
        col_s1, col_s2, col_s3 = st.columns(3)
        with col_s1:
            # Metrik kustom (Gambar 1, 5, 6)
            st.metric(label="Ad Spend (MTD)", value="Rp 4.5M", delta="-5% Vs MTD Lalu", delta_color="inverse")
        with col_s2:
            st.metric(label="Total Reach", value="850K", delta="+15% Vs Hari Lalu")
        with col_s3:
            st.metric(label="New Leads", value="142", delta="+22% Vs Hari Lalu")

        # Top Leads Today Kustom
        st.divider()
        st.markdown("🚨 Top Leads Today")
        st.markdown("- Bpk. Andi (Property Developer - JKT)")
        st.markdown("- Ibu Sinta (Founder Kafe - BANDUNG)")

        # Section: Analisis ROI & OPEX Kerugian (Pindah dari menu utama ke Admin)
        # Menampilkan section kustom (Gambar 7 - Tanpa Tombol Hijau)
        st.divider()
        st.header("⚖️ Analisis ROI & Efisiensi OPEX Kerugian")
        
        col_oi1, col_oi2 = st.columns(2)
        with col_oi1:
            # Placeholder untuk input ROI (Potensi Dana Aman)
            st.number_input("Omzet Usaha (Rp)", value=200000000)
            st.number_input("OPEX Kasir (Rp)", value=20000000)
            st.slider("Persentase OPEX Kebocoran (%)", 1, 30, 20)
            
            # Tombol Hitung Analisis Kerugian Putih
            st.markdown("<button class='pilih-button' style='width: 240px;'>Hitung Analisis Kerugian</button>", unsafe_allow_html=True)

        with col_oi2:
            # Section metrik ROI kustom
            st.markdown("#### Metrik Efisiensi Dasbor (Potensi)")
            
            c_oi2_1, c_oi2_2 = st.columns(2)
            with c_oi2_1:
                # Metrik Laba Bersih
                st.metric(label="Laba Bersih", value="Rp 400.250.000", delta="Normal", delta_color="inverse")
            with c_oi2_2:
                # Metrik Dana Aman
                st.metric(label="Dana Aman", value="Rp 15.700.000", delta="Fraud Detector Aktif")

            # Ikon Edge Filtering (Hijau Dashed - Gambar 7)
            st.markdown("<div class='edge-box'>\
                🤖 Edge Filtering Active<br>VOID / SPLIT Transaction Monitoring</div>", unsafe_allow_html=True)

            # Tombol Logout Admin Putih
            st.divider()
            if st.button("Keluar Admin (Log Out)"):
                st.session_state.admin_logged_in = False
                st.rerun()

# --- 5. FOOTER ---
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026 | Digitizing Trust</small></center>", unsafe_allow_html=True)
