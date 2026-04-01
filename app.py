import streamlit as st
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG & KEAMANAN (LOCKED) ---
WHATSAPP_NUMBER = "6282122190885" 
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

if 'auth_vguard' not in st.session_state:
    st.session_state['auth_vguard'] = False

# --- 2. PREMIUM UI DESIGN (ASLI & RAPI) ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #1e293b; border-right: 1px solid #334155; }
    .product-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 20px; border-radius: 20px; border: 1px solid #334155;
        height: 100%; display: flex; flex-direction: column; justify-content: space-between;
    }
    .price-tag { color: #34d399; font-size: 24px; font-weight: bold; margin: 5px 0; }
    .feature-list { font-size: 12px; color: #cbd5e1; text-align: left; line-height: 1.5; }
    .wa-btn {
        display: block; text-align: center; background-color: #059669; color: white !important;
        padding: 10px; border-radius: 10px; text-decoration: none; font-weight: bold; margin-top: 15px;
    }
    .visi-teks { line-height: 1.8; text-align: justify; color: #cbd5e1; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (LOCKED) ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", use_column_width=True)
    st.markdown('<p style="text-align:center; font-weight:800; font-size:22px; color:white;">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#38bdf8; font-size:13px; margin-top:-10px;">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.divider()
    menu = st.radio("MENU UTAMA:", ["Home", "Produk & Investasi", "Portal Klien", "Admin Panel"])

# --- 4. HALAMAN: HOME (VISI MISI 200 KATA) ---
if menu == "Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.subheader("Digitizing Trust, Eliminating Leakage")
    st.divider()
    
    col_img, col_text = st.columns([1, 2])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_column_width=True)
    with col_text:
        st.header("Visi & Misi")
        st.markdown("""
        <div class="visi-teks">
        Sebagai seorang <b>Senior Business Leader</b> dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, 
        saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi, melainkan <b>ketidakpastian data dan kebocoran internal</b>. 
        Di dunia digital yang serba cepat ini, kepercayaan (trust) tidak lagi cukup jika hanya berdasarkan janji atau intuisi; 
        kepercayaan harus bisa diukur, diverifikasi, dan didigitalisasi. Inilah alasan utama saya mendirikan <b>V-Guard AI Intelligence</b>.<br><br>
        Visi kami adalah menjadi standar global dalam <b>Digital Trust</b>. Kami percaya bahwa setiap pemilik bisnis—mulai dari tokoh retail 
        mandiri (V-LITE) hingga korporasi multinasional (V-ENTERPRISE)—berhak mendapatkan transparansi mutlak atas aset mereka. 
        Melalui prinsip <b>'Digitizing Trust'</b>, kami mengubah setiap titik data mentah dari CCTV, mesin kasir (POS), laporan stok gudang (VCS), 
        dan mutasi bank menjadi bukti otentik yang tidak dapat dimanipulasi oleh siapa pun.<br><br>
        Misi utama kami, <b>'Eliminating Leakage'</b>, dijalankan dengan dedikasi tinggi untuk membangun benteng pertahanan 
        prediktif guna menghentikan pola kebocoran sebelum menjadi kerugian finansial yang signifikan. Kami tidak hanya mendeteksi 
        kecurangan (fraud) setelah terjadi, tetapi kami memberikan kendali penuh ke tangan pemilik usaha, memberikan ketenangan 
        pikiran (<i>peace of mind</i>), dan memastikan setiap rupiah yang Anda investasikan bekerja secara jujur dan optimal untuk masa depan bisnis Anda.
        </div>
        """, unsafe_allow_html=True)
        st.caption("— **Erwin Sinaga**, Founder V-Guard AI Intelligence")

# --- 5. HALAMAN: PRODUK & INVESTASI ---
elif menu == "Produk & Investasi":
    st
