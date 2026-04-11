import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# --- 1. KONFIGURASI API KEY (WAJIB PALING ATAS) ---
GEMINI_API_KEY = "ISI_API_KEY_ANDA_DI_SINI" 

try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Koneksi API Gagal: {e}")

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .justified-text { text-align: justify; line-height: 1.8; font-size: 16px; }
    .sidebar-title { color: #2563eb; font-weight: 800; text-align: center; font-size: 26px; }
    .founder-label { text-align: center; font-weight: bold; color: #64748b; font-size: 14px; margin-top: 5px; }
    .product-card { border: 1px solid #e2e8f0; border-radius: 12px; padding: 25px; text-align: center; height: 100%; background: #fff; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
    .slogan { text-align: center; font-size: 28px; font-weight: bold; color: #1e3a8a; margin-top: 20px; margin-bottom: 10px; }
    .section-title { color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; margin-top: 50px; margin-bottom: 25px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (HANYA FOTO & JUDUL) ---
with st.sidebar:
    st.markdown('<div class="sidebar-title">V-Guard AI</div>', unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.markdown('<div class="founder-label">Founder - CEO</div>', unsafe_allow_html=True)
    st.write("---")
    st.info("Sistem Otonom Aktif")

# --- 4. TAMPILAN SATU HALAMAN PENUH ---

# BAGIAN 1: SLOGAN & VISI MISI
st.markdown('<div class="slogan">"Digitizing Trust, Eliminating Leakage"</div>', unsafe_allow_html=True)
col_img, col_txt = st.columns([1, 2.5])
with col_img:
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
with col_txt:
    st.markdown('<div class="justified-text">', unsafe_allow_html=True)
    st.write("""
    **Visi: Menjadi Jangkar Kepercayaan Digital dan Standar Global Integritas Bisnis** V-Guard AI Intelligence bervisi menciptakan ekosistem bisnis global yang sepenuhnya transparan, aman, dan berintegritas tinggi melalui inovasi teknologi kecerdasan buatan terdepan. Kami hadir bukan sekadar sebagai penyedia solusi perangkat lunak, melainkan sebagai jangkar kepercayaan bagi setiap pemilik bisnis di era ketidakpastian global yang serba cepat. Kami memastikan setiap pemilik usaha memiliki ketenangan pikiran total melalui validasi kejujuran sistem secara real-time, di mana data operasional tidak lagi bisa dimanipulasi oleh kepentingan pribadi. Kami bercita-cita menjadi standar emas global dalam layanan Integrity Assurance, di mana teknologi kecerdasan buatan otonom kami mampu menghapuskan segala bentuk keraguan operasional serta manipulasi finansial dalam dunia bisnis yang kompetitif.

    **Misi: Eliminasi Kebocoran Aset Melalui Edge Intelligence** Misi kami adalah memberikan perlindungan aset yang tak tertembus melalui penerapan teknologi Edge Filtering yang mutakhir untuk membangun infrastruktur integritas digital yang mampu mengubah etika kerja menjadi data terukur secara akurat. Kami berkomitmen menerapkan algoritma cerdas untuk deteksi dini anomali finansial tepat di titik kejadian transaksi guna mencegah kebocoran sebelum dampak kerugian meluas, sekaligus memastikan efisiensi biaya operasional bagi mitra kami melalui sistem penyaringan data yang cerdas. Melalui Command Center terenkripsi tingkat militer, kami memberikan kedaulatan penuh bagi pemilik usaha untuk memantau bisnis mereka secara otonom dari mana saja. V-Guard menjaga disiplin pengembangan perangkat lunak yang sangat ketat sesuai standar operasional baku guna menjaga warisan bisnis klien dari risiko sistemik, kecurangan, maupun serangan siber selamanya.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# BAGIAN 2: PRODUK & LAYANAN (5 KOLOM)
st.markdown('<div class="section-title">🏷️ PRODUK & LAYANAN STRATEGIS</div>', unsafe_allow_html=True)
pkgs = {
    "V-LITE": {"akt": "1.5 Jt", "bln": "750 rb", "target": "Mikro / 1 Kasir", "f": "Anomali Filter Lokal, WA Summary, Cloud Secure"},
    "V-PRO": {"akt": "3 Jt", "bln": "1.5 Jt", "target": "Retail & Kafe", "f": "VCS Integration, Fraud-Only API Upload, Bank Audit"},
    "V-SIGHT": {"akt": "7,5 Jt", "bln": "3,5 Jt", "target": "Gudang & Toko", "f": "CCTV AI Behavior, Stock Monitor, Visual Audit"},
    "V-ENTERPRISE": {"akt": "15 Jt", "bln": "10 Jt", "target": "Korporasi", "f": "The Core Brain, Dedicated Server, Custom AI SOP"},
    "V-ULTRA": {"akt": "25 Jt", "bln": "14.9 Jt", "target": "Investor/VIP", "f": "Executive Dash, Heatmap, VIP Priority"}
}
cols = st.columns(5)
for i, (n, info) in enumerate(pkgs.items()):
    with cols[i]:
        st.markdown(f"""
        <div class="product-card">
            <b style="font-size:18px; color:#1e3a8a;">{n}</b><br>
            <small style="color:#d63384;">{info['target']}</small><br><hr>
            <div style="font-size:13px; text-align:left; min-height:100px;">• {info['f'].replace(', ', '<br>• ')}</div>
            <br>
            <small>Aktivasi: {info['akt']}</small><br>
            <b style="color:#2563eb; font-size:18px;">Bln: {info['bln']}</b>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"Pilih {n}", key=n, use_container_width=True)

# BAGIAN 3: PORTAL KLIEN & ANALISIS
st.markdown('<div class="section-title">📱 PORTAL KLIEN & ONBOARDING</div>', unsafe_allow_html=True)
c_left, c_right = st.columns(2)
with c_left:
    st.subheader("Pemesanan Baru")
    st.text_input("Nama Usaha")
    st.selectbox("Pilih Paket", list(pkgs.keys()))
    st.button("Kirim Form Pemesanan", use_container_width=True)
with c_right:
    st.subheader("Login Command Center")
    st.text_input("Client ID")
    st.text_input("Password", type="password")
    st.button("Masuk Sistem", use_container_width=True)

# BAGIAN 4: ADMIN CENTER (DIPOTONG PASSWORD)
st.markdown('<div class="section-title">🔒 EXECUTIVE ADMIN FOLDER</div>', unsafe_allow_html=True)
pass_admin = st.text_input("Masukkan Password Admin untuk Melihat Efisiensi API", type="password")
if pass_admin == "w1nbju8282":
    st.success("Akses Diterima.")
    ca1, ca2 = st.columns(2)
    with ca1:
        raw_api = st.number_input("Estimasi Biaya API Tanpa Filter (Rp)", value=5000000)
    with ca2:
        st.metric("Pengehematan Biaya API (20%)", f"Rp {raw_api * 0.20:,.0f}", delta="Edge Filtering Active")
    st.info("Strategi: Data mentah kasir difilter lokal. Hanya indikasi fraud/void yang dikirim ke API Cloud.")
