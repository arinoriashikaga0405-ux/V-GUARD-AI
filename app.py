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

# --- 2. CSS PERBAIKAN TAMPILAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main-slogan {
        text-align: center; font-size: 32px; font-weight: 800; color: #1e3a8a;
        margin-bottom: 30px; letter-spacing: 1px;
    }
    .justified-text {
        text-align: justify; line-height: 1.8; font-size: 16px; color: #333;
        background: #ffffff; padding: 20px; border-radius: 10px;
    }
    .product-card { 
        border: 1px solid #e2e8f0; border-radius: 15px; padding: 20px; 
        text-align: center; height: 580px; background: #fff; 
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .product-title { color: #1e3a8a; font-weight: bold; font-size: 20px; }
    .target-text { color: #d63384; font-size: 13px; font-weight: bold; margin-bottom: 15px; }
    .feature-list { text-align: left; font-size: 13px; min-height: 220px; line-height: 1.8; color: #444; }
    .price-box { margin-top: auto; padding: 12px; border-radius: 10px; background: #f8fafc; border: 1px solid #f1f5f9; }
    .section-title { color: #1e3a8a; font-weight: bold; font-size: 18px; text-transform: uppercase; margin: 40px 0 20px 0; border-left: 5px solid #1e3a8a; padding-left: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER & VISI MISI (250 KATA) ---
st.markdown(f'<div class="main-slogan">"Digitizing Trust, Eliminating Leakage"</div>', unsafe_allow_html=True)

col_foto, col_visi = st.columns([1, 2.5])

with col_foto:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.info("👤 Founder Photo")

with col_visi:
    st.markdown('<div class="justified-text">', unsafe_allow_html=True)
    st.write("""
    **VISI: Menjadi Jangkar Kepercayaan Digital dan Standar Global Integritas Bisnis** V-Guard AI Intelligence bervisi untuk menjadi pilar utama dalam ekosistem bisnis global yang mengedepankan transparansi mutlak dan keamanan aset berbasis kecerdasan buatan. Di tengah era volatilitas digital yang serba cepat, kami memposisikan diri sebagai "jangkar kepercayaan" bagi para pemilik bisnis dan investor. Kami tidak sekadar membangun perangkat lunak; kami membangun standar baru di mana integritas bisnis tidak lagi bersifat abstrak, melainkan menjadi data yang terukur secara akurat. Kami bercita-cita untuk menciptakan dunia usaha yang bebas dari risiko sistemik, di mana setiap transaksi divalidasi oleh kebenaran digital yang absolut.

    **MISI: Eliminasi Kebocoran Aset Melalui Edge Intelligence dan Perlindungan Siber Berlapis** Misi utama kami adalah memberdayakan pelaku bisnis melalui penerapan teknologi **Edge Filtering** yang mutakhir. Kami berkomitmen untuk membangun infrastruktur integritas digital yang mampu mengubah etika kerja menjadi parameter performa yang transparan. Dengan algoritma deteksi dini, V-Guard secara proaktif mengidentifikasi anomali finansial tepat di titik kejadian transaksi, guna mengeliminasi potensi kebocoran sebelum dampak kerugian meluas. Lebih dari itu, kami menjaga disiplin pengembangan sistem yang ketat guna melindungi warisan bisnis klien dari risiko siber maupun kecurangan internal. Melalui inovasi tanpa henti, V-Guard berupaya mendigitalkan rasa aman, memastikan setiap unit usaha dapat tumbuh secara eksponensial dalam ekosistem yang bersih, efisien, dan terlindungi selamanya.
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
                <div class="target-text">{info['t']}</div><hr>
                <div class="feature-list">{"<br>".join(info['f'])}</div>
            </div>
            <div class="price-box">
                <small>Aktivasi: {info['a']}</small><br>
                <b style="color: #2563eb; font-size: 19px;">Bln: {info['b']}</b>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"Pilih {name}", key=f"btn_{i}", use_container_width=True)

# --- 5. PORTAL ADMINISTRASI ---
st.markdown('<div class="section-title">📱 PORTAL DATA & PENDAFTARAN</div>', unsafe_allow_html=True)
c_reg, c_log = st.columns(2)
with c_reg:
    with st.container(border=True):
        st.subheader("Daftar Unit Baru")
        st.text_input("Nama Lengkap (Sesuai KTP)")
        st.file_uploader("Upload Foto KTP", type=['jpg', 'png'])
        st.button("Kirim Berkas", type="primary", use_container_width=True)

with c_log:
    with st.container(border=True):
        st.subheader("Dashboard Owner")
        st.text_input("ID Unit")
        st.text_input("Password", type="password")
        st.button("Masuk Sistem", use_container_width=True)

# --- 6. ADMIN (FOLDER AMAN) ---
st.write("---")
with st.expander("🔒 Admin Control"):
    if st.text_input("Master Password", type="password") == ADMIN_PASSWORD:
        st.success("Akses Diterima")
        raw = st.number_input("Estimasi Biaya API (Rp)", value=5000000)
        st.metric("Dana Terselamatkan (20%)", f"Rp {raw * 0.20:,.0f}")
