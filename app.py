import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# 1. INTEGRASI GOOGLE GEMINI AI
# Dapatkan API Key di: https://aistudio.google.com/
API_KEY = "MASUKKAN_API_KEY_GOOGLE_STUDIO_BAPAK"
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("API Key Gemini belum valid. Fitur Audit AI akan berjalan dalam mode simulasi.")

# 2. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

if 'db_nasabah' not in st.session_state:
    now = datetime.now().date()
    st.session_state.db_nasabah = [{
        "ID": 101, "Tgl": str(now), "Pelanggan": "Siska",
        "Bisnis": "Cafe Maju", "Paket": "SMART", "Harga": 2500000, 
        "Jatuh_Tempo": str(now + timedelta(days=5)), "Status": "🟢 AKTIF"
    }]

if 'admin_in' not in st.session_state:
    st.session_state.admin_in = False

PWD = "w1nbju8282"

def format_rp(n):
    v = "{:,.0f}".format(float(n))
    return "Rp " + v.replace(",", ".")

# 3. SIDEBAR (NAVIGASI SOP)
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.markdown("**Erwin Sinaga**\nSenior Business Leader")
    st.write("---")
    m = st.radio("Menu Utama:", ["1. Profil Founder", "2. Visi, Misi & ROI", "3. Panel Admin"])
    st.write("---")
    st.link_button("💬 Support WA", "https://wa.me/628212190885")

# 4. HALAMAN 1: PROFIL (LOCKED 150 WORDS)
if m == "1. Profil Founder":
    st.header("Profil Kepemimpinan")
    st.write("""Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel dan adaptif terhadap tantangan ekonomi masa depan.""")

# 5. HALAMAN 2: VISI, MISI & ROI
elif m == "2. Visi, Misi & ROI":
    st.header("Strategi & Analisis ROI")
    st.info("**Visi:** Standar emas audit AI real-time.\n\n**Misi:** Mencegah kebocoran aset melalui integrasi Gemini AI Studio.")
    st.write("---")
    oz = st.number_input("Omzet Bulanan Bisnis (Rp):", value=100000000, step=1000000)
    bc = oz * 0.07
    st.error("Potensi Kebocoran (7%): " + format_rp(bc))
    st.success("Dana Diselamatkan V-Guard: " + format_rp(bc - 2500000))

# 6. PANEL ADMIN (VCS, ALARM, GEMINI AUDIT)
elif m == "3. Panel Admin":
    if not st.session_state.admin_in:
        p = st.text_input("Admin Password:", type="password")
        if st.button("Login"):
            if p == PWD:
                st.session_state.admin_in = True
                st.
