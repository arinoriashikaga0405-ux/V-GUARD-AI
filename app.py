import streamlit as st
import hashlib
from datetime import datetime
import os

# --- 1. KONFIGURASI KEAMANAN (LOCKED) ---
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
        padding: 20px; border-radius: 20px; border: 1px solid #334155;
        height: 100%; display: flex; flex-direction: column; justify-content: space-between;
        margin-bottom: 20px;
    }
    .price-tag { color: #34d399; font-size: 24px; font-weight: bold; margin: 5px 0; }
    .roi-box { background: #1e293b; padding: 25px; border-radius: 15px; border: 1px solid #38bdf8; margin-top: 20px; }
    .wa-btn {
        display: block; text-align: center; background-color: #059669; color: white !important;
        padding: 10px; border-radius: 10px; text-decoration: none; font-weight: bold; margin-top: 15px;
    }
    .visi-teks { line-height: 1.8; text-align: justify; color: #cbd5e1; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_column_width=True)
    st.markdown('<p style="text-align:center; font-weight:800; font-size:22px; color:white;">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#38bdf8; font-size:13px; margin-top:-10px;">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.divider()
    menu = st.radio("MENU UTAMA:", ["Home", "Produk & ROI", "Portal Klien", "Admin Panel"])

# --- 5. HALAMAN: HOME (VISI MISI UTUH) ---
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
        st.markdown(f'<div class="visi-teks">{VISI_MISI_UTUH}</div>', unsafe_allow_html=True)
        st.caption("— **Erwin Sinaga**, Founder V-Guard AI Intelligence")

# --- 6. HALAMAN: PRODUK & ROI KERUGIAN ---
elif menu == "Produk & ROI":
    st.title("🛡️ Layanan & Kalkulator ROI")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown('<div class="product-card"><h3>V-LITE</h3><div class="price-tag">Rp 1.5M</div><p>UMKM Dasar</p><a href="#" class="wa-btn">Daftar</a></div>', unsafe_allow_html=True)
    with col2: st.markdown('<div class="product-card"><h3>V-PRO</h3><div class="price-tag">Rp 3.5M</div><p>Resto/Retail</p><a href="#" class="wa-btn">Daftar</a></div>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="product-card"><h3>V-SIGHT</h3><div class="price-tag">Rp 5.0M</div><p>Toko Emas</p><a href="#" class="wa-btn">Daftar</a></div>', unsafe_allow_html=True)
    with col4: st.markdown('<div class="product-card"><h3>V-ENTERPRISE</h3><div class="price-tag">CUSTOM</div><p>Korporasi</p><a href="#" class="wa-btn">Daftar</a></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="roi-box">', unsafe_allow_html=True)
    st.subheader("📊 Analisis ROI & Potensi Kerugian")
    omzet = st.number_input("Masukkan Omzet Bulanan Bisnis Anda (Rp):", value=500000000, step=10000000)
    bocor = omzet * 0.05
    selamat = bocor * 0.90
    
    c_roi1, c_roi2 = st.columns(2)
    with c_roi1: st.error(f"**Estimasi Kebocoran Anda:**\n\nRp {bocor:,.0f} / Bulan")
    with c_roi2: st.success(f"**Penyelamatan V-Guard AI:**\n\nRp {selamat:,.0f} / Bulan")
    st.info(f"Dalam 1 tahun, V-Guard menyelamatkan aset Anda senilai: **Rp {selamat*12:,.0f}**")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 7. HALAMAN: PORTAL KLIEN (LOGIN USER AKTIF) ---
elif menu == "Portal Klien":
    st.title("🔑 Portal Klien Teraktivasi")
    with st.form("login_klien"):
        st.write("Login Khusus Klien yang Sudah Aktifasi")
        u_id = st.text_input("User ID Klien")
        u_pw = st.text_input("Password", type="password")
        if st.form_submit_button("LOGIN PORTAL"):
            if u_id in USER_AKTIF and USER_AKTIF[u_id] == u_pw:
                st.success(f"Selamat Datang, {u_id}! Layanan Anda AKTIF.")
            else:
                st.error("Akses Ditolak. Pastikan pembayaran sudah diaktifkan oleh Admin.")

# --- 8. HALAMAN: ADMIN PANEL (LOCKED) ---
elif menu == "Admin Panel":
    st.title("🔐 CEO Command Center")
    with st.form("login_admin"):
        a_pw = st.text_input("Admin PIN:", type="password")
        if st.form_submit_button("MASUK ADMIN"):
            if hashlib.sha256(a_pw.encode()).hexdigest() == ADMIN_PWD_HASH:
                st.success("Akses Diterima, Pak Founder.")
                st.write("### Daftar Antrian Aktifasi Klien")
                st.table([{"Nama": "Toko Berkah", "Paket": "V-LITE", "Bukti": "Terunggah"}])
            else:
                st.error("PIN Salah.")

st.divider()
st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI | @{datetime.now().year} | Erwin Sinaga</p>', unsafe_allow_html=True)
