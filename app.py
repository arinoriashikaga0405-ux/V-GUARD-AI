import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")
wa_url = "https://wa.me/6282122190885"

# 2. DATA PAKET (DYNAMIC PACKAGES)
pkgs = [
    {"T": "MIKRO", "N": "Basic Guard", "S": "2.5jt", "M": "500rb", "B": ["Fraud Dasar", "WA Support"]},
    {"T": "MENENGAH", "N": "Premium Shield", "S": "7.5jt", "M": "1.5jt", "B": ["Anomaly Detection", "Dashboard"]},
    {"T": "ENTERPRISE", "N": "Enterprise Vault", "S": "50jt", "M": "5jt", "B": ["Full Integration", "Audit Bulanan"]},
    {"T": "CORPORATE", "N": "Elite Managed", "S": "85jt", "M": "10jt", "B": ["24/7 Response", "Custom AI Training"]}
]

# 3. NAVIGASI SIDEBAR
menu = st.sidebar.radio("Pilih Menu:", ["🏠 Home & AI Services", "📦 Produk & Layanan", "👤 Profil Founder", "🔐 Admin Dashboard"])

# --- HALAMAN 1: HOME ---
if menu == "🏠 Home & AI Services":
    st.title("🛡️ V-Guard AI Systems")
    st.markdown("### *Next-Generation Financial Security*")
    st.write("Solusi intermediary cerdas untuk keamanan bisnis Anda.")
    st.write("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("**Real-time Detection**")
        st.write("Mendeteksi pola mencurigakan dalam milidetik.")
    with c2:
        st.info("**End-to-End Link**")
        st.write("Koneksi otomatis ke jaringan fraud global.")
    with c3:
        st.info("**Risk Scoring**")
        st.write("Penilaian risiko prediktif untuk tiap entitas.")

# --- HALAMAN 2: PRODUK (DYNAMIC VIEW) ---
elif menu == "📦 Produk & Layanan":
    st.title("📦 Paket Investasi Keamanan")
    cols = st.columns(4)
    for i, p in enumerate(pkgs):
        with cols[i]:
            st.subheader(f"🛡️ {p['T']}")
            st.write(f"Setup: **Rp {p['S']}**")
            st.write(f"Bulanan: **Rp {p['M']}**")
            for b in p['B']: st.write(f"✅ {b}")
            st.link_button(f"Pesan {p['T']}", wa_url, use_container_width=True)

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

# --- HALAMAN 4: ADMIN DASHBOARD (MONITORING & INPUT DATA) ---
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
        
        st.write("---")
        st.subheader("📊 Monitoring Real-time (Control Panel)")
        
        # FITUR INPUT DATA UNTUK ADMIN
        col_in1, col_in2 = st.columns(2)
        with col_in1:
            val_aman = st.number_input("Jumlah Data Aman:", value=94)
        with col_in2:
            val_anomali = st.number_input("Jumlah Data Anomali:", value=6)
            
        # GRAFIK DINAMIS BERDASARKAN INPUT
        df = pd.DataFrame({'Status':['Aman','Anomali'], 'Skor':[val_aman, val_anomali]})
        fig = px.pie(df, values='Skor', names='Status', hole=0.4, 
                     color_discrete_sequence=['#00CC96', '#EF553B'])
        st.plotly_chart(fig, use_container_width=True)

        st.write("---")
        st.subheader("📦 Monitoring Dynamic Packages")
        st.table(pd.DataFrame(pkgs).drop(columns=['B'])) # Menampilkan ringkasan paket

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
