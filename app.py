import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- 1. INITIALIZE SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False
if 'audit_logs' not in st.session_state:
    st.session_state.audit_logs = [
        {"Klien": "Toko Berkah Jaya", "Segmen": "Retail", "Jadwal": "21:00", "Status": "✅ Terpindai", "Hasil": "Aman"},
        {"Klien": "B2B Trading Sinar", "Segmen": "Trading", "Jadwal": "22:30", "Status": "❌ Belum Upload", "Hasil": "Pending"}
    ]

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 3. PREMIUM CSS (TAMPILAN EKSEKUTIF) ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; height: 45px; }
    .card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #e2e8f0; text-align: center; height: 100%; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .roi-box { background: #eff6ff; padding: 25px; border-radius: 15px; border: 2px dashed #1e3a8a; }
    .header-text { color: #1e3a8a; font-weight: bold; border-left: 5px solid #1e3a8a; padding-left: 10px; margin-bottom: 15px; }
    .metric-card { background: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; }
    .admin-card { background: #f1f5f9; padding: 15px; border-radius: 10px; border-left: 5px solid #1e3a8a; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("### 👤 CEO: ERWIN SINAGA")
    st.caption("Founder & CEO VGUARD AI")
    st.write("---")
    if st.button("🏠 Beranda Utama"): 
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.auth:
        if st.button("🔓 Log Out Admin"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 5. LOGIKA HALAMAN ---
if st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🔐 Executive Access</h1>', unsafe_allow_html=True)
        col_l1, col_l2, col_l3 = st.columns([1,2,1])
        with col_l2:
            pwd = st.text_input("Password Admin:", type="password")
            if st.button("Masuk ke Command Center"):
                if pwd == "VGUARD2026":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Akses Ditolak!")
    else:
        # --- COMMAND CENTER ---
        st.header("💻 Command Center - Erwin Sinaga")
        
        # Dashboard Visual (Metrics)
        m1, m2, m3, m4 = st.columns(4)
        with m1: st.markdown('<div class="metric-card">💰 <b>Total Saved</b><br>Rp 1.450.000.000</div>', unsafe_allow_html=True)
        with m2: st.markdown('<div class="metric-card">👥 <b>Klien Aktif</b><br>12 Perusahaan</div>', unsafe_allow_html=True)
        with m3: st.markdown('<div class="metric-card">⚠️ <b>Fraud Alert</b><br>2 Temuan Hari Ini</div>', unsafe_allow_html=True)
        with m4: st.markdown('<div class="metric-card">✅ <b>System Health</b><br>99.9% Online</div>', unsafe_allow_html=True)
        
        st.write("---")
        
        # Tabs Navigasi
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🔍 V-Scan & Analisa", "📊 Monitoring Audit", "📍 Geolocation Map", "💰 Billing & AR", "⚙️ Manajemen Klien"
        ])
        
        with tab1:
            st.markdown('<p class="header-text">🚀 V-SCAN: DEEP-DIVE ANALISA FRAUD</p>', unsafe_allow_html=True)
            klien_analisa = st.selectbox("Pilih Klien:", ["Toko Berkah Jaya", "B2B Trading Sinar"])
            uploaded_file = st.file_uploader(f"Unggah Data {klien_analisa}", type=['csv', 'xlsx'])
            if uploaded_file:
                with st.spinner('Menganalisa data transaksi...'):
                    time.sleep(2)
                    st.success("✅ Analisa Deep-Dive Selesai")
                    st.line_chart(pd.DataFrame({'Fraud': [5, 12, 3, 14]}))
                    st.markdown(f'<div class="admin-card">📜 <b>Audit Trail:</b> Analisa sukses oleh CEO pada {datetime.now().strftime("%H:%M:%S")}</div>', unsafe_allow_html=True)
                    c1, c2 = st.columns(2)
                    with c1: st.download_button("📥 DOWNLOAD PDF", data="Laporan", file_name="Audit.pdf")
                    with c2: 
                        if st.button("📲 KIRIM WHATSAPP"): st.success("Notifikasi Terkirim!")

        with tab2:
            st.markdown('<p class="header-text">📅 MONITORING KEPATUHAN & PENJADWALAN</p>', unsafe_allow_html=True)
            st.table(pd.DataFrame(st.session_state.audit_logs))
            col_b1, col_b2 = st.columns(2)
            with col_b1: st.button("📲 KIRIM REMINDER WA OTOMATIS")
            with col_b2: st.button("🔔 KIRIM NOTIFIKASI FRAUD")

        with tab3:
            st.markdown('<p class="header-text">📍 SEBARAN KLIEN V-GUARD</p>', unsafe_allow_html=True)
            st.map(pd.DataFrame({'lat': [-6.2088, -6.1751], 'lon': [106.8456, 106.8272]}))

        with tab4:
            st.markdown('<p class="header-text">💵 BILLING & AR CONTROL</p>', unsafe_allow_html=True)
            st.table(pd.DataFrame({"Klien": ["Toko Berkah", "Sinar B2B"], "Nilai": ["5JT", "10JT"], "Status": ["Lunas", "Jatuh Tempo"]}))

        with tab5:
            st.markdown('<p class="header-text">⚙️ PENDAFTARAN KLIEN BARU</p>', unsafe_allow_html=True)
            with st.form("new_client"):
                st.text_input("Nama Bisnis/Klien")
                st.selectbox("Pilih Paket", ["V-START", "V-GROW", "V-PRIME"])
                if st.form_submit_button("Simpan Klien ke Database"):
                    st.success("Klien Berhasil Terdaftar!")

else:
    # --- HALAMAN DEPAN (PROFIL CEO) ---
    st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.info("ERWIN SINAGA - CEO")
    with col2:
        st.subheader("👤 Profil & Filosofi")
        st.write("VGUARD AI: Membangun ekosistem bisnis tanpa kebocoran melalui integrasi AI.")
        if st.button("🚀 MASUK KE COMMAND CENTER"):
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    st.markdown('<p class="header-text">📈 KALKULATOR PENYELAMATAN PROFIT (ROI)</p>', unsafe_allow_html=True)
    st.markdown('<div class="roi-box">', unsafe_allow_html=True)
    omzet = st.number_input("Estimasi Omzet Bulanan (Rp)", value=250000000)
    kebocoran = st.slider("Tingkat Kebocoran (%)", 1, 15, 3)
    st.success(f"Potensi Profit Diselamatkan: Rp {(omzet * (kebocoran/100) * 0.95):,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
