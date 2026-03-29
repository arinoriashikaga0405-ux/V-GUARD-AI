import streamlit as st

# ==========================================
# 1. KONFIGURASI HALAMAN & TEMA WARNA (CSS KEREN)
# ==========================================
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    /* Mengubah Background Halaman Menjadi Abu-abu Sangat Terang */
    .main { background-color: #F4F7F6; color: #102A43; }
    
    /* Mengubah Sidebar Menjadi Biru Navy */
    section[data-testid="stSidebar"] {
        background-color: #102A43 !important;
        color: white !important;
    }
    
    /* Warna teks dan radio button di sidebar */
    section[data-testid="stSidebar"] .stMarkdown, 
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] .stRadio {
        color: white !important;
    }

    /* Mengubah Header (Bagian Hitam di image_1.png) menjadi Biru Navy Mewah */
    .hero-bg {
        background-color: #102A43;
        padding: 60px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 40px;
        border-bottom: 5px solid #FFD700; /* Garis Bawah Emas */
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }
    .hero-bg h1 { color: #FFD700 !important; font-size: 50px !important; }
    .hero-bg h3 { opacity: 0.9; }

    /* Gaya untuk Kotak Layanan (Card) - Menjadi Putih Bersih dengan Bayangan Lembut */
    .card-service {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.2s; /* Efek Hover */
        height: 100%;
        color: #102A43;
    }
    .card-service:hover {
        transform: translateY(-5px); /* Sedikit terangkat saat hover */
        box-shadow: 0 8px 12px rgba(0,0,0,0.2);
    }
    .card-service h3 { color: #102A43; border-bottom: 2px solid #FFD700; display: inline-block; padding-bottom: 10px; }
    .card-service .price { font-size: 30px; font-weight: bold; color: #102A43; margin-top: 20px; }
    
    /* Warna Khusus untuk Paket PRO agar menonjol */
    .card-service-pro {
        border: 3px solid #FFD700;
        transform: scale(1.03); /* Sedikit lebih besar */
    }

    /* Tombol WhatsApp Hijau */
    .stLinkButton > a {
        background-color: #25D366 !important;
        color: white !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        padding: 10px 20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. MENU UTAMA DI SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("## 🛡️ V-GUARD MENU")
    
    # PERBAIKAN: Menambahkan Foto Bapak di Sidebar agar selalu muncul
    # Masukkan link foto Bapak di sini
    url_foto_bapak = "LINK_FOTO_PRESIDEN_DIREKSI_BAPAK" 
    # Placeholder jika link Bapak belum ada
    if url_foto_bapak == "LINK_FOTO_PRESIDEN_DIREKSI_BAPAK":
        url_foto_bapak = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"

    col_side_1, col_side_2, col_side_3 = st.columns([1,2,1])
    with col_side_2:
        st.image(url_foto_bapak, width=100)
    st.markdown("<center>Erwin Sinaga, Founder V-GUARD</center>", unsafe_allow_html=True)
    st.divider()

    halaman = st.radio("Pilih Tampilan:", ["🌐 Landing Page (Klien)", "🔐 Admin Dashboard"])
    st.divider()
    st.write("📍 Tangerang, Banten, Indonesia")

# ==========================================
# 3. HALAMAN 1: LANDING PAGE (UNTUK KLIEN)
# ==========================================
if halaman == "🌐 Landing Page (Klien)":
    # Hero Section - Mewah (image_1.png -> Update)
    st.markdown("""
        <div class="hero-bg">
            <h1>V-GUARD AI SYSTEMS</h1>
            <h3>Hentikan Kebocoran Finansial Bisnis Anda Hari Ini.</h3>
            <p>Sistem Audit Otonom Berbasis AI untuk Transparansi Mutlak 24/7.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Tombol WhatsApp
    st.link_button("🟢 KONSULTASI AUDIT GRATIS (WA)", "https://wa.me/6281234567890", use_container_width=True)

    st.write("###")

    # Bagian Profil & Filosofi (Sesuai keinginan Bapak)
    c1, c2 = st.columns([1, 2])
    with c1:
        # Menampilkan foto Bapak lagi, lebih besar di halaman utama
        st.image(url_foto_bapak, width=280)
    with c2:
        st.markdown("<h2 style='color:#102A43;'>FILOSOFI KAMI</h2>", unsafe_allow_html=True)
        st.write("""
        V-GUARD AI Systems lahir dari pengalaman kepemimpinan strategis selama lebih dari satu dekade. 
        Kami memahami bahwa musuh terbesar pertumbuhan bisnis adalah kebocoran yang tidak terdeteksi.
        
        Mengacu pada standar **POJK No. 56/2016**, kami hadir sebagai mitra audit mandiri yang 
        menjaga integritas aset Anda dengan kecerdasan AI tingkat tinggi. Kami memberikan 
        ketenangan pikiran (peace of mind) bagi para pemilik bisnis.
        """)
        # Menambahkan data profil singkat Bapak
        st.markdown("**Profil Founder:** Erwin Sinaga (10+ Tahun Pengalaman Strategis, Tangerang)")

    st.write("---")

    # Bagian Layanan - Sangat Keren (image_2.png -> Update)
    st.markdown("<h2 style='text-align: center; color:#102A43;'>DAFTAR LAYANAN V-GUARD AI</h2>", unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    
    with p1:
        st.markdown("""
            <div class="card-service">
                <h3>V-GUARD LITE</h3>
                <p class="price">7,5 Jt / thn</p>
                <ul style='text-align: left;'>
                    <li>Audit Transaksi Harian</li>
                    <li>Laporan WhatsApp Otomatis</li>
                    <li>Deteksi Selisih Kas</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
    with p2:
        st.markdown("""
            <div class="card-service card-service-pro">
                <h3 style='border-bottom: 2px solid #FFD700;'>V-GUARD PRO</h3>
                <p class="price">15 Jt / thn</p>
                <ul style='text-align: left;'>
                    <li><b>Semua Fitur LITE</b></li>
                    <li>Predictive Risk Alarm</li>
                    <li>Analisis Tren Mingguan</li>
                </ul>
                <p style='color: #FFD700; font-weight:bold; margin-top:10px;'>Paling Populer!</p>
            </div>
            """, unsafe_allow_html=True)
            
    with p3:
        st.markdown("""
            <div class="card-service">
                <h3>ENTERPRISE</h3>
                <p class="price">25 Jt / thn</p>
                <ul style='text-align: left;'>
                    <li><b>Semua Fitur PRO</b></li>
                    <li>Visual Guard Monitoring</li>
                    <li>Konsultasi Strategis Senior</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    st.write("---")
    st.markdown("<center>© 2026 V-GUARD AI Systems | Tangerang, Banten</center>", unsafe_allow_html=True)

# ==========================================
# 4. HALAMAN 2: ADMIN DASHBOARD (Proteksi Password)
# ==========================================
elif halaman == "🔐 Admin Dashboard":
    st.title("🔐 Panel Kendali Admin V-GUARD")
    st.info("Masukkan password untuk mengakses fitur audit AI.")
    pw = st.text_input("Password:", type="password")
    
    if pw == "vguard2026": # Ganti password sesuai keinginan Bapak
        st.success("Selamat bekerja, Pak Erwin.")
        st.divider()
        st.subheader("Jalankan Audit AI Profesional")
        data_audit = st.text_area("Masukkan data audit:")
        if st.button("Proses Audit Sekarang"):
            st.write("Menganalisis data...")
    elif pw != "":
        st.error("Password Salah!")
