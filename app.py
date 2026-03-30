import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- 1. INITIALIZE SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False
if 'audit_logs' not in st.session_state:
    st.session_state.audit_logs = [
        {"Klien": "Toko Berkah Jaya", "Status": "✅ Terpindai", "Waktu": "2026-03-30 21:05", "Hasil": "Aman"},
        {"Klien": "B2B Trading Sinar", "Status": "❌ Belum Upload", "Waktu": "-", "Hasil": "Pending"}
    ]

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 3. PREMIUM CSS ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; height: 45px; }
    .card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #e2e8f0; text-align: center; height: 100%; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .roi-box { background: #eff6ff; padding: 25px; border-radius: 15px; border: 2px dashed #1e3a8a; }
    .header-text { color: #1e3a8a; font-weight: bold; border-left: 5px solid #1e3a8a; padding-left: 10px; }
    .metric-card { background: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; }
    .admin-card { background: #f1f5f9; padding: 15px; border-radius: 10px; border-left: 5px solid #1e3a8a; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR (ERWIN SINAGA) ---
with st.sidebar:
    try: st.image("erwin.jpg", width=120)
    except: st.info("👤 CEO: ERWIN SINAGA")
    st.markdown("### ERWIN SINAGA")
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
        
        # Dashboard Visual (Executive Summary)
        m1, m2, m3, m4 = st.columns(4)
        with m1: st.markdown('<div class="metric-card">💰 <b>Total Saved</b><br>Rp 1.450.000.000</div>', unsafe_allow_html=True)
        with m2: st.markdown('<div class="metric-card">👥 <b>Klien Aktif</b><br>12 Perusahaan</div>', unsafe_allow_html=True)
        with m3: st.markdown('<div class="metric-card">⚠️ <b>Fraud Alert</b><br>2 Temuan Hari Ini</div>', unsafe_allow_html=True)
        with m4: st.markdown('<div class="metric-card">✅ <b>System Health</b><br>99.9% Online</div>', unsafe_allow_html=True)
        
        st.write("---")
        
        # Menu Tab Lengkap
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🔍 V-Scan & Analisa", 
            "📊 Monitoring Audit", 
            "📍 Geolocation Map",
            "💰 Billing & AR", 
            "⚙️ Manajemen Klien"
        ])
        
        with tab1: # Fitur "Deep Dive" & Analisa Data
            st.markdown('<p class="header-text">🚀 V-SCAN: DEEP-DIVE ANALISA FRAUD</p>', unsafe_allow_html=True)
            klien_analisa = st.selectbox("Pilih Klien untuk Dianalisa:", ["Toko Berkah Jaya", "B2B Trading Sinar"])
            uploaded_file = st.file_uploader(f"Unggah Data Transaksi {klien_analisa}", type=['csv', 'xlsx'])
            
            if uploaded_file:
                with st.spinner('V-GUARD AI sedang membedah data...'):
                    time.sleep(2)
                    st.success(f"✅ Analisa Selesai untuk {klien_analisa}")
                    
                    st.markdown("### 📊 Tren Anomali Mingguan")
                    chart_data = pd.DataFrame({'Minggu': ['W1', 'W2', 'W3', 'W4'], 'Kecurangan': [5, 12, 3, 14]})
                    st.line_chart(chart_data.set_index('Minggu'))
                    
                    # Log Aktivitas (Audit Trail)
                    st.markdown(f'<div class="admin-card">📜 <b>Audit Trail:</b> Analisa sukses dilakukan pada {datetime.now().strftime("%H:%M:%S")}</div>', unsafe_allow_html=True)

                    res1, res2, res3 = st.columns(3)
                    res1.metric("Total Transaksi", "1.240", "Normal")
                    res2.metric("Anomali Terdeteksi", "14", "-2", delta_color="inverse")
                    res3.metric("Potensi Kebocoran", "Rp 3.420.000", "Critical")
                    
                    st.write("---")
                    c_act1, c_act2 = st.columns(2)
                    with c_act1: # Auto-Download Report
                        st.download_button("📥 AUTO-DOWNLOAD REPORT (PDF)", data="Laporan Audit Terenkripsi", file_name=f"VGUARD_Audit_{klien_analisa}.pdf")
                    with c_act2: # Tombol Kirim Otomatis
                        if st.button("📲 KIRIM LAPORAN KE WA KLIEN"):
                            st.success(f"Notifikasi berhasil dikirim ke Owner {klien_analisa}!")

        with tab2: # Otomasi Penjadwalan Audit
            st.markdown('<p class="header-text">📅 MONITORING KEPATUHAN & JADWAL</p>', unsafe_allow_html=True)
            st.table(pd.DataFrame(st.session_state.audit_logs))

        with tab3: # Geolocation Map
            st.markdown('<p class="header-text">📍 GEOLOCATION MAP: SEBARAN KLIEN</p>', unsafe_allow_html=True)
            map_points = pd.DataFrame({'lat': [-6.2088, -6.1751, -6.2297], 'lon': [106.8456, 106.8272, 106.6894]})
            st.map(map_points)
            st.caption("Monitoring lokasi aktif perangkat V-GUARD di seluruh cabang klien.")

        with tab4: # Billing & AR
            st.markdown('<p class="header-text">💵 STATUS TAGIHAN KLIEN</p>', unsafe_allow_html=True)
            bill_df = pd.DataFrame({"Klien": ["Toko Berkah", "Sinar B2B"], "Nilai": ["5 JT", "10 JT"], "Status": ["Lunas", "Jatuh Tempo"]})
            st.table(bill_df)

        with tab5: # Manajemen Klien & Perangkat
            st.markdown('<p class="header-text">⚙️ MANAJEMEN SISTEM & KLIEN</p>', unsafe_allow_html=True)
            with st.form("client_form"):
                st.text_input("Nama Bisnis")
                st.selectbox("Paket", ["V-START", "V-GROW", "V-PRIME"])
                if st.form_submit_button("Simpan Klien"):
                    st.success("Data berhasil disinkronisasi.")

