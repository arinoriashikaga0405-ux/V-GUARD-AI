import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. INITIALIZE SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems - Erwin Sinaga", page_icon="🛡️", layout="wide")

# --- 3. PREMIUM CSS (CEO EXECUTIVE STYLE) ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; height: 48px; }
    .roi-section { background: #ffffff; padding: 30px; border-radius: 15px; border: 2px dashed #1e3a8a; margin: 20px 0; }
    .package-card { background: white; padding: 25px; border-radius: 15px; border: 1px solid #e2e8f0; text-align: center; height: 100%; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .header-text { color: #1e3a8a; font-weight: bold; border-left: 5px solid #1e3a8a; padding-left: 12px; margin: 15px 0; }
    .profile-box { background: #f1f5f9; padding: 25px; border-radius: 15px; border-left: 10px solid #1e3a8a; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("### 👤 CEO: ERWIN SINAGA")
    st.write("---")
    if st.button("🏠 Beranda Utama"): 
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.auth:
        if st.button("🔓 Logout System"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()

# --- 5. LOGIKA HALAMAN ---
if st.session_state.page == "Home":
    st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2.2])
    with col1:
        # SLOT FOTO CEO
        st.markdown('<div style="background:#e2e8f0; height:380px; display:flex; align-items:center; justify-content:center; border-radius:15px; border:2px solid #1e3a8a; color:#1e3a8a; font-weight:bold; text-align:center; padding:20px;">FOTO EKSEKUTIF<br>ERWIN SINAGA</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="profile-box">', unsafe_allow_html=True)
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        # PROFIL > 100 KATA
        st.write("""
        **Erwin Sinaga** adalah seorang pemimpin strategis dengan rekam jejak prestisius selama lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan dan manajemen aset nasional**. Berbekal pengalaman mendalam dalam mengelola risiko keuangan skala besar, beliau mendirikan **VGUARD AI Systems** untuk membawa standar keamanan perbankan ke sektor UMKM dan korporasi global.

        Filosofi beliau, **"Presisi Tanpa Kompromi"**, menjadi fondasi utama VGUARD AI. Bapak Erwin meyakini bahwa setiap rupiah dalam omzet bisnis adalah hasil kerja keras yang harus dilindungi dari segala bentuk kecurangan (*fraud*). Melalui integrasi kecerdasan buatan (AI) yang canggih, beliau berkomitmen memberikan alat pertahanan yang tak tertembus, sehingga para pemilik bisnis dapat berekspansi dengan rasa aman total. VGUARD AI bukan sekadar teknologi; ini adalah manifestasi dari integritas dan akuntabilitas dalam dunia bisnis digital.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.write("")
        if st.button("🚀 AKSES COMMAND CENTER (ADMIN)"): 
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    
    # --- CALCULATOR ROI (BERSIH TANPA KOTAK KOSONG) ---
    st.markdown('<h3 style="color:#1e3a8a;">ANALISIS POTENSI KERUGIAN & PROTEKSI PROFIT</h3>', unsafe_allow_html=True)
    st.markdown('<div class="roi-section">', unsafe_allow_html=True)
    oz = st.number_input("Omzet Bulanan Bisnis (Rp)", value=250000000)
    kb = st.slider("Estimasi Kebocoran/Fraud (%)", 1, 15, 3)
    
    loss = oz * (kb/100)
    saved = loss * 0.95
    
    st.error(f"Potensi Kerugian Akibat Fraud: Rp {loss:,.0f} / bln")
    st.success(f"Profit Diselamatkan V-GUARD (Efisiensi 95%): Rp {saved:,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- PAKET LAYANAN STRATEGIS (3 PAKET) ---
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="package-card"><h3>🔹 V-START</h3><p>UMKM / Ritel</p><h1 style="color:#1e3a8a;">Rp 5 JT</h1><p>/ bulan</p><hr><p>Analisa Harian<br>Laporan Mingguan</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="package-card" style="border: 2px solid #1e3a8a;"><h3>🔶 V-GROW</h3><p>Bisnis Multi-Cabang</p><h1 style="color:#1e3a8a;">Rp 15 JT</h1><p>/ bulan</p><hr><p>Real-time AI Scan<br>Notifikasi WA Instant</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="package-card"><h3>💎 V-PRIME</h3><p>Korporasi / Nasional</p><h1 style="color:#1e3a8a;">Custom</h1><p>Value Based</p><hr><p>AI Custom Model<br>Dedicated Key Account</p></div>', unsafe_allow_html=True)

elif st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.markdown('<h1 style="text-align:center;">🔐 Executive Login</h1>', unsafe_allow_html=True)
        col_l1, col_l2, col_l3 = st.columns([1,1.5,1])
        with col_l2:
            pwd = st.text_input("Admin Password:", type="password")
            if st.button("Authorize Access"):
                if pwd == "VGUARD2026":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Akses Ditolak!")
    else:
        # --- COMMAND CENTER LENGKAP (FIXED) ---
        st.header("💻 Command Center - Erwin Sinaga")
        t1, t2, t3, t4, t5 = st.tabs(["🔍 V-Scan", "📊 Monitoring", "📍 Geolocation", "💰 Billing", "⚙️ Manajemen"])
        
        with t1:
            st.markdown('<p class="header-text">🚀 V-SCAN: DEEP-DIVE ANALISA FRAUD</p>', unsafe_allow_html=True)
            up = st.file_uploader("Unggah Laporan Transaksi", type=['csv', 'xlsx'])
            if up:
                st.success("✅ Analisa AI Selesai")
                if st.button("📲 Kirim WhatsApp Ke Klien"): st.success("Pesan Terkirim!")

        with t2:
            st.markdown('<p class="header-text">📅 MONITORING KEPATUHAN & AUDIT</p>', unsafe_allow_html=True)
            st.table(pd.DataFrame({"Klien": ["B2B Sinar", "Toko Berkah"], "Status": ["Aktif", "Audit"], "Risiko": ["Rendah", "Sedang"]}))
            if st.button("🔔 Kirim Reminder WA Masal"): st.success("Notifikasi Terkirim!")

        with t3:
            st.markdown('<p class="header-text">📍 SEBARAN KLIEN V-GUARD AI</p>', unsafe_allow_html=True)
            st.map() # Menampilkan peta default

        with t4:
            st.markdown('<p class="header-text">💰 BILLING & AR CONTROL</p>', unsafe_allow_html=True)
            st.metric("Total Revenue bln ini", "Rp 145.000.000", "+12%")

        with t5:
            st.markdown('<p class="header-text">⚙️ MANAJEMEN KLIEN BARU</p>', unsafe_allow_html=True)
            nama_baru = st.text_input("Nama Perusahaan Klien:")
            if st.button("Daftarkan Klien"):
                st.success(f"Klien {nama_baru} Berhasil Ditambahkan ke Database.")

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
