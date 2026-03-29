import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

# 1. SETUP DASAR
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# API KEY (Pastikan tidak ada spasi di awal/akhir)
GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("AI Belum Siap.")

# LOGIN STATE
if 'role' not in st.session_state:
    st.session_state.role = None

# 2. DESIGN (Format Satu Baris Agar Tidak Eror Tanda Petik)
st.markdown('<style>.hero-bg { background: #0e1117; padding: 25px; border-radius: 15px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 30px; }.card-v { background: white; padding: 18px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); border-top: 5px solid #FFD700; height: 500px; display: flex; flex-direction: column; justify-content: space-between; }.card-v h4 { font-size: 18px; color: #111; font-weight: bold; text-align: center; }.card-v .price { font-size: 20px; color: #d42f2f; font-weight: bold; text-align: center; }.card-v .label { font-size: 11px; font-weight: bold; color: #999; text-transform: uppercase; margin-top: 5px; }.card-v p, .card-v ul { font-size: 13px; color: #333; margin: 2px 0; }.stLinkButton button { width: 100%; background-color: #FFD700 !important; color: #000 !important; }</style>', unsafe_allow_html=True)

# 3. SIDEBAR & NAVIGASI
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    if os.path.exists('erwin.jpg'):
        st.image('erwin.jpg', width=80)
    st.markdown("<b>Erwin Sinaga</b><br><small>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()
    menu = st.radio("Navigasi:", ["🌐 Beranda", "📝 Meeting Lab", "📊 Dashboard"])
    
    if not st.session_state.role:
        with st.form("login"):
            u = st.text_input("User").lower()
            p = st.text_input("Pass", type="password")
            if st.form_submit_button("Masuk"):
                if u == "admin" and p == "Vguard2026":
                    st.session_state.role = "admin"
                    st.rerun()
    else:
        if st.button("Logout"):
            st.session_state.role = None
            st.rerun()

# 4. ISI HALAMAN BERANDA
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    
    WA = "https://wa.me/6282122190885"
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown('<div class="card-v"><h4>🌱 V-START</h4><div class="price">3,5 Jt /Bln</div><div class="label">Deskripsi</div><p>Audit otomatis mandiri.</p><div class="label">Fitur</div><ul><li>Cek Stok</li><li>Laporan Mingguan</li></ul><div class="label">Target</div><p>UMKM Mikro / Kedai.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL", WA)

    with c2:
        st.markdown('<div class="card-v"><h4>📦 V-LITE</h4><div class="price">7,5 Jt /Bln</div><div class="label">Deskripsi</div><p>Monitoring jarak jauh aktif.</p><div class="label">Fitur</div><ul><li>Laporan WA Real-time</li><li>Integrasi POS</li></ul><div class="label">Target</div><p>Retailer & Cafe.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL", WA)

    with c3:
        st.markdown('<div class="card-v" style="border: 2px solid #FFD700;"><h4>🚀 V-PRO</h4><div class="price">15 Jt /Bln</div><div class="label">Deskripsi</div><p>Deep AI Fraud Audit.</p><div class="label">Fitur</div><ul><li>Analisis Perilaku</li><li>Hingga 5 Outlet</li></ul><div class="label">Target</div><p>Franchise & Cabang.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL", WA)

    with c4:
        st.markdown('<div class="card-v" style="background-color:#0e1117; color:white;"><h4 style="color:white;">🏢 CORPORATE</h4><div class="price" style="color:#FFD700;">Custom</div><div class="label">Deskripsi</div><p style="color:#ccc">Proteksi skala nasional.</p><div class="label">Fitur</div><ul style="color:#ccc"><li>Unlimited Outlet</li><li>Dedicated Support</li></ul><div class="label">Target</div><p style="color:#ccc">Holding & Enterprise.</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI CEO", WA)

elif menu == "📝 Meeting Lab":
    st.title("📝 Meeting Lab")
    txt = st.text_area("Tempel transkrip rapat:")
    if st.button("Analisis AI"):
        if txt:
            res = model.generate_content(f"Rangkum: {txt}")
            st.write(res.text)

else:
    st.title("📊 Dashboard")
    st.info("Silakan login untuk melihat data.")
