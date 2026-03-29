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

# Konfigurasi AI (Gunakan API Key Bapak)
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# DATA KONTAK TERBARU PAK ERWIN
WA_NOMOR = "6282122190885" 

# 2. CSS EXECUTIVE DESIGN
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; color: white !important; border-right: 2px solid #FFD700; }
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
    </style>
    """, unsafe_allow_html=True)

# 3. FUNGSI FOTO
def get_foto(lebar):
    if os.path.exists('erwin.jpg'):
        return st.image(Image.open('erwin.jpg'), width=lebar)
    else:
        return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)

# 4. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #FFD700;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(80)
    with col_n:
        st.markdown(f"<div style='padding-top:10px;'><p style='color: white; font-weight: bold; margin-bottom: 0px;'>Erwin Sinaga</p><p style='color: #FFD700; font-size: 11px;'>Founder & CEO</p></div>", unsafe_allow_html=True)
    st.divider()
    halaman = st.radio("MENU UTAMA:", ["🌐 Beranda", "🤖 AI Auditor", "📝 AI Meeting Summarizer", "🔐 Panel WA Admin"])
    st.divider()
    st.info("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: BERANDA
# ==========================================
if halaman == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Audit Digital & Deteksi Fraud Skala Corporate.</p></div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(350)
    with c2:
        st.markdown("## SISTEM PROTEKSI ASET")
        st.write("V-Guard menggunakan AI mutakhir untuk mengawasi setiap transaksi bisnis Anda, mendeteksi kecurangan secara real-time, dan mengirimkan Alarm Merah langsung ke WhatsApp Anda.")
        st.success("🎯 Fokus pada Profit, Biarkan V-Guard Menjaga Aset Anda.")

    st.divider()
    p1, p2, p3 = st.columns(3)
    def wa_link(paket):
        pesan = f"Halo Pak Erwin, saya ingin konsultasi paket V-GUARD *{paket}*."
        return f"https://wa.me/{WA_NOMOR}?text={urllib.parse.quote(pesan)}"

    with p1:
        st.markdown('<div class="card-service"><h3>📦 V-LITE</h3><h2 style="color:#d4af37">7,5 Jt</h2><p>1 Outlet<br>Daily Alarm WA</p></div>', unsafe_allow_html=True)
        st.link_button("PILIH PAKET", wa_link("V-LITE"))
    with p2:
        st.markdown('<div class="card-service" style="border: 3px solid #FFD700"><h3>🚀 V-PRO</h3><h2 style="color:#d4af37">15 Jt</h2><p>5 Outlet<br><b>AI Deep Audit</b></p></div>', unsafe_allow_html=True)
        st.link_button("PILIH PAKET", wa_link("V-PRO"))
    with p3:
        st.markdown('<div class="card-service"><h3>🏢 CORPORATE</h3><h2 style="color:#d4af37">25 Jt</h2>
