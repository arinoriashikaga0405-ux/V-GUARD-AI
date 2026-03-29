import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
from PIL import Image

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

# 2. CSS BERSIH (MENCEGAH SYNTAX ERROR)
st.markdown('<style>.stApp { background-color: #f4f6f9; }</style>', unsafe_allow_html=True)
st.markdown('<style>[data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }</style>', unsafe_allow_html=True)
st.markdown('<style>.hero-bg { background: #0e1117; padding: 30px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 30px; }</style>', unsafe_allow_html=True)
st.markdown('<style>.card-v { background: white !important; padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #FFD700; min-height: 520px; display: flex; flex-direction: column; justify-content: space-between; }</style>', unsafe_allow_html=True)
st.markdown('<style>.card-v h4 { color: #111; text-align: center; font-weight: 800; margin-bottom: 5px; } .card-v .price { color: #d42f2f; font-weight: bold; text-align: center; font-size: 20px; }</style>', unsafe_allow_html=True)
st.markdown('<style>.stLinkButton button { width: 100%; background-color: #FFD700 !important; color: #000 !important; font-weight: bold; }</style>', unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    f_col, n_col = st.columns([1, 2])
    with f_col: get_foto(65)
    with n_col: st.markdown("<b style='color:white;'>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    nav = ["🌐 Beranda", "📝 Meeting Lab"]
    if st.session_state.role == "admin": nav.append("🤖 Panel Admin")
    elif st.session_state.role == "klien": nav.append("📊 Laporan Klien")
    else: nav.append("🔑 Masuk Ke Sistem")
    menu = st.radio("MENU UTAMA:", nav)
    if st.session_state.role:
        if st.button("🚪 Keluar"):
            st.session_state.role = None
            st.rerun()

# 4. HALAMAN BERANDA
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(300)
    with c2:
        st.subheader("📊 Analisis Potensi Penyelamatan")
        omset = st.number_input("Omset Bulanan (Rp):", value=100000000, step=10000000)
        leak = st.slider("Kebocoran (%):", 1, 15, 3)
        hasil_save = omset * (leak / 100)
        st.success(f"V-GUARD dapat menyelamatkan: **Rp {hasil_save:,.0f} / Bulan**")
    
    st.divider()
    st.markdown("<h3 style='text-align:center;'>Layanan V-GUARD</h3>", unsafe_allow_html=True)
    
    WA = "https://wa.me/6282122190885"
    p1, p2, p3, p4 = st.columns(4)
    
    with p1:
        st.markdown('<div class="card-v"><div><h4>🌱 V-START</h4><div class="price">3,5 Jt /Bln</div><hr><p><b>Deskripsi:</b> Audit otomatis mingguan UMKM Mikro.</p><p><b>Fitur:</b> Stok, Kas, WA Report.</p><p><b>Market:</b> Kedai/SME.</p></div></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
    with p2:
        st.markdown('<div class="card-v"><div><h4>📦 V-LITE</h4><div class="price">7,5 Jt /Bln</div><hr><p><b>Deskripsi:</b> Monitoring harian aktif jarak jauh.</p><p><b>Fitur:</b> Real-time, POS Integration.</p><p><b>Market:</b> Retail/Cafe.</p></div></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
    with p3:
        st.markdown('<div class="card-v" style="border: 2px solid #FFD700"><div><h4>🚀 V-PRO</h4><div class="price">15 Jt /Bln</div><hr><p><b>Deskripsi:</b> Deep AI Fraud Audit sistemik.</p><p><b>Fitur:</b> Analisis Kasir, AI Alert.</p><p><b>Market:</b> Franchise.</p></div></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
    with p4:
        st.markdown('<div class="card-v"><div><h4>🏢 CORPORATE</h4><div class="price">Custom</div><hr><p><b>Deskripsi:</b> Proteksi skala nasional Enterprise.</p><p><b>Fitur:</b> Unlimited, Dedicated Support.</p><p><b>Market:</b> Holding/Nasional.</p></div></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)

elif menu == "🔑 Masuk Ke Sistem":
    st.markdown('<div class="hero-bg"><h1>LOGIN</h1></div>', unsafe_allow_html=True)
    with st.form("login"):
        u = st.text_input("Username").strip().lower()
        p = st.text_input("Password", type="password")
        if st.form_submit_button("Masuk"):
            if u == "admin" and p == "Vguard2026":
                st.session_state.role = "admin"
                st.rerun()
            elif u == "klien" and p == "User2026":
                st.session_state.role = "klien"
                st.rerun()
            else: st.error("Gagal Login!")

elif menu == "🤖 Panel Admin":
    st.markdown('<div class="hero-bg"><h1>PANEL ADMIN</h1></div>', unsafe_allow_html=True)
    st.write("Selamat datang, Pak Erwin.")

elif menu == "📊 Laporan Klien":
    st.markdown('<div class="hero-bg"><h1>DASHBOARD KLIEN</h1></div>', unsafe_allow_html=True)

elif menu == "📝 Meeting Lab":
    st.title("📝 Meeting Lab")
    txt = st.text_area("Input Teks:")
    if st.button("Proses"):
        if txt:
            res = model.generate_content(f"Rangkum: {txt}")
            st.write(res.text)
