import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

# --- 1. KEAMANAN DATA ---
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
    .justified-text { text-align: justify; line-height: 1.6; font-size: 15px; background: white; padding: 15px; border-radius: 10px; border: 1px solid #f1f5f9; }
    .product-card { 
        border: 1px solid #e2e8f0; border-radius: 12px; padding: 15px; 
        text-align: center; height: 540px; background: #fff; 
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .product-title { color: #1e3a8a; font-weight: bold; font-size: 18px; }
    .feature-list { text-align: left; font-size: 12px; line-height: 1.6; color: #444; min-height: 180px; margin: 10px 0; }
    .price-box { margin-top: auto; padding: 10px; border-radius: 10px; background: #f8fafc; border: 1px solid #f1f5f9; }
    .section-title { color: #1e3a8a; font-weight: bold; font-size: 18px; border-left: 5px solid #1e3a8a; padding-left: 15px; margin: 30px 0 15px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER ---
st.markdown('<div class="main-slogan">"Digitizing Trust, Eliminating Leakage"</div>', unsafe_allow_html=True)

col_f, col_v = st.columns([1, 2.5])
with col_f:
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    else: st.info("👤 Founder Photo")

with col_v:
    st.markdown('<div class="justified-text"><b>VISI: Menjadi Jangkar Kepercayaan Digital.</b> V-Guard AI Intelligence bervisi menjadi pilar utama ekosistem bisnis global yang mengedepankan transparansi mutlak dan keamanan aset berbasis AI. Kami membangun standar baru di mana integritas bisnis menjadi data yang terukur dan tidak dapat dimanipulasi secara sepihak.<br><br><b>MISI: Eliminasi Kebocoran Aset Melalui Edge Intelligence.</b> Misi kami adalah memberdayakan pelaku bisnis melalui teknologi Edge Filtering mutakhir. Dengan algoritma deteksi dini, V-Guard secara proaktif mengidentifikasi anomali finansial tepat di titik transaksi untuk mengeliminasi potensi kebocoran sebelum kerugian meluas, serta menjaga disiplin pengembangan sistem dari risiko siber maupun kecurangan internal.</div>', unsafe_allow_html=True)

# --- 4. PRODUK 5 KOLOM ---
st.markdown('<div class="section-title">🏷️ PRODUK & LAYANAN STRATEGIS</div>', unsafe_allow_html=True)
pkgs = {
    "V-LITE": {"t": "Mikro / 1 Kasir", "f": ["• Anomali Filter Lokal", "• WA Summary", "• Cloud Secure"], "a": "1.5 Jt", "b": "750 rb"},
    "V-PRO": {"t": "Retail & Kafe", "f": ["• VCS Integration", "• Fraud-Only Upload", "• Bank Audit Link"], "a": "3 Jt", "b": "1.5 Jt"},
    "V-SIGHT": {"t": "Gudang & Toko", "f": ["• CCTV AI Behavior", "• Stock Monitor", "• Visual Audit"], "a": "7,5 Jt", "b": "3,5 Jt"},
    "V-ENTERPRISE": {"t": "Korporasi", "f": ["• The Core Brain", "• Dedicated Server", "• Custom AI SOP"], "a": "15 Jt", "b": "10 Jt"},
    "V-ULTRA": {"t": "Investor/VIP", "f": ["• Executive Dash", "• Heatmap", "• VIP Priority"], "a": "25 Jt", "b": "14.9 Jt"}
}

cols = st.columns(5)
for i, (name, info) in enumerate(pkgs.items()):
    with cols[i]:
        st.markdown(f'<div class="product-card"><div><div class="product-title">{name}</div><div style="color:#d63384;font-size:12px;font-weight:bold;">{info["t"]}</div><hr><div class="feature-list">{"<br>".join(info["f"])}</div></div><div class="price-box"><small style="font-size:10px;">Aktivasi: {info["a"]}</small><br><b style="color:#2563eb;font-size:16px;">Bln: {info["b"]}</b></div></div>', unsafe_allow_html=True)
        st.button("Pilih Paket", key=f"btn_{i}", use_container_width=True)

# --- 5. PORTAL & ADMIN ---
st.write("---")
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="section-title">📱 PENDAFTARAN</div>', unsafe_allow_html=True)
    with st.container(border=True):
