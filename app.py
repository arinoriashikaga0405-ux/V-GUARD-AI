import streamlit as st
import os
from PIL import Image

# 1. SETTING DASAR
st.set_page_config(page_title="V-GUARD AI", page_icon="🛡️", layout="wide")

# STATE MANAGEMENT
if 'role' not in st.session_state: st.session_state.role = None
if 'user_name' not in st.session_state: st.session_state.user_name = "Visitor"

def get_foto(lebar):
    url = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try: return st.image(Image.open('erwin.jpg'), width=lebar)
        except: return st.image(url, width=lebar)
    return st.image(url, width=lebar)

# 2. CSS STYLING (FIXED LAYOUT)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .banner { background: #0e1117; padding: 30px; border-radius: 12px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 25px; }
    .card { background: #0e1117; color: white; padding: 25px; border-radius: 15px; border-left: 8px solid #FFD700; box-shadow: 0 4px 10px rgba(0,0,0,0.2); }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (LOGIKA MENU PENDEK)
with st.sidebar:
    st.markdown("<h2 style='color:#FFD700;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(65)
    with c2: st.markdown(f"<b style='color:white;'>{st.session_state.user_name}</b>", unsafe_allow_html=True)
    st.divider()
    
    # Menu dibuat sangat pendek agar tidak terputus lagi
    opt = ["Beranda", "Login"]
    if st.session_state.role == "admin":
        opt = ["Beranda", "Klien", "Scanner"]
    
    menu = st.radio("NAVIGASI", opt)

    if st.session_state.role and st.button("Logout"):
        st.session_state.role, st.session_state.user_name = None, "Visitor"
        st.rerun()

# 4. HALAMAN BERANDA (PROFIL & FILOSOFI)
if menu == "Beranda":
    st.markdown('<div class="banner"><h1>V-GUARD AI SYSTEMS</h1><p style="color:#FFD700;">Mencegah Kerugian Owner Melalui Deteksi Proaktif</p></div>', unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1.2, 1.8])
    with col_l:
        get_foto(420)
    with col_r:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h2 style="color:#FFD700;">🛡️ About V-GUARD</h2>', unsafe_allow_html=True)
        st.write("Platform deteksi fraud sistemik oleh **Erwin Sinaga** (Senior Business Executive).")
        st.write("Pengalaman perbankan 10+ tahun untuk memproteksi aset bisnis Anda hingga 90%.")
        st.divider()
        st.markdown('<h3 style="color:#FFD700;">Filosofi</h3>', unsafe_allow_html=True)
        st.write("Kami memastikan setiap rupiah aset Anda terlindungi dengan standar keamanan tinggi.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.divider()
    st.subheader("📊 Kalkulator ROI")
    omset = st.number_input("Omset Bulanan (Rp):", value=100000000)
    st.metric("Potensi Aset Terselamatkan", f"Rp {omset * 0.027:,.0f}")

# 5. HALAMAN LOGIN
elif menu == "Login":
    st.title("🔑 Security Login")
    u = st.text_input("ID").lower().strip()
    p = st.text_input("Key", type="password")
    if st.button("Authenticate"):
        if u == "admin" and p == "Vguard2026":
            st.session_state.role, st.session_state.user_name = "admin", "Erwin Sinaga"
            st.rerun()
        else: st.error("Akses Ditolak.")

# 6. FITUR LAIN
elif menu == "Klien":
    st.title("👥 Management Klien")
elif menu == "Scanner":
    st.title("🤖 AI Scanner")
    st.file_uploader("Upload Data")
