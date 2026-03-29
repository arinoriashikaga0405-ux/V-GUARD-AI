import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os
from datetime import datetime

# 1. KONFIGURASI SISTEM (Wajib di baris pertama)
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Masukkan API Key Bapak di sini
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. CSS TAMPILAN MEWAH (Warna Biru Navy & Emas - DIKUNCI)
st.markdown("""
    <style>
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; color: white !important; }
    .hero-bg { 
        background-color: #0e1117; padding: 50px; border-radius: 20px; color: white; 
        text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px;
    }
    .card-service {
        background-color: white; padding: 25px; border-radius: 15px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center; height: 100%; color: #0e1117;
    }
    .founder-text {
        display: flex; flex-direction: column; justify-content: center; height: 80px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. FUNGSI AMBIL FOTO (Pencarian Ganda agar Tidak Hilang Lagi)
def get_foto(lebar):
    # Mencari berbagai kemungkinan nama file yang Bapak upload
    list_nama = ['bapak_erwin.jpg', 'Bapak_erwin.jpg', 'bapak_erwin.JPG']
    
    file_ketemu = None
    for nama in list_nama:
        if os.path.exists(nama):
            file_ketemu = nama
            break
            
    if file_ketemu:
        return st.image(Image.open(file_ketemu), width=lebar)
    else:
        # Jika benar-benar tidak ketemu di server, gunakan ikon placeholder agar web tidak crash
        return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)

# 4. SIDEBAR NAVIGATION (PROFIL SEJAJAR)
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD SYSTEMS")
    
    # Menyejajarkan Foto dan Nama
    col_f, col_n = st.columns([1, 2])
    with col_f:
        get_foto(80)
    with col_n:
        st.markdown(f"""
            <div class='founder-text'>
                <p style='color: white; font-weight: bold; margin-bottom: 0px;'>Erwin Sinaga</p>
                <p style='color: #FFD700; font-size: 11px;'>Founder V-GUARD</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.divider()
    halaman = st.radio("Navigasi Utama:", ["🌐 Promosi & Umum", "👥 Monitoring Klien", "🔐 Admin & Invoice"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: PROMOSI (LANDING PAGE DIKUNCI)
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
        get_foto(350) # Foto besar di Landing Page
    with c2:
        st.markdown("## FILOSOFI & PROFIL")
        # TEKS SESUAI PERMINTAAN BAPAK
        st.write("""
        V-Guard bukan sekadar software, tapi **AI Auditor** yang memberikan **Alarm Merah** ke Business Owner 
        untuk mendeteksi kebocoran dana, menagih piutang lewat WA, dan mengirim laporan mingguan 
        ke Klien setiap minggu. 
        """)
        st.info("📍 Berdomisili di Tangerang, melayani audit digital seluruh Indonesia.")
        
        st.write("### Paket Layanan V-GUARD")
        p1, p2, p3 = st.columns(3)
        p1.markdown('<div class="card-service"><b>📦 LITE</b><br>7,5 Jt</div>', unsafe_allow_html=True)
        p2.markdown('<div class="card-service" style="border: 2px solid #FFD700"><b>🚀 PRO</b><br>15 Jt</div>', unsafe_allow_html=True)
        p3.markdown('<div class="card-service"><b>🏢 ENTERPRISE</b><br>25 Jt</div>', unsafe_allow_html=True)

# 5. HALAMAN LAIN (Tetap berfungsi)
elif halaman == "👥 Monitoring Klien":
    st.title("👥 Monitoring Klien Real-time")
    st.info("Data diamankan dengan enkripsi V-Guard.")

else:
    st.title("🔐 Panel Admin")
    st.text_input("Password Admin:", type="password")
