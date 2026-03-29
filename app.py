import streamlit as st
import google.generativeai as genai
import os
import pandas as pd
import numpy as np
from PIL import Image

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# API KEY GEMINI (Mesin Utama Deteksi Fraud)
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

# 2. CSS STYLING
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .hero-bg { background: #0e1117; padding: 35px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 30px; }
    .card-v { background: white !important; padding: 22px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #FFD700; min-height: 400px; display: flex; flex-direction: column; justify-content: space-between; }
    .bio-section { background: #0e1117; color: white; padding: 25px; border-radius: 15px; border-left: 6px solid #FFD700; }
    .fraud-panel { background: #ffffff; padding: 20px; border-radius: 12px; border: 2px solid #d42f2f; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    f_col, n_col = st.columns([1, 2])
    with f_col: get_foto(65)
    with n_col: st.markdown(f"<b style='color:white;'>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    nav = ["🌐 Beranda", "🤖 Panel Admin (Fraud Detection)", "📊 Laporan Klien", "📝 Meeting Lab"]
    if not st.session_state.role: nav.append("🔑 Masuk Ke Sistem")
    menu = st.radio("MENU UTAMA:", nav)
    if st.session_state.role:
        if st.button("🚪 Logout"):
            st.session_state.role = None
            st.rerun()

# 4. HALAMAN BERANDA
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>The Future of Responsible AI Security & Fraud Detection</p></div>', unsafe_allow_html=True)
    c_img, c_txt = st.columns([1, 2])
    with c_img: get_foto(350)
    with c_txt:
        st.markdown(f"""
        <div class="bio-section">
            <h3 style='color:#FFD700;'>🛡️ About V-GUARD</h3>
            <p>Didirikan 2026, <b>V-GUARD</b> fokus pada deteksi fraud dan governance AI. Dengan <b>10 tahun pengalaman perbankan</b>, kami membawa standar keamanan finansial kelas tinggi ke industri AI.</p>
            <p><i>"Cegah kerugian bisnis hingga 90% dengan deteksi proaktif."</i></p>
        </div>
        """, unsafe_allow_html=True)
    st.divider()
    p1, p2, p3, p4 = st.columns(4)
    WA = "https://wa.me/6282122190885"
    with p1: 
        st.markdown('<div class="card-v"><h4>🌱 V-START</h4><hr><p>Audit mingguan UMKM.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
    with p2: 
        st.markdown('<div class="card-v"><h4>📦 V-LITE</h4><hr><p>Monitoring harian aktif.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
    with p3: 
        st.markdown('<div class="card-v" style="border:2px solid #FFD700"><h4>🚀 V-PRO</h4><hr><p>Deep AI Fraud Audit.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
    with p4: 
        st.markdown('<div class="card-v"><h4>🏢 CORPORATE</h4><hr><p>Skala Nasional.</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI CEO", WA)

# 5. PANEL ADMIN (FITUR DETEKSI FRAUD NYATA)
elif menu == "🤖 Panel Admin (Fraud Detection)":
    if st.session_state.role != "admin":
        st.warning("Silakan Login Admin untuk akses fitur deteksi.")
    else:
        st.markdown('<div class="hero-bg"><h1>AI FRAUD COMMAND CENTER</h1></div>', unsafe_allow_html=True)
        
        st.subheader("🔍 Scan Data Transaksi Klien")
        st.write("Unggah log transaksi klien (CSV/Excel) untuk dianalisis oleh Mesin V-GUARD.")
        
        up_file = st.file_uploader("Pilih file data transaksi...", type=['csv', 'xlsx'])
        
        if up_file:
            st.success("File berhasil diunggah. Menyiapkan analisis AI...")
            if st.button("🚀 Jalankan Deteksi Fraud Sistemik"):
                with st.spinner("V-GUARD sedang menganalisis pola anomali..."):
                    # Simulasi pengiriman data ke AI (Gemini)
                    prompt = "Bapak Erwin, sistem V-GUARD telah menemukan indikasi fraud pada data tersebut. Tolong berikan ringkasan risiko manajemen dan langkah mitigasi yang harus diambil
