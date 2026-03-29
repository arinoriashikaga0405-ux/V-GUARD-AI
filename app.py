import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
# Menggunakan VGUARD AI Systems sebagai judul tab
st.set_page_config(page_title="VGUARD AI Systems - Founder Erwin", page_icon="🛡️", layout="wide")

# --- 2. CSS CUSTOM UNTUK TAMPILAN GAGAH ---
st.markdown("""
    <style>
    /* Mengubah warna background halaman utama */
    .main { background-color: #f0f2f6; }
    
    /* Membuat Title lebih besar dan berbayang */
    .big-title { font-size: 3.5rem !important; font-weight: bold; color: #1a237e; text-shadow: 2px 2px 4px rgba(0,0,0,0.1); margin-bottom: 0px;}
    
    /* Membuat Subheader lebih jelas */
    .cool-subheader { font-size: 1.5rem !important; color: #3949ab; font-weight: normal; margin-top: 0px;}
    
    /* Membuat Misi dalam kotak biru yang modern */
    .mission-box { background-color: #e8eaf6; padding: 20px; border-radius: 10px; border-left: 10px solid #3949ab; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin: 20px 0;}
    .mission-text { font-size: 1.2rem !important; color: #1a237e; font-style: italic;}
    
    /* Membuat Teks Profil & Filosofi */
    .profil-title { font-size: 1.8rem !important; font-weight: bold; color: #1a237e; margin-top: 20px;}
    .profil-text { font-size: 1.1rem !important; line-height: 1.6; color: #333;}
    
    /* Mendesain 4 Kotak Paket Harga agar modern dan klik-able */
    div.stInfo, div.stWarning, div.stError, div.stSuccess { border-radius: 10px; padding: 25px !important; box-shadow: 0 10px 15px rgba(0,0,0,0.05); transition: 0.3s; margin-bottom: 20px; text-align: center; color: black; }
    div.stInfo:hover, div.stWarning:hover, div.stError:hover, div.stSuccess:hover { box-shadow: 0 15px 20px rgba(0,0,0,0.1); transform: translateY(-5px); }
    
    /* Tombol Kontak Kami di bagian bawah */
    .stButton>button { width: 100%; border-radius: 5px; height: 3.5em; background-color: #1a237e; color: white; font-weight: bold; font-size: 1.2rem;}
    .stButton>button:hover { background-color: #3949ab; color: white; border: none; }
    
    /* Menghilangkan margin atas agar foto profil tidak terlalu jauh */
    .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGASI (Fitur Tetap Lengkap) ---
with st.sidebar:
    try:
        # PENTING: File 'erwin.jpg' harus ada di folder yang sama di GitHub
        st.image("erwin.jpg", width=200, caption="Erwin - Founder & CEO")
    except:
        st.write("👤 [Foto Erwin Belum Diupload]")

    st.title("🛡️ VGUARD AI")
    st.write("---")
    
    menu = st.sidebar.radio("Navigasi Sistem", [
        "Beranda Eksekutif", 
        "Dashboard Performa (Demo)", 
        "AI Scanner Audit (Fitur Utama)"
    ])

# --- 4. LOGIKA MENU (Edisi CEO yang Lebih Keren) ---

if menu == "Beranda Eksekutif":
    # HEADER BRANDING (Modern & Gagah)
    st.markdown('<p class="big-title">🛡️ VGUARD AI Systems</p>', unsafe_allow_html=True)
    st.markdown('<p class="cool-subheader">*Next-Generation Operational Security & Revenue Optimization*</p>', unsafe_allow_html=True)
    st.write("---")

    # BAGIAN 1: MISI BAPAK (Lebih Menjual)
    st.write("#### MISI KAMI")
    st.markdown('<div class="mission-box"><span class="mission-text">👉 "Digitizing Trust, Eliminating Leakage: Memberdayakan Pelaku Bisnis Indonesia Melalui Integritas Teknologi AI"</span></div>', unsafe_allow_html=True)

    # BAGIAN 2: PROFIL & FILOSOFI BAPAK (Lebih Menginspirasi)
    st.write("---")
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            # PENTING: File 'erwin.jpg' harus ada di folder yang sama di GitHub
            st.image("erwin.jpg", width=300)
        except:
            st.error("Gagal memuat foto erwin.jpg. Pastikan file ada di GitHub.")
    
    with col2:
        st.markdown('<p class="profil-title">Visi Pemimpin</p>', unsafe_allow_html=True)
        st.markdown(f"""
        <p class="profil-text">
        Halo, saya **Erwin**, Founder dan CEO VGUARD AI Systems. <br>
        Didirikan pada {datetime.now().year}, VGUARD AI lahir dari visi untuk menghapus kebocoran operasional yang seringkali tidak terdeteksi 
        dan menggerogoti keuntungan bisnis di Indonesia. Kami tidak hanya merekam, kami menganalisis dan memberikan intelijen 
        kepada Anda, para pemilik bisnis, agar dapat fokus pada ekspansi tanpa rasa khawatir.
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="profil-title">Filosofi Keamanan</p>', unsafe_allow_html=True)
        st.markdown("""
        <p class="profil-text">
        **VGUARD AI** adalah "Audit Officer" pribadi Anda yang bekerja 24 jam. 
        Filosofi kami adalah menghadirkan teknologi AI masa depan yang mudah digunakan, untuk mengamankan aset Anda dan mencegah 
        kerugian secara sistemik. Kami mentransformasikan data menjadi ketenangan pikiran Anda.
        </p>
        """, unsafe_allow_html=True)

    # BAGIAN 3: KATALOG 4 PAKET LANGGANAN (Mempertahankan 4 Kotak)
    st.write("---")
    st.write("### Pilih Solusi Keamanan Anda:")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.info("### V-START")
        st.write("## **Rp 2,5 Juta**")
        st.write("Maintenance: Rp 1 Jt/Bulan")
        st.write("🔹 Audit Transaksi Retail Harian\n🔹 Notifikasi WA Bot Aktif\n🔹 Laporan Mingguan Dasar")

    with c2:
        st.warning("### V-GROW")
        st.write("## **Rp 5 Juta**")
        st.write("Maintenance: Rp 2,5 Jt/Bulan")
        st.write("🔹 Semua Fitur V-START\n🔹 AI Fraud Detection (Kecurangan)\n🔹 Integrasi Stok Barang Real-Time")

    with c3:
        st.error("### V-PRIME")
        st.write("## **Rp 10 Juta**")
        st.write("Maintenance: Rp 5 Jt/Bulan")
        st.write("🔹 Semua Fitur V-GROW\n🔹 Audit Multi-Cabang\n🔹 Prediksi Kerugian Berbasis AI")

    with c4:
        st.success("### V-CUSTOM")
        st.write("## **Negotiable**")
        st.write("Maintenance: Negotiable")
        st.write("🔹 Solusi Tailor-Made\n🔹 Integrasi ERP (SAP, dll)\n🔹 Dedicated Support 24/7")

    # BAGIAN 4: TOMBOL KONTAK UTAMA (Call to Action)
    st.write("---")
    colA, colB, colC = st.columns([1, 2, 1])
    with colB:
        st.subheader("Siap Mengamankan Bisnis Anda?")
        st.write("Pilih Paket VGUARD AI Systems Sekarang!")
        if st.button("🛡️ Hubungi VGUARD AI Systems Sekarang"):
            st.success("Anda akan diarahkan ke WhatsApp Admin VGUARD AI Systems untuk Konsultasi.")
            # st.markdown("[Klik di Sini untuk Konsultasi](https://wa.me/628123456789)") # Ganti nomor Bapak

elif menu == "Dashboard Performa (Demo)":
    st.title("🛡️ VGUARD AI: Dashboard Performa (Demo)")
    chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['V-START', 'V-GROW'])
    st.line_chart(chart_data)

elif menu == "AI Scanner Audit (Fitur Utama)":
    st.title("🔍 VGUARD AI: Scanner Audit")
    try:
        api_key = st.secrets["MY_API_KEY"]
        st.success("Sistem Terkoneksi: API VGUARD Aktif")
    except KeyError:
        st.error("Sistem Offline: API Key belum dikonfigurasi.")

    input_data = st.text_area("Masukkan Data untuk Diaudit:")
    if st.button("Jalankan Analisis AI"):
        st.info("Sedang menganalisis data melalui VGUARD Engine...")

# --- 5. FOOTER ---
st.write("---")
st.caption("© 2026 VGUARD AI Systems | Intelligence for Your Business Security | Tangerang, Indonesia")
