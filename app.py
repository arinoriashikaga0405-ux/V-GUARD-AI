import streamlit as st
import os
from dotenv import load_dotenv

# --- 1. SETTING HALAMAN & KEAMANAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")
load_dotenv()
ADMIN_PW = os.getenv("ADMIN_PASSWORD") # Pastikan isi .env Bapak benar

if 'page' not in st.session_state:
    st.session_state.page = "🏠 Visi & Misi"

# --- 2. CSS STANDAR VISUAL V-GUARD ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #f8fafc; }
    .stButton>button { width: 100%; border-radius: 8px; text-align: left; padding: 12px; font-weight: bold; margin-bottom: 5px; }
    .main-slogan { text-align: center; font-size: 32px; font-weight: 800; color: #1e3a8a; margin: 20px 0; }
    .justified-text { text-align: justify; line-height: 1.8; font-size: 15px; color: #333; background: white; padding: 25px; border-radius: 12px; border: 1px solid #e2e8f0; }
    .product-card { 
        border: 1px solid #e2e8f0; border-radius: 15px; padding: 20px; 
        text-align: center; min-height: 480px; background: #fff;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .roi-display { background: #1e3a8a; color: white; padding: 40px; border-radius: 15px; text-align: center; margin-top: 20px; }
    .admin-green-box { background: #f0fdf4; border: 2px dashed #22c55e; color: #166534; padding: 30px; border-radius: 15px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGASI (DASHBOARD TERPISAH SESUAI SOP) ---
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD NAV")
    if st.button("🏠 Visi & Misi"): st.session_state.page = "🏠 Visi & Misi"
    if st.button("📊 ROI (Dana Aman)"): st.session_state.page = "📊 ROI (Dana Aman)"
    if st.button("📦 Layanan Produk"): st.session_state.page = "📦 Layanan Produk"
    if st.button("📱 Portal Klien"): st.session_state.page = "📱 Portal Klien"
    if st.button("🔒 Admin Center"): st.session_state.page = "🔒 Admin Center"
    st.write("---")
    st.info("SOP Status: **ACTIVE**")
    st.caption("Digitizing Trust, Eliminating Leakage")

# --- 4. HALAMAN: VISI & MISI ---
if st.session_state.page == "🏠 Visi & Misi":
    st.markdown('<div class="main-slogan">"Digitizing Trust, Eliminating Leakage"</div>', unsafe_allow_html=True)
    c_img, c_txt = st.columns([1, 2.5])
    with c_img:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
        else: st.info("👤 Founder Photo")
    with c_txt:
        st.markdown('<div class="justified-text">', unsafe_allow_html=True)
        st.write("""
        **VISI: Menjadi Jangkar Kepercayaan Digital dan Standar Global Integritas Bisnis** V-Guard AI Intelligence bervisi untuk menjadi pilar utama dalam ekosistem bisnis global yang mengedepankan transparansi mutlak dan keamanan aset berbasis kecerdasan buatan terdepan. Kami memposisikan diri sebagai "jangkar kepercayaan" bagi para pemilik bisnis dan investor, memastikan integritas bisnis menjadi data yang terukur dan tidak dapat dimanipulasi secara sepihak.
        
        **MISI: Eliminasi Kebocoran Aset Melalui Edge Intelligence dan Perlindungan Siber Berlapis** Misi kami adalah memberdayakan pelaku bisnis melalui penerapan teknologi **Edge Filtering** yang mutakhir. Dengan algoritma deteksi dini, V-Guard secara proaktif mengidentifikasi anomali finansial tepat di titik transaksi guna mengeliminasi potensi kebocoran sebelum dampak kerugian meluas. Kami menjaga warisan bisnis klien dari risiko internal maupun siber secara berkelanjutan selamanya.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# --- 5. HALAMAN: ROI (MENGHITUNG KERUGIAN KLIEN) ---
elif st.session_state.page == "📊 ROI (Dana Aman)":
    st.subheader("📈 Kalkulator Proteksi Dana Klien (ROI)")
    omzet = st.number_input("Omzet Bulanan Klien (Rp)", value=100000000)
    leak_pct = st.slider("Estimasi Kebocoran Dana (%)", 5, 40, 20)
    
    # Hitung Dana Aman (Hak Klien)
    dana_aman = omzet * (leak_pct / 100)
    st.markdown(f'<div class="roi-display"><h2>Potensi Dana Aman: Rp {dana_aman:,.0f}</h2><p>Kebocoran yang berhasil ditutup oleh V-Guard</p></div>', unsafe_allow_html=True)

# --- 6. HALAMAN: LAYANAN PRODUK ---
elif st.session_state.page == "📦 Layanan Produk":
    st.subheader("🏷️ Paket Layanan Strategis")
    pkgs = {
        "V-LITE": ["Mikro / 1 Kasir", "• Anomali Filter Lokal<br>• WA Summary Notif"],
        "V-PRO": ["Retail & Kafe", "• VCS Integration<br>• Bank Audit Link"],
        "V-SIGHT": ["Gudang & Toko", "• AI CCTV Behavior<br>• Visual Audit"],
        "V-ENTERPRISE": ["Korporasi", "• Core Brain AI<br>• Custom AI SOP"],
        "V-ULTRA": ["Investor/VIP", "• Exec Dash<br>• VIP Support"]
    }
    cols = st.columns(5)
    for i, (name, val) in enumerate(pkgs.items()):
        with cols[i]:
            st.markdown(f"""<div class="product-card"><div><h3>{name}</h3><small>{val[0]}</small><hr><div style='text-align:left; font-size:12px;'>{val[1]}</div></div><button style='width:100%; margin-top:10px;'>Pilih {name}</button></div>""", unsafe_allow_html=True)

# --- 7. HALAMAN: PORTAL KLIEN & ADMIN CENTER ---
elif st.session_state.page == "📱 Portal Klien":
    st.subheader("📱 Portal Pendaftaran Klien")
    with st.container(border=True):
        st.text_input("Nama Owner")
        st.file_uploader("Upload KTP (Auto-Filtering)")
        st.button("Daftar & Proteksi Aset Sekarang", type="primary", use_container_width=True)

elif st.session_state.page == "🔒 Admin Center":
    st.subheader("🔒 Executive Dashboard (Internal)")
    pw = st.text_input("Master Password", type="password")
    
    if pw == ADMIN_PW:
        st.success("Akses Diterima")
        st.write("### Analisis Multi-Channel & Efisiensi API")
        
        api_raw = st.number_input("Total Biaya API Mentah (Rp)", value=5000000)
        
        # Logika pemotongan 20% otomatis di Dashboard Admin
        api_net = api_raw * 0.8
        st.markdown(f"""
            <div class="admin-green-box">
                <p>🛡️ SOP EDGE FILTERING ACTIVE</p>
                <h2 style='margin:10px 0;'>Biaya API Net: Rp {api_net:,.0f}</h2>
                <p>Profit Efisiensi (20%): Rp {api_raw * 0.2:,.0f}</p>
            </div>
            """, unsafe_allow_html=True)
