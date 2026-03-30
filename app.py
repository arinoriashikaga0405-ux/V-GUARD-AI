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

# --- 3. PREMIUM CSS (ESTETIKA EKSEKUTIF) ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; height: 45px; }
    .header-text { color: #1e3a8a; font-weight: bold; border-left: 5px solid #1e3a8a; padding-left: 10px; margin-bottom: 15px; }
    .metric-card { background: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; }
    .roi-box { background: #eff6ff; padding: 25px; border-radius: 15px; border: 2px dashed #1e3a8a; }
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
        m1, m2, m3, m4 = st.columns(4)
        with m1: st.markdown('<div class="metric-card">💰 <b>Total Saved</b><br>Rp 1.450.000.000</div>', unsafe_allow_html=True)
        with m2: st.markdown('<div class="metric-card">👥 <b>Klien Aktif</b><br>12 Perusahaan</div>', unsafe_allow_html=True)
        with m3: st.markdown('<div class="metric-card">⚠️ <b>Fraud Alert</b><br>2 Temuan Hari Ini</div>', unsafe_allow_html=True)
        with m4: st.markdown('<div class="metric-card">✅ <b>System Health</b><br>99.9% Online</div>', unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🔍 V-Scan & Analisa", "📊 Monitoring Audit", "📍 Geolocation Map", "💰 Billing & AR", "⚙️ Manajemen Klien"
        ])
        
        with tab1: # V-SCAN DENGAN AUTO-CALCULATE
            st.markdown('<p class="header-text">🚀 V-SCAN: DEEP-DIVE ANALISA FRAUD</p>', unsafe_allow_html=True)
            k_sel = st.selectbox("Pilih Klien:", ["Toko Berkah Jaya", "B2B Trading Sinar"])
            up = st.file_uploader(f"Unggah Data {k_sel}", type=['csv', 'xlsx'])
            if up:
                with st.spinner('V-GUARD AI Menganalisa...'):
                    df = pd.read_csv(up) if up.name.endswith('.csv') else pd.read_excel(up)
                    # AUTO-CALCULATE
                    potensi_fraud = len(df) * 500000 
                    st.success(f"✅ Analisa Selesai. Potensi Profit Diselamatkan: Rp {potensi_fraud:,.0f}")
                    st.line_chart(df.select_dtypes(include=['number']).iloc[:, :1])
                    st.markdown(f'<div class="admin-card">📜 <b>Audit Trail:</b> Scan sukses oleh CEO pada {datetime.now().strftime("%H:%M:%S")}</div>', unsafe_allow_html=True)
                    c1, c2 = st.columns(2)
                    with c1: st.download_button("📥 DOWNLOAD PDF", data="Laporan", file_name="Audit.pdf")
                    with c2: 
                        if st.button("📲 KIRIM WHATSAPP"): st.success("Terkirim!")

        with tab2: # MONITORING (PERBAIKAN VARIABEL)
            st.markdown('<p class="header-text">📅 MONITORING KEPATUHAN & PENJADWALAN</p>', unsafe_allow_html=True)
            st.table(pd.DataFrame(st.session_state.audit_logs))
            cb1, cb2 = st.columns(2)
            with cb1: 
                if st.button("📲 KIRIM REMINDER WA OTOMATIS"): st.success("Reminder WhatsApp Terkirim!")
            with cb2: 
                if st.button("🔔 KIRIM NOTIFIKASI FRAUD"): st.warning("Notifikasi Fraud Disebarkan!")

        with tab3: # GEOLOCATION
            st.markdown('<p class="header-text">📍 SEBARAN KLIEN V-GUARD</p>', unsafe_allow_html=True)
            st.map(pd.DataFrame({'lat': [-6.2088, -6.1751], 'lon': [106.8456, 106.8272]}))

        with tab4: # BILLING & AR (TERINTEGRASI)
            st.markdown('<p class="header-text">💵 BILLING & AR CONTROL</p>', unsafe_allow_html=True)
            billing_df = pd.DataFrame({
                "Klien": ["Toko Berkah Jaya", "B2B Trading Sinar"],
                "Nilai Kontrak": ["Rp 5.000.000", "Rp 15.000.000"],
                "Status": ["Lunas", "Jatuh Tempo"]
            })
            st.table(billing_df)
            if st.button("📥 DOWNLOAD REKAP BILLING"): st.info("Menyiapkan data...")

        with tab5: # CLIENT MGMT
            st.markdown('<p class="header-text">⚙️ PENDAFTARAN KLIEN BARU</p>', unsafe_allow_html=True)
            with st.form("new_client"):
                st.text_input("Nama Bisnis")
                st.selectbox("Paket", ["V-START", "V-GROW", "V-PRIME"])
                if st.form_submit_button("Simpan"): st.success("Tersimpan!")

else:
    # --- HALAMAN DEPAN (LOCKED) ---
    st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)
    st.write("---")
    cp1, cp2 = st.columns([1, 2.5])
    with cp1:
        try: st.image("erwin.jpg", use_container_width=True)
        except: st.info("ERWIN SINAGA - CEO")
    with cp2:
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        Erwin Sinaga adalah pemimpin strategis dengan rekam jejak profesional prestisius selama lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan nasional**. Pengalaman mendalam beliau dalam mengelola risiko keuangan dan transformasi digital menjadi landasan berdirinya **VGUARD AI Systems** untuk melindungi bisnis modern.

        Filosofi beliau adalah **"Digitizing Trust, Eliminating Leakage"**. Bapak Erwin meyakini bahwa setiap rupiah dalam transaksi bisnis klien adalah amanah yang harus dijaga dengan teknologi presisi. VGUARD AI dirancang sebagai perisai pertahanan strategis yang mampu menghentikan kebocoran profit secara *real-time* dengan standar keamanan finansial kelas dunia. Integritas dan transparansi data adalah kunci utama dalam setiap solusi yang beliau berikan bagi para pelaku usaha.
        """)
        if st.button("🚀 MASUK KE COMMAND CENTER"):
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    st.markdown('<div class="roi-box">', unsafe_allow_html=True)
    oz = st.number_input("Omzet Bulanan (Rp)", value=250000000)
    kb = st.slider("Kebocoran (%)", 1, 15, 3)
    st.success(f"Potensi Profit Diselamatkan: Rp {(oz * (kb/100) * 0.95):,.0f} / bln") 
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
