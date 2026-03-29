import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- 2. CSS (DIBERSIHKAN TOTAL) ---
st.markdown("""
<style>
    .main { background-color: #f1f5f9; }
    .header-box { 
        text-align: center; 
        padding: 40px; 
        background: white; 
        border-bottom: 5px solid #1e3a8a; 
        margin-bottom: 30px; 
    }
    .profile-card { 
        background: white; 
        padding: 40px; 
        border-radius: 20px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.1); 
        border-left: 10px solid #1e3a8a; 
    }
    .roi-container { 
        background: #eff6ff; 
        padding: 30px; 
        border-radius: 20px; 
        border: 2px dashed #1e3a8a; 
        margin: 30px 0; 
    }
    .card-paket { 
        background: white; 
        padding: 25px; 
        border-radius: 20px; 
        border: 1px solid #e2e8f0; 
        height: 480px; 
        text-align: center; 
    }
    .price-tag { font-size: 1.8rem; font-weight: bold; color: #1e3a8a; margin: 10px 0; }
    .stButton>button { 
        background: #1e3a8a !important; 
        color: white !important; 
        border-radius: 12px; 
        height: 50px; 
        font-weight: bold; 
        width: 100%; 
    }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
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
    if st.session_state.authenticated:
        if st.button("🔓 Log Out Admin"):
            st.session_state.authenticated = False
            st.session_state.page = "Home"
            st.rerun()
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 4. FUNGSI PAKET ---
def draw_paket(title, price, desc):
    st.markdown(f"""
    <div class="card-paket">
        <h3 style="color:#1e3a8a;">{title}</h3>
        <div class="price-tag">{price}</div>
        <hr>
        <div style="text-align:left; font-size:0.9rem; min-height:160px;">{desc}</div>
        <div style="background:#fee2e2; color:#ef4444; padding:5px; border-radius:10px; font-size:0.75rem; font-weight:bold; margin-top:20px;">🔥 Fire Alarm Ready</div>
    </div>
    """, unsafe_allow_html=True)

# --- 5. LOGIKA NAVIGASI ---
if st.session_state.page == "Admin":
    if not st.session_state.authenticated:
        st.title("🔐 Akses Terbatas Admin")
        # Password Anda: VGUARD2026
        pwd = st.text_input("Masukkan Password Executive:", type="password")
        if st.button("Masuk ke Command Center"):
            if pwd == "VGUARD2026":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Password Salah. Akses Ditolak.")
    else:
        st.title("💻 Command Center - Erwin Sinaga")
        
        # FITUR UNGGAH & AUDIT
        st.subheader("🛡️ Audit Data & Fraud Detection")
        up = st.file_uploader("Unggah Laporan Transaksi Klien", type=['csv', 'xlsx'])
        if up: st.success("Data diterima. V-Guard AI siap melakukan audit.")
        
        # ALARM PIUTANG
        st.write("---")
        st.subheader("💰 Alarm Monitoring Piutang (AR)")
        st.warning("⚠️ Terdeteksi 3 Piutang Mendekati Jatuh Tempo")
        if st.button("🚨 KIRIM ALARM PIUTANG (WA)"):
            st.success("WhatsApp Alert Terkirim Otomatis!")

else:
    # --- HALAMAN BERANDA ---
    st.markdown('<div class="header-box"><h1 style="color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1></div>', unsafe_allow_html=True)

    # SEKSI PROFIL
    c1, c2 = st.columns([1, 2.8])
    with c1:
        try: st.image("erwin.jpg", use_container_width=True)
        except: st.info("CEO Image")
    with c2:
        st.markdown(f"""
        <div class="profile-card">
            <h2 style="color:#1e3a8a;">👤 Profil & Filosofi: Erwin Sinaga</h2>
            <p style="font-size:1.1rem; line-height:1.8; text-align:justify;">
                Erwin Sinaga memadukan pengalaman eksekutif perbankan selama lebih dari 10 tahun dengan teknologi AI untuk mewujudkan visi <b>'Digitizing Trust, Eliminating Leakage'</b>. VGUARD AI hadir sebagai perisai pertahanan bisnis Anda terhadap kebocoran profit dan fraud.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.button("🚀 BUKA COMMAND CENTER"):
            st.session_state.page = "Admin"
            st.rerun()

    # SEKSI ROI
    st.write("---")
    st.subheader("📈 Kalkulator ROI Penyelamatan Profit")
    st.markdown('<div class="roi-container">', unsafe_allow_html=True)
    o = st.number_input("Omzet Bulanan (Rp)", value=100000000, step=10
