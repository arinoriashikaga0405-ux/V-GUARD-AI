import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

# 1. SETUP
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")
wa_url = "https://wa.me/6282122190885"

# 2. DATA PAKET
pkgs = {
    "MIKRO": {"N": "Basic Guard", "S": 2500000, "M": 500000},
    "MENENGAH": {"N": "Premium Shield", "S": 7500000, "M": 1500000},
    "ENTERPRISE": {"N": "Enterprise Vault", "S": 50000000, "M": 5000000},
    "CORPORATE": {"N": "Elite Managed", "S": 85000000, "M": 10000000}
}

# 3. NAVIGASI
menu = st.sidebar.radio("Pilih Menu:", ["🏠 Home", "📦 Produk", "👤 Profil", "🔐 Admin"])

# --- HOME ---
if menu == "🏠 Home":
    st.title("🛡️ V-Guard AI Systems")
    st.write("Solusi intermediary cerdas untuk keamanan bisnis Anda.")
    st.write("---")
    c1, c2, c3 = st.columns(3)
    with c1: st.info("**Real-time Detection**")
    with c2: st.info("**End-to-End Link**")
    with c3: st.info("**Risk Scoring**")

# --- PRODUK ---
elif menu == "📦 Produk":
    st.title("📦 Paket Investasi Keamanan")
    cols = st.columns(4)
    for i, (tier, data) in enumerate(pkgs.items()):
        with cols[i]:
            st.subheader(f"🛡️ {tier}")
            st.write(f"Setup: Rp {data['S']:,}")
            st.write(f"Bulanan: Rp {data['M']:,}")
            st.link_button(f"Pesan {tier}", wa_url, use_container_width=True)

# --- PROFIL ---
elif menu == "👤 Profil":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
        else: st.subheader("Founder Erwin Sinaga")
    with r:
        st.subheader("Erwin Sinaga")
        st.write("Bapak Erwin Sinaga adalah Senior Business Leader dengan pengalaman 10+ tahun sebagai CEO/CSO di perbankan.")

# --- ADMIN DASHBOARD ---
elif menu == "🔐 Admin":
    st.title("🔐 Secure Admin Access")
    if 'auth' not in st.session_state: st.session_state.auth = False
    
    if not st.session_state.auth:
        pwd = st.text_input("Password Admin:", type="password")
        if st.button("Authorize"):
            if pwd == st.secrets["ADMIN_PASSWORD"]:
                st.session_state.auth = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        st.success("Akses Diberikan. Selamat datang, Pak Erwin.")
        if st.button("Logout"):
            st.session_state.auth = False
            st.rerun()
        
        tab1, tab2 = st.tabs(["🚨 Alarm Monitoring", "🧾 Invoice"])
        
        with tab1:
            st.subheader("🚨 Live Security Alarm")
            st.error("18:45 | Massive Withdrawal | 🚨 ANOMALI | Origin: Unknown (Proxy)")
            st.write("18:32 | API Request | Aman | Origin: 104.22.1.5")
            st.write("18:30 | Login Access | Aman | Origin: 192.168.1.1")
            
            st.write("---")
            val_anomali = st.slider("Simulasi Anomali (%):", 0, 100, 6)
            fig = px.pie(values=[100-val_anomali, val_anomali], names=['Aman', 'Anomali'], hole=0.4, color_discrete_sequence=['#00CC96', '#EF553B'])
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            st.subheader("🧾 Invoice Generator")
            c_name = st.text_input("Nama Klien:")
            c_pkg = st.selectbox("Pilih Paket:", list(pkgs.keys()))
            
            if st.button("Generate Invoice"):
                sel = pkgs[c_pkg]
                tot = sel['S'] + sel['M']
                st.info(f"INVOICE #VGD-{datetime.now().strftime('%Y%m%d')}")
                st.write(f"Klien: {c_name}")
                st.write(f"Paket: {sel['N']}")
                st.write(f"Setup: Rp {sel['S']:,}")
                st.write(f"Bulanan: Rp {sel['M']:,}")
                st.markdown(f"### TOTAL: Rp {tot:,}")
                st.write("Draf siap dikirimkan.")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
