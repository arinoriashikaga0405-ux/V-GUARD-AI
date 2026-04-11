import streamlit as st
import os
from dotenv import load_dotenv

# --- 1. KONFIGURASI & SESSION ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")
load_dotenv()
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

if 'menu' not in st.session_state:
    st.session_state.menu = "🏠 Home (Visi Misi)"

# --- 2. CSS STANDAR SOP V-GUARD ---
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; height: 45px; }
    .main-slogan { text-align: center; font-size: 30px; font-weight: 800; color: #1e3a8a; margin: 20px 0; }
    .justified-text { text-align: justify; line-height: 1.8; font-size: 15px; background: white; padding: 25px; border-radius: 12px; border: 1px solid #e2e8f0; }
    .product-card { 
        border: 1px solid #e2e8f0; border-radius: 15px; padding: 20px; 
        text-align: center; min-height: 400px; background: #fff;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .roi-display { background: #1e3a8a; color: white; padding: 30px; border-radius: 15px; text-align: center; }
    .admin-metric { background: #f0fdf4; border: 1px solid #22c55e; padding: 20px; border-radius: 12px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. NAVIGASI SIDEBAR ---
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD NAV")
    if st.button("🏠 Home (Visi Misi)"): st.session_state.menu = "🏠 Home (Visi Misi)"
    if st.button("📊 ROI (Dana Aman)"): st.session_state.menu = "📊 ROI (Dana Aman)"
    if st.button("📱 Portal Klien"): st.session_state.menu = "📱 Portal Klien"
    if st.button("🔒 Admin Portal"): st.session_state.menu = "🔒 Admin Portal"
    st.write("---")
    st.info("SOP Status: **ACTIVE**")

# --- 4. HOME: VISI & MISI ---
if st.session_state.menu == "🏠 Home (Visi Misi)":
    st.markdown('<div class="main-slogan">"Digitizing Trust, Eliminating Leakage"</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2.5])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
        else: st.info("Founder Photo")
    with c2:
        st.markdown('<div class="justified-text">', unsafe_allow_html=True)
        st.write("""
        **VISI: Menjadi Jangkar Kepercayaan Digital dan Standar Global Integritas Bisnis** V-Guard AI Intelligence bervisi untuk menjadi pilar utama dalam ekosistem bisnis global yang mengedepankan transparansi mutlak dan keamanan aset berbasis kecerdasan buatan terdepan. Kami memposisikan diri sebagai "jangkar kepercayaan" bagi para pemilik bisnis dan investor, memastikan integritas bisnis menjadi data yang terukur dan tidak dapat dimanipulasi.
        
        **MISI: Eliminasi Kebocoran Aset Melalui Edge Intelligence dan Perlindungan Siber Berlapis** Misi kami adalah memberdayakan pelaku bisnis melalui penerapan teknologi Edge Filtering yang mutakhir. Dengan algoritma deteksi dini, V-Guard secara proaktif mengidentifikasi anomali finansial tepat di titik kejadian transaksi, guna mengeliminasi potensi kebocoran sebelum dampak kerugian meluas.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# --- 5. ROI: MENGHITUNG KERUGIAN KLIEN ---
elif st.session_state.menu == "📊 ROI (Dana Aman)":
    st.subheader("📊 Kalkulator Proteksi Dana Klien")
    omzet = st.number_input("Input Omzet Bulanan Klien (Rp)", value=100000000)
    leak_pct = st.slider("Estimasi Kebocoran Dana (%)", 5, 40, 20)
    
    dana_aman = omzet * (leak_pct / 100)
    st.markdown(f'<div class="roi-display"><h2>Potensi Dana Aman: Rp {dana_aman:,.0f}</h2><p>Kebocoran yang berhasil dihentikan oleh sistem V-Guard AI</p></div>', unsafe_allow_html=True)
    
    st.write("---")
    # Grid Produk Strategis
    cols = st.columns(5)
    pkgs = ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE", "V-ULTRA"]
    targets = ["1 Kasir", "Retail", "Gudang", "Korporasi", "VIP"]
    for i, p in enumerate(pkgs):
        with cols[i]:
            st.markdown(f'<div class="product-card"><b>{p}</b><br><small>{targets[i]}</small><hr><p style="font-size:11px; text-align:left;">• AI Anomaly Filter<br>• Real-time Guard<br>• Fraud Detection</p></div>', unsafe_allow_html=True)
            st.button(f"Pilih {p}", key=f"btn_{i}")

# --- 6. ADMIN PORTAL: BIAYA API NET (SAVING 20%) ---
elif st.session_state.menu == "🔒 Admin Portal":
    st.subheader("🔒 Dashboard Internal Admin")
    pw = st.text_input("Master Password", type="password")
    
    if pw == ADMIN_PASSWORD:
        st.success("Akses Diterima")
        st.write("### Analisis Operasional & Efisiensi API")
        
        api_raw = st.number_input("Total Biaya API Mentah (Rp)", value=5000000)
        # Logika pemotongan 20% otomatis di Admin
        api_net = api_raw * 0.8
        api_saving = api_raw * 0.2
        
        c_a1, c_a2 = st.columns(2)
        with c_a1:
            st.markdown(f'<div class="admin-metric"><h3>Biaya API Net</h3><h2>Rp {api_net:,.0f}</h2><p>(Sudah Potong 20%)</p></div>', unsafe_allow_html=True)
        with c_a2:
            st.markdown(f'<div class="admin-metric" style="border-color:#1e3a8a;"><h3>Total Efisiensi</h3><h2>Rp {api_saving:,.0f}</h2><p>Profit dari Edge Filtering</p></div>', unsafe_allow_html=True)
            
        st.divider()
        st.write("**Daftar Klien Aktif:** 12 Klien")
    elif pw:
        st.error("Password Salah!")

# --- 7. PORTAL KLIEN ---
elif st.session_state.menu == "📱 Portal Klien":
    st.subheader("📱 Pendaftaran Klien Baru")
    with st.form("reg"):
        st.text_input("Nama Lengkap Owner")
        st.file_uploader("Upload KTP (Auto-Filtering)")
        st.form_submit_button("Daftar & Proteksi Aset")
