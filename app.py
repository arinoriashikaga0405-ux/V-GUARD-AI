import streamlit as st
import os
from PIL import Image

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# INITIAL DATABASE
if 'role' not in st.session_state:
    st.session_state.role = None
if 'user_name' not in st.session_state:
    st.session_state.user_name = "Visitor"
if 'user_id' not in st.session_state:
    st.session_state.user_id = None
if 'db_klien' not in st.session_state:
    st.session_state.db_klien = {
        "klien_demo": {"paket": "V-LITE", "tagihan": 7500000, "due": "2026-04-05"}
    }

def get_foto(lebar):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try:
            return st.image(Image.open('erwin.jpg'), width=lebar)
        except:
            return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# 2. CSS STYLING (MENGIKUTI SCREENSHOT)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .hero-bg { background: #0e1117; padding: 40px; border-radius: 12px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px; }
    .bio-section { background: #0e1117; color: white; padding: 30px; border-radius: 15px; border-left: 8px solid #FFD700; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    h1, h2, h3 { color: white; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1:
        get_foto(65)
    with c2:
        st.markdown(f"<b style='color:white;'>{st.session_state.user_name}</b>", unsafe_allow_html=True)
        st.markdown("<small style='color:#FFD700;'>V-GUARD Ecosystem</small>", unsafe_allow_html=True)
    st.divider()
    
    if st.session_state.role == "admin":
        menu = st.radio("FOUNDER MENU:",
