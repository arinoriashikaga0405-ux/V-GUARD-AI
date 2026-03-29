import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

# 1. KONFIGURASI HALAMAN UTAMA
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# API KEY BAPAK
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

# 2. STATUS LOGIN & ROLE
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
        height: 380px; display: flex; flex-direction: column; justify-content: space-between;
    }
    .card-v h4 { font-size: 16px; font-weight: 800; color: #111; text-align: center; margin: 0; }
    .card-v .price { font-size: 20px; color: #d42f2f; font-weight: bold; text-align: center; }
    .stLinkButton button { width: 100%; background-color: #FFD700 !important; color: #000 !important; font-weight: bold; border-radius: 8px; }
    .login-box { background: white; padding: 30px; border-radius: 15px; border: 1px solid #ddd; box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
</style>
""", unsafe_allow_html=True)

# 4. SIDEBAR (NAVIGASI & IDENTITAS)
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    
    # Identitas Founder
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(65)
    with col_n: st.markdown("<b>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    
    # Menu Navigasi Dinamis
    nav_list = ["🌐 Beranda", "📝 Meeting Lab"]
    
    if st.session_state.role == "admin":
        nav_list.append("🤖 Panel Admin")
    elif st.session_state.role == "klien":
        nav_list.append("📊 Laporan Klien")
    else:
        nav_list.append("🔑 Masuk Ke Sistem")
        
    menu = st.radio("NAVIGASI:", nav_list)

    if st.session_state.role:
        st.write("---")
        if st.button("🚪 Keluar (Logout)"):
            st.session_state.role = None
            st.rerun()

# 5. LOGIKA HALAMAN
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    
    # Kalkulator Potensi Kerugian
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(300)
    with c2:
        st.subheader("📊 Kalkulator Potensi Kerugian Operasional")
        omset = st.number_input("Omset Bulanan Bisnis (Rp):", value=100000000, step=10000000)
        kebocoran = st.slider("Estimasi Kebocoran (%) (Bawaan FAM A40: 3%):", 1, 15, 3)
        penyelamatan = omset * (kebocoran / 100)
        st.info(f"Potensi Kerugian yang Dapat Dicegah: **Rp {penyelamatan:,.0f} /Bulan**")

    st.divider()
    st.markdown("<h3 style='text-align:center;'>Layanan Strategis V-GUARD</h3>", unsafe_allow_html=True)
    
    WA = "https://wa.me/6282122190885"
    p1, p2, p3, p4 = st.columns(4)
    with p1: 
        st.markdown('<div class="card-v"><h4>🌱 V-START</h4><div class="price">3,5 Jt</div><p>Audit otomatis mingguan.</p></div>', unsafe_allow_html=True)
        st.link_button("PILIH", WA)
    with p2:
        st.markdown('<div class="card-v"><h4>📦 V-LITE</h4><div class="price">7,5 Jt</div><p>Monitoring jarak jauh.</p></div>', unsafe_allow_html=True)
        st.link_button("PILIH", WA)
    with p3:
        st.markdown('<div class="card-v" style="border:2px solid #FFD700"><h4>🚀 V-PRO</h4><div class="price">15 Jt</div><p>Deep AI Fraud Audit.</p></div>', unsafe_allow_html=True)
        st.link_button("PILIH", WA)
    with p4:
        st.markdown('<div class="card-v" style="background:#0e1117;color:white"><h4>🏢 CORPORATE</h4><div class="price" style="color:#FFD700">Custom</div><p>Skala Nasional.</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI CEO", WA)

elif menu == "🔑 Masuk Ke Sistem":
    st.markdown('<div class="hero-bg"><h1>LOGIN V-GUARD</h1><p>Gunakan kredensial Admin atau Klien Anda</p></div>', unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1, 1])
    with col_l:
        st.info("ℹ️ **Informasi Login**\n\nGunakan 'admin' untuk akses penuh Panel Administrator, atau 'klien' untuk melihat laporan keamanan bisnis Anda.")
    
    with col_r:
        with st.form("form_login_utama"):
            username = st.text_input("Username").strip().lower()
            password = st.text_input("Password", type="password").strip()
            submit = st.form_submit_button("Masuk Sekarang")
            
            if submit:
                if username == "admin" and password == "Vguard2026":
                    st.session_state.role = "admin"
                    st.success("Login Berhasil sebagai Admin!")
                    st.rerun()
                elif username == "klien" and password == "User2026":
                    st.session_state.role = "klien"
                    st.success("Login Berhasil sebagai Klien!")
                    st.rerun()
                else:
                    st.error("Kombinasi Username/Password Salah!")

elif menu == "🤖 Panel Admin":
    st.title("🤖 Panel Administrator")
    st.write(f"Selamat datang kembali, Pak **Erwin Sinaga**.")
    st.info("Di sini Anda dapat mengaudit data transaksi dan memantau pola fraud AI.")

elif menu == "📊 Laporan Klien":
    st.title("📊 Laporan Keamanan Bisnis")
    st.write("Berikut adalah ringkasan mingguan proteksi aset Anda.")

elif menu == "📝 Meeting Lab":
    st.title("📝 AI Meeting Lab")
    txt_area = st.text_area("Tempel transkrip rapat di sini:", height=250)
    if st.button("🚀 Analisis Strategis"):
        if txt_area:
            with st.spinner("AI sedang bekerja..."):
                res = model.generate_content(f"Rangkum poin strategis: {txt_area}")
                st.write(res.text)
