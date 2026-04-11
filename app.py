import streamlit as st
import os
from dotenv import load_dotenv

# --- 1. KONFIGURASI & KEAMANAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")
load_dotenv()
ADMIN_PW = os.getenv("ADMIN_PASSWORD")

if 'menu' not in st.session_state:
    st.session_state.menu = "🏠 Visi & Misi"

# --- 2. CSS STANDAR SOP V-GUARD ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #f8fafc; }
    .stButton>button { width: 100%; border-radius: 8px; text-align: left; padding: 12px; font-weight: bold; margin-bottom: 5px; }
    .main-slogan { text-align: center; font-size: 30px; font-weight: 800; color: #1e3a8a; margin: 20px 0; }
    .justified-text { text-align: justify; line-height: 1.8; font-size: 15px; color: #333; background: white; padding: 25px; border-radius: 12px; border: 1px solid #e2e8f0; }
    .roi-display { background: #1e3a8a; color: white; padding: 40px; border-radius: 15px; text-align: center; margin-top: 20px; }
    .admin-green-box { background: #f0fdf4; border: 2px dashed #22c55e; color: #166534; padding: 30px; border-radius: 15px; text-align: center; }
    .product-card { 
        border: 1px solid #e2e8f0; border-radius: 15px; padding: 20px; 
        text-align: center; min-height: 480px; background: #fff;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION (MUTLAK TERPISAH) ---
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD DASHBOARD")
    if st.button("🏠 Visi & Misi"): st.session_state.menu = "🏠 Visi & Misi"
    if st.button("📊 ROI (Dana Aman)"): st.session_state.menu = "📊 ROI (Dana Aman)"
    if st.button("📦 Layanan Produk"): st.session_state.menu = "📦 Layanan Produk"
    if st.button("📱 Portal Klien"): st.session_state.menu = "📱 Portal Klien"
    if st.button("🔒 Admin Center"): st.session_state.menu = "🔒 Admin Center"
    st.write("---")
    st.info("SOP Status: **ACTIVE**")
    st.caption("Digitizing Trust, Eliminating Leakage")

# --- 4. DASHBOARD: VISI & MISI ---
if st.session_state.menu == "🏠 Visi & Misi":
    st.markdown('<div class="main-slogan">"Digitizing Trust, Eliminating Leakage"</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2.5])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
        else: st.info("👤 Founder Photo (erwin.jpg)")
    with c2:
        st.markdown('<div class="justified-text">', unsafe_allow_html=True)
        st.write("""
        **VISI: Menjadi Jangkar Kepercayaan Digital dan Standar Global Integritas Bisnis** V-Guard AI Intelligence bervisi untuk menjadi pilar utama dalam ekosistem bisnis global yang mengedepankan transparansi mutlak dan keamanan aset berbasis kecerdasan buatan terdepan. Di tengah era volatilitas digital yang serba cepat, kami memposisikan diri sebagai "jangkar kepercayaan" bagi para pemilik bisnis dan investor. Kami tidak sekadar membangun perangkat lunak; kami membangun standar baru di mana integritas bisnis tidak lagi bersifat abstrak, melainkan menjadi data yang terukur, dapat diverifikasi, dan tidak dapat dimanipulasi secara sepihak. Kami bercita-cita untuk menciptakan dunia usaha yang bebas dari risiko sistemik, divalidasi oleh kebenaran digital yang absolut. Melalui teknologi kami, kepercayaan bukan lagi harapan, melainkan kepastian matematis yang mendasari setiap interaksi ekonomi.

        **MISI: Eliminasi Kebocoran Aset Melalui Edge Intelligence dan Perlindungan Siber Berlapis** Misi kami adalah memberdayakan pelaku bisnis melalui penerapan teknologi **Edge Filtering** yang mutakhir untuk membangun infrastruktur integritas digital yang mampu mengubah etika kerja menjadi parameter performa yang akurat. Dengan algoritma deteksi dini, V-Guard secara proaktif mengidentifikasi anomali finansial tepat di titik transaksi guna mengeliminasi potensi kebocoran sebelum dampak kerugian meluas. Kami menjaga warisan bisnis klien dari risiko internal maupun siber secara berkelanjutan selamanya.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# --- 5. DASHBOARD: ROI (HITUNG KERUGIAN KLIEN) ---
elif st.session_state.menu == "📊 ROI (Dana Aman)":
    st.subheader("📈 Analisis Potensi Kerugian Dana Klien")
    omzet = st.number_input("Omzet Bulanan Klien (Rp)", value=100000000)
    leak_pct = st.slider("Estimasi Kebocoran (%)", 5, 40, 20)
    dana_aman = omzet * (leak_pct / 100)
    st.markdown(f'<div class="roi-display"><h2>Potensi Dana Aman: Rp {dana_aman:,.0f}</h2><p>Kebocoran dana yang berhasil dihentikan oleh V-Guard</p></div>', unsafe_allow_html=True)

# --- 6. DASHBOARD: LAYANAN PRODUK ---
elif st.session_state.menu == "📦 Layanan Produk":
    st.subheader("🏷️ Katalog Layanan V-Guard")
    pkgs = {
        "V-LITE": ["Mikro", "• Filter Lokal<br>• WA Notif"],
        "V-PRO": ["Retail", "• VCS Integration<br>• Bank Link"],
        "V-SIGHT": ["Gudang", "• CCTV AI Behavior<br>• Audit Visual"],
        "V-ENTERPRISE": ["Korporasi", "• Core Brain AI<br>• Custom SOP"],
        "V-ULTRA": ["VIP", "• Exec Dash<br>• VIP Support"]
    }
    cols = st.columns(5)
    for i, (name, val) in enumerate(pkgs.items()):
        with cols[i]:
            st.markdown(f"""<div class="product-card"><div><h3>{name}</h3><small>{val[0]}</small><hr><div style='text-align:left; font-size:12px;'>{val[1]}</div></div><button style='width:100%; margin-top:15px;'>Pilih {name}</button></div>""", unsafe_allow_html=True)

# --- 7. DASHBOARD: PORTAL KLIEN ---
elif st.session_state.menu == "📱 Portal Klien":
    st.subheader("📱 Pendaftaran Klien Baru")
    with st.container(border=True):
        st.text_input("Nama Owner")
        st.file_uploader("Upload KTP")
        st.button("Daftar Sekarang", type="primary")

# --- 8. DASHBOARD: ADMIN CENTER (LOGIKA POTONG 20%) ---
elif st.session_state.menu == "🔒 Admin Center":
    st.subheader("🔒 Executive Admin Control")
    if st.text_input("Password", type="password") == ADMIN_PW:
        st.write("### Analisis Efisiensi Biaya API")
        api_raw = st.number_input("Input Biaya API Mentah (Rp)", value=5000000)
        api_net = api_raw * 0.8 # LOGIKA POTONG 20% OTOMATIS
        st.markdown(f"""
            <div class="admin-green-box">
                <p>🛡️ SOP EDGE FILTERING ACTIVE</p>
                <h2 style='margin:10px 0;'>Biaya API Net: Rp {api_net:,.0f}</h2>
                <p>Profit Efisiensi (20%): Rp {api_raw * 0.2:,.0f}</p>
            </div>
            """, unsafe_allow_html=True)
