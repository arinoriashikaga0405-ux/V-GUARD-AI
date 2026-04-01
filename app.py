import streamlit as st
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG & KEAMANAN ---
WHATSAPP_NUMBER = "6282122190885" 
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

if 'auth_vguard' not in st.session_state:
    st.session_state['auth_vguard'] = False

# --- 2. PREMIUM UI DESIGN ---
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
    .roi-container {
        background: #1e293b; padding: 30px; border-radius: 20px; 
        border: 1px solid #334155; margin-top: 40px;
    }
    .loss-alert { background-color: #fee2e2; color: #991b1b; padding: 15px; border-radius: 10px; font-weight: bold; margin-bottom: 10px; }
    .save-alert { background-color: #d1fae5; color: #065f46; padding: 15px; border-radius: 10px; font-weight: bold; }
    .visi-teks { line-height: 1.8; text-align: justify; color: #cbd5e1; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_column_width=True)
    st.markdown('<p style="text-align:center; font-weight:800; font-size:22px; color:white;">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#38bdf8; font-size:13px; margin-top:-10px;">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.divider()
    menu = st.radio("NAVIGASI:", ["🏠 Home", "📦 Produk & Investasi", "🔑 Portal Klien", "🔐 Admin Panel"])

# --- 📂 HALAMAN: HOME (VISI MISI UTUH) ---
if menu == "🏠 Home":
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
        st.caption(f"— **Erwin Sinaga**, Founder V-Guard AI Intelligence")

# --- 📂 HALAMAN: PRODUK & INVESTASI ---
elif menu == "📦 Produk & Investasi":
    st.title("🛡️ Detail Layanan & Investasi V-Guard AI")
    
    col1, col2, col3, col4 = st.columns(4)
    
    # 1. V-LITE
    with col1:
        st.markdown(f'''<div class="product-card">
            <h3>V-LITE</h3>
            <p style="font-size:11px; color:#38bdf8;">Target: Toko Mandiri / UMKM</p>
            <div class="price-tag">Rp 1.5M</div>
            <small>Bulanan: 750rb</small><hr>
            <div class="feature-list">
                • <b>AI Fraud Dasar:</b> Deteksi Void mencurigakan.<br>
                • <b>Laporan PDF WA:</b> Ringkasan bulanan otomatis.<br>
                • <b>Notifikasi Standar:</b> Selisih stok signifikan.<br>
                • <b>Akses 1 User:</b> Khusus Pemilik.
            </div>
            <a href="https://wa.me/{WHATSAPP_NUMBER}" class="wa-btn">Daftar Sekarang</a>
        </div>''', unsafe_allow_html=True)

    # 2. V-PRO
    with col2:
        st.markdown(f'''<div class="product-card">
            <h3>V-PRO</h3>
            <p style="font-size:11px; color:#38bdf8;">Target: Resto / Cafe / Retail</p>
            <div class="price-tag">Rp 3.5M</div>
            <small>Bulanan: 1.2jt</small><hr>
            <div class="feature-list">
                • <b>Real-Time Monitor:</b> Notifikasi instan ke HP.<br>
                • <b>VCS Integrasi:</b> Sinkron Stok-Kasir-Bank.<br>
                • <b>Audit Harian:</b> Closing terverifikasi AI.<br>
                • <b>Prioritas Support:</b> Bantuan teknis utama.
            </div>
            <a href="https://wa.me/{WHATSAPP_NUMBER}" class="wa-btn">Daftar Sekarang</a>
        </div>''', unsafe_allow_html=True)

    # 3. V-SIGHT
    with col3:
        st.markdown(f'''<div class="product-card">
            <h3>V-SIGHT</h3>
            <p style="font-size:11px; color:#38bdf8;">Target: Toko Emas / Gudang</p>
            <div class="price-tag">Rp 5.0M</div>
            <small>Bulanan: 1.5jt</small><hr>
            <div class="feature-list">
                • <b>AI Behavior:</b> Baca gerak-gerik mencurigakan.<br>
                • <b>Visual Audit:</b> Cocokkan struk & video CCTV.<br>
                • <b>Deteksi Fisik:</b> Hitung objek/orang masuk.<br>
                • <b>Cloud Storage:</b> Rekaman aman tidak bisa dihapus.
            </div>
            <a href="https://wa.me/{WHATSAPP_NUMBER}" class="wa-btn">Daftar Sekarang</a>
        </div>''', unsafe_allow_html=True)

    # 4. V-ENTERPRISE
    with col4:
        st.markdown(f'''<div class="product-card">
            <h3>V-ENTERPRISE</h3>
            <p style="font-size:11px; color:#38bdf8;">Target: Korporasi / Pabrik</p>
            <div class="price-tag">CUSTOM</div>
            <small>Skala Korporasi</small><hr>
            <div class="feature-list">
                • <b>Multi-Cabang:</b> Monitoring ratusan cabang.<br>
                • <b>Forensik Digital:</b> Investigasi korupsi sistematis.<br>
                • <b>Dedicated Server:</b> Keamanan tingkat perbankan.<br>
                • <b>Custom API:</b> Integrasi ERP & Akuntansi.
            </div>
            <a href="https://wa.me/{WHATSAPP_NUMBER}" class="wa-btn">Daftar Sekarang</a>
        </div>''', unsafe_allow_html=True)

    st.divider()

    # BAGIAN BAWAH: KALKULATOR ROI
    st.markdown("### 📈 Kalkulator Penyelamatan Aset (ROI)")
    with st.container():
        st.markdown('<div class="roi-container">', unsafe_allow_html=True)
        omzet = st.number_input("Input Omzet Bulanan Bisnis (Rp):", min_value=0, value=500000000, step=10000000)
        loss = omzet * 0.05
        save = loss * 0.90
        st.markdown(f'<div class="loss-alert">🚨 Estimasi Kebocoran Aset (5%): Rp {loss:,.0f} / Bulan</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="save-alert">🛡️ Target Penyelamatan V-Guard (90%): Rp {save:,.0f} / Bulan</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI | @{datetime.now().year} | Erwin Sinaga</p>', unsafe_allow_html=True)
