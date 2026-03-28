import streamlit as st

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. STYLE DARK BLUE & HIGH CONTRAST (CSS) ---
st.markdown("""
<style>
    /* Latar Belakang Utama Dark Blue */
    .stApp { background-color: #001529 !important; }
    
    /* Sidebar Darker Navy */
    [data-testid="stSidebar"] {
        background-color: #000c17 !important;
        border-right: 1px solid #002140;
    }

    /* Paksa semua teks di Sidebar & Main menjadi Putih Terang */
    [data-testid="stSidebar"] .stText, [data-testid="stSidebar"] label, [data-testid="stSidebar"] p, .stMarkdown p {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* Kotak Metrik (Card) */
    [data-testid="stMetric"] {
        background-color: #002140 !important;
        border: 1px solid #004a99 !important;
        border-radius: 12px !important;
        padding: 20px !important;
        border-left: 6px solid #f0c04a !important;
    }
    
    /* Nilai Metrik Putih Terang */
    [data-testid="stMetricValue"] > div { color: #ffffff !important; font-weight: bold !important; }
    [data-testid="stMetricLabel"] > div { color: #ced4da !important; }

    /* Tombol Logout & WA */
    div.stButton > button {
        border-radius: 8px !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA LOGIN ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    # Tampilan Halaman Depan / Login
    st.markdown("<h1 style='text-align: center; color: white;'>🛡️ V-GUARD AI SOLUTIONS</h1>", unsafe_allow_html=True)
    st.divider()
    with st.container():
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        if st.button("Masuk Ke Dashboard"):
            if user == "admin" and pwd == "vguard2026":
                st.session_state['logged_in'] = True
                st.session_state['role'] = "admin"
                st.rerun()
            elif user == "shandy" and pwd == "vertigo123":
                st.session_state['logged_in'] = True
                st.session_state['role'] = "client"
                st.rerun()
    st.stop()

# --- 4. DASHBOARD UTAMA (SIDEBAR LENGKAP KEMBALI) ---
if st.session_state['logged_in']:
    
    # --- SIDEBAR NAVIGASI (FITUR YANG HILANG ADA DI SINI) ---
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/1055/1055644.png", width=100)
        st.markdown("<h2 style='color: white;'>V-GUARD AI</h2>", unsafe_allow_html=True)
        st.divider()
        
        # Fitur 1: Pengaturan Operasional
        st.subheader("⚙️ Pengaturan AI")
        st.selectbox("Jam Mulai Operasional", ["08:00", "09:00", "10:00"], index=2)
        st.selectbox("Jam Selesai Operasional", ["20:00", "21:00", "22:00"], index=2)
        st.success("🟢 Monitoring Aktif")
        
        st.divider()
        
        # Fitur 2: Menu Navigasi (Sesuai Screenshot Laptop)
        st.subheader("Menu Navigasi")
        menu = st.radio("Pilih Menu:", [
            "🔴 Executive Dashboard", 
            "⚫ Audit Engine", 
            "⚫ Finance & Payment", 
            "⚫ HR & Payroll Monitoring"
        ], label_visibility="collapsed")
        
        st.divider()
        
        # Fitur 3: Informasi Akun & Logout
        st.write(f"User: **{st.session_state['role'].upper()}**")
        if st.button("Logout", use_container_width=True):
            st.session_state['logged_in'] = False
            st.rerun()

    # --- KONTEN UTAMA (DASHBOARD) ---
    st.markdown(f"<h1 style='color: white;'>{menu}</h1>", unsafe_allow_html=True)
    
    # Bagian Metrics
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="Audit Bulan Ini", value="1,284", delta="12%")
    with m2:
        st.metric(label="Anomali Terdeteksi", value="42", delta="-5%", delta_color="inverse")
    with m3:
        st.metric(label="Revenue Terproteksi", value="IDR 8.2B", delta="8%")

    st.divider()
    
    # Bagian Invoice & WA (Teks Putih Terang)
    st.subheader("🔔 Monitor Invoice & Tagihan")
    
    def baris_invoice(nama, tagihan, tgl, k_id):
        c_teks, c_btn = st.columns([4, 1])
        with c_teks:
            st.markdown(f"<p style='color: white; font-size: 1.1rem;'><b>{nama}</b> | {tagihan} | Tempo: {tgl}</p>", unsafe_allow_html=True)
        with c_btn:
            st.button("📩 Kirim WA", key=k_id)

    baris_invoice("Ko Shandy Vertigo", "Rp 5,000,000", "30 Maret 2026", "wa_s1")
    baris_invoice("Client SME B", "Rp 1,250,000", "02 April 2026", "wa_s2")

    st.divider()
    
    # Bagian CCTV
    st.subheader("📽️ Live CCTV Audit")
    st.text_input("Link RTSP/IP Cam:", "rtsp://admin:password@192.168.1.100:554/live")
    st.image("https://via.placeholder.com/1000x400.png?text=V-Guard+Live+Stream+Security+Active", use_column_width=True)
