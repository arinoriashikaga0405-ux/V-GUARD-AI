import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. API SETUP ---
KEY = "MASUKKAN_API_KEY_BAPAK"
try:
    genai.configure(api_key=KEY)
    ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI")

# --- 2. SESSION DATA ---
if 'db' not in st.session_state:
    skrg = datetime.now().date()
    jt = str(skrg + timedelta(days=5))
    st.session_state.db = [{
        "ID": 101, "Bisnis": "Cafe Maju", 
        "Harga": 2500000, "Tempo": jt
    }]

if 'login' not in st.session_state:
    st.session_state.login = False

# --- 3. TEKS PROFIL (SOP) ---
T_PROFIL = """Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel."""

# --- 4. FORMAT RP ---
def rp(n):
    v = "{:,.0f}".format(float(n)).replace(",", ".")
    return "Rp " + v

# --- 5. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.write("**Erwin Sinaga**")
    st.write("---")
    m = st.radio("Menu:", ["Profil", "ROI", "Admin"])
    st.write("---")
    st.caption("© 2026 V-Guard AI")

# --- 6. HALAMAN ---
if m == "Profil":
    st.header("Profil Founder")
    st.write(T_PROFIL)

elif m == "ROI":
    st.header("Analisis ROI")
    oz = st.number_input("Omzet:", value=100000000)
    bc = oz * 0.07
    st.error("Bocor (7%): " + rp(bc))
    st.success("Save: " + rp(bc - 2500000))

elif m == "Admin":
    if not st.session_state.login:
        p = st.text_input("Sandi:", type="password")
        if st.button("Masuk"):
            if p == "w1nbju8282":
                st.session_state.login = True
                st.rerun()
    else:
        if st.button("🔒 Keluar"):
            st.session_state.login = False
            st.rerun()
        
        st.error("🚨 FRAUD ALERT DETECTED!")
        
        # Cek Jatuh Tempo
        tday = datetime.now().date()
        for k in st.session_state.db:
            d_jt = datetime.strptime(k['Tempo'], "%Y-%m-%d").date()
            if (d_jt - tday).days <= 7:
                st.warning("⚠️ JATUH TEMPO: " + k["Bisnis"])

        t1, t2 = st.tabs(["VCS Input", "Database"])
        with t1:
            with st.form("vcs"):
                bn = st.text_input("Bisnis")
                hr = st.number_input("Harga", value=2500000)
                tg = st.date_input("Tempo")
                if st.form_submit