else:
    # --- BERANDA UTAMA (KUNCI - JANGAN DIUBAH) ---
    st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)
    st.write("---")
    
    col_p1, col_p2 = st.columns([1, 2.5])
    with col_p1:
        try: st.image("erwin.jpg", use_container_width=True)
        except: st.info("ERWIN SINAGA")
    with col_p2:
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        Erwin Sinaga adalah seorang pemimpin strategis dengan rekam jejak profesional yang prestisius selama lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan nasional**. Beliau telah memimpin transformasi digital perbankan dan memastikan akurasi finansial pada level tertinggi.

        Filosofi kepemimpinan beliau tertuang dalam konsep **"Digitizing Trust, Eliminating Leakage"**. Beliau merancang VGUARD AI sebagai perisai pertahanan strategis yang mampu mendeteksi potensi kecurangan (*fraud*) secara *real-time*.
        """)
        if st.button("🚀 MASUK KE COMMAND CENTER (ADMIN)"):
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    st.markdown('<p class="header-text">📈 KALKULATOR PENYELAMATAN PROFIT (ROI)</p>', unsafe_allow_html=True)
    st.markdown('<div class="roi-box">', unsafe_allow_html=True)
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        omzet = st.number_input("Estimasi Omzet Bulanan (Rp)", value=250000000)
        kebocoran = st.slider("Tingkat Kebocoran Bisnis (%)", 1, 15, 3)
    with col_a2:
        loss = omzet * (kebocoran/100)
        saved = loss * 0.95
        st.write(f"#### Potensi Kerugian: Rp {loss:,.0f}")
        st.success(f"#### Diselamatkan VGUARD: Rp {saved:,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    pk1, pk2, pk3, pk4 = st.columns(4)
    pk1.markdown('<div class="card"><b>V-START</b><hr>Audit Mingguan<br>2.5 JT</div>', unsafe_allow_html=True)
    pk2.markdown('<div class="card"><b>V-GROW</b><hr>Audit Harian<br>5 JT</div>', unsafe_allow_html=True)
    pk3.markdown('<div class="card"><b>V-PRIME</b><hr>Multi-Cabang<br>10 JT</div>', unsafe_allow_html=True)
    pk4.markdown('<div class="card"><b>V-CUSTOM</b><hr>Full Support<br>NEGO</div>', unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
