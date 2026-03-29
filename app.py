import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# API KEY
GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Koneksi AI Terputus.")

# Fungsi Foto Aman
def get_foto(lebar):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try:
            return st.image(Image.open('erwin.jpg'), width=lebar)
        except:
            return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# 2. STATUS LOGIN (Sangat Penting)
if 'role' not in st.session_state:
    st.session_state.role = None

# 3. DESIGN CSS (SIDEBAR HITAM & KOTAK PROPORSIONAL)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    [data-testid="stSidebar"] .stMarkdown b { color: white !important; }
    .hero-bg { background: #0e1117; padding: 20px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 20px; }
    .card-v { 
        background: white; padding: 15px; border-radius: 10px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 5px solid #FFD700; 
        height: 400px; display: flex; flex-direction: column; justify-content: space-between;
    }
    .card-v h4 { font-size: 16px; font-weight: 800; color: #111; text-align: center; margin: 0; }
    .card-v .price { font-size: 20px; color: #d42f2f; font-weight: bold; text-align: center; }
    .stLinkButton button { width: 100%; background-color: #FFD700 !important; color: #000 !important; font-weight: bold; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

# 4. SIDEBAR (NAVIGASI)
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(65)
    with col_n: st.markdown("<b>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    
    # Menu dinamis berdasarkan Login
    menu_options = ["🌐 Beranda", "📝 Meeting Lab", "🔑 Masuk Ke Sistem"]
    if st.session_state.role == "admin":
        menu_options = ["🌐 Beranda", "📝 Meeting Lab", "🤖 Panel Admin"]
    elif st.session_state.role == "klien":
        menu_options = ["🌐 Beranda", "📝 Meeting Lab", "📊 Laporan Klien"]
        
    menu = st.radio("NAVIGASI:", menu_options)

    if st.session_state.role:
        if st.button("🚪 Keluar (Logout)"):
            st.session_state.role = None
            st.rerun()

# 5. LOGIKA HALAMAN
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    
    # Kalkulator ROI
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(280)
    with c2:
        st.subheader("📊 Kalkulator Potensi Kerugian")
        omset = st.number_input("Omset Bulanan (Rp):", value=100000000)
        kebocoran = st.slider("Estimasi Kebocoran (%):", 1, 15, 3)
        st.info(f"Potensi Penyelamatan: **Rp {omset*(kebocoran/100):,.0f} /Bulan**")

    st.divider()
    # Menampilkan 4 Paket (V-START, V-LITE, V-PRO, CORPORATE)
    WA = "https://wa.me/6282122190885"
    p1, p2, p3, p4 = st.columns(4)
    with p1: 
        st.markdown('<div class="card-v"><h4>🌱 V-START</h4><div class="price">3,5 Jt</div><p>Audit otomatis mingguan.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL", WA)
    with p2:
        st.markdown('<div class="card-v"><h4>📦 V-LITE</h4><div class="price">7,5 Jt</div><p>Monitoring jarak jauh.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL", WA)
    with p3:
        st.markdown('<div class="card-v" style="border:2px solid #FFD700"><h4>🚀 V-PRO</h4><div class="price">15 Jt</div><p>Deep AI Fraud Audit.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL", WA)
    with p4:
        st.markdown('<div class="card-v" style="background:#0e1117;color:white"><h4>🏢 CORPORATE</h4><div class="price" style="color:#FFD700">Custom</div><p>Skala Nasional.</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI CEO", WA)

elif menu == "🔑 Masuk Ke Sistem":
    st.title("🔑 Login V-GUARD")
    with st.container():
        u = st.text_input("Username (Admin/Klien)").strip().lower()
        p = st.text_input("Password", type="password").strip()
        if st.button("Masuk"):
            if u == "admin" and p == "Vguard2026":
                st.session_state.role = "admin"
                st.success("Berhasil masuk sebagai Admin!")
                st.rerun()
            elif u == "klien" and p == "User2026":
                st.session_state.role = "klien"
                st.success("Berhasil masuk sebagai Klien!")
                st.rerun()
            else:
                st.error("Username atau Password salah!")

elif menu == "🤖 Panel Admin":
    st.title("🤖 Panel Administrator")
    st.write("Selamat datang, Pak Erwin. Di sini Bapak bisa mengaudit data transaksi.")

elif menu == "📊 Laporan Klien":
    st.title("📊 Laporan Keamanan Bisnis")
    st.write("Halaman khusus laporan mingguan klien.")

elif menu == "📝 Meeting Lab":
    st.title("📝 AI Meeting Lab")
    txt = st.text_area("Tempel transkrip rapat:")
    if st.button("Analisis AI"):
        if txt:
            res = model.generate_content(f"Rangkum: {txt}")
            st.info(res.text)
