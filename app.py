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

# Konfigurasi AI
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# DATA KONTAK FIX PAK ERWIN
WA_NOMOR = "6282122190885" 

# 2. CSS EXECUTIVE DESIGN
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .hero-bg { 
        background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); 
        padding: 50px; border-radius: 25px; color: white; text-align: center; 
        border-bottom: 8px solid #FFD700; box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin-bottom: 40px;
    }
    .card-service { 
        background: white; padding: 25px; border-radius: 20px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.1); color: #0e1117; 
        border-top: 6px solid #FFD700; height: 100%; text-align: center;
    }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(45deg, #FFD700, #b8860b) !important; 
        color: #0e1117 !important; font-weight: bold; border: none;
    }
    .profile-box {
        background-color: #ffffff; padding: 25px; border-radius: 15px;
        border-left: 5px solid #FFD700; box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. FUNGSI FOTO
def get_foto(lebar):
    if os.path.exists('erwin.jpg'):
        return st.image(Image.open('erwin.jpg'), width=lebar)
    else:
        return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)

# 4. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #FFD700;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(80)
    with col_n:
        st.markdown(f"<div style='padding-top:10px;'><p style='color: white; font-weight: bold; margin-bottom: 0px;'>Erwin Sinaga</p><p style='color: #FFD700; font-size: 11px;'>Founder & CEO</p></div>", unsafe_allow_html=True)
    st.divider()
    halaman = st.radio("MENU UTAMA:", ["🌐 Beranda & Profil", "🤖 AI Auditor Engine", "📝 AI Meeting Lab", "🔐 Admin Panel"])

# ==========================================
# HALAMAN 1: BERANDA & FILOSOFI (KEMBALI)
# ==========================================
if halaman == "🌐 Beranda & Profil":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>The Future of Corporate Revenue Protection & Audit.</p></div>', unsafe_allow_html=True)
    
    col_img, col_txt = st.columns([1, 1.8])
    
    with col_img:
        get_foto(450)
    
    with col_txt:
        st.markdown("## 🛡️ FILOSOFI & PROFIL")
        st.markdown(f"""
        <div class="profile-box">
            <p><b>V-Guard</b> lahir dari visi seorang leader dengan pengalaman lebih dari 10 tahun di manajemen strategis 
            dan optimasi pendapatan. Kami memahami bahwa musuh terbesar pertumbuhan bisnis bukanlah kompetisi, 
            melainkan <b>kebocoran internal (fraud)</b> yang tidak terdeteksi.</p>
            <p>Dipimpin oleh <b>Erwin Sinaga</b>, kami mengintegrasikan kecerdasan buatan (AI) untuk menjadi 
            'Mata Elektronik' yang menjaga aset Anda 24/7 tanpa kompromi.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🎯 Misi Kami:")
        st.write("- Memberikan **Ketenangan Pikiran** bagi Business Owner.")
        st.write("- Mendeteksi anomali transaksi secara **Real-Time**.")
        st.write("- Transformasi audit manual menjadi **Sistem Otonom** yang tak bisa disuap.")

    st.divider()
    st.markdown("<h2 style='text-align: center;'>Investment & Subscription Packages</h2>", unsafe_allow_html=True)
    
    p1, p2, p3 = st.columns(3)
    def wa_link(paket):
        pesan = f"Halo Pak Erwin, saya ingin konsultasi mengenai V-GUARD paket *{paket}*."
        return f"https://wa.me/{WA_NOMOR}?text={urllib.parse.quote(pesan)}"

    with p1:
        st.markdown('<div class="card-service"><h3>📦 V-LITE</h3><h2 style="color:#d4af37">7,5 Jt</h2><hr>1 Outlet<br>Daily Alarm WA<br>Basic Analytics</div>', unsafe_allow_html=True)
        st.link_button("KONSULTASI SEKARANG", wa_link("V-LITE"))
    with p2:
        st.markdown('<div class="card-service" style="border: 4px solid #FFD700"><h3>🚀 V-PRO</h3><h2 style="color:#d4af37">15 Jt</h2><p style="color:orange; font-size:12px;"><b>MOST POPULAR</b></p><hr>5 Outlet<br><b>AI Deep Audit</b><br>Meeting Summarizer</div>', unsafe_allow_html=True)
        st.link_button("KONSULTASI SEKARANG", wa_link("V-PRO"))
    with p3:
        st.markdown('<div class="card-service"><h3>🏢 CORPORATE</h3><h2 style="color:#d4af37">25 Jt</h2><hr>Unlimited Outlet<br>Full API Integration<br>Priority AI Guard</div>', unsafe_allow_html=True)
        st.link_button("KONSULTASI SEKARANG", wa_link("CORPORATE"))

# (Halaman 2, 3, 4 Mengikuti Struktur AI yang Sudah Kita Buat)
elif halaman == "🤖 AI Auditor Engine":
    st.title("🤖 AI Auditor Engine")
    st.info("Fitur analisis data transaksi secara massal.")

elif halaman == "📝 AI Meeting Lab":
    st.title("📝 AI Meeting Summarizer")
    st.info("Fitur rangkuman rapat otomatis.")

elif halaman == "🔐 Admin Panel":
    st.title("🔐 Admin Panel WA")
    st.write("Kontrol notifikasi Alarm Merah.")
