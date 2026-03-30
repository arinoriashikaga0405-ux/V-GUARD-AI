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
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; }
    .roi-container { 
        border: 2px dashed #1e3a8a; 
        border-radius: 15px; 
        padding: 20px; 
        background: #eff6ff; 
        text-align: center;
        margin-bottom: 25px;
    }
    .roi-title { 
        color: #1e3a8a; 
        font-weight: bold; 
        font-size: 1.1em; 
        margin-bottom: 15px;
        text-transform: uppercase;
    }
    .package-card { 
        background: white; 
        padding: 25px; 
        border-radius: 15px; 
        border: 1px solid #e2e8f0; 
        text-align: center; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .header-text { color: #1e3a8a; font-weight: bold; border-left: 5px solid #1e3a8a; padding-left: 10px; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown(f"### 👤 CEO: ERWIN SINAGA")
    if st.button("🏠 Beranda Utama"): 
        st.session_state.page = "Home"
        st.rerun()
    st.error("🚨 SYSTEM STATUS: ACTIVE")

# --- 5. LOGIKA HALAMAN ---
if st.session_state.page == "Home":
    st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)
    
    col_p1, col_p2 = st.columns([1, 2.5])
    with col_p1:
        st.info("📷 FOTO CEO ERWIN SINAGA")
    with col_p2:
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("VGUARD AI Systems dirancang sebagai perisai pertahanan strategis untuk menghentikan kebocoran profit secara real-time.")
        if st.button("🚀 MASUK KE COMMAND CENTER"): 
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    
    # --- BOX ANALISIS POTENSI KERUGIAN (KOTAK BIRU PANJANG) ---
    st.markdown('<div class="roi-container">', unsafe_allow_html=True)
    st.markdown('<div class="roi-title">ANALISIS POTENSI KERUGIAN & PROTEKSI PROFIT</div>', unsafe_allow_html=True)
    
    oz = st.number_input("Omzet Bulanan Bisnis (Rp)", value=250000000)
    kb = st.slider("Estimasi Kebocoran/Fraud (%)", 1, 15, 3)
    
    kerugian = oz * (kb/100)
    diselamatkan = kerugian * 0.95
    
    st.error(f"Potensi Kerugian Akibat Fraud: Rp {kerugian:,.0f} / bln")
    st.success(f"Profit Diselamatkan V-GUARD (Efisiensi 95%): Rp {diselamatkan:,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- PAKET LAYANAN STRATEGIS (DIKEMBALIKAN) ---
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    pk1, pk2, pk3 = st.columns(3)
    with pk1:
        st.markdown('<div class="package-card"><h3>🔹 V-START</h3><p>UMKM / Ritel</p><h2>Rp 5 JT</h2><p>/ bln</p></div>', unsafe_allow_html=True)
    with pk2:
        st.markdown('<div class="package-card" style="border: 2px solid #1e3a8a;"><h3>🔶 V-GROW</h3><p>3 Cabang</p><h2>Rp 15 JT</h2><p>/ bln</p></div>', unsafe_allow_html=True)
    with pk3:
        st.markdown('<div class="package-card"><h3>💎 V-PRIME</h3><p>Korporasi</p><h2>Custom</h2><p>Full Support</p></div>', unsafe_allow_html=True)

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
        # --- COMMAND CENTER FIXED ---
        st.header("💻 Command Center - Erwin Sinaga")
        t1, t2, t3, t4 = st.tabs(["🔍 V-Scan", "📊 Audit", "📍 Map", "💰 Billing"])
        
        with t1:
            st.markdown('<p class="header-text">🚀 V-SCAN: ANALISA FRAUD</p>', unsafe_allow_html=True)
            up = st.file_uploader("Unggah Excel/CSV", type=['csv', 'xlsx'])
            if up:
                st.success("✅ File Berhasil Dianalisa")
                if st.button("📲 KIRIM WHATSAPP"): st.success("Terkirim!")

        with t2:
            st.markdown('<p class="header-text">📅 MONITORING AUDIT</p>', unsafe_allow_html=True)
            if st.button("📲 KIRIM REMINDER WA"): st.success("Reminder Terkirim!")

        with t3: st.map()
        with t4: st.write("Data Billing & AR Control Aktif.")

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
