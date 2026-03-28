import streamlit as st

# --- 1. PENGATURAN HALAMAN & DESAIN (CSS) ---
st.set_page_config(page_title="V-GUARD AI", layout="wide")

st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stButton>button {
        width: 100%; border-radius: 8px; height: 3.5em;
        background-color: #004a99; color: white; font-weight: bold;
    }
    [data-testid="stMetric"] {
        background-color: white; padding: 15px; border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #e1e4e8;
    }
    .promo-card {
        background-color: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-left: 8px solid #004a99;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. LOGIKA LOGIN & SESSION ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- 3. HALAMAN DEPAN (PROMOSI) ---
if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align: center; color: #004a99;'>🛡️ V-GUARD AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem;'>Solusi AI untuk Keamanan Bisnis & Audit Real-time</p>", unsafe_allow_html=True)
    
    # Gambar Banner Teknologi
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1000&q=80", use_column_width=True)
    
    st.divider()

    # Kolom Fitur Unggulan
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='promo-card'><h3>🔍 Real-time Audit</h3><p>Deteksi kebocoran kasir otomatis menggunakan Google Gemini AI.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='promo-card'><h3>📱 WA Automation</h3><p>Laporan harian & penagihan piutang otomatis dikirim ke HP Bapak.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='promo-card'><h3>📹 Smart CCTV</h3><p>Pantau visual toko & kepatuhan karyawan secara remote & cerdas.</p></div>", unsafe_allow_html=True)

    st.divider()

    # Form Login Tersembunyi di bawah
    with st.expander("🔐 Masuk ke Dashboard Klien / Admin"):
        user_input = st.text_input("Username")
        pwd_input = st.text_input("Password", type="password")
        if st.button("Masuk"):
            if user_input == "admin" and pwd_input == "vguard2026":
                st.session_state['logged_in'] = True
                st.session_state['role'] = "admin"
                st.rerun()
            elif user_input == "shandy" and pwd_input == "vertigo123":
                st.session_state['logged_in'] = True
                st.session_state['role'] = "client"
                st.rerun()
            else:
                st.error("Username atau Password Salah")
    
    st.markdown("<p style='text-align: center; color: gray; margin-top: 50px;'>V-Guard AI © 2026 - By Erwin Sinaga</p>", unsafe_allow_html=True)
    st.stop() # Berhenti di sini jika belum login

# --- 4. DASHBOARD UTAMA (SETELAH LOGIN) ---
if st.session_state['logged_in']:
    
    # SIDEBAR
    with st.sidebar:
        st.title("🛡️ V-GUARD")
        st.write(f"Logged in as: **{st.session_state['role'].upper()}**")
        st.divider()
        
        if st.session_state['role'] == "admin":
            st.success("✅ Gemini AI Active")
            st.success("✅ WhatsApp Connected")
            st.info("🔵 System: Master Admin")
        else:
            st.success("🏢 Store: Vertigo (Shandy)")
            st.info("📶 Monitoring: Active")
            
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()

    # ISI DASHBOARD
    st.header(f"Dashboard {st.session_state['role'].capitalize()}")
    
    # Ringkasan Angka (Metrics)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="Total Turnover Today", value="Rp 12.500.000", delta="+8%")
    with m2:
        st.metric(label="Loss Detected", value="Rp 450.000", delta="-2%", delta_color="inverse")
    with m3:
        st.metric(label="System Accuracy", value="99.2%", delta="Sangat Baik")

    st.divider()

    # Area Konten (CCTV / Grafik)
    col_content, col_log = st.columns([2, 1])
    
    with col_content:
        st.subheader("📹 Live Camera Feed")
        st.image("https://via.placeholder.com/800x450.png?text=Live+CCTV+Streaming+V-Guard", use_column_width=True)
        
    with col_log:
        st.subheader("📑 Recent Activity")
        st.warning("15:45 - Gap detected at Cashier 1")
        st.info("15:30 - Daily report sent to WhatsApp")
        st.success("15:00 - Staff attendance verified")
