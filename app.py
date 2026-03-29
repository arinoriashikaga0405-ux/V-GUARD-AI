import streamlit as st
import pandas as pd
import google.generativeai as genai
import urllib.parse
import os
from PIL import Image

# 1. KONFIGURASI SISTEM
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Konfigurasi AI - Ganti dengan API Key Bapak
API_KEY = "ISI_KODE_API_BAPAK_DI_SINI" 
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Gagal konfigurasi AI: {e}")

# DATA KONTAK
WA_NOMOR = "6282122190885" 

# 2. LOGIKA LOGIN
if 'role' not in st.session_state:
    st.session_state.role = None

def login():
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔐 Akses Sistem")
    user = st.sidebar.text_input("Username", key="user_in")
    pw = st.sidebar.text_input("Password", type="password", key="pw_in")
    if st.sidebar.button("Masuk"):
        if user == "admin" and pw == "admin123":
            st.session_state.role = "admin"
            st.rerun()
        elif user == "klien" and pw == "klien123":
            st.session_state.role = "klien"
            st.rerun()
        else:
            st.sidebar.error("Username/Password Salah")

# 3. FUNGSI FOTO (Wajah Bapak)
def tampilkan_foto(lebar):
    if os.path.exists('erwin.jpg'):
        return st.image(Image.open('erwin.jpg'), width=lebar)
    else:
        # Ikon cadangan jika file di GitHub belum ada
        return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)

# 4. CSS EXECUTIVE DESIGN (Tanda kutip sudah diperbaiki total)
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
    .profile-box {
        background-color: #ffffff; padding: 20px; border-radius: 12px;
        border-left: 5px solid #FFD700; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# 5. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #FFD700; margin-bottom:0px;'>🛡️ V-GUARD</h1>", unsafe_allow_html=True)
    st.divider()

    # Foto di Sidebar
    col_f, col_n = st.columns([1, 2])
    with col_f:
        tampilkan_foto(60)
    with col_n:
        st.markdown("<p style='color: white; font-weight: bold; margin-bottom: 0px;'>Erwin Sinaga</p><p style='color: #FFD700; font-size: 11px;'>Founder & CEO</p>", unsafe_allow_html=True)
    st.divider()

    if st.session_state.role:
        st.markdown(f"<p style='color:white;'>Mode: {st.session_state.role.upper()}</p>", unsafe_allow_html=True)
        if st.button("🚪 Logout"):
            st.session_state.role = None
            st.rerun()
    
    halaman = st.radio("MENU UTAMA:", ["🌐 Beranda & Layanan", "🤖 AI Auditor", "📝 AI Meeting Lab"])
    
    if not st.session_state.role:
        login()

# ==========================================
# HALAMAN 1: BERANDA
# ==========================================
if halaman == "🌐 Beranda & Layanan":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection & Fraud Detection Intelligence.</p></div>', unsafe_allow_html=True)
    
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        tampilkan_foto(350)
    with col_txt:
        st.markdown("### 🛡️ Mengapa Bisnis Anda Membutuhkan V-GUARD?")
        st.markdown("""
        <div class="profile-box">
            <p>V-Guard adalah sistem berbasis AI untuk optimasi pendapatan. 
            Kami mendeteksi <b>kebocoran internal (fraud)</b> yang tidak terlihat oleh sistem biasa.</p>
            <p>Mulai amankan omset Anda hari ini dengan teknologi Audit Otonom.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Kalkulator
    st.markdown("<h3 style='text-align: center;'>🧮 Kalkulator Penyelamatan Aset</h3>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        omset = st.number_input("Omset Bulanan (Rp):", min_value=0, value=100000000, step=10000000)
        leak = st.slider("Estimasi Kebocoran (%):", 0, 15, 3)
    with c2:
        rugi = omset * (leak / 100)
        st.markdown(f'<div class="roi-box"><p>Potensi Kerugian yang Dapat Dicegah:</p><h1 style="color:#d42f2f;">Rp {rugi:,.0f}</h1></div>', unsafe_allow_html=True)

    st.divider()
    
    # Layanan
    p1, p2, p3 = st.columns(3)
    def wa_link(pkt):
        msg = f"Halo Pak Erwin, saya tertarik paket {pkt}."
        return f"https://wa.me/{WA_NOMOR}?text={urllib.parse.quote(msg)}"

    with p1:
        st.markdown('<div class="card-service"><h4>📦 V-LITE</h4><h3>7,5 Jt</h3><hr><p>1 Outlet<br>Daily Alarm WA</p></div>', unsafe_allow_html=True)
        st.link_button("KONSULTASI", wa_link("V-LITE"))
    with p2:
        st.markdown('<div class="card-service" style="border:3px solid #FFD700"><h4>🚀 V-PRO</h4><h3>15 Jt</h3><hr><p>5 Outlet<br>AI Deep Audit</p></div>', unsafe_allow_html=True)
        st.link_button("KONSULTASI", wa_link("V-PRO"))
    with p3:
        st.markdown('<div class="card-service"><h4>🏢 CORPORATE</h4><h3>25 Jt</h3><hr><p>Unlimited<br>Priority Support</p></div>', unsafe_allow_html=True)
        st.link_button("KONSULTASI", wa_link("CORPORATE"))

# ==========================================
# HALAMAN 2: AI AUDITOR (Admin Only)
# ==========================================
elif halaman == "🤖 AI Auditor":
    st.title("🤖 AI Auditor Engine")
    if st.session_state.role != "admin":
        st.warning("Silakan login sebagai ADMIN di sidebar.")
    else:
        file = st.file_uploader("Unggah Transaksi", type=["csv", "xlsx"])
        if file:
            df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
            st.dataframe(df.head())
            if st.button("Audit Data"):
                if 'nominal' in df.columns:
                    anomali = df[df['nominal'] > (df['nominal'].mean() * 3)]
                    st.success(f"Ditemukan {len(anomali)} kecurigaan fraud.")
                    st.table(anomali)

elif halaman == "📝 AI Meeting Lab":
    st.title("📝 AI Meeting Lab")
    st.info("Fitur Summary Rapat Segera Hadir.")
