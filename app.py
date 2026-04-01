import streamlit as st
import os

# --- 1. SETTINGS & STYLE (LOCKED) ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #1e293b; border-right: 1px solid #334155; }
    .product-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 20px; border-radius: 20px; border: 1px solid #334155;
        height: 100%; margin-bottom: 20px;
    }
    .price-tag { color: #34d399; font-size: 24px; font-weight: bold; }
    .wa-btn {
        display: block; text-align: center; background-color: #059669; color: white !important;
        padding: 10px; border-radius: 10px; text-decoration: none; font-weight: bold; margin-top: 15px;
    }
    .visi-teks { line-height: 1.8; text-align: justify; color: #cbd5e1; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR (LOCKED) ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    # Menampilkan foto profil
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", use_column_width=True)
    st.markdown('<p style="text-align:center; font-weight:800; font-size:22px; color:white;">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#38bdf8; font-size:13px; margin-top:-10px;">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.divider()
    
    # Definisi Menu yang SANGAT PRESISI
    menu = st.radio("MENU UTAMA:", ["HOME", "PRODUK & LAYANAN", "PORTAL KLIEN", "ADMIN PANEL"])

# --- 3. LOGIKA HALAMAN (SYNCHRONIZED) ---

if menu == "HOME":
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

elif menu == "PRODUK & LAYANAN":
    st.title("🛡️ Detail Layanan & Investasi")
    st.divider()
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="product-card"><h3>V-LITE</h3><div class="price-tag">Rp 1.5M</div><p>SME/UMKM</p><hr><a href="https://wa.me/6282122190885" class="wa-btn">Daftar</a></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="product-card"><h3>V-PRO</h3><div class="price-tag">Rp 3.5M</div><p>Resto & Cafe</p><hr><a href="https://wa.me/6282122190885" class="wa-btn">Daftar</a></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="product-card"><h3>V-SIGHT</h3><div class="price-tag">Rp 5.0M</div><p>Toko Emas</p><hr><a href="https://wa.me/6282122190885" class="wa-btn">Daftar</a></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="product-card"><h3>V-ENTERPRISE</h3><div class="price-tag">CUSTOM</div><p>Korporasi</p><hr><a href="https://wa.me/6282122190885" class="wa-btn">Daftar</a></div>', unsafe_allow_html=True)

elif menu == "PORTAL KLIEN":
    st.title("🔑 Portal Order Pelanggan")
    st.divider()
    
    with st.form("portal_form"):
        st.subheader("Pendaftaran Paket Baru")
        nomor_order = datetime.now().strftime("%Y%m%d%H%M")
        st.info(f"Order ID: VG-{nomor_order}")
        
        c_1, c_2 = st.columns(2)
        with c_1:
            nama_p =
