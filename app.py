import streamlit as st
import os
from PIL import Image

# 1. KONFIGURASI UTAMA (LOCKED)
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# DATA PAKET (STRUKTUR BIAYA BARU)
# V-START: 2.5jt Pasang + 1jt Bulanan
# V-GROW: 5jt Pasang + 2.5jt Bulanan
# V-PRIME: 10jt Pasang + 5jt Bulanan
pk = {
    "V-START": {"psg": 2500000, "bln": 1000000, "ftr": "AI Scanner Dasar, Laporan Mingguan", "mkt": "UMKM / Retail"},
    "V-GROW": {"psg": 5000000, "bln": 2500000, "ftr": "AI Real-time, Integrasi POS, Alarm WA", "mkt": "Restoran / Cafe"},
    "V-PRIME": {"psg": 10000000, "bln": 5000000, "ftr": "Audit Fraud Sistemik, Prioritas Support", "mkt": "Korporasi / Gudang"}
}

if 'role' not in st.session_state: st.session_state.role = None
if 'user_name' not in st.session_state: st.session_state.user_name = "Visitor"

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
    .p-card { background:#0e1117; color:white; padding:20px; border-radius:10px; border-top:4px solid #FFD700; min-height:320px; text-align:center; }
    .fee-tag { color: #FFD700; font-weight: bold; font-size: 0.9em; }
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
    
    menu = st.radio("NAVIGASI", m_list)
    if st.session_state.role and st.button("Logout"):
        st.session_state.role, st.session_state.user_name = None, "Visitor"
        st.rerun()

# 4. HALAMAN BERANDA (PROFIL & STRUKTUR BIAYA BARU)
if menu == "Beranda":
    st.markdown('<div class="v-head"><h1>V-GUARD AI SYSTEMS</h1><p style="color:#FFD700;">Solusi Proteksi Aset Bisnis Terpercaya</p></div>', unsafe_allow_html=True)
    
    col_foto, col_teks = st.columns([1.2, 1.8])
    with col_foto: get_foto(400)
    with col_teks:
        st.markdown('<div class="v-card"><h2 style="color:#FFD700;">🛡️ About V-GUARD</h2><p>Dikembangkan oleh <b>Erwin Sinaga</b>, pakar strategi bisnis dengan pengalaman perbankan 10+ tahun. Kami mendeteksi kebocoran sebelum menjadi kerugian permanen.</p><hr style="border-color:#444;"><h3 style="color:#FFD700;">Filosofi Keamanan</h3><p>Proteksi 24/7 dengan sistem AI yang terus belajar dari setiap pola transaksi di bisnis Anda.</p></div>', unsafe_allow_html=True)
    
    st.divider()
    st.subheader("📦 Paket Investasi Sistem")
    cols = st.columns(3)
    for i, (nama, d) in enumerate(pk.items()):
        with cols[i]:
            st.markdown(f"""
            <div class="p-card">
                <h3 style="color:#FFD700;">{nama}</h3>
                <p class="fee-tag">Biaya Pemasangan: Rp {d['psg']:,}</p>
                <h2 style="margin:10px 0;">Rp {d['bln']:,}<span style="font-size:0.4em; color:#aaa;">/bulan</span></h2>
                <p style="font-size:0.85em; color:#ddd; min-height:60px;">{d['ftr']}</p>
                <p style="font-size:0.8em; color:#FFD700; border-top:1px solid #333; padding-top:10px;"><i>Target: {d['mkt']}</i></p>
            </div>
            """, unsafe_allow_html=True)

# 5. LOGIN
elif menu == "Login":
    st.markdown('<div class="v-head"><h1>SECURITY LOGIN</h1></div>', unsafe_allow_html=True)
    u = st.text_input("User ID").lower().strip()
    p = st.text_input("Access Key", type="password")
    if st.button("Masuk"):
        if u == "admin" and p == "Vguard2026":
            st.session_state.role, st.session_state.user_name = "admin", "Erwin Sinaga"
            st.rerun()
        else: st.error("Akses Ditolak.")

elif menu == "Management": st.title("👥 Management Klien")
elif menu == "Scanner": st.title("🤖 AI Fraud Scanner")
