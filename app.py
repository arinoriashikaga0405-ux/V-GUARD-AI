import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
from PIL import Image

# 1. KONFIGURASI DASAR
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# API KEY
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

# 2. CSS EXECUTIVE (SEMUA PAKET PUTIH & PROPORSIONAL)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    [data-testid="stSidebar"] .stMarkdown b { color: white !important; }
    
    .hero-bg { 
        background: #0e1117; padding: 30px; border-radius: 12px; 
        color: white; text-align: center; border-bottom: 4px solid #FFD700; 
        margin-bottom: 30px; 
    }
    
    .card-v { 
        background: white !important; 
        padding: 20px; 
        border-radius: 12px; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); 
        border-top: 5px solid #FFD700; 
        min-height: 550px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        margin-bottom: 20px;
    }
    
    .card-v h4 { font-size: 18px; font-weight: 800; color: #111; text-align: center; margin-bottom: 10px; }
    .card-v .price { font-size: 20px; color: #d42f2f; font-weight: bold; text-align: center; margin-bottom: 15px; }
    .card-v .label { font-size: 11px; font-weight: bold; color: #888; text-transform: uppercase; margin-top: 10px; border-bottom: 1px solid #eee; padding-bottom: 3px; }
    .card-v p, .card-v ul { font-size: 13px; color: #333; line-height: 1.5; margin: 5px 0; padding-left: 0; list-style-position: inside; }
    
    .stLinkButton button { 
        width: 100%; background-color: #FFD700 !important; 
        color: #000 !important; font-weight: bold; border-radius: 8px; border: none; 
    }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
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
        st.divider()
        if st.button("🚪 Keluar (Logout)"):
            st.session_state.role = None
            st.rerun()

# 4. HALAMAN BERANDA
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    
    # Kalkulator
    c_img, c_calc = st.columns([1, 2])
    with c_img: get_foto(300)
    with c_calc:
        st.subheader("📊 Analisis Potensi Penyelamatan Dana")
        omset = st.number_input("Omset Bulanan Bisnis (Rp):", value=100000000, step=10000000)
        kebocoran = st.slider("Estimasi Kebocoran Operasional (%):", 1, 15, 3)
        hasil = omset * (kebocoran / 100)
        st.success(f"V-GUARD dapat menyelamatkan aset Anda senilai: **Rp {hasil:,.0f} / Bulan**")
    
    st.divider()
    st.markdown("<h3 style='text-align:center; margin-bottom:20px;'>Paket Solusi Keamanan</h3>", unsafe_allow_html=True)
    
    # Kartu Paket
    WA = "https://wa.me/6282122190885"
    p1, p2, p3, p4 = st.columns(4)
    
    with p1:
        st.markdown('<div class="card-v"><div><h4>🌱 V-START</h4><div class="price">3,5 Jt /Bln</div><div class="label">Deskripsi</div><p>Audit otomatis mingguan untuk validasi operasional UMKM.</p><div class="label">Fitur Utama</div><ul><li>Cek Stok & Kas</li><li>Laporan basic via WA</li><li>1 Outlet</li></ul><div class="label">Target Market</div><p>Kedai / UMKM Mandiri</p></div></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
    
    with p2:
        st.markdown('<div class="card-v"><div><h4>📦 V-LITE</h4><div class="price">7,5 Jt /Bln</div><div class="label">Deskripsi</div><p>Monitoring aktif harian untuk pemilik yang jarang di tempat.</p><div class="label">Fitur Utama</div><ul><li>Laporan WA Real-time</li><li>Integrasi Sistem POS</li><li>1 Outlet Premium</li></ul><div class="label">Target Market</div><p>Retailer & Cafe</p></div></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
        
    with p3:
        st.markdown('<div class="card-v" style="border: 2px solid #FFD700"><div><h4>🚀 V-PRO</h4><div class="price">15 Jt /Bln</div><div class="label">Deskripsi</div><p>Deep AI Fraud Audit untuk deteksi kecurangan sistemik.</p><div class="label">Fitur Utama</div><ul><li>Analisis Perilaku Kasir</li><li>Prioritas Alert AI</li><li>Hingga 5 Outlet</li></ul><div class="label">Target Market</div><p>Franchise & Cabang</p></div></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
        
    with p4:
        st.markdown('<div class="card-v"><div><h4>🏢 CORPORATE</h4><div class="price">Custom</div><div class="label">Deskripsi</div><p>Proteksi skala nasional untuk skalabilitas bisnis tanpa batas.</p><div class="label">Fitur Utama</div><ul><li>Unlimited Outlet</li><li>Dedicated Support</li><li>Review Strategis Bulanan</li></ul><div class="label">Target Market</div><p>Holding / Enterprise</p></div></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI CEO", WA)

# 5. HALAMAN LAINNYA
elif menu == "🔑 Masuk Ke Sistem":
    st.markdown('<div class="hero-bg"><h1>LOGIN SISTEM</h1></div>', unsafe_allow_html=True)
    with st.form("login_box"):
        u = st.text_input("Username").strip().lower()
        p = st.text_input("Password", type="password")
        if st.form_submit_button("Masuk"):
            if u == "admin" and p == "Vguard2026":
                st.session_state.role = "admin"
                st.rerun()
            elif u == "klien" and p == "User2026":
                st.session_state.role = "klien"
                st.rerun()
            else: st.error("Akses Ditolak!")

elif menu == "🤖 Panel Admin":
    st.markdown('<div class="hero-bg"><h1>PANEL ADMINISTRATOR</h1></div>', unsafe_allow_html=True)
    st.info("Selamat datang kembali, Pak Erwin. Modul audit sedang siap dijalankan.")

elif menu == "📊 Laporan Klien":
    st.markdown('<div class="hero-bg"><h1>DASHBOARD KLIEN</h1></div>', unsafe_allow_html=True)
    st.info("Halaman monitoring real-time untuk pemilik bisnis.")

elif menu == "📝 Meeting Lab":
    st.title("📝 Meeting Lab")
    catatan = st.text_area("Masukkan teks rapat Bapak:")
    if st.button("Analisis Strategi"):
        if catatan:
            with st.spinner("AI sedang merangkum..."):
                res = model.generate_content(f"Rangkum poin penting dan rencana aksi dari teks ini: {catatan}")
                st.info(res.text)
