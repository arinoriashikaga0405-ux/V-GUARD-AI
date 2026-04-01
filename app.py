import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. CONFIG ---
K = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=K)
    ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI")

# --- 2. DATA ---
if 'ord' not in st.session_state:
    st.session_state.ord = []
if 'db' not in st.session_state:
    t = datetime.now().date()
    j = str(t + timedelta(days=5))
    st.session_state.db = [{
        "ID":101, "Nama":"Siska",
        "Bisnis":"Cafe Maju", "Harga":2500000,
        "Tempo":j
    }]
if 'ok' not in st.session_state:
    st.session_state.ok = False

# --- 3. PROFIL (150 KATA) ---
P = """Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel."""

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.write("**Erwin Sinaga**")
    m = st.radio("Menu:", ["Profil", "ROI", "Paket", "Order", "Admin"])

# --- 5. LOGIKA ---
if m == "Profil":
    st.header("Profil Founder")
    st.write(P)

elif m == "ROI":
    st.header("Visi & ROI 7%")
    oz = st.number_input("Omzet:", 100000000)
    bc = oz * 0.07
    st.error("Bocor: Rp {:,.0f}".format(bc))
    st.success("Save: Rp {:,.0f}".format(bc-2500000))

elif m == "Paket":
    st.header("Layanan")
    st.info("BASIC (1.5jt): 4 Fitur")
    st.write("1.AI, 2.Report, 3.Alarm, 4.Mail")
    st.info("SMART (2.5jt): 5 Fitur")
    st.write("1.VCS, 2.Audit, 3.WA, 4.Dash, 5.Web")
    st.info("PRO (5jt): 6 Fitur")
    st.write("1.Forensik, 2.Aset, 3.Multi, 4-6.Full")

elif m == "Order":
    st.header("Order")
    with st.form("f"):
        n = st.text_input("Nama")
        u = st.text_input("Usaha")
        p = st.selectbox("Paket", ["BASIC", "SMART", "PRO"])
        st.file_uploader("Data")
        if st.form_submit_button("Kirim"):
            st.session_state.ord.append({"N":n,"U":u,"P":p})
            st.success("Sent!")

elif m == "Admin":
    if not st.session_state.ok:
        # Teks dipisah agar tidak terpotong
        txt_pass = "Security Code"
        pw = st.text_input(txt_pass, type="password")
        if st.button("Login"):
            if pw == "w1nbju8282":
                st.session_state.ok = True
                st.rerun()
    else:
        if st.button("Keluar"):
            st.session_state.ok = False
            st.rerun()
        st.error("🚨 FRAUD ALERT!")
        # Notif H-7
        td = datetime.now().date()
        for k in st.session_state.db:
            jt = datetime.strptime(k['Tempo'],"%Y-%m-%d").date()
            if (jt-td).days <= 7:
                st.warning("⚠️ H-7: " + k["Bisnis"])
        st.write("---")
        st.subheader("Order Masuk")
        st.table(pd.DataFrame(st.session_state.ord))
        st.subheader("Laba (60%)")
        om = sum([x['Harga'] for x in st.session_state.db])
        st.metric("Total", "Rp {:,.0f}".format(om))
        st.
