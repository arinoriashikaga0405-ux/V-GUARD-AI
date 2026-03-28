import streamlit as st

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. STYLE DARK BLUE PREMIUM (CSS) ---
st.markdown("""
<style>
    /* Latar Belakang Utama Dark Blue */
    .main { 
        background-color: #001f3f; 
    }
    
    /* Perbaikan Sidebar agar Senada */
    [data-testid="stSidebar"] {
        background-color: #001529 !important;
        border-right: 1px solid #003366;
    }

    /* Perbaikan Kotak Metrik (Card) */
    [data-testid="stMetric"] {
        background-color: #002b55 !important;
        border: 1px solid #004080 !important;
        border-radius: 15px !important;
        padding: 20px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
        border-left: 6px solid #f0c04a !important; /* Garis Kuning Khas V-Guard */
    }
    
    /* Warna Teks Metrik (Putih Terang) */
    [data-testid="stMetricValue"] > div { color: #ffffff !important; font-weight: bold !important; }
    [data-testid="stMetricLabel"] > div { color: #ced4da !important; }

    /* Judul & Teks Utama (Putih & Terang) */
    h1, h2, h3, p, span, label { 
        color: #ffffff !important; 
    }
    
    /* Khusus untuk teks Invoice agar terbaca jelas */
    .invoice-text {
        color: #ffffff !important;
        font-size: 1.1rem;
        font-weight: 500;
        background: rgba(255, 255, 255, 0.05);
        padding: 10px;
        border-radius: 8px;
    }

    /* Tombol Kirim WA (Hijau WhatsApp) */
    div.stButton > button {
        background-color: #25D366; 
        color: white; 
        border-radius: 8px; 
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #128C7E;
        transform: scale(1.02);
    }

    /* Input Box & Selectbox */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #003366 !important;
        color: white !important;
        border: 1px solid #004a99 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA AKSES ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- 4. TAMPILAN DEPAN (PROMOSI) ---
if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align: center;'>🛡️ V-GUARD AI SOLUTIONS</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1000&q=80", use_column_width=True)
    st.divider()
    with st.expander("🔐 MASUK KE DASHBOARD"):
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        if st.button("Masuk Sekarang"):
            if user == "admin" and pwd == "vguard2026":
                st.session_state['logged_in'] = True
                st.session_state['role'] = "admin"
                st.rerun()
            elif user == "shandy" and pwd == "vertigo123":
                st.session_state['logged_in'] = True
                st.session_state['role'] = "client"
                st.rerun()
    st.stop()

# --- 5. DASHBOARD UTAMA (DARK BLUE THEME) ---
if st.session_state['logged_in']:
    
    # --- SIDEBAR ---
    with st.sidebar:
        # Gunakan logo V-Guard Bapak
        st.image("https://cdn-icons-png.flaticon.com/512/1055/1055644.png", width=120) 
        st.markdown("<h2 style='text-align: center;'>V-GUARD AI</h2>", unsafe_allow_html=True)
        st.divider()
        
        st.subheader("⚙️ Pengaturan AI")
        st.selectbox("Jam Mulai Operasional", ["08:00", "09:00", "10:00"], index=2)
        st.selectbox("Jam Selesai Operasional", ["20:00", "21:00", "22:00"], index=2)
        st.success("🟢 Monitoring Aktif")
        
        st.divider()
        st.subheader("Navigation")
        st.markdown("🔴 **Executive Dashboard**")
        st.markdown("⚪ **Audit Engine**")
        st.markdown("⚪ **Finance & Payment**")
        
        if st.button("Logout", key="logout_btn"):
            st.session_state['logged_in'] = False
            st.rerun()

    # --- ISI DASHBOARD ---
    st.markdown("<h2>🔴 Executive Dashboard</h2>", unsafe_allow_html=True)
    
    # Kolom Metrik
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="Audit Bulan Ini", value="1,284", delta="12%")
    with m2:
        st.metric(label="Anomali Terdeteksi", value="42", delta="-5%", delta_color="inverse")
    with m3:
        st.metric(label="Revenue Terproteksi", value="IDR 8.2B", delta="8%")

    st.divider()
    
    # Monitor Invoice (Sekarang Teks Putih & Terbaca Jelas)
    st.markdown("<h3>🔔 Monitor Invoice Klien</h3>", unsafe_allow_html=True)
    
    def invoice_item(nama, total, tempo, key):
        col_txt, col_btn = st.columns([4, 1])
        with col_txt:
            st.markdown(f"<div class='invoice-text'><b>{nama}</b> | Total: {total} | Tempo: {tempo}</div>", unsafe_allow_html=True)
        with col_btn:
            st.button("📩 Kirim WA", key=key)

    invoice_item("Ko Shandy Vertigo", "Rp 5,000,000", "30 Maret 2026", "wa1")
    invoice_item("Client SME B", "Rp 1,250,000", "02 April 2026", "wa2")

    st.divider()
    
    # CCTV Section
    st.markdown("<h3>📽️ Live CCTV Monitoring</h3>", unsafe_allow_html=True)
    st.text_input("URL CCTV (RTSP/IP Camera):", "rtsp://admin:password@192.168.1.100:554/live")
    # Placeholder Video/Image
    st.image("https://via.placeholder.com/1000x400.png?text=V-Guard+Live+Stream+Security+Active", use_column_width=True)
