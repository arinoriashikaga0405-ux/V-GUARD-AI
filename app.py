import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. ENGINE AI ---
K_AI = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=K_AI)
    v_ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI Intelligence")

# --- 2. DATA SESSION ---
if 'db' not in st.session_state:
    t = datetime.now().date()
    j = str(t + timedelta(days=5))
    # Struktur data dibuat flat agar tidak terpotong
    d = {"ID": 101, "Bisnis": "Cafe Maju", "Harga": 2500000, "Tempo": j}
    st.session_state.db = [d]

if 'ok' not in st.session_state:
    st.session_state.ok = False

# --- 3. PROFIL (SOP) ---
T_P = """Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan."""

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.write("**Erwin Sinaga**")
    m = st.radio("Intelligence Menu:", ["Profil", "ROI Engine", "Admin"])
    st.write("---")
    st.caption("© 2026 V-Guard AI")

# --- 5. HALAMAN ---
if m == "Profil":
    st.header("Profil Founder")
    st.write(T_P)

elif m == "ROI Engine":
    st.header("V-Guard ROI Analysis")
    oz = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    bc = oz * 0.07
    sv = bc - 2500000
    st.error("Estimasi Kebocoran (7%): Rp {:,.0f}".format(bc))
    st.success("Dana Diselamatkan: Rp {:,.0f}".format(sv))

elif m == "Admin":
    if not st.session_state.ok:
        p = st.text_input("Password:", type="password")
        if st.button("Authorize"):
            if p == "w1nbju8282":
                st.session_state.ok = True
                st.rerun()
    else:
        if st.button("🔒 Logout"):
            st.session_state.ok = False
            st.rerun()
        
        st.error("🚨 FRAUD ALERT DETECTED!")
        
        # Notif Jatuh Tempo H-7
        td = datetime.now().date()
        for k in st.session_state.db:
            jt = datetime.strptime(k['Tempo'], "%Y-%m-%d").date()
            if (jt - td).days <= 7:
                st.warning("⚠️ JATUH TEMPO: " + k["Bisnis"])

        t1, t2 = st.tabs(["VCS Input", "Audit AI"])
        with t1:
            with st.form("v"):
                bn = st.text_input("Nama Bisnis")
                hr = st.number_input("Harga Kontrak", 2500000)
                tg = st.date_input("Target Tempo")
                if st.form_submit_button("SIMPAN DATA"):
                    # Teknik anti-potong: Buat variabel dulu
                    new_item = {"ID":105, "Bisnis":bn, "Harga":hr, "Tempo":str(tg)}
                    st.session_state.db.append(new_item)
                    st.rerun()
        with t2:
            st.table(pd.DataFrame(st.session_state.db))
            tx = st.text_area("Audit Data Transaksi:")
            if st.button("PROSES AUDIT"):
                res = v_ai.generate_content(tx)
                st.write(res.text)
