import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. INITIALIZE SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems - CEO Erwin Sinaga", page_icon="🛡️", layout="wide")

# --- 3. PREMIUM CSS (ESTETIKA EKSEKUTIF) ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; height: 48px; }
    .roi-section { background: #ffffff; padding: 30px; border-radius: 15px; border: 2px dashed #1e3a8a; margin: 20px 0; }
    .package-card { background: white; padding: 25px; border-radius: 15px; border: 1px solid #e2e8f0; text-align: center; height: 100%; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .header-text { color: #1e3a8a; font-weight: bold; border-left: 5px solid #1e3a8a; padding-left: 12px; margin: 15px 0; }
    .profile-box { background: #f1f5f9; padding: 25px; border-radius: 15px; border-left: 8px solid #1e3a8a; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("### 👤 CEO: ERWIN SINAGA")
    st.write("---")
    if st.button("🏠 Kembali ke Beranda"): 
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.auth:
        if st.button("🔓 Keluar Sistem"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()

# --- 5. LOGIKA HALAMAN ---
if st.session_state.page == "Home":
    st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2.2])
    with col1:
        # Menampilkan placeholder foto yang lebih baik
        st.markdown('<div style="background:#e2e8f0; height:350px; display:flex; align-items:center; justify-content:center; border-radius:15px; border:2px solid #1e3a8a; color:#1e3a8a; font-weight:bold;">PAS FOTO ERWIN SINAGA</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="profile-box">', unsafe_allow_html=True)
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        **Erwin Sinaga** adalah seorang pemimpin strategis dengan rekam jejak prestisius selama lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan nasional**. Beliau membawa disiplin ketat perbankan dan manajemen risiko ke dalam dunia teknologi melalui **VGUARD AI Systems**. Sebagai Founder, beliau memahami bahwa kebocoran kecil dalam transaksi bisnis dapat menjadi ancaman fatal bagi pertumbuhan perusahaan jangka panjang.

        Filosofi kepemimpinan beliau adalah **"Presisi Tanpa Kompromi"**. Bapak Erwin meyakini bahwa setiap rupiah dalam omzet klien adalah amanah yang harus dijaga dengan teknologi kecerdasan buatan paling mutakhir. VGUARD AI bukan sekadar alat audit, melainkan perisai pertahanan strategis yang dirancang untuk memberikan ketenangan pikiran bagi para pemilik bisnis modern agar mereka dapat fokus sepenuhnya pada ekspansi tanpa rasa takut akan kecurangan atau *fraud*.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.write("")
        if st.button("🚀 BUKA COMMAND CENTER (ADMIN)"): 
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    
    # --- CALCULATOR ROI ---
    st.markdown('<h3 style="color:#1e3a8a;">ANALISIS POTENSI KERUGIAN & PROTEKSI PROFIT</h3>', unsafe_allow_html=True)
    st.markdown('<div class="roi-section">', unsafe_allow_html=True)
    oz = st.number_input("Omzet Bulanan Bisnis (Rp)", value=250000000)
    kb = st.slider("Estimasi Kebocoran/Fraud (%)", 1, 15, 3)
    
    loss = oz * (kb/100)
    saved = loss * 0.95
    
    st.error(f"Potensi Kerugian Akibat Fraud: Rp {loss:,.0f} / bln")
    st.success(f"Profit Diselamatkan V-GUARD (Efisiensi 95%): Rp {saved:,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- PAKET LAYANAN STRATEGIS (3 PAKET UTAMA) ---
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="package-card"><h3>🔹 V-START</h3><p>Ritel & UMKM</p><h1>Rp 5 JT</h1><p>/ bulan</p><hr><p>Scan Harian<br>Report Mingguan</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="package-card" style="border: 2px solid #1e3a8a;"><h3>🔶 V-GROW</h3><p>Bisnis Multi-Cabang</p><h1>Rp 15 JT</h1><p>/ bulan</p><hr><p>Real-time Scan<br>Notifikasi WA Otomatis</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="package-card"><h3>💎 V-PRIME</h3><p>Korporasi / Nasional</p><h1>Custom</h1><p>Value Based</p><hr><p>Full AI Customization<br>Dedicated Analyst</p></div>', unsafe_allow_html=True)

elif st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.markdown('<h1 style="text-align:center;">🔐 Executive Access</h1>', unsafe_allow_html=True)
        col_l1, col_l2, col_l3 = st.columns([1,2,1])
        with col_l2:
            pwd = st.text_input("Password Admin:", type="password")
            if st.button("Masuk"):
                if pwd == "VGUARD2026":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Akses Ditolak!")
    else:
        # --- COMMAND CENTER LENGKAP ---
        st.header("💻 Command Center - Erwin Sinaga")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔍 V-Scan", "📊 Monitoring", "📍 Map", "💰 Billing", "⚙️ Klien"])
        
        with tab1:
            st.markdown('<p class="header-text">🚀 V-SCAN: DEEP-DIVE ANALISA FRAUD</p>', unsafe_allow_html=True)
            up = st.file_uploader("Unggah Laporan Penjualan (CSV/Excel)", type=['csv', 'xlsx'])
            if up:
                st.success("✅ File Dianalisa Sempurna")
                if st.button("📲 Kirim WhatsApp Ke Klien"): st.success("Terkirim!")

        with tab2:
            st.markdown('<p class="header-text">📅 KEPATUHAN & PENJADWALAN</p>', unsafe_allow_html=True)
            st.table(pd.DataFrame({"Klien": ["Toko Maju"], "Status": ["Aktif"], "Last Audit": ["H-1"]}))
            if st.button("🔔 Kirim Reminder WA Otomatis"): st.success("Reminder Terkirim!")

        with tab3:
            st.markdown('<p class="header-text">📍 SEBARAN GEOLOKASI KLIEN</p>', unsafe_allow_html=True)
            st.map()

        with tab4:
            st.markdown('<p class="header-text">💵 BILLING & AR CONTROL</p>', unsafe_allow_html=True)
            st.info("Total Piutang Berjalan: Rp 45.000.000")

        with tab5:
            st.markdown('<p class="header-text">⚙️ MANAJEMEN KLIEN BARU</p>', unsafe_allow_html=True
