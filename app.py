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

# 2. CSS EXECUTIVE DESIGN (Optimasi Compact)
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .hero-bg { 
        background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); 
        padding: 30px; border-radius: 20px; color: white; text-align: center; 
        border-bottom: 6px solid #FFD700; box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        margin-bottom: 25px;
    }
    .hero-bg h1 { font-size: 30px; color: #FFD700; }
    .card-service { 
        background: white; padding: 15px; border-radius: 15px; 
        box-shadow: 0 8px 20px rgba(0,0,0,0.08); color: #0e1117; 
        border-top: 5px solid #FFD700; text-align: center;
        height: 280px; display: flex; flex-direction: column; justify-content: space-between;
    }
    .stButton>button { 
        width: 100%; border-radius: 10px; height: 3em; 
        background: linear-gradient(45deg, #FFD700, #b8860b) !important; 
        color: #0e1117 !important; font-weight: bold; border: none; font-size: 14px;
    }
    .profile-box {
        background-color: #ffffff; padding: 20px; border-radius: 12px;
        border-left: 5px solid #FFD700; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
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
    with col_f: get_foto(60) # Sidebar foto lebih kecil
    with col_n:
        st.markdown(f"<div style='padding-top:5px;'><p style='color: white; font-weight: bold; margin-bottom: 0px;'>Erwin Sinaga</p><p style='color: #FFD700; font-size: 11px;'>Founder & CEO</p></div>", unsafe_allow_html=True)
    st.divider()
    halaman = st.radio("MENU UTAMA:", ["🌐 Beranda & Profil", "🤖 AI Auditor", "📝 AI Meeting Lab"])

# ==========================================
# HALAMAN 1: BERANDA & PROFIL
# ==========================================
if halaman == "🌐 Beranda & Profil":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>The Future of Corporate Revenue Protection.</p></div>', unsafe_allow_html=True)
    
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        get_foto(320) # Ukuran foto diperkecil menjadi 320px
    with col_txt:
        st.markdown("### 🛡️ FILOSOFI & PROFIL")
        st.markdown("""
        <div class="profile-box">
            <p><b>V-Guard</b> lahir dari visi manajemen strategis dan optimasi pendapatan. 
            Kami memahami bahwa musuh terbesar pertumbuhan bisnis adalah <b>kebocoran internal (fraud)</b> yang tidak terdeteksi.</p>
            <p>Sistem ini mengintegrasikan kecerdasan buatan (AI) untuk menjadi 'Mata Elektronik' 
            yang menjaga aset Anda 24/7 tanpa kompromi.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("✅ **Real-Time Fraud Detection** | ✅ **AI Autonomous Audit**")

    st.divider()
    st.markdown("<h3 style='text-align: center;'>Layanan Strategis</h3>", unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    
    def wa_link(paket):
        pesan = f"Halo Pak Erwin, saya ingin konsultasi paket V-GUARD *{paket}*."
        return f"https://wa.me/{WA_NOMOR}?text={urllib.parse.quote(pesan)}"

    with p1:
        st.markdown('<div class="card-service"><div><h4>📦 V-LITE</h4><h3 style="color:#d4af37">7,5 Jt</h3><hr><p style="font-size:13px;">1 Outlet<br>Daily Alarm WA</p></div></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI SAYA", wa_link("V-LITE"))
    with p2:
        st.markdown('<div class="card-service" style="border: 3px solid #FFD700"><div><h4>🚀 V-PRO</h4><h3 style="color:#d4af37">15 Jt</h3><hr><p style="font-size:13px;">5 Outlet<br><b>AI Deep Audit</b></p></div></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI SAYA", wa_link("V-PRO"))
    with p3:
        st.markdown('<div class="card-service"><div><h4>🏢 CORPORATE</h4><h3 style="color:#d4af37">25 Jt</h3><hr><p style="font-size:13px;">Unlimited Outlet<br>Priority Support</p></div></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI SAYA", wa_link("CORPORATE"))

# ==========================================
# HALAMAN LAIN (SIMPEL)
# ==========================================
elif halaman == "🤖 AI Auditor":
    st.title("🤖 AI Auditor Engine")
    st.info("Fitur analisis data transaksi.")

elif halaman == "📝 AI Meeting Lab":
    st.title("📝 AI Meeting Summarizer")
    st.info("Fitur rangkuman rapat otomatis.")
