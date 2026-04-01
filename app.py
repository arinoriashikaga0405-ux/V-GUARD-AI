import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. CONFIG & ENGINE AI ---
K_V = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=K_V)
    v_ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE ---
if 'db_o' not in st.session_state: st.session_state.db_o = []
if 'db_n' not in st.session_state:
    t = datetime.now().date()
    st.session_state.db_n = [{
        "ID": 101, "Nama": "Siska", "Bisnis": "Cafe Maju", 
        "Paket": "SMART", "Harga": 2500000, 
        "Tempo": str(t + timedelta(days=5))
    }]
if 'is_ad' not in st.session_state: st.session_state.is_ad = False

# --- 3. KONTEN SOP (150 KATA MURNI) ---
T_P = """Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel."""

# --- 4. CSS PREMIUM ---
st.markdown("""
<style>
    .alarm { background: #ff4b4b; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; border: 2px solid yellow; margin-bottom: 20px; }
    .notif { background: #fff3cd; padding: 10px; border-radius: 5px; border-left: 5px solid #ffc107; margin-bottom: 5px; color: black; }
    .photo-placeholder {
        width: 150px; height: 150px; background-color: #6B7280; border-radius: 10px;
        color: white; font-size: 60px; font-weight: bold; display: flex;
        align-items: center; justify-content: center; border: 3px solid #D1D5DB;
    }
</style>
""", unsafe_allow_html=True)

# --- 5. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    else:
        st.markdown('<div class="photo-placeholder">ES</div>', unsafe_allow_html=True)
    
    st.markdown("**Erwin Sinaga**\nSenior Business Leader")
    st.write("---")
    m = st.radio("Navigasi Utama:", ["Profil Founder", "Visi, Misi & ROI", "Paket Unggulan", "Registrasi & Upload", "Operasional & Audit"])
    st.write("---")
    st.caption("© 2026 V-Guard AI Intelligence")

# --- 6. LOGIKA HALAMAN ---
if m == "Profil Founder":
    st.header("Profil Kepemimpinan")
    col_img, col_txt
