import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. SETUP ---
KEY = "GANTI_DENGAN_API_KEY_BAPAK"
try:
    genai.configure(api_key=KEY)
    ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI")

# --- 2. CSS ---
st.markdown("""
<style>
    .alarm { background: #ff4b4b; color: white; padding: 15px; text-align: center; font-weight: bold; }
    .notif { background: #fff3cd; padding: 10px; border-left: 5px solid #ffc107; }
</style>
""", unsafe_allow_html=True)

# --- 3. DATABASE ---
if 'db' not in st.session_state:
    skrg = datetime.now().date()
    st.session_state.db = [{
        "ID": 101, "Bisnis": "Cafe Maju", 
        "Harga": 2500000, 
        "Tempo": str(skrg + timedelta(days=5))
    }]

if 'log' not in st.session_state:
    st.session_state.log = False

# --- 4. PROFIL (SOP) ---
T_PRO = """Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel."""

# --- 5. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.write("**Erwin Sinaga**")
    st.write("---")
    m = st.radio("Intelligence Menu:", ["Profil", "ROI Engine", "Control"])
    st.write("---")
    st.caption("© 2026 V-Guard AI")

# --- 6. LOGIKA ---
if m == "Profil":
    st.header("Profil Founder")
    st.write(T_PRO)

elif m == "ROI Engine":
    st.header("V-Guard ROI Analysis")
    oz = st.number_input("Omzet:", value=100000000)
    bc = oz * 0.07
    sv = bc - 2500000
    # Pecah baris agar tidak terpotong
    t_bc = "Bocor (7%):"
    v_bc = "Rp " + str(bc)
    st.error(t_bc + " " + v_bc)
    t_sv = "Save via V-Guard:"
    v_sv = "Rp " + str(sv)
    st.success(t_sv + " " + v_sv)

elif m == "Control":
    if not st.session_state.log:
        p = st.text_input("Security Code:", type="password")
        if st.button("Authorize"):
            if p == "w1nbju8282":
                st.session_state.log = True
                st.rerun()
    else:
        if st.button("🔒 Logout"):
            st.session_state.log = False
            st.rerun()
        
        st.markdown('<div class="alarm">🚨 FRAUD ALERT!</div>', unsafe_allow_html=True)
        
        # Notif H-7
        tday = datetime.now().date()
        for k in st.session_state.db:
            d_jt = datetime.strptime(k['Tempo'], "%Y-%m-%d").date()
            if (d_jt - tday).days <= 7:
                msg = "⚠️ TEMPO: " + k["Bisnis"]
                st
