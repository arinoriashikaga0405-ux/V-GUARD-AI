import streamlit as st

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. STYLE KONTRAS MAKSIMAL (CSS) ---
st.markdown("""
<style>
    .stApp { background-color: #001529 !important; }
    [data-testid="stSidebar"] { background-color: #000c17 !important; border-right: 1px solid #002140; }

    /* Memastikan Semua Teks Sidebar Putih Terang */
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] h3 {
        color: #ffffff !important; font-weight: bold !important;
    }

    /* Header Cyan untuk Judul Bagian */
    .cyan-header {
        color: #00f2ff !important; font-size: 1.5rem !important; font-weight: bold !important;
        margin-top: 20px !important; border-bottom: 2px solid #00f2ff33; padding-bottom: 5px;
    }

    /* Kotak Metrik */
    [data-testid="stMetric"] { background-color: #002140 !important; border: 1px solid #004a99 !important; border-radius: 12px !important; }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; }
    [data-testid="stMetricLabel"] > div { color: #f0c04a !important; }

    /* Tombol Logout & Kirim Laporan */
    .stButton>button[kind="secondary"] { background-color: #ff4b4b !important; color: white !important; border: none !important; width: 100% !important; }
    .stButton>button[kind="primary"] { background-color: #00f2ff !important; color: #001529 !important; font-weight: bold !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA LOGIN ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align: center; color: white;'>🛡️ V-GUARD AI LOGIN</h1>", unsafe_allow_html=True)
    with st.container():
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("Masuk"):
            if u == "admin" and p == "vguard2026":
                st.session_state.update({'logged_in': True, 'role': 'admin'})
                st.rerun()
    st.stop()

# --- 4. DASHBOARD UTAMA ---
if st.session_state['logged_in']:
    
    with st.sidebar:
        # Logo Section
        st.markdown("<div style='text-align: center;'><img src='https://cdn-icons-png.flaticon.com/512/1055/1055644.png' width='80'><h2 style='color: white;'>V-GUARD AI</h2></div>", unsafe_allow_html=True)
        st.divider()
        
        # Pengaturan AI
        st.markdown("### ⚙️ Pengaturan AI")
        st.selectbox("Mulai Operasional", ["08:00", "09:00", "10:00"], index=2)
        st.selectbox("Selesai Operasional", ["20:00", "21:00", "22:00"], index=2)
        st.success("🟢 Monitoring Aktif")
        
        st.divider()
        
        # NAVIGASI (Laporan Mingguan Ditambahkan Kembali)
        st.markdown("### Menu Navigasi")
        menu = st.radio("Nav", [
            "🔴 Executive Dashboard", 
            "📊 Laporan Mingguan",
            "⚫ Audit Engine", 
            "⚫ Finance & Payment"
        ], label_visibility="collapsed")
        
        st.divider()
        
        # Info Sesi & Logout
        st.markdown(f"<p style='color: white;'>Sesi: {st.session_state['role'].upper()}</p>", unsafe_allow_html=True)
        if st.button("Logout", key="out", type="secondary"):
            st.session_state['logged_in'] = False
            st.rerun()

    # --- LOGIKA TAMPILAN HALAMAN ---
    
    if menu == "🔴 Executive Dashboard":
        st.markdown("<h1 style='color: white;'>Executive Dashboard</h1>", unsafe_allow_html=True)
        m1, m2, m3 = st.columns(3)
        with m1: st.metric("Audit Bulan Ini", "1,284", "12%")
        with m2: st.metric("Anomali Terdeteksi", "42", "-5%", delta_color="inverse")
        with m3: st.metric("Revenue Terproteksi", "IDR 8.2B", "8%")

        st.markdown("<div class='cyan-header'>🔔 Monitor Invoice & Tagihan</div>", unsafe_allow_html=True)
        st.info("Fitur penagihan otomatis via WhatsApp aktif.")
        st.divider()
        st.markdown("<div class='cyan-header'>📽️ Live CCTV Audit</div>", unsafe_allow_html=True)
        st.image("https://via.placeholder.com/1000x400.png?text=Live+Audit+Active+Stream", use_column_width=True)

    elif menu == "📊 Laporan Mingguan":
        st.markdown("<h1 style='color: white;'>📊 Laporan Mingguan Klien</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color: white;'>Kirim rangkuman performa audit dan efisiensi dana ke klien secara otomatis.</p>", unsafe_allow_html=True)
        
        # Simulasi Daftar Laporan
        with st.container():
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.markdown("<div style='background: #002b55; padding: 15px; border-radius: 10px; border: 1px solid #00f2ff; color: white;'><b>LAPORAN_WEEK4_MARCH_VGUARD.PDF</b><br>Klien: Ko Shandy Vertigo | Periode: 21-28 Maret 2026</div>", unsafe_allow_html=True)
            with col_b:
                if st.button("🚀 Kirim Laporan", key="send_rep", type="primary"):
                    st.toast("Laporan Berhasil Terkirim ke WhatsApp Ko Shandy!")
        
        st.divider()
        st.markdown("<h3 style='color: white;'>Pratinjau Statistik Minggu Ini</h3>", unsafe_allow_html=True)
        st.bar_chart({"Kebocoran Dana": [10, 15, 5, 2], "Audit Sukses": [100, 120, 115, 130]})

    else:
        st.markdown(f"<h1 style='color: white;'>{menu}</h1>", unsafe_allow_html=True)
        st.warning("Halaman ini sedang dalam pengembangan.")
