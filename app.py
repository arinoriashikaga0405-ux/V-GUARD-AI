import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

# --- 1. KEAMANAN TINGKAT TINGGI ---
# Mengambil API Key dari file .env (Sangat Aman)
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "w1nbju8282")

if API_KEY:
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Koneksi AI Gagal: {e}")
else:
    st.warning("⚠️ API Key tidak ditemukan di sistem keamanan (.env).")

# --- 2. KONFIGURASI TAMPILAN (SESUAI SCREENSHOT) ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .justified-text { text-align: justify; line-height: 1.6; font-size: 15px; }
    .product-card { 
        border: 1px solid #e2e8f0; border-radius: 15px; padding: 20px; 
        text-align: center; height: 560px; background: #fff; 
        box-shadow: 0 2px 10px rgba(0,0,0,0.05); 
    }
    .product-title { color: #1e3a8a; font-weight: bold; font-size: 20px; }
    .target-text { color: #d63384; font-size: 13px; font-weight: bold; margin-bottom: 15px; }
    .feature-list { text-align: left; font-size: 13px; min-height: 200px; line-height: 1.8; color: #444; }
    .price-box { margin-top: 15px; padding: 10px; border-radius: 10px; background: #f8fafc; }
    .section-title { color: #1e3a8a; font-weight: bold; font-size: 18px; border-bottom: 2px solid #f1f5f9; padding-bottom: 10px; margin-top: 30px; }
    </style>
    """, unsafe_allow_html=True)

# Fungsi Proteksi Gambar
def safe_image(path):
    if os.path.exists(path):
        try:
            st.image(Image.open(path), use_container_width=True)
        except: st.info("👤 Foto Error")
    else: st.info("👤 Foto Tidak Ada")

# --- 3. ISI UTAMA ---
col_f, col_v = st.columns([1, 2.5])
with col_f:
    safe_image("erwin.jpg")
with col_v:
    st.markdown('<div class="justified-text">', unsafe_allow_html=True)
    st.write("""
    **Visi: Menjadi Jangkar Kepercayaan Digital dan Standar Global Integritas Bisnis** V-Guard AI Intelligence bervisi menciptakan ekosistem bisnis global yang sepenuhnya transparan, aman, dan berintegritas tinggi melalui inovasi teknologi kecerdasan buatan terdepan.
    
    **Misi: Eliminasi Kebocoran Aset Melalui Edge Intelligence** Misi kami adalah memberikan perlindungan aset yang tak tertembus melalui penerapan teknologi Edge Filtering yang mutakhir untuk membangun infrastruktur integritas digital.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# LAYANAN (5 KOLOM)
st.markdown('<div class="section-title">🏷️ PRODUK & LAYANAN STRATEGIS</div>', unsafe_allow_html=True)
pkgs = {
    "V-LITE": {"t": "Mikro / 1 Kasir", "f": ["Anomali Filter Lokal", "WA Summary", "Cloud Secure"], "a": "1.5 Jt", "b": "750 rb"},
    "V-PRO": {"t": "Retail & Kafe", "f": ["VCS Integration", "Fraud-Only Upload", "Bank Audit Link"], "a": "3 Jt", "b": "1.5 Jt"},
    "V-SIGHT": {"t": "Gudang & Toko", "f": ["CCTV AI Behavior", "Stock Monitor", "Visual Audit"], "a": "7,5 Jt", "b": "3,5 Jt"},
    "V-ENTERPRISE": {"t": "Korporasi", "f": ["The Core Brain", "Dedicated Server", "Custom AI SOP"], "a": "15 Jt", "b": "10 Jt"},
    "V-ULTRA": {"t": "Investor/VIP", "f": ["Executive Dash", "Heatmap", "VIP Priority"], "a": "25 Jt", "b": "14.9 Jt"}
}

cols = st.columns(5)
for i, (name, info) in enumerate(pkgs.items()):
    with cols[i]:
        st.markdown(f"""
        <div class="product-card">
            <div class="product-title">{name}</div>
            <div class="target-text">{info['t']}</div><hr>
            <div class="feature-list">{"".join([f"• {f}<br>" for f in info['f']])}</div>
            <div class="price-box">
                <small>Aktivasi: {info['a']}</small><br>
                <b style="color: #2563eb; font-size: 18px;">Bln: {info['b']}</b>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"Pilih {name}", key=f"btn_{i}", use_container_width=True)

# PORTAL DATA KLIEN
st.markdown('<div class="section-title">📱 PORTAL DATA & ADMINISTRASI</div>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.text_input("Nama Lengkap Klien")
    st.file_uploader("Upload KTP", type=['jpg', 'png'])
with c2:
    st.text_input("Username")
    st.text_input("Password", type="password")

# FOLDER ADMIN (TERPROTEKSI PASSWORD)
st.write("---")
with st.expander("🔒 Folder Keuangan Admin"):
    if st.text_input("Input Master Password", type="password") == ADMIN_PASSWORD:
        st.success("Akses Diterima")
        raw = st.number_input("Estimasi Biaya API (Rp)", value=5000000)
        st.metric("Penghematan (20%)", f"Rp {raw * 0.20:,.0f}", delta="Edge Filtering Aktif")
