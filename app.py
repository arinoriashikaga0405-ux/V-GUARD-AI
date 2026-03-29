import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# API KEY BAPAK
GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Koneksi AI Terputus.")

# Fungsi Foto (Aman dari Eror)
def get_foto(lebar):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try:
            return st.image(Image.open('erwin.jpg'), width=lebar)
        except:
            return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# 2. DESIGN CSS (KOTAK KECIL & SIDEBAR HITAM)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    [data-testid="stSidebar"] .stMarkdown b { color: white !important; }
    
    .hero-bg { background: #0e1117; padding: 20px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 20px; }
    
    .card-v { 
        background: white; padding: 15px; border-radius: 10px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 5px solid #FFD700; 
        height: 420px; display: flex; flex-direction: column; justify-content: space-between;
    }
    .card-v h4 { font-size: 16px; font-weight: 800; color: #111; text-align: center; margin: 0; }
    .card-v .price { font-size: 20px; color: #d42f2f; font-weight: bold; text-align: center; }
    .card-v .label { font-size: 10px; font-weight: bold; color: #999; text-transform: uppercase; margin-top: 5px; border-bottom: 1px solid #eee; }
    .card-v p, .card-v ul { font-size: 12px; color: #444; margin: 3px 0; padding-left: 10px; }
    
    .stLinkButton button { width: 100%; background-color: #FFD700 !important; color: #000 !important; font-weight: bold; height: 35px; font-size: 12px !important; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(65)
    with col_n: st.markdown("<b>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    menu = st.radio("MENU UTAMA:", ["🌐 Beranda", "📝 Meeting Lab", "🤖 Admin"])

# 4. HALAMAN BERANDA
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    
    # FITUR ROI & POTENSI KERUGIAN
    c_roi1, c_roi2 = st.columns([1, 2])
    with c_roi1:
        get_foto(280)
    with c_roi2:
        st.subheader("📊 Kalkulator Potensi Kerugian")
        omset = st.number_input("Omset Bulanan Bisnis (Rp):", value=100000000, step=10000000)
        kebocoran = st.slider("Estimasi Kebocoran Operasional (%):", 1, 15, 3)
        penyelamatan = omset * (kebocoran / 100)
        st.info(f"Potensi Kerugian yang Bisa Diselamatkan V-GUARD: **Rp {penyelamatan:,.0f} /Bulan**")

    st.divider()
    st.markdown("<h3 style='text-align:center;'>Pilihan Layanan Strategis</h3>", unsafe_allow_html=True)
    
    WA = "https://wa.me/6282122190885"
    p1, p2, p3, p4 = st.columns(4)
    
    with p1:
        st.markdown(f'<div class="card-v"><h4>🌱 V-START</h4><div class="price">3,5 Jt /Bln</div><div class="label">Deskripsi</div><p>Audit otomatis mandiri.</p><div class="label">Fitur</div><ul><li>Cek Stok</li><li>Lap. Mingguan</li></ul><div class="label">Target</div><p>UMKM Mikro</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
    with p2:
        st.markdown(f'<div class="card-v"><h4>📦 V-LITE</h4><div class="price">7,5 Jt /Bln</div><div class="label">Deskripsi</div><p>Monitoring jarak jauh.</p><div class="label">Fitur</div><ul><li>Notif WhatsApp</li><li>Integrasi POS</li></ul><div class="label">Target</div><p>Retail & Cafe</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
    with p3:
        st.markdown(f'<div class="card-v" style="border: 2px solid #FFD700;"><h4>🚀 V-PRO</h4><div class="price">15 Jt /Bln</div><div class="label">Deskripsi</div><p>Deep AI Fraud Audit.</p><div class="label">Fitur</div><ul><li>Pola Fraud AI</li><li>Hingga 5 Outlet</li></ul><div class="label">Target</div><p>Franchise</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA)
    with p4:
        st.markdown(f'<div class="card-v" style="background-color:#0e1117; color:white;"><h4 style="color:white;">🏢 CORPORATE</h4><div class="price" style="color:#FFD700;">Custom</div><div class="label">Deskripsi</div><p style="color:#ccc">Skala Nasional.</p><div class="label">Fitur</div><ul style="color:#ccc"><li>Unlimited Outlet</li><li>Dedicated Dev</li></ul><div class="label">Target</div><p style="color:#ccc">Holding Enterprise</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI CEO", WA)

# 5. HALAMAN MEETING LAB
elif menu == "📝 Meeting Lab":
    st.title("📝 AI Meeting Lab")
    trans = st.text_area("Tempel transkrip rapat di sini:", height=250)
    if st.button("🚀 ANALISIS STRATEGIS"):
        if trans:
            with st.spinner("Menganalisis..."):
                res = model.generate_content(f"Rangkum poin strategis dan action plan: {trans}")
                st.write(res.text)
        else: st.warning("Masukkan teks.")

else:
    st.title("🤖 Admin Panel")
    st.info("Fitur audit transaksi sedang dalam pengembangan.")
