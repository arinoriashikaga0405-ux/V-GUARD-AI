import streamlit as st
import os
from PIL import Image

# 1. KONFIGURASI UTAMA (LOCKED)
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# DATA PAKET & DATABASE (Sesuai Instruksi Harga & Market)
if 'role' not in st.session_state: st.session_state.role = None
if 'user_name' not in st.session_state: st.session_state.user_name = "Visitor"

pk = {
    "V-START": {"hrga": 2500000, "ftr": "AI Scanner Dasar, Laporan Mingguan", "mkt": "UMKM / Retail Kecil"},
    "V-GROW": {"hrga": 5500000, "ftr": "AI Real-time, Integrasi POS, Alarm WA", "mkt": "Restoran / Cafe"},
    "V-PRIME": {"hrga": 12500000, "ftr": "Audit Fraud Sistemik, Prioritas Support", "mkt": "Gudang / Korporasi"}
}

def get_foto(w):
    path, url = 'erwin.jpg', "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists(path):
        try: return st.image(Image.open(path), width=w)
        except: return st.image(url, width=w)
    return st.image(url, width=w)

# 2. CSS STYLE (BLACK & GOLD - PRESTISIUS)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid='stSidebar'] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .v-head { background: #0e1117; padding: 35px; border-radius: 12px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px; }
    .v-card { background: #0e1117; color: white; padding: 25px; border-radius: 15px; border-left: 10px solid #FFD700; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    .p-card { background:#0e1117; color:white; padding:20px; border-radius:10px; border-top:4px solid #FFD700; min-height:280px; }
    h1, h2, h3 { color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (FOUNDER - CEO EDITION)
with st.sidebar:
    st.markdown("<h2 style='color:#FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(65)
    with c2: 
        st.markdown(f"<b style='color:white; font-size:1.1em;'>{st.session_state.user_name}</b>", unsafe_allow_html=True)
        st.markdown("<div style='color:#FFD700; font-size:0.8em; font-weight:bold;'>FOUNDER - CEO</div>", unsafe_allow_html=True)
    st.divider()
    
    m_list = ["Beranda", "Login"]
    if st.session_state.role == "admin": m_list = ["Beranda", "Management", "Scanner"]
    elif st.session_state.role == "klien": m_list = ["Beranda", "Tagihan"]
    
    menu = st.radio("NAVIGASI", m_list)
    if st.session_state.role and st.button("Logout"):
        st.session_state.role, st.session_state.user_name = None, "Visitor"
        st.rerun()

# 4. HALAMAN BERANDA (PROFIL & PAKET KEMBALI MUNCUL)
if menu == "Beranda":
    st.markdown('<div class="v-head"><h1>V-GUARD AI SYSTEMS</h1><p style="color:#FFD700;">Mencegah Kerugian Owner Melalui Deteksi Proaktif</p></div>', unsafe_allow_html=True)
    
    col_foto, col_teks = st.columns([1.2, 1.8])
    with col_foto: get_foto(400)
    with col_teks:
        st.markdown('<div class="v-card"><h2 style="color:#FFD700;">🛡️ About V-GUARD</h2><p>Platform deteksi fraud sistemik oleh <b>Erwin Sinaga</b> (Senior Business Executive).</p><p>Pengalaman perbankan 10+ tahun kami gunakan untuk memproteksi aset bisnis Anda hingga 90%.</p><hr style="border-color:#444;"><h3 style="color:#FFD700;">Filosofi</h3><p>Kami memastikan setiap rupiah aset Anda terlindungi dengan standar keamanan tinggi dan audit AI proaktif.</p></div>', unsafe_allow_html=True)
    
    st.divider()
    st.subheader("📦 Pilihan Paket Layanan")
    cols = st.columns(3)
    for i, (nama, d) in enumerate(pk.items()):
        with cols[i]:
            st.markdown(f'<div class="p-card"><h3 style="color:#FFD700;">{nama}</h3><p><b>Rp {d["hrga"]:,}</b></p><p style="font-size:0.85em;">{d["ftr"]}</p><p style="font-size:0.8em; color:#FFD700;"><i>Market: {d["mkt"]}</i></p></div>', unsafe_allow_html=True)

# 5. HALAMAN LOGIN
elif menu == "Login":
    st.markdown('<div class="v-head"><h1>SECURITY LOGIN</h1></div>', unsafe_allow_html=True)
    u = st.text_input("User ID").lower().strip()
    p = st.text_input("Access Key", type="password")
    if st.button("Masuk"):
        if u == "admin" and p == "Vguard2026":
            st.session_state.role, st.session_state.user_name = "admin", "Erwin Sinaga"
            st.rerun()
        else: st.error("Akses Ditolak.")

# FITUR ADMIN (MANAGEMENT & SCANNER)
elif menu == "Management": st.title("👥 Management Klien")
elif menu == "Scanner": st.title("🤖 AI Fraud Scanner")
