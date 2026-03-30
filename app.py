import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. INITIALIZE SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems - CEO Erwin Sinaga", page_icon="🛡️", layout="wide")

# --- 3. PREMIUM CSS (RINGKAS & EKSEKUTIF) ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; height: 45px; }
    .roi-section { background: #ffffff; padding: 20px; border-radius: 12px; border: 2px dashed #1e3a8a; margin: 10px 0; }
    
    /* CSS UNTUK 4 KOTAK PAKET - TINGGI 200PX */
    .package-card { 
        background: white; 
        padding: 12px; 
        border-radius: 10px; 
        border: 1px solid #e2e8f0; 
        text-align: center; 
        height: 200px; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        font-size: 0.85em;
    }
    .package-card h3 { color: #1e3a8a; margin-bottom: 5px; font-size: 1em; }
    .package-card h2 { color: #1e3a8a; margin: 5px 0; font-size: 1.2em; }
    
    .profile-box { background: #f1f5f9; padding: 20px; border-radius: 12px; border-left: 6px solid #1e3a8a; }
    .header-text { color: #1e3a8a; font-weight: bold; border-left: 5px solid #1e3a8a; padding-left: 10px; margin: 12px 0; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("### 👤 CEO: ERWIN SINAGA")
    if st.button("🏠 Beranda Utama"): 
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.auth:
        if st.button("🔓 Logout Admin"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()

# --- 5. LOGIKA HALAMAN ---
if st.session_state.page == "Home":
    st.markdown('<h1 style="text-align:center; color:#1e3a8a; margin-bottom:0;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2.2])
    with col1:
        # FOTO DIPULIHKAN (UKURAN KECIL PROPORSIAL)
        st.markdown('<div style="background:#e2e8f0; height:280px; display:flex; align-items:center; justify-content:center; border-radius:12px; border:2px solid #1e3a8a; color:#1e3a8a; font-weight:bold; text-align:center; font-size:0.9em; padding:10px;">FOTO EKSEKUTIF<br>ERWIN SINAGA</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="profile-box">', unsafe_allow_html=True)
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        **Erwin Sinaga** adalah pemimpin strategis dengan rekam jejak prestisius selama lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan nasional**. Beliau mengintegrasikan disiplin manajemen risiko perbankan ke dalam **VGUARD AI Systems** untuk melindungi aset bisnis dari kebocoran transaksi yang merugikan.

        Filosofi beliau adalah **"Presisi Tanpa Kompromi"**. Bapak Erwin meyakini bahwa setiap rupiah dalam omzet klien adalah amanah yang harus dijaga dengan teknologi AI mutakhir. VGUARD AI dirancang sebagai perisai pertahanan strategis yang memberikan ketenangan bagi pemilik bisnis agar tetap fokus pada ekspansi tanpa takut akan kecurangan atau *fraud*.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.write("")
        if st.button("🚀 AKSES COMMAND CENTER"): 
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    
    # --- CALCULATOR ROI ---
    st.markdown('<div class="roi-section">', unsafe_allow_html=True)
    st.markdown('<p style="color:#1e3a8a; font-weight:bold; margin-bottom:5px;">ANALISIS POTENSI KERUGIAN & PROTEKSI PROFIT</p>', unsafe_allow_html=True)
    c_roi1, c_roi2 = st.columns(2)
    with c_roi1:
        oz = st.number_input("Omzet Bulanan (Rp)", value=250000000)
    with c_roi2:
        kb = st.slider("Kebocoran/Fraud (%)", 1, 15, 3)
    
    loss = oz * (kb/100)
    st.error(f"Potensi Rugi: Rp {loss:,.0f} | Profit Diselamatkan AI: Rp {(loss * 0.95):,.0f}")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 4 PAKET LAYANAN STRATEGIS (UKURAN KECIL) ---
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.markdown('<div class="package-card"><h3>🔹 V-START</h3><p>Ritel & UMKM</p><h2>Rp 5 JT</h2><hr><p>Scan Harian<br>Report Mingguan</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="package-card" style="border: 2px solid #1e3a8a;"><h3>🔶 V-GROW</h3><p>3 Cabang</p><h2>Rp 15 JT</h2><hr><p>Real-time Scan<br>Notifikasi WA</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="package-card"><h3>💎 V-PRIME</h3><p>Korporasi</p><h2>Custom</h2><hr><p>Value Based<br>Full AI Support</p></div>', unsafe_allow_html=True)
    with p4:
        st.markdown('<div class="package-card"><h3>🚀 V-ENTERPRISE</h3><p>Global / Holding</p><h2>Contact</h2><hr><p>Private Server<br>Custom AI Model</p></div>', unsafe_allow_html=True)

elif st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.markdown('<h1 style="text-align:center;">🔐 Admin Authorization</h1>', unsafe_allow_html=True)
        col_l1, col_l2, col_l3 = st.columns([1,1.5,1])
        with col_l2:
            pwd = st.text_input("Enter Password:", type="password")
            if st.button("Login"):
                if pwd == "VGUARD2026":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Akses Ditolak!")
    else:
        # --- COMMAND CENTER LENGKAP ---
        st.header("💻 Command Center - Erwin Sinaga")
        t1, t2, t3, t4, t5 = st.tabs(["🔍 V-Scan", "📊 Monitoring", "📍 Map", "💰 Billing", "⚙️ Klien"])
        with t1:
            st.markdown('<p class="header-text">🚀 ANALISA FRAUD REAL-TIME</p>', unsafe_allow_html=True)
            st.file_uploader("Unggah Laporan")
            if st.button("📲 Kirim WA"): st.success("Pesan Terkirim!")
        with t2:
            st.markdown('<p class="header-text">📅 JADWAL AUDIT</p>', unsafe_allow_html=True)
            st.table(pd.DataFrame({"Klien": ["Maju Jaya"], "Status": ["Aktif"]}))
        with t3: st.map()
        with t4: st.metric("Piutang Berjalan", "Rp 145.000.000")
        with t5:
            st.text_input("Nama Perusahaan Baru")
            if st.button("Simpan"): st.success("Klien Terdaftar")

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
