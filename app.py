import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIG & PERMANENT STATE ---
st.set_page_config(page_title="VGUARD AI Systems - CEO Erwin Sinaga", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. CSS BAKU & KAKU (IDENTIK DENGAN SCREENSHOT) ---
# Tujuannya agar visual tidak berubah tanpa persetujuan Bapak.
st.markdown("""
<style>
    .stApp { background-color: white; }
    
    /* Sidebar Gelap Baku */
    [data-testid="stSidebar"] { 
        background-color: #0f172a !important; 
        color: white !important;
        padding-top: 30px;
    }
    [data-testid="stSidebar"] *, .stButton>button { color: white !important; font-weight: bold; }
    
    /* Tombol Navigasi Merah Baku */
    .stButton>button { 
        background-color: #dc2626 !important; 
        border-radius: 8px; 
        width: 100%; height: 45px; margin-bottom: 10px;
    }

    /* Kontainer Banner Tengah */
    .vguard-banner {
        display: flex; align-items: center; justify-content: center;
        gap: 15px; background: white; padding: 25px; border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 30px;
    }
    .banner-text { color: #1e3a8a; font-size: 2.2em; font-weight: bold; margin: 0; }
    
    /* Foto & Profil Baku */
    .profile-box { background: #f8fafc; padding: 20px; border-radius: 12px; height: 100%; border-left: 5px solid #1e3a8a; }

    /* Paket Layanan Ramping (4 Kolom) */
    .pkg-card {
        background: white; border: 1px solid #e2e8f0; padding: 20px;
        border-radius: 10px; text-align: center; height: 100%;
        display: flex; flex-direction: column;
    }
    .pkg-name { color: #1e3a8a; font-size: 1.4em; font-weight: bold; }
    .wa-button { 
        display: block; background: #25d366; color: white !important; 
        text-decoration: none !important; padding: 10px; border-radius: 8px; 
        font-weight: bold; text-align: center; margin-top: auto;
    }
</style>
""", unsafe_allow_html=True)

wa_num = "62821221190885"

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)
    # Foto Bulat Baku
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
    st.markdown("### CEO: ERWIN SINAGA")
    st.write("---")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🏠 BERANDA UTAMA"):
        st.session_state.page = "Home"
        st.rerun()
    
    if st.session_state.auth:
        if st.button("🔓 KELUAR"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()

# --- 4. HALAMAN BERANDA ---
if st.session_state.page == "Home":
    # Banner Tengah Baku
    st.markdown(f"""
    <div class="vguard-banner">
        <img src="https://cdn-icons-png.flaticon.com/512/1004/1004666.png" width="40">
        <h1 class="banner-text">VGUARD AI SYSTEMS</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Foto & Profil Baku
    c1, c2 = st.columns([1, 2.3])
    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", caption="CEO Erwin Sinaga", use_container_width=True)
    with c2:
        st.markdown('<div class="profile-box">', unsafe_allow_html=True)
        st.markdown("### 👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        **Erwin Sinaga** adalah pemimpin strategis dengan rekam jejak prestisius selama lebih dari sepuluh tahun sebagai eksekutif senior di industri perbankan nasional. Melalui **VGUARD AI Systems**, beliau mentransformasi keahlian audit perbankan ke dalam solusi teknologi cerdas untuk mengamankan profit bisnis dari ancaman fraud.

        Filosofi beliau, **"Presisi Tanpa Kompromi"**, memastikan bahwa setiap modul AI bekerja dengan akurasi maksimal demi integritas data dan keamanan aset klien.
        """)
        if st.button("🚀 BUKA COMMAND CENTER (ADMIN)"):
            st.session_state.page = "Admin"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")
    
    # Analisis ROI
    st.markdown("#### 📊 ANALISIS PROTEKSI PROFIT")
    ca, cb = st.columns(2)
    with ca: 
        omzet = st.number_input("Omzet Bulanan (Rp)", value=250000000)
    with cb: 
        bocor = st.slider("Estimasi Kebocoran (%)", 1, 15, 3)
    
    saved = omzet * (bocor/100) * 0.95
    st.success(f"Potensi Profit Diselamatkan V-GUARD: Rp {saved:,.0f} / bln")

    st.write("---")
    
    # Paket Layanan Ramping (4 Kolom)
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    p1, p2, p3, p4 = st.columns(4)
    
    packs = [
        {"n": "V-START", "p": "Rp 5 JT", "f": ["Scan Harian", "Report Mingguan"]},
        {"n": "V-GROW", "p": "Rp 15 JT", "f": ["Real-time Scan", "Notifikasi WA"]},
        {"n": "V-PRIME", "p": "Rp 50 JT", "f": ["Audit Trail Bank", "Full Support"]},
        {"n": "V-ENTERPRISE", "p": "Custom", "f": ["Private Server", "Custom AI Model"]}
    ]
    
    cols = [p1, p2, p3, p4]
    for i, x in enumerate(packs):
        with cols[i]:
            st.markdown(f"""
            <div class="pkg-card">
                <div class="pkg-name">{x['n']}</div>
                <hr style="border: 0.5px solid #e2e8f0; margin: 15px 0;">
                <div style="color:gray;font-size:0.8em;">Target: Bisnis</div>
                <div class="pkg-price">{x['p']} <span style="font-size:0.4em; color:gray;">/ bln</span></div>
                <div style="text-align:left; font-size:0.9em; margin-bottom:15px; flex-grow:1;">
                    {"".join([f"• {feat}<br>" for feat in x['f']])}
                </div>
                <a href="https://wa.me/{wa_num}?text=Halo Pak Erwin, saya tertarik paket {x['n']}" class="wa-button">💬 Chat WhatsApp</a>
            </div>
            """, unsafe_allow_html=True)

# --- 5. HALAMAN ADMIN (COMMAND CENTER) ---
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
        st.header("💻
