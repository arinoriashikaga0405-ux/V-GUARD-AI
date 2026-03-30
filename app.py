import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI UTAMA ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- 2. SIDEBAR ---
with st.sidebar:
    st.markdown("### 👤 CEO: ERWIN SINAGA")
    if st.button("🏠 Beranda Utama"):
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.auth:
        if st.button("🔓 Keluar Admin"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()

# --- 3. LOGIKA HALAMAN ---
if st.session_state.page == "Home":
    # Header sesuai konsep baku Bapak
    st.markdown("<h1 style='text-align: center; color: #1e3a8a;'>🛡️ VGUARD AI SYSTEMS</h1>", unsafe_allow_html=True)
    
    col_foto, col_bio = st.columns([1, 2.5])
    with col_foto:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=200)
        st.info("Founder & CEO: Erwin Sinaga")
        
    with col_bio:
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        **Erwin Sinaga** adalah pemimpin strategis dengan pengalaman lebih dari sepuluh tahun sebagai eksekutif senior di perbankan nasional. 
        VGUARD AI Systems hadir sebagai solusi presisi tinggi untuk mengamankan aset bisnis Anda dari risiko kebocoran data dan kecurangan sistemik.
        """)
        if st.button("🚀 MASUK KE COMMAND CENTER"):
            st.session_state.page = "Admin"
            st.rerun()

    st.divider()
    
    # Kalkulator ROI
    st.markdown("#### 📊 ANALISIS POTENSI KERUGIAN & PROTEKSI PROFIT")
    c1, c2 = st.columns(2)
    with c1:
        oz = st.number_input("Omzet Bulanan (Rp)", value=250000000)
    with c2:
        kb = st.slider("Estimasi Kebocoran (%)", 1, 15, 3)
    
    saved = oz * (kb/100) * 0.95
    st.success(f"Potensi Profit Diselamatkan: Rp {saved:,.0f} / bln")

    st.divider()
    
    # Paket Layanan Ramping
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    p1, p2, p3, p4 = st.columns(4)
    
    p1.info("### 🔹 V-START\n\nRp 5 JT / Bln\n\nScan Harian & Report")
    p2.success("### 🔶 V-GROW\n\nRp 15 JT / Bln\n\nReal-time AI & WA")
    p3.warning("### 💎 V-PRIME\n\nRp 50 JT / Bln\n\nFull AI & Support")
    p4.error("### 🏢 ENTERPRISE\n\nCustom Price\n\nPrivate AI Model")

elif st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.title("🔐 Login Command Center")
        pwd = st.text_input("Password Admin:", type="password")
        if st.button("Verifikasi"):
            if pwd == "VGUARD2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Akses Ditolak!")
    else:
        st.header("💻 Command Center - Erwin Sinaga")
        
        # Perbaikan agar tidak error unterminated string
        menu_tabs = ["🔍 V-Scan", "📊 Monitoring", "📍 Map", "💰 Billing", "⚙️ Klien"]
        t1, t2, t3, t4, t5 = st.tabs(menu_tabs)
        
        with t1:
            st.write("### 🚀 V-SCAN FRAUD")
            st.file_uploader("Unggah Laporan")
        with t2:
            st.write("### 📅 MONITORING")
            st.table(pd.DataFrame({"Klien": ["Toko Maju"], "Status": ["Aktif"]}))
        with t3:
            st.write("### 📍 GEOLOKASI")
            st.map()
        with t4:
            st.write("### 💰 BILLING")
            st.metric("Piutang Berjalan", "Rp 45.000.000")
        with t5:
            st.write("### ⚙️ MANAJEMEN KLIEN")
            st.text_input("Nama Bisnis")

st.divider()
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
