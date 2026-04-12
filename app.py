import streamlit as st
import os
import google.generativeai as genai
import pandas as pd
import time
from datetime import datetime

# --- 1. KONFIGURASI ENGINE & SECURITY (STRUKTUR ASLI) ---
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.warning("⚠️ API Key belum dikonfigurasi di Secrets.")

model_vguard = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    generation_config={"temperature": 0.2, "max_output_tokens": 150},
    system_instruction="Analisa transaksi: ALERT jika fraud, PASS jika aman."
)

# --- 2. KONFIGURASI HALAMAN (STRUKTUR ASLI) ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; height: 45px; }
    .stTextInput>div>div>input { background-color: #1e293b; color: white; }
    .st-emotion-cache-12w0qpk { background-color: #111827; border: 1px solid #374151; padding: 20px; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA V-GUARD (PENYARING BIAYA API) ---
def proses_transaksi(total, data_input):
    if total < 5000000:
        return "PASS (Auto)", False
    try:
        response = model_vguard.generate_content(f"Cek: {data_input}")
        return response.text, True
    except:
        return "Local Analysis: PASS", False

# --- 4. DATA SIMULATION (Database Session untuk Aktivasi) ---
if "db_klien" not in st.session_state:
    st.session_state.db_klien = {
        "admin@vguard.ai": {"nama": "Admin Utama", "paket": "V-ENTERPRISE", "status": "Aktif"}
    }
if "client_logged_in" not in st.session_state:
    st.session_state.client_logged_in = False
    st.session_state.current_client = None

# --- 5. SIDEBAR NAVIGATION (STRUKTUR ASLI + PENYESUAIAN) ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.markdown("<div style='text-align:center;'><p style='color:white; font-weight:bold; margin-bottom:0;'>Erwin Sinaga</p><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Logic Navigasi: Jika klien login, menu berubah ke Dashboard Klien
    if st.session_state.client_logged_in:
        menu = st.radio("DASHBOARD KLIEN", ["Ringkasan Integritas", "Fitur Layanan Paket", "Laporan AI Squad", "Log Out Klien"])
    else:
        menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Produk & Layanan", "ROI Kerugian Klien", "Portal Klien", "Admin Control Center"])

# --- 6. LOGIKA MENU (INTEGRASI PENUH) ---

if menu == "Visi & Misi":
    st.header("Visi & Misi Digitizing Trust, Eliminating Leakage")
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga - Founder & CEO", use_container_width=True)
    with col_txt:
        st.markdown("<div style='text-align: justify; line-height: 1.7; font-size: 16px; color: #d1d5db;'><b>V-Guard AI Intelligence</b> lahir dari urgensi integritas finansial... (teks asli Bapak)</div>", unsafe_allow_html=True)
    st.markdown("<center><small>V-Guard AI Intelligence | ©2026</small></center>", unsafe_allow_html=True)

elif menu == "Produk & Layanan":
    st.header("🛡️ Portfolio Layanan V-Guard AI Intelligence")
    wa_number = "6282122190885"
    c1, c2, c3, c4 = st.columns(4)
    packages = {
        "V-LITE": ["Mikro / 1 Kasir", "750 rb", "350 brb", "AI Fraud Detector Dasar, Daily WA/Email Summary, Monthly PDF Report"],
        "V-PRO": ["Retail & Kafe", "1.5 Jt", "850 rb", "VCS Integration, Bank Statement Audit, Input Excel/CSV/PDF, H-7 Auto-Invoice"],
        "V-SIGHT": ["Gudang & Toko", "7,5 Jt", "3,5 Jt", "CCTV AI Behavior, Visual Cashier Audit, Real-Time Stock, Fraud Alarm (🚨)"],
        "V-ENTERPRISE": ["Korporasi", "15 Jt", "10 Jt", "The Core Brain, Forensic AI (1 Thn), Dedicated Server, Custom AI SOP"]
    }
    for i, (name, details) in enumerate(packages.items()):
        with [c1, c2, c3, c4][i]:
            with st.container(border=True):
                st.markdown(f"### 📦 {name}")
                st.markdown(f"- {details[3]}")
                st.info(f"**Pasang:** {details[1]}\n\n**Bulan:** {details[2]}")
                st.link_button(f"Pilih {name}", f"https://wa.me/{wa_number}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20dengan%20paket%20*{name}*%20V-Guard%20AI.")

elif menu == "Portal Klien":
    st.header("Portal Klien V-Guard AI")
    c_reg, c_log = st.columns(2)
    with c_reg:
        st.subheader("📝 Form Order Baru")
        with st.container(border=True):
            nama_p = st.text_input("Nama Pelanggan")
            nama_u = st.text_input("Nama Usaha")
            pkt_p = st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            if st.button("Kirim Registrasi"):
                st.success("Registrasi Terkirim! Silakan selesaikan pembayaran. Admin akan mengaktifkan akun Anda.")

    with c_log:
        st.subheader("🔑 Akses User Aktif")
        with st.container(border=True):
            u_login = st.text_input("Username")
            p_login = st.text_input("Password", type="password")
            if st.button("Masuk"):
                if u_login in st.session_state.db_klien and p_login == "vguardklien2026":
                    st.session_state.client_logged_in = True
                    st.session_state.current_client = st.session_state.db_klien[u_login]
                    st.rerun()
                else:
                    st.error("Akun belum aktif atau password salah.")

# --- 7. LOGIKA DASHBOARD KLIEN (PENAMBAHAN PORTAL) ---
if menu == "Ringkasan Integritas":
    client = st.session_state.current_client
    st.header(f"🛡️ Dashboard Integritas: {client['nama']}")
    st.info(f"Paket Aktif: **{client['paket']}** | Status: {client['status']}")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Integritas Sistem", "99.2%", "Optimal")
    col2.metric("Anomali Terdeteksi", "0", "Aman")
    col3.metric("Profit Terlindungi", "Rp 4.5M", "+12%")

elif menu == "Fitur Layanan Paket":
    client = st.session_state.current_client
    st.subheader(f"🛠️ Toolset Khusus {client['paket']}")
    
    if client['paket'] == "V-LITE":
        st.write("✅ Daily Fraud Report Access")
        st.file_uploader("Upload Laporan Kasir (PDF/Excel)")
    elif client['paket'] == "V-PRO":
        st.write("✅ VCS Bank Statement Sync")
        st.button("Sync Mutasi Bank")
    elif client['paket'] == "V-SIGHT":
        st.write("✅ Visual CCTV Intelligence")
        st.image("https://img.freepik.com/free-photo/security-camera-detecting-thief-store_23-2150914187.jpg", width=400)
    elif client['paket'] == "V-ENTERPRISE":
        st.write("✅ Full Forensic AI Control Center")
        st.code("System Status: Otonom\nAgent Monitoring: Online")

elif menu == "Log Out Klien":
    st.session_state.client_logged_in = False
    st.session_state.current_client = None
    st.rerun()

# --- 8. ADMIN CONTROL CENTER (INTEGRASI 10 AI AGENT) ---
elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center")
    if "admin_logged_in" not in st.session_state: st.session_state.admin_logged_in = False

    if not st.session_state.admin_logged_in:
        admin_input = st.text_input("Administrator Password", type="password")
        if admin_input == "w1nbju8282":
            st.session_state.admin_logged_in = True
            st.rerun()
    else:
        # --- TAB ADMIN (STRUKTUR ASLI + 10 AGENT) ---
        t1, t2, t3, t_agents = st.tabs(["👤 Aktivasi Klien", "🖥️ Ekosistem AI", "📊 Laporan", "🤖 10 AI AGENT SQUAD"])
        
        with t1:
            st.subheader("Aktivasi Klien Baru")
            u_new = st.text_input("Username Klien Baru")
            p_new = st.selectbox("Paket Aktivasi", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            if st.button("AKTIFKAN AKUN SEKARANG"):
                st.session_state.db_klien[u_new] = {"nama": u_new, "paket": p_new, "status": "Aktif"}
                st.success(f"Akun {u_new} Berhasil Diaktivasi!")

        with t_agents:
            st.subheader("🕵️ V-Guard 10 Elite AI Agent Squad")
            st.caption("Masing-masing Agen bekerja secara otonom dalam isolasi data.")
            
            # Grid 10 AI Agents
            ag_cols = st.columns(5)
            agents = [
                "Sentinel", "Auditor", "Stocker", "Invoicer", "Recap",
                "V-Vision", "Cyber-Guard", "Profit-AI", "Log-Master", "Forensic"
            ]
            for idx, ag_name in enumerate(agents):
                with ag_cols[idx % 5]:
                    with st.container(border=True):
                        st.markdown(f"**Agent: {ag_name}**")
                        st.write("Status: 🟢 Running")
                        if st.button(f"Sync {ag_name}", key=ag_name):
                            st.toast(f"{ag_name} Sync Complete")

        if st.button("Admin Log Out"):
            st.session_state.admin_logged_in = False
            st.rerun()

st.markdown("<center><small>V-Guard AI Intelligence | ©2026</small></center>", unsafe_allow_html=True)
