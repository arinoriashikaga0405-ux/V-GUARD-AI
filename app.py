import streamlit as st
import os
import pandas as pd

# --- 1. KONFIGURASI HALAMAN & TEMA ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Premium Eksekutif (Berdasarkan Struktur Dokumen) [cite: 306-313]
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; height: 45px; }
    .stTextInput>div>div>input { background-color: #1e293b; color: white; }
    div[data-testid="stMetricValue"] { font-size: 22px; color: #238636; }
    .mission-box { 
        text-align: justify; line-height: 1.7; font-size: 16px; color: #d1d5db;
        background-color: #1e293b; padding: 25px; border-radius: 15px; border-left: 10px solid #238636;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR NAVIGATION [cite: 314-321] ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.markdown("<div style='text-align:center;'><p style='color:white; font-weight:bold; margin-bottom:0;'>Erwin Sinaga</p><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    menu = st.radio("NAVIGASI UTAMA", [
        "Visi & Misi", 
        "Produk & Layanan", 
        "Analisis ROI Kerugian", 
        "Portal Klien", 
        "Admin Control Center"
    ])
    
    st.markdown("---")
    # Penambahan Fitur Efisiensi 20% yang diminta
    st.success("📉 Efisiensi Server & API: 20%") 
    st.error("🚨 FIRE ALARM: ACTIVE")

# --- 3. LOGIKA MENU UTAMA ---

# A. VISI & MISI [cite: 323-342]
if menu == "Visi & Misi":
    st.header("Visi & Misi V-Guard AI Intelligence")
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga - Founder & CEO", use_container_width=True)
    with col_txt:
        st.markdown(f"""
        <div class="mission-box">
        <b>V-Guard AI Intelligence</b> lahir dari urgensi integritas finansial. Sebagai entitas yang dipimpin oleh profesional dengan pengalaman 10 tahun di perbankan, kami memahami bahwa celah sistem adalah potensi kerugian fatal.<br><br>
        Misi kami adalah mendigitalisasi kepercayaan (Digital Trust) melalui audit cerdas otonom 24 jam. Dengan optimasi <b>Efisiensi API & Server sebesar 20%</b>, kami memastikan perlindungan aset yang maksimal dengan biaya infrastruktur yang lebih ringan bagi klien.<br><br>
        Visi kami adalah menjadi standar global dalam "Integrity Assurance", menjaga warisan bisnis Anda tetap utuh melalui inovasi teknologi yang melampaui standar audit konvensional.
        </div>
        """, unsafe_allow_html=True)

# B. PRODUK & LAYANAN [cite: 343-382]
elif menu == "Produk & Layanan":
    st.header("🛡️ Portfolio Layanan V-Guard AI")
    wa_number = "6282122190885"
    c1, c2, c3, c4 = st.columns(4)
    
    packages = {
        "V-LITE": ["Mikro", "1.5 Jt", "750 rb", "AI Fraud Detector Dasar, Laporan WA"],
        "V-PRO": ["Retail", "3 Jt", "1.5 Jt", "VCS Integration, Audit Bank, H-7 Invoice"],
        "V-SIGHT": ["Gudang", "7.5 Jt", "3.5 Jt", "CCTV AI Behavior, Real-Time Stock, Alarm"],
        "V-ENTERPRISE": ["Korporasi", "15 Jt", "10 Jt", "The Core Brain, Forensic AI, Dedicated Server"]
    }
    
    for i, (name, details) in enumerate(packages.items()):
        with [c1, c2, c3, c4][i]:
            with st.container(border=True):
                st.markdown(f"### 📦 {name}")
                st.caption(f"🎯 Target: {details[0]}")
                st.write(f"- {details[3]}")
                st.info(f"**Pasang:** {details[1]}\n\n**Bulan:** {details[2]}")
                st.link_button(f"Pilih {name}", f"https://wa.me/{wa_number}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20dengan%20paket%20*{name}*")

# C. ANALISIS ROI [cite: 398-415]
elif menu == "Analisis ROI Kerugian":
    st.header("📊 Analisis Potensi Kerugian vs ROI")
    col_a, col_b = st.columns(2)
    with col_a:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
        leak = st.slider("Estimasi Kebocoran (%)", 1, 20, 5)
        loss = omzet * (leak / 100)
        st.error(f"Potensi Kerugian: Rp {loss:,.0f} / bulan")
    with col_b:
        st.success(f"💰 Profit Diselamatkan: Rp {loss * 0.8:,.0f} / bln")
        st.caption("ROI dihitung berdasarkan pencegahan kebocoran & efisiensi biaya server 20%.")

# D. PORTAL KLIEN [cite: 416-435]
elif menu == "Portal Klien":
    st.header("🔑 Portal Klien V-Guard AI")
    c_reg, c_log = st.columns(2)
    with c_reg:
        st.subheader("📝 Registrasi Klien Baru")
        with st.container(border=True):
            st.text_input("Nama Usaha")
            st.selectbox("Paket Pilihan", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.button("Kirim Registrasi")
    with c_log:
        st.subheader("🔑 Akses User")
        with st.container(border=True):
            st.text_input("Username")
            pw = st.text_input("Password", type="password")
            if st.button("Masuk"):
                if pw == "vguardklien2026": st.success("Selamat Datang!")
                else: st.error("Password Salah.")

# E. ADMIN CONTROL CENTER [cite: 436-588]
elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center")
    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False
    
    if not st.session_state.admin_logged_in:
        admin_input = st.text_input("Administrator Password", type="password")
        if admin_input == "w1nbju8282":
            st.session_state.admin_logged_in = True
            st.rerun()
    else:
        if st.button("Log Out"):
            st.session_state.admin_logged_in = False
            st.rerun()
            
        t1, t2, t3, t4 = st.tabs(["🖥️ Ekosistem AI", "📈 Performa", "👁️ V-SIGHT", "💎 V-ULTRA"])
        
        with t1:
            st.subheader("🌐 Global AI Ecosystem")
            st.write("Google Gemini AI & Vision AI Status: **ONLINE**")
            st.info("Efisiensi Logika Lokal (Edge): **Aktif 20%**")
            
        with t2:
            st.subheader("📈 Monitoring Laba")
            st.metric("Dana Terselamatkan", "Rp 15.700.000", delta="AI Fraud Detector Aktif")
            
        with t3:
            st.subheader("👁️ Visual Command Center")
            st.warning("AI Behavior: Memantau laci kasir & stok gudang secara real-time.")
            
        with t4:
            st.subheader("💎 V-ULTRA Enterprise")
            st.code("Dedicated Server IP: 10.0.88.24\nEncryption: AES-256")
            st.metric("ROI Penyelamatan Aset", "Rp 1.250.000.000 / Thn", delta="Efisiensi 20%")

# FOOTER [cite: 590]
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | © 2026 Powered by Erwin Sinaga</small></center>", unsafe_allow_html=True)
