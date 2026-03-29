import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from PIL import Image

# 1. KONFIGURASI UTAMA & AI
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# API KEY BAPAK (SUDAH TERPASANG)
GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"

if GOOGLE_API_KEY:
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except:
        st.error("Gagal mengonfigurasi AI.")

# Fungsi Foto
def get_foto(lebar):
    try:
        if os.path.exists('erwin.jpg'):
            return st.image(Image.open('erwin.jpg'), width=lebar)
        else:
            return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)
    except:
        st.write("📸")

# 2. SISTEM LOGIN
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

# 3. CSS DESIGN (UKURAN TULISAN BESAR & 4 KOLOM)
st.markdown("""<style>
    .stApp { background-color: #f4f6f9; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 3px solid #FFD700; }
    .hero-bg { background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); padding: 30px; border-radius: 20px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 25px; }
    
    .card-service { 
        background: white; 
        padding: 25px; 
        border-radius: 15px; 
        box-shadow: 0 5px 15px rgba(0,0,0,0.1); 
        border-top: 6px solid #FFD700; 
        text-align: center; 
        height: 300px; 
        display: flex; 
        flex-direction: column; 
        justify-content: space-between;
    }
    .card-service h4 { font-size: 20px; font-weight: bold; margin-bottom: 8px; color: #1a1a1a; }
    .card-service h3 { font-size: 28px; margin: 10px 0; color: #d42f2f; font-weight: bold; }
    .card-service p { font-size: 15px; line-height: 1.5; color: #444; margin-bottom: 15px; }
    .stLinkButton button { width: 100%; height: 45px; font-size: 16px !important; font-weight: bold; }
</style>""", unsafe_allow_html=True)

# 4. SIDEBAR & NAVIGASI
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #FFD700;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    col_f, col_n = st.columns([1, 2])
    with col_f: 
        get_foto(60)
    with col_n: 
        st.markdown("<b style='color:white;'>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
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

# ==========================================
# 5. HALAMAN BERANDA
# ==========================================
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    
    c_roi1, c_roi2 = st.columns([1, 2])
    with c_roi1: 
        get_foto(350)
    with c_roi2:
        st.subheader("🛡️ Proteksi Aset & Deteksi Fraud")
        st.write("Gunakan teknologi AI untuk mengunci profit dan mendeteksi kebocoran bisnis secara real-time.")
        omset = st.number_input("Omset Bulanan (Rp):", value=100000000)
        leak = st.slider("Estimasi Kebocoran (%):", 0, 15, 3)
        st.markdown(f"### Potensi Penyelamatan: :red[Rp {omset*(leak/100):,.0f}]")

    st.divider()
    
    st.markdown("<h2 style='text-align:center;'>Layanan Strategis V-GUARD</h2>", unsafe_allow_html=True)
    WA_LINK = "https://wa.me/6282122190885"
    
    # TAMPILAN 4 KOLOM (Besar & Jelas)
    p1, p2, p3, p4 = st.columns(4)
    
    with p1:
        st.markdown('<div class="card-service"><h4>🌱 V-START</h4><h3>3,5 Jt</h3><p>Audit mingguan otomatis khusus untuk UMKM pemula.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA_LINK)
    with p2:
        st.markdown('<div class="card-service"><h4>📦 V-LITE</h4><h3>7,5 Jt</h3><p>1 Outlet. Laporan audit harian dikirim via WhatsApp.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA_LINK)
    with p3:
        st.markdown('<div class="card-service" style="border:3px solid #FFD700"><h4>🚀 V-PRO</h4><h3>15 Jt</h3><p>5 Outlet. Analisis Deep Fraud Audit AI tercanggih.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA_LINK)
    with p4:
        st.markdown('<div class="card-service" style="background-color:#0e1117; color:white; border-top:6px solid #FFD700;"><h4>🏢 CORP & ENTERPRISE</h4><h3 style="color:#FFD700;">Custom</h3><p style="color:#eee">Unlimited Outlet. Integrasi On-site & Model AI Khusus.</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI CEO", WA_LINK)

# ==========================================
# 6. HALAMAN MEETING LAB
# ==========================================
elif menu == "📝 Meeting Lab":
    st.title("📝 AI Meeting Lab")
    st.write("Masukkan transkrip rapat Anda untuk dianalisis oleh AI V-GUARD.")
    txt =
