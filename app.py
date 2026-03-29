import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os

# 1. KONFIGURASI SISTEM
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Konfigurasi AI (Masukkan API Key Bapak)
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# CSS TAMPILAN MEWAH BIRU NAVY
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; color: white !important; }
    section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] p { color: white !important; }
    .hero-bg { 
        background-color: #0e1117; padding: 50px; border-radius: 20px; color: white; 
        text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px;
    }
    .card-service {
        background-color: white; padding: 25px; border-radius: 15px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center; height: 100%; color: #0e1117;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. FUNGSI UNTUK MENGAMBIL FOTO LOKAL (Anti-Error)
def get_bapak_photo(lebar):
    try:
        # Mencari file bapak.png di GitHub Bapak
        if os.path.exists('bapak.png'):
            image = Image.open('bapak.png')
            st.image(image, width=lebar)
        else:
            # Jika file tidak ditemukan, pakai ikon default standar
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)
    except:
        # Pencegahan error jika Pillow bermasalah
        st.write("📸 [Foto V-GUARD]")

# 3. SIDEBAR NAVIGATION & PROFIL
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD SYSTEMS")
    
    # Menampilkan foto Bapak di sidebar (Kecil)
    get_bapak_photo(120)
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
        # Menampilkan foto Bapak yang besar di Landing Page
        get_bapak_photo(300)
    with c2:
        st.markdown("## FILOSOFI & PROFIL")
        st.write("""
        V-GUARD AI Systems hadir sebagai solusi audit masa depan yang transparan dan akurat. 
        Dipimpin oleh Erwin Sinaga, seorang Senior Business Leader dengan pengalaman 
        keamanan teknologi tercanggih, kami berkomitmen menjaga integritas aset bisnis Anda.
        """)
        st.info("📍 Berdomisili di Tangerang, melayani audit digital seluruh Indonesia.")

    st.write("### Daftar Layanan")
    p1, p2, p3 = st.columns(3)
    p1.markdown('<div class="card-service"><h3>📦 LITE</h3><h2>7,5 Jt</h2><p>Audit Angka Dasar</p></div>', unsafe_allow_html=True)
    p2.markdown('<div class="card-service" style="border: 2px solid #FFD700;"><h3>🚀 PRO</h3><h2 style="color: #FFD700;">15 Jt</h2><p>Investigasi Fraud AI</p></div>', unsafe_allow_html=True)
    p3.markdown('<div class="card-service"><h3>🏢 ENTERPRISE</h3><h2>25 Jt</h2><p>Strategis & Profit</p></div>', unsafe_allow_html=True)

# Lanjutan kode Halaman Area Klien dan Panel Admin tetap sama seperti kode sebelumnya...
