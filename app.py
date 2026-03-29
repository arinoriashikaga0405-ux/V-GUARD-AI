import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os

# 1. KONFIGURASI TEMA & HEADERS (Modern & Clean)
st.set_page_config(page_title="V-Guard AI | Security & Analytics", page_icon="🛡️", layout="wide")

# Konfigurasi AI (Masukkan API Key Bapak)
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. CSS CUSTOM (Sesuai Panduan: Biru Tua, Teal, Putih)
st.markdown("""
    <style>
    /* Global Style */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
    
    .main { background-color: #ffffff; }
    
    /* Sidebar - Deep Navy */
    section[data-testid="stSidebar"] { background-color: #0A192F !important; color: white !important; }
    
    /* Hero Section */
    .hero-container {
        background: linear-gradient(135deg, #0A192F 0%, #112240 100%);
        padding: 60px; border-radius: 15px; color: white; text-align: center;
        border-bottom: 4px solid #64FFDA; margin-bottom: 40px;
    }
    
    /* Service Cards */
    .card {
        padding: 20px; border-radius: 10px; background: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #e0e0e0;
        text-align: center; height: 100%;
    }
    
    /* Status Badge */
    .badge-safe { background-color: #d1fae5; color: #065f46; padding: 5px 10px; border-radius: 20px; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR: PROFIL FOUNDER (SEJAJAR & RAPI)
with st.sidebar:
    st.markdown("<h2 style='color: #64FFDA;'>🛡️ V-GUARD AI</h2>", unsafe_allow_html=True)
    
    # Grid untuk Foto & Nama agar SEJAJAR
    col_foto, col_nama = st.columns([1, 2])
    with col_foto:
        try:
            # Menggunakan file bapak_erwin.jpg yang Bapak upload
            img = Image.open('bapak_erwin.jpg')
            st.image(img, use_container_width=True)
        except:
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", use_container_width=True)
    
    with col_nama:
        st.markdown(f"""
            <div style='padding-top: 5px;'>
                <p style='color: white; font-weight: 600; margin-bottom: 0;'>Erwin Sinaga</p>
                <p style='color: #8892B0; font-size: 12px;'>Founder & Senior Leader</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    halaman = st.sidebar.selectbox("Navigasi Sistem", ["🌐 Promosi & Umum", "👥 Area Layanan Klien", "🔐 Panel Admin"])
    st.divider()
    st.markdown("<p style='font-size: 10px; color: #8892B0;'>Powered by Python & GitHub Integration</p>", unsafe_allow_html=True)

# ==========================================
# HALAMAN 1: PROMOSI & UMUM (LANDING PAGE)
# ==========================================
if halaman == "🌐 Promosi & Umum":
    st.markdown("""
        <div class='hero-container'>
            <h1 style='color: #64FFDA;'>V-Guard AI: Deteksi Kerugian Bisnis Anda</h1>
            <p style='font-size: 18px; opacity: 0.8;'>Solusi deteksi anomali berbasis Artificial Intelligence dengan standar keamanan tinggi.</p>
            <br><button style='background-color: #64FFDA; border: none; padding: 10px 25px; border-radius: 5px; font-weight: bold;'>Mulai Sekarang</button>
        </div>
        """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 2])
    with c1:
        try:
            st.image(Image.open('bapak_erwin.jpg'), caption="Founder V-Guard AI", use_container_width=True)
        except:
            st.warning("Unggah foto bapak_erwin.jpg ke GitHub untuk profil maksimal.")
    
    with c2:
        st.subheader("🛡️ Tentang V-Guard AI")
        st.write("""
        V-Guard AI adalah platform analitik cerdas yang dirancang untuk membantu pemilik bisnis 
        mendeteksi potensi kerugian secara real-time. Menggunakan algoritma Python canggih, 
        kami membedah setiap aliran data transaksi untuk memastikan integritas aset Anda.
        """)
        st.markdown("""
        **Kenapa Memilih Kami?**
        * ✅ Deteksi Anomali Real-Time
        * ✅ Integrasi Alur Kerja GitHub yang Mulus
        * ✅ Didukung oleh Kepemimpinan Strategis 10+ Tahun
        """)

# ==========================================
# HALAMAN 2: AREA LAYANAN KLIEN
# ==========================================
elif halaman == "👥 Area Layanan Klien":
    st.header("👥 Manajemen Solusi & Akses Data")
    st.write("Pantau kesehatan finansial bisnis Anda dari dashboard yang intuitif.")
    
    # Mockup Dashboard
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Total Omset", "Rp 450M", "+12%")
    col_b.metric("Deteksi Anomali", "2 Kasus", "-5%", delta_color="inverse")
    col_c.metric("Security Score", "98%", "🛡️")

    st.write("### Laporan Terkini")
    df = pd.DataFrame({
        "ID Klien": ["C001", "C002", "C003"],
        "Layanan": ["PRO", "LITE", "ENTERPRISE"],
        "Status": ["🛡️ Aman", "⚠️ Investigasi", "🛡️ Aman"],
        "Last Sync": ["GitHub Push: 2m ago", "GitHub Push: 10m ago", "GitHub Push: 1h ago"]
    })
    st.table(df)

# ==========================================
# HALAMAN 3: PANEL ADMIN (SECURITY & LOGIN)
# ==========================================
else:
    st.header("🔐 Akses Aman Manajemen Bisnis")
    col_login, _ = st.columns([1, 1])
    
    with col_login:
        with st.form("admin_login"):
            st.image("https://cdn-icons-png.flaticon.com/512/2592/2592201.png", width=50) # Icon Shield
            user = st.text_input("Username")
            pw = st.text_input("Password", type="password")
            submit = st.form_submit_button("Masuk ke Panel Keamanan")
            
            if submit and pw == "vguard2026":
                st.success("Akses Diterima. Sinkronisasi dengan Repository Backend...")
                st.info("Status Sistem: Python Engine v1.5 Running | GitHub Webhook Active")
            elif submit:
                st.error("Akses Ditolak. Upaya login ini dicatat oleh sistem.")
