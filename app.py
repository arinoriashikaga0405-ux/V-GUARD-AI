import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os
from datetime import datetime
import urllib.parse

# 1. KONFIGURASI SISTEM
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Konfigurasi AI (Masukkan API Key Bapak di sini)
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. CSS TAMPILAN MEWAH
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
    .founder-text { display: flex; flex-direction: column; justify-content: center; height: 80px; }
    </style>
    """, unsafe_allow_html=True)

# 3. FUNGSI AMBIL FOTO (Kunci ke erwin.jpg)
def get_foto(lebar):
    # Menggunakan nama file yang Bapak informasikan
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
        st.markdown("""
            <div class='founder-text'>
                <p style='color: white; font-weight: bold; margin-bottom: 0px;'>Erwin Sinaga</p>
                <p style='color: #FFD700; font-size: 11px;'>Founder V-GUARD</p>
            </div>
        """, unsafe_allow_html=True)
    st.divider()
    halaman = st.radio("Navigasi:", ["🌐 Promosi & Umum", "👥 Monitoring Klien", "🔐 Panel Admin (WhatsApp)"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: PROMOSI
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
        get_foto(350) 
    with c2:
        st.markdown("## FILOSOFI & PROFIL")
        st.write("""
        V-Guard bukan sekadar software, tapi **AI Auditor** yang memberikan **Alarm Merah** ke Business Owner 
        untuk mendeteksi kebocoran dana, menagih piutang lewat WA, dan mengirim laporan mingguan 
        ke Klien setiap minggu. 
        """)
        st.info("📍 Berdomisili di Tangerang, melayani audit digital seluruh Indonesia.")
        st.write("### Paket Layanan")
        p1, p2, p3 = st.columns(3)
        p1.markdown('<div class="card-service"><b>📦 LITE</b><br>7,5 Jt</div>', unsafe_allow_html=True)
        p2.markdown('<div class="card-service" style="border: 2px solid #FFD700"><b>🚀 PRO</b><br>15 Jt</div>', unsafe_allow_html=True)
        p3.markdown('<div class="card-service"><b>🏢 ENTERPRISE</b><br>25 Jt</div>', unsafe_allow_html=True)

# ==========================================
# HALAMAN 3: PANEL ADMIN (WhatsApp Feature)
# ==========================================
elif halaman == "🔐 Panel Admin (WhatsApp)":
    st.title("🔐 Panel Kendali WhatsApp")
    pw = st.text_input("Password Admin:", type="password")
    if pw == "vguard2026":
        st.success("Akses Diterima.")
        t1, t2 = st.tabs(["🚨 Alarm Merah", "🧾 Penagihan Invoice"])
        with t1:
            wa_num = st.text_input("No WA Owner (628...):")
            owner = st.text_input("Nama Owner:")
            txt_alarm = f"[🚨 V-GUARD ALARM MERAH]\n\nYth. {owner},\nSistem mendeteksi selisih transaksi (Kebocoran Dana).\nSegera cek laporan terbaru di sistem.\n\nSalam,\nErwin Sinaga"
            if st.button("Kirim Alarm Merah"):
                st.link_button("🚀 Buka WhatsApp", f"https://wa.me/{wa_num}?text={urllib.parse.quote(txt_alarm)}")
        with t2:
            wa_num2 = st.text_input("No WA Klien:", key="wa2")
            nominal = st.text_input("Total Tagihan (Rp):")
            txt_inv = f"[🛡️ V-GUARD INVOICE]\n\nHalo,\nTagihan V-Guard Anda sebesar Rp {nominal} telah jatuh tempo.\nMohon segera diselesaikan.\n\nTerima kasih,\nErwin Sinaga"
            if st.button("Kirim Invoice"):
                st.link_button("🧾 Buka WhatsApp", f"https://wa.me/{wa_num2}?text={urllib.parse.quote(txt_inv)}")
else:
    st.title("👥 Monitoring Klien")
    st.info("Sistem AI V-Guard sedang memantau data.")
