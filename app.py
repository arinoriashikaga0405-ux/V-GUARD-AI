import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Dashboard", page_icon="🛡️", layout="wide")
wa_num = "6282122190885"

# 2. SISTEM LOGIN
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI SECURE GATE")
    st.subheader("Founder: Erwin Sinaga")
    pwd_input = st.text_input("Masukkan Password Admin:", type="password")
    if st.button("Authorize Access"):
        try:
            if pwd_input.strip() == st.secrets["ADMIN_PASSWORD"].strip():
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("❌ Password Salah.")
        except:
            st.error("⚠️ Atur ADMIN_PASSWORD di menu Secrets Streamlit!")
    st.stop()

# 3. NAVIGASI SIDEBAR
st.sidebar.title("🛡️ V-Guard AI Menu")
page = st.sidebar.radio("Navigasi:", ["🏠 Home", "📊 Dashboard Monitoring", "📦 Products & Packages", "👤 Corporate Profile"])

if st.sidebar.button("🔒 Logout"):
    st.session_state.auth = False
    st.rerun()

# --- HALAMAN 1: HOME ---
if page == "🏠 Home":
    st.title("🛡️ Welcome to V-Guard AI")
    st.header("Our Philosophy")
    st.write("At V-Guard AI, our philosophy is: **Empowering Businesses Through Intelligent Protection**.")
    st.write("---")
    st.subheader("🎯 Vision & Mission")
    c1, c2 = st.columns(2)
    with c1: st.info("**Vision**: Menjadi penyedia solusi keamanan finansial berbasis AI terdepan global.")
    with c2: st.info("**Mission**: Mengembangkan teknologi AI inovatif yang proaktif.")

# --- HALAMAN 2: DASHBOARD MONITORING ---
elif page == "📊 Dashboard Monitoring":
    st.header("📊 V-Guard Real-time Monitoring")
    st.success("Sistem AI aktif mengawasi anomali transaksi.")
    df_data = pd.DataFrame({'Kategori': ['Aman', 'Anomali'], 'Skor': [94, 6]})
    fig_data = px.pie(df_data, values='Skor', names='Kategori', title="Ringkasan Risiko Hari Ini", hole=0.3)
    st.plotly_chart(fig_data, use_container_width=True)

# --- HALAMAN 3: PRODUCTS & PACKAGES ---
elif page == "📦 Products & Packages":
    st.header("📦 Our Products & Services Packages")
    st.write("Silakan pilih paket investasi keamanan yang sesuai.")
    
    pkgs = [
        {"N": "Mikro", "P": "Basic Guard", "S": "2.5jt", "B": "750rb", "F": ["Real-time Mon", "Email Alert"]},
        {"N": "Menengah", "P": "Premium Shield", "S": "7.5jt", "B": "2.5jt", "F": ["Advanced AI", "WA Alert"]},
        {"N": "Enterprise", "P": "Enterprise Vault", "S": "50jt", "B": "8.5jt", "F": ["ERP Integration", "AI CCTV"]},
        {"N": "Corporate", "P": "Elite Managed", "S": "85jt", "B": "15jt", "F": ["Face Recognition", "CSO Advisory"]}
    ]
    
    cols = st.columns(4)
    for i, p in enumerate(pkgs):
        with cols[i]:
            st.warning(f"**{p['N']}**")
            st.subheader(p['P'])
            st.write(f"Setup: **Rp {p['S']}**")
            st.write(f"Bulan: **Rp {p['B']}**")
            for feat in p['F']:
                st.write(f"- {feat}")
            wa_url = f"https://wa.me/{wa_num}?text=Halo%20Pak%20Erwin%2C%20minat%20paket%20{p['P
