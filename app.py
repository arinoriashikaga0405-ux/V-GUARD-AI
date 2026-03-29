import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os

# 1. KONFIGURASI SISTEM
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Konfigurasi AI (Masukkan kembali API Key Bapak di sini)
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# CSS TAMPILAN MEWAH BIRU NAVY
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; color: white !important; }
    section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] p { color: white !important; }
    .hero-bg { 
        background-color: #0e1117; padding: 50px; border-radius: 20px; color: white; 
        text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px;
    }
    .card-service {
        background-color: white; padding: 25px; border-radius: 15px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center; height: 100%; color: #0e1117;
    }
    </style>
    """, unsafe_allow_html=True)

# FUNGSI UNTUK CEK FOTO
def ambil_foto(lebar):
    nama_file = 'foto_erwin.jpg'
    if os.path.exists(nama_file):
        img = Image.open(nama_file)
        st.image(img, width=lebar)
    else:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)

# 2. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD NAVIGASI")
    ambil_foto(120)
    st.markdown("<center><b>Erwin Sinaga</b><br>Founder V-GUARD</center>", unsafe_allow_html=True)
    st.divider()
    halaman = st.radio("Pilih Halaman:", ["🌐 Promosi & Umum", "👥 Area Layanan Klien", "🔐 Panel Admin"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: PROMOSI & UMUM
# ==========================================
if halaman == "🌐 Promosi & Umum":
    st.markdown("""
        <div class="hero-bg">
            <h1 style='color: #FFD700;'>V-GUARD AI SYSTEMS</h1>
            <h3>Hentikan Kebocoran Finansial Bisnis Anda.</h3>
            <p>Sistem Audit Otonom Berbasis AI | Standar POJK No. 56/2016.</p>
        </div>
        """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 2])
    with c1:
        ambil_foto(300)
    with c2:
        st.markdown("## FILOSOFI & PROFIL")
        st.write("""
        V-GUARD AI Systems hadir sebagai solusi audit masa depan yang transparan dan akurat. 
        Dipimpin oleh Erwin Sinaga, kami berkomitmen menjaga integritas aset bisnis Anda.
        """)
        st.link_button("🟢 KONSULTASI VIA WHATSAPP", "https://wa.me/6281234567890")

    st.write("### Daftar Layanan")
    p1, p2, p3 = st.columns(3)
    p1.markdown('<div class="card-service"><h3>📦 LITE</h3><h2>7,5 Jt</h2><p>Audit Angka Dasar</p></div>', unsafe_allow_html=True)
    p2.markdown('<div class="card-service" style="border: 2px solid #FFD700;"><h3>🚀 PRO</h3><h2 style="color: #FFD700;">15 Jt</h2><p>Investigasi Fraud AI</p></div>', unsafe_allow_html=True)
    p3.markdown('<div class="card-service"><h3>🏢 ENTERPRISE</h3><h2>25 Jt</h2><p>Strategis & Profit</p></div>', unsafe_allow_html=True)

# ==========================================
# HALAMAN 2: AREA KLIEN
# ==========================================
elif halaman == "👥 Area Layanan Klien":
    st.title("👥 Dashboard Monitor Klien")
    data_klien = {
        "Nama Bisnis": ["Resto BSD Utama", "Retail Tangerang", "Cafe Serpong", "Gudang Logistik"],
        "Paket": ["V-GUARD PRO", "V-GUARD LITE", "V-GUARD PRO", "ENTERPRISE"],
        "Status": ["🛡️ Aman", "⚠️ Cek Selisih", "🛡️ Aman", "🛡️ Aman"]
    }
    st.table(pd.DataFrame(data_klien))

# ==========================================
# HALAMAN 3: PANEL ADMIN (SISTEM AI)
# ==========================================
else:
    st.title("🔐 Panel Kendali Admin V-GUARD")
    pw = st.text_input("Password Admin:", type="password")
    if pw == "vguard2026":
        paket = st.selectbox("Pilih Paket Audit:", ["LITE", "PRO", "ENTERPRISE"])
        data_input = st.text_area("Masukkan Data Transaksi:")
        if st.button("JALANKAN AUDIT"):
            # Prompt AI berdasarkan paket
            if paket == "LITE": prompt = "Audit selisih angka: "
            elif paket == "PRO": prompt = "Cari pola kecurangan/fraud: "
            else: prompt = "Berikan analisis strategis profit: "
            
            res = model.generate_content(prompt + data_input)
            st.markdown(res.text)
