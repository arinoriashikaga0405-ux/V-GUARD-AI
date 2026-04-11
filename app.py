import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

# --- 1. KEAMANAN DATA (.env) ---
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

if API_KEY:
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception:
        pass

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS UNTUK TAMPILAN ELEGAN & SIMETRIS
st.markdown("""
    <style>
    .main-slogan { text-align: center; font-size: 32px; font-weight: 800; color: #1e3a8a; margin-bottom: 30px; }
    .justified-text { text-align: justify; line-height: 1.8; font-size: 15px; color: #333; background: #fff; padding: 20px; border-radius: 12px; }
    
    /* Layout Kartu Produk 5 Kolom */
    .product-card { 
        border: 1px solid #e2e8f0; border-radius: 15px; padding: 20px; 
        text-align: center; height: 550px; background: #fff; 
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .product-title { color: #1e3a8a; font-weight: bold; font-size: 20px; }
    .target-text { color: #d63384; font-size: 13px; font-weight: bold; margin-bottom: 15px; }
    .feature-list { text-align: left; font-size: 12px; line-height: 1.8; color: #444; min-height: 200px; }
    .price-box { margin-top: auto; padding: 12px; border-radius: 10px; background: #f8fafc; border: 1px solid #f1f5f9; }
    .section-title { color: #1e3a8a; font-weight: bold; font-size: 18px; border-left: 5px solid #1e3a8a; padding-left: 15px; margin: 40px 0 20px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER & VISI MISI (250 KATA) ---
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
    **VISI: Menjadi Jangkar Kepercayaan Digital dan Standar Global Integritas Bisnis** V-Guard AI Intelligence bervisi untuk menjadi pilar utama dalam ekosistem bisnis global yang mengedepankan transparansi mutlak dan keamanan aset berbasis kecerdasan buatan terdepan. Di tengah era volatilitas digital yang serba cepat, kami memposisikan diri sebagai "jangkar kepercayaan" bagi para pemilik bisnis dan investor. Kami tidak sekadar membangun perangkat lunak; kami membangun standar baru di mana integritas bisnis tidak lagi bersifat abstrak, melainkan menjadi data yang terukur, dapat diverifikasi, dan tidak dapat dimanipulasi secara sepihak. Kami bercita-cita untuk menciptakan dunia usaha yang bebas dari risiko sistemik, di mana setiap transaksi divalidasi oleh kebenaran digital yang absolut.

    **MISI: Eliminasi Kebocoran Aset Melalui Edge Intelligence dan Perlindungan Siber Berlapis** Misi utama kami adalah memberdayakan pelaku bisnis melalui penerapan teknologi **Edge Filtering** yang mutakhir untuk membangun infrastruktur integritas digital yang mampu mengubah etika kerja menjadi parameter performa yang akurat. Dengan algoritma deteksi dini, V-Guard secara proaktif mengidentifikasi anomali finansial tepat di titik kejadian transaksi, guna mengeliminasi potensi kebocoran sebelum dampak kerugian meluas. Lebih dari itu, kami menjaga disiplin pengembangan sistem yang sangat ketat guna melindungi warisan bisnis klien dari risiko siber maupun kecurangan internal secara berkelanjutan. Melalui inovasi tanpa henti, V-Guard berupaya mendigitalkan rasa aman, memastikan bahwa setiap unit usaha dapat tumbuh secara eksponensial dalam ekosistem yang bersih, efisien, dan terlindungi selamanya.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. PRODUK & LAYANAN (5 KOLOM SIMETRIS) ---
st.markdown('<div class="section-title">🏷️ PRODUK & LAYANAN STRATEGIS</div>', unsafe_allow_html=True)

pkgs = {
    "V-LITE": {"t": "Mikro / 1 Kasir", "f": ["• Anomali Filter Lokal", "• WA Summary", "• Cloud Secure"], "a": "1.5 Jt", "b": "750 rb"},
    "V-PRO": {"t": "Retail & Kafe", "f": ["• VCS Integration", "• Fraud-Only API Upload", "• Bank Audit Link"], "a": "
