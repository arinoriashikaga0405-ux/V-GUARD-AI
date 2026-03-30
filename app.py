import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database
if 'db_nasabah' not in st.session_state or len(st.session_state.db_nasabah) == 0:
    st.session_state.db_nasabah = [
        {"Waktu": "2026-03-31", "Nama Personal": "Admin", "Nama Bisnis": "Contoh Corp", "Paket": "BASIC", "Harga": "2.500.000", "Status": "🔴 Menunggu Aktivasi"}
    ]

# 2. CSS CUSTOM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 16px; margin-top: 10px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .package-card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #e0e0e0; height: 580px; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .profile-box { text-align: justify; line-height: 1.8; padding: 25px; background: white; border-radius: 15px; font-size: 16px; border: 1px solid #f0f0f0; }
    .vision-box { background: #fdfdfd; padding: 25px; border-left: 5px solid #007bff; border-radius: 10px; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● System Online / Connected</p>', unsafe_allow_html=True)
    
    menu = st.radio("Folder Navigasi:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 📦 Paket Layanan", "4. 📝 Registrasi Klien", "5. 🔐 Admin Dashboard"])
    st.write("---")
    
    # PERUBAHAN: Tombol Customer Service (Menggantikan Hubungi Erwin Sinaga)
    st.markdown("### Support Center")
    st.link_button("💬 Chat Customer Service", "https://wa.me/628212190885?text=Halo%20Customer%20Service%20V-Guard%20AI,%20saya%20ingin%20bertanya.")

# --- FOLDER 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    col1, col2 = st.columns([1, 2.5])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col2:
        st.markdown(f"""<div class="profile-box">
        <b>Bapak Erwin Sinaga</b> merupakan seorang Pemimpin Bisnis Senior (Senior Business Leader) yang telah mengukir rekam jejak impresif selama lebih dari sepuluh tahun di sektor perbankan dan manajemen aset nasional. Sepanjang kariernya, beliau telah memegang berbagai peran strategis, termasuk posisi krusial sebagai Chief Executive Officer (CEO) dan Chief Sales Officer (CSO), di mana beliau bertanggung jawab penuh atas manajemen risiko, kepatuhan operasional, serta pengawasan aset korporasi berskala besar. Pengalaman mendalam ini memberikan beliau pemahaman unik mengenai titik-titik lemah dalam sistem manajemen konvensional yang sering kali menjadi celah terjadinya kebocoran finansial dan inefisiensi operasional. <br><br>
        V-Guard AI didirikan atas dasar visi besar beliau untuk mendemokratisasi standar keamanan audit kelas perbankan agar dapat diakses oleh ekosistem UMKM dan perusahaan menengah di Indonesia. Beliau sangat meyakini bahwa integritas sebuah bisnis sangat bergantung pada transparansi data yang akurat. Oleh karena itu, melalui implementasi teknologi Artificial Intelligence, beliau berkomitmen untuk membangun sebuah "Benteng Pertahanan Digital" yang mampu bekerja secara otonom selama 24/7. <br><br>
        Kepemimpinan beliau di V-Guard AI tidak hanya berfokus pada inovasi teknologi semata, namun juga pada penciptaan nilai ekonomi (ROI) yang nyata bagi para pemilik bisnis. Dengan dedikasi tinggi, Bapak Erwin Sinaga terus memastikan bahwa setiap solusi yang dihadirkan V-Guard AI mampu menutup celah kecurangan (fraud), meningkatkan disiplin operasional, dan pada akhirnya memberikan ketenangan pikiran (peace of mind) bagi para pengusaha dalam mengelola aset berharga mereka.
        </div>""", unsafe_allow_html=True)

# --- FOLDER 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Strategi & Analisis ROI")
    st.markdown("""<div class="vision-box">
    <h3>Visi</h3>
    <p>Menjadi benteng pertahanan digital terdepan di Indonesia yang mengeliminasi kebocoran aset bisnis melalui kecerdasan buatan.</p>
    <h3>Misi</h3>
    <ul>
