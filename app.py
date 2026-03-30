import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Dashboard", page_icon="🛡️", layout="wide")

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
            st.error("⚠️ Password belum diatur di menu Secrets!")
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
    st.write("At V-Guard AI, our philosophy is simple: **Empowering Businesses Through Intelligent Protection**.")
    st.write("---")
    st.subheader("🎯 Vision & Mission")
    c1, c2 = st.columns(2)
    with c1: st.info("**Vision**: Menjadi penyedia solusi keamanan finansial berbasis AI terdepan secara global.")
    with c2: st.info("**Mission**: Mengembangkan teknologi AI inovatif yang mengantisipasi risiko secara otomatis.")

# --- HALAMAN 2: DASHBOARD MONITORING ---
elif page == "📊 Dashboard Monitoring":
    st.header("📊 V-Guard Real-time Monitoring")
    st.success("Sistem AI aktif mengawasi anomali transaksi.")
    df_data = pd.DataFrame({'Kategori': ['Aman', 'Anomali'], 'Skor': [94, 6]})
    fig = px.pie(df_data, values='Skor', names='Kategori', title="Ringkasan Risiko Hari Ini", hole=0.3)
    st.plotly_chart(fig, use_container_width=True)

# --- HALAMAN 3: PRODUCTS & PACKAGES ---
elif page == "📦 Products & Packages":
    st.header("📦 Our Products & Services Packages")
    st.write("Pilih paket investasi keamanan yang sesuai. Klik tombol di bawah untuk konsultasi langsung.")
    
    wa_num = "6282122190885" 
    data_produk = [
        {"Seg": "Mikro", "Pk": "Basic Guard", "Set": "2.5jt", "Bul": "750rb", "Feat": ["Monitoring Real-time", "Email Alert", "Limit 1rb Tx"]},
        {"Seg": "Menengah", "Pk": "Premium Shield", "Set": "7.5jt", "Bul": "2.5jt", "Feat": ["Advanced Fraud AI", "WhatsApp Alert", "Limit 5rb Tx"]},
        {"Seg": "Enterprise", "Pk": "Enterprise Vault", "Set": "50jt", "Bul": "8.5jt", "Feat": ["ERP Integration", "AI CCTV Object Detection", "Custom AI Model"]},
        {"Seg": "Corporate", "Pk": "Elite Managed", "Set": "85jt", "Bul": "15jt", "Feat": ["AI CCTV Face Recognition", "Managed Security Ops", "Advisory Pak Erwin"]}
    ]
    
    cols = st.columns(4)
    for i, p in enumerate(data_produk):
        with cols[i]:
