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

st.set_page_config(page_title="V-Guard AI", layout="wide")

# --- 2. DATA ---
if 'ord' not in st.session_state: st.session_state.ord = []
if 'db' not in st.session_state:
    sk = datetime.now().date()
    jt = str(sk + timedelta(days=5))
    st.session_state.db = [{"ID":101, "Bisnis":"Cafe Maju", "Harga":2500000, "Tempo":jt}]
if 'ok' not in st.session_state: st.session_state.ok = False

# --- 3. PROFIL (SOP 150 KATA) ---
T_P = """Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel."""

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
    st.write("**Erwin Sinaga**")
    m = st.radio("Navigasi:", ["Profil", "ROI & Paket", "Order", "Admin"])
    st.write("---")
    st.caption("© 2026 V-Guard AI")

# --- 5. HALAMAN ---
if m == "Profil":
    st.header("Profil Founder")
    st.write(T_P)

elif m == "ROI & Paket":
    st.header("ROI & Paket Layanan")
    oz = st.number_input("Omzet (Rp):", 100000000)
    bc = oz * 0.07
    st.error("Bocor (7%): Rp {:,.0f}".format(bc))
    st.success("Save via V-Guard: Rp {:,.0f}".format(bc-2500000))
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📦 BASIC (1.5jt)")
        st.write("1. AI Monitor\n2. Report Mingguan\n3. Alarm\n4. Support")
        st.subheader("🚀 SMART (2.5jt)")
        st.write("1. Basic+\n2. VCS System\n3. Audit Realtime\n4. Notif WA\n5. Dashboard")
    with c2:
        st.subheader("🛡️ PRO (5jt)")
        st.write("1. Smart+\n2. Forensic\n3. Konsultasi\n4. Proteksi\n5. Multi-User")
        st.subheader("👑 ENTERPRISE (10jt)")
        st.write("1. Pro+\n2. Custom AI\n3. Onsite Audit\n4. 24/7\n5. Risk Mgmt\n6. Fraud Ins.")

elif m == "Order":
    st.header("Formulir Order")
    with st.form("f_ord"):
        nm = st.text_input("Nama")
        us = st.text_input("Usaha")
        pk = st.selectbox("Paket", ["BASIC", "SMART", "PRO", "ENTERPRISE"])
        st.file_uploader("Upload Data")
        if st.form_submit_button("Kirim Order"):
            st.session_state.ord.append({"Nama":nm, "Usaha":us, "Paket":pk})
            st.success("Order Terkirim!")

elif m == "Admin":
    if not st.session_state.ok:
        p = st.text_input("Pass:", type="password")
        if st.button("Masuk"):
            if p == "w1nbju8282":
                st.session_state.ok = True
                st.rerun()
    else:
        if st.button("🔒 Keluar"):
            st.session_state.ok = False
            st.rerun()
        st.error("🚨 FRAUD ALERT DETECTED!")
        td = datetime.now().date()
        for k in st.session_state.db:
            jt = datetime.strptime(k['Tempo'], "%Y-%m
