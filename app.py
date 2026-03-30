import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. INITIALIZE SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 3. PREMIUM CSS ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; height: 45px; }
    .roi-box-header { 
        background: #eff6ff; 
        padding: 20px; 
        border-radius: 15px 15px 0 0; 
        border: 2px dashed #1e3a8a; 
        border-bottom: none;
        text-align: center; 
        font-weight: bold;
        color: #1e3a8a;
        letter-spacing: 1px;
    }
    .roi-box-body { 
        background: #ffffff; 
        padding: 20px; 
        border-radius: 0 0 15px 15px; 
        border: 2px dashed #1e3a8a; 
        margin-bottom: 20px;
    }
    .package-card { background: white; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; text-align: center; height: 100%; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("### 👤 CEO: ERWIN SINAGA")
    st.write("---")
    if st.button("🏠 Beranda Utama"): 
        st.session_state.page = "Home"
        st.rerun()

# --- 5. HALAMAN DEPAN ---
if st.session_state.page == "Home":
    st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2.5])
    with col1:
        st.info("📷 FOTO CEO ERWIN SINAGA")
    with col2:
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("Erwin Sinaga adalah pemimpin strategis dengan rekam jejak profesional lebih dari sepuluh tahun di perbankan nasional. VGUARD AI adalah perisai pertahanan bisnis Anda.")
        if st.button("🚀 MASUK KE COMMAND CENTER"):
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    
    # KOTAK PANJANG SESUAI INSTRUKSI BAPAK
    st.markdown('<div class="roi-box-header">ANALISIS POTENSI KERUGIAN & PROTEKSI PROFIT</div>', unsafe_allow_html=True)
    st.markdown('<div class="roi-box-body">', unsafe_allow_html=True)
    oz = st.number_input("Omzet Bulanan Bisnis (Rp)", value=250000000)
    kb = st.slider("Estimasi Kebocoran/Fraud (%)", 1, 15, 3)
    hasil = oz * (kb/100)
    st.error(f"Potensi Kerugian Akibat Fraud: Rp {hasil:,.0f} / bln")
    st.success(f"Profit Diselamatkan V-GUARD (Efisiensi 95%): Rp {(hasil * 0.95):,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

    # TABEL PAKET LAYANAN (DIPERTAHANKAN)
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="package-card"><h3>🔹 V-START</h3><p>UMKM / Ritel</p><h2>Rp 5 JT</h2><p>/ bln</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="package-card" style="border:2px solid #1e3a8a;"><h3>🔶 V-GROW</h3><p>3 Cabang</p><h2>Rp 15 JT</h2><p>/ bln</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="package-card"><h3>💎 V-PRIME</h3><p>Korporasi</p><h2>Custom</h2><p>Full AI Support</p></div>', unsafe_allow_html=True)

# --- LOGIN ADMIN (SEDERHANA) ---
elif st.session_state.page == "Admin":
    st.header("🔐 Admin Access")
    pwd = st.text_input("Password:", type="password")
    if st.button("Login"):
        st.success("Akses Diberikan (Fitur Command Center Aktif)")

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin Sinaga")
