import streamlit as st
import google.generativeai as genai

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# CSS UNTUK TAMPILAN MEWAH
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .hero-bg { 
        background-color: #0e1117; 
        padding: 50px; 
        border-radius: 20px; 
        color: white; 
        text-align: center;
        margin-bottom: 30px;
        border-bottom: 5px solid #FFD700;
    }
    .card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        height: 100%;
    }
    .card:hover { box-shadow: 0 8px 16px 0 rgba(0,0,0,0.3); }
    </style>
    """, unsafe_allow_html=True)

# 2. SIDEBAR
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD MENU")
    halaman = st.radio("Navigasi:", ["🌐 Landing Page", "🔐 Admin Dashboard"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# --- HALAMAN 1: LANDING PAGE ---
if halaman == "🌐 Landing Page":
    # Hero Section dengan warna Gelap (Eksklusif)
    st.markdown("""
        <div class="hero-bg">
            <h1 style='font-size: 45px;'>🛡️ V-GUARD AI SYSTEMS</h1>
            <p style='font-size: 20px; opacity: 0.8;'>Hentikan Kebocoran Finansial Bisnis Anda Hari Ini.</p>
            <p>Sistem Audit Otonom Berbasis AI untuk Transparansi Mutlak 24/7.</p>
        </div>
        """, unsafe_allow_html=True)
    
    col_wa1, col_wa2, col_wa3 = st.columns([1,1,1])
    with col_wa2:
        st.link_button("🟢 KONSULTASI AUDIT GRATIS", "https://wa.me/6281234567890", use_container_width=True)

    st.write("###")

    # Profil Founder
    col1, col2 = st.columns([1, 2])
    with col1:
        # Menampilkan gambar user atau placeholder yang lebih baik
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250)
    with col2:
        st.markdown("## FILOSOFI KAMI")
        st.write("""
        V-GUARD AI Systems lahir dari pengalaman kepemimpinan strategis selama lebih dari satu dekade. 
        Kami memahami bahwa musuh terbesar pertumbuhan bisnis adalah kebocoran yang tidak terdeteksi.
        
        Mengacu pada standar **POJK No. 56/2016**, kami hadir sebagai mitra audit mandiri 
        yang menjaga integritas aset Anda dengan kecerdasan AI tingkat tinggi.
        """)

    st.write("---")

    # Daftar Layanan dengan Card
    st.markdown("<h2 style='text-align: center;'>DAFTAR LAYANAN</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""<div class="card"><h3>📦 LITE</h3><h2 style='color: #1f77b4;'>7,5 Jt</h2><p>• Audit Transaksi Harian<br>• Laporan WA Otomatis<br>• Deteksi Selisih Kas</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="card" style='border: 2px solid #FFD700;'><h3>🚀 PRO</h3><h2 style='color: #2ca02c;'>15 Jt</h2><p>• <b>Semua Fitur LITE</b><br>• Predictive Risk Alarm<br>• Analisis Tren Mingguan</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="card"><h3>🏢 ENTERPRISE</h3><h2 style='color: #ff7f0e;'>25 Jt</h2><p>• <b>Semua Fitur PRO</b><br>• Visual Guard Monitoring<br>• Konsultasi Strategis Senior</p></div>""", unsafe_allow_html=True)

# --- HALAMAN 2: ADMIN DASHBOARD ---
else:
    st.title("🔐 Panel Admin")
    # (Kode Admin Bapak yang sebelumnya tetap bisa digunakan di sini)
    st.info("Gunakan Sidebar untuk kembali ke Landing Page.")
