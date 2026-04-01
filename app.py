import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database & Login State
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "MEDIUM", "Harga": 7500000, "Status": "🟢 AKTIF", "Log": "System Initialized"}
    ]

if 'admin_auth' not in st.session_state:
    st.session_state.admin_auth = False

# Variabel Kontak
WA_NUMBER = "628212190885"

# 2. CSS CUSTOM (Memasukkan teks ke dalam kotak & Desain Sidebar)
st.markdown(f"""
<style>
    .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }}
    
    /* KOTAK PAKET LAYANAN */
    .product-card {{
        background-color: #f8f9fa;
        border: 1px solid #e0e0e0;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        min-height: 400px;
        transition: 0.3s;
        border-top: 8px solid #1E3A8A;
    }}
    .product-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }}
    .package-title {{ font-size: 24px; font-weight: bold; color: #1E3A8A; margin-bottom: 10px; }}
    .price-tag {{ font-size: 20px; font-weight: bold; color: #333; margin-bottom: 15px; }}
    .feature-list {{ text-align: left; font-size: 14px; line-height: 1.6; color: #555; margin-bottom: 20px; }}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (Tampilkan Semua Folder Seperti Awal)
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Capture", 
        "5. 🔐 Admin Control Center", 
        "6. 📜 Laporan Audit Klien"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", f"https://wa.me/{WA_NUMBER}")

# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("""
        Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang telah mengabdikan lebih dari satu dekade karir profesionalnya 
        untuk mendalami seluk-beluk operasional bisnis dan efisiensi organisasi di skala nasional. Dengan keahlian mendalam 
        dalam navigasi industri finansial, beliau memiliki kemampuan analitis yang tajam dalam mengidentifikasi titik-titik rawan 
        kebocoran aset yang seringkali luput dari pengawasan manajemen konvensional.
        
        Sebagai arsitek utama V-Guard AI, Bapak Erwin Sinaga fokus pada misi besar untuk mendemokrasikan fungsi audit internal 
        agar dapat diakses oleh semua skala bisnis, mulai dari UMKM hingga korporasi besar. Berdomisili di Tangerang, beliau aktif 
        menjembatani kesenjangan antara teknologi AI dengan kebutuhan nyata di lapangan, memastikan bahwa setiap rupiah investasi 
        terjaga dengan aman dan memberikan hasil maksimal bagi pertumbuhan ekonomi nasional.
        """)

# --- MENU 2: VISI & ROI ---
elif
