import streamlit as st
import pandas as pd
import google.generativeai as genai
import urllib.parse
import os
from PIL import Image

# 1. KONFIGURASI DASAR (Harus di paling atas)
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# 2. DEFINISI FUNGSI FOTO (Didefinisikan di awal agar tidak NameError)
def get_foto(lebar):
    try:
        if os.path.exists('erwin.jpg'):
            return st.image(Image.open('erwin.jpg'), width=lebar)
        else:
            # Ikon cadangan jika file foto belum ada di GitHub
            return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)
    except:
        st.write("📸")

# 3. KONFIGURASI AI
API_KEY = "ISI_KODE_API_BAPAK" 
try:
    genai.configure(api_key=API_KEY)
except:
    pass

WA_NOMOR = "6282122190885" 

# 4. LOGIKA LOGIN
if 'role' not in st.session_state:
    st.session_state.role = None

def login_vguard():
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔐 Login Akses")
    with st.sidebar.form("login_form"):
        u = st.text_input("Username").strip().lower()
        p = st.text_input("Password", type="password").strip()
        submit = st.form_submit_button("Masuk Ke Sistem")
        if submit:
            if u == "admin" and p == "Vguard2026":
                st.session_state.role = "admin"
                st.rerun()
            elif u == "klien" and p == "User2026":
                st.session_state.role = "klien"
                st.rerun()
            else:
                st.sidebar.error("Login Gagal!")

# 5. CSS DESIGN (Tampilan Dashboard)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 3px solid #FFD700; }
    .hero-bg { background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); padding: 30px; border-radius: 20px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 25px; }
    .card-service { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); border-top: 5px solid #FFD700; text-align: center; height: 320px; }
</style>
""", unsafe_allow_html=True)

# 6. SIDEBAR & NAVIGASI (Perbaikan Menu)
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>🛡️ V-GUARD</h1>", unsafe_allow_html=True)
    
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(60)
    with col_n: st.markdown("<b style='color:white;'>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    
    st.divider()
    
    # Penentuan Menu berdasarkan Role
    if st.session_state.role == "admin":
        opsi_menu = ["🌐 Beranda", "🤖 AI Auditor (Admin)", "📝 Meeting Lab"]
    elif st.session_state.role == "klien":
        opsi_menu = ["🌐 Beranda", "📊 Dashboard Klien", "📝 Meeting Lab"]
    else:
        opsi_menu = ["🌐 Beranda", "📝 Meeting Lab"]
    
    menu = st.radio("NAVIGASI:", opsi_menu)

    if st.session_state.role:
        st.success(f"Mode: {st.session_state.role.upper()}")
        if st.button("🚪 Logout"):
            st.session_state.role = None
            st.rerun()
    else:
        login_vguard()

# ==========================================
# LOGIKA HALAMAN (LANDING PAGE)
# ==========================================
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(350)
    with c2:
        st.subheader("🛡️ Proteksi Aset & Deteksi Fraud")
        st.write("V-Guard menutup celah kebocoran operasional bisnis Anda dengan AI.")
        st.info("Gunakan menu navigasi untuk mengakses fitur utama.")

elif menu == "🤖 AI Auditor (Admin)":
    st.title("🤖 AI Auditor Engine (Halaman Admin)")
    st.write("Selamat Datang di Pusat Audit Strategis.")
    # Fitur upload khusus admin
    f = st.file_uploader("Upload Transaksi", type=['csv','xlsx'])

elif menu == "📊 Dashboard Klien":
    st.title("📊 Dashboard Laporan Klien")
    st.write("Halaman ini khusus untuk menampilkan statistik performa bisnis Anda.")
    st.metric("Estimasi Profit Aman", "Rp 125.000.000", "+5%")

elif menu == "📝 Meeting Lab":
    st.title("📝 AI Meeting Lab")
    st.info("Fitur ringkuman rapat otomatis sedang dikembangkan.")
