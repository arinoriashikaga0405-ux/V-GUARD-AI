import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. ENGINE AI (KEY BAPAK) ---
K_V = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=K_V)
    v_ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE ---
if 'db_ord' not in st.session_state: st.session_state.db_ord = []
if 'db_vcs' not in st.session_state:
    t = datetime.now().date()
    st.session_state.db_vcs = [{
        "ID": 101, "Nama": "Siska", "Bisnis": "Cafe Maju", 
        "Paket": "SMART", "Harga": 2500000, 
        "Tempo": str(t + timedelta(days=5))
    }]
if 'is_ad' not in st.session_state: st.session_state.is_ad = False

# --- 3. KONTEN SOP ---
PROFIL = """Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel."""

VISI = "Menjadi standar emas dunia dalam sistem audit real-time berbasis AI."
MISI = "1. Transparansi Finansial. 2. Cegah Manipulasi. 3. Proteksi Aset. 4. Akuntabilitas."

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
    st.markdown("**Erwin Sinaga**\nSenior Business Leader")
    st.write("---")
    m = st.radio("Navigasi:", ["Profil", "Visi Misi", "Layanan", "Order", "Admin"])
    st.write("---")
    st.caption("© 2026 V-Guard AI")

# --- 5. LOGIKA HALAMAN ---

if m == "Profil":
    st.header("Profil Founder")
    st.write(PROFIL)

elif m == "Visi Misi":
    st.header("Visi & Misi")
    st.info(VISI)
    st.write(MISI)

elif m == "Layanan":
    st.header("ROI & 4 Paket Layanan")
    oz = st.number_input("Omzet (Rp):", value=100000000)
    bc = oz * 0.07
    st.error(f"Potensi Bocor (7%): Rp {bc:,.0f}")
    st.success(f"Penyelamatan Aset: Rp {bc - 2500000:,.0f}")
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📦 BASIC (1.5jt)")
        st.write("AI Monitor, Report, Alarm, Support")
        st.subheader("🚀 SMART (2.5jt)")
        st.write("Basic+, VCS, Audit, WA, Dash")
    with c2:
        st.subheader("🛡️ PRO (5jt)")
        st.write("Smart+, Forensic, Konsul, Aset, Multi")
        st.subheader("👑 ENTERPRISE (10jt)")
        st.write("Pro+, Custom, Onsite, 24/7, Risk, Insur")

elif m == "Order":
    st.header("Formulir Order VCS")
    with st.form("f_ord"):
        n = st.text_input("Nama")
        u = st.text_input("Usaha")
        p = st.selectbox("Paket", ["BASIC", "SMART", "PRO", "ENTERPRISE"])
        st.file_uploader("Upload Data")
        if st.form_submit_button("KIRIM"):
            st.session_state.db_ord.append({"Nama":n, "Usaha":u, "Paket":p})
            st.success("Order Terkirim!")

elif m == "Admin":
    if not st.session_state.is_ad:
        pw = st.text_input("Security Code:", type="password")
        if st.button("Authorize"):
            if pw == "w1nbju8282":
                st.session_state.is_ad = True
                st.rerun()
    else:
        if st.button("🔒 Logout"):
            st.session_state.is_ad = False
            st.rerun()
        st.error("🚨 FRAUD ALERT DETECTED!")
        
        # Notif H-7
        td = datetime.now().date()
        for k in st.session_state.db_vcs:
            jt = datetime.strptime(k['Tempo'], "%Y-%m-%d").date()
            if (jt - td).days <= 7:
                st.warning(f"⚠️ INVOICE H-7: {k['Bisnis']}")

        t1, t2, t3, t4, t5 = st.tabs(["🛒 Order", "➕ Klien", "📊 VCS", "📈 Laba", "🔍 AI"])
        
        with t1:
            st.table(pd.DataFrame(st.session_state.db_ord))
        with t2:
            with st.form("f_add"):
                an, ab = st.text_input("Nama"), st.text_input("Bisnis")
                ah = st.number_input("Harga", value=2500000)
                at = st.date_input("Tempo")
                if st.form_submit_button("SIMPAN"):
                    st.session_state.db_vcs.append({"ID":105,"Nama":an,"Bisnis":ab,"Harga":ah,"Tempo":str(at)})
                    st.rerun()
        with t3:
            st.dataframe(pd.DataFrame(st.session_state.db_vcs))
