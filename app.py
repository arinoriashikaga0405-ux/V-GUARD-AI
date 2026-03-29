import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .main-title { font-size: 3rem !important; font-weight: 800; color: #1e3a8a; text-align: center; }
    .card-paket {
        background-color: #ffffff; padding: 20px; border-radius: 15px; 
        border: 1px solid #e2e8f0; height: 450px; text-align: center;
    }
    .alarm-tag { 
        color: #ef4444; font-weight: bold; font-size: 0.85rem;
        border: 1px solid #fecaca; background: #fee2e2; padding: 4px; border-radius: 5px;
    }
    .stButton>button { background-color: #1e3a8a; color: white; border-radius: 8px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI")
    if st.button("🏠 Beranda Utama"):
        st.session_state.page = "Home"
        st.rerun()
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 4. LOGIKA NAVIGASI ---
if st.session_state.page == "Admin":
    st.title("💻 Admin Portal")
    pwd = st.text_input("Password", type="password")
    if pwd == "vguard2026":
        st.warning("🚨 [ALARM] Temuan Mencurigakan Terdeteksi!")
        if st.button("🔔 Kirim Fire Alarm"):
            st.error("Alarm Terkirim!")

elif st.session_state.page == "Klien":
    st.title("📱 Owner Dashboard")
    st.metric("Status Keamanan", "PROTECTED", "V-Guard AI")
    st.info("Log Terakhir: [ALARM] Deteksi Fraud di Store 01.")

else:
    # --- BERANDA ---
    st.markdown('<p class="main-title">🛡️ VGUARD AI SYSTEMS</p>', unsafe_allow_html=True)
    
    # Profil CEO (Single Line String)
    txt = "Saya **Erwin**, Founder VGUARD AI, membawa **10 tahun pengalaman perbankan** untuk mengamankan bisnis Anda melalui teknologi **V-Guard Fire Alarm**."
    st.info(txt)

    col_adm, col_cli = st.columns(2)
    with col_adm:
        if st.button("Masuk Admin Portal"):
            st.session_state.page = "Admin"
            st.rerun()
    with col_cli:
        if st.button("Masuk Client Portal"):
            st.session_state.page = "Klien"
            st.rerun()

    st.write("---")
    st.subheader("🏷️ LAYANAN & FITUR UTAMA")
    p1, p2, p3, p4 = st.columns(4)
    
    # Definisi HTML yang Ringkas agar tidak terpotong
    with p1:
        st.markdown('<div class="card-paket"><b>V-START</b><h3>2.5 JT</h3><hr><p>• Audit Retail<br>• Notif WA<br><br><span class="alarm-tag">🔥 Fire Alarm</span></p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="card-paket"><b>V-GROW</b><h3>5 JT</h3><hr><p>• AI Fraud Deteksi<br>• Sinkron Stok<br><br><span class="alarm-tag">🔥 Fire Alarm</span></p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="card-paket"><b>V-PRIME</b><h3>10 JT</h3><hr><p>• Multi-Cabang<br>• Predictive AI<br><br><span class="alarm-tag">🔥 Fire Alarm</span></p></div>', unsafe_allow_html=True)
    with p4:
        st.markdown('<div class="card-paket"><b>V-CUSTOM</b><h3>NEGO</h3><hr><p>• Solusi Enterprise<br>• Integrasi ERP<br><br><span class="alarm-tag">🔥 Fire Alarm</span></p></div>', unsafe_allow_html=True)

st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin")
