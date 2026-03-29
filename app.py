import streamlit as st
import os
from PIL import Image

# 1. KONFIGURASI HALAMAN UTAMA (TERKUNCI)
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# INITIAL DATABASE & PAKET (SESUAI INSTRUKSI HARGA & MARKET)
if 'role' not in st.session_state: st.session_state.role = None
if 'user_name' not in st.session_state: st.session_state.user_name = "Visitor"
if 'user_id' not in st.session_state: st.session_state.user_id = None

# Definisi Paket V-Guard
if 'daftar_paket' not in st.session_state:
    st.session_state.daftar_paket = {
        "V-START": {"harga": 2500000, "fitur": "AI Scanner Dasar, Laporan Mingguan, 1 User Admin", "market": "UMKM / Toko Retail Kecil"},
        "V-GROW": {"harga": 5500000, "fitur": "AI Real-time Detection, Integrasi POS, Alarm Merah SMS/WA", "market": "Restoran / Cafe / Cabang Retail"},
        "V-PRIME": {"harga": 12500000, "fitur": "Audit Fraud Sistemik, Prediksi Kebocoran, Prioritas Support", "market": "Distributor / Gudang / Korporasi"}
    }

if 'db_klien' not in st.session_state:
    st.session_state.db_klien = {
        "klien_demo": {"paket": "V-GROW", "tagihan": 5500000, "due": "2026-04-05"}
    }

def get_foto(lebar):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try: return st.image(Image.open('erwin.jpg'), width=lebar)
        except: return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# 2. CSS STYLING (HITAM & EMAS - TERKUNCI)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .vguard-header { background: #0e1117; padding: 35px; border-radius: 12px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px; }
    .vguard-card { background-color: #0e1117; color: white; padding: 25px; border-radius: 15px; border-left: 10px solid #FFD700; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    h1, h2, h3 { color: white !important; }
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
        menu = st.radio("NAVIGASI:", ["🌐 Beranda", "👥 Management Klien", "🤖 AI Fraud Scanner"])
    elif st.session_state.role == "klien":
        menu = st.radio("NAVIGASI:", ["🌐 Beranda", "📅 Invoice & Payment"])
    else:
        menu = st.radio("NAVIGASI:", ["🌐 Beranda", "🔑 Masuk Ke Sistem"])

    if st.session_state.role and st.button("🚪 Logout"):
        st.session_state.role, st.session_state.user_name = None, "Visitor"
        st.rerun()

# 4. HALAMAN BERANDA (TAMPILAN PROFIL TETAP GAGAH)
if menu == "🌐 Beranda":
    st.markdown('<div class="vguard-header"><h1>V-GUARD AI SYSTEMS</h1><p style="color:#FFD700;">Mencegah Kerugian Owner Melalui Deteksi Proaktif</p></div>', unsafe_allow_html=True)
    
    col_foto, col_teks = st.columns([1.2, 1.8])
    with col_foto: get_foto(400)
    with col_teks:
        st.markdown(f"""
        <div class="vguard-card">
            <h2 style="color:#FFD700;">🛡️ About V-GUARD</h2>
            <p>Platform deteksi fraud sistemik yang dibangun oleh <b>Erwin Sinaga</b> (Senior Business Executive).</p>
            <p>Pengalaman perbankan 10+ tahun kami gunakan untuk memproteksi aset bisnis Anda dari kebocoran hingga 90%.</p>
            <hr style="border-color: #444;">
            <h3 style="color:#FFD700;">Filosofi</h3>
            <p>Kami memastikan setiap rupiah aset Anda terlindungi dengan standar keamanan tinggi dan audit AI proaktif.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    st.subheader("📦 Pilihan Paket Layanan")
    cols = st.columns(3)
    for i, (nama, d) in enumerate(st.session_state.daftar_paket.items()):
        with cols[i]:
            st.markdown(f"""
            <div style="background:#0e1117; color:white; padding:20px; border-radius:10px; border-top:4px solid #FFD700; height:2
