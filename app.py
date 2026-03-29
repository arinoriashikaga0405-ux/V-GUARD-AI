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

# Konfigurasi AI (Masukkan kembali API Key Bapak di sini)
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# NOMOR WHATSAPP BAPAK
WA_NOMOR = "6282125691947" 

# 2. CSS TAMPILAN PREMIUM
st.markdown("""
    <style>
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; color: white !important; }
    .hero-bg { 
        background-color: #0e1117; padding: 50px; border-radius: 20px; color: white; 
        text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px;
    }
    .card-service {
        background-color: white; padding: 25px; border-radius: 15px; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.2); text-align: left; height: 100%; color: #0e1117;
        border-top: 5px solid #FFD700;
    }
    .card-title { color: #0e1117; font-size: 20px; font-weight: bold; margin-bottom: 10px; text-align: center; }
    .card-price { color: #d4af37; font-size: 24px; font-weight: bold; text-align: center; margin-bottom: 15px; }
    .founder-text { display: flex; flex-direction: column; justify-content: center; height: 80px; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #FFD700 !important; color: #0e1117 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. FUNGSI AMBIL FOTO (Kunci ke erwin.jpg)
def get_foto(lebar):
    if os.path.exists('erwin.jpg'):
        return st.image(Image.open('erwin.jpg'), width=lebar)
    else:
        return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)

# 4. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD SYSTEMS")
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
    halaman = st.radio("Navigasi:", ["🌐 Beranda & Layanan", "🤖 AI Auditor (Upload Data)", "🔐 Panel Kontrol WA"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: BERANDA & DETAIL LAYANAN
# ==========================================
if halaman == "🌐 Beranda & Layanan":
    st.markdown("""
        <div class="hero-bg">
            <h1 style='color: #FFD700;'>V-GUARD AI SYSTEMS</h1>
            <h3>AI Auditor Terpercaya untuk Bisnis Anda.</h3>
            <p>Hentikan Kebocoran Finansial Sekarang.</p>
        </div>
        """, unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c1:
        get_foto(350) 
    with c2:
        st.markdown("## SOLUSI V-GUARD")
        st.write("🛡️ V-Guard hadir sebagai tameng finansial bagi pemilik bisnis (SME/UMKM). Kami menggunakan kecerdasan buatan untuk memastikan aset Anda terlindungi.")
        
        st.markdown("### ✨ Fitur Unggulan:")
        st.markdown("- **🚨 Alarm Merah:** Notifikasi instan saat terdeteksi selisih.")
        st.markdown("- **🤖 AI Deep Audit:** Analisis data transaksi otomatis.")
        st.markdown("- **📊 Laporan Mingguan:** Ringkasan audit langsung ke WhatsApp.")

    st.divider()
    st.markdown("<h2 style='text-align: center;'>Pilih Paket Proteksi Anda</h2>", unsafe_allow_html=True)
    
    p1, p2, p3 = st.columns(3)
    def wa_link(paket):
        pesan = f"Halo Pak Erwin, saya tertarik dengan paket V-GUARD *{paket}*."
        return f"https://wa.me/{WA_NOMOR}?text={urllib.parse.quote(pesan)}"

    with p1:
        st.markdown('<div class="card-service"><div class="card-title">📦 V-LITE</div><div class="card-price">7,5 Jt <small>/bln</small></div><ul><li>1 Outlet</li><li>Alarm Merah</li></ul></div>', unsafe_allow_html=True)
        st.link_button("Konsultasi Lite", wa_link("V-LITE"))
    with p2:
        st.markdown('<div class="card-service"><div class="card-title">🚀 V-PRO</div><div class="card-price">15 Jt <small>/bln</small></div><p style="text-align:center; color:orange;"><b>POPULER</b></p><ul><li>5 Outlet</li><li>AI Deep Audit</li></ul></div>', unsafe_allow_html=True)
        st.link_button("Konsultasi Pro", wa_link("V-PRO"))
    with p3:
        st.markdown('<div class="card-service"><div class="card-title">🏢 V-ENTERPRISE</div><div class="card-price">25 Jt <small>/bln</small></div><ul><li>Unlimited Outlet</li><li>API Custom</li></ul></div>', unsafe_allow_html=True)
        st.link_button("Konsultasi Enterprise", wa_link("V-ENTERPRISE"))

# ==========================================
# HALAMAN 2: AI AUDITOR
# ==========================================
elif halaman == "🤖 AI Auditor (Upload Data)":
    st.title("🤖 Analisis Data AI Auditor")
    uploaded_file = st.file_uploader("Pilih File Excel/CSV", type=['csv', 'xlsx'])
    if uploaded_file:
        if st.button("JALANKAN AUDIT AI"):
            st.info("AI V-Guard sedang menganalisis data...")

# ==========================================
# HALAMAN 3: PANEL KONTROL WA
# ==========================================
elif halaman == "🔐 Panel Kontrol WA":
    st.title("🔐 Panel Admin")
    pw = st.text_input("Password Admin:", type="password")
    if pw == "vguard2026":
        st.success("Akses Diterima.")
        t1, t2, t3 = st.tabs(["🚨 Alarm Merah", "🧾 Penagihan WA", "📊 Laporan Mingguan"])
        with t1:
            wa1 = st.text_input("No WA Owner (628...):")
            msg1 = "*[🚨 V-GUARD ALARM MERAH]*\nSistem mendeteksi anomali. Segera cek sistem."
            if st.button("Kirim Alarm"):
                st.link_button("🚀 Buka WA", f"https://wa.me/{wa1}?text={urllib.parse.quote(msg1)}")
        # ... (Fitur lainnya mengikuti pola yang sama)
