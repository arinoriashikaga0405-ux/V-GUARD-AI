import streamlit as st
import os
from PIL import Image

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# INITIAL DATABASE
if 'role' not in st.session_state: st.session_state.role = None
if 'user_name' not in st.session_state: st.session_state.user_name = "Visitor"
if 'user_id' not in st.session_state: st.session_state.user_id = None
if 'db_klien' not in st.session_state:
    st.session_state.db_klien = {"klien_demo": {"paket": "V-LITE", "tagihan": 7500000}}

def get_foto(lebar):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try: return st.image(Image.open('erwin.jpg'), width=lebar)
        except: return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# 2. CSS STYLING (BLACK & GOLD)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .hero-bg { background: #0e1117; padding: 40px; border-radius: 12px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px; }
    .bio-section { background: #0e1117; color: white; padding: 30px; border-radius: 15px; border-left: 8px solid #FFD700; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='color:#FFD700;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(65)
    with c2: st.markdown(f"<b style='color:white;'>{st.session_state.user_name}</b>", unsafe_allow_html=True)
    st.divider()
    
    if st.session_state.role == "admin":
        menu = st.radio("MENU:", ["🌐 Beranda", "👥 Klien", "🤖 Scanner"])
    elif st.session_state.role == "klien":
        menu = st.radio("MENU:", ["🌐 Beranda", "📅 Tagihan"])
    else:
        menu = st.radio("MENU:", ["🌐 Beranda", "🔑 Login"])

    if st.session_state.role and st.button("🚪 Logout"):
        st.session_state.role, st.session_state.user_name = None, "Visitor"
        st.rerun()

# 4. HALAMAN BERANDA
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p style="color:#FFD700;">Mencegah Kerugian Owner Melalui Deteksi Proaktif</p></div>', unsafe_allow_html=True)
    col_f, col_t = st.columns([1.2, 1.8])
    with col_f: get_foto(400)
    with col_t:
        st.markdown('<div class="bio-section">', unsafe_allow_html=True)
        st.markdown('<h2 style="color:#FFD700;">🛡️ About V-GUARD</h2>', unsafe_allow_html=True)
        st.write("Platform deteksi fraud sistemik yang dibangun oleh **Erwin Sinaga** (Senior Business Executive). Pengalaman perbankan 10+ tahun kami gunakan untuk memproteksi aset bisnis Anda dari kebocoran hingga 90%.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.divider()
    st.subheader("📊 Kalkulator ROI Fraud")
    omset = st.number_input("Omset Bulanan Bisnis (Rp):", value=100000000)
    st.metric("Potensi Aset Terselamatkan /Bulan", f"Rp {omset * 0.027:,.0f}")

# 5. HALAMAN LOGIN
elif menu == "🔑 Login":
    st.title("🔑 Security Login")
    u = st.text_input("User ID").lower().strip()
    p = st.text_input("Access Key", type="password")
    if st.button("AUTHENTICATE"):
        if u == "admin" and p == "Vguard2026":
            st.session_state.role, st.session_state.user_name = "admin", "Erwin
