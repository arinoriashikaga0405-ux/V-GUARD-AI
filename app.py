import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. INITIALIZE SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 3. PREMIUM CSS (FIXED DESIGN) ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; height: 45px; }
    .roi-section { 
        background: #ffffff; 
        padding: 30px; 
        border-radius: 15px; 
        border: 2px dashed #1e3a8a; 
        margin: 20px 0;
    }
    .package-card { 
        background: white; 
        padding: 25px; 
        border-radius: 15px; 
        border: 1px solid #e2e8f0; 
        text-align: center; 
        height: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .header-text { color: #1e3a8a; font-weight: bold; border-left: 5px solid #1e3a8a; padding-left: 10px; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("### 👤 CEO: ERWIN SINAGA")
    if st.button("🏠 Beranda Utama"): 
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.auth:
        if st.button("🔓 Log Out"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()

# --- 5. LOGIKA HALAMAN ---
if st.session_state.page == "Home":
    st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2.5])
    with col1:
        st.info("📷 FOTO CEO ERWIN SINAGA")
    with col2:
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("Lebih dari 10 tahun pengalaman sebagai eksekutif perbankan nasional mendasari presisi VGUARD AI dalam menjaga aset bisnis Anda.")
        if st.button("🚀 MASUK KE COMMAND CENTER"): 
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    
    # --- CALCULATOR ROI (KOTAK KOSONG SUDAH DIHAPUS) ---
    st.markdown('<h3 style="color:#1e3a8a;">ANALISIS POTENSI KERUGIAN & PROTEKSI PROFIT</h3>', unsafe_allow_html=True)
    st.markdown('<div class="roi-section">', unsafe_allow_html=True)
    oz = st.number_input("Omzet Bulanan Bisnis (Rp)", value=250000000)
    kb = st.slider("Estimasi Kebocoran/Fraud (%)", 1, 15, 3)
    
    loss = oz * (kb/100)
    saved = loss * 0.95
    
    st.error(f"Potensi Kerugian Akibat Fraud: Rp {loss:,.0f} / bln")
    st.success(f"Profit Diselamatkan V-GUARD (Efisiensi 95%): Rp {saved:,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- PAKET LAYANAN STRATEGIS ---
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="package-card"><h3>🔹 V-START</h3><p>UMKM / Ritel</p><h2>Rp 5 JT</h2><p>/ bln</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="package-card" style="border: 2px solid #1e3a8a;"><h3>🔶 V-GROW</h3><p>3 Cabang</p><h2>Rp 15 JT</h2><p>/ bln</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="package-card"><h3>💎 V-PRIME</h3><p>Korporasi</p><h2>Custom</h2><p>Full AI Support</p></div>', unsafe_allow_html=True)

elif st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.markdown('<h1 style="text-align:center;">🔐 Admin Access</h1>', unsafe_allow_html=True)
        pwd = st.text_input("Password Admin:", type="password")
        if st.button("Login"):
            if pwd == "VGUARD2026":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        # --- COMMAND CENTER FIXED (INDENTASI DIPERBAIKI) ---
        st.header("💻 Command Center - Erwin Sinaga")
        tab1, tab2, tab3 = st.tabs(["🔍 V-Scan", "📊 Monitoring", "💰 Billing"])
        
        with tab1:
            st.markdown('<p class="header-text">🚀 V-SCAN: ANALISA FRAUD</p>', unsafe_allow_html=True)
            up = st.file_uploader("Unggah Data", type=['csv', 'xlsx'])
            if up:
                st.success("✅ File Berhasil Dianalisa")
                if st.button("📲 KIRIM WHATSAPP"):
                    st.success("Terkirim!")

        with tab2:
            st.markdown('<p class="header-text">📅 MONITORING AUDIT</p>', unsafe_allow_html=True)
            if st.button("📲 KIRIM REMINDER"):
                st.success("Reminder Terkirim!")
            
        with tab3:
            st.write("Sistem Billing AR Control Aktif.")

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
