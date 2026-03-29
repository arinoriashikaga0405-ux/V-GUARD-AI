import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. CSS ANTI-ERROR ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; }
    .card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #e2e8f0; text-align: center; height: 100%; }
    .roi-box { background: #eff6ff; padding: 25px; border-radius: 15px; border: 2px dashed #1e3a8a; }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ VGUARD AI")
    st.write("**CEO: ERWIN SINAGA**")
    if st.button("🏠 Beranda Utama"): 
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.auth:
        if st.button("🔓 Log Out"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()
    st.error("🚨 FIRE ALARM: ACTIVE")

# --- 4. LOGIKA HALAMAN ---
if st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.header("🔐 Executive Access")
        pwd = st.text_input("Password Admin:", type="password")
        if st.button("Buka Command Center"):
            if pwd == "VGUARD2026":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        st.header("💻 Command Center - Erwin Sinaga")
        st.info("Status: Monitoring Fraud & Invoice Terintegrasi")
        
        col_adm1, col_adm2 = st.columns(2)
        with col_adm1:
            st.subheader("🛡️ Fraud Detection")
            if st.button("🚨 AKTIFKAN FIRE ALARM"):
                st.error("ALARM AKTIF! Notifikasi kebocoran dikirim ke Owner.")
        
        with col_adm2:
            st.subheader("📑 Invoice & AR")
            if st.button("🔔 KIRIM NOTIFIKASI INVOICE"):
                st.success("Notifikasi WhatsApp Piutang Berhasil Dikirim!")
        
        st.write("---")
        st.file_uploader("Unggah Data Transaksi Klien untuk Audit AI", type=['csv', 'xlsx'])

else:
    # --- HALAMAN BERANDA ---
    st.title("🛡️ VGUARD AI SYSTEMS")
    
    # SEKSI PROFIL (WAJIB MINIMAL 100 KATA)
    st.write("---")
    col_p1, col_p2 = st.columns([1, 3])
    with col_p1:
        st.info("👤 **CEO PROFILE**\n\nErwin Sinaga\n\nFounder VGUARD AI")
    with col_p2:
        st.subheader("Filosofi: Digitizing Trust, Eliminating Leakage")
        st.write("""
        Erwin Sinaga adalah seorang pemimpin strategis dengan rekam jejak profesional selama lebih dari sepuluh tahun sebagai eksekutif senior di industri perbankan nasional. Berbekal pengalaman mendalam dalam manajemen risiko, optimasi pendapatan, dan kepemimpinan tim berskala besar, beliau mendirikan VGUARD AI Systems sebagai solusi mutakhir bagi tantangan integritas bisnis di era digital. 
        
        Visi utama beliau adalah membantu para pemilik usaha kecil, menengah (UMKM), hingga perusahaan korporasi dalam mengatasi kebocoran profit yang sering kali tidak terdeteksi oleh sistem konvensional. Melalui filosofi 'Digitizing Trust, Eliminating Leakage', Bapak Erwin memastikan bahwa setiap transaksi di dalam bisnis klien memiliki tingkat keamanan dan transparansi yang setara dengan standar perbankan. VGUARD AI bukan sekadar alat audit, melainkan perisai pertahanan strategis (V-Guard Fire Alarm) yang dirancang untuk melindungi setiap rupiah aset berharga Anda dari tindakan fraud dan inefisiensi operasional.
        """)
        if st.button("🚀 MASUK KE ADMIN COMMAND CENTER"):
            st.session_state.page = "Admin"
            st.rerun()

    # SEKSI ROI (PENGHITUNG KERUGIAN)
    st.write("---")
    st.subheader("📈 Kalkulator ROI (Penghitung Potensi Kerugian)")
    with st.container():
        st.markdown('<div class="roi-box">', unsafe_allow_html=True)
        c_r1, c_r2 = st.columns(2)
        with c_r1:
            omzet = st.number_input("Total Omzet Bulanan Klien (Rp)", value=100000000, step=10000000)
            bocor = st.slider("Estimasi Kebocoran / Fraud (%)", 1, 10, 3)
        with c_r2:
            loss = omzet * (bocor/100)
            st.metric("Potensi Kerugian Klien", f"Rp {loss:,.0f}")
            st.success(f"Dapat Diselamatkan V-Guard: Rp {loss*0.95:,.0f}")
        st.markdown('</div>', unsafe_allow_html=True)

    # SEKSI PAKET (WAJIB ADA)
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    pk1, pk2, pk3, pk4 = st.columns(4)
    with pk1: st.markdown('<div class="card"><b>V-START</b><br>2.5 JT<hr>Audit Harian & WA Alert Dasar</div>', unsafe_allow_html=True)
    with pk2: st.markdown('<div class="card"><b>V-GROW</b><br>5 JT<hr>AI Fraud & Sinkron Stok Otomatis</div>', unsafe_allow_html=True)
    with pk3: st.markdown('<div class="card"><b>V-PRIME</b><br>10 JT<hr>Multi-Cabang & Predictive Analytics</div>', unsafe_allow_html=True)
    with pk4: st.markdown('<div class="card"><b>V-CUSTOM</b><br>NEGO<hr>Integrasi ERP & Support Strategis 24/7</div>', unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
