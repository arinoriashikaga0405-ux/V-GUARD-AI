import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

# --- 1. KEAMANAN ---
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

if API_KEY:
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception: pass

# --- 2. CONFIG & CSS ---
st.set_page_config(page_title="V-Guard AI", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main-slogan { text-align: center; font-size: 30px; font-weight: 800; color: #1e3a8a; margin-bottom: 20px; }
    .justified-text { text-align: justify; line-height: 1.6; font-size: 15px; background: white; padding: 20px; border-radius: 10px; }
    .product-card { 
        border: 1px solid #e2e8f0; border-radius: 12px; padding: 15px; 
        text-align: center; height: 520px; background: #fff; 
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .product-title { color: #1e3a8a; font-weight: bold; font-size: 18px; }
    .feature-list { text-align: left; font-size: 12px; line-height: 1.5; color: #444; min-height: 180px; }
    .price-box { margin-top: auto; padding: 10px; border-radius: 8px; background: #f8fafc; border: 1px solid #f1f5f9; }
    .section-title { color: #1e3a8a; font-weight: bold; font-size: 18px; border-left: 5px solid #1e3a8a; padding-left: 15px; margin: 30px 0 15px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER & VISI MISI ---
st.markdown('<div class="main-slogan">"Digitizing Trust, Eliminating Leakage"</div>', unsafe_allow_html=True)

col_f, col_v = st.columns([1, 2.5])
with col_f:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.info("👤 Founder Photo")

with col_v:
    st.markdown('<div class="justified-text">', unsafe_allow_html=True)
    st.write("""
    **VISI: Menjadi Jangkar Kepercayaan Digital.** V-Guard AI Intelligence bervisi menjadi pilar utama ekosistem bisnis global yang mengedepankan transparansi mutlak dan keamanan aset berbasis AI. Kami membangun standar baru di mana integritas bisnis menjadi data yang terukur dan tidak dapat dimanipulasi secara sepihak.<br><br>
    **MISI: Eliminasi Kebocoran Aset Melalui Edge Intelligence.** Misi kami adalah memberdayakan pelaku bisnis melalui teknologi Edge Filtering mutakhir. Dengan algoritma deteksi dini, V-Guard secara proaktif mengidentifikasi anomali finansial tepat di titik transaksi untuk mengeliminasi potensi kebocoran sebelum kerugian meluas.
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. PRODUK 5 KOLOM ---
st.markdown('<div class="section-title">🏷️ PRODUK & LAYANAN STRATEGIS</div>', unsafe_allow_html=True)
pkgs = {
    "V-LITE": ["Mikro / 1 Kasir", "• Anomali Filter Lokal<br>• WA Summary<br>• Cloud Secure", "1.5 Jt", "750 rb"],
    "V-PRO": ["Retail & Kafe", "• VCS Integration<br>• Fraud API Upload<br>• Bank Audit Link", "3 Jt", "1.5 Jt"],
    "V-SIGHT": ["Gudang & Toko", "• CCTV AI Behavior<br>• Stock Monitor<br>• Visual Audit", "7.5 Jt", "3.5 Jt"],
    "
