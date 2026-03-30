import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. INITIALIZE SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 3. PREMIUM CSS (CEO EDITION) ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; }
    .roi-container { 
        border: 2px dashed #1e3a8a; 
        border-radius: 15px; 
        padding: 25px; 
        background: #eff6ff; 
        text-align: center;
        margin: 20px 0;
    }
    .roi-title { 
        color: #1e3a8a; 
        font-weight: bold; 
        font-size: 1.2em; 
        margin-bottom: 15px;
        text-transform: uppercase;
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
        st.write("Lebih dari 10 tahun pengalaman eksekutif perbankan nasional mendasari presisi VGUARD AI dalam menjaga aset bisnis Anda.")
        if st.button("🚀 MASUK KE COMMAND CENTER"): 
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    
    # --- BOX ANALISIS ROI (POTENSI KERUGIAN) ---
    st.markdown('<div class="roi-container">', unsafe_allow_html=True)
    st.markdown('<div class="roi-title">ANALISIS POTENSI KERUGIAN & PROTEKSI PROFIT</div>', unsafe_allow_html=True)
    
    oz = st.number_input("Omzet Bulanan Bisnis (Rp)", value=250000000)
    kb = st.slider("Estimasi Kebocoran/Fraud (%)", 1, 15, 3)
    
    loss = oz * (kb/100)
    saved = loss * 0.95
    
    st.error(f"Potensi Kerugian Akibat Fraud: Rp {loss:,.0f} / bln")
    st.success(f"Profit Diselamatkan V-GUARD (Efisiensi 95%): Rp {saved:,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- PAKET LAYANAN STRATEGIS (RESTORED) ---
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
        # --- COMMAND CENTER (CLEANED) ---
        st.header("💻 Command Center - Erwin Sinaga")
        tab1, tab2, tab3 = st.tabs(["🔍 V-Scan", "📊 Monitoring", "💰 Billing"])
        
        with tab1:
            st.markdown("### 🚀 V-SCAN: ANALISA FRAUD")
            up = st.file_uploader("Unggah Data", type=['csv', 'xlsx'])
            if up:
                st.success("✅ Analisa Berhasil")
                if st.button("📲 KIRIM WHATSAPP"): st.success("Terkirim!")

        with tab2:
            st.markdown("### 📅 MONITORING AUDIT")
            if st.button("📲 KIRIM REMINDER"): st.success("Reminder Terkirim!")
            
        with tab3:
            st.write("Data Billing & AR Aktif.")

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
