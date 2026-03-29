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

# Simulasi Data Invoice (Bisa dikoneksikan ke Database nantinya)
if 'invoices' not in st.session_state:
    st.session_state.invoices = [
        {"klien": "PT Maju Jaya", "nominal": "Rp 25.000.000", "jatuh_tempo": (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')},
        {"klien": "Toko Berkah", "nominal": "Rp 5.500.000", "jatuh_tempo": (datetime.now() + timedelta(days=15)).strftime('%Y-%m-%d')},
    ]

# 2. CSS STYLING EXECUTIVE
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .hero-bg { background: #0e1117; padding: 35px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 30px; }
    .bio-section { background: #0e1117; color: white; padding: 25px; border-radius: 15px; border-left: 6px solid #FFD700; }
    .red-alert { background: #ff4b4b; color: white; padding: 20px; border-radius: 10px; border: 3px solid #000; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0.5; } }
    .invoice-notif { background: #fff3cd; color: #856404; padding: 15px; border-radius: 8px; border-left: 5px solid #ffeeba; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; color:white;'><b>Erwin Sinaga</b><br><small>Founder & CEO</small></div>", unsafe_allow_html=True)
    st.divider()
    menu = st.radio("MENU UTAMA:", ["🌐 Beranda", "🤖 Panel Admin (Fraud Scan)", "📊 Monitoring Invoice", "🔑 Masuk Ke Sistem"])
    if st.session_state.role and st.button("🚪 Logout"):
        st.session_state.role = None
        st.rerun()

# 4. HALAMAN BERANDA
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Mencegah Kerugian Owner Melalui Deteksi Proaktif</p></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-section">
        <h3 style='color:#FFD700;'>🛡️ Filosofi V-GUARD</h3>
        <p>Dengan pengalaman perbankan lebih dari 10 tahun, kami memastikan setiap rupiah aset Anda terlindungi. 
        Sistem kami dirancang untuk memberikan <b>Alarm Merah</b> seketika saat kecurangan terdeteksi.</p>
    </div>
    """, unsafe_allow_html=True)

# 5. PANEL ADMIN & ALARM MERAH
elif menu == "🤖 Panel Admin (Fraud Scan)":
    if st.session_state.role != "admin":
        st.warning("Akses Khusus Founder & Admin.")
    else:
        st.title("🔍 Fraud Detection Scanner")
        up_file = st.file_uploader("Upload Data Transaksi Klien", type=['csv', 'xlsx'])
        if up_file:
            if st.button("🚀 Jalankan Analisis AI"):
                with st.spinner("V-GUARD sedang bekerja..."):
                    # SIMULASI ALARM MERAH (Input AI)
                    st.markdown("""
                    <div class="red-alert">
                        🚨 ALARM MERAH: TERDETEKSI POLA TRANSAKSI MENCURIGAKAN PADA LOG KLIEN!
                    </div>
                    """, unsafe_allow_html=True)
                    res = model.generate_content("Berikan langkah mitigasi fraud untuk Bapak Erwin Sinaga.")
                    st.write(res.text)

# 6. MONITORING INVOICE & NOTIFIKASI JATUH TEMPO
elif menu == "📊 Monitoring Invoice":
    if not st.session_state.role:
        st.warning("Silakan Login.")
    else:
        st.title("📅 Invoice & Payment Monitor")
        
        # Logika Notifikasi Jatuh Tempo (7 hari)
        for inv in st.session_state.invoices:
            due_date = datetime.strptime(inv['jatuh_tempo'], '%Y-%m-%d')
            if due_date <= datetime.now() + timedelta(days=7):
                st.markdown(f"""
                <div class="invoice-notif">
                    ⚠️ <b>Peringatan Jatuh Tempo:</b> Invoice {inv['klien']} sebesar {inv['nominal']} 
                    akan jatuh tempo pada {inv['jatuh_tempo']}!
                </div>
                """, unsafe_allow_html=True)
        
        st.subheader("Daftar Invoice")
        st.table(st.session_state.invoices)

# 7. LOGIN
elif menu == "🔑 Masuk Ke Sistem":
    with st.form("l"):
        u = st.text_input("User ID")
        p = st.text_input("Access Key", type="password")
        if st.form_submit_button("Authenticate"):
            if u == "admin" and p == "Vguard2026": 
                st.session_state.role = "admin"
                st.rerun()
            else: st.error("Akses Ditolak")
