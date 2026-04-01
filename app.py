import streamlit as st
import hashlib
import os

# --- 1. DATA VISI MISI (LOCKED - 200 WORDS) ---
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

# --- 2. CONFIG & STYLE ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #1e293b; }
    .card { background: #1e293b; padding: 20px; border-radius: 15px; border: 1px solid #334155; margin-bottom: 20px; }
    .price { color: #34d399; font-size: 22px; font-weight: bold; }
    .btn { display: block; text-align: center; background: #059669; color: white !important; padding: 10px; border-radius: 8px; text-decoration: none; margin-top: 15px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
st.sidebar.markdown("<h2 style='text-align:center;'>Erwin Sinaga</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align:center; color:#38bdf8;'>Founder & CEO V-Guard AI</p>", unsafe_allow_html=True)
st.sidebar.divider()
menu = st.sidebar.radio("PILIH MENU:", ["Home", "Produk & Investasi", "Portal Klien", "Admin Panel"])

# --- 4. LOGIC HALAMAN ---

if menu == "Home":
    st.title("🛡️ V-Guard AI Intelligence")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", width=200)
    st.header("Visi & Misi")
    st.markdown(f"<div style='text-align:justify; line-height:1.8; font-size:16px;'>{VISI_MISI_LENGKAP}</div>", unsafe_allow_html=True)
    st.caption("— **Erwin Sinaga**, Founder V-Guard AI Intelligence")

elif menu == "Produk & Investasi":
    st.title("🛡️ Layanan & Investasi")
    # Menggunakan kolom tanpa 'with' agar lebih aman dari IndentationError
    col1, col2, col3, col4 = st.columns(4)
    col1.markdown("<div class='card'><h3>V-LITE</h3><p class='price'>Rp 1.5M</p><p>UMKM</p><a href='#' class='btn'>Daftar</a></div>", unsafe_allow_html=True)
    col2.markdown("<div class='card'><h3>V-PRO</h3><p class='price'>Rp 3.5M</p><p>Resto</p><a href='#' class='btn'>Daftar</a></div>", unsafe_allow_html=True)
    col3.markdown("<div class='card'><h3>V-SIGHT</h3><p class='price'>Rp 5.0M</p><p>Toko Emas</p><a href='#' class='btn'>Daftar</a></div>", unsafe_allow_html=True)
    col4.markdown("<div class='card'><h3>V-ENTERPRISE</h3><p class='price'>CUSTOM</p><p>Korporasi</p><a href='#' class='btn'>Daftar</a></div>", unsafe_allow_html=True)
    
    st.divider()
    st.subheader("📈 Kalkulator ROI")
    omzet = st.number_input("Input Omzet Bulanan (Rp):", value=500000000, step=10000000)
    st.error(f"Potensi Kebocoran (5%): Rp {omzet*0.05:,.0f} / Bulan")
    st.success(f"Target Penyelamatan V-Guard (90%): Rp {(omzet*0.05)*0.9:,.0f} / Bulan")

elif menu == "Portal Klien":
    st.title("🔑 Portal Order")
    with st.form("form_order_vguard"):
        st.write("Lengkapi data pemesanan paket:")
        nama_pelanggan = st.text_input("Nama Lengkap Pelanggan")
        nama_usaha = st.text_input("Nama Usaha / Bisnis")
        paket_pilihan = st.selectbox("Pilih Paket Layanan", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
        upload_berkas = st.file_uploader("Upload Dokumen (KTP/Bukti Bayar)", type=['jpg','png','pdf'])
        
        # Tombol submit dalam form
        submitted = st.form_submit_button("KIRIM PENGAJUAN")
        if submitted:
            if nama_pelanggan and nama_usaha:
                st.success(f"Berhasil! Order untuk {nama_usaha} telah diterima.")
            else:
                st.warning("Mohon isi Nama Pelanggan dan Nama Usaha.")

elif menu == "Admin Panel":
    st.title("🔐 CEO Command Center")
    st.info("Akses terbatas.")

st.sidebar.divider()
st.sidebar.caption("V-Guard AI © 2026")
