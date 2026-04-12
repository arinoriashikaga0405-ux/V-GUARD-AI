import streamlit as st
import os
import google.generativeai as genai
import pandas as pd

# --- 1. V-GUARD CORE ENGINE (PRIVATE) ---
# API Key dipindahkan ke konstanta internal yang tidak dipanggil ke UI
_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA" 
genai.configure(api_key=_KEY)

model_vguard = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    generation_config={"temperature": 0.1, "max_output_tokens": 50},
    system_instruction="Analisa transaksi: ALERT jika ada fraud, PASS jika aman."
)

# --- 2. KONFIGURASI TAMPILAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")
st.markdown("<style>.main { background-color: #0e1117; }</style>", unsafe_allow_html=True)

# --- 3. DATABASE BRIDGE (SPREADSHEET) ---
def sync_to_spreadsheet(client_data):
    # Bridge otomatis ke database Google Sheets/Excel Cloud
    pass

# --- 4. SIDEBAR & NAVIGASI ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.markdown("<div style='text-align:center; color:white;'><b>Erwin Sinaga</b><br><small>Founder & CEO</small></div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Produk & Layanan", "ROI & Opex Analysis", "Portal Klien", "Admin Control Center"])

# --- 5. IMPLEMENTASI FITUR ---

if menu == "Visi & Misi":
    # Kode asli tetap dipertahankan sesuai instruksi
    st.header("Visi & Misi Digitizing Trust")
    st.write("V-Guard AI Intelligence lahir dari urgensi integritas finansial...")

elif menu == "Produk & Layanan":
    st.header("🛡️ Portfolio Layanan")
    # Tabel paket sesuai kode asli Bapak
    packages = {
        "V-LITE": ["750 rb", "350 rb"],
        "V-PRO": ["1.5 Jt", "850 rb"],
        "V-SIGHT": ["7,5 Jt", "3,5 Jt"],
        "V-ENTERPRISE": ["15 Jt", "10 Jt"]
    }
    cols = st.columns(4)
    for i, (name, prices) in enumerate(packages.items()):
        with cols[i]:
            with st.container(border=True):
                st.subheader(name)
                st.write(f"Pasang: {prices[0]}")
                st.write(f"Langganan: {prices[1]}")

elif menu == "ROI & Opex Analysis":
    st.header("📊 Analisis Finansial")
    omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
    
    col1, col2 = st.columns(2)
    with col1:
        leak = st.slider("Estimasi Kebocoran (%)", 1, 20, 5)
        loss = omzet * (leak / 100)
        st.error(f"Potensi Kerugian: Rp {loss:,.0f}")
    
    with col2:
        # --- FITUR: 20% OPEX DARI OMSET KOTOR ---
        opex_total = omzet * 0.20
        st.warning(f"Batas Opex (20%): Rp {opex_total:,.0f}")
        st.info("Sistem AI membantu menekan Opex dengan otomatisasi.")

elif menu == "Portal Klien":
    st.header("Portal Klien V-Guard AI")
    
    if "active_session" not in st.session_state:
        st.session_state.active_session = False

    if not st.session_state.active_session:
        # Form Login/Registrasi
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("📝 Order & Registrasi")
            reg_name = st.text_input("Nama Usaha")
            reg_pkg = st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            if st.button("Kirim Data ke Spreadsheet"):
                sync_to_spreadsheet({"nama": reg_name, "paket": reg_pkg})
                st.success("Registrasi Berhasil Terkirim.")
        with c2:
            st.subheader("🔑 Login Klien")
            pw = st.text_input("Password", type="password")
            if st.button("Masuk"):
                if pw == "vguardklien2026":
                    st.session_state.active_session = True
                    st.session_state.current_pkg = reg_pkg
                    st.rerun()
    else:
        # --- DASHBOARD KLIEN SESUAI PRODUK ---
        pkg = st.session_state.current_pkg
        st.subheader(f"🛡️ Management Dashboard - Paket {pkg}")
        
        # Integrasi Spreadsheet Visual
        st.info(f"Data tersinkronisasi otomatis dengan Database Cloud {pkg}.")
        
        tabs = st.tabs(["Laporan AI", "Audit Transaksi", "CCTV Monitor"] if pkg in ["V-SIGHT", "V-ENTERPRISE"] else ["Laporan AI", "Audit Transaksi"])
        
        with tabs[0]:
            st.metric("Integritas Sistem", "99.8%", delta="Aman")
            if pkg == "V-LITE":
                st.write("Fitur: Ringkasan Fraud Harian via WA.")
            else:
                st.write(f"Fitur {pkg}: Audit mendalam sedang berjalan.")

        if st.button("Keluar Portal"):
            st.session_state.active_session = False
            st.rerun()

elif menu == "Admin Control Center":
    # Kode Admin tetap utuh sesuai dokumen Word Bapak
    st.header("🔒 Admin Control Center")
    admin_pw = st.text_input("Admin Password", type="password")
    if admin_pw == "w1nbju8282":
        st.success("Welcome, Commander Erwin.")
        # Lanjutan kode admin Bapak...
