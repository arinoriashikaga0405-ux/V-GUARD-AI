import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. SETTING DASAR ---
st.set_page_config(page_title="VGUARD AI Systems - CEO Erwin Sinaga", page_icon="🛡️", layout="wide")

# Inisialisasi status halaman
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("### 👤 CEO: ERWIN SINAGA")
    st.write("---")
    if st.button("🏠 Halaman Beranda"):
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.auth:
        if st.button("🔓 Keluar Admin"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()

# --- 3. HALAMAN BERANDA (HOME) ---
if st.session_state.page == "Home":
    # Header Baku: Logo & Judul
    st.markdown("<h1 style='text-align: center; color: #1e3a8a;'>🛡️ VGUARD AI SYSTEMS</h1>", unsafe_allow_html=True)
    
    # Section Profil & Bio
    col_foto, col_bio = st.columns([1, 2.5])
    
    with col_foto:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=220)
        st.info("Founder & CEO: Erwin Sinaga")
        
    with col_bio:
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        **Erwin Sinaga** adalah pemimpin strategis dengan rekam jejak profesional lebih dari sepuluh tahun di perbankan nasional. 
        **VGUARD AI Systems** hadir sebagai perisai pertahanan bisnis Anda untuk menjaga aset dengan presisi tinggi melalui integrasi teknologi AI terbaru.
        
        Bapak Erwin meyakini bahwa setiap rupiah dalam omzet bisnis klien adalah amanah besar yang harus dijaga dengan teknologi kecerdasan buatan paling mutakhir. Keamanan aset klien adalah prioritas utama yang tidak dapat ditawar.
        """)
        if st.button("🚀 MASUK KE COMMAND CENTER"):
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    
    # Kalkulator ROI
    st.markdown("#### 📊 ANALISIS POTENSI KERUGIAN & PROTEKSI PROFIT")
    ca, cb = st.columns(2)
    with ca:
        omzet = st.number_input("Omzet Bulanan Bisnis (Rp)", value=250000000)
    with cb:
        kebocoran = st.slider("Estimasi Kebocoran/Fraud (%)", 1, 15, 3)
    
    saved = omzet * (kebocoran/100) * 0.95
    st.success(f"**Potensi Profit Diselamatkan: Rp {saved:,.0f} / bln**")
    st.caption("*Berdasarkan Efisiensi V-GUARD 95%")

    st.write("---")
    
    # Paket Layanan Strategis (4 Kolom Ramping)
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    p1, p2, p3, p4 = st.columns(4)
    
    wa_link = "https://wa.me/62821221190885?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20"
    
    with p1:
        st.info("### 🔹 V-START\n\n**Rp 5 JT / Bln**\n\nScan Harian & Report")
        st.link_button("💬 Pilih V-START", wa_link + "V-START")
    with p2:
        st.success("### 🔶 V-GROW\n\n**Rp 15 JT / Bln**\n\nReal-time AI & WA")
        st.link_button("💬 Pilih V-GROW", wa_link + "V-GROW")
    with p3:
        st.warning("### 💎 V-PRIME\n\n**Rp 50 JT / Bln**\n\nFull AI & Support")
        st.link_button("💬 Pilih V-PRIME", wa_link + "V-PRIME")
    with p4:
        st.error("### 🏢 ENTERPRISE\n\n**Custom Price**\n\nPrivate AI Model")
        st.link_button("💬 Pilih ENTERPRISE", wa_link + "ENTERPRISE")

# --- 4. HALAMAN ADMIN (COMMAND CENTER) ---
elif st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.title("🔐 Executive Access")
        pwd = st.text_input("Password Admin:", type="password")
        if st.button("Verifikasi"):
            if pwd == "VGUARD2026":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        st.header("💻 Command Center - Erwin Sinaga")
        # 5 Tab Fitur Admin Lengkap
        t1, t2, t3, t4, t5 = st.tabs(["🔍 V-Scan", "📊 Monitoring
