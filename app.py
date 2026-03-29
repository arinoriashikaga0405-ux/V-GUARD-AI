import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. CSS ANTI-ERROR (PREMIUM VISUAL) ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; height: 45px; }
    .card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #e2e8f0; text-align: center; height: 100%; transition: 0.3s; }
    .card:hover { border-color: #1e3a8a; transform: translateY(-5px); }
    .roi-box { background: #eff6ff; padding: 25px; border-radius: 15px; border: 2px dashed #1e3a8a; }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR (DENGAN FOTO ANDA) ---
with st.sidebar:
    # MENAMPILKAN FOTO ERWIN SINAGA
    try:
        st.image("erwin.jpg", width=120)
    except:
        st.info("👤 CEO: ERWIN SINAGA")
        
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

# --- 4. LOGIKA NAVIGASI ---
if st.session_state.page == "Admin":
    if not st.session_state.auth:
        # AKSES TERBATAS
        st.header("🔐 Executive Access")
        st.markdown('<div class="alarm-banner">🚨 SISTEM MONITORING FRAUD & PIUTANG 🚨</div>', unsafe_allow_html=True)
        pwd = st.text_input("Masukkan Password Admin:", type="password")
        if st.button("Masuk ke Command Center"):
            if pwd == "VGUARD2026":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        # COMMAND CENTER ERWIN
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
        st.file_uploader("Unggah Data Transaksi Klien untuk Audit AI V-Guard", type=['csv', 'xlsx'])

else:
    # --- HALAMAN BERANDA ---
    st.title("🛡️ VGUARD AI SYSTEMS")
    
    # SEKSI PROFIL (DENGAN FOTO ANDA & WAJIB MINIMAL 100 KATA)
    st.write("---")
    col_p1, col_p2 = st.columns([1, 2.5])
    with col_p1:
        # MENAMPILKAN FOTO ERWIN SINAGA DI PROFIL
        try:
            st.image("erwin.jpg", use_container_width=True)
        except:
            st.info("ERWIN SINAGA\n\nFounder VGUARD AI")
    with col_p2:
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        Erwin Sinaga adalah seorang pemimpin strategis dengan rekam jejak profesional selama lebih dari sepuluh tahun sebagai eksekutif senior di industri perbankan nasional. Berbekal pengalaman mendalam dalam manajemen risiko, optimasi pendapatan, dan kepemimpinan tim berskala besar, beliau mendirikan VGUARD AI Systems sebagai solusi mutakhir bagi tantangan integritas bisnis di era digital.
        
        Visi utama beliau adalah membantu para pemilik usaha kecil, menengah (UMKM), hingga perusahaan korporasi dalam mengatasi kebocoran profit yang sering kali tidak terdeteksi oleh sistem konvensional. Melalui filosofi 'Digitizing Trust, Eliminating Leakage', Bapak Erwin memastikan bahwa setiap transaksi di dalam bisnis klien memiliki tingkat keamanan dan transparansi yang setara dengan standar perbankan. VGUARD AI bukan sekadar alat audit, melainkan perisai pertahanan strategis (V-Guard Fire Alarm) yang dirancang untuk melindungi setiap rupiah aset berharga Anda dari tindakan fraud dan inefisiensi operasional.
        """)
        if st.button("🚀 BUKA COMMAND CENTER (ADMIN)"):
            st.session_state.page = "Admin"
            st.rerun()

    # SEKSI ROI (PENGHITUNG KERUGIAN)
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

    # SEKSI PAKET LAYANAN (WAJIB ADA)
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    pk1, pk2, pk3, pk4 = st.columns(4)
    with pk1: st.markdown('<div class="card"><b>V-START</b><br>2.5 JT<hr>Audit Harian Retail<br>Notifikasi WA Aktif<br>Monitor Piutang Dasar</div>', unsafe_allow_html=True)
    with pk2: st.markdown('<div class="card"><b>V-GROW</b><br>5 JT<hr>AI Fraud Detection<br>Sinkron Stok Otomatis<br>AR Auto-Reminder</div>', unsafe_allow_html=True)
    with pk3: st.markdown('<div class="card"><b>V-PRIME</b><br>10 JT<hr>Multi-Cabang Control<br>Predictive Analytics<br>Full AR Control</div>', unsafe_allow_html=True)
    with pk4: st.markdown('<div class="card"><b>V-CUSTOM</b><br>NEGO<hr>Solusi Enterprise<br>Integrasi ERP/SAP<br>Support Strategis 24/7</div>', unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
