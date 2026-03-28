import streamlit as st

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. STYLE MEWAH (DARK THEME & CARD) ---
st.markdown("""
<style>
    .main { background-color: #0e1117; color: white; }
    [data-testid="stMetric"] {
        background-color: #1a1c24; padding: 20px; border-radius: 10px;
        border-left: 5px solid #f0c04a; box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .stSidebar { background-color: #0e1117 !important; border-right: 1px solid #333; }
    .promo-card {
        background-color: #ffffff; color: #333; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-left: 8px solid #004a99;
    }
    div.stButton > button {
        background-color: #004a99; color: white; border-radius: 8px; width: 100%; height: 3.5em;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA AKSES ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- 4. TAMPILAN DEPAN (LANDING PAGE PROMOSI) ---
if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align: center; color: #004a99;'>🛡️ V-GUARD AI SOLUTIONS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #555;'>Loss Detection & SME Management System</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1000&q=80", use_column_width=True)
    
    st.divider()
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='promo-card'><h3>🔍 Audit Engine</h3><p>Verifikasi struk vs visual CCTV otomatis.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='promo-card'><h3>💰 Revenue Guard</h3><p>Proteksi omzet dari kebocoran internal.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='promo-card'><h3>📱 WA Automation</h3><p>Tagih invoice & kirim laporan otomatis.</p></div>", unsafe_allow_html=True)

    st.divider()
    with st.expander("🔐 LOGIN AREA (CLIENT & ADMIN)"):
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        if st.button("Login"):
            if user == "admin" and pwd == "vguard2026":
                st.session_state['logged_in'] = True
                st.session_state['role'] = "admin"
                st.rerun()
            elif user == "shandy" and pwd == "vertigo123":
                st.session_state['logged_in'] = True
                st.session_state['role'] = "client"
                st.rerun()
    st.stop()

# --- 5. DASHBOARD ASLI (SESUAI SCREENSHOT BAPAK) ---
if st.session_state['logged_in']:
    
    # --- SIDEBAR NAVIGASI ---
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/1055/1055644.png", width=100)
        st.title("V-GUARD AI SOLUTIONS")
        st.divider()
        
        st.subheader("⚙️ Pengaturan AI")
        st.selectbox("Jam Mulai Operasional", ["08:00", "09:00", "10:00"], index=2)
        st.selectbox("Jam Selesai Operasional", ["20:00", "21:00", "22:00"], index=2)
        st.success("🟢 Status: AI Monitoring Aktif")
        
        st.divider()
        st.subheader("Navigation")
        st.radio("Menu", ["🔴 Executive Dashboard", "⚫ Audit Engine", "⚫ Finance & Payment", "⚫ HR & Payroll Monitoring"], label_visibility="collapsed")
        
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()

    # --- MAIN CONTENT ---
    # Header Metrics (Kartu Biru)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="Audit Bulan Ini", value="1,284")
    with m2:
        st.metric(label="Anomali Terdeteksi", value="42")
    with m3:
        st.metric(label="Revenue Terproteksi", value="IDR 8.2B")

    st.divider()
    
    # Monitor Invoice (Sesuai Screenshot)
    st.subheader("🔔 Monitor Invoice Klien")
    col_inv1, col_btn1 = st.columns([4, 1])
    with col_inv1:
        st.write("**Ko Shandy Vertigo** | Total: Rp 5,000,000 | Tempo: 30 Maret 2026")
    with col_btn1:
        st.button("📩 Kirim WA", key="btn1")
        
    col_inv2, col_btn2 = st.columns([4, 1])
    with col_inv2:
        st.write("**Client SME B** | Total: Rp 1,250,000 | Tempo: 02 April 2026")
    with col_btn2:
        st.button("📩 Kirim WA", key="btn2")

    st.divider()
    
    # Live CCTV Monitoring
    st.subheader("📽️ Live CCTV Monitoring")
    st.text_input("Masukkan URL CCTV (RTSP/IP Camera):", "rtsp://admin:password@192.168.1.100:554/live")
    with st.expander("Cara mendapatkan URL CCTV"):
        st.write("Pastikan IP Camera Anda sudah mendukung protokol RTSP dan Port Forwarding sudah aktif.")
