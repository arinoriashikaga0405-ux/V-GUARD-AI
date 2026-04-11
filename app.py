import streamlit as st
import pandas as pd

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Executive Platform", page_icon="🛡️", layout="wide")

# Inisialisasi State Halaman
if 'page' not in st.session_state:
    st.session_state.page = "Visi & Misi"

# --- 2. CSS CUSTOM (CLEAN & PREMIUM) ---
st.markdown("""
    <style>
    .block-container { padding-top: 1rem; }
    .main { background-color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #0f172a !important; }
    
    /* Box Narasi Premium */
    .mission-box { 
        background-color: #ffffff; padding: 40px; border-radius: 15px; 
        border-left: 10px solid #1e3a8a; box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }
    .founder-sidebar-text { color: white; text-align: center; margin-top: 10px; }
    .card-paket {
        background-color: white; padding: 20px; border-radius: 12px;
        border: 1px solid #e2e8f0; text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (NAVIGASI LENGKAP) ---
with st.sidebar:
    try:
        st.image("erwin.jpg", use_container_width=True)
    except:
        st.info("Founder Photo (erwin.jpg)")
    
    st.markdown('<div class="founder-sidebar-text">', unsafe_allow_html=True)
    st.markdown("### **Erwin Sinaga**")
    st.caption("Founder & CEO V-GUARD AI")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    # Menu Navigasi Sesuai Permintaan
    st.session_state.page = st.radio("STRATEGIC MENU", [
        "Visi & Misi", 
        "Layanan Produk", 
        "ROI Analysis", 
        "Portal Klien", 
        "Admin Center"
    ])
    
    st.markdown("---")
    st.success("📉 Hemat API & Server: 20%")
    st.error("🚨 FIRE ALARM: ACTIVE")

# --- 4. KONTEN STRATEGIS ---

# A. HALAMAN VISI & MISI (250 KATA)
if st.session_state.page == "Visi & Misi":
    st.markdown("<h1 style='text-align:center; color:#1e3a8a;'>🛡️ VGUARD AI SYSTEMS</h1>", unsafe_allow_html=True)
    col_l, col_m, col_r = st.columns([0.5, 4, 0.5])
    with col_m:
        st.markdown(f"""
        <div class="mission-box">
        <h3>Visi Strategis: Digitizing Trust</h3>
        <p>V-Guard AI hadir sebagai jangkar teknologi global dalam misi <b>Digitalisasi Kepercayaan (Digitizing Trust)</b>. Kami mentransformasi ekosistem bisnis konvensional menjadi entitas digital yang sepenuhnya transparan, aman, dan berintegritas tinggi. Visi kami adalah menghapuskan paradigma kerugian akibat kelalaian manusia dan kecurangan sistemik melalui perlindungan mandiri yang bekerja otomatis di setiap lini transaksi. Kami membangun dunia di mana setiap pemilik usaha memiliki ketenangan pikiran total, memastikan bahwa pertumbuhan ekonomi perusahaan berdiri di atas pondasi kejujuran yang divalidasi oleh kecerdasan buatan, menjamin setiap rupiah yang masuk adalah murni hasil produktivitas yang terlindungi.</p>
        <br>
        <h3>Misi Operasional: Eliminating Leakage</h3>
        1. <b>Infrastruktur Integritas:</b> Membangun sistem digital yang mengonversi etika operasional menjadi data terukur secara real-time.<br>
        2. <b>Eliminasi Kebocoran (Leakage):</b> Teknologi Edge Filtering presisi tinggi untuk deteksi anomali finansial.<br>
        3. <b>Efisiensi API 20%:</b> Optimasi pemrosesan lokal untuk menekan biaya server dan cloud API.<br>
        4. <b>Kedaulatan Command Center:</b> Akses kontrol mutlak bagi Owner melalui sistem terenkripsi.<br>
        5. <b>Standarisasi SOP:</b> Disiplin pengembangan perangkat lunak sesuai standar operasional baku.
        </div>
        """, unsafe_allow_html=True)

# B. LAYANAN PRODUK
elif st.session_state.page == "Layanan Produk":
    st.title("📦 Layanan Produk & Paket")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="card-paket"><h3>V-LITE</h3><p>Proteksi Dasar Sensor & Laci</p><h4>Rp 2.5jt/bln</h4></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card-paket"><h3>V-PRO</h3><p>AI Fraud Detection & API Integration</p><h4>Rp 5jt/bln</h4></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="card-paket"><h3>V-ULTIMATE</h3><p>Full System & Visual Intelligence</p><h4>Custom</h4></div>', unsafe_allow_html=True)

# C. ROI ANALYSIS
elif st.session_state.page == "ROI Analysis":
    st.title("📊 ROI Analysis")
    st.write("Analisis penghematan biaya operasional dengan efisiensi API 20%.")
    st.metric("Estimasi Penghematan", "20%", "+Rp 15.000.000 / bln")

# D. PORTAL KLIEN
elif st.session_state.page == "Portal Klien":
    st.title("🔑 Client Access Portal")
    with st.columns(3)[1]:
        st.text_input("Username")
        st.text_input("Password", type="password")
        st.button("Login Ke Dashboard", use_container_width=True)

# E. ADMIN CENTER
elif st.session_state.page == "Admin Center":
    st.title("🎮 Admin Command Center")
    pwd = st.text_input("Master Key", type="password")
    if pwd == "vguard2026":
        st.subheader("🤖 Status 10 AI Squad")
        squad = pd.DataFrame({"Agen": ["Visionary", "Watchdog", "Sentinel", "Analyst", "Growth", "Liaison", "Treasurer", "Legalist", "Strategist", "Concierge"], "Status": ["Online"]*10})
        st.table(squad)

st.markdown("---")
st.markdown("<center>© 2026 V-GUARD AI | Digital Integrity Powered by Erwin Sinaga</center>", unsafe_allow_html=True)
