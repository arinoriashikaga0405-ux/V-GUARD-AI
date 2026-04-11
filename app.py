import streamlit as st
import os
from dotenv import load_dotenv

# --- 1. CONFIG & SESSION ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")
load_dotenv()
ADMIN_PW = os.getenv("ADMIN_PASSWORD")

if 'page' not in st.session_state:
    st.session_state.page = "🏠 Home (Visi Misi)"

# --- 2. CSS STANDAR SOP V-GUARD ---
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; height: 45px; }
    .main-slogan { text-align: center; font-size: 32px; font-weight: 800; color: #1e3a8a; margin: 20px 0; }
    .justified-text { text-align: justify; line-height: 1.8; font-size: 15px; color: #333; background: white; padding: 25px; border-radius: 12px; border: 1px solid #e2e8f0; }
    .product-card { 
        border: 1px solid #e2e8f0; border-radius: 15px; padding: 20px; 
        text-align: center; min-height: 520px; background: #fff;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .product-title { color: #1e3a8a; font-weight: bold; font-size: 18px; }
    .feature-list { text-align: left; font-size: 12px; color: #555; line-height: 1.6; margin: 15px 0; min-height: 180px; }
    .roi-display { background: #1e3a8a; color: white; padding: 25px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    .api-saving-box { background: #f0fdf4; border: 1px dashed #166534; color: #166534; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. NAVIGASI SIDEBAR (SOP) ---
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD MENU")
    if st.button("🏠 Home (Visi Misi)"): st.session_state.page = "🏠 Home (Visi Misi)"
    if st.button("📊 ROI & Layanan"): st.session_state.page = "📊 ROI & Layanan"
    if st.button("📱 Portal Klien"): st.session_state.page = "📱 Portal Klien"
    if st.button("🔒 Admin Portal"): st.session_state.page = "🔒 Admin Portal"
    st.write("---")
    st.info("SOP Status: **ACTIVE**")
    st.caption("Digitizing Trust, Eliminating Leakage")

# --- 4. HALAMAN HOME: VISI & MISI ---
if st.session_state.page == "🏠 Home (Visi Misi)":
    st.markdown('<div class="main-slogan">"Digitizing Trust, Eliminating Leakage"</div>', unsafe_allow_html=True)
    c_img, c_txt = st.columns([1, 2.5])
    with c_img:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
        else: st.info("👤 Founder Photo")
    with c_txt:
        st.markdown('<div class="justified-text">', unsafe_allow_html=True)
        st.write("""
        **VISI: Menjadi Jangkar Kepercayaan Digital dan Standar Global Integritas Bisnis** V-Guard AI Intelligence bervisi untuk menjadi pilar utama dalam ekosistem bisnis global yang mengedepankan transparansi mutlak dan keamanan aset berbasis kecerdasan buatan terdepan. Di tengah era volatilitas digital yang serba cepat, kami memposisikan diri sebagai "jangkar kepercayaan" bagi para pemilik bisnis dan investor. Kami tidak sekadar membangun perangkat lunak; kami membangun standar baru di mana integritas bisnis tidak lagi bersifat abstrak, melainkan menjadi data yang terukur, dapat diverifikasi, dan tidak dapat dimanipulasi secara sepihak. Kami bercita-cita untuk menciptakan dunia usaha yang bebas dari risiko sistemik, divalidasi oleh kebenaran digital yang absolut. Melalui teknologi kami, kepercayaan bukan lagi harapan, melainkan kepastian matematis yang mendasari setiap interaksi ekonomi.

        **MISI: Eliminasi Kebocoran Aset Melalui Edge Intelligence dan Perlindungan Siber Berlapis** Misi utama kami adalah memberdayakan pelaku bisnis melalui penerapan teknologi **Edge Filtering** yang mutakhir untuk membangun infrastruktur integritas digital yang mampu mengubah etika kerja menjadi parameter performa yang akurat. Dengan algoritma deteksi dini, V-Guard secara proaktif mengidentifikasi anomali finansial tepat di titik kejadian transaksi, guna mengeliminasi potensi kebocoran sebelum dampak kerugian meluas. Kami menjaga disiplin pengembangan sistem yang sangat ketat sesuai standar operasional baku guna menjaga warisan bisnis klien dari risiko siber maupun kecurangan internal secara berkelanjutan. Melalui inovasi tanpa henti, V-Guard berupaya mendigitalkan rasa aman bagi setiap unit usaha yang berada di bawah perlindungan kami agar tumbuh dalam ekosistem yang efisien dan terlindungi selamanya.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# --- 5. HALAMAN ROI & PRODUK (SAVING 20% API) ---
elif st.session_state.page == "📊 ROI & Layanan":
    st.subheader("📈 ROI & Analisis Efisiensi API")
    col_roi, col_api = st.columns(2)
    with col_roi:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
        leak = st.slider("Kebocoran (%)", 5, 40, 20)
        st.markdown(f'<div class="roi-display"><h3>Dana Aman (ROI): Rp {(omzet * leak/100):,.0f}</h3><p>Dana Terkunci V-Guard</p></div>', unsafe_allow_html=True)
    with col_api:
        api_cost = st.number_input("Biaya Operasional API (Rp)", value=5000000)
        st.markdown(f"""
        <div class="api-saving-box">
            <p>🛡️ SOP EDGE FILTERING ACTIVE</p>
            <p style='font-size:22px;'>Biaya API Net: Rp {(api_cost * 0.8):,.0f}</p>
            <p style='color:#166534;'>Efisiensi 20%: Rp {(api_cost * 0.2):,.0f}</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    pkgs = {
        "V-LITE": ["Mikro / 1 Kasir", "• Filter Lokal<br>• WA Summary Notif", "1.5 Jt", "750 rb"],
        "V-PRO": ["Retail & Kafe", "• VCS Link Integration<br>• Bank Audit Link", "3 Jt", "1.5 Jt"],
        "V-SIGHT": ["Gudang & Toko", "• CCTV AI Behavior<br>• Visual Audit", "7.5 Jt", "3.5 Jt"],
        "V-ENTERPRISE": ["Korporasi", "• Core Brain AI<br>• Custom AI SOP", "15 Jt", "10 Jt"],
        "V-ULTRA": ["Investor/VIP", "• Executive Dash<br>• VIP Support", "25 Jt", "14.9 Jt"]
    }
    cols = st.columns(5)
    for i, (name, val) in enumerate(pkgs.items()):
        with cols[i]:
            st.markdown(f"""<div class="product-card"><div><div class="product-title">{name}</div><div style='color:#d63384; font-size:12px; font-weight:bold;'>{val[0]}</div><hr><div class="feature-list">{val[1]}</div></div><div style='background:#f1f5f9; padding:10px; border-radius:10px;'><small>Aktivasi: {val[2]}</small><br><b style='color:#2563eb; font-size:18px;'>Bln: {val[3]}</b></div></div>""", unsafe_allow_html=True)
            st.button(f"Pilih {name}", key=f"btn_{i}")

# --- 6. PORTAL KLIEN & ADMIN ---
elif st.session_state.page == "📱 Portal Klien":
    st.subheader("📱 Pendaftaran Klien Baru")
    with st.container(border=True):
        st.text_input("Nama Owner")
        st.file_uploader("Upload KTP", type=['jpg', 'png'])
        st.button("Daftar & Proteksi Aset", type="primary", use_container_width=True)

elif st.session_state.page == "🔒 Admin Portal":
    st.subheader("🔒 Executive Control Panel")
    if st.text_input("Password", type="password") == ADMIN_PW:
        st.success("Akses Diterima")
        st.metric("Dana Terproteksi", "Rp 128.5M", delta="+20% API Saved")
