import streamlit as st
import hashlib
import os

# --- 1. DATA VISI MISI (LOCKED - 200 WORDS) ---
# Kita simpan di variabel agar tidak mengganggu struktur menu
VISI_MISI_TEXT = (
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

# --- 2. CONFIG & STYLE (LOCKED) ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #1e293b; }
    .card { background: #1e293b; padding: 20px; border-radius: 15px; border: 1px solid #334155; margin-bottom: 10px; }
    .price { color: #34d399; font-size: 20px; font-weight: bold; }
    .btn { display: block; text-align: center; background: #059669; color: white !important; padding: 8px; border-radius: 5px; text-decoration: none; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (NO ICONS - CLEAN) ---
st.sidebar.markdown("<h2 style='text-align:center;'>Erwin Sinaga</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align:center; color:#38bdf8;'>Founder & CEO V-Guard AI</p>", unsafe_allow_html=True)
st.sidebar.divider()
menu = st.sidebar.radio("PILIH MENU:", ["Home", "Produk & Investasi", "Portal Klien", "Admin Panel"])

# --- 4. LOGIC HALAMAN ---

if menu == "Home":
    st.title("🛡️ V-Guard AI Intelligence")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_column_width=True)
    with col2:
        st.header("Visi & Misi")
        st.markdown(f"<div style='text-align:justify; line-height:1.6;'>{VISI_MISI_TEXT}</div>", unsafe_allow_html=True)
        st.caption("— Erwin Sinaga, Founder V-Guard AI Intelligence")

elif menu == "Produk & Investasi":
    st.title("🛡️ Layanan & Investasi")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div class='card'><h3>V-LITE</h3><p class='price'>Rp 1.5M</p><p>750rb/bln</p><a href='#' class='btn'>Daftar</a></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'><h3>V-PRO</h3><p class='price'>Rp 3.5M</p><p>1.2jt/bln</p><a href='#' class='btn'>Daftar</a></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card'><h3>V-SIGHT</h3><p class='price'>Rp 5.0M</p><p>1.5jt/bln</p><a href='#' class='btn'>Daftar</a></div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='card'><h3>V-ENTERPRISE</h3><p class='price'>CUSTOM</p><p>Skala Besar</p><a href='#' class='btn'>Daftar</a></div>", unsafe_allow_html=True)
    
    st.divider()
    st.subheader("📈 Kalkulator ROI")
    omzet = st.number_input("Input Omzet Bulanan (Rp):", value=500000000, step=10000000)
    st.error(f"Estimasi Kebocoran (5%): Rp {omzet*0.05:,.0f}")
    st.success(f"Penyelamatan V-Guard (90%): Rp {(omzet*0.05)*0.9:,.0f}")

elif menu == "Portal Klien":
    st.title("🔑 Portal Order")
    with
