import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. LABEL PROTECTOR (ANTI-POTONG) ---
L_PR = "1. Profil Founder"
L_VS = "2. Visi, Misi & ROI"
L_PK = "3. Paket Unggulan"
L_RG = "4. Registrasi & Upload"
L_OP = "5. Operasional & Audit"
B_KRM = "KIRIM DATA"
B_SMP = "SIMPAN"
B_RUN = "JALANKAN AI"
B_OUT = "🔒 LOGOUT"
B_LOG = "AUTHORIZE"

# --- 2. ENGINE AI ---
K_V = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=K_V)
    v_ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 3. DATABASE ---
if 'db_o' not in st.session_state: st.session_state.db_o = []
if 'db_n' not in st.session_state:
    t = datetime.now().date()
    st.session_state.db_n = [{
        "ID": 101, "Nama": "Siska", "Bisnis": "Cafe Maju", 
        "Paket": "SMART", "Harga": 2500000, 
        "Tempo": str(t + timedelta(days=5))
    }]
if 'is_ad' not in st.session_state: st.session_state.is_ad = False

# --- 4. KONTEN SOP (150 KATA) ---
T_P = """Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel."""

# --- 5. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
    st.markdown("**Erwin Sinaga**\nSenior Business Leader")
    st.write("---")
    m = st.radio("Navigasi Utama:", [L_PR, L_VS, L_PK, L_RG, L_OP])
    st.write("---")
    st.caption("© 2026 V-Guard AI")

# --- 6. HALAMAN ---
if m == L_PR:
    st.header("Profil Kepemimpinan")
    st.write(T_P)

elif m == L_VS:
    st.header("Visi, Misi & ROI")
    st.info("**Visi:** Menjadi standar emas dunia dalam audit AI.")
    st.write("**Misi:** Transparansi, Proteksi, Akuntabilitas.")
    st.write("---")
    oz = st.number_input("Omzet (Rp):", value=100000000)
    bc = oz * 0.07
    st.error(f"Potensi Bocor (7%): Rp {bc:,.0f}")
    st.success(f"Penyelamatan Aset: Rp {bc - 2500000:,.0f}")

elif m == L_PK:
    st.header("4 Produk Layanan")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📦 BASIC (1.5jt)")
        st.write("AI, Report, Alarm, Support")
        st.subheader("🚀 SMART (2.5jt)")
        st.write("Basic+, VCS, Audit, WA, Dash")
    with c2:
        st.subheader("🛡️ PRO (5jt)")
        st.write("Smart+, Forensic, Konsul, Aset")
        st.subheader("👑 ENTERPRISE (10jt)")
        st.write("Pro+, Custom, Onsite, Fraud Ins.")

elif m == L_RG:
    st.header("Registrasi Klien VCS")
    with st.form("f_reg"):
        n, u = st.text_input("Nama"), st.text_input("Usaha")
        p = st.selectbox("Paket", ["BASIC", "SMART", "PRO", "ENTERPRISE"])
        if st.form_submit_button(B_KRM):
            st.session_state.db_o.append({"Nama":n, "Usaha":u, "Paket":p})
            st.success("Terkirim!")

elif m == L_OP:
    if not st.session_state.is_ad:
        pw = st.text_input("Security Code:", type="password")
        if st.button(B_LOG):
            if pw == "w1nbju8282":
                st.session_state.is_ad = True
                st.rerun()
    else:
        if st.button(B_OUT):
            st.session_state.is_ad = False
            st.rerun
