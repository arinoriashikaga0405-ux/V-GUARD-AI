import streamlit as st
import hashlib
from datetime import datetime
import os
import urllib.parse

# --- 1. KONFIGURASI KEAMANAN & API (LOCKED) ---
WA_NUMBER = "628212190885" 
API_KEY_AI = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
ADMIN_PWD_HASH = hashlib.sha256("admin123".encode()).hexdigest()
USER_AKTIF = {"client01": "bayar123", "vguard_user": "sukses2026"}

# --- 2. DATA VISI MISI (UTUH 200 KATA) ---
VISI_MISI_UTUH = (
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

# --- 3. PREMIUM UI STYLE ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #1e293b; border-right: 1px solid #334155; }
    .product-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 25px; border-radius: 20px; border: 1px solid #334155;
        height: 100%; display: flex; flex-direction: column; justify-content: space-between;
        margin-bottom: 20px;
    }
    .price-tag { color: #34d399; font-size: 26px; font-weight: bold; margin: 10px 0; }
    .feature-item { color: #cbd5e1; font-size: 13px; margin: 5px 0; line-height: 1.4; }
    .wa-btn {
        display: block; text-align: center; background-color: #059669; color: white !important;
        padding: 12px; border-radius: 10px; text-decoration: none; font-weight: bold; margin-top: 15px;
    }
    .roi-box { background: #1e293b; padding: 25px; border-radius: 15px; border: 1px solid #38bdf8; margin-top: 25px; }
    .visi-teks { line-height: 1.8; text-align: justify; color: #cbd5e1; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", use_column_width=True)
    st.markdown('<p style="text-align:center; font-weight:800; font-size:22px; color:white;">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#38bdf8; font-size:13px; margin-top:-10px;">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.divider()
    menu = st.radio("MENU UTAMA:", ["Home", "Produk & Layanan", "Portal Klien", "Admin Panel"])

# --- 5. HALAMAN: HOME ---
if menu == "Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.subheader("Digitizing Trust, Eliminating Leakage")
    st.divider()
    col_img, col_text = st.columns([1, 2])
    with col_img:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_column_width=True)
    with col_text:
        st.header("Visi & Misi")
        st.markdown(f'<div class="visi-teks">{VISI_MISI_UTUH}</div>', unsafe_allow_html=True)
        st.caption("— **Erwin Sinaga**, Founder V-Guard AI Intelligence")

# --- 6. HALAMAN: PRODUK & LAYANAN ---
elif menu == "Produk & Layanan":
    st.title("🛡️ Paket Layanan & ROI")
    col1, col2, col3, col4 = st.columns(4)
    
    def create_wa_link(package):
        msg = f"Halo Pak Erwin, saya tertarik daftar paket {package} di V-Guard AI."
        return f"https://wa.me/{WA_NUMBER}?text={urllib.parse.quote(msg)}"

    with col1:
        st.markdown(f'<div class="product-card"><h3>V-LITE</h3><div class="price-tag">Rp 1.5M</div>'
                    '<p class="feature-item">✔ AI Fraud Detection Dasar</p>'
                    '<p class="feature-item">✔ Laporan WA Harian</p>'
                    '<p class="feature-item">✔ Notifikasi Real-time</p>'
                    f'<a href="{create_wa_link("V-LITE")}" class="wa-btn">Daftar</a></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="product-card"><h3>V-PRO</h3><div class="price-tag">Rp 3.5M</div>'
                    '<p class="feature-item">✔ Monitor POS Real-time</p>'
                    '<p class="feature-item">✔ Integrasi VCS (Stok)</p>'
                    '<p class="feature-item">✔ Audit Video Harian</p>'
                    f'<a href="{create_wa_link("V-PRO")}" class="wa-btn">Daftar</a></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="product-card"><h3>V-SIGHT</h3><div class="price-tag">Rp 5.0M</div>'
                    '<p class="feature-item">✔ AI Behavior Analysis</p>'
                    '<p class="feature-item">✔ Visual Audit Advance</p>'
                    '<p class="feature-item">✔ Cloud Storage 30 Hari</p>'
