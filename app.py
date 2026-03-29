import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os

# 1. KONFIGURASI (PENTING: HARUS DI PALING ATAS)
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Masukkan API Key Bapak di sini
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. SIDEBAR DENGAN FOTO SEJAJAR (COLUMNS)
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD SYSTEMS")
    
    # Membuat 2 kolom agar foto dan nama sejajar kesamping
    col_foto, col_nama = st.columns([1, 2])
    
    with col_foto:
        if os.path.exists('bapak.png'):
            img = Image.open('bapak.png')
            st.image(img, use_container_width=True)
        else:
            # Ikon sementara jika bapak.png belum ditemukan
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", use_container_width=True)
            
    with col_nama:
        st.markdown("""
            <div style='padding-top: 10px;'>
                <p style='color: white; font-weight: bold; margin-bottom: 0px;'>Erwin Sinaga</p>
                <p style='color: #FFD700; font-size: 12px;'>Founder V-GUARD</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.divider()
    halaman = st.radio("Pilih Halaman:", ["🌐 Promosi & Umum", "👥 Area Layanan Klien", "🔐 Panel Admin"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# 3. HALAMAN UTAMA (PROMOSI)
if halaman == "🌐 Promosi & Umum":
    st.markdown("<h1 style='text-align: center;'>V-GUARD AI SYSTEMS</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # Menampilkan foto besar di landing page
        if os.path.exists('bapak.png'):
            st.image(Image.open('bapak.png'), width=300)
        else:
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=300)
            
    with col2:
        st.markdown("## FILOSOFI & PROFIL")
        st.write("V-GUARD AI Systems hadir sebagai solusi audit masa depan yang transparan.")
        st.info("Senior Leader dengan pengalaman 10+ tahun dalam manajemen strategis.")

# Lanjutkan sisa kode halaman lainnya seperti sebelumnya...
