import streamlit as st

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. STYLE PREMIUM (HIGH-CONTRAST DARK THEME) ---
st.markdown("""
<style>
    /* Latar belakang utama */
    .main { background-color: #0e1117; }
    
    /* Perbaikan Kotak Metrik (Kartu Biru/Gelap) */
    [data-testid="stMetric"] {
        background-color: #1a1c24 !important;
        border: 1px solid #30363d !important;
        border-radius: 12px !important;
        padding: 20px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5) !important;
        border-left: 6px solid #f0c04a !important;
    }
    
    /* Paksa warna teks metrik agar putih terang */
    [data-testid="stMetricValue"] > div { color: #ffffff !important; font-size: 2rem !important; font-weight: bold !important; }
    [data-testid="stMetricLabel"] > div { color: #a1a1a1 !important; font-size: 1rem !important; }

    /* Styling Sidebar */
    .stSidebar { background-color: #0e1117 !important; border-right: 1px solid #30363d; }
    
    /* Tombol Kirim WA agar lebih mencolok */
    div.stButton > button {
        background-color: #075E54; color: white; border-radius: 8px; border: none; font-weight: bold;
    }
    div.stButton > button:hover { background-color: #128C7E; color: white; border: 1px solid white; }

    /* Halaman Depan (Iklan) */
    .promo-card {
        background-color: white; color: #333; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-left: 8px solid #004a99; margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA AKSES ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- 4. TAMPILAN DEPAN (PROMOSI PUBLIK) ---
if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align: center; color: #004a99;'>🛡️ V-GUARD AI SOLUTIONS</h1>", unsafe_allow_html=True)
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

# --- 5. DASHBOARD UTAMA (SETELAH LOGIN) ---
if st.session_state['logged_in']:
    
    # --- SIDEBAR ---
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/1055/1055644.png", width=80)
        st.title("V-GUARD AI")
        st.divider()
        
        st.subheader("⚙️ Pengaturan AI")
        st.selectbox("Jam Mulai Operasional", ["08:00", "09:00", "10:00"], index=2)
        st.selectbox("Jam Selesai Operasional", ["20:00", "21:00", "22:00"], index=2)
        st.success("🟢 Monitoring Aktif")
        
        st.divider()
        st.subheader("Navigation")
        st.write("🔴 **Executive Dashboard**")
        st.write("⚪ Audit Engine")
        st.write("⚪ Finance & Payment")
        
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()

    # --- ISI UTAMA ---
    st.markdown("<h2 style='color: white;'>🔴 Executive Dashboard</h2>", unsafe_allow_html=True)
    
    # Row 1: Metrics (Dibuat lebih rapi & kontras)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="Audit Bulan Ini", value="1,284", delta="12%")
    with m2:
        st.metric(label="Anomali Terdeteksi", value="42", delta="-5%")
    with m3:
        st.metric(label="Revenue Terproteksi", value="IDR 8.2B", delta="8%")

    st.divider()
    
    # Row 2: Monitor Invoice (Gunakan Kolom agar rapi)
    st.markdown("<h3 style='color: white;'>🔔 Monitor Invoice Klien</h3>", unsafe_allow_html=True)
    
    def invoice_row(nama, total, tempo, key):
        col_text, col_btn = st.columns([4, 1])
        with col_text:
            st.markdown(f"<p style='color: #e0e0e0; margin-bottom: 0;'><b>{nama}</b> | Total: {total} | Tempo: {tempo}</p>", unsafe_allow_html=True)
        with col_btn:
            st.button(f"📩 Kirim WA", key=key)

    invoice_row("Ko Shandy Vertigo", "Rp 5,000,000", "30 Maret 2026", "btn_shandy")
    invoice_row("Client SME B", "Rp 1,250,000", "02 April 2026", "btn_smeb")

    st.divider()
    
    # Row 3: CCTV
    st.markdown("<h3 style='color: white;'>📽️ Live CCTV Monitoring</h3>", unsafe_allow_html=True)
    st.text_input("URL CCTV (RTSP/IP Camera):", "rtsp://admin:password@192.168.1.100:554/live")
    st.image("https://via.placeholder.com/1000x400.png?text=Live+CCTV+Stream+V-Guard+Active", use_column_width=True)
