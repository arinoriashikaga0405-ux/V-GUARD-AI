import streamlit as st
import os
from PIL import Image

# 1. KONFIGURASI HALAMAN UTAMA (TERKUNCI)
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# INITIAL DATABASE & PAKET (HARGA & MARKET TETAP)
if 'role' not in st.session_state: st.session_state.role = None
if 'user_name' not in st.session_state: st.session_state.user_name = "Visitor"
if 'user_id' not in st.session_state: st.session_state.user_id = None

# Definisi Paket V-Guard (Sesuai Instruksi Bapak)
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
    
    # Navigasi Menu
    if st.session_state.role == "admin":
        menu = st.radio("NAVIGASI:", ["🌐 Beranda", "👥 Management Klien", "🤖 AI Fraud Scanner"])
    elif st.session_state.role == "klien":
        menu = st.radio("NAVIGASI:", ["🌐 Beranda", "📅 Invoice & Payment"])
