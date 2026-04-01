import streamlit as st
import hashlib
import os

# --- 1. DATA MASTER (LOCKED & SAFE) ---
WHATSAPP = "6282122190885"

# Teks Visi Misi dipisah agar tidak merusak struktur kode
VISI_TEKS = (
    "Sebagai seorang <b>Senior Business Leader</b> dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, "
    "saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi, melainkan <b>ketidakpastian data dan kebocoran internal</b>. "
    "Di dunia digital yang serba cepat ini, kepercayaan (trust) tidak lagi cukup jika hanya berdasarkan janji atau intuisi; "
    "kepercayaan harus bisa diukur, diverifikasi, dan didigitalisasi. Inilah alasan utama saya mendirikan <b>V-Guard AI Intelligence</b>.<br><br>"
    "Visi kami adalah menjadi standar global dalam <b>Digital Trust</b>. Kami percaya bahwa setiap pemilik bisnis—mulai dari tokoh retail "
    "mandiri (V-LITE) hingga korporasi multinasional (V-ENTERPRISE)—berhak mendapatkan transparansi mutlak atas aset mereka. "
    "Melalui prinsip <b>'Digitizing Trust'</b>, kami mengubah setiap titik data mentah dari CCTV, mesin kasir (POS), laporan stok gudang (VCS), "
    "dan mutasi bank menjadi bukti otentik yang tidak dapat dimanipulasi oleh siapa pun.<br><br>"
    "Misi utama kami, <b>'Eliminating Leakage'</b>, dijalankan dengan dedikasi tinggi untuk membangun benteng pertahanan "
    "prediktif guna menghentikan pola kebocoran sebelum menjadi kerugian finansial yang signifikan. Kami tidak hanya mendeteksi "
    "kecurangan (fraud) setelah terjadi, tetapi kami memberikan kendali penuh ke tangan pemilik usaha, memberikan ketenangan "
    "pikiran (<i>peace of mind</i>), dan memastikan setiap rupiah yang Anda investasikan bekerja secara jujur dan optimal untuk masa depan bisnis Anda."
)

# --- 2. CONFIG UTAMA ---
st.set_page_config(page_title="V-Guard AI", layout="wide")

# CSS Locked
st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #1e293b; }
    .card { background: #1e293b; padding: 20px; border-radius: 15px; border: 1px solid #334155; margin-bottom: 10px; }
    .btn { display: block; text-align: center; background: #059669; color: white !important; padding: 10px; border-radius: 8px; text-decoration: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (NO ICONS) ---
st.sidebar.markdown("<h2 style='text-align:center;'>Erwin Sinaga</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align:center; color:#38bdf8;'>Founder & CEO V-Guard AI</p>", unsafe_allow_html=True)
st.sidebar.divider()
menu = st.sidebar.radio("MENU:", ["Home", "Produk & Investasi", "Portal Klien", "Admin Panel"])

# --- 4. LOGIC HALAMAN ---
if menu == "Home":
    st.title("🛡️ V-Guard AI Intelligence")
    col1, col2 = st.columns([1, 2])
    with col2:
        st.header("Visi & Misi")
        st.markdown(f"<div style='text-align:justify;'>{VISI_TEKS}</div>", unsafe_allow_html=True)
        st.caption("— Erwin Sinaga, Founder V-Guard AI Intelligence")

elif menu == "Produk & Investasi
