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
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.image("https://www.w3schools.com/howto/img_avatar.png", use_container_width=True)
    
    st.title("🛡️ V-Guard AI")
    st.markdown('<p class="status-connected">● System Online / Connected</p>', unsafe_allow_html=True)
    
    menu = st.radio("Folder Navigasi:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 📦 Paket Layanan", "4. 📝 Registrasi Klien", "5. 🔐 Admin Dashboard"])
    st.write("---")
    st.link_button("📞 Hubungi Erwin Sinaga", "https://wa.me/628212190885")

# --- FOLDER 1: PROFIL FOUNDER (JUDUL TEKS DIHAPUS) ---
if menu == "1. 👤 Profil Founder":
    # Judul dihapus sesuai permintaan Bapak
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
        else:
            st.markdown("### [Foto Erwin Sinaga]")
    with col2:
        st.markdown("""<div class="profile-box">
        Bapak Erwin Sinaga merupakan seorang profesional dan Pemimpin Bisnis Senior yang telah mendedikasikan lebih dari sepuluh tahun kariernya dalam industri perbankan serta manajemen aset nasional. Melalui perjalanan panjang di sektor keuangan formal, beliau telah membangun keahlian mendalam dalam manajemen risiko strategis, kepatuhan operasional (compliance), hingga pengawasan aset korporasi yang sangat kompleks. Pengalaman ini membentuk pemahaman beliau bahwa celah kecurangan atau fraud sering kali muncul dari kelemahan sistem pengawasan manual yang tidak mampu bekerja secara real-time. <br><br>
        V-Guard AI didirikan berdasarkan visi besar Bapak Erwin Sinaga untuk membawa standar keamanan audit perbankan yang sangat ketat ke dalam ekosistem bisnis UMKM dan perusahaan menengah di Indonesia. Beliau sangat meyakini bahwa pemanfaatan teknologi Artificial Intelligence adalah solusi mutlak untuk menutup celah kebocoran finansial dan memastikan transparansi aset bagi para pemilik bisnis. Melalui V-Guard AI, beliau berkomitmen untuk menyediakan benteng pertahanan digital cerdas yang mampu melakukan deteksi dini terhadap setiap anomali transaksi.
        </div>""", unsafe_allow_html=True)

# --- FOLDER 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Analisis ROI")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=500000000, step=10000000)
    st.success(f"🛡️ Target Penyelamatan Aset: Rp {omzet * 0.045:,.0f}")

# --- FOLDER 3: PAKET LAYANAN ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Layanan V-Guard AI")
    p_cols = st.columns(4)
    pkgs = [
        {"n": "BASIC", "c": "#f8f9fa", "f": ["Audit Harian", "Laporan Mingguan"]},
        {"n": "MEDIUM", "c": "#e3f2fd", "f": ["Semua Fitur BASIC", "AI CCTV Integration"]},
        {"n": "ENTERPRISE", "c": "#e8f5e9", "f": ["Semua Fitur MEDIUM", "Multi-Branch Dashboard"]},
        {"n": "CORPORATE", "c": "#fff3e0", "f": ["Semua Fitur ENTERPRISE", "Custom AI Model"]}
    ]
    for i, p in enumerate(pkgs):
        with p_cols[i]:
            st.markdown(f'<div class="package-card" style="background-color: {p["c"]};"><h3>{p["n"]}</h3><hr><ul>{"".join([f"<li>{item}</li>" for item in p["f"]])}</ul></div>', unsafe_allow_html=True)
            st.link_button(f"Pilih Paket {p['n']}", f"https://wa.me/628212190885?text=Saya%20pilih%20{p['n']}")

# --- FOLDER 4: REGISTRASI ---
elif menu == "4. 📝 Registrasi Klien":
    st.header("📝 Registrasi Nasabah Baru")
    with st.form("reg"):
        n = st.text_input("Nama Bisnis:")
        p = st.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        if st.form_submit_button("Kirim Data Pendaftaran"):
            st.session_state.db_nasabah.append({"Waktu": datetime.now().strftime("%Y-%m-%d"), "Nama": n, "Bidang": "-", "Paket": p, "Harga": "-", "Status": "🔴 Menunggu Aktivasi"})
            st.success("Terkirim!")

# --- FOLDER 5: ADMIN DASHBOARD ---
elif menu == "5. 🔐 Admin Dashboard":
    st.header("🔐 Admin Intelligence")
    pw = st.text_input("Password:", type="password")
    if pw == "w1nbju8282":
        t1, t2 = st.tabs(["📊 Database & Aktivasi", "📝 Hasil Audit"])
        with t1:
            if st.session_state.db_nasabah:
                st.table(pd.DataFrame(st.session_state.db_nasabah))
                pilih = st.selectbox("Pilih Nasabah untuk Diaktifkan:", range(len(st.session_state.db_nasabah)), 
                                     format_func=lambda x: st.session_state.db_nasabah[x]['Nama'])
                if st.button("🟢 AKTIFKAN SEKARANG"):
                    st.session_state.db_nasabah[pilih]['Status'] = "🟢 AKTIF"
                    st.rerun()

# 4. FOOTER
st.markdown('<div class="footer">© 2026 V-Guard AI Systems</div>', unsafe_allow_html=True)
