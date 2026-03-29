import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os

# 1. KONFIGURASI TAMPILAN (Modern & Clean)
st.set_page_config(page_title="V-Guard AI | Deteksi Kerugian Bisnis", page_icon="🛡️", layout="wide")

# Masukkan API Key Bapak di sini
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. CSS CUSTOM (Warna: Navy, Teal, White - Sesuai Prompt Desain)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Open+Sans:wght@400;600&display=swap');
    
    html, body, [class*="css"] { font-family: 'Open Sans', sans-serif; }
    h1, h2, h3 { font-family: 'Montserrat', sans-serif; }

    /* Header & Sidebar */
    section[data-testid="stSidebar"] { background-color: #0A192F !important; }
    
    /* Hero Section Gradient */
    .hero-box {
        background: linear-gradient(135deg, #ffffff 0%, #e6f7ff 100%);
        padding: 50px; border-radius: 20px; border-left: 8px solid #008080;
        margin-bottom: 30px;
    }
    
    .btn-mulai {
        background-color: #008080; color: white; padding: 12px 30px;
        border-radius: 8px; text-decoration: none; font-weight: bold;
        display: inline-block; margin-top: 20px;
    }

    /* About Section */
    .about-card {
        background: white; padding: 30px; border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR (PROFIL SEJAJAR)
with st.sidebar:
    st.markdown("<h2 style='color: #64FFDA; font-size: 22px;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    col_f, col_n = st.columns([1, 2])
    with col_f:
        if os.path.exists('bapak_erwin.jpg'):
            st.image(Image.open('bapak_erwin.jpg'), use_container_width=True)
        else:
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", use_container_width=True)
    with col_n:
        st.markdown("<p style='color: white; font-weight: bold; margin-bottom:0;'>Erwin Sinaga</p><p style='color: #008080; font-size: 12px;'>Founder V-Guard</p>", unsafe_allow_html=True)
    
    st.divider()
    menu = st.radio("Menu Utama:", ["🌐 Promosi & Umum", "👥 Area Klien", "🔐 Panel Admin"])

# ==========================================
# HALAMAN 1: PROMOSI & UMUM (LANDING PAGE)
# ==========================================
if menu == "🌐 Promosi & Umum":
    # HERO SECTION
    with st.container():
        col_text, col_img = st.columns([1.2, 1])
        with col_text:
            st.markdown("""
                <div style='padding-top: 50px;'>
                    <h1 style='color: #0A192F; font-size: 45px; line-height: 1.1;'>
                        V-Guard AI: <br><span style='color: #008080;'>Deteksi Kerugian Bisnis Anda</span>
                    </h1>
                    <p style='font-size: 18px; color: #555;'>Amankan aset Anda dengan solusi audit AI otonom terdepan. Deteksi selisih dan fraud real-time sesuai standar POJK.</p>
                    <a href='#' class='btn-mulai'>Mulai Sekarang</a>
                </div>
            """, unsafe_allow_html=True)
        with col_img:
            # Ilustrasi AI/Python (Menggunakan Ikon dari Flaticon sebagai placeholder visual)
            st.image("https://img.freepik.com/free-vector/artificial-intelligence-concept-illustration_114360-7001.jpg", use_container_width=True)

    st.write("---")

    # TENTANG KAMI SECTION
    st.markdown("<h2 style='text-align: center; color: #0A192F;'>🛡️ Tentang V-Guard AI</h2>", unsafe_allow_html=True)
    c_about1, c_about2 = st.columns([1, 1])
    with c_about1:
        st.markdown("""
            <div class='about-card'>
                <p>V-Guard AI adalah solusi audit otonom berbasis visual yang didukung kecerdasan buatan. 
                Kami membantu pemilik bisnis dan direksi mendeteksi kebocoran finansial, anomali kasir, 
                dan pola fraud dengan presisi tinggi.</p>
                <b>Manfaat Utama:</b><br>
                ✅ Efisiensi Audit hingga 90%<br>
                ✅ Laporan Real-time via WhatsApp/Web<br>
                ✅ Deteksi Kecurangan Visual (CCTV Integration)
            </div>
        """, unsafe_allow_html=True)
    with c_about2:
        # Visual Pendukung: Perbandingan Tanpa vs Dengan AI
        st.image("https://img.freepik.com/free-vector/data-inform-illustration-concept_114360-1501.jpg", caption="Analisis Data Akurat", use_container_width=True)

# ==========================================
# HALAMAN LAINNYA (Placeholder)
# ==========================================
elif menu == "👥 Area Klien":
    st.title("👥 Dashboard Layanan Klien")
    st.info("Fitur pelacakan anomali real-time sedang aktif.")
    st.table(pd.DataFrame({"Klien": ["Resto BSD", "Cafe Serpong"], "Status": ["Aman", "Aman"]}))

else:
    st.title("🔐 Panel Admin")
    st.text_input("Admin Password", type="password")
