import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- 1. INISIALISASI SISTEM (Wajib di Atas) ---
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False
if 'audit_logs' not in st.session_state:
    st.session_state.audit_logs = [
        {"Klien": "Toko Berkah Jaya", "Status": "✅ Terpindai", "Waktu": "2026-03-30 21:05", "Hasil": "Aman"},
        {"Klien": "B2B Trading Sinar", "Status": "❌ Belum Upload", "Waktu": "-", "Hasil": "Pending"}
    ]

# --- 2. KONFIGURASI TAMPILAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 3. PREMIUM CUSTOM CSS ---
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

# --- 4. SIDEBAR CEO ---
with st.sidebar:
    try: st.image("erwin.jpg", width=120)
    except: st.info("👤 CEO: ERWIN SINAGA")
    st.markdown(f"### ERWIN SINAGA")
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

# --- 5. LOGIKA NAVIGASI HALAMAN ---
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
        # --- COMMAND CENTER - FULL STRATEGIC DASHBOARD ---
        st.header("💻 Command Center - Erwin Sinaga")
        
        # A. Executive Summary Metrics
        m1, m2, m3, m4 = st.columns(4)
        with m1: st.markdown('<div class="metric-card">💰 <b>Total Saved</b><br>Rp 1.450.000.000</div>', unsafe_allow_html=True)
        with m2: st.markdown('<div class="metric-card">👥 <b>Klien Aktif</b><br>12 Perusahaan</div>', unsafe_allow_html=True)
        with m3: st.markdown('<div class="metric-card">⚠️ <b>Fraud Alert</b><br>2 Temuan Hari Ini</div>', unsafe_allow_html=True)
        with m4: st.markdown('<div class="metric-card">✅ <b>System Health</b><br>99.9% Online</div>', unsafe_allow_html=True)
        
        st.write("---")
        
        # B. Navigasi Tab Strategis
        tabs = st.tabs(["🔍 V-Scan & Analisa", "📊 Monitoring Audit", "📍 Geolocation Map", "💰 Billing & AR", "⚙️ Manajemen Klien"])
        
        with tabs[0]: # V-SCAN DEEP DIVE
            st.markdown('<p class="header-text">🚀 V-SCAN: DEEP-DIVE ANALISA FRAUD</p>', unsafe_allow_html=True)
            klien = st.selectbox("Pilih Klien untuk Dianalisa:", ["Toko Berkah Jaya", "B2B Trading Sinar"])
            file = st.file_uploader(f"Unggah Data Transaksi {klien}", type=['csv', 'xlsx'])
            
            if file:
                with st.spinner('V-GUARD AI sedang membedah data...'):
                    time.sleep(2)
                    st.success(f"✅ Analisa Selesai untuk {klien}")
                    
                    st.markdown("### 📊 Tren Anomali Mingguan")
                    chart_data = pd.DataFrame({'Minggu': ['W1', 'W2', 'W3', 'W4'], 'Fraud': [5, 12, 3, 14]})
                    st.line_chart(chart_data.set_index('Minggu'))
                    
                    st.markdown(f'<div class="admin-card">📜 <b>Audit Trail:</b> Scan sukses dilakukan oleh CEO Erwin Sinaga pada {datetime.now().strftime("%H:%M:%S")}</div>', unsafe_allow_html=True)

                    res1, res2, res3 = st.columns(3)
                    res1.metric("Total Transaksi", "1.240", "Normal")
                    res2.metric("Anomali Terdeteksi", "14", "-2", delta_color="inverse")
                    res3.metric("Potensi Kebocoran", "Rp 3.420.000", "Critical")
                    
                    st.write("---")
                    c1, c2 = st.columns(2)
                    with c1: st.download_button("📥 DOWNLOAD REPORT (PDF)", data="Dummy PDF Content", file_name=f"Audit_{klien}.pdf")
                    with c2: 
                        if st.button("📲 KIRIM LAPORAN KE WA KLIEN"): st.success("Terkirim!")

        with tabs[1]: # MONITORING AUDIT
            st.markdown('<p class="header-text">📅 OTOMASI PENJADWALAN AUDIT</p>', unsafe_allow_html=True)
            st.table(pd.DataFrame(st.session_state.audit_logs))

        with tabs[2]: # GEOLOCATION MAP
            st.markdown('<p class="header-text">📍 GEOLOCATION MAP: SEBARAN KLIEN</p>', unsafe_allow_html=True)
            map_data = pd.DataFrame({'lat': [-6.2088, -6.1751, -6.2297], 'lon': [106.8456, 106.8272, 106.6894]})
            st.map(map_data)

        with tabs[3]: # BILLING & AR
            st.markdown('<p class="header-text">💵 STATUS TAGIHAN & BILLING</p>', unsafe_allow_html=True)
            st.table(pd.DataFrame({"Klien": ["Toko Berkah", "Sinar B2B"], "Status": ["Lunas", "Jatuh Tempo"]}))

        with tabs[4]: # MANAJEMEN KLIEN
            st.markdown('<p class="header-text">⚙️ PENDAFTARAN KLIEN BARU</p>', unsafe_allow_html=True)
            with st.form("new_client"):
                st.text_input("Nama Bisnis/Klien")
                st.selectbox("Paket AI", ["V-START", "V-GROW", "V-PRIME"])
                if st.form_submit_button("Simpan ke Database"): st.success("Klien Terdaftar!")

else:
    # --- BERANDA UTAMA ---
    st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns([1, 2.5])
    with col1:
        try: st.image("erwin.jpg", use_container_width=True)
        except: st.info("ERWIN SINAGA")
    with col2:
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        Erwin Sinaga adalah pemimpin strategis dengan rekam jejak sepuluh tahun sebagai eksekutif senior perbankan.
        Beliau merancang VGUARD AI dengan visi **"Digitizing Trust, Eliminating Leakage"**.
        """)
        if st.button("🚀 MASUK KE COMMAND CENTER (ADMIN)"):
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    st.markdown('<p class="header-text">📈 KALKULATOR PENYELAMATAN PROFIT (ROI)</p>', unsafe_allow_html=True)
    st.markdown('<div class="roi-box">', unsafe_allow_html=True)
    ca1, ca2 = st.columns(2)
    with ca1:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=250000000)
        kebocoran = st.slider("Tingkat Kebocoran (%)", 1, 15, 3) [cite: Screenshot 2
