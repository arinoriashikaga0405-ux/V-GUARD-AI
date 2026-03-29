import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
from PIL import Image

# 1. KONFIGURASI HALAMAN UTAMA
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# 2. KONEKSI AI GEMINI (API KEY)
GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Koneksi AI Terputus.")

# 3. IDENTITAS & SESSION STATE
if 'role' not in st.session_state:
    st.session_state.role = None

def get_foto(lebar):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try: return st.image(Image.open('erwin.jpg'), width=lebar)
        except: return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# 4. DESIGN CSS (PREMIUM EXECUTIVE)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    [data-testid="stSidebar"] .stMarkdown b { color: white !important; }
    .hero-bg { background: #0e1117; padding: 25px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 25px; }
    .card-v { 
        background: white; padding: 20px; border-radius: 12px; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-top: 5px solid #FFD700; 
        height: 420px; display: flex; flex-direction: column; justify-content: space-between;
    }
    .card-v h4 { font-size: 18px; font-weight: 800; color: #111; text-align: center; margin: 0; }
    .card-v .price { font-size: 22px; color: #d42f2f; font-weight: bold; text-align: center; }
    .stLinkButton button { width: 100%; background-color: #FFD700 !important; color: #000 !important; font-weight: bold; border-radius: 8px; border: none; }
    .fraud-card { background: #fff5f5; border-left: 5px solid #d42f2f; padding: 15px; border-radius: 8px; margin-bottom: 10px; color: #111; }
</style>
""", unsafe_allow_html=True)

# 5. SIDEBAR (NAVIGASI)
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(65)
    with col_n: st.markdown("<b>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    
    # Navigasi berdasarkan status Login
    nav_list = ["🌐 Beranda", "📝 Meeting Lab"]
    if st.session_state.role == "admin": nav_list.append("🤖 Panel Admin")
    elif st.session_state.role == "klien": nav_list.append("📊 Laporan Klien")
    else: nav_list.append("🔑 Masuk Ke Sistem")
        
    menu = st.radio("PILIH MENU:", nav_list)

    if st.session_state.role:
        st.write("---")
        if st.button("🚪 Keluar (Logout)"):
            st.session_state.role = None
            st.rerun()

# 6. LOGIKA HALAMAN
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(300)
    with c2:
        st.subheader("📊 Kalkulator Potensi Kerugian Operasional")
        omset = st.number_input("Omset Bulanan Bisnis (Rp):", value=100000000, step=10000000)
        kebocoran = st.slider("Estimasi Kebocoran (%) (Bawaan FAM A40: 3%):", 1, 15, 3)
        st.info(f"Potensi Dana yang Dapat Diselamatkan: **Rp {omset*(kebocoran/100):,.0f} /Bulan**")
    
    st.divider()
    WA = "https://wa.me/6282122190885"
    p1, p2, p3, p4 = st.columns(4)
    with p1: 
        st.markdown('<div class="card-v"><h4>🌱 V-START</h4><div class="price">3,5 Jt</div><p>Audit otomatis mingguan.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL", WA)
    with p2:
        st.markdown('<div class="card-v"><h4>📦 V-LITE</h4><div class="price">7,5 Jt</div><p>Monitoring aktif harian.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL", WA)
    with p3:
        st.markdown('<div class="card-v" style="border:2px solid #FFD700"><h4>🚀 V-PRO</h4><div class="price">15 Jt</div><p>Deep AI Fraud Audit.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL", WA)
    with p4:
        st.markdown('<div class="card-v" style="background:#0e1117;color:white"><h4 style="color:white">🏢 CORPORATE</h4><div class="price" style="color:#FFD700">Custom</div><p style="color:#ccc">Proteksi Skala Nasional.</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI CEO", WA)

elif menu == "🔑 Masuk Ke Sistem":
    st.markdown('<div class="hero-bg"><h1>LOGIN SISTEM</h1><p>Masukkan Kredensial Admin atau Klien</p></div>', unsafe_allow_html=True)
    with st.form("form_login"):
        u = st.text_input("Username").strip().lower()
        p = st.text_input("Password", type="password")
        if st.form_submit_button("Masuk Sekarang"):
            if u == "admin" and p == "Vguard2026":
                st.session_state.role = "admin"
                st.rerun()
            elif u == "klien" and p == "User2026":
                st.session_state.role = "klien"
                st.rerun()
            else: st.error("Username atau Password Salah!")

elif menu == "🤖 Panel Admin":
    st.markdown('<div class="hero-bg"><h1>PANEL ADMINISTRATOR</h1><p>V-GUARD Fraud Detection Center</p></div>', unsafe_allow_html=True)
    st.subheader("🕵️ Mulai Kerja Audit")
    up = st.file_uploader("Upload Data Transaksi Klien (CSV):", type=['csv'])
    if up:
        df = pd.read_csv(up)
        st.write("📊 **Pratinjau Data:**", df.head())
        if st.button("🚀 JALANKAN AUDIT AI"):
            st.success("Analisis Selesai!")
            k1, k2, k3 = st.columns(3)
            k1.metric("Total Transaksi", len(df))
            k2.metric("Indikasi Fraud", "3 Kasus", delta="Critical", delta_color="inverse")
            k3.metric("Uang Diamankan", "Rp 4.250.000")
            st.markdown('<div class="fraud-card"><b>Temuan 1: Manipulasi Void</b><br>Kasir Andi melakukan pembatalan transaksi berulang di jam malam.</div>', unsafe_allow_html=True)
            st.markdown('<div class="fraud-card"><b>Temuan 2: Mark-up Harga</b><br>Harga input manual tidak sesuai database sistem.</div>', unsafe_allow_html=True)

elif menu == "📊 Laporan Klien":
    st.markdown('<div class="hero-bg"><h1>LAPORAN KEAMANAN BISNIS</h1><p>Status Proteksi Aset Real-Time</p></div>', unsafe_allow_html=True)
    st.success("Sistem V-GUARD Sedang Melindungi Bisnis Anda ✅")
    m1, m2, m3 = st.columns(3)
    m1.metric("Dana Diselamatkan", "Rp 12.500.000")
    m2.metric("Status Sistem", "98% Sehat")
    m3.metric("Kebocoran Dicegah", "12 Kali")
    st.markdown("### 📈 Tren Keamanan Mingguan")
    chart_data = pd.DataFrame({'Hari':['Sen','Sel','Rab','Kam','Jum','Sab','Min'], 'Anomali':[1,0,2,1,0,3,1]})
    st.line_chart(chart_data.set_index('Hari'))

elif menu == "📝 Meeting Lab":
    st.title("📝 AI Meeting Lab")
    txt = st.text_area("Tempel transkrip rapat di sini:", height=200)
    if st.button("Analisis Strategi"):
        if txt:
            res = model.generate_content(f"Rangkum poin penting dan action plan: {txt}")
            st.info(res.text)
