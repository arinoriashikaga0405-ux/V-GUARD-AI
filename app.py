import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. CONFIG & API ---
# Ganti dengan API KEY Bapak
MY_KEY = "MASUKKAN_API_KEY_BAPAK"
try:
    genai.configure(api_key=MY_KEY)
    ai_model = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI", layout="wide")

# --- 2. DATA PROFIL (SOP 150 KATA) ---
TEKS_PROFIL = """Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel."""

# --- 3. DATABASE SESSION ---
if 'db' not in st.session_state:
    hari_ini = datetime.now().date()
    jt = str(hari_ini + timedelta(days=5))
    st.session_state.db = [{
        "ID": 101, "Bisnis": "Cafe Maju", 
        "Harga": 2500000, "Jatuh_Tempo": jt
    }]

if 'login' not in st.session_state:
    st.session_state.login = False

# --- 4. FUNGSI FORMAT ---
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
    menu = st.radio("Menu:", ["Profil", "ROI", "Admin"])
    st.write("---")
    st.link_button("Chat Support", "https://wa.me/628212190885")

# --- 6. LOGIKA HALAMAN ---
if menu == "Profil":
    st.header("Profil Founder")
    st.write(TEKS_PROFIL)

elif menu == "ROI":
    st.header("Analisis ROI")
    st.info("Visi: Audit AI Real-time. Misi: Mencegah kebocoran.")
    oz = st.number_input("Omzet (Rp):", value=100000000)
    bc = oz * 0.07
    st.error("Bocor (7%): " + rp(bc))
    st.success("Save: " + rp(bc - 2500000))

elif menu == "Admin":
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
        
        st.error("🚨 FRAUD ALERT: ANOMALI TERDETEKSI!")
        
        # Notif H-7
        skrg = datetime.now().date()
        for k in st.session_state.db:
            d_jt = datetime.strptime(k['Jatuh_Tempo'], "%Y-%m-%d").date()
            if (d_jt - skrg).days <= 7:
                st.warning("⚠️ JATUH TEMPO: " + k["Bisnis"] + " ("+ k['Jatuh_Tempo'] +")")

        t1, t2, t3 = st.tabs(["VCS Input", "Database", "Gemini Audit"])
        with t1:
            with st.form("vcs"):
                bn = st.text_input("Bisnis")
                hr = st.number_input("Harga", value=2500000)
                tg = st.date_input("Jatuh Tempo")
                if st.form_submit_button("Simpan"):
                    st.session_state.db.append({
                        "ID":
