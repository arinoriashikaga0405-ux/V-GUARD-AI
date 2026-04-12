import streamlit as st
import os
import google.generativeai as genai
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# --- 1. KONFIGURASI ENGINE & SECURITY ---
try:
    # Ambil API Key dari Secrets Streamlit
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
except:
    st.error("🚨 API Key tidak ditemukan di Secrets!")
    st.stop()

# Konfigurasi Efisiensi Biaya API < 20%
model_gemini = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    generation_config={"temperature": 0.2, "max_output_tokens": 50},
    system_instruction="Analisa transaksi. Balas 'ALERT' jika Fraud, 'PASS' jika normal."
)

# --- 2. KONEKSI GOOGLE SHEETS ---
# Pastikan URL Sheet sudah dimasukkan di Secrets sebagai GSHEET_URL
conn = st.connection("gsheets", type=GSheetsConnection)

# --- 3. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; height: 45px; }
    .visi-misi-box { text-align: justify; line-height: 1.7; font-size: 16px; color: #d1d5db; background-color: #112240; padding: 25px; border-radius: 12px; border-left: 5px solid #238636; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.markdown("<div style='text-align:center;'><p style='color:white; font-weight:bold; margin-bottom:0;'>Erwin Sinaga</p><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.divider()
    menu = st.radio("NAVIGASI", ["Visi & Misi", "Produk & Layanan", "Portal Klien", "Admin Control Center"])

# --- 5. LOGIKA MENU ---

if menu == "Visi & Misi":
    st.markdown("<h1 style='text-align: center;'>Digitizing Trust, Eliminating Leakage</h1>", unsafe_allow_html=True)
    col_img, col_txt = st.columns([1, 2], gap="large")
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga", use_container_width=True)
    with col_txt:
        st.markdown('<div class="visi-misi-box"><b>V-Guard AI</b> hadir untuk mendigitalisasi kepercayaan. Dengan pengalaman di industri perbankan, kami mengeliminasi kebocoran operasional melalui audit AI otonom 24/7. Kami memastikan setiap Rupiah Anda terjaga tanpa beban biaya cloud berlebih.</div>', unsafe_allow_html=True)

elif menu == "Portal Klien":
    st.header("🔑 Portal Dashboard Klien")
    
    tab_reg, tab_login = st.tabs(["📝 Registrasi Baru", "🔓 Login Dashboard"])
    
    with tab_reg:
        with st.form("reg_form", clear_on_submit=True):
            nama = st.text_input("Nama Lengkap")
            usaha = st.text_input("Nama Usaha")
            paket = st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            submit = st.form_submit_button("Daftar & Hubungkan ke Cloud")
            
            if submit:
                # Simpan ke Google Sheets
                new_data = pd.DataFrame([{"Nama": nama, "Usaha": usaha, "Paket": paket, "Tanggal": pd.Timestamp.now()}] )
                conn.create(data=new_data)
                st.success(f"Selamat {nama}! Data Anda telah terhubung ke Google Sheet V-Guard. Admin akan mengaktifkan akun Anda.")

    with tab_login:
        user_in = st.text_input("Username")
        pass_in = st.text_input("Password", type="password")
        if st.button("Masuk"):
            if pass_in == "vguard2026":
                st.session_state.client_logged = True
                st.success(f"Dashboard Online: Aktif paket {user_in}")
            else:
                st.error("Kredensial salah.")

elif menu == "Admin Control Center":
    st.header("🔒 Executive Command Center")
    if not st.session_state.get("admin_logged", False):
        pwd = st.text_input("Admin Password", type="password")
        if st.button("Login Admin"):
            if pwd == "w1nbju8282":
                st.session_state.admin_logged = True
                st.rerun()
    else:
        st.success("Monitoring OPEX & API (Target < 20%)")
        omset = st.number_input("Omset Kotor (Rp)", value=50000000)
        plafon = omset * 0.20
        st.metric("Plafon Biaya API (SOP 20%)", f"Rp {plafon:,.0f}")
        
        # Ambil data pendaftar dari GSheets
        st.subheader("📋 Data Klien dari Google Sheets")
        data_klien = conn.read()
        st.dataframe(data_klien)

# --- FOOTER ---
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026 | Secured by Gemini 1.5 Flash</small></center>", unsafe_allow_html=True)
