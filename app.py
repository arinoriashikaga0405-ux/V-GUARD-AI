import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. ENGINE AI ---
K_V = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=K_V)
    v_ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATA SESSION ---
if 'ord' not in st.session_state: st.session_state.ord = []
if 'db' not in st.session_state:
    t = datetime.now().date()
    st.session_state.db = [{"ID":101, "Nama":"Siska", "Bisnis":"Cafe Maju", "Paket":"SMART", "Harga":2500000, "Tempo":str(t + timedelta(days=5))}]
if 'ok' not in st.session_state: st.session_state.ok = False

# --- 3. PROFIL & VISI (SOP 150 KATA) ---
T_P = """Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel."""

# --- 4. SIDEBAR ---
st.sidebar.title("🛡️ V-GUARD AI")
if os.path.exists("erwin.jpg"): st.sidebar.image("erwin.jpg")
st.sidebar.markdown("**Erwin Sinaga**\nSenior Business Leader")
m = st.sidebar.radio("Navigasi Utama:", ["Profil Founder", "Visi & Misi", "ROI & Layanan", "Order Pelanggan", "Admin Panel"])
st.sidebar.write("---")
st.sidebar.caption("© 2026 V-Guard AI")

# --- 5. LOGIKA HALAMAN ---

if m == "Profil Founder":
    st.header("Leadership Profile")
    st.write(T_P)

elif m == "Visi & Misi":
    st.header("Visi & Misi Perusahaan")
    st.subheader("🛡️ Visi")
    st.info("Menjadi standar emas dunia dalam sistem audit real-time berbasis AI.")
    st.subheader("🚀 Misi")
    st.write("1. Transparansi Finansial\n2. Cegah Manipulasi\n3. Keamanan Aset\n4. Akuntabilitas")

elif m == "ROI & Layanan":
    st.header("ROI & 4 Paket Layanan")
    oz = st.number_input("Omzet (Rp):", value=100000000)
    bc = oz * 0.07
    st.error(f"Potensi Bocor (7%): Rp {bc:,.0f}")
    st.success(f"Save: Rp {bc - 2500000:,.0f}")
    st.write("---")
    st.info("**BASIC (1.5jt):** AI Monitor, Report, Alarm, Support (4 Fitur)")
    st.info("**SMART (2.5jt):** Basic+, VCS, Audit, WA, Dash (5 Fitur)")
    st.info("**PRO (5jt):** Smart+, Forensik, Aset, Multi, Consult (5 Fitur)")
    st.info("**ENTERPRISE (10jt):** Pro+, Custom AI, Onsite, 24/7, Risk, Insur (6 Fitur)")

elif m == "Order Pelanggan":
    st.header("Formulir Order VCS")
    o_nm = st.text_input("Nama Pelanggan")
    o_us = st.text_input("Nama Usaha")
    o_pk = st.selectbox("Pilih Paket", ["BASIC", "SMART", "PRO", "ENTERPRISE"])
    st.file_uploader("Upload Data")
    if st.button("Kirim Order"):
        st.session_state.ord.append({"Nama":o_nm, "Usaha":o_us, "Paket":o_pk})
        st.success("Order Terkirim!")

elif m == "Admin Panel":
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
            if (jt - td).days <= 7:
                st.warning(f"⚠️ INVOICE H-7: {k['Bisnis']}")
        
        st.write("---")
        st.subheader("➕ TAMBAH KLIEN (VCS)")
        a_n = st.text_input("Nama")
        a_b = st.text_input("Bisnis")
        a_h = st.number_input("Harga", value=2500000)
        a_t = st.date_input("Tempo")
        if st.button("Simpan Klien"):
            st.session_state.db.append({"ID":105, "Nama":a_n, "Bisnis":a_b, "Paket":"Manual", "Harga":a_h, "Tempo":str(a_t)})
            st.rerun()

        st.write("---")
        st.subheader("📊 DATABASE & LABA (60%)")
        st.table(pd.DataFrame(st.session_state.db))
        st.table(pd.DataFrame(st.session_state.ord))
        omzet = sum([x['Harga'] for x in st.session_state.db])
        st.success(f"Estimasi Laba Bersih: Rp {omzet * 0.6:,.0f}")
        
        st.write("---")
        st.subheader("🔍 AUDIT GEMINI")
        tx = st.text_area("Tempel Data:")
        if st.button("Run Audit AI"):
            rs = v_ai.generate_content("Analisis fraud: " + tx)
            st.write(rs.text)
