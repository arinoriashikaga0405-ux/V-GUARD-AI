import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE ---
# API Key sudah terpasang sesuai instruksi Bapak
KEY_AI = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"

try:
    genai.configure(api_key=KEY_AI)
    v_engine = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI", layout="wide")

# --- 2. DATABASE ---
if 'db_nasabah' not in st.session_state:
    skrg = datetime.now().date()
    st.session_state.db_nasabah = [{
        "ID": 101, "Tgl": str(skrg), 
        "Pelanggan": "Siska", "Bisnis": "Cafe Maju", 
        "Paket": "SMART", "Harga": 2500000, 
        "Jatuh_Tempo": str(skrg + timedelta(days=5)),
        "Status": "🟢 AKTIF"
    }]

if 'is_admin' not in st.session_state:
    st.session_state.is_admin = False

# --- 3. UI STYLE ---
st.markdown("""
<style>
    .alarm { background: #ff4b4b; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; border: 2px solid yellow; }
    .notif { background: #fff3cd; padding: 10px; border-radius: 5px; border-left: 5px solid #ffc107; margin-bottom: 5px; color: black; }
    .profil-box { line-height: 1.8; text-align: justify; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.markdown("**Erwin Sinaga**\nSenior Business Leader")
    st.write("---")
    menu = st.radio("Menu:", ["Profil", "Visi & ROI", "Admin"])
    st.write("---")
    st.link_button("💬 Support", "https://wa.me/628212190885")

# --- 5. HALAMAN ---

if menu == "Profil":
    st.header("Profil Founder")
    st.markdown('<div class="profil-box">Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan.</div>', unsafe_allow_html=True)

elif menu == "Visi & ROI":
    st.header("ROI Engine")
    st.info("Visi: Audit AI Real-time. Misi: Proteksi aset.")
    oz = st.number_input("Omzet (Rp):", value=100000000)
    bc = oz * 0.07
    st.error("Bocor (7%): Rp {:,.0f}".format(bc))
    st.success("Save: Rp {:,.0f}".format(bc - 2500000))

elif menu == "Admin":
    if not st.session_state.is_admin:
        pw = st.text_input("Password:", type="password")
        if st.button("Login"):
            if pw == "w1nbju8282":
                st.session_state.is_admin = True
                st.rerun()
    else:
        if st.button("🔒 Logout"):
            st.session_state.is_admin = False
            st.rerun()
        
        st.markdown('<div class="alarm">🚨 FRAUD ALERT DETECTED!</div>', unsafe_allow_html=True)
        
        # Notifikasi H-7
        td = datetime.now().date()
        for k in st.session_state.db_nasabah:
            jt = datetime.strptime(k['Jatuh_Tempo'], "%Y-%m-%d").date()
            if (jt - td).days <= 7
