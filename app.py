import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide")
wa_url = "https://wa.me/6282122190885"

# 2. LOGIN SISTEM
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI SECURE GATE")
    pwd = st.text_input("Password Admin:", type="password")
    if st.button("Masuk"):
        if pwd == st.secrets["ADMIN_PASSWORD"]:
            st.session_state.auth = True
            st.rerun()
        else: st.error("Password Salah!")
    st.stop()

# 3. NAVIGASI
menu = st.sidebar.radio("Menu Utama:", ["Dashboard", "Produk & Layanan", "Profil Founder"])

if menu == "Dashboard":
    st.header("📊 Real-time Security Monitoring")
    df = pd.DataFrame({'Status':['Aman','Anomali'], 'Skor':[94, 6]})
    fig = px.pie(df, values='Skor', names='Status', hole=0.3, color_discrete_sequence=['#00CC96', '#EF553B'])
    st.plotly_chart(fig, use_container_width=True)

# --- HALAMAN PRODUK & LAYANAN (VERSI PERCANTIK) ---
elif menu == "Produk & Layanan":
    st.title("📦 Our Security Solution Packages")
    st.write("Solusi perlindungan finansial berbasis AI yang disesuaikan dengan skala bisnis Anda.")
    st.write("---")
    
    # Data Paket
    pkgs = [
        {
            "tier": "MIKRO",
            "name": "Basic Guard",
            "setup": "2.5 Juta",
            "monthly": "500 Ribu",
            "benefits": ["Proteksi Fraud Dasar", "Laporan Mingguan", "Support Chat WA"]
        },
        {
            "tier": "MENENGAH",
            "name": "Premium Shield",
            "setup": "7.5 Juta",
            "monthly": "1.5 Juta",
            "benefits": ["AI Anomaly Detection", "Dashboard Real-time", "Priority Support"]
        },
        {
            "tier": "ENTERPRISE",
            "name": "Enterprise Vault",
            "setup": "50 Juta",
            "monthly": "5 Juta",
            "benefits": ["Full AI Integration", "Audit Keamanan Bulanan", "Dedicated Analyst"]
        },
        {
            "tier": "CORPORATE",
            "name": "Elite Managed",
            "setup": "85 Juta",
            "monthly": "10 Juta",
            "benefits": ["End-to-End Intermediary", "Custom AI Training", "24/7 On-site Response"]
        }
    ]
    
    cols = st.columns(4)
    
    for i, p in enumerate(pkgs):
        with cols[i]:
            # Bagian Atas Kartu
            st.subheader(f"🛡️ {p['tier']}")
            st.markdown(f"### {p['name']}")
            st.write("---")
            
            # Detail Harga
            st.write("**Biaya Pemasangan:**")
            st.success(f"Rp {p['setup']}")
            st.write("**Biaya Bulanan:**")
            st.info(f"Rp {p['monthly']}")
            
            # Manfaat
            st.write("**Manfaat & Fitur:**")
            for b in p['benefits']:
                st.write(f"✅ {b}")
