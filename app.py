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
        st.error("Gagal mengonfigurasi AI. Cek koneksi atau Key.")

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

# 3. CSS DESIGN (KOMPAK & TANPA EROR)
st.markdown("""<style>
    .stApp { background-color: #f4f6f9; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 3px solid #FFD700; }
    .hero-bg { background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 20px; }
    
    .card-service { 
        background: white; 
        padding: 10px; 
        border-radius: 10px; 
        box-shadow: 0 2px 6px rgba(0,0,0,0.05); 
        border-top: 4px solid #FFD700; 
        text-align: center; 
        height: 220px; 
        display: flex; 
        flex-direction: column; 
        justify-content: space-between;
    }
    .card-service h4 { font-size: 13px; font-weight: bold; margin-bottom: 2px; color: #333; }
    .card-service h3 { font-size: 16px; margin: 4px 0; color: #0e1117; }
    .card-service p { font-size: 10px; line-height: 1.2; color: #666; margin-bottom: 5px; }
    .stLinkButton button { width: 100%; height: 28px; font-size: 10px !important; padding: 0px; }
</style>""", unsafe_allow_html=True)

# 4. SIDEBAR & NAVIGASI
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #FFD700;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(60)
    with col_n: st.markdown("<b style='color:white;'>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
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
    
    # ROI Calculator
    c_roi1, c_roi2 = st.columns([1, 2])
    with c_roi1: get_foto(350)
    with c_roi2:
        st.subheader("🛡️ Proteksi Aset & Deteksi Fraud")
        omset = st.number_input("Omset Bulanan (Rp):", value=100000000)
        leak = st.slider("Estimasi Kebocoran (%):", 0, 15, 3)
        st.markdown(f"### Potensi Penyelamatan: :red[Rp {omset*(leak/100):,.0f}]")

    st.divider()
    
    # 5 Paket Sejajar
    st.markdown("<h3 style='text-align:center;'>Layanan Strategis V-GUARD</h3>", unsafe_allow_html=True)
    WA_LINK = "https://wa.me/6282122190885"
    
    p1, p2, p3, p4, p5 = st.columns(5)
    
    with p1:
        st.markdown('<div class="card-service"><h4>🌱 V-START</h4><h3>3,5 Jt</h3><p>Audit mingguan untuk UMKM pemula.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL", WA_LINK)
    with p2:
        st.markdown('<div class="card-service"><h4>📦 V-LITE</h4><h3>7,5 Jt</h3><p>1 Outlet. Laporan harian via WhatsApp.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL", WA_LINK)
    with p3:
        st.markdown('<div class="card-service" style="border:2px solid #FFD700"><h4>🚀 V-PRO</h4><h3>15 Jt</h3><p>5 Outlet. Deep Fraud Audit AI.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL", WA_LINK)
    with p4:
        st.markdown('<div class="card-service"><h4>🏢 CORP</h4><h3>25 Jt</h3><p>Unlimited. Priority Support.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL", WA_LINK)
    with p5:
        st.markdown('<div class="card-service" style="background-color:#0e1117; color:white;"><h4>💎 ENTERPRISE</h4><h3>Custom</h3><p>Custom AI Solution & On-site.</p></div>', unsafe_allow_html=True)
        st.link_button("CEO", WA_LINK)

# ==========================================
# 6. HALAMAN MEETING LAB (AI AKTIF)
# ==========================================
elif menu == "📝 Meeting Lab":
    st.title("📝 AI Meeting Lab")
    txt = st.text_area("Tempel transkrip rapat di sini:", height=300)
    if st.button("🚀 PROSES AI"):
        if txt:
            with st.spinner("AI sedang merangkum..."):
                res = model.generate_content(f"Rangkum poin strategis dan action plan dari teks ini: {txt}")
                st.info(res.text)
        else:
            st.warning("Isi teks dulu.")

# 7. LOGIKA HALAMAN LAINNYA
elif menu == "📊 Dashboard Klien":
    st.title("📊 Dashboard Laporan Klien")
    st.metric("Profit Aman", "Rp 158.000.000", "+8%")

elif menu == "🤖 AI Auditor (Admin)":
    st.title("🤖 AI Auditor (Admin)")
    st.file_uploader("Upload file transaksi (CSV/Excel)")
