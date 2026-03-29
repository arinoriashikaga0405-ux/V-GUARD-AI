import streamlit as st
import google.generativeai as genai
import os
import pandas as pd
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

# INITIAL DATABASE (Penyimpanan Sementara)
if 'role' not in st.session_state: st.session_state.role = None
if 'user_name' not in st.session_state: st.session_state.user_name = "Visitor"
if 'user_id' not in st.session_state: st.session_state.user_id = None
if 'db_klien' not in st.session_state:
    # Data dummy awal agar halaman tidak putih
    st.session_state.db_klien = {
        "klien": {"paket": "V-LITE", "tagihan": 7500000, "due": "2026-04-05"}
    }

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
    .bio-section { background: #0e1117; color: white; padding: 25px; border-radius: 15px; border-left: 6px solid #FFD700; }
    .red-alert { background: #ff4b4b; color: white; padding: 20px; border-radius: 10px; border: 3px solid black; text-align: center; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0.3; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    f_col, n_col = st.columns([1, 2])
    with f_col: get_foto(65)
    with n_col: 
        st.markdown(f"<b style='color:white;'>{st.session_state.user_name}</b><br><small style='color:#FFD700;'>V-GUARD Ecosystem</small>", unsafe_allow_html=True)
    st.divider()
    
    if st.session_state.role == "admin":
        menu = st.radio("FOUNDER MENU:", ["🌐 Beranda", "👥 Management Klien", "🤖 AI Fraud Scanner"])
    elif st.session_state.role == "klien":
        menu = st.radio("CLIENT DASHBOARD:", ["🌐 Beranda", "📅 Invoice & Payment"])
    else:
        menu = st.radio("VISITOR MENU:", ["🌐 Beranda", "🔑 Masuk Ke Sistem"])

    if st.session_state.role and st.button("🚪 Logout"):
        st.session_state.role = None
        st.session_state.user_name = "Visitor"
        st.session_state.user_id = None
        st.rerun()

# 4. LOGIKA HALAMAN UTAMA
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Mencegah Kerugian Owner Melalui Deteksi Proaktif</p></div>', unsafe_allow_html=True)
    c_img, c_txt = st.columns([1, 2])
    with c_img: get_foto(350)
    with c_txt:
        st.markdown('<div class="bio-section"><h3 style="color:#FFD700;">🛡️ About V-GUARD</h3><p>Platform deteksi fraud sistemik oleh <b>Erwin Sinaga</b>. Pengalaman perbankan 10+ tahun untuk memproteksi aset bisnis Anda.</p></div>', unsafe_allow_html=True)
    st.divider()
    st.subheader("📈 Kalkulator ROI Fraud")
    omset = st.number_input("Omset Bulanan Bisnis (Rp):", value=100000000)
    st.metric("Potensi Aset Terselamatkan", f"Rp {omset * 0.027:,.0f}")

elif menu == "🔑 Masuk Ke Sistem":
    st.markdown('<div class="hero-bg"><h1>SECURITY LOGIN</h1></div>', unsafe_allow_html=True)
    with st.form("login_form"):
        u = st.text_input("User ID").lower().strip()
        p = st.text_input("Access Key", type="password")
        if st.form_submit_button("AUTHENTICATE"):
            if u == "admin" and p == "Vguard2026":
                st.session_state.role, st.session_state.user_name = "admin", "Erwin Sinaga"
                st.rerun()
            elif u in st.session_state.db_klien and p == "User2026":
                st.session_state.role, st.session_state.user_id, st.session_state.user_name = "klien", u, u.upper()
                st.rerun()
            else:
                st.error("Akses Ditolak. Periksa kembali ID dan Key Bapak.")

elif menu == "👥 Management Klien":
    st.title("👥 Management Klien")
    with st.form("add_klien"):
        new_u = st.text_input("User ID Klien Baru:")
        new_v = st.number_input("Tagihan:", value=3500000)
        if st.form_submit_button("Daftarkan Klien"):
            st.session_state.db_klien[new_u] = {"paket": "V-START", "tagihan": new_v, "due": "2026-05-01"}
            st.success(f"Klien {new_u} berhasil didaftarkan!")

elif menu == "🤖 AI Fraud Scanner":
    st.markdown('<div class="hero-bg"><h1>AI COMMAND CENTER</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="red-alert">🚨 ALARM MERAH: SISTEM SIAP ANALISIS 🚨</div>', unsafe_allow_html=True)
    st.file_uploader("Upload Data Transaksi untuk Scan")

elif menu == "📅 Invoice & Payment":
    st.title("📅 Dashboard Tagihan Klien")
    u_id = st.session_state.user_id
    if u_id in st.session_state.db_klien:
        data = st.session_state.db_klien[u_id]
        st.metric("Total Tagihan Aktif", f"Rp {data['tagihan']:,}")
        st.write(f"Paket: {data['paket']} | Jatuh Tempo: {data['due']}")
    else:
        st.warning("Data tagihan tidak ditemukan. Silakan hubungi Admin.")
