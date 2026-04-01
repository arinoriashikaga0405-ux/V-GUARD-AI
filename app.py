import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. SETUP & API ---
# Masukkan API KEY Bapak dari Google AI Studio
API_KEY = "GANTI_DENGAN_API_KEY_BAPAK"
try:
    genai.configure(api_key=API_KEY)
    ai_model = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. CSS UI (SOP VISUAL) ---
st.markdown("""
<style>
    .main { background-color: #f5f7f9; }
    .stMetric { background: white; padding: 15px; border-radius: 10px; border: 1px solid #ddd; }
    .fraud-alarm { background: #ff4b4b; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; border: 2px solid yellow; margin-bottom: 20px; }
    .notif-jt { background: #fff3cd; color: #856404; padding: 10px; border-radius: 5px; border-left: 5px solid #ffc107; margin-bottom: 8px; }
    .profil-box { max-width: 800px; line-height: 1.8; text-align: justify; color: #1e293b; }
</style>
""", unsafe_allow_html=True)

# --- 3. DATABASE SESSION ---
if 'db' not in st.session_state:
    now = datetime.now().date()
    st.session_state.db = [{
        "ID": 101, "Bisnis": "Cafe Maju", 
        "Harga": 2500000, "Tempo": str(now + timedelta(days=5))
    }]

if 'login' not in st.session_state:
    st.session_state.login = False

# --- 4. DATA PROFIL (SOP 150 KATA) ---
TEKS_PROFIL = """Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel."""

# --- 5. SIDEBAR (V-GUARD STYLE) ---
with st.sidebar:
    st.markdown("<h1 style='text-align:center;'>🛡️ V-GUARD AI</h1>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.markdown("<h3 style='text-align:center;'>Erwin Sinaga</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:12px;'>Senior Business Leader</p>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("Intelligence Menu:", [
        "1. Profil Founder", 
        "2. V-Guard ROI Engine", 
        "3. Operational Control"
    ])
    st.write("---")
    st.link_button("💬 Support Center", "https://wa.me/628212190885")
    st.caption("© 2026 V-Guard AI Intelligence")

# --- 6. LOGIKA HALAMAN ---
if menu == "1. Profil Founder":
    st.header("Profil Kepemimpinan")
    st.markdown(f'<div class="profil-box">{TEKS_PROFIL}</div>', unsafe_allow_html=True)

elif menu == "2. V-Guard ROI Engine":
    st.header("Analisis Kebocoran & ROI")
    st.info("**Visi:** Standar emas audit AI real-time. **Misi:** Proteksi aset bisnis.")
    
    col1, col2 = st.columns(2)
    with col1:
        omzet = st.number_input("Omzet Bulanan (Rp):", value=100000000, step=5000000)
        bocor = omzet * 0.07
        save = bocor - 2500000
    
    with col2:
        st.metric("
