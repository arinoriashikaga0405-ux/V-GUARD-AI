import streamlit as st
import os

# --- 1. SETTING HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

if 'menu' not in st.session_state:
    st.session_state.menu = "🏠 Visi & Misi"

# --- 2. CSS STANDAR VISUAL (PRESISI) ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #f8fafc; }
    .stButton>button { width: 100%; border-radius: 8px; text-align: left; padding: 10px; border: 1px solid #e2e8f0; background: white; margin-bottom: 5px; }
    .main-title { text-align: center; font-size: 30px; font-weight: 800; color: #1e3a8a; margin-bottom: 20px; }
    .justified-text { text-align: justify; line-height: 1.8; font-size: 15px; color: #333; }
    .roi-blue-box { background: #1e3a8a; color: white; padding: 40px; border-radius: 15px; text-align: center; margin-top: 20px; }
    .admin-green-box { background: #f0fdf4; border: 2px dashed #22c55e; color: #166534; padding: 30px; border-radius: 15px; text-align: center; }
    .product-card { border: 1px solid #e2e8f0; border-radius: 15px; padding: 20px; text-align: center; background: white; min-height: 450px; display: flex; flex-direction: column; justify-content: space-between; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGASI (SOP SEPARATED) ---
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD NAV")
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
    st.markdown('<div class="main-title">"Digitizing Trust, Eliminating Leakage"</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2.5])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
        else: st.info("Founder Photo")
    with c2:
        st.markdown('<div class="justified-text">', unsafe_allow_html=True)
        st.write("""
        **VISI:** Menjadi Jangkar Kepercayaan Digital dan Standar Global Integritas Bisnis V-Guard AI Intelligence bervisi untuk menjadi pilar utama dalam ekosistem bisnis global yang mengedepankan transparansi mutlak dan keamanan aset. 
        
        **MISI:** Eliminasi Kebocoran Aset Melalui Edge Intelligence dan Perlindungan Siber Berlapis. Kami secara proaktif mengidentifikasi anomali finansial tepat di titik kejadian transaksi untuk mengeliminasi potensi kebocoran sebelum dampak kerugian meluas.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# --- 5. DASHBOARD: ROI (DANA AMAN) ---
elif st.session_state.menu == "📊 ROI (Dana Aman)":
    st.subheader("📈 Kalkulator Kebocoran Dana (ROI)")
    omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
    leak_pct = st.slider("Estimasi Kebocoran (%)", 5, 40, 20)
    dana_aman = omzet * (leak_pct / 100)
    st.markdown(f'<div class="roi-blue-box"><h2>Potensi Dana Aman: Rp {dana_aman:,.0f}</h2><p>Kebocoran yang berhasil dihentikan oleh sistem V-Guard AI</p></div>', unsafe_allow_html=True)

# --- 6. DASHBOARD: LAYANAN PRODUK ---
elif st.session_state.menu == "📦 Layanan Produk":
    st.subheader("🏷️ Paket Layanan Strategis")
    pkgs = {
        "V-LITE": ["1 Kasir", "• Filter Lokal<br>• WA Summary Notif"],
        "V-PRO": ["Retail", "• VCS Integration<br>• Bank Audit Link"],
        "V-SIGHT": ["Gudang", "• AI CCTV Behavior<br>• Visual Audit"],
        "V-ENTERPRISE": ["Korporasi", "• Core Brain AI<br>• Dedicated Server"],
        "V-ULTRA": ["VIP", "• Executive Dash<br>• VIP Support"]
    }
    cols = st.columns(5)
    for i, (name, val) in enumerate(pkgs.items()):
        with cols[i]:
            st.markdown(f"""<div class="product-card"><div><h3>{name}</h3><small>{val[0]}</small><hr><div style='text-align:left; font-size:12px;'>{val[1]}</div></div><button style='width:100%; margin-top:10px;'>Pilih {name}</button></div>""", unsafe_allow_html=True)

# --- 7. DASHBOARD: PORTAL KLIEN ---
elif st.session_state.menu == "📱 Portal Klien":
    st.subheader("📱 Pendaftaran Klien")
    with st.container(border=True):
        st.text_input("Nama Owner")
        st.file_uploader("Upload Identitas (KTP)")
        st.button("Kunci Proteksi Sekarang")

# --- 8. DASHBOARD: ADMIN CENTER (LOGIKA 20% DISINI) ---
elif st.session_state.menu == "🔒 Admin Center":
    st.subheader("🔒 Executive Admin Control")
    pw = st.text_input("Master Password", type="password")
    if pw == "admin123": # Sesuaikan password
        st.write("### Analisis Efisiensi API Operasional")
        api_raw = st.number_input("Input Biaya API Mentah (Rp)", value=5000000)
        api_net = api_raw * 0.8
        st.markdown(f"""
            <div class="admin-green-box">
                <p>🛡️ SOP EDGE FILTERING ACTIVE</p>
                <h2>Biaya API Net: Rp {api_net:,.0f}</h2>
                <p>Profit Efisiensi (20%): Rp {api_raw * 0.2:,.0f}</p>
            </div>
            """, unsafe_allow_html=True)
