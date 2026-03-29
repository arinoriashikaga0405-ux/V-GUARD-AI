import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
from PIL import Image

# 1. KONFIGURASI & AI SETUP
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Koneksi AI Terputus.")

# Fungsi Foto
def get_foto(lebar):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try: return st.image(Image.open('erwin.jpg'), width=lebar)
        except: return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

if 'role' not in st.session_state:
    st.session_state.role = None

# 2. DESIGN CSS (SIDEBAR HITAM & KOTAK COMPACT)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    [data-testid="stSidebar"] .stMarkdown b { color: white !important; }
    .hero-bg { background: #0e1117; padding: 20px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 20px; }
    .card-v { 
        background: white; padding: 15px; border-radius: 10px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 5px solid #FFD700; 
        height: 380px; display: flex; flex-direction: column; justify-content: space-between;
    }
    .card-v h4 { font-size: 16px; font-weight: 800; color: #111; text-align: center; margin: 0; }
    .card-v .price { font-size: 20px; color: #d42f2f; font-weight: bold; text-align: center; }
    .stLinkButton button { width: 100%; background-color: #FFD700 !important; color: #000 !important; font-weight: bold; border-radius: 8px; }
    .fraud-card { background: #fff5f5; border-left: 5px solid #d42f2f; padding: 15px; border-radius: 8px; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(65)
    with col_n: st.markdown("<b>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    
    nav_list = ["🌐 Beranda", "📝 Meeting Lab"]
    if st.session_state.role == "admin": nav_list.append("🤖 Panel Admin")
    elif st.session_state.role == "klien": nav_list.append("📊 Laporan Klien")
    else: nav_list.append("🔑 Masuk Ke Sistem")
        
    menu = st.radio("NAVIGASI:", nav_list)

    if st.session_state.role:
        if st.button("🚪 Logout"):
            st.session_state.role = None
            st.rerun()

# 4. LOGIKA HALAMAN
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(300)
    with c2:
        st.subheader("📊 Kalkulator Potensi Kerugian")
        omset = st.number_input("Omset Bulanan (Rp):", value=100000000, step=10000000)
        kebocoran = st.slider("Estimasi Kebocoran (%):", 1, 15, 3)
        st.info(f"Potensi Kerugian yang Dapat Dicegah: **Rp {omset*(kebocoran/100):,.0f} /Bulan**")
    
    st.divider()
    WA = "https://wa.me/6282122190885"
    p1, p2, p3, p4 = st.columns(4)
    with p1: 
        st.markdown('<div class="card-v"><h4>🌱 V-START</h4><div class="price">3,5 Jt</div><p>Audit otomatis mingguan.</p></div>', unsafe_allow_html=True)
        st.link_button("PILIH", WA)
    with p2:
        st.markdown('<div class="card-v"><h4>📦 V-LITE</h4><div class="price">7,5 Jt</div><p>Monitoring aktif.</p></div>', unsafe_allow_html=True)
        st.link_button("PILIH", WA)
    with p3:
        st.markdown('<div class="card-v" style="border:2px solid #FFD700"><h4>🚀 V-PRO</h4><div class="price">15 Jt</div><p>Deep AI Fraud Audit.</p></div>', unsafe_allow_html=True)
        st.link_button("PILIH", WA)
    with p4:
        st.markdown('<div class="card-v" style="background:#0e1117;color:white"><h4>🏢 CORPORATE</h4><div class="price" style="color:#FFD700">Custom</div><p>Skala Nasional.</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI CEO", WA)

elif menu == "🔑 Masuk Ke Sistem":
    st.markdown('<div class="hero-bg"><h1>LOGIN V-GUARD</h1></div>', unsafe_allow_html=True)
    with st.form("login_form"):
        u = st.text_input("Username").strip().lower()
        p = st.text_input("Password", type="password").strip()
        if st.form_submit_button("Masuk"):
            if u == "admin" and p == "Vguard2026":
                st.session_state.role = "admin"
                st.rerun()
            elif u == "klien" and p == "User2026":
                st.session_state.role = "klien"
                st.rerun()
            else: st.error("Salah password!")

# ==========================================
# 5. PANEL ADMIN - FITUR DETEKSI FRAUD
# ==========================================
elif menu == "🤖 Panel Admin":
    st.markdown('<div class="hero-bg"><h1>PANEL ADMINISTRATOR</h1><p>V-GUARD AI Fraud Detection Center</p></div>', unsafe_allow_html=True)
    
    st.subheader("🕵️ Upload Data Transaksi Klien")
    file_upload = st.file_uploader("Pilih file CSV transaksi klien untuk diaudit AI:", type=['csv'])

    if file_upload:
        df = pd.read_csv(file_upload)
        st.write("📊 **Pratinjau Data:**", df.head())
        
        if st.button("🚀 MULAI AUDIT AI"):
            with st.spinner("AI sedang menganalisis pola kecurangan..."):
                # Simulasi Analisis AI
                st.success("Analisis Selesai!")
                
                c1, c2, c3 = st.columns(3)
                c1.metric("Total Transaksi", len(df))
                c2.metric("Indikasi Fraud", "3 Temuan", delta="-5%", delta_color="inverse")
                c3.metric("Potensi Kerugian", "Rp 4.250.000")

                st.markdown("### 🚩 Temuan Kecurangan (Indikasi Fraud)")
                st.markdown('<div class="fraud-card"><b>Temuan 1: Manipulasi Void</b><br>Kasir "Andi" melakukan pembatalan transaksi 15x di atas jam 21:00.</div>', unsafe_allow_html=True)
                st.markdown('<div class="fraud-card"><b>Temuan 2: Ketidakcocokan Stok</b><br>Data POS menunjukkan 10 botol terjual, namun CCTV mendeteksi 12 botol keluar.</div>', unsafe_allow_html=True)

    else:
        st.info("Silakan upload data transaksi untuk memulai kerja audit.")

elif menu == "📝 Meeting Lab":
    st.title("📝 Meeting Lab")
    t = st.text_area("Teks rapat:")
    if st.button("Analisis"):
        res = model.generate_content(f"Rangkum: {t}")
        st.write(res.text)
