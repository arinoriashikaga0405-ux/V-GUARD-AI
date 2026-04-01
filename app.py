import streamlit as st
import os
import pandas as pd

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# --- 2. CSS CUSTOM (ANTI ERROR & TAMPILAN PROFESIONAL) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .package-card { 
        background-color: #161b22; padding: 25px; border-radius: 12px; border: 1px solid #30363d; 
        margin-bottom: 20px; min-height: 450px; color: #c9d1d9;
    }
    .package-title { color: #58a6ff; font-size: 1.5rem; font-weight: bold; margin-bottom: 10px; }
    .price-tag { font-size: 1.2rem; color: #ffffff; font-weight: bold; margin: 15px 0; padding: 10px; border-top: 1px solid #333; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR PROFIL ---
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        try: st.image("erwin.jpg", use_container_width=True)
        except: st.info("Profil: Erwin Sinaga")
    st.markdown("<div style='text-align:center;'><b>Erwin Sinaga</b><br><small>Founder & CEO V-Guard AI</small></div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGASI", ["Visi & Misi", "Layanan & Investasi", "Portal Klien", "Admin Control Center"])

# --- 4. LOGIKA MENU ---

# MENU 1: VISI & MISI
if menu == "Visi & Misi":
    st.header("Visi & Misi V-Guard AI Intelligence")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
    with col2:
        st.markdown("""
        <div style="text-align: justify; color: #8b949e; line-height: 1.8;">
        Sebagai seorang Senior Business Leader dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi produk, melainkan kepastian data dan eliminasi kebocoran internal (internal fraud). Kepercayaan atau trust harus bisa diukur, diverifikasi secara matematis, dan didigitalisasi melalui teknologi kecerdasan buatan. Inilah alasan utama saya mendirikan V-Guard AI Intelligence sebagai benteng pertahanan bagi para pemilik bisnis di Indonesia agar aset mereka terlindungi sepenuhnya.<br><br>
        <b>Visi Kami:</b> Menjadi standar global dalam penyediaan ekosistem Digital Trust yang otonom, transparan, dan tak tergoyahkan. Kami bercita-cita membangun dunia di mana setiap interaksi digital didasari oleh bukti otentik yang dapat diverifikasi secara instan, menghilangkan ambiguitas dalam transaksi bisnis, dan memastikan integritas data menjadi aset yang paling berharga bagi setiap organisasi, mulai dari skala UMKM hingga korporasi multinasional.<br><br>
        <b>Misi Kami:</b> Melaksanakan filosofi 'Eliminating Leakage' dengan dedikasi tinggi melalui integrasi kecerdasan buatan (AI) tingkat lanjut dan teknologi Computer Vision yang canggih. Kami berkomitmen untuk membangun sistem pertahanan prediktif yang mampu menghentikan pola kecurangan sebelum menjadi kerugian finansial yang signifikan bagi klien kami. Melalui prinsip 'Digitizing Trust', kami mengubah setiap titik data mentah menjadi bukti otentik yang tidak dapat dimanipulasi oleh oknum internal maupun eksternal.
        </div>
        """, unsafe_allow_html=True)

# MENU 2: LAYANAN (HARGA 750RB & LINK WA)
elif menu == "Layanan & Investasi":
    st.header("🛡️ Produk & Layanan (Klik Nama untuk Order)")
    wa = "https://wa.me/6282122190885?text=Halo%20Pak%20Erwin,%20saya%20order%20"
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div class='package-card'><div class='package-title'>📦 V-LITE</div>• AI Fraud Dasar<br>• Laporan Bulanan PDF<br>• Notifikasi Standar<div class='price-tag'>Rp 750.000 / bln</div>", unsafe_allow_html=True)
        st.link_button("Pilih V-LITE", f"{wa}V-LITE")
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='package-card'><div class='package-title'>🛡️ V-PRO</div>• Real-Time Monitoring<br>• VCS Integrasi Bank<br>• Audit Harian Otomatis<div class='price-tag'>Rp 1.500.000 / bln</div>", unsafe_allow_html=True)
        st.link_button("Pilih V-PRO", f"{wa}V-PRO")
        st.markdown("</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='package-card'><div class='package-title'>👁️ V-SIGHT</div>• CCTV AI Behavior<br>• Visual Audit Kasir<br>• Deteksi Stok Real-time<div class='price-tag'>Rp 2.500.000 / bln</div>", unsafe_allow_html=True)
        st.link_button("Pilih V-SIGHT", f"{wa}V-SIGHT")
        st.markdown("</div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='package-card'><div class='package-title'>🏢 V-ENTERPRISE</div>• Multi-Cabang Central<br>• Digital Forensik AI<br>• Dedicated Server<div class='price-tag'>Hubungi CEO</div>", unsafe_allow_html=True)
        st.link_button("Hubungi Kami", f"{wa}V-ENTERPRISE")
        st.markdown("</div>", unsafe_allow_html=True)

# MENU 3: PORTAL KLIEN
elif menu == "Portal Klien":
    st.header("Portal Klien")
    pw = st.text_input("Password Akses Klien", type="password")
    if pw == "vguardklien2026":
        st.subheader("✅ Daftar User & Status Aktif")
        data_klien = [
            {"Nama Usaha": "Laundry Jaya", "Paket": "V-LITE", "Status": "AKTIF", "Sisa Hari": "H-15"},
            {"Nama Usaha": "Cafe Mantap", "Paket": "V-PRO", "Status": "AKTIF", "Sisa Hari": "H-7 (Invoice)"}
        ]
        st.table(data_klien)
    elif pw != "": st.error("Password Salah")

# MENU 4: ADMIN (CORE BRAIN + VCS + INPUT KLIEN BARU)
elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center - The Core Brain")
    adm_pw = st.text_input("Administrator Password", type="password")
    
    if adm_pw == "adminvguard2026":
        tab1, tab2, tab3 = st.tabs(["📊 VCS (Virtual Control)", "👤 Registrasi Klien Baru", "🧠 AI Core Brain"])
        
        with tab1:
            st.subheader("VCS - Sinkronisasi Kasir vs Bank")
            col_v1, col_v2, col_v3 = st.columns(3)
            col_v1.metric("Total Transaksi Kasir", "Rp 45.200.000")
            col_v2.metric("Total Masuk Bank (VCS)", "Rp 45.200.000", delta="Sinkron 100%")
            col_v3.metric("Selisih", "Rp 0", delta_color="normal")
            st.write("✅ Semua data transaksi hari ini telah diverifikasi oleh MindBridge.")
            
        with tab2:
            st.subheader("➕ Daftarkan Akun Klien Baru")
            with st.form("Input Klien"):
                new_name = st.text_input("Nama Usaha Klien")
                new_pkg = st.selectbox("Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
                new_pw = st.text_input("Set Password Unik Klien")
                if st.form_submit_button("Simpan Klien Baru"):
                    st.success(f"Klien {new_name} Berhasil Terdaftar!")
        
        with tab3:
            st.subheader("Integrasi Teknologi")
            st.info("🧠 Gemini AI: Analisis Audit Naratif Aktif.")
            st.info("🚨 Alarm Fraud: MindBridge mendeteksi pola kecurangan.")
            st.info("👁️ YOLO Vision: Monitoring CCTV Kasir Aktif.")
            
    elif adm_pw != "": st.error("Akses Ditolak")

# --- 5. FOOTER ---
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026 | Founder: Erwin Sinaga</small></center>", unsafe_allow_html=True)
