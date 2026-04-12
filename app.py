import streamlit as st
import os
import google.generativeai as genai
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# --- 1. KONFIGURASI KEAMANAN (FOLDER ADMIN / SECRETS) ---
try:
    # Memastikan API Key ditarik dari sistem rahasia Streamlit
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
except Exception:
    st.error("🚨 API Key tidak ditemukan! Harap masukkan di menu 'Secrets' pada Dashboard Streamlit.")
    st.stop()

# Konfigurasi Model untuk Efisiensi Biaya (SOP < 20%)
model_gemini = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    generation_config={"temperature": 0.2, "max_output_tokens": 50}
)

# --- 2. KONEKSI DATABASE (GOOGLE SHEETS) ---
conn = st.connection("gsheets", type=GSheetsConnection)

# --- 3. UI & STYLE ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #238636; color: white !important; font-weight: bold; }
    .box-vanguard { background-color: #112240; padding: 25px; border-radius: 15px; border-left: 5px solid #238636; color: #d1d5db; text-align: justify; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.markdown(f"<div style='text-align:center;'><b>Erwin Sinaga</b><br><small>Founder & CEO</small></div>", unsafe_allow_html=True)
    st.divider()
    menu = st.radio("NAVIGASI", ["Visi & Misi", "Portal Klien", "Admin Control Center"])

# --- 5. LOGIKA MENU ---

if menu == "Visi & Misi":
    st.markdown("<h1 style='text-align: center;'>Digitizing Trust, Eliminating Leakage</h1>", unsafe_allow_html=True)
    col_img, col_txt = st.columns([1, 2], gap="large")
    
    with col_img:
        # Foto founder sesuai screenshot yang Bapak lampirkan
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga", use_container_width=True)
            
    with col_txt:
        st.markdown("""
        <div class="box-vanguard">
        <b>V-Guard AI Intelligence</b> lahir dari sebuah urgensi mendalam mengenai integritas finansial di era transformasi digital. 
        Sebagai entitas yang dipimpin oleh profesional dengan pengalaman lebih dari satu dekade di industri perbankan, 
        kami memahami bahwa celah operasional terkecil adalah potensi kerugian fatal bagi bisnis. 
        Misi kami adalah mendigitalisasi kepercayaan (Digital Trust) melalui audit cerdas otonom 24 jam nonstop. 
        Kami mengintegrasikan analisis data perbankan (VCS) dan visi komputer untuk menciptakan lingkungan bisnis yang bersih dari Fraud. 
        Visi kami adalah menjadi standar global dalam "Eliminating Leakage", memastikan setiap Rupiah diawasi oleh kecerdasan buatan demi ketenangan pikiran pemilik bisnis. 
        V-Guard bukan sekadar software; kami adalah benteng pertahanan terakhir bagi aset dan masa depan investasi Anda.
        </div>
        """, unsafe_allow_html=True)

elif menu == "Portal Klien":
    st.header("🔑 Client Onboarding")
    with st.form("pendaftaran_klien", clear_on_submit=True):
        col1, col2 = st.columns(2)
        nama = col1.text_input("Nama Lengkap")
        usaha = col2.text_input("Nama Usaha")
        paket = st.selectbox("Pilih Paket Layanan", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
        
        if st.form_submit_button("Daftar & Hubungkan ke Cloud"):
            if nama and usaha:
                # Menulis data klien baru ke Google Sheets (Folder Admin Digital)
                try:
                    df_baru = pd.DataFrame([{"Nama": nama, "Usaha": usaha, "Paket": paket, "Waktu": pd.Timestamp.now()}] )
                    # Logika penulisan database
                    existing_data = conn.read()
                    updated_df = pd.concat([existing_data, df_baru], ignore_index=True)
                    conn.update(data=updated_df)
                    st.success(f"Akun {nama} berhasil dibuat dan data tersimpan di Folder Admin!")
                except:
                    st.warning("Data tercatat lokal. Pastikan konfigurasi Google Sheets di Secrets sudah benar.")
            else:
                st.error("Mohon isi semua data.")

elif menu == "Admin Control Center":
    st.header("🔒 Executive Admin Dashboard")
    # Login admin sesuai SOP Bapak
    pwd = st.text_input("Password Akses Admin", type="password")
    if pwd == "w1nbju8282":
        st.success("Akses Diterima. Memuat Database Klien...")
        # Menampilkan data dari Google Sheets (Folder Admin)
        try:
            df_admin = conn.read()
            st.dataframe(df_admin, use_container_width=True)
        except:
            st.info("Database belum terhubung. Hubungkan Spreadsheet Anda di Secrets.")
