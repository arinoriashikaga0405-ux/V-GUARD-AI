import streamlit as st
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG & KEAMANAN ---
WHATSAPP_NUMBER = "6282122190885" 
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()
CLIENT_LICENSES = ["VGUARD-2026-001", "VGUARD-VIP-ERWIN", "VGUARD-PRO-JAYA"]

if 'auth_vguard' not in st.session_state:
    st.session_state['auth_vguard'] = False
if 'client_authenticated' not in st.session_state:
    st.session_state['client_authenticated'] = False

# --- 2. PREMIUM UI DESIGN ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #1e293b; border-right: 1px solid #334155; }
    
    .founder-name { text-align: center; font-weight: 800; font-size: 24px; color: white; margin-top: 10px; }
    .founder-title { text-align: center; color: #38bdf8; font-size: 13px; margin-top: -10px; font-weight: 500; }

    /* Card Produk */
    .product-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 25px; border-radius: 20px; border: 1px solid #334155;
        text-align: center; height: 100%;
    }
    .price-tag { color: #34d399; font-size: 26px; font-weight: bold; margin: 10px 0; }
    .wa-btn {
        display: block; text-align: center; background-color: #059669; color: white !important;
        padding: 12px; border-radius: 12px; text-decoration: none; font-weight: bold; margin-top: 20px;
    }
    
    /* Panel ROI (Bagian Bawah) */
    .roi-section {
        background: rgba(52, 211, 153, 0.05);
        border: 2px dashed #34d399;
        padding: 30px; border-radius: 25px; margin-top: 50px;
    }
    .roi-title { color: #34d399; font-size: 22px; font-weight: 800; margin-bottom: 20px; text-align: center; }
    .roi-box { background: #1e293b; padding: 15px; border-radius: 15px; border: 1px solid #334155; text-align: center; }
    .visi-teks { line-height: 1.8; text-align: justify; color: #cbd5e1; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_column_width=True)
    st.markdown('<p class="founder-name">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p class="founder-title">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.divider()
    menu = st.radio("FOLDER NAVIGASI:", ["🏠 Home", "📦 Produk & Investasi", "🔑 Portal Klien", "🔐 Admin Panel"])

# --- 📂 FOLDER 1: HOME (VISI MISI UPDATE) ---
if menu == "🏠 Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.subheader("Digitizing Trust, Eliminating Leakage")
    st.divider()
    
    col_a, col_b = st.columns([1, 2])
    with col_a:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_column_width=True)
    with col_b:
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
        st.caption(f"— **Erwin Sinaga**, Founder V-Guard AI Intelligence")

# --- 📂 FOLDER 2: PRODUK & INVESTASI (2 BAGIAN) ---
elif menu == "📦 Produk & Investasi":
    st.title("🛡️ Layanan Investasi V-Guard AI")
    st.write("Pilih tingkatan proteksi sistem untuk bisnis Anda.")
    
    # BAGIAN ATAS: PRODUK
    col1, col2, col3, col4 = st.columns(4)
    products = [
        ("V-LITE", "1.5M", "250rb", "• AI Fraud Dasar<br>• Laporan PDF WA"),
        ("V-PRO", "3.5M", "750rb", "• Real-Time Monitor<br>• VCS Automate"),
        ("V-SIGHT", "5.0M", "1.2jt", "• Behavior Visual<br>• Secure Cloud Storage"),
        ("V-ENTERPRISE", "CUSTOM", "Custom", "• Multi-Cabang Central<br>• Digital Forensik")
    ]
    cols = [col1, col2, col3, col4]
    for i, (name, price, monthly, desc) in enumerate(products):
        with cols[i]:
            st.markdown(f'''<div class="product-card">
                <h3>{name}</h3><div class="price-tag">Rp {price}</div><small>Bulanan: {monthly}</small><hr>
                <p style="font-size:13px; color:#cbd5e1; text-align:left;">{desc}</p>
                <a href="https://wa.me/{WHATSAPP_NUMBER}" class="wa-btn">Daftar Sekarang</a>
            </div>''', unsafe_allow_html=True)

    # BAGIAN BAWAH: PANEL ROI
    st.markdown('<div class="roi-section">', unsafe_allow_html=True)
    st.markdown('<p class="roi-title">📊 ANALISIS POTENSI ROI (PENYELAMATAN KERUGIAN)</p>', unsafe_allow_html=True)
    r1, r2, r3, r4 = st.columns(4)
    roi_data = ["Rp 2jt - 5jt", "Rp 10jt - 25jt", "Rp 30jt - 75jt", "> Rp 100jt"]
    for i, val in enumerate(roi_data):
        with [r1, r2, r3, r4][i]:
            st.markdown(f'<div class="roi-box"><small>SAVE ESTIMATE</small><br><b style="color:#34d399; font-size:18px;">{val}</b><br><small>/ Bulan</small></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 📂 FOLDER 3: PORTAL KLIEN (NAMA, PAKET, HARGA) ---
elif menu == "🔑 Portal Klien":
    st.title("🔑 Portal Pelanggan")
    tab_reg, tab_active = st.tabs(["📝 Pendaftaran Baru", "🔓 Akses Client Aktif"])
    with tab_reg:
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Nama Pelanggan")
            st.text_input("Nama Bisnis")
        with c2:
            st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.text_input("Harga Investasi (Rp)")
        if st.button("🚀 Kirim Pendaftaran"): st.success("Data terkirim.")

    with tab_active:
        if not st.session_state['client_authenticated']:
            client_key = st.text_input("ID Lisensi", type="password")
            if st.button("Buka Dashboard"):
                if client_key in CLIENT_LICENSES:
                    st.session_state['client_authenticated'] = True
                    st.rerun()
                else: st.error("ID Lisensi salah.")
        else:
            st.success("Dashboard Aktif.")
            if st.button("🔒 Keluar"):
                st.session_state['client_authenticated'] = False
                st.rerun()

# --- 📂 FOLDER 4: ADMIN PANEL ---
elif menu == "🔐 Admin Panel":
    st.header("🔐 CEO Command Center")
    if not st.session_state['auth_vguard']:
        pwd = st.text_input("Sandi Founder", type="password")
        if st.button("Login Admin"):
            if hashlib.sha256(pwd.encode()).hexdigest() == ADMIN_PWD_HASH:
                st.session_state['auth_vguard'] = True
                st.rerun()
            else: st.error("Akses Ditolak.")
    else:
        st.subheader("📁 Folder Internal: Kirim ke Engine AI")
        st.file_uploader("Upload Data", type=['csv','xlsx'])
        if st.button("Logout Admin"):
            st.session_state['auth_vguard'] = False
            st.rerun()

st.divider()
st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI | @{datetime.now().year} | Erwin Sinaga</p>', unsafe_allow_html=True)
