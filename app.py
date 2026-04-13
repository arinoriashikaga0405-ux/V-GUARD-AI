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

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; height: 45px; }
    .stTextInput>div>div>input { background-color: #1e293b; color: white; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA V-GUARD (PENYARING BIAYA API 20%) ---
def proses_transaksi(total, data_input):
    if total < 5000000:
        return "PASS (Auto)", False
    response = model_gemini.generate_content(f"Cek: {data_input}")
    return response.text, True

if menu == "Visi & Misi":
    st.header("Visi & Misi Digitizing Trust, Eliminating Leakage")
    
    # MENAMPILKAN FOTO FOUNDER DI HALAMAN VISI & MISI
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga - Founder & CEO", use_container_width=True)
        else:
            st.info("File erwin.jpg tidak ditemukan di direktori.")

    with col_txt:
        st.markdown("""
        <div style="text-align: justify; line-height: 1.7; font-size: 16px; color: #d1d5db;">
        <b>V-Guard AI Intelligence</b> lahir dari urgensi integritas finansial di era transformasi digital. Sebagai entitas yang dipimpin oleh profesional dengan pengalaman lebih dari satu dekade di industri perbankan dan manajemen aset, kami memahami bahwa celah terkecil dalam sistem operasional adalah potensi kerugian fatal bagi sebuah bisnis. Misi utama kami adalah mendigitalisasi kepercayaan (Digital Trust) melalui pembuktian matematis dan audit cerdas yang bekerja secara otonom 24 jam nonstop tanpa kompromi.<br><br>
        Kami percaya bahwa kejujuran sistem tidak boleh hanya bergantung pada pengawasan manusia yang memiliki keterbatasan, melainkan harus dibangun di atas fondasi teknologi AI yang presisi. Melalui ekosistem V-Guard, kami mengintegrasikan analisis data perbankan (VCS), visi komputer, dan deteksi anomali prediktif untuk menciptakan lingkungan bisnis yang bersih dari segala bentuk kecurangan (Fraud). Strategi kami adalah memberikan transparansi mutlak kepada pemilik bisnis melalui laporan yang akurat dan real-time.<br><br>
        Visi kami adalah menjadi standar global dalam " Eliminating Leakage ", di mana setiap pemilik bisnis, mulai dari UMKM hingga korporasi besar, dapat menjalankan operasional mereka dengan tenang karena setiap Rupiah diawasi oleh kecerdasan buatan yang tak kenal lelah. V-Guard bukan sekadar perangkat lunak, melainkan benteng pertahanan terakhir bagi aset dan masa depan investasi Anda. Kami hadir untuk mengeliminasi kebocoran, mengoptimalkan profitabilitas, dan menjaga warisan bisnis Anda tetap utuh melalui inovasi teknologi yang melampaui standar audit konvensional saat ini.
        </div>
        """, unsafe_allow_html=True)


elif menu == "ROI Kerugian Klien":
    st.header("📊 Analisis Potensi Kerugian vs ROI")
    col_a, col_b = st.columns(2)
    with col_a:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
        leak = st.slider("Estimasi Kebocoran (%)", 1, 20, 5)
        loss = omzet * (leak / 100)
        st.error(f"Potensi Kerugian: Rp {loss:,.0f} / bulan")

        
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

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- 1. DEFINISI FUNGSI ADMIN (Kode Bapak) ---
def admin_center_vguard():
    # Judul ini hanya akan muncul di dalam menu Admin
    st.header("🔒 Admin Control Center - V-Guard AI Intelligence")

    # --- SECURITY LAYER ---
    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False

    if not st.session_state.admin_logged_in:
        col_l, _ = st.columns([1, 1])
        with col_l:
            admin_pwd = st.text_input("Administrator Password", type="password")
            if st.button("Buka Akses Kontrol"):
                if admin_pwd == "w1nbju8282":
                    st.session_state.admin_logged_in = True
                    st.rerun()
                else:
                    st.error("Akses Ditolak.")
        return # Berhenti di sini jika belum login

    # --- KONTEN ADMIN (Hanya muncul jika sudah login) ---
    col_st, col_out = st.columns([5, 1])
    col_st.success("✅ Akses Eksekutif Aktif: Erwin Sinaga (Founder & CEO)")
    if col_out.button("Log Out"):
        st.session_state.admin_logged_in = False
        st.rerun()

    st.divider()

    # --- 10 AI AGENT SQUAD ---
    st.subheader("🤖 V-Guard 10 Elite AI Agent Squad")
    agents = [
        {"name": "Sentinel", "task": "Fraud Detection", "icon": "🕵️"},
        {"name": "Auditor", "task": "Financial Sync", "icon": "💰"},
        {"name": "Stocker", "task": "Visual Inventory", "icon": "📦"},
        {"name": "Invoicer", "task": "Auto Billing", "icon": "📄"},
        {"name": "Recap", "task": "Data Summary", "icon": "📊"},
        {"name": "V-Vision", "task": "CCTV Analysis", "icon": "👁️"},
        {"name": "Cyber-Guard", "task": "Network Security", "icon": "🛡️"},
        {"name": "Profit-AI", "task": "ROI Optimization", "icon": "📈"},
        {"name": "Log-Master", "task": "System Logs", "icon": "📜"},
        {"name": "Forensic", "task": "Investigation", "icon": "🔍"}
    ]
    ag_cols = st.columns(5)
    for idx, ag in enumerate(agents):
        with ag_cols[idx % 5]:
            with st.container(border=True):
                st.markdown(f"{ag['icon']} **{ag['name']}**")
                st.caption(f"Status: 🟢 Running")
                st.button(f"Sync {ag['name']}", key=f"sync_{ag['name']}")

    st.divider()

    # --- TABS MANAJEMEN ---
    tabs = st.tabs(["👤 Aktivasi", "🖥️ Ekosistem", "⚙️ Pengaturan", "📊 Laporan", "🛡️ Keamanan", "💾 Backup", "🌐 Jaringan", "📈 Performa", "💎 V-ULTRA"])
    
    with tabs[0]: # Aktivasi
        st.subheader("📝 Pembuatan & Aktivasi Akun Klien")
        with st.container(border=True):
            c_a, c_b = st.columns(2)
            new_user = c_a.text_input("Username Klien")
            new_mail = c_a.text_input("Email Bisnis")
            paket = c_b.selectbox("Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            tgl_bayar = c_b.date_input("Tanggal Bayar", value=datetime.now())
            if st.button("🚀 AKTIFKAN & SIMPAN"):
                st.success(f"Akun {new_user} Aktif!")

    with tabs[3]: # Laporan & Invoicer H-7
        st.subheader("📊 Laporan & Invoicer (H-7 Monitoring)")
        st.info("Agent Invoicer memindai jatuh tempo dalam 7 hari.")
        # Simulasi H-7
        with st.container(border=True):
            st.warning("🔔 **REMINDER H-7**: Toko Maju")
            st.write("Tagihan: Rp 1.500.000 | Jatuh Tempo: 20 April 2026")
            st.button("Kirim WA Reminder")

    with tabs[4]: # 10 Pilar Keamanan
        st.subheader("🛡️ 10 Pilar Keamanan V-Guard AI")
        c1, c2 = st.columns(2)
        c1.write("1. **E2EE** | 2. **MFA** | 3. **RBAC** | 4. **File Scan** | 5. **Audit Log**")
        c2.write("6. **Rate Limit** | 7. **Data Masking** | 8. **Pen-Test** | 9. **PDP** | 10. **Incident Response**")

    st.markdown("<center><small>V-Guard AI Intelligence Admin Portal | ©2026</small></center>", unsafe_allow_html=True)

# --- 2. SISTEM NAVIGASI UTAMA (PENTING!) ---
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    # Menu pilihan
    menu = st.radio("NAVIGASI UTAMA", 
                    ["Visi & Misi", "Produk & Layanan", "ROI Kerugian Klien", "Portal Klien", "Admin Control Center"])

# --- 3. EKSEKUSI MENU (SEKAT KETAT) ---
if menu == "Visi & Misi":
    st.header("Visi & Misi")
    st.write("Target: Zero Leakage, High Integrity.")

elif menu == "Produk & Layanan":
    st.header("Produk & Layanan")
    st.write("Integrasi: MindBridge, DataRobot, Alteryx.")

elif menu == "ROI Kerugian Klien":
    st.header("ROI Kerugian Klien")

elif menu == "Portal Klien":
    st.header("Portal Klien")


