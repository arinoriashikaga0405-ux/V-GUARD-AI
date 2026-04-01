import streamlit as st
from PIL import Image
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# API KEY & INTEGRASI CORE BRAIN
GEMINI_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"

# --- CSS CUSTOM ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .package-card { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 20px; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white; font-weight: bold; }
    .feature-list { font-size: 0.85rem; color: #8b949e; line-height: 1.4; }
    .core-brain-box { background-color: #0d1117; padding: 15px; border: 1px solid #1f6feb; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR PROFIL ---
with st.sidebar:
    foto_path = "erwin.jpg"
    if os.path.exists(foto_path):
        try:
            st.image(foto_path, use_container_width=True) # Memastikan foto tetap tampil
        except:
            st.error("File erwin.jpg rusak. Mohon upload ulang.")
    else:
        st.info("Upload 'erwin.jpg' untuk menampilkan foto profil.")
    
    st.markdown("<div style='text-align:center;'><h3>Erwin Sinaga</h3><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Layanan & Investasi", "Portal Klien", "Admin Control Center"])

# --- 1. VISI & MISI (MINIMAL 200 KATA) ---
if menu == "Visi & Misi":
    st.header("Visi & Misi V-Guard AI Intelligence")
    col_v1, col_v2 = st.columns([1, 2])
    with col_v1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg") # Foto di dalam konten Visi & Misi
    
    with col_v2:
        st.markdown("""
        <div style="text-align: justify; color: #8b949e; line-height: 1.8;">
        Sebagai seorang Senior Business Leader dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi produk, melainkan kepastian data dan eliminasi kebocoran internal (internal fraud). Di dunia digital yang serba cepat ini, kepercayaan atau <i>trust</i> tidak lagi cukup jika hanya berdasarkan janji atau intuisi semata; kepercayaan harus bisa diukur, diverifikasi secara matematis, dan didigitalisasi melalui teknologi kecerdasan buatan. Inilah alasan utama saya mendirikan V-Guard AI Intelligence sebagai benteng pertahanan bagi para pemilik bisnis di Indonesia agar aset mereka terlindungi sepenuhnya dari tindakan tidak bertanggung jawab di dalam operasional harian.<br><br>
        
        <b>Visi Kami:</b> Menjadi standar global dalam penyediaan ekosistem Digital Trust yang otonom, transparan, dan tak tergoyahkan. Kami bercita-cita membangun dunia di mana setiap interaksi digital didasari oleh bukti otentik yang dapat diverifikasi secara instan, menghilangkan ambiguitas dalam transaksi bisnis, dan memastikan integritas data menjadi aset yang paling berharga bagi setiap organisasi, mulai dari skala UMKM hingga korporasi multinasional. Kami percaya bahwa transparansi adalah hak setiap pemilik bisnis, dan teknologi kami hadir untuk menjamin hal tersebut terwujud tanpa kompromi sedikitpun di setiap lini perusahaan.<br><br>
        
        <b>Misi Kami:</b> Melaksanakan filosofi 'Eliminating Leakage' dengan dedikasi tinggi melalui integrasi kecerdasan buatan (AI) tingkat lanjut dan teknologi Computer Vision yang canggih. Kami berkomitmen untuk membangun sistem pertahanan prediktif yang mampu menghentikan pola kecurangan sebelum menjadi kerugian finansial yang signifikan bagi klien kami. Melalui prinsip 'Digitizing Trust', kami mengubah setiap titik data mentah menjadi bukti otentik yang tidak dapat dimanipulasi oleh oknum internal maupun eksternal. Kami berdedikasi untuk memberikan ketenangan pikiran bagi setiap pengusaha melalui audit otomatis yang jujur, akurat, dan real-time, demi masa depan ekonomi Indonesia yang lebih bersih, efisien, dan memiliki tingkat kepercayaan digital yang tinggi di kancah internasional.
        </div>
        """, unsafe_allow_html=True)

# --- 2. LAYANAN & INVESTASI (NAMA PRODUK = TOMBOL WA) ---
elif menu == "Layanan & Investasi":
    st.header("🛡️ Produk V-Guard AI (Klik Nama untuk Order)")
    
    def wa_link(produk):
        return f"
