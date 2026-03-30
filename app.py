import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")
wa_url = "https://wa.me/6282122190885"

# 2. DATA MASTER (DYNAMIC PACKAGES)
pkgs = {
    "MIKRO": {"N": "Basic Guard", "S": 2500000, "M": 500000},
    "MENENGAH": {"N": "Premium Shield", "S": 7500000, "M": 1500000},
    "ENTERPRISE": {"N": "Enterprise Vault", "S": 50000000, "M": 5000000},
    "CORPORATE": {"N": "Elite Managed", "S": 85000000, "M": 10000000}
}

# 3. NAVIGASI
menu = st.sidebar.radio("Pilih Menu:", ["🏠 Home & AI Services", "📦 Produk & Layanan", "👤 Profil Founder", "🔐 Admin Dashboard"])

# --- HALAMAN 1: HOME ---
if menu == "🏠 Home & AI Services":
    st.title("🛡️ V-Guard AI Systems")
    st.write("Next-Generation Financial Security. Solusi intermediary cerdas untuk bisnis Anda.")
    st.write("---")
    c1, c2, c3 = st.columns(3)
    with c1: st.info("**Real-time Detection**")
    with c2: st.info("**End-to-End Link**")
    with c3: st.info("**Risk Scoring**")

# --- HALAMAN 2: PRODUK ---
elif menu == "📦 Produk & Layanan":
    st.title("📦 Paket Investasi Keamanan")
    cols = st.columns(4)
    for i, (tier, data) in enumerate(pkgs.items()):
        with cols[i]:
            st.subheader(f"🛡️ {tier}")
            st.write(f"Setup: **Rp {data['S']:,}**")
            st.write(f"Bulanan: **Rp {data['M']:,}**")
            st.link_button(f"Pesan {tier}", wa_url, use_container_width=True)

# --- HALAMAN 3: PROFIL ---
elif menu == "👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
        else: st.subheader("Erwin Sinaga, Founder")
    with r:
        st.subheader("Erwin Sinaga")
        st.write("Bapak Erwin Sinaga adalah Senior Business Leader dengan pengalaman 10+ tahun sebagai CEO/CSO di perbankan.")

# --- HALAMAN 4: ADMIN DASHBOARD (ALARM & INVOICE) ---
elif menu == "🔐 Admin Dashboard":
    st.title("🔐 Secure Admin Access")
    if 'auth' not in st.session_state: st.session_state.auth = False
    
    if not st.session_state.auth:
        pwd = st.text_input("Masukkan Password Admin:", type="password")
        if st.button("Authorize"):
            if pwd == st.secrets["ADMIN_PASSWORD"]:
                st.session_state.auth = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        st.success("Akses Diberikan. Selamat datang, Pak Erwin.")
        if st.button("Logout Admin"):
            st.session_state.auth = False
            st.rerun()
        
        tab1, tab2 = st.tabs(["📊 Monitoring & Alarm", "🧾 Invoice Generator"])
        
        with tab1:
            st.subheader("🚨 Live Security Alarm")
            # Simulasi Alarm Log
            log_data = [
                {"Waktu": "18:30", "Event": "Login Access", "Status": "Aman", "IP": "192.168.1.1"},
                {"Waktu": "18:32", "Event": "API Request", "Status": "Aman", "IP": "104.22.1.5"},
                {"Waktu": "18:45", "Event": "Massive Withdrawal", "Status": "🚨 ANOMALI", "IP": "Unknown (Proxy)"},
            ]
            for log in log_data:
                if "ANOMALI" in log['Status']:
                    st.error(f"**{log['Waktu']}** | {log['Event']} | {log['Status']} | Origin: {log['IP']}")
                else:
                    st.write(f"{log['Waktu']} | {log['Event']} | {log['Status']} | Origin: {log['IP']}")
            
            st.write("---")
            val_anomali = st.slider("Simulasi Tingkat Anomali (%):", 0, 100, 6)
            fig = px.pie(values=[100-val_anomali, val_anomali], names=['Aman', 'Anomali'], hole=0.4, color_discrete_sequence=['#00CC96', '#EF553B'])
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            st.subheader("🧾 Create New Invoice")
            c_name = st.text_input("Nama Klien / Perusahaan:")
            c_pkg = st.selectbox("Pilih Paket:", list(pkgs.keys()))
            
            if st.button("Generate Invoice Draft"):
                selected = pkgs[c_pkg]
                total = selected['S'] + selected['M']
                st.markdown(f"""
                ---
                **INVOICE #VGD-{datetime.now().strftime('%Y%m%d%H%M')}**
