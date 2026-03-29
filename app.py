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

# 2. CSS TAMPILAN MEWAH (Warna Biru Navy & Emas)
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

# 3. FUNGSI AMBIL FOTO (Kunci ke bapak_erwin.jpg)
def get_foto(lebar):
    if os.path.exists('bapak_erwin.jpg'):
        return st.image(Image.open('bapak_erwin.jpg'), width=lebar)
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
    halaman = st.radio("Navigasi Utama:", ["🌐 Promosi & Umum", "👥 Monitoring Klien", "🔐 Panel Admin (WhatsApp)"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: PROMOSI (DESAIN DIKUNCI)
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
        st.write("### Paket Layanan V-GUARD")
        p1, p2, p3 = st.columns(3)
        p1.markdown('<div class="card-service"><b>📦 LITE</b><br>7,5 Jt</div>', unsafe_allow_html=True)
        p2.markdown('<div class="card-service" style="border: 2px solid #FFD700"><b>🚀 PRO</b><br>15 Jt</div>', unsafe_allow_html=True)
        p3.markdown('<div class="card-service"><b>🏢 ENTERPRISE</b><br>25 Jt</div>', unsafe_allow_html=True)

# ==========================================
# HALAMAN 3: PANEL ADMIN (WhatsApp Feature)
# ==========================================
elif halaman == "🔐 Panel Admin (WhatsApp)":
    st.title("🔐 Panel Kendali AI Auditor")
    pw = st.text_input("Password Admin:", type="password")
    
    if pw == "vguard2026":
        st.success("Akses Diterima.")
        tab1, tab2 = st.tabs(["🚨 Kirim Alarm Merah", "🧾 Penagihan Invoice"])
        
        with tab1:
            st.subheader("Kirim Alarm Merah ke Owner")
            no_wa = st.text_input("No WhatsApp Owner (Contoh: 62812...):", key="wa1")
            nama_klien = st.text_input("Nama Owner/Klien:")
            selisih = st.text_input("Jumlah Selisih/Temuan (Rp):")
            
            msg_alarm = f"[🚨 V-GUARD AI AUDITOR - ALARM MERAH]\n\nYth. {nama_klien},\n\nSistem AI V-GUARD mendeteksi Anomali Transaksi (Alarm Merah) pada bisnis Anda.\n\n🔍 Temuan AI: Terdeteksi selisih sebesar Rp {selisih} (Indikasi Kebocoran).\n\nSegera lakukan audit fisik untuk mencegah kerugian lebih lanjut.\n\nSalam,\nErwin Sinaga - Founder V-GUARD"
            
            if st.button("Generate Link WhatsApp Alarm"):
                link_wa = f"https://wa.me/{no_wa}?text={urllib.parse.quote(msg_alarm)}"
                st.link_button("🚀 KIRIM VIA WHATSAPP SEKARANG", link_wa)

        with tab2:
            st.subheader("Penagihan Invoice Jatuh Tempo")
            no_wa2 = st.text_input("No WhatsApp Klien (Contoh: 62812...):", key="wa2")
            nama_klien2 = st.text_input("Nama Klien:", key="nk2")
            total = st.text_input("Total Tagihan (Rp):")
            
            msg_inv = f"[🛡️ V-GUARD SYSTEMS - PENGINGAT PEMBAYARAN]\n\nHalo {nama_klien2},\n\nKami menginformasikan bahwa dukungan AI Auditor V-GUARD Anda telah memasuki masa jatuh tempo.\n\n💰 Total Tagihan: Rp {total}\n🏦 Pembayaran: Bank Mandiri/BCA a/n Erwin Sinaga\n\nMohon segera diselesaikan agar proteksi Alarm Merah tetap berjalan.\n\nTerima kasih,\nErwin Sinaga"
            
            if st.button("Generate Link WhatsApp Invoice"):
                link_wa2 = f"https://wa.me/{no_wa2}?text={urllib.parse.quote(msg_inv)}"
                st.link_button("🧾 KIRIM TAGIHAN VIA WHATSAPP", link_wa2)

else:
    st.title("👥 Monitoring Klien")
    st.info("Sistem AI memantau anomali secara real-time.")
