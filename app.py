import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM (STABIL & MEWAH) ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .header-box { 
        text-align: center; padding: 40px; background: white; 
        border-bottom: 5px solid #1e3a8a; margin-bottom: 30px; 
    }
    .main-title { font-size: 3.5rem !important; font-weight: 800; color: #1e3a8a; }
    .profile-card { 
        background: white; padding: 30px; border-radius: 20px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-left: 10px solid #1e3a8a;
    }import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM (STABIL & PREMIUM) ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .header-box { 
        text-align: center; padding: 40px; background: white; 
        border-bottom: 5px solid #1e3a8a; margin-bottom: 30px; 
    }
    .main-title { font-size: 3.5rem !important; font-weight: 800; color: #1e3a8a; }
    .profile-card { 
        background: white; padding: 30px; border-radius: 20px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-left: 10px solid #1e3a8a;
    }
    .roi-container {
        background: #eff6ff; padding: 30px; border-radius: 20px;
        border: 2px dashed #1e3a8a; margin: 30px 0;
    }
    .card-paket {
        background: white; padding: 30px; border-radius: 20px; border: 1px solid #e2e8f0;
        height: 550px; text-align: center;
    }
    .price-tag { font-size: 2.2rem; font-weight: bold; color: #1e3a8a; margin: 15px 0; }
    .alarm-tag { 
        background: #fee2e2; color: #ef4444; padding: 6px 15px; border-radius: 20px; 
        font-size: 0.85rem; font-weight: bold; margin-top: 20px; display: inline-block;
    }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 12px; height: 50px; font-weight: bold; width: 100%; }
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
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 4. LOGIKA NAVIGASI ---
if st.session_state.page == "Admin":
    st.title("💻 Command Center - Alat Kerja Strategis")
    t1, t2 = st.tabs(["🛡️ Deteksi Fraud", "💰 Kontrol Piutang (AR)"])
    
    with t1:
        st.subheader("Investigasi Kecurangan Real-Time")
        st.error("🚨 [ALARM] Anomali Transaksi Terdeteksi")
        if st.button("🔔 Kirim Fire Alarm"):
            st.success("Notifikasi Berhasil Dikirim!")

    with t2:
        st.subheader("Manajemen Piutang")
        st.info("PT. Niaga Sakti | Nilai: Rp 75.000.000 | Tempo: Besok")
        if st.button("📲 Kirim Reminder Penagihan"):
            st.success("WhatsApp Reminder Terkirim!")

else:
    # --- HALAMAN BERANDA ---
    st.markdown('<div class="header-box"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)

    # SEKSI PROFIL & FILOSOFI
    c_img, c_txt = st.columns([1, 2.5])
    with c_img:
        try:
            st.image("erwin.jpg", use_container_width=True)
        except:
            st.info("CEO Image")
    with c_txt:
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        **Erwin Sinaga** adalah pemimpin strategis dengan rekam jejak lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan**. Keahliannya menjadi fondasi lahirnya **VGUARD AI Systems**. 
        
        Filosofi beliau, **"Digitizing Trust, Eliminating Leakage"**, menekankan bahwa integritas bisnis harus dijaga melalui sistem digital yang transparan. Melalui teknologi **V-Guard Fire Alarm**, Pak Erwin berkomitmen menciptakan perisai pertahanan yang mendeteksi setiap indikasi fraud dan kebocoran transaksi secara real-time demi pertumbuhan usaha yang berkelanjutan.
        """)
        if st.button("🚀 BUKA ALAT KERJA ADMIN"):
            st.session_state.page = "Admin"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # --- SEKSI ROI (DIPERBAIKI TOTAL) ---
    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Profit (ROI)")
    st.markdown('<div class="roi-container">', unsafe_allow_html=True)
    col_in, col_out = st.columns(2)
    with col_in:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000, step=10000000)
        bocor = st.slider("Estimasi Kebocoran (%)", 1, 10, 3)
    with col_out:
        kerugian = omzet * (bocor/100)
        hasil_saved = kerugian * 0.95
        st.write(f"### Potensi Kerugian: Rp {kerugian:,.0f}")
        st.success(f"### Diselamatkan V-Guard: Rp {hasil_saved:,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

    # SEKSI LAYANAN
    st.write("---")
    .roi-container {
        background: #eff6ff; padding: 30px; border-radius: 20px;
        border: 2px dashed #1e3a8a; margin: 30px 0;
    }
    .card-paket {
        background: white; padding: 30px; border-radius: 20px; border: 1px solid #e2e8f0;
        height: 550px; text-align: center; transition: 0.3s;
    }
    .card-paket:hover { border-color: #ef4444; }
    .price-tag { font-size: 2.2rem; font-weight: bold; color: #1e3a8a; margin: 15px 0; }
    .alarm-tag { 
        background: #fee2e2; color: #ef4444; padding: 6px 15px; border-radius: 20px; 
        font-size: 0.85rem; font-weight: bold; margin-top: 20px; display: inline-block;
    }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 12px; height: 50px; font-weight: bold; width: 100%; }
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
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 4. LOGIKA NAVIGASI ---
if st.session_state.page == "Admin":
    st.title("💻 Command Center - Alat Kerja Strategis")
    t1, t2 = st.tabs(["🛡️ Deteksi Fraud", "💰 Kontrol Piutang (AR)"])
    
    with t1:
        st.subheader("Investigasi Kecurangan Real-Time")
        st.error("🚨 [ALARM] Anomali Transaksi Terdeteksi: Store Tangerang")
        if st.button("🔔 Kirim Fire Alarm"):
            st.success("Notifikasi Berhasil Dikirim!")

    with t2:
        st.subheader("Manajemen Piutang Jatuh Tempo")
        st.info("PT. Niaga Sakti | Nilai: Rp 75.000.000 | Tempo: Besok")
        if st.button("📲 Kirim Reminder Penagihan"):
            st.success("WhatsApp Reminder Terkirim!")

else:
    # --- HALAMAN BERANDA ---
    st.markdown('<div class="header-box"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)

    # SEKSI PROFIL & FILOSOFI
    c_img, c_txt = st.columns([1, 2.5])
    with c_img:
        try:
            st.image("erwin.jpg", use_container_width=True)
        except:
            st.info("CEO Image")
    with c_txt:
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        **Erwin Sinaga** adalah pemimpin strategis dengan rekam jejak lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan**. Keahliannya menjadi fondasi lahirnya **VGUARD AI Systems**. 
        
        Filosofi beliau, **"Digitizing Trust, Eliminating Leakage"**, menekankan bahwa integritas bisnis harus dijaga melalui sistem digital yang transparan. Melalui teknologi **V-Guard Fire Alarm**, Pak Erwin berkomitmen menciptakan perisai pertahanan yang mendeteksi setiap indikasi fraud dan kebocoran transaksi secara real-time demi pertumbuhan usaha yang berkelanjutan.
        """)
        if st.button("🚀 BUKA ALAT KERJA ADMIN"):
            st.session_state.page = "Admin"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # SEKSI ROI
    st.write("---")
    st.subheader("📈 Kalkulator Pen
