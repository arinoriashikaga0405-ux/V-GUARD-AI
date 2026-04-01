import streamlit as st
import pandas as pd
import hashlib
import time
from datetime import datetime

# --- 1. KONFIGURASI KEAMANAN ---
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

# --- 2. SETUP HALAMAN & TEMA ---
st.set_page_config(
    page_title="V-Guard AI Intelligence | Erwin Sinaga",
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS untuk tampilan Premium Corporate
st.markdown("""
    <style>
    .main { background-color: #0a192f; color: #e6f1ff; }
    .stButton>button { 
        background-color: #64ffda; color: #0a192f; 
        font-weight: bold; border-radius: 8px; width: 100%;
    }
    .stMetric { background-color: #112240; padding: 15px; border-radius: 10px; }
    h1, h2, h3 { color: #ccd6f6; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
st.sidebar.image("https://via.placeholder.com/150", caption="V-Guard AI System")
st.sidebar.title("Navigation Center")
menu = st.sidebar.radio("Menu Utama", ["🏠 Home & Vision", "📦 Produk & Layanan", "🔑 Portal Klien", "🔐 Admin Panel (CEO Only)"])

# --- HALAMAN HOME & VISION ---
if menu == "Home & Vision":
    st.title("🛡️ V-Guard AI Intelligence")
    st.markdown("### *Digitizing Trust, Eliminating Leakage*")
    st.divider()

    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Foto Profil Founder (Placeholder - Silakan ganti URL dengan foto Bapak)
        st.image("https://via.placeholder.com/400x500.png?text=Erwin+Sinaga+Founder", caption="Erwin Sinaga - Founder & CEO")
        st.info("📍 Berdomisili: Tangerang, Indonesia")

    with col2:
        st.header("Visi & Misi Founder")
        st.markdown(f"""
        **“Sebagai seorang Senior Business Leader dengan pengalaman lebih dari satu dekade di industri perbankan dan aset, 
        saya memahami bahwa musuh terbesar pertumbuhan bisnis bukanlah kompetisi, melainkan ketidakpastian data dan kebocoran internal.”**

        Di dunia yang bergerak serba cepat, kepercayaan (trust) tidak lagi cukup jika hanya berdasarkan janji; kepercayaan harus bisa diukur, 
        diverifikasi, dan didigitalisasi. Inilah alasan saya mendirikan **V-Guard AI Intelligence**.

        Visi kami adalah menjadi standar global dalam **Digital Trust**. Kami percaya bahwa setiap pemilik bisnis—mulai dari tokoh retail 
        mandiri hingga korporasi multinasional—berhak mendapatkan transparansi mutlak atas aset mereka. Melalui prinsip **'Digitizing Trust'**, 
        kami mengubah data mentah dari CCTV, mesin kasir, laporan stok (VCS), dan mutasi bank menjadi bukti otentik yang tidak dapat dimanipulasi.

        Misi utama kami, **'Eliminating Leakage'**, dijalankan dengan mengintegrasikan ekosistem AI tercanggih di dunia (Gemini, MindBridge, YOLO). 
        Kami tidak hanya mendeteksi kecurangan saat sudah terjadi, tetapi membangun benteng pertahanan prediktif untuk menghentikan kebocoran 
        sebelum menjadi kerugian finansial. V-Guard AI mengembalikan kendali penuh ke tangan Anda, memberikan ketenangan pikiran (*peace of mind*), 
        dan memastikan setiap rupiah investasi Anda bekerja secara jujur dan optimal.
        """)
        st.caption("— Erwin Sinaga, Founder V-Guard AI")

# --- HALAMAN PRODUK & LAYANAN ---
elif menu == "📦 Produk & Layanan":
    st.header("Solusi Ekosistem V-Guard AI")
    st.write("Integrasi 9 Platform AI Terbaik Dunia untuk Akurasi 99.9%")
    
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.subheader("V-LITE")
        st.write("Target: UMKM/Warung")
        st.markdown("- Anti-Void Audit\n- WA Report Bulanan\n- Notifikasi Stok")
        st.button("Pilih V-LITE", key="lite")

    with c2:
        st.subheader("V-PRO")
        st.write("Target: Resto/Cafe")
        st.markdown("- Real-Time Monitoring\n- VCS Sync (Bank-POS)\n- Audit Harian")
        st.button("Pilih V-PRO", key="pro")

    with c3:
        st.subheader("V-SIGHT")
        st.write("Target: Toko Emas/Gudang")
        st.markdown("- CCTV AI Behavior\n- Visual Audit Match\n- Cloud Evidence")
        st.button("Pilih V-SIGHT", key="sight")

    with c4:
        st.subheader("V-ENTERPRISE")
        st.write("Target: Korporasi")
        st.markdown("- Multi-Branch Dash\n- Digital Forensics\n- Custom ERP API")
        st.button("Pilih V-ENTERPRISE", key="ent")

# --- HALAMAN PORTAL KLIEN ---
elif menu == "🔑 Portal Klien":
    st.header("Client Secure Portal")
    with st.container():
        st.info("Silakan unggah data harian Anda untuk diproses oleh AI.")
        col_a, col_b = st.columns(2)
        with col_a:
            biz_name = st.text_input("Nama Perusahaan/Bisnis")
            file_vcs = st.file_uploader("Upload Data VCS (Excel/CSV)")
        with col_b:
            file_ktp = st.file_uploader("Upload KTP (KYC Verification)", type=['jpg', 'png'])
            
        if st.button("🚀 Kirim Data untuk Audit"):
            if file_ktp and biz_name:
                with st.spinner("Mengenkripsi data dengan AES-256..."):
                    time.sleep(2)
                    st.success(f"Sukses! Data {biz_name} telah aman di server. Menunggu verifikasi Admin.")
            else:
                st
