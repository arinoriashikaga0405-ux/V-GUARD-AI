import streamlit as st
import pandas as pd
from datetime import datetime
import os
import google.generativeai as genai

# --- 1. KEAMANAN & KONFIGURASI AI ---
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.warning("⚠️ API Key belum dikonfigurasi di Secrets.")

# --- 2. KONEKSI GOOGLE SHEETS (DIBUNGKUS AGAR TIDAK ERROR) ---
try:
    from st_gsheets_connection import GSheetsConnection
    conn = st.connection("gsheets", type=GSheetsConnection)
    koneksi_aktif = True
except Exception:
    koneksi_aktif = False

# --- 3. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# (Gunakan sisa kode menu Bapak seperti biasa di bawah ini)

st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; height: 45px; }
    .stTextInput>div>div>input { background-color: #1e293b; color: white; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA V-GUARD ---
def proses_transaksi(total, data_input):
    if total < 5000000:
        return "PASS (Auto)", False
    try:
        response = model_vguard.generate_content(f"Cek: {data_input}")
        return response.text, True
    except:
        return "ERROR: Cek API Key", False

# --- 4. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.markdown("<div style='text-align:center;'><p style='color:white; font-weight:bold; margin-bottom:0;'>Erwin Sinaga</p><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Produk & Layanan", "ROI Kerugian Klien", "Portal Klien", "Admin Control Center"])

# --- 5. LOGIKA MENU ---

if menu == "Visi & Misi":
    st.header("Visi & Misi: Digitizing Trust, Eliminating Leakage")
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga - Founder & CEO", use_container_width=True)
        else:
            st.info("Profil Founder V-Guard AI")

    with col_txt:
        st.markdown("""
        <div style="text-align: justify; line-height: 1.7; font-size: 16px; color: #d1d5db;">
        <b>V-Guard AI Intelligence</b> lahir dari urgensi integritas finansial di era transformasi digital. 
        Misi utama kami adalah mendigitalisasi kepercayaan (Digital Trust) melalui pembuktian matematis 
        dan audit cerdas yang bekerja secara otonom 24 jam nonstop tanpa kompromi.<br><br>
        Kami percaya bahwa kejujuran sistem tidak boleh hanya bergantung pada pengawasan manusia, 
        melainkan harus dibangun di atas fondasi teknologi AI yang presisi. Melalui ekosistem V-Guard, 
        kami mengintegrasikan analisis data perbankan (VCS), visi komputer, dan deteksi anomali prediktif.
        </div>
        """, unsafe_allow_html=True)

elif menu == "Produk & Layanan":
    st.header("🛡️ Portfolio Layanan V-Guard AI Intelligence")
    wa_number = "6282122190885"
    packages = {
        "V-LITE": ["Mikro / 1 Kasir", "750 rb", "350 rb", "AI Fraud Detector Dasar, Daily WA/Email Summary"],
        "V-PRO": ["Retail & Kafe", "1.5 Jt", "850 rb", "VCS Integration, Bank Statement Audit, Input Excel/CSV/PDF"],
        "V-SIGHT": ["Gudang & Toko", "7.5 Jt", "3.5 Jt", "CCTV AI Behavior, Visual Cashier Audit, Real-Time Stock"],
        "V-ENTERPRISE": ["Korporasi", "15 Jt", "10 Jt", "The Core Brain, Forensic AI, Custom AI SOP"]
    }
    cols = st.columns(4)
    for i, (name, details) in enumerate(packages.items()):
        with cols[i]:
            with st.container(border=True):
                st.markdown(f"### 📦 {name}")
                st.caption(details[0])
                st.write(details[3])
                st.info(f"**Setup:** {details[1]}\n\n**Bulanan:** {details[2]}")
                st.link_button(f"Pilih {name}", f"https://wa.me/{wa_number}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20{name}")

elif menu == "ROI Kerugian Klien":
    st.header("📊 Analisis Potensi Kerugian vs ROI")
    col_a, col_b = st.columns(2)
    with col_a:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
        leak = st.slider("Estimasi Kebocoran (%)", 1, 20, 5)
        loss = omzet * (leak / 100)
        st.error(f"Potensi Kerugian: Rp {loss:,.0f} / bulan")
    with col_b:
        st.success(f"ROI Penyelamatan dengan V-Guard: Rp {loss * 0.8:,.0f} / bulan")

elif menu == "Portal Klien":
    st.header("🌐 Portal Klien V-Guard AI")
    c_reg, c_log = st.columns(2)
    with c_reg:
        st.subheader("📝 Form Order Baru")
        with st.container(border=True):
            st.text_input("Nama Pelanggan")
            st.text_input("Nama Usaha")
            st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.button("Kirim Registrasi")
    with c_log:
        st.subheader("🔑 Akses User Aktif")
        with st.container(border=True):
            st.text_input("Username", key="client_user")
            pw = st.text_input("Password", type="password", key="client_pw")
            if st.button("Masuk"):
                if pw == "vguardklien2026": st.success("Selamat Datang!")
                else: st.error("Password Salah.")

elif menu == "Admin Control Center":
    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False

    if not st.session_state.admin_logged_in:
        admin_input = st.text_input("Administrator Password", type="password")
        if admin_input == "w1nbju8282":
            st.session_state.admin_logged_in = True
            st.rerun()
    else:
        col_header, col_logout = st.columns([5, 1])
        with col_header: st.success("Akses Eksekutif Aktif")
        with col_logout:
            if st.button("Log Out"):
                st.session_state.admin_logged_in = False
                st.rerun()

        st.markdown("### 📊 Ringkasan Eksekutif & AI Squad")
        c_api1, c_api2, c_api3 = st.columns(3)
        c_api1.metric("Anggaran API", "Rp 10.000.000")
        c_api2.metric("Biaya Terpakai", "Rp 1.200.000", delta="-15% (Hemat)")
        c_api3.metric("Efisiensi Sistem", "88%")
        
        st.progress(0.12, text="Kuota API Cloud: 12%")
        
        st.subheader("🤖 V-Guard AI Squad Agents")
        sq = st.columns(4)
        agents = [("🕵️ Sentinel", "Memantau Fraud"), ("💰 Auditor", "VCS Sync"), ("📦 Stocker", "Visual Check"), ("📄 Invoicer", "H-7 Ready")]
        for i, (name, status) in enumerate(agents):
            with sq[i]:
                with st.container(border=True):
                    st.markdown(f"**{name}**")
                    st.caption(status)

        t1, t2, t3 = st.tabs(["👤 Aktivasi Klien", "🖥️ Ekosistem AI", "💎 V-ULTRA"])
        with t1:
            st.text_input("Username Klien Baru")
            st.selectbox("Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.button("Aktifkan Akun")
        with t2:
            st.write("Sistem terhubung ke Google Gemini 1.5 Flash & YOLO Vision Engine.")
        with t3:
            st.metric("ROI Penyelamatan Aset", "Rp 1.250.000.000 / Tahun")

st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026</small></center>", unsafe_allow_html=True)
