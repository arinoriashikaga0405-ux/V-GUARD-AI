import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# --- 1. INISIALISASI API & SESSION ---
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
ADMIN_PW = os.getenv("ADMIN_PASSWORD")

if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("⚠️ API KEY TIDAK DITEMUKAN! Pastikan file .env sudah benar.")

if 'menu' not in st.session_state:
    st.session_state.menu = "🏠 Visi & Misi"

# --- 2. CSS STANDAR VISUAL V-GUARD ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 8px; text-align: left; padding: 10px; border: 1px solid #e2e8f0; background: white; margin-bottom: 5px; font-weight: bold; }
    .main-slogan { text-align: center; font-size: 32px; font-weight: 800; color: #1e3a8a; margin: 20px 0; }
    .justified-text { text-align: justify; line-height: 1.8; font-size: 15px; color: #333; background: white; padding: 25px; border-radius: 12px; border: 1px solid #e2e8f0; }
    .roi-box { background: #1e3a8a; color: white; padding: 40px; border-radius: 15px; text-align: center; }
    .admin-box { background: #f0fdf4; border: 2px dashed #22c55e; color: #166534; padding: 30px; border-radius: 15px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD NAV")
    if st.button("🏠 Visi & Misi"): st.session_state.menu = "🏠 Visi & Misi"
    if st.button("📦 Produk & Layanan"): st.session_state.menu = "📦 Produk & Layanan"
    if st.button("📊 ROI (Dana Aman)"): st.session_state.menu = "📊 ROI (Dana Aman)"
    if st.button("📱 Portal Klien"): st.session_state.menu = "📱 Portal Klien"
    if st.button("⚙️ Admin Center"): st.session_state.menu = "⚙️ Admin Center"
    st.write("---")
    st.info(f"API Status: {'🟢 Terhubung' if api_key else '🔴 Diskonek'}")

# --- 4. LOGIKA DASHBOARD ---
if st.session_state.menu == "🏠 Visi & Misi":
    st.markdown('<div class="main-slogan">"Digitizing Trust, Eliminating Leakage"</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2.5])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.markdown('<div class="justified-text">', unsafe_allow_html=True)
        st.write("**VISI:** Menjadi Jangkar Kepercayaan Digital dan Standar Global Integritas Bisnis V-Guard AI Intelligence bervisi untuk menjadi pilar utama dalam ekosistem bisnis global yang mengedepankan transparansi mutlak.")
        st.write("**MISI:** Eliminasi Kebocoran Aset Melalui Edge Intelligence dan Perlindungan Siber Berlapis guna menjaga warisan bisnis klien selamanya.")
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.menu == "📊 ROI (Dana Aman)":
    st.subheader("📊 Kalkulator Proteksi Dana Klien")
    omzet = st.number_input("Omzet Bulanan Klien (Rp)", value=100000000)
    leak = st.slider("Estimasi Kebocoran (%)", 5, 40, 20)
    st.markdown(f'<div class="roi-box"><h2>Potensi Dana Aman: Rp {(omzet * leak/100):,.0f}</h2><p>Kebocoran dihentikan oleh sistem V-Guard AI</p></div>', unsafe_allow_html=True)

elif st.session_state.menu == "⚙️ Admin Center":
    st.subheader("⚙️ Executive Control")
    pw = st.text_input("Master Password", type="password")
    if pw == ADMIN_PW:
        api_raw = st.number_input("Input Biaya API Mentah (Rp)", value=5000000)
        api_net = api_raw * 0.8
        st.markdown(f"""<div class="admin-box"><p>🛡️ SOP EDGE FILTERING ACTIVE</p><h2>Biaya API Net: Rp {api_net:,.0f}</h2><p>Efisiensi Sistem (20%): Rp {api_raw * 0.2:,.0f}</p></div>""", unsafe_allow_html=True)
