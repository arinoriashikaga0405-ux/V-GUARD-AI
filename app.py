import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False
if 'audit_logs' not in st.session_state:
    # Simulasi Data Awal untuk Demo Investor
    st.session_state.audit_logs = [
        {"Klien": "Toko Berkah Jaya", "Jadwal": "21:00", "Status": "✅ Terpindai", "Waktu": "2026-03-30 21:05", "Hasil": "Aman"},
        {"Klien": "B2B Trading Sinar", "Jadwal": "22:00", "Status": "❌ Belum Upload", "Waktu": "-", "Hasil": "Pending"}
    ]

# --- 2. CSS PREMIUM & DASHBOARD ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; height: 45px; }
    .card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #e2e8f0; text-align: center; height: 100%; transition: 0.3s; }
    .roi-box { background: #eff6ff; padding: 25px; border-radius: 15px; border: 2px dashed #1e3a8a; }
    .status-box { padding: 10px; border-radius: 10px; font-weight: bold; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR (CEO ERWIN SINAGA) ---
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

# --- 4. LOGIKA HALAMAN ---
if st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.header("🔐 Executive Access")
        pwd = st.text_input("Masukkan Password Admin:", type="password")
        if st.button("Masuk ke Command Center"):
            if pwd == "VGUARD2026":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        # --- COMMAND CENTER ERWIN SINAGA ---
        st.header("💻 Command Center - Erwin Sinaga")
        st.subheader("📊 Monitoring Kepatuhan & Penjadwalan Audit")
        
        # TABEL MONITORING (FITUR BARU)
        df_logs = pd.DataFrame(st.session_state.audit_logs)
        st.table(df_logs)
        
        c_adm1, c_adm2 = st.columns(2)
        with c_adm1:
            st.info("💡 Tip CEO: Kirim reminder ke klien yang berstatus 'Belum Upload' untuk menjaga retensi.")
            if st.button("🚨 KIRIM REMINDER WA OTOMATIS"):
                st.success("Notifikasi pengingat jadwal audit telah dikirim ke 1 mitra.")
        
        with c_adm2:
            st.warning("⚠️ Fraud Alert: Terdeteksi selisih stok di Mitra 'Toko Berkah'.")
            if st.button("🔔 KIRIM NOTIFIKASI FRAUD"):
                st.error("Fire Alarm dikirim ke Owner Mitra!")

        st.write("---")
        st.subheader("📑 Kelola Invoice & AR")
        if st.button("🔔 BLAST NOTIFIKASI JATUH TEMPO"):
            st.success("Invoice Reminder dikirim ke semua debitur klien.")

else:
    # --- HALAMAN BERANDA ---
    st.title("🛡️ VGUARD AI SYSTEMS")
    
    # SEKSI PROFIL (WAJIB MINIMAL 100 KATA)
    st.write("---")
    col_p1, col_p2 = st.columns([1, 2.5])
    with col_p1:
        try: st.image("erwin.jpg", use_container_width=True)
        except: st.info("ERWIN SINAGA\n\nFounder VGUARD AI")
    with col_p2:
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        Erwin Sinaga adalah seorang pemimpin strategis dengan rekam jejak profesional selama lebih dari sepuluh tahun sebagai eksekutif senior di industri perbankan nasional. Berbekal pengalaman mendalam dalam manajemen risiko, optimasi pendapatan, dan kepemimpinan tim berskala besar, beliau mendirikan VGUARD AI Systems sebagai solusi mutakhir bagi tantangan integritas bisnis di era digital.
        
        Visi utama beliau adalah membantu para pemilik usaha kecil, menengah (UMKM), hingga perusahaan korporasi dalam mengatasi kebocoran profit yang sering kali tidak terdeteksi oleh sistem konvensional. Melalui filosofi 'Digitizing Trust, Eliminating Leakage', Bapak Erwin memastikan bahwa setiap transaksi di dalam bisnis klien memiliki tingkat keamanan dan transparansi yang setara dengan standar perbankan. VGUARD AI bukan sekadar alat audit, melainkan perisai pertahanan strategis (V-Guard Fire Alarm) yang dirancang untuk melindungi setiap rupiah aset berharga Anda dari tindakan fraud dan inefisiensi operasional.
        """)
        if st.button("🚀 BUKA COMMAND CENTER (ADMIN)"):
            st.session_state.page = "Admin"
            st.rerun()

    # SEKSI ROI (WAJIB ADA)
    st.write("---")
    st.subheader("📈 Kalkulator ROI Penyelamatan Profit")
    st.markdown('<div class="roi-box">', unsafe_allow_html=True)
    c_r1, c_r2 = st.columns(2)
    with c_r1:
        omzet = st.number_input("Total Omzet Bulanan Klien (Rp)", value=100000000, step=10000000)
        bocor = st.slider("Estimasi Kebocoran Tradisional (%)", 1, 10, 3)
    with c_r2:
        loss = omzet * (bocor/100)
        st.write(f"### Potensi Kerugian: Rp {loss:,.0f}")
        st.success(f"### Diselamatkan V-Guard AI: Rp {loss*0.95:,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

    # SEKSI PAKET (WAJIB ADA)
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    pk1, pk2, pk3, pk4 = st.columns(4)
    with pk1: st.markdown('<div class="card"><b>V-START</b><br>2.5 JT<hr>Audit Mingguan<br>WA Alert Dasar</div>', unsafe_allow_html=True)
    with pk2: st.markdown('<div class="card"><b>V-GROW</b><br>5 JT<hr>Audit Harian<br>AI Fraud Detection</div>', unsafe_allow_html=True)
    with pk3: st.markdown('<div class="card"><b>V-PRIME</b><br>10 JT<hr>Multi-Cabang<br>AR Auto-Reminder</div>', unsafe_allow_html=True)
    with pk4: st.markdown('<div class="card"><b>V-CUSTOM</b><br>NEGO<hr>Integrasi ERP<br>Support 24/7</div>', unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
