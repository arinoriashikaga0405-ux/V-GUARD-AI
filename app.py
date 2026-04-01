import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. ENGINE ---
K_AI = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=K_AI)
    v_ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI")

# --- 2. DATA ---
if 'db' not in st.session_state:
    t = datetime.now().date()
    j = str(t + timedelta(days=5))
    st.session_state.db = [{
        "ID": 101, "Bisnis": "Cafe Maju", 
        "Harga": 2500000, "Tempo": j
    }]

if 'ok' not in st.session_state:
    st.session_state.ok = False

# --- 3. PROFIL SOP ---
T_P = """Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan."""

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.write("**Erwin Sinaga**")
    m = st.radio("Menu:", ["Profil", "ROI", "Admin"])
    st.write("---")
    st.caption("© 2026 V-Guard AI")

# --- 5. HALAMAN ---
if m == "Profil":
    st.header("Profil Founder")
    st.write(T_P)

elif m == "ROI":
    st.header("ROI Engine")
    oz = st.number_input("Omzet:", value=100000000)
    bc = oz * 0.07
    st.error("Bocor (7%): Rp {:,.0f}".format(bc))
    st.success("Save: Rp {:,.0f}".format(bc - 2500000))

elif m == "Admin":
    if not st.session_state.ok:
        p = st.text_input("Pass:", type="password")
        if st.button("Login"):
            if p == "w1nbju8282":
                st.session_state.ok = True
                st.rerun()
    else:
        if st.button("🔒 Keluar"):
            st.session_state.ok = False
            st.rerun()
        
        st.error("🚨 FRAUD ALERT!")
        
        # Notif H-7 (Versi Aman)
        td = datetime.now().date()
        for k in st.session_state.db:
            jt = datetime.strptime(k['Tempo'], "%Y-%m-%d").date()
            hari = (jt - td).days
            # Baris pendek agar tidak terpotong
            if hari <= 7:
                st.warning("⚠️ TEMPO: " + k["Bisnis"])

        t1, t2 = st.tabs(["VCS", "Audit"])
        with t1:
            with st.form("v"):
                bn = st.text_input("Bisnis")
                hr = st.number_input("Harga", 2500000)
                tg = st.date_input("Tempo")
                if st.form_submit_button("Simpan"):
                    n = {"ID":105, "Bisnis":bn, "Harga":hr, "Tempo":str(tg)}
                    st.session_state.db.append(
