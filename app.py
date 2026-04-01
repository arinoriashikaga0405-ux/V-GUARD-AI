import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. CORE CONFIG ---
K_V = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=K_V)
    v_ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI")

# --- 2. DATABASE ---
if 'ord' not in st.session_state: st.session_state.ord = []
if 'db' not in st.session_state:
    t = datetime.now().date()
    j = str(t + timedelta(days=5))
    st.session_state.db = [{"ID":101, "Bisnis":"Cafe Maju", "Harga":2500000, "Tempo":j}]
if 'ok' not in st.session_state: st.session_state.ok = False

# --- 3. KONTEN SOP (150 KATA) ---
T_P = """Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel."""

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
    st.write("**Erwin Sinaga**")
    m = st.radio("Pilih Menu:", ["Profil", "ROI & Paket", "Order", "Admin"])

# --- 5. LOGIKA HALAMAN ---
if m == "Profil":
    st.header("Profil Founder")
    st.write(T_P)

elif m == "ROI & Paket":
    st.header("ROI & 4 Paket Layanan")
    oz = st.number_input("Omzet (Rp):", 100000000)
    bc = oz * 0.07
    st.error("Potensi Bocor (7%): Rp {:,.0f}".format(bc))
    st.success("Save: Rp {:,.0f}".format(bc-2500000))
    st.write("---")
    st.info("BASIC (1.5jt): AI Monitor, Report, Alarm, Support (4 Fitur)")
    st.info("SMART (2.5jt): Basic+, VCS, Audit, WA, Dash (5 Fitur)")
    st.info("PRO (5jt): Smart+, Forensik, Aset, Multi, Consult (5 Fitur)")
    st.info("ENTERPRISE (10jt): Pro+, Custom, Onsite, 24/7, Risk, Insur (6 Fitur)")

elif m == "Order":
    st.header("Formulir Order VCS")
    with st.form("f"):
        nm = st.text_input("Nama Anda")
        us = st.text_input("Nama Usaha")
        pk = st.selectbox("Paket", ["BASIC", "SMART", "PRO", "ENTERPRISE"])
        st.file_uploader("Upload Data Pelanggan")
        if st.form_submit_button("Kirim Order"):
            st.session_state.ord.append({"N":nm, "U":us, "P":pk})
            st.success("Order Terkirim ke Admin!")

elif m == "Admin":
    if not st.session_state.ok:
        pw = st.text_input("Security Code:", type="password")
        if st.button("Authorize"):
            if pw == "w1nbju8282":
                st.session_state.ok = True
                st.rerun()
    else:
        if st.button("🔒 Logout"):
            st.session_state.ok = False
            st.rerun()
        st.error("🚨 FRAUD ALERT DETECTED!")
        # Notif H-7
        td = datetime.now().date()
        for k in st.session_state.db:
            jt = datetime.strptime(k['Tempo'], "%Y-%m-%d").date()
            if (jt-td).days <= 7:
                st.warning("⚠️ INVOICE H-7: " + k["Bisnis"])
        st.write("---")
        st.write("**🛒 ORDER MASUK:**")
        st.table(pd.DataFrame(st.session_state.ord))
        st.write("**📊 DATABASE VCS:**")
        st.table(pd.DataFrame(st.session_state.db))
        st.write("**📈 LABA (60%):**")
        om = sum([x['Harga'] for x in st.session_state.db])
        st.success("Laba: Rp {:,.0f}".format(om*0.6))
        st.write("---")
        st.write("**🔍 AUDIT GEMINI:**")
        tx = st.text_area("Tempel Data:")
        if st.button("Run Audit AI"):
            rs = v_ai.generate_content("Audit fraud: " + tx)
            st.write(rs.text)

st.caption("© 2026 V-Guard AI | Secured by Erwin Sinaga")
