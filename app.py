import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. API SETUP ---
# Masukkan API Key Bapak di sini
KEY = "GANTI_DENGAN_API_KEY_BAPAK"
try:
    genai.configure(api_key=KEY)
    ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard")

# --- 2. DATA ---
if 'db' not in st.session_state:
    hr = datetime.now().date()
    jt = str(hr + timedelta(days=5))
    st.session_state.db = [{
        "ID": 101, "Bisnis": "Cafe Maju", 
        "Harga": 2500000, "Tempo": jt
    }]

if 'log' not in st.session_state:
    st.session_state.log = False

# --- 3. PROFIL (SOP) ---
T_PRO = """Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel."""

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.write("**Erwin Sinaga**")
    st.write("---")
    m = st.radio("Menu:", ["Profil", "ROI", "Admin"])
    st.write("---")
    st.caption("© 2026 V-Guard AI")

# --- 5. HALAMAN ---
if m == "Profil":
    st.header("Profil Founder")
    st.write(T_PRO)

elif m == "ROI":
    st.header("Analisis ROI")
    oz = st.number_input("Omzet:", 100000000)
    bc = oz * 0.07
    st.error("Bocor (7%): Rp " + str(bc))
    st.success("Save: Rp " + str(bc-2500000))

elif m == "Admin":
    if not st.session_state.log:
        p = st.text_input("Pass:", type="password")
        if st.button("Login"):
            if p == "w1nbju8282":
                st.session_state.log = True
                st.rerun()
    else:
        if st.button("🔒 Logout"):
            st.session_state.log = False
            st.rerun()
        
        st.error("🚨 FRAUD DETECTED!")
        
        # Notif H-7
        tday = datetime.now().date()
        for k in st.session_state.db:
            d_jt = datetime.strptime(k['Tempo'], "%Y-%m-%d").date()
            if (d_jt - tday).days <= 7:
                st.warning("⚠️ TEMPO: " + k["Bisnis"])

        t1, t2 = st.tabs(["Input", "Data"])
        with t1:
            with st.form("vcs"):
                bn = st.text_input("Bisnis")
                hr = st.number_input("Harga", 2500000)
                tg = st.date_input("Tempo")
                ok = st.form_submit_button("SIMPAN")
                if ok:
                    itm = {}
                    itm["ID"] = 105
                    itm["Bisnis"] = bn
                    itm["Harga"] = hr
                    itm["Tempo"] = str(tg)
                    st.session_state.db.append(itm)
                    st.rerun()
        with t2:
            st.table(pd.DataFrame(st.session_state.db))
            txt = st.text_area("Audit AI:")
            go = st.button("AUDIT")
            if go:
                if KEY != "GANTI_DENGAN_API_KEY_BAPAK":
                    res = ai.generate_content(txt)
                    st.write(res.text)

# --- FINISH ---
