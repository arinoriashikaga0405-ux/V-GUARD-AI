import streamlit as st
import pandas as pd

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI SOLUTIONS", layout="wide", initial_sidebar_state="expanded")

# --- 2. CSS MASTER: IDENTITAS VISUAL V-GUARD ---
st.markdown("""
<style>
    /* Background & Font Utama */
    .stApp { background-color: #001529 !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* --- CSS LANDING PAGE PROMOSI --- */
    .hero-banner {
        width: 100%;
        border-radius: 15px;
        overflow: hidden;
        margin-bottom: 30px;
        border: 2px solid #00f2ff;
    }
    .promo-title { color: #00f2ff; font-size: 2.5rem; font-weight: bold; text-align: center; margin-bottom: 10px; }
    .promo-subtitle { color: white; text-align: center; font-size: 1.2rem; margin-bottom: 40px; }
    
    /* --- CSS LOGIN BOX --- */
    .login-box {
        background-color: #002140;
        padding: 40px;
        border-radius: 15px;
        border: 1px solid #00f2ff;
        box-shadow: 0 10px 25px rgba(0,242,255,0.2);
    }

    /* --- CSS DASHBOARD (DIKUNCI) --- */
    [data-testid="stSidebar"] { background-color: #000c17 !important; border-right: 2px solid #FFD700; }
    [data-testid="stSidebar"] * { color: #ffffff !important; }
    
    /* Metrik Kontras Tinggi */
    [data-testid="stMetric"] { 
        background-color: #002140 !important; 
        border: 2px solid #004a99 !important; 
        border-radius: 12px !important; 
        padding: 20px !important; 
    }
    [data-testid="stMetricValue"] > div { color: #ffffff !important; font-weight: bold !important; font-size: 2rem !important; }
    [data-testid="stMetricLabel"] > div { color: #FFD700 !important; font-weight: bold !important; font-size: 1.1rem !important; }

    /* Tombol-Tombol */
    .stButton>button { border-radius: 8px !important; font-weight: bold !important; }
    .btn-login>div>button { background-color: #00f2ff !important; color: #001529 !important; width: 100% !important; }
    .btn-wa>div>button { background-color: #ff4b4b !important; color: white !important; }
    .btn-logout>div>button { background-color: #ff4b4b !important; color: white !important; width: 100% !important; }

    /* Header Section */
    .cyan-header {
        color: #00f2ff !important; font-size: 1.5rem !important; font-weight: bold !important;
        border-bottom: 2px solid #00f2ff; padding-bottom: 10px; margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA NAVIGASI (SESSION STATE) ---
if 'page' not in st.session_state:
    st.session_state['page'] = 'promo' # Halaman default adalah promosi

# --- 4. TAMPILAN HALAMAN PROMOSI (LANDING PAGE) ---
if st.session_state['page'] == 'promo':
    # Banner Sirkuit (Berdasarkan Screenshot 2026-03-28 171652.jpg)
    st.markdown("""
        <div class="hero-banner">
            <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80" style="width:100%;">
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='promo-title'>🛡️ V-GUARD AI SOLUTIONS</div>", unsafe_allow_html=True)
    st.markdown("<div class='promo-subtitle'>Sistem Audit & Proteksi Revenue Berbasis AI Terintegrasi</div>", unsafe_allow_html=True)

    # Box Login Terintegrasi di Landing Page
    _, col_mid, _ = st.columns([1, 1.5, 1])
    with col_mid:
        with st.container():
            st.markdown("<div class='login-box'>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align: center; color: white;'>🔑 Masuk ke Dashboard</h3>", unsafe_allow_html=True)
            u = st.text_input("Username / Email", placeholder="admin@vguard.ai")
            p = st.text_input("Password", type="password", placeholder="••••••••")
            
            st.markdown("<div class='btn-login'>", unsafe_allow_html=True)
            if st.button("MASUK SEKARANG"):
                if u == "admin" and p == "vguard2026":
                    st.session_state['page'] = 'dashboard'
                    st.rerun()
                else:
                    st.error("Akses ditolak. Periksa kembali kredensial Anda.")
            st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Footer Promosi
    st.markdown("<p style='text-align: center; color: gray; margin-top: 50px;'>© 2026 V-GUARD AI Solutions. All Rights Reserved.</p>", unsafe_allow_html=True)

# --- 5. TAMPILAN DASHBOARD (ADMIN & KLIEN) ---
elif st.session_state['page'] == 'dashboard':
    
    # SIDEBAR (Mempertahankan Logo Perisai Emas & Fitur Pengaturan)
    with st.sidebar:
        st.markdown("""
            <div style='text-align: center;'>
                <img src='https://cdn-icons-png.flaticon.com/512/1055/1055644.png' width='100' style='filter: drop-shadow(0 0 10px #FFD700);'>
                <h2 style='color: #FFD700;'>V-GUARD AI</h2>
            </div>
        """, unsafe_allow_html=True)
        st.divider()
        
        # Fitur Pengaturan AI
        st.markdown("### ⚙️ Pengaturan AI")
        st.selectbox("Jam Mulai Operasional", ["08:00", "09:00", "10:00"], index=2)
        st.selectbox("Jam Selesai Operasional", ["20:00", "21:00", "22:00"], index=2)
        st.success("🟢 Status: AI Monitoring Aktif")
        
        st.divider()
        st.markdown("### Menu Navigasi")
        menu = st.radio("Pilih Halaman:", [
            "🔴 Executive Dashboard", 
            "📊 Laporan Mingguan",
            "⚫ Audit Engine", 
            "⚫ Finance & Payment",
            "⚫ HR Monitoring"
        ])
        
        st.divider()
        st.write("Sesi: **ADMIN**")
        st.markdown("<div class='btn-logout'>", unsafe_allow_html=True)
        if st.button("LOGOUT"):
            st.session_state['page'] = 'promo'
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # KONTEN UTAMA DASHBOARD
    if menu == "🔴 Executive Dashboard":
        st.markdown("<h1 style='color: white;'>🔵 Executive Dashboard</h1>", unsafe_allow_html=True)
        
        # Kolom Metrik (Putih & Tebal)
        col1, col2, col3 = st.columns(3)
        col1.metric("Audit Bulan Ini", "1,284", "12%")
        col2.metric("Anomali Terdeteksi", "42", "-5%", delta_color="inverse")
        col3.metric("Revenue Terproteksi", "IDR 8.2B", "8%")

        # Monitor Invoice Klien
        st.markdown("<div class='cyan-header'>🔔 Monitor Invoice Klien</div>", unsafe_allow_html=True)
        def inv_card(nama, total, tempo, key):
            c1, c2 = st.columns([4, 1])
            with c1:
                st.markdown(f"""
                    <div style='background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 5px solid #00f2ff;'>
                        <span style='color: white; font-weight: bold; font-size: 1.1rem;'>👤 {nama}</span><br>
                        <span style='color: #FFD700;'>Total: {total}</span> | <span style='color: #aaa;'>Tempo: {tempo}</span>
                    </div>
                """, unsafe_allow_html=True)
            with c2:
                st.markdown("<div class='btn-wa'>", unsafe_allow_html=True)
                st.button("✉️ Kirim WA", key=key, use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)

        inv_card("Ko Shandy Vertigo", "Rp 5.000.000", "30 Maret 2026", "wa1")
        inv_card("Client SME B", "Rp 1.250.000", "02 April 2026", "wa2")

        # Live CCTV Monitoring
        st.markdown("<div class='cyan-header'>📽️ Live CCTV Monitoring</div>", unsafe_allow_html=True)
        st.text_input("Masukkan URL CCTV (RTSP/IP Camera):", "rtsp://admin:password@192.168.1.100:554/live")
        st.image("https://via.placeholder.com/1200x500.png?text=V-GUARD+LIVE+AI+AUDIT+STREAMING", use_column_width=True)

    elif menu == "📊 Laporan Mingguan":
        st.markdown("<h1 style='color: white;'>📊 Laporan Mingguan</h1>", unsafe_allow_html=True)
        st.info("Fitur simulasi pengiriman laporan mingguan ke klien aktif.")
        chart_data = pd.DataFrame({"Data": [10, 25, 15, 30]})
        st.bar_chart(chart_data, color="#00f2ff")
