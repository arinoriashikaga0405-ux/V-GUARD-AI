import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - CEO Erwin Sinaga", page_icon="🛡️", layout="wide")

# --- 2. CSS BAKU (KEMBALI KE PUTIH BERSIH & RAPI) ---
st.markdown("""
<style>
    .stApp { background-color: white; }
    
    /* Header Tengah Baku */
    .header-container {
        display: flex; align-items: center; justify-content: center;
        gap: 15px; padding: 30px 0;
    }
    .main-title {
        color: #1e3a8a; font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 2.5em; font-weight: 800; margin: 0;
    }
    
    /* Box Profil Rapi */
    .profile-box { 
        background: #f8fafc; padding: 25px; border-radius: 15px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-left: 5px solid #1e3a8a;
    }
    
    /* Paket Layanan Strategis (4 Kolom) */
    .package-card { 
        background: white; padding: 20px; border-radius: 12px; 
        border: 1px solid #e2e8f0; text-align: center; height: 100%;
        display: flex; flex-direction: column; 
    }
    .pkg-name { color: #1e3a8a; font-size: 1.5em; font-weight: bold; }
    .pkg-price { color: #1e3a8a; font-size: 1.8em; font-weight: bold; margin: 15px 0; }
    .wa-button { 
        display: block; background: #25d366; color: white !important; 
        text-decoration: none !important; padding: 12px; border-radius: 8px; 
        font-weight: bold; margin-top: auto;
    }
</style>
""", unsafe_allow_html=True)

wa_number = "62821221190885"

if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 3. BERANDA UTAMA (KEMBALI KE KONSEP AWAL) ---
if st.session_state.page == "Home":
    # HEADER TENGAH
    st.markdown("""
    <div class="header-container">
        <img src="https://cdn-icons-png.flaticon.com/512/1004/1004666.png" width="50">
        <h1 class="main-title">VGUARD AI SYSTEMS</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # SEKSI PROFIL & FILOSOFI
    c1, c2 = st.columns([1, 2.5])
    with c1:
        # Foto Profil Baku
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", use_container_width=True)
        st.info("Founder & CEO: Erwin Sinaga")
    with c2:
        st.markdown('<div class="profile-box">', unsafe_allow_html=True)
        st.markdown("### 👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        Pemimpin strategis dengan pengalaman lebih dari sepuluh tahun sebagai eksekutif senior di perbankan nasional. 
        **VGUARD AI Systems** hadir sebagai solusi presisi tinggi untuk mengamankan aset bisnis Anda dari risiko kebocoran data.

        Filosofi Kami: **"Presisi Tanpa Kompromi"**.
        """)
        if st.button("🚀 MASUK KE COMMAND CENTER"):
            st.session_state.page = "Admin"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")
    
    # FITUR ANALISIS ROI (PENGAMAN PROFIT)
    st.markdown("#### 📊 ANALISIS POTENSI KERUGIAN & PROTEKSI PROFIT")
    col_a, col_b = st.columns(2)
    with col_a: omzet = st.number_input("Omzet Bulanan (Rp)", value=250000000)
    with col_b: bocor = st.slider("Estimasi Kebocoran (%)", 1, 10, 3)
    st.success(f"Potensi Profit Diselamatkan: Rp {(omzet * (bocor/100) * 0.95):,.0f} / bln")

    # PAKET LAYANAN STRATEGIS (4 KOLOM RAPI)
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    p1, p2, p3, p4 = st.columns(4)
    
    packs = [
        {"n": "V-START", "t": "Target: UMKM", "p": "Rp 5 JT", "f": ["Scan Harian", "Laporan Mingguan", "Support Desk"]},
        {"n": "V-GROW", "t": "Target: Multi-Cabang", "p": "Rp 15 JT", "f": ["Real-time Scan", "Notifikasi WA", "Priority Support"]},
        {"n": "V-PRIME", "t": "Target: Korporasi", "p": "Rp 50 JT", "f": ["Audit Trail Bank", "Full AI Support", "Dedicated Manager"]},
        {"n": "V-ENTERPRISE", "t": "Target: Holding", "p": "Rp 150 JT", "f": ["Private Server", "Custom AI Model", "CEO Advisory"]}
    ]
    
    cols = [p1, p2, p3, p4]
    for i, x in enumerate(packs):
        with cols[i]:
            st.markdown(f"""
            <div class="package-card">
                <div class="pkg-name">{x['n']}</div>
                <div style="font-size:0.8em; color:gray;">{x['t']}</div>
                <hr style="border: 0.5px solid #e2e8f0; margin: 15px 0;">
                <div class="pkg-price">{x['p']} <span style="font-size:0.4em; color:gray;">/ bln</span></div>
                <div style="text-align:left; font-size:0.85em; margin-bottom:20px; flex-grow:1;">
                    {"".join([f"• {feat}<br>" for feat in x['f']])}
                </div>
                <a href="https://wa.me/{wa_number}?text=Halo Pak Erwin, saya tertarik paket {x['n']}" class="wa-button">💬 Chat WhatsApp</a>
            </div>
            """, unsafe_allow_html=True)

# --- 4. PANEL ADMIN ---
elif st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.markdown('<h1 style="text-align:center;">🔐 Executive Access</h1>', unsafe_allow_html=True)
        pwd = st.text_input("Password Admin:", type="password")
        if st.button("Masuk"):
            if pwd == "VGUARD2026": st.session_state.auth = True; st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        st.header("💻 Command Center - Erwin Sinaga")
        st.tabs(["🔍 V-Scan", "📊 Monitoring", "📍 Map", "💰 Billing", "⚙️ Klien"])
        if st.sidebar.button("🔓 Logout"):
            st.session_state.auth = False; st.session_state.page = "Home"; st.rerun()

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | CEO Erwin Sinaga")
