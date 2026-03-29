import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os
from datetime import datetime
import urllib.parse
import io

# 1. KONFIGURASI SISTEM
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Masukkan API Key Bapak di sini
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# DATA KONTAK FIX PAK ERWIN
WA_NOMOR = "6282122190885" 

# 2. CSS EXECUTIVE DESIGN (Optimasi Ukuran Compact)
st.markdown("""
    <style>
    /* Background & Sidebar */
    .stApp { background-color: #f8f9fa; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; color: white !important; border-right: 2px solid #FFD700; }
    
    /* Hero Section (Lebih Ringkas) */
    .hero-bg { 
        background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); 
        padding: 40px 20px; border-radius: 20px; color: white; text-align: center; 
        border-bottom: 6px solid #FFD700; box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        margin-bottom: 30px;
    }
    .hero-bg h1 { font-size: 35px; margin-bottom: 10px; color: #FFD700; }
    .hero-bg p { font-size: 16px; opacity: 0.9; }
    
    /* Pricing Cards (Diperkecil) */
    .card-service { 
        background: white; padding: 20px; border-radius: 15px; 
        box-shadow: 0 8px 20px rgba(0,0,0,0.08); color: #0e1117; 
        border-top: 5px solid #FFD700; transition: transform 0.3s;
        height: 300px; text-align: center; /* Tinggi dikunci agar sejajar */
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .card-service:hover { transform: translateY(-5px); }
    .card-title { font-size: 18px; font-weight: 700; color: #0e1117; margin-bottom: 5px; }
    .card-price { font-size: 24px; font-weight: 800; color: #d4af37; margin-bottom: 15px; }
    .card-features { font-size: 13px; color: #555; line-height: 1.4; text-align: left; padding: 0 10px; margin-bottom: 15px; }
    
    /* Sidebar Profile */
    .founder-text { display: flex; flex-direction: column; justify-content: center; height: 80px; padding-left: 10px; }
    
    /* Custom Button (Lebih Kecil) */
    .stButton>button { 
        width: 100%; border-radius: 8px; height: 3em; 
        background: linear-gradient(45deg, #FFD700, #b8860b) !important; 
        color: #0e1117 !important; font-weight: 700; border: none; font-size: 14px;
    }
    
    /* Profile Box */
    .profile-box {
        background-color: #ffffff; padding: 20px; border-radius: 12px;
        border-left: 5px solid #FFD700; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. FUNGSI FOTO
def get_foto(lebar):
    if os.path.exists('erwin.jpg'):
        img = Image.open('erwin.jpg')
        return st.image(img, width=lebar)
    else:
        return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)

# 4. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #FFD700; margin-bottom:0;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 11px; margin-top:-5px;'>AI AUDITOR SYSTEMS</p>", unsafe_allow_html=True)
    
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(70) # Foto sidebar diperkecil sedikit
    with col_n:
        st.markdown(f"""
            <div class='founder-text'>
                <p style='color: white; font-weight: bold; margin-bottom: 0px; font-size: 15px;'>Erwin Sinaga</p>
                <p style='color: #FFD700; font-size: 11px; font-style: italic;'>Founder & CEO</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    halaman = st.radio("MAIN CONSOLE:", ["🌐 Beranda & Profil", "🤖 AI Auditor Engine", "📝 AI Meeting Lab", "🔐 Admin Control WA"])
    st.divider()
    st.info("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: BERANDA & PROFIL
# ==========================================
if halaman == "🌐 Beranda & Profil":
    st.markdown("""
        <div class="hero-bg">
            <h1>V-GUARD AI SYSTEMS</h1>
            <p>Sistem Audit Otonom. Deteksi Fraud. Perlindungan Aset Corporate.</p>
        </div>
        """, unsafe_allow_html=True)
    
    col_img, col_txt = st.columns([1, 1.8])
    
    with col_img:
        st.markdown("### Founder Profile")
        get_foto(350) # Ukuran foto diperkecil dari 400 ke 350
    
    with col_txt:
        st.markdown("## 🛡️ FILOSOFI & PROFIL")
        st.markdown(f"""
        <div class="profile-box">
            <p><b>V-Guard</b> lahir dari visi seorang senior business leader dengan pengalaman lebih dari 10 tahun di manajemen strategis 
            dan optimasi pendapatan. Kami memahami bahwa musuh terbesar pertumbuhan bisnis bukanlah kompetisi, 
            melainkan <b>kebocoran internal (fraud)</b> yang tidak terdeteksi.</p>
            <p>Kami mengintegrasikan kecerdasan buatan (AI) mutakhir untuk menjadi 
            'Mata Elektronik' yang menjaga aset Anda 24/7 tanpa kompromi, memastikan setiap rupiah 
            pendapatan Anda aman dan tercatat.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🎯 Misi Kami:")
        col_a, col_b = st.columns(2)
        with col_a:
            st.write("✅ **Real-Time Fraud Detection**")
            st.write("✅ **Automatic Alarm System (WA)**")
        with col_b:
            st.write("✅ **Deep AI Data Analytics**")
            st.write("✅ **Autonomous Audit System**")

    st.divider()
    st.markdown("<h2 style='text-align: center;'>Layanan Strategis V-GUARD</h2>", unsafe_allow_html=True)
    
    p1, p2, p3 = st.columns(3)
    def wa_link(paket):
        pesan = f"Halo Pak Erwin, saya tertarik konsultasi mengenai V-GUARD paket *{paket}*."
        return f"https://wa.me/{WA_NOMOR}?text={urllib.parse.quote(pesan)}"

    with p1:
        st.markdown("""
            <div class="card-service">
                <div>
                    <div class="card-title">📦 V-LITE</div>
                    <div class="card-price">Rp 7,5 Jt <small>/bln</small></div>
                    <div class="card-features">
                        • Audit 1 Outlet<br>
