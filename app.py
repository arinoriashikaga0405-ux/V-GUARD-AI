import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os
from datetime import datetime

# 1. KONFIGURASI SISTEM (Anti-Error)
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Masukkan kembali API Key Bapak di sini
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. CSS TAMPILAN MEWAH (Warna Biru Navy & Emas, Teks Putih Terang)
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
    .invoice-box { border: 2px solid #e0e0e0; padding: 20px; border-radius: 10px; background-color: #fff; color: #000; }
    </style>
    """, unsafe_allow_html=True)

# 3. FUNGSI AMBIL FOTO (Kunci Foto Bapak dari image_22.png)
def tampilkan_foto(lebar):
    # MENYESUAIKAN KE NAMA FILE YANG BENAR: bapak_erwin.jpg
    if os.path.exists('bapak_erwin.jpg'):
        st.image(Image.open('bapak_erwin.jpg'), width=lebar)
    else:
        # Ikon cadangan jika bapak_erwin.jpg tidak ditemukan agar web tidak crash
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)

# 4. SIDEBAR NAVIGATION DENGAN PROFIL SEJAJAR
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD SYSTEMS")
    
    # Grid untuk foto & nama agar SEJAJAR KE SAMPING
    col_foto, col_nama = st.columns([1, 2])
    
    with col_foto:
        tampilkan_foto(80) # Foto kecil di sidebar
        
    with col_nama:
        st.markdown("""
            <div style='padding-top: 10px;'>
                <p style='color: white; font-weight: bold; margin-bottom: 0px;'>Erwin Sinaga</p>
                <p style='color: #FFD700; font-size: 12px;'>Founder V-GUARD</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.divider()
    halaman = st.radio("Pilih Halaman:", ["🌐 Promosi & Umum", "👥 Monitoring Klien", "🔐 Admin & Invoice"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: PROMOSI (LANDING PAGE - DESAIN DIKUNCI MATI)
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
        tampilkan_foto(350) # Foto besar Bapak di landing page
    with c2:
        st.markdown("## FILOSOFI & PROFIL")
        # TEKS BARU YANG TEGAS SESUAI PERMINTAAN
        st.write("""
        V-GUARD bukan sekadar software, tapi **AI Auditor** yang memberikan **Alarm Merah** ke Business Owner. 
        Sistem kami dirancang untuk mendeteksi kebocoran dana secara proaktif, menagih piutang lewat WA, 
        dan mengirim laporan mingguan ke Klien setiap minggu. Dibawah kepemimpinan Erwin Sinaga, 
        kami memastikan aset Anda aman dan transparan.
        """)
        st.info("📍 Berdomisili di Tangerang, melayani audit digital seluruh Indonesia.")
        
        st.write("### Daftar Layanan")
        p1, p2, p3 = st.columns(3)
        p1.markdown('<div class="card-service"><b>📦 LITE</b><br>7,5 Jt</div>', unsafe_allow_html=True)
        p2.markdown('<div class="card-service" style="border:1px solid #FFD700"><b>🚀 PRO</b><br>15 Jt</div>', unsafe_allow_html=True)
        p3.markdown('<div class="card-service"><b>🏢 ENTERPRISE</b><br>25 Jt</div>', unsafe_allow_html=True)

# ==========================================
# HALAMAN LAINNYA (Placeholders)
# ==========================================
elif halaman == "👥 Monitoring Klien":
    st.title("👥 Dashboard Monitor Klien")
    st.info("Fitur pelacakan anomali real-time sedang aktif.")

else:
    st.title("🔐 Panel Admin & Penagihan")
    st.text_input("Password Admin:", type="password")
