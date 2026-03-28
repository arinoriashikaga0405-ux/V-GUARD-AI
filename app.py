import streamlit as st

# Konfigurasi Tema via CSS
st.markdown(f"""
    <style>
    /* Global Styles */
    .stApp {{
        background-color: #001529;
        color: white;
        font-family: 'Poppins', sans-serif;
    }}

    /* Sidebar Customization */
    [data-testid="stSidebar"] {{
        background-color: #000c17;
        border-right: 1px solid #00f2ff33;
    }}

    /* Metric Cards */
    .metric-card {{
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid #00f2ff;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }}
    .metric-value {{
        font-size: 2rem;
        font-weight: bold;
        color: #ffffff;
    }}
    .metric-label {{
        color: #00f2ff;
        font-size: 0.9rem;
    }}

    /* Buttons */
    .stButton>button {{
        background-color: #00f2ff;
        color: #001529;
        border-radius: 5px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        box-shadow: 0px 0px 15px #00f2ff;
        color: #001529;
    }}

    /* WA Button */
    .wa-button {{
        background-color: #ff4b4b !important;
        color: white !important;
        border: none;
        padding: 5px 15px;
        border-radius: 4px;
        text-decoration: none;
        font-size: 14px;
    }}
    </style>
    """, unsafe_allow_html=True)

# Contoh Struktur Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/shield.png") # Placeholder Logo Perisai
    st.title("V-GUARD AI")
    st.markdown("---")
    st.button("🏠 Executive Dashboard")
    st.button("🔍 Audit Engine")
    st.button("💰 Finance & Payment")
    st.markdown("---")
    st.subheader("Pengaturan AI")
    st.text_input("Jam Operasional", "10:00 - 22:00")
    st.success("🟢 Monitoring Aktif")
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🚪 Logout"):
        pass

# Contoh Main Dashboard
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="metric-card"><p class="metric-label">Audit Bulan Ini</p><p class="metric-value">1,284</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><p class="metric-label">Anomali Terdeteksi</p><p class="metric-value">12</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card" style="border-color:#FFD700;"><p class="metric-label">Revenue Terproteksi</p><p class="metric-value">Rp 450M</p></div>', unsafe_allow_html=True)

st.markdown("### 🎥 Live CCTV Audit")
st.text_input("Input RTSP URL", placeholder="rtsp://admin:password@ip_address")
st.image("https://images.unsplash.com/photo-1557683316-973673baf926?w=800", caption="Live Stream Placeholder")

st.markdown("### 🧾 Penagihan Klien")
st.write("Klien: PT. Maju Jaya | Status: Pending")
st.markdown('<a href="#" class="wa-button">🚀 Kirim WA</a>', unsafe_allow_html=True)
