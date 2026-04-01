import streamlit as st
import hashlib
from datetime import datetime
import os

# --- 1. KONFIGURASI KEAMANAN & DATA (LOCKED) ---
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
    .feature-item { color: #cbd5e1; font-size: 13px; margin: 5px 0; list-style-type: '✔ '; }
    .roi-box { background: #1e293b; padding: 25px; border-radius: 15px; border: 1px solid #38bdf8; margin-top: 25px; }
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
    menu = st.radio("MENU UTAMA:", ["Home", "Produk & Layanan", "Portal Klien", "Admin Panel"])

# --- 5. HALAMAN: HOME (VISI MISI UTUH) ---
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

# --- 6. HALAMAN: PRODUK & LAYANAN (DENGAN FITUR LENGKAP) ---
elif menu == "Produk & Layanan":
    st.title("🛡️ Paket Layanan & Kalkulator ROI")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="product-card"><h3>V-LITE</h3><div class="price-tag">Rp 1.5M</div>'
                    '<p class="feature-item">AI Fraud Detection Dasar</p>'
                    '<p class="feature-item">Laporan WA Harian</p>'
                    '<p class="feature-item">Notifikasi Real-time</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="product-card"><h3>V-PRO</h3><div class="price-tag">Rp 3.5M</div>'
                    '<p class="feature-item">Monitor POS Real-time</p>'
                    '<p class="feature-item">Integrasi VCS (Stok)</p>'
                    '<p class="feature-item">Audit Video Harian</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="product-card"><h3>V-SIGHT</h3><div class="price-tag">Rp 5.0M</div>'
                    '<p class="feature-item">AI Behavior Analysis</p>'
                    '<p class="feature-item">Visual Audit Advance</p>'
                    '<p class="feature-item">Cloud Storage 30 Hari</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="product-card"><h3>V-ENTERPRISE</h3><div class="price-tag">CUSTOM</div>'
                    '<p class="feature-item">Multi-Branch System</p>'
                    '<p class="feature-item">Forensik Digital</p>'
                    '<p class="feature-item">Dedicated AI Support</p></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="roi-box">', unsafe_allow_html=True)
    st.subheader("📊 Analisis Potensi Kerugian & ROI")
    omzet = st.number_input("Input Omzet Bulanan (Rp):", value=500000000, step=10000000)
    bocor = omzet * 0.05
    selamat = bocor * 0.90
    c1, c2 = st.columns(2)
    c1.error(f"**Estimasi Kebocoran:** Rp {bocor:,.0f} / bln")
    c2.success(f"**Penyelamatan V-Guard:** Rp {selamat:,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 7. HALAMAN: PORTAL KLIEN (USER AKTIF & PENDAFTARAN) ---
elif menu == "Portal Klien":
    tab1, tab2 = st.tabs(["🔑 Login User Aktif", "📝 Pendaftaran Calon Pelanggan"])
    
    with tab1:
        st.subheader("Portal Klien Teraktivasi")
        with st.form("login_klien"):
            u_id = st.text_input("User ID Klien")
            u_pw = st.text_input("Password", type="password")
            if st.form_submit_button("MASUK DASHBOARD"):
                if u_id in USER_AKTIF and USER_AKTIF[u_id] == u_pw:
                    st.success(f"Selamat Datang, {u_id}. Layanan Anda Aktif.")
                else: st.error("ID belum aktif/salah.")

    with tab2:
        st.subheader("Formulir Calon Pelanggan Baru")
        with st.form("pendaftaran_baru"):
            st.write("Silakan isi data untuk pengajuan aktiv
