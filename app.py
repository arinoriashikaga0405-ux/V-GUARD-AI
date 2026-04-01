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

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE SESSION ---
if 'db_order' not in st.session_state:
    st.session_state.db_order = []
if 'db_vcs' not in st.session_state:
    t = datetime.now().date()
    st.session_state.db_vcs = [{
        "ID": 101, "Nama": "Siska", "Bisnis": "Cafe Maju", 
        "Paket": "SMART", "Harga": 2500000, 
        "Tempo": str(t + timedelta(days=5))
    }]
if 'is_admin' not in st.session_state:
    st.session_state.is_admin = False

# --- 3. CSS CUSTOM ---
st.markdown("""
<style>
    .main { background-color: #f5f7f9; }
    .alarm { background: #ff4b4b; color: white; padding: 20px; border-radius: 10px; text-align: center; font-weight: bold; border: 3px solid yellow; }
    .notif { background: #fff3cd; padding: 15px; border-radius: 8px; border-left: 10px solid #ffc107; margin-bottom: 10px; color: black; }
    .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI")
    else:
        st.warning("Unggah file 'erwin.jpg' ke GitHub Bapak.")
    st.markdown("### **Erwin Sinaga**\n*Senior Business Leader*")
    st.write("---")
    m = st.radio("Intelligence Navigasi:", 
                 ["Profil Founder", "Visi & Misi", "ROI & Layanan", "Order Pelanggan", "Admin Panel"])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- 5. LOGIKA HALAMAN ---

# --- PROFIL ---
if m == "Profil Founder":
    st.header("Leadership Profile")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
        else: st.info("Foto Founder")
    with col2:
        st.write("""Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 
        
        Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel.""")

# --- VISI & MISI ---
elif m == "Visi & Misi":
    st.header("Visi & Misi Perusahaan")
    st.subheader("🛡️ Visi")
    st.info("Menjadi standar emas dunia dalam sistem audit real-time berbasis AI untuk menjamin keamanan aset bisnis secara absolut.")
    st.subheader("🚀 Misi")
    st.write("1. Menciptakan transparansi finansial melalui teknologi AI.")
    st.write("2. Mencegah manipulasi data dan kebocoran modal sejak dini.")
    st.write("3. Memberikan rasa aman bagi pengusaha dalam mengelola operasional.")
    st.write("4. Membangun ekosistem bisnis yang bersih dan akuntabel.")

# --- ROI & LAYANAN ---
elif m == "ROI & Layanan":
    st.header("ROI Analysis & Produk Layanan")
    oz = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    bc = oz * 0.07
    st.error(f"Potensi Kebocoran (7%): Rp {bc:,.0f}")
    st.success(f"Penyelamatan Aset: Rp {bc - 2500000:,.0f}")
    st.write("---")
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.markdown("**BASIC (1.5jt)**\n- AI Monitor\n- Report Mingguan\n- Alarm Dasar\n- Email Support")
    with p2:
        st.markdown("**SMART (2.5jt)**\n- Fitur Basic\n- VCS System\n- Audit Realtime\n- Notif WA\n- Dashboard")
    with p3:
        st.markdown("**PRO (5jt)**\n- Fitur Smart\n- Digital Forensic\n- Konsultasi Strategis\n- Proteksi Aset\n- Multi-User")
    with
