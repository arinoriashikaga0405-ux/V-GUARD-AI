import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from PIL import Image

st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"

if GOOGLE_API_KEY:
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except:
        st.error("Gagal mengonfigurasi AI.")

def get_foto(lebar):
    try:
        if os.path.exists('erwin.jpg'):
            return st.image(Image.open('erwin.jpg'), width=lebar)
        else:
            return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)
    except:
        st.write("📸")

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
                st.sidebar.error("Username/Password Salah")

st.markdown("""<style>
    .stApp { background-color: #f4f6f9; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 3px solid #FFD700; }
    .hero-bg { background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); padding: 30px; border-radius: 20px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 25px; }
    .card-service { 
        background: white; 
        padding: 30px; 
        border-radius: 15px; 
        box-shadow: 0 8px 20px rgba(0,0,0,0.1); 
        border-top: 8px solid #FFD700; 
        text-align: center; 
        height: 380px; 
        display: flex; 
        flex-direction: column; 
        justify-content: space-between;
    }
    .card-service h4 { font-size: 24px; font-weight: bold; color: #1a1a1a; margin-bottom: 10px; }
    .card-service h3 { font-size: 32px; color: #d42f2f; font-weight: bold; margin: 15px 0; }
    .card-service p { font-size: 18px; line-height: 1.6; color: #444; }
    .stLinkButton button { width: 100%; height: 55px; font-size: 18px !important; font-weight: bold; background-color: #FFD700 !important; color: #0e1117 !important; border-radius: 10px; }
</style>""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #FFD700;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    col_f, col_n = st.columns([1, 2])
    with col_f: 
        get_foto(60)
    with col_n: 
        st.markdown("<b style='color:white; font-size:18px;'>Erwin Sinaga</b><br><span style='color:#FFD700;'>Founder & CEO</span>", unsafe_allow_html=True)
    st.divider()

    opsi = ["🌐 Beranda", "📝 Meeting Lab"]
    if st.session_state.role == "admin":
        opsi.insert(1, "🤖 AI Auditor (Admin)")
    elif st.session_state.role == "klien":
        opsi.insert(1, "📊 Dashboard Klien")
    
    menu = st.radio("NAVIGASI UTAMA:", opsi)

    if st.session_state.role:
        st.success(f"Mode: {st.session_state.role.upper()}")
        if st.button("🚪 Logout"):
            st.session_state.role = None
            st.rerun()
    else:
        login_vguard()

if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p style="font-size:20px;">Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    
    c_roi1, c_roi2 = st.columns([1, 2])
    with c_roi1: 
        get_foto(350)
    with c_roi2:
        st.subheader("🛡️ Proteksi Aset & Deteksi Fraud")
        st.write("Gunakan teknologi AI V-GUARD untuk amankan profit dan deteksi kebocoran bisnis.")
        omset = st.number_input("Omset Bulanan (Rp):", value=100000000)
        leak = st.slider("Estimasi Kebocoran (%):", 0, 15, 3)
        st.markdown(f"### Potensi Penyelamatan: :red[Rp {omset*(leak/100):,.0f}]")

    st.divider()
    
    st.markdown("<h2 style='text-align:center; margin-bottom:30px;'>Layanan Strategis V-GUARD</h2>", unsafe_allow_html=True)
