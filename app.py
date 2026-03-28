import streamlit as st

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. STYLE DARK BLUE HIGH CONTRAST (CSS) ---
st.markdown("""
<style>
    /* Latar Belakang Utama Dark Blue Gelap */
    .stApp {
        background-color: #001529 !important;
    }
    
    /* Perbaikan Sidebar agar Terintegrasi */
    [data-testid="stSidebar"] {
        background-color: #000c17 !important;
        border-right: 1px solid #002140;
    }

    /* Perbaikan Kotak Metrik (Card Biru Tua) */
    [data-testid="stMetric"] {
        background-color: #002140 !important;
        border: 1px solid #004a99 !important;
        border-radius: 12px !important;
        padding: 20px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5) !important;
        border-left: 6px solid #f0c04a !important;
    }
    
    /* Paksa Teks Metrik Menjadi Putih Terang */
    [data-testid="stMetricValue"] > div { color: #ffffff !important; font-weight: bold !important; }
    [data-testid="stMetricLabel"] > div { color: #ffffff !important; opacity: 1 !important; }

    /* Gaya Khusus untuk Baris Invoice agar Sangat Jelas */
    .invoice-container {
        background-color: #002140;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 1px solid #004a99;
    }
    .invoice-text {
        color: #ffffff !important;
        font-weight: bold !important;
        font-size: 1.1rem;
    }

    /* Judul & Semua Teks Standar Menjadi Putih */
    h1, h2, h3, p, span, label, div { 
        color: #ffffff !important; 
    }

    /* Tombol Kirim WA (Hijau Menyala) */
    div.stButton > button {
        background-color: #25D366 !important; 
        color: white !important; 
        border-radius: 8px !important; 
        font-weight: bold !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA LOGIN ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    # Tampilan Login dengan Background Navy
    st.markdown("<h1 style='text-align: center;'>🛡️ V-GUARD AI LOGIN</h1>", unsafe_allow_html=True)
    with st.container():
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

# --- 4. DASHBOARD UTAMA (SETELAH LOGIN) ---
if st.session_state['logged_in']:
    
    # SIDEBAR
    with st.sidebar:
        # Menampilkan logo agar lebih jelas di background gelap
        st.image("https://cdn-icons-png.flaticon.com/512/1055/1055644.png", width=100)
        st.markdown("<h3>V-GUARD AI SOLUTIONS</h3>", unsafe_allow_html=True)
        st.divider()
        st.write(f"Sesi: **{st.session_state['role'].upper()}**")
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()

    # KONTEN UTAMA
    st.markdown("<h2>🔴 Executive Dashboard</h2>", unsafe_allow_html=True)
    
    # Row 1: Metrics
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="Audit Bulan Ini", value="1,284", delta="12%")
    with m2:
        st.metric(label="Anomali Terdeteksi", value="42", delta="-5%", delta_color="inverse")
    with m3:
        st.metric(label="Revenue Terproteksi", value="IDR 8.2B", delta="8%")

    st.divider()
    
    # Row 2: Monitor Invoice (TEKS PUTIH TERANG)
    st.markdown("<h3>🔔 Monitor Invoice Klien</h3>", unsafe_allow_html=True)
    
    def display_invoice(nama, total, tempo, key):
        st.markdown(f"""
        <div class="invoice-container">
            <span class="invoice-text">👤 {nama} | 💰 {total} | 📅 {tempo}</span>
        </div>
        """, unsafe_allow_html=True)
        st.button("📩 Kirim WA Sekarang", key=key)
        st.write("")

    display_invoice("Ko Shandy Vertigo", "Rp 5,000,000", "30 Maret 2026", "wa_1")
    display_invoice("Client SME B", "Rp 1,250,000", "02 April 2026", "wa_2")

    st.divider()
    
    # Row 3: CCTV
    st.markdown("<h3>📽️ Live CCTV Monitoring</h3>", unsafe_allow_html=True)
    st.text_input("URL CCTV (RTSP/IP Camera):", "rtsp://admin:password@192.168.1.100:554/live")
    st.image("https://via.placeholder.com/1000x400.png?text=V-Guard+Live+Stream+Security+Active", use_column_width=True)
