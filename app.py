import streamlit as st
import pandas as pd
import google.generativeai as genai
import urllib.parse
import os
from PIL import Image # Library untuk memproses foto

# 1. KONFIGURASI SISTEM & API
st.set_page_config(page_title="V-GUARD AI - Revenue Protection", page_icon="🛡️", layout="wide")

# Masukkan API Key asli Anda di bawah ini
API_KEY = "ISI_KODE_AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA" 
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("API Key AI belum terkonfigurasi dengan benar di server.")

# DATA KONTAK
WA_NOMOR = "6282122190885" 

# 2. FUNGSI FOTO (Wajah Bapak Kembali)
def get_foto(lebar):
    if os.path.exists('erwin.jpg'):
        # Membuka dan menampilkan foto asli
        return st.image(Image.open('erwin.jpg'), width=lebar)
    else:
        # Ikon cadangan korporat jika file erwin.jpg belum diunggah ke GitHub
        return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)

# 3. LOGIKA LOGIN SESSION STATE
if 'role' not in st.session_state:
    st.session_state.role = None

def login():
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔐 Akses Klien/Admin")
    user = st.sidebar.text_input("Username")
    pw = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Masuk"):
        if user == "admin" and pw == "admin123":
            st.session_state.role = "admin"
            st.rerun()
        elif user == "klien" and pw == "klien123":
            st.session_state.role = "klien"
            st.rerun()
        else:
            st.sidebar.error("Akses Ditolak: Kredensial Salah")

# 4. CSS EXECUTIVE DESIGN (Landing Page Promosi Korporat)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    section[data-testid="stSidebar"] { 
        background-color: #0e1117 !important; 
        border-right: 3px solid #FFD700; 
    }
    .hero-bg { 
        background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); 
        padding: 40px; border-radius: 25px; color: white; text-align: center; 
        border-bottom: 8px solid #FFD700; box-shadow: 0 15px 35px rgba(0,0,0,0.3);
        margin-bottom: 30px;
    }
    .hero-bg h1 { font-size: 36px; color: #FFD700; }
    .card-service { 
        background: white; padding: 20px; border-radius: 20px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.1); color: #0e1117; 
        border-top: 6px solid #FFD700; text-align: center;
        height: 320px; display: flex; flex-direction: column; justify-content: space-between;
    }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(45deg, #FFD700, #b8860b) !important; 
        color: #0e1117 !important; font-weight: bold; border: none;
    }
    .roi-box {
        background-color: #fffde6; padding: 25px; border-radius: 15px;
        border: 2px solid #FFD700; text-align: center;
    }
    .sidebar-user {
        background: rgba(255,255,255,0.05); padding: 10px; border-radius: 8px;
        color: white; border: 1px solid rgba(255,215,0,0.3);
    }
    /* Styling khusus profil halaman */
    .profile-box {
        background-color: #ffffff; padding: 20px; border-radius: 12px;
        border-left: 5px solid #FFD700; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# 5. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #FFD700; margin-bottom:0px;'>🛡️ V-GUARD</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; font-size:12px; margin-top:0px;'>Revenue Protection Intelligence</p>", unsafe_allow_html=True)
    st.divider()

    # Bagian Profil dengan Foto (60px)
    col_f, col_n = st.columns([1, 2])
    with col_f:
        get_foto(60) # Foto Bapak muncul di sini
    with col_n:
        st.markdown(f"<p style='color: white; font-weight: bold; margin-bottom: 0px;'>Erwin Sinaga</p><p style='color: #FFD700; font-size: 11px;'>Founder & CEO</p>", unsafe_allow_html=True)
    st.divider()

    if st.session_state.role:
        st.markdown(f"""<div class='sidebar-user'><b>Active Session:</b> {st.session_state.role.upper()}</div>""", unsafe_allow_html=True)
        if st.button("🚪 Logout"):
            st.session_state.role = None
            st.rerun()
        st.divider()

    # Menu Utama
    halaman = st.radio("MENU UTAMA:", ["🌐 Beranda & Layanan", "🤖 AI Auditor", "📝 AI Meeting Lab"])
    
    # Menampilkan Form Login jika belum masuk
    if st.session_state.role is None:
        login()
            
    st.divider()
    st.info("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: BERANDA & PROFIL (Foto Besar di Beranda)
# ==========================================
if halaman == "🌐 Beranda & Layanan":
    # 1. Hero Banner
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Solusi Cerdas Mencegah Kebocoran Omset & Memaksimalkan Keuntungan Bisnis.</p></div>', unsafe_allow_html=True)
    
    # 2. Nilai Bisnis & Filosofi (Menampilkan Foto Profil 320px)
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        # Foto Bapak muncul besar di Landing Page
        get_foto(320)
    with col_txt:
        st.markdown("### 🛡️ Filosofi V-GUARD")
        st.markdown("""
        <div class="profile-box">
            <p style="font-size:16px; color:#444; line-height:1.7;"><b>V-Guard</b> lahir dari visi manajemen strategis untuk optimasi pendapatan Anda. 
            Kebocoran internal (fraud) adalah musuh terbesar pertumbuhan. Kami memahami celah ini.</p>
            <p style="font-size:16px; color:#444; line-height:1.7;">Sistem ini mengintegrasikan kecerdasan buatan (AI) untuk menjadi 'Mata Elektronik' yang menjaga aset Anda 24/7 tanpa kompromi.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("✅ Real-Time Fraud Detection | ✅ AI Autonomous Audit")
    st.divider()

    # 3. KALKULATOR ROI (Kunci Promosi)
    st.markdown("<h3 style='text-align: center;'>🧮 Kalkulator Penyelamatan Aset</h3>", unsafe_allow_html=True)
    c_roi1, c_roi2 = st.columns(2)
    with c_roi1:
        omset = st.number_input("Omset Bulanan (Rp):", min_value=0, value=100000000, step=10000000)
        leakage = st.slider("Estimasi Kebocoran/Fraud (%):", 0, 15, 3)
    with c_roi2:
        potensi_rugi = omset * (leakage / 100)
        st.markdown(f"""
            <div class="roi-box">
                <p style="margin:0; font-size:16px; color:#555;">Potensi Kerugian yang Dapat Dicegah per Bulan:</p>
                <h1 style="color: #d42f2f; margin:10px 0;">Rp {potensi_rugi:,.0f}</h1>
                <p style="font-size: 13px; color: #777;">Tingkatkan ROI Anda dengan menutup celah kebocoran internal otomatis.</p>
            </div>
        """, unsafe_allow_html=True)

    # 4. PAKET LAYANAN STRATEGIS
    st.divider()
    st.markdown("<h3 style='text-align: center;'>Pilih Layanan V-GUARD</h3>", unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    
    def wa_link(paket):
        pesan = f"Halo Pak Erwin, saya ingin konsultasi paket V-GUARD {paket}."
        return f"https://wa.me/{WA_NOMOR}?text={urllib.parse.quote(pesan)}"

    with p1:
        st.markdown('<div class="card-service"><div><h4>📦 V-LITE</h4><h3 style="color:#d4af37">7,5 Jt</h3><hr><p style="font-size:13px;">• 1 Outlet/Toko<br>• Daily Alarm via WA<br>• Summary Laporan Mingguan</p></div></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI SAYA", wa_link("V-LITE"))
    with p2:
        st.markdown('<div class="card-service" style="border: 3px solid #FFD700;"><div><h4>🚀 V-PRO</h4><h3 style="color:#d4af37">15 Jt</h3><hr><p style="font-size:13px;">• 5 Outlet/Toko<br>• **AI Deep Audit**
