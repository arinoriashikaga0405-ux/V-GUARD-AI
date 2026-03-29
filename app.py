import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os

# 1. KONFIGURASI SISTEM
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Masukkan API Key Bapak di sini
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# CSS TAMPILAN MEWAH BIRU NAVY & EMAS
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; color: white; }
    .hero-bg { 
        background-color: #0e1117; padding: 50px; border-radius: 20px; color: white; 
        text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px;
    }
    .card-service {
        background-color: white; padding: 25px; border-radius: 15px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center; height: 100%; color: #0e1117;
    }
    .package-pro { border: 2px solid #FFD700; transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

# FUNGSI UNTUK CEK DAN AMBIL FOTO LOKAL
def tampilkan_foto_profil(lebar):
    try:
        # Mencari file bapak.png di GitHub Bapak
        if os.path.exists('bapak.png'):
            image = Image.open('bapak.png')
            st.image(image, width=lebar)
        else:
            # Jika foto tidak ditemukan, pakai ikon default standar
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)
    except:
        # Pencegahan error jika Pillow bermasalah
        st.write("📸 [Foto V-GUARD]")

# 2. SIDEBAR NAVIGATION & PROFIL
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD SYSTEMS")
    
    # Menampilkan foto profil di sidebar (Kecil)
    tampilkan_foto_profil(120)
    st.markdown("<center><b>Erwin Sinaga</b><br>Founder V-GUARD</center>", unsafe_allow_html=True)
    
    st.divider()
    halaman = st.radio("Pilih Halaman:", ["🌐 Promosi & Umum", "👥 Area Layanan Klien", "🔐 Panel Admin"])
    st.divider()
    st.write("📍 Tangerang, Banten, Indonesia")

# ==========================================
# HALAMAN 1: PROMOSI & UMUM (LANDING PAGE)
# ==========================================
if halaman == "🌐 Promosi & Umum":
    st.markdown("""
        <div class="hero-bg">
            <h1 style='color: #FFD700;'>V-GUARD AI SYSTEMS</h1>
            <h3>Hentikan Kebocoran Finansial Bisnis Anda.</h3>
            <p>Sistem Audit Otonom Berbasis AI | Standar POJK No. 56/2016.</p>
        </div>
        """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 2])
    with c1:
        # Menampilkan foto profil besar di Landing Page
        tampilkan_foto_profil(300)
    with c2:
        st.markdown("## FILOSOFI & PROFIL")
        st.write("""
        V-GUARD AI Systems lahir dari visi Erwin Sinaga, seorang Senior Business Leader 
        dengan pengalaman kepemimpinan strategis selama lebih dari satu dekade. 
        Kami hadir untuk memberikan transparansi mutlak bagi pemilik bisnis melalui 
        teknologi Audit AI tercanggih.
        """)
        st.info("Berdomisili di Tangerang, melayani audit digital seluruh Indonesia.")
        st.link_button("🟢 KONSULTASI AUDIT VIA WHATSAPP", "https://wa.me/6281234567890")

    st.write("### Daftar Layanan")
    p1, p2, p3 = st.columns(3)
    p1.markdown('<div class="card-service"><h3>📦 LITE</h3><h2>7,5 Jt</h2><p>Audit Angka Dasar</p></div>', unsafe_allow_html=True)
    p2.markdown('<div class="card-service package-pro"><h3>🚀 PRO</h3><h2 style="color: #FFD700;">15 Jt</h2><p>Investigasi Fraud AI</p></div>', unsafe_allow_html=True)
    p3.markdown('<div class="card-service"><h3>🏢 ENTERPRISE</h3><h2>25 Jt</h2><p>Strategis & Profit</p></div>', unsafe_allow_html=True)

# Lanjutan kode Halaman Area Klien dan Panel Admin tetap sama seperti kode sebelumnya...
