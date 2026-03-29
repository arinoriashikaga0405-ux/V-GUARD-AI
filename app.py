import streamlit as st
import os
from PIL import Image

# ==========================================
# 1. KONFIGURASI HALAMAN UTAMA (WAJIB PERTAMA)
# ==========================================
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# INITIAL DATABASE SIMULATION
if 'role' not in st.session_state: st.session_state.role = None
if 'user_name' not in st.session_state: st.session_state.user_name = "Visitor"
if 'user_id' not in st.session_state: st.session_state.user_id = None
if 'db_klien' not in st.session_state:
    st.session_state.db_klien = {
        "klien_demo": {"paket": "V-LITE", "tagihan": 7500000, "due": "2026-04-05"}
    }

# FUNGSI FOTO PROFIL (SELALU PRIORITASKAN FOTO BAPAK)
def get_foto(lebar, caption=None):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try: 
            img = Image.open('erwin.jpg')
            return st.image(img, width=lebar, caption=caption)
        except: return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# ==========================================
# 2. CSS STYLING PRESTISIUS (BLACK & GOLD)
# ==========================================
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .hero-bg { background-color: #0e1117; padding: 40px; border-radius: 12px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    .hero-bg h1 { color: white; font-size: 3em; margin-bottom: 10px; }
    .hero-bg p { color: #FFD700; font-size: 1.2em; }
    .bio-section { background-color: #0e1117; color: white; padding: 30px; border-radius: 15px; border-left: 8px solid #FFD700; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    .red-alert { background-color: #ff4b4b; color: white; padding: 20px; border-radius: 10px; border: 3px solid black; text-align: center; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0.3; } }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. SIDEBAR NAVIGATION
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    f_col, n_col = st.columns([1, 2])
    with f_col:
        get_foto(70) # Foto profil kecil
    with n_col: 
        st.markdown(f"<b style='color:white; font-size: 1.2em;'>{st.session_state.user_name}</b><br><small style='color:#FFD700;'>V-GUARD Ecosystem</small>", unsafe_allow_html=True)
    st.divider()
    
    # Navigasi Dinamis
    if st.session_state.role == "admin":
        menu = st.radio("FOUNDER MENU
