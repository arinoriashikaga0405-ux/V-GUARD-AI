import streamlit as st
import os
from dotenv import load_dotenv

# --- 1. KEAMANAN & SESSION ---
load_dotenv()
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

if 'page' not in st.session_state:
    st.session_state.page = "Landing"

# --- 2. CSS V-GUARD STANDAR SOP ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")
st.markdown("""
    <style>
    .main-slogan { text-align: center; font-size: 32px; font-weight: 800; color: #1e3a8a; margin-bottom: 10px; }
    .justified-text { text-align: justify; line-height: 1.8; font-size: 15px; background: white; padding: 25px; border-radius: 12px; border: 1px solid #e2e8f0; }
    .card-paket { border: 1px solid #e2e8f0; border-radius: 15px; padding: 20px; text-align: center; height: 500px; background: #fff; display: flex; flex-direction: column; justify-content: space-between; }
    .roi-display { background: #1e3a8a; color: white; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    .api-saving-box { background: #eff6ff; border: 1px dashed #1e3a8a; color: #1e3a8a; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. NAVIGASI SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD NAV")
    if st.button("🏠 Home (Visi Misi)", use_container_width=True): st.session_state.page = "Landing"
    if st.button("📊 ROI & Layanan", use_container_width=True): st.session_state.page = "Produk"
    if st.button("📱 Portal Klien", use_container_width=True): st.session_state.page = "Klien"
    if st.button("🔒 Admin Portal", use_container_width=True): st.session_state.page = "Admin"
    st.write("---")
    st.markdown("**SOP Status:** Active")

# --- 4. LANDING: VISI MISI 250 KATA ---
if st.session_state.page == "Landing":
    st.markdown('<div class="main-slogan">"Digitizing Trust, Eliminating Leakage"</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2.5])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
        else: st.info("👤 Founder Photo")
    with c2:
        st.markdown('<div class="justified-text">', unsafe_allow_html=True)
        st.write("""
        **VISI: Menjadi Jangkar Kepercayaan Digital dan Standar Global Integritas Bisnis** V-Guard AI Intelligence bervisi untuk menjadi pilar utama dalam ekosistem bisnis global yang mengedepankan transparansi mutlak dan keamanan aset berbasis kecerdasan buatan terdepan. Di tengah era volatilitas digital yang serba cepat, kami memposisikan diri sebagai "jangkar kepercayaan" bagi para pemilik bisnis dan investor. Kami tidak sekadar membangun perangkat lunak; kami membangun standar baru di mana integritas bisnis tidak lagi bersifat abstrak, melainkan menjadi data yang terukur, dapat diverifikasi, dan tidak dapat dimanipulasi secara sepihak. Kami bercita-cita untuk menciptakan dunia usaha yang bebas dari risiko sistemik, di mana setiap transaksi divalidasi oleh kebenaran digital yang absolut. Melalui teknologi kami, kepercayaan bukan lagi sebuah harapan, melainkan sebuah kepastian matematis yang mendasari setiap interaksi ekonomi.

        **MISI: Eliminasi Kebocoran Aset Melalui Edge Intelligence dan Perlindungan Siber Berlapis** Misi utama kami adalah memberdayakan pelaku bisnis melalui penerapan teknologi **Edge Filtering** yang mutakhir untuk membangun infrastruktur integritas digital yang mampu mengubah etika kerja menjadi parameter performa yang akurat. Dengan algoritma deteksi dini, V-Guard secara proaktif mengidentifikasi anomali finansial tepat di titik kejadian transaksi, guna mengeliminasi potensi kebocoran sebelum dampak kerugian meluas. Lebih dari itu, kami menjaga disiplin pengembangan sistem yang sangat ketat guna melindungi warisan bisnis klien dari risiko siber maupun kecurangan internal secara berkelanjutan. Melalui inovasi tanpa henti, V-Guard berupaya mendigitalkan rasa aman, memastikan setiap unit usaha dapat tumbuh secara eksponensial dalam ekosistem yang bersih, efisien, dan terlindungi selamanya.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# --- 5. PRODUK & ROI (20% SAVING PADA OPERASIONAL) ---
elif st.session_state.page == "Produk":
    st.subheader("📊 ROI & Analisis Efisiensi API")
    c_r1, c_r2 = st.columns(2)
    with c_r1: 
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
        leakage = st.slider("Leakage (%)", 5, 40, 20)
        st.markdown(f'<div class="roi-display"><h3>Potensi Dana Aman: Rp {(omzet * leakage/100):,.0f}</h3></div>', unsafe_allow_html=True)
    
    with c_r2:
        api_raw = st.number_input("Biaya Operasional API (Rp)", value=5000000)
        api_final = api_raw * 0.80  # PEMOTONGAN 20% DISINI
        st.markdown(f"""
        <div class="api-saving-box">
            <p>SOP EDGE FILTERING ACTIVE</p>
            <p style="font-size:20px;">Biaya API Setelah Hemat 20%: <br>Rp {api_final:,.0f}</p>
            <small>Hemat: Rp {(api_raw * 0.2):,.0f} (Net Profit)</small>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    pkgs = {
        "V-LITE": ["1 Kasir", "• Anomali Filter<br>• WA Summary", "1.5 Jt", "750 rb"],
        "V-PRO": ["Retail", "• VCS Link<br>• Fraud API", "3 Jt", "1.5 Jt"],
        "V-SIGHT": ["Gudang", "• AI Behavior<br>• Visual Audit", "7.5 Jt", "3.5 Jt"],
        "V-ENTERPRISE": ["Korporat", "• Dedicated Srv<br>• Custom SOP", "15 Jt", "10 Jt"],
        "V-ULTRA": ["VIP", "• Exec Dash<br>• VIP Support", "25 Jt", "14.9 Jt"]
    }
    cols = st.columns(5)
    for i, (name, val) in enumerate(pkgs.items()):
        with cols[i]:
            st.markdown(f'<div class="card-paket"><div><b>{name}</b><br><small>{val[0]}</small><hr><div style="text-align:left;font-size:12px;">{val[1]}</div></div><div style="background:#f1f5f9;padding:10px;border-radius:10px;"><small>Aktif: {val[2]}</small><br><b>Bln: {val[3]}</b></div></div>', unsafe_allow_html=True)
            st.button(f"Pilih {name}", key=f"pk_{i}", use_container_width=True)

# --- 6. PORTAL KLIEN ---
elif st.session_state.page == "Klien":
    st.subheader("📱 Portal Pendaftaran")
    with st.container(border=True):
        st.text_input("Nama Owner")
        st.file_uploader("Upload KTP (Verifikasi AI)", type=['jpg','png'])
        st.button("Daftar & Kunci Aset", type="primary", use_container_width=True)

# --- 7. ADMIN PORTAL ---
elif st.session_state.page == "Admin":
    st.subheader("🔒 Admin Control")
    with st.expander("Login"):
        if st.text_input("Password", type="password") == ADMIN_PASSWORD:
            st.success("Akses Diterima")
            st.metric("Dana Terproteksi", "Rp 1.2M", delta="Efficiency +20%")
