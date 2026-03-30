import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- 1. INITIALIZE SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False
if 'audit_logs' not in st.session_state:
    st.session_state.audit_logs = [
        {"Klien": "Toko Berkah Jaya", "Segmen": "Retail", "Jadwal": "21:00", "Status": "✅ Terpindai", "Hasil": "Aman"},
        {"Klien": "B2B Trading Sinar", "Segmen": "Trading", "Jadwal": "22:30", "Status": "❌ Belum Upload", "Hasil": "Pending"}
    ]

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# --- 3. PREMIUM CSS ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; height: 45px; }
    .card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #e2e8f0; text-align: center; height: 100%; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .roi-box { background: #eff6ff; padding: 25px; border-radius: 15px; border: 2px dashed #1e3a8a; }
    .header-text { color: #1e3a8a; font-weight: bold; border-left: 5px solid #1e3a8a; padding-left: 10px; margin-bottom: 15px; }
    .metric-card { background: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; }
    .admin-card { background: #f1f5f9; padding: 15px; border-radius: 10px; border-left: 5px solid #1e3a8a; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("### 👤 CEO: ERWIN SINAGA")
    st.caption("Founder & CEO VGUARD AI")
    st.write("---")
    if st.button("🏠 Beranda Utama"): 
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.auth:
        if st.button("🔓 Log Out Admin"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 5. LOGIKA HALAMAN ---
if st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🔐 Executive Access</h1>', unsafe_allow_html=True)
        col_l1, col_l2, col_l3 = st.columns([1,2,1])
        with col_l2:
            pwd = st.text_input("Password Admin:", type="password")
            if st.button("Masuk ke Command Center"):
                if pwd == "VGUARD2026":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Akses Ditolak!")
    else:
        # --- COMMAND CENTER ---
        st.header("💻 Command Center - Erwin Sinaga")
        m1, m2, m3, m4 = st.columns(4)
        with m1: st.markdown('<div class="metric-card">💰 <b>Total Saved</b><br>Rp 1.450.000.000</div>', unsafe_allow_html=True)
        with m2: st.markdown('<div class="metric-card">👥 <b>Klien Aktif</b><br>12 Perusahaan</div>', unsafe_allow_html=True)
        with m3: st.markdown('<div class="metric-card">⚠️ <b>Fraud Alert</b><br>2 Temuan Hari Ini</div>', unsafe_allow_html=True)
