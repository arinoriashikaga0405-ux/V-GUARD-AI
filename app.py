import streamlit as st
import google.generativeai as genai
import os
import pandas as pd
import numpy as np
from PIL import Image
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

def get_foto(lebar):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try: return st.image(Image.open('erwin.jpg'), width=lebar)
        except: return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# 2. CSS CUSTOM EXEC (PROFIL BESAR + ALARM RED ALERT)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .hero-bg { background: #0e1117; padding: 35px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 30px; }
    .bio-section { background: #0e1117; color: white; padding: 25px; border-radius: 15px; border-left: 6px solid #FFD700; }
    .card-v { background: white !important; padding: 22px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #FFD700; min-height: 400px; display: flex; flex-direction: column; justify-content: space-between; }
    .price { font-size: 1.2em; color: #FFD700; font-weight: bold; margin: 10px 0; }
    .red-alert-box { background-color: #ff4b4b; color: white; padding: 20px; border-radius: 10px; border: 3px solid black; text-align: center; font-weight: bold; animation: blinker 1.2s linear infinite; margin-top: 20px; }
    @keyframes blinker { 50% { opacity: 0.3; } }
    .invoice-warning { background-color: #fff3cd; color: #856404; padding: 15px; border-radius: 8px; border-left: 8px solid #ffcc00; margin-bottom: 15px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    f_col, n_col = st.columns([1, 2])
    with f_col: get_foto(65)
    with n_col: st.markdown("<b style='color:white;'>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    nav_options = ["🌐 Beranda (Profil & ROI)", "🤖 Panel Admin (Fraud Scan)", "📊 Monitoring Invoice", "🔑 Masuk Ke Sistem"]
    menu = st.radio("MENU UTAMA:", nav_options)
    if st.session_state.role and st.button("🚪 Logout"):
        st.session_state.role = None
        st.rerun()

# 4. BERANDA (FULL PROFIL, FILOSOFI, ROI FRAUD)
if menu == "🌐 Beranda (Profil & ROI)":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>The Future of Responsible AI Security & Fraud Detection</p></div>', unsafe_allow_html=True)
    
    # PROFIL & FILOSOFI (Muncul Dominan)
    c_img, c_txt = st.columns([1, 2])
    with c_img: get_foto(350)
    with c_txt:
        st.markdown('<div class="bio-section"><h3 style="color:#FFD700;">🛡️ About V-GUARD</h3><p>Didirikan pada 2026, <b>V-GUARD</b> adalah platform deteksi fraud dan tata kelola AI bertanggung jawab. Dibangun oleh <b>Erwin Sinaga</b> dengan pengalaman perbankan 10+ tahun (Strategic Management) untuk membawa standar kepatuhan finansial ke dalam ekosistem AI.</p><p><i>"Misi kami adalah mencegah kebocoran aset hingga 90% dengan analisis AI proaktif, memastikan setiap rupiah bisnis owner terlindungi."</i></p></div>', unsafe_allow_html=True)
    
    st.divider()
    
    # FITUR ROI FRAUD (Muncul Dominan)
    st.subheader("📈 Kalkulator ROI Pencegahan Fraud")
    st.write("Estimasikan penghematan aset bisnis Anda dengan V-GUARD.")
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        omset = st.number_input("Omset Bulanan Bisnis (Rp):", value=100000000, step=10000000)
        leak = st.slider("Estimasi Kebocoran Operasional Tanpa AI (%):", 1, 15, 3)
    with col_r2:
        saved_money = omset * (leak/100) * 0.9 # Asumsi 90% kebocoran tercegah
        st.metric(label="Potensi Aset Terselamatkan /Bulan", value=f"Rp {saved_money:,.0f}", delta="90% Efektivitas")
        st.caption("Perhitungan berdasarkan simulasi pencegahan kebocoran proaktif V-GUARD.")

    st.divider()
    
    # PAKET LAYANAN
    p1, p2, p3, p4 = st.columns(4)
    WA_LINK = "https://wa.me/6282122190885"
    with p1: 
        st.markdown('<div class="card-v"><h4>🌱 V-START</h4><div class="price">3,5 Jt /Bln</div><hr><p>Audit mingguan UMKM.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA_LINK)
    with p2: 
        st.markdown('<div class="card-v"><h4>📦 V-LITE</h4><div class="price">7,5 Jt /Bln</div><hr><p>Monitoring harian aktif.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA_LINK)
    with p3: 
        st.markdown('<div class="card-v" style="border:2px solid #FFD700"><h4>🚀 V-PRO</h4><div class="price">15 Jt /Bln</div><hr><p>Deep AI Fraud Audit.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA_LINK)
    with p4: 
        st.markdown('<div class="card-v"><h4>🏢 CORPORATE</h4><div class="price">Custom</div><hr><p>Skala Nasional.</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI CEO", WA_LINK)

# 5. PANEL ADMIN (DENGAN RED ALERT/ALARM)
elif menu == "🤖 Panel Admin (Fraud Scan)":
    if st.session_state.role != "admin": st.warning("Silakan Login Admin.")
    else:
        st.markdown('<div class="hero-bg"><h1>AI FRAUD COMMAND CENTER</h1></div>', unsafe_allow_html=True)
        up_file = st.file_uploader("Upload Data Transaksi Klien", type=['csv', 'xlsx'])
        if up_file:
            if st.button("🚀 JALANKAN DETEKSI SISTEMIK"):
                with st.spinner("Menganalisis kebocoran dana..."):
                    # TRIGGER ALARM MERAH (Red Alert)
                    st.markdown('<div class="red-alert-box">🚨 RED ALERT: TERDETEKSI POTENSI FRAUD KLIEN! 🚨</div>', unsafe_allow_html=True)
                    res = model.generate_content("Analisis mitigasi fraud untuk Founder V-GUARD Erwin Sinaga.")
                    st.write(res.text)

# 6. INVOICE MONITOR (DENGAN NOTIFIKASI)
elif menu == "📊 Monitoring Invoice":
    if not st.session_state.role: st.warning("Silakan Login.")
    else:
        st.title("📅 Dashboard Invoice")
        invoices = [{"Klien": "PT Maju Jaya", "Nominal": "Rp 25.000.000", "Jatuh Tempo": (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')}]
        for inv in invoices:
            due = datetime.strptime(inv['Jatuh Tempo'], '%Y-%m-%d')
            if due <= datetime.now() + timedelta(days=7):
                st.markdown(f'<div class="invoice-warning">⚠️ Invoice {inv["Klien"]} ({inv["Nominal"]}) segera jatuh tempo!</div>', unsafe_allow_html=True)
        st.table(invoices)

# 7. LOGIN SYSTEM (FIXED)
elif menu == "🔑 Masuk Ke Sistem":
    st.markdown('<div class="hero-bg"><h1>SECURITY LOGIN</h1></div>', unsafe_allow_html=True)
    with st.form("login_vguard"):
        u = st.text_input("User ID (Gunakan 'admin' atau 'klien')").strip().lower()
        p = st.text_input("Access Key", type="password")
        submit = st.form_submit_button("AUTHENTICATE")
        
        if submit:
            # Login Admin/Founder
            if u == "admin" and p == "Vguard2026":
                st.session_state.role = "admin"
                st.success("Akses Founder Diterima. Selamat Datang Pak Erwin.")
                st.rerun()
            # Login Klien (Perbaikan di sini)
            elif u == "klien" and p == "User2026":
                st.session_state.role = "klien"
                st.success("Akses Klien Diterima.")
                st.rerun()
            else:
                st.error("User ID atau Access Key Salah. Silakan hubungi Administrator.")
