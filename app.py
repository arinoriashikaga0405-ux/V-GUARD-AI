import streamlit as st
import google.generativeai as genai
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# API KEY GEMINI
GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Koneksi AI Terputus.")

if 'role' not in st.session_state:
    st.session_state.role = None

# Simulasi Data Invoice untuk Notifikasi
if 'invoices' not in st.session_state:
    st.session_state.invoices = [
        {"Klien": "PT Sumber Rejeki", "Nominal": "Rp 45.000.000", "Jatuh Tempo": (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')},
        {"Klien": "UD Lancar Jaya", "Nominal": "Rp 12.500.000", "Jatuh Tempo": (datetime.now() + timedelta(days=12)).strftime('%Y-%m-%d')},
    ]

# 2. CSS CUSTOM UNTUK ALARM & NOTIFIKASI
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .hero-bg { background: #0e1117; padding: 35px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 30px; }
    .red-alert-box { 
        background-color: #ff4b4b; 
        color: white; 
        padding: 25px; 
        border-radius: 10px; 
        border: 4px solid black; 
        text-align: center;
        font-weight: bold;
        animation: blinker 1.2s linear infinite;
        margin-bottom: 20px;
    }
    @keyframes blinker { 50% { opacity: 0.3; } }
    .invoice-warning { 
        background-color: #fff3cd; 
        color: #856404; 
        padding: 15px; 
        border-radius: 8px; 
        border-left: 8px solid #ffcc00;
        margin-bottom: 15px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; color:white;'><b>Erwin Sinaga</b><br><small>Founder & CEO</small></div>", unsafe_allow_html=True)
    st.divider()
    menu = st.radio("MENU UTAMA:", ["🌐 Beranda", "🤖 Panel Admin (Fraud Scan)", "📊 Monitoring Invoice", "🔑 Masuk Ke Sistem"])

# 4. HALAMAN BERANDA
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Mencegah Kerugian Owner Melalui Deteksi Proaktif</p></div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background: #0e1117; color: white; padding: 25px; border-radius: 15px; border-left: 6px solid #FFD700;">
        <h3 style='color:#FFD700;'>🛡️ Filosofi V-GUARD</h3>
        <p>Dengan pengalaman perbankan lebih dari 10 tahun, kami memastikan setiap rupiah aset Anda terlindungi. 
        Sistem dirancang untuk memberikan <b>Alarm Merah</b> seketika saat kecurangan terdeteksi.</p>
    </div>
    """, unsafe_allow_html=True)

# 5. PANEL ADMIN: FITUR ALARM MERAH
elif menu == "🤖 Panel Admin (Fraud Scan)":
    if st.session_state.role != "admin":
        st.warning("Halaman ini hanya untuk akses Founder (Erwin Sinaga).")
    else:
        st.markdown('<div class="hero-bg"><h1>FRAUD COMMAND CENTER</h1></div>', unsafe_allow_html=True)
        up_file = st.file_uploader("Upload Data Transaksi untuk Analisis Keamanan", type=['csv', 'xlsx'])
        
        if up_file:
            st.info("File berhasil diterima. Menyiapkan pemindaian anomali...")
            if st.button("🚀 JALANKAN SCAN DETEKSI KERUGIAN"):
                with st.spinner("AI sedang memproses data..."):
                    # TRIGGER ALARM MERAH
                    st.markdown("""
                    <div class="red-alert-box">
                        🚨 ALARM MERAH: TERDETEKSI POTENSI KEBOCORAN DANA / FRAUD SISTEMIK! 🚨
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Analisis dari AI
                    res = model.generate_content("Analisis singkat risiko fraud dan langkah mitigasi untuk Bapak Erwin Sinaga.")
                    st.error("Laporan Analisis AI:")
                    st.write(res.text)

# 6. MONITORING INVOICE: FITUR NOTIFIKASI JATUH TEMPO
elif menu == "📊 Monitoring Invoice":
    if not st.session_state.role:
        st.warning("Silakan Login terlebih dahulu.")
    else:
        st.title("📅 Dashboard Monitoring Pembayaran")
        
        # Logika Deteksi Jatuh Tempo Otomatis
        st.subheader("🔔 Notifikasi Sistem")
        ada_peringatan = False
        for inv in st.session_state.invoices:
            due = datetime.strptime(inv['Jatuh Tempo'], '%Y-%m-%d')
            # Cek jika jatuh tempo dalam 7 hari atau sudah lewat
            if due <= datetime.now() + timedelta(days=7):
                ada_peringatan = True
                st.markdown(f"""
                <div class="invoice-warning">
                    ⚠️ PERINGATAN: Invoice {inv['Klien']} ({inv['Nominal']}) 
                    akan jatuh tempo pada {inv['Jatuh Tempo']}!
                </div>
                """, unsafe_allow_html=True)
        
        if not ada_peringatan:
            st.success("Tidak ada invoice yang mendekati jatuh tempo saat ini.")
            
        st.divider()
        st.subheader("Detail Tagihan Aktif")
        st.table(st.session_state.invoices)

# 7. LOGIN SYSTEM
elif menu == "🔑 Masuk Ke Sistem":
    with st.form("login_vguard"):
        u = st.text_input("User ID").strip()
        p = st.text_input("Access Key", type="password")
        if st.form_submit_button("LOGIN"):
            if u.lower() == "admin" and p == "Vguard2026":
                st.session_state.role = "admin"
                st.success("Akses Founder Diterima.")
                st.rerun()
            else:
                st.error("Kredensial salah.")
