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
    except Exception: pass

# --- 2. CSS PERBAIKAN TOTAL (AGAR TIDAK BERANTAKAN) ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main-slogan {
        text-align: center; font-size: 28px; font-weight: 800; color: #1e3a8a;
        margin-bottom: 25px;
    }
    .justified-text {
        text-align: justify; line-height: 1.6; font-size: 14px; color: #333;
        background: #ffffff; padding: 15px; border-radius: 10px;
    }
    /* Kunci tinggi container agar sejajar 5 kolom */
    .product-card { 
        border: 1px solid #e2e8f0; border-radius: 12px; padding: 15px; 
        text-align: center; height: 500px; background: #fff; 
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        display: flex; flex-direction: column;
    }
    .product-title { color: #1e3a8a; font-weight: bold; font-size: 18px; margin-bottom: 2px; }
    .target-text { color: #d63384; font-size: 12px; font-weight: bold; margin-bottom: 10px; }
    .feature-list { text-align: left; font-size: 12px; height: 200px; line-height: 1.6; color: #444; overflow: hidden; }
    .price-box { margin-top: auto; padding: 8px; border-radius: 8px; background: #f8fafc; border: 1px solid #f1f5f9; }
    .section-title { color: #1e3a8a; font-weight: bold; font-size: 16px; text-transform: uppercase; margin: 30px 0 15px 0; border-left: 5px solid #1e3a8a; padding-left: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER & VISI MISI ---
st.markdown('<div class="main-slogan">"Digitizing Trust, Eliminating Leakage"</div>', unsafe_allow_html=True)

col_foto, col_visi = st.columns([1, 2.8])

with col_foto:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.info("👤 Founder Photo")

with col_visi:
    st.markdown('<div class="justified-text">', unsafe_allow_html=True)
    st.write("""
    **VISI: Menjadi Jangkar Kepercayaan Digital dan Standar Global Integritas Bisnis**   
    V-Guard AI Intelligence bervisi untuk menjadi pilar utama dalam ekosistem bisnis global yang mengedepankan transparansi mutlak dan keamanan aset berbasis kecerdasan buatan. Kami memposisikan diri sebagai "jangkar kepercayaan" bagi para pemilik bisnis dan investor, di mana integritas bisnis menjadi data yang terukur dan tidak dapat dimanipulasi.

    **MISI: Eliminasi Kebocoran Aset Melalui Edge Intelligence**   
    Misi utama kami adalah memberdayakan pelaku bisnis melalui teknologi **Edge Filtering** mutakhir guna membangun infrastruktur integritas digital. Dengan algoritma deteksi dini, V-Guard secara proaktif mengidentifikasi anomali finansial tepat di titik transaksi untuk mengeliminasi potensi kebocoran sebelum dampak kerugian meluas, serta menjaga disiplin pengembangan sistem yang ketat dari risiko siber maupun kecurangan internal.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. LAYANAN PRODUK (5 KOLOM SIMETRIS) ---
st.markdown('<div class="section-title">🏷️ PRODUK & LAYANAN STRATEGIS</div>', unsafe_allow_html=True)

pkgs = {
    "V-LITE": {"t": "Mikro / 1 Kasir", "f": ["• Anomali Filter Lokal", "• WA Summary", "• Cloud Secure"], "a": "1.5 Jt", "b": "750 rb"},
    "V-PRO": {"t": "Retail & Kafe", "f": ["• VCS Integration", "• Fraud-Only API Upload", "• Bank Audit Link"], "a": "3 Jt", "b": "1.5 Jt"},
    "V-SIGHT": {"t": "Gudang & Toko", "f": ["• CCTV AI Behavior", "• Stock Monitor", "• Visual Audit"], "a": "7,5 Jt", "b": "3,5 Jt"},
    "V-ENTERPRISE": {"t": "Korporasi", "f": ["• The Core Brain", "• Dedicated Server", "• Custom AI SOP"], "a": "15 Jt", "b": "10 Jt"},
    "V-ULTRA": {"t": "Investor/VIP", "f": ["• Executive Dash", "• Heatmap", "• VIP Priority Support"], "a": "25 Jt", "b": "14.9 Jt"}
}

cols = st.columns(5)
for i, (name, info) in enumerate(pkgs.items()):
    with cols[i]:
        st.markdown(f"""
        <div class="product-card">
            <div>
                <div class="product-title">{name}</div>
                <div class="target-text">{info['t']}</div><hr style="margin:5px 0;">
                <div class="feature-list">{"<br>".join(info['f'])}</div>
            </div>
            <div class="price-box">
                <small style="font-size:10px;">Aktivasi: {info['a']}</small><br>
                <b style="color: #2563eb; font-size: 16px;">Bln: {info['b']}</b>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"Pilih {name}", key=f"btn_{i}", use_container_width=True)

# --- 5. PORTAL ADMINISTRASI ---
st.markdown('<div class="section-title">📱 PORTAL DATA & PENDAFTARAN</div>', unsafe_allow_html=True)
c_reg, c_log = st.columns(2)
with c_reg:
    with st.container(border=True):
        st.text_input("Nama Klien (Sesuai KTP)")
        st.file_uploader("Upload Foto KTP", type=['jpg', 'png'])
        st.button("Kirim Berkas", type="primary", use_container_width=True)

with c_log:
    with st.container(border=True):
        st.text_input("ID Unit")
        st.text_input("Password", type="password")
        st.button("Masuk Sistem", use_container_width=True)

# --- 6. ADMIN CONTROL ---
if ADMIN_PASSWORD:
    st.write("---")
    with st.expander("🔒 Admin Control"):
        if st.text_input("Master Password", type="password") == ADMIN_PASSWORD:
            st.success("Akses Diterima")
            raw = st.number_input("Estimasi Biaya API (Rp)", value=5000000)
            st.metric("Dana Terselamatkan (20%)", f"Rp {raw * 0.20:,.0f}")
