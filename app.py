import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database dengan Data Contoh
if 'db_nasabah' not in st.session_state or len(st.session_state.db_nasabah) == 0:
    st.session_state.db_nasabah = [
        {"Waktu": "2026-03-31", "Nama": "Nasabah Contoh", "Bidang": "Retail", "Paket": "BASIC", "Harga": "2.5jt", "Status": "🔴 Menunggu Aktivasi"}
    ]

# 2. CSS CUSTOM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 16px; margin-top: 10px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .package-card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #e0e0e0; height: 580px; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .profile-box { text-align: justify; line-height: 1.8; padding: 20px; background: white; border-radius: 15px; font-size: 16px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    # Memanggil Foto Utama Founder (erwin.jpg)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.image("https://www.w3schools.com/howto/img_avatar.png", use_container_width=True)
    
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● System Online / Connected</p>', unsafe_allow_html=True)
    
    menu = st.radio("Folder Navigasi:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 📦 Paket Layanan", "4. 📝 Registrasi Klien", "5. 🔐 Admin Dashboard"])
    st.write("---")
    st.link_button("📞 Hubungi Erwin Sinaga", "https://wa.me/628212190885")

# --- FOLDER 1: PROFIL FOUNDER (MEMANGGIL IKON RESMI) ---
if menu == "1. 👤 Profil Founder":
    # Memanggil Ikon Resmi Berlatar Biru (erwin_icon.png) di bagian atas
    if os.path.exists("erwin_icon.png"):
        st.image("erwin_icon.png", width=60, caption="") # Menampilkan ikon dengan ukuran kecil
    else:
        st.warning("Mohon unggah file 'erwin_icon.png' (ikon resmi) ke folder project GitHub Bapak.")
    
    col1, col2 = st.columns([1, 2.5])
    with col1:
        # Menampilkan Foto Besar Founder di samping narasi
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
        else:
            st.info("Foto Founder (erwin.jpg)")
            
    with col2:
        st.markdown(f"""<div class="profile-box">
        <b>Bapak Erwin Sinaga</b> merupakan seorang profesional dan Pemimpin Bisnis Senior yang telah mendedikasikan lebih dari sepuluh tahun kariernya dalam industri perbankan serta manajemen aset nasional. Melalui perjalanan panjang di sektor keuangan formal, beliau telah membangun keahlian mendalam dalam manajemen risiko strategis, kepatuhan operasional (compliance), hingga pengawasan aset korporasi yang sangat kompleks. Pengalaman ini membentuk pemahaman beliau bahwa celah kecurangan atau fraud sering kali muncul dari kelemahan sistem pengawasan manual yang tidak mampu bekerja secara real-time. <br><br>
        V-Guard AI didirikan berdasarkan visi besar Bapak Erwin Sinaga untuk membawa standar keamanan audit perbankan yang sangat ketat ke dalam ekosistem bisnis UMKM dan perusahaan menengah di Indonesia. Beliau sangat meyakini bahwa pemanfaatan teknologi Artificial Intelligence adalah solusi mutlak untuk menutup celah kebocoran finansial dan memastikan transparansi aset bagi para pemilik bisnis. Melalui V-Guard AI, beliau berkomitmen untuk menyediakan benteng pertahanan digital cerdas yang mampu melakukan deteksi dini terhadap setiap anomali transaksi.
        </div>""", unsafe_allow_html=True)

# --- FOLDER LAIN TETAP SAMA (DIPOTONG AGAR RINGKAS) ---
# ... (Blok elif menu untuk ROI, Paket, Registrasi, Admin) ...

# 4. FOOTER
st.markdown('<div class="footer">© 2026 V-Guard AI Systems</div>', unsafe_allow_html=True)
