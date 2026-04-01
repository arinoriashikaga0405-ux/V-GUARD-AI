import streamlit as st
import hashlib
from datetime import datetime
import os

# --- 1. KONFIGURASI SISTEM (LOCKED) ---
# Nomor WhatsApp Founder Erwin Sinaga
MY_WA = "628212190885" 
ADMIN_PWD_HASH = hashlib.sha256("admin123".encode()).hexdigest()
USER_AKTIF = {"client01": "bayar123", "vguard_user": "sukses2026"}

# --- 2. DATA VISI MISI (UTUH 200+ KATA) ---
VISI_MISI_LENGKAP = (
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

st.markdown(f"""
    <style>
    .main {{ background-color: #0f172a; color: #f8fafc; }}
    [data-testid="stSidebar"] {{ background-color: #1e293b; border-right: 1px solid #334155; }}
    .product-card {{
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 25px; border-radius: 20px; border: 1px solid #334155;
        height: 100%; display: flex; flex-direction: column; justify-content: space-between;
        margin-bottom: 20px;
    }}
    .price-tag {{ color: #34d399; font-size: 26px; font-weight: bold; margin: 10px 0; }}
    .wa-btn {{
        display: block; text-align: center; background-color: #25d366; color: white !important;
        padding: 12px; border-radius: 12px; text-decoration: none; font-weight: bold; margin-top: 15px;
        transition: 0.3s;
    }}
    .wa-btn:hover {{ background-color: #128c7e; }}
    .visi-teks {{ line-height: 1.8; text-align: justify; color: #cbd5e1; font-size: 16px; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_column_width=True)
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
        st.markdown(f'<div class="visi-teks">{VISI_MISI_LENGKAP}</div>', unsafe_allow_html=True)
        st.caption("— **Erwin Sinaga**, Founder V-Guard AI Intelligence")

# --- 6. HALAMAN: PRODUK & LAYANAN (WHATSAPP LINKED) ---
elif menu == "Produk & Layanan":
    st.title("💎 Paket Layanan Digital Trust")
    col1, col2, col3, col4 = st.columns(4)
    
    # Nama Produk dan Fitur
    paket = [
        ("V-LITE", "1.5M", "Audit Fraud Dasar, Laporan WA Harian, Alert Real-time"),
        ("V-PRO", "3.5M", "Monitor POS Online, Integrasi VCS, Audit Video Harian"),
        ("V-SIGHT", "5.0M", "AI Behavior Analysis, Visual Audit Pro, Cloud 30 Hari"),
        ("V-ENTERPRISE", "CUSTOM", "Multi-Branch Management, Forensik Digital AI, Dedicated Support")
    ]

    for i, (name, price, desc) in enumerate(paket):
        with [col1, col2, col3, col4][i]:
            st.markdown(f"""
                <div class="product-card">
                    <h3>{name}</h3>
                    <div class="price-tag">Rp {price}</div>
                    <p style="font-size:12px; color:#cbd5e1;">{desc}</p>
                    <a href="https://wa.me/{MY_WA}?text=Halo%20Pak%20Erwin,%20saya%20ingin%20bertanya%20tentang%20paket%20{name}" 
                       class="wa-btn">DAFTAR VIA WHATSAPP</a>
                </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    st.subheader("📊 Analisis Potensi Penyelamatan Aset (ROI)")
    omzet = st.number_input("Masukkan Omzet Bulanan Bisnis (Rp):", value=500000000, step=10000000)
    bocor = omzet * 0.05
    selamat = bocor * 0.90
    c1, c2 = st.columns(2)
    c1.error(f"**Potensi Kebocoran Internal:** Rp {bocor:,.0f} / bln")
    c2.success(f"**Penyelamatan V-Guard AI:** Rp {selamat:,.0f} / bln")

# --- 7. HALAMAN: PORTAL KLIEN (DAFTAR & LOGIN) ---
elif menu == "Portal Klien":
    tab1, tab2 = st.tabs(["🔑 Login User Aktif", "📝 Pendaftaran Calon Pelanggan"])
    with tab1:
        with st.form("login"):
            uid = st.text_input("User ID Klien")
            upw = st.text_input("Password", type="password")
            if st.form_submit_button("MASUK DASHBOARD"):
                if uid in USER_AKTIF and USER_AKTIF[uid] == upw:
                    st.success(f"Selamat Datang {uid}. Status: AKTIF.")
                else: st.error("ID tidak valid.")
    with tab2:
        with st.form("daftar"):
            st.write("Isi data untuk verifikasi aktivasi:")
            st.text_input("Nama Lengkap Pelanggan")
            st.text_input("Jenis Usaha")
            st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.file_uploader("Upload KTP / Dokumen Usaha")
            if st.form_submit_button("KIRIM DATA PENDAFTARAN"):
                st.success("Data berhasil dikirim ke Admin V-Guard.")

# --- 8. HALAMAN: ADMIN PANEL (LOCKED) ---
elif menu == "Admin Panel":
    st.title("🔐 CEO Command Center")
    pin = st.text_input("Admin PIN Otoritas:", type="password")
    if pin:
        if hashlib.sha256(pin.encode()).hexdigest() == ADMIN_PWD_HASH:
            st.success("Akses Diterima, Pak Founder Erwin Sinaga.")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.subheader("🚨 Monitoring")
                st.button("🔔 Audit Alarms (Active)")
                st.button("📑 Notifikasi Invoice VCS")
                st.button("📹 CCTV Global Link")
            with c2:
                st.subheader("💰 Financials")
                st.button("📊 Laporan Rugi Laba")
                st.button("📉 Audit Fraud Report")
            with c3:
                st.subheader("⚙️ Management")
                st.button("➕ Buat Akun Klien Baru")
                st.button("✅ Verifikasi Pendaftaran")
        else: st.error("PIN Salah.")

st.divider()
st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI Intelligence | @{datetime.now().year} | Founder: Erwin Sinaga</p>', unsafe_allow_html=True)
