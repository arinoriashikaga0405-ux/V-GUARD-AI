import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 2. CSS BAKU (Mencegah Tampilan Berantakan) ---
st.markdown("""
<style>
    .stApp { background-color: white; }
    .main-header { text-align: center; padding: 20px; }
    .profile-section { background-color: #f1f5f9; padding: 20px; border-radius: 15px; }
    .package-box { 
        border-radius: 10px; padding: 20px; height: 180px; 
        display: flex; flex-direction: column; justify-content: center;
    }
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 3. BERANDA (SESUAI INSTRUKSI BAKU) ---
if st.session_state.page == "Home":
    # Header Logo & Judul (Tengah)
    st.markdown("<div class='main-header'><h1 style='color: #1e3a8a;'>🛡️ VGUARD AI SYSTEMS</h1></div>", unsafe_allow_html=True)
    
    # Kolom Profil
    c1, c2 = st.columns([1, 2.5])
    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=220)
        st.info("Founder & CEO: Erwin Sinaga")
        
    with c2:
        st.markdown("### 👤 Profil & Filosofi: Erwin Sinaga")
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
    ca, cb = st.columns(2)
    with ca: oz = st.number_input("Omzet Bulanan (Rp)", value=250000000)
    with cb: kb = st.slider("Estimasi Kebocoran (%)", 1, 15, 3)
    st.success(f"Potensi Profit Diselamatkan: Rp {(oz * (kb/100) * 0.95):,.0f} / bln")

    st.divider()
    
    # Paket Layanan (4 Kolom Ramping & Bersih)
    st.markdown("#### 🏷️ PAKET LAYANAN STRATEGIS")
    p1, p2, p3, p4 = st.columns(4)
    
    with p1:
        st.markdown("<div class='package-box' style='background-color: #e0f2fe;'><h3 style='color: #0369a1;'>🔹 V-START</h3><p>Rp 5 JT / Bln<br>Scan Harian & Report</p></div>", unsafe_allow_html=True)
    with p2:
        st.markdown("<div class='package-box' style='background-color: #f0fdf4;'><h3 style='color: #15803d;'>🔶 V-GROW</h3><p>Rp 15 JT / Bln<br>Real-time AI & WA</p></div>", unsafe_allow_html=True)
    with p3:
        st.markdown("<div class='package-box' style='background-color: #fff7ed;'><h3 style='color: #c2410c;'>💎 V-PRIME</h3><p>Rp 50 JT / Bln<br>Full AI & Support</p></div>", unsafe_allow_html=True)
    with p4:
        st.markdown("<div class='package-box' style='background-color: #fef2f2;'><h3 style='color: #b91c1c;'>🏢 ENTERPRISE</h3><p>Custom Price<br>Private AI Model</p></div>", unsafe_allow_html=True)

# --- 4. ADMIN (5 TAB LENGKAP) ---
elif st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.title("🔐 Login Admin")
        pwd = st.text_input("Password:", type="password")
        if st.button("Masuk"):
            if pwd == "VGUARD2026":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Ditolak")
    else:
        st.header("💻 Command Center - Erwin Sinaga")
        # 5 Tab sesuai instruksi Bapak
        t1, t2, t3, t4, t5 = st.tabs(["🔍 V-Scan", "📊 Monitoring", "📍 Map", "💰 Billing", "⚙️ Klien"])
        with t1: st.write("### 🚀 V-Scan Fraud Detection")
        with t2: st.write("### 📊 Compliance Monitoring")
        with t3: st.map()
        with t4: st.metric("Total Piutang", "Rp 45.000.000")
        with t5: st.write("### ⚙️ Manajemen Klien")
        if st.sidebar.button("🔓 Logout"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()

st.divider()
st.caption(f"© {datetime.now().year} VGUARD AI Systems | CEO Erwin Sinaga")
