import streamlit as st
import os
from PIL import Image

# 1. SETUP HALAMAN
st.set_page_config(page_title="V-GUARD AI", page_icon="🛡️", layout="wide")

# DATA AWAL
if 'role' not in st.session_state:
    st.session_state.role = None
if 'user_name' not in st.session_state:
    st.session_state.user_name = "Visitor"

def get_foto(lebar):
    url = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try: return st.image(Image.open('erwin.jpg'), width=lebar)
        except: return st.image(url, width=lebar)
    return st.image(url, width=lebar)

# 2. CSS SEDERHANA (TETAP BLACK & GOLD)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .hero { background: #0e1117; padding: 30px; border-radius: 12px; color: white; text-align: center; border-bottom: 5px solid #FFD700; }
    .box { background: #0e1117; color: white; padding: 25px; border-radius: 15px; border-left: 8px solid #FFD700; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color:#FFD700;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    get_foto(80)
    st.markdown(f"<b style='color:white;'>{st.session_state.user_name}</b>", unsafe_allow_html=True)
    st.divider()
    
    if st.session_state.role == "admin":
        m = st.radio("MENU:", ["Beranda", "Klien", "Scanner"])
    else:
        m = st.radio("MENU:", ["Beranda", "Login"])

    if st.session_state.role and st.button("Logout"):
        st.session_state.role, st.session_state.user_name = None, "Visitor"
        st.rerun()

# 4. HALAMAN UTAMA (PROFIL & FILOSOFI)
if m == "Beranda":
    st.markdown('<div class="hero"><h1>V-GUARD AI SYSTEMS</h1><p style="color:#FFD700;">Mencegah Kerugian Owner</p></div>', unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1, 2])
    with col_l:
        get_foto(350)
    with col_r:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.subheader("🛡️ About V-GUARD")
        st.write("Dibangun oleh **Erwin Sinaga** (Senior Business Executive).")
        st.write("Pengalaman perbankan 10+ tahun untuk proteksi aset bisnis Anda hingga 90%.")
        st.divider()
        st.subheader("Filosofi")
        st.write("Kami memastikan setiap rupiah aset Anda terlindungi dengan standar tinggi.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.divider()
    omset = st.number_input("Omset (Rp):", value=100000000)
    st.metric("Aset Terselamatkan", f"Rp {omset * 0.027:,.0f}")

# 5. LOGIN SYSTEM
elif m == "Login":
    st.title("🔑 Login")
    u = st.text_input("User ID").lower().strip()
    p = st.text_input("Key", type="password")
    if st.button("Masuk"):
        if u == "admin" and p == "Vguard2026":
            st.session_state.role, st.session_state.user_name = "admin", "Erwin Sinaga"
            st.rerun()
        else:
            st.error("Gagal.")

# 6. FITUR ADMIN
elif m == "Klien":
    st.title("👥 Management")
    st.write("Fitur admin aktif.")

elif m == "Scanner":
    st.title("🤖 AI Scanner")
    st.file_uploader("Upload Data")
