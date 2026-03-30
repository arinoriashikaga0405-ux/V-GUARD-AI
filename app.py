import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")
wa_url = "https://wa.me/6282122190885"

# 2. NAVIGASI SIDEBAR
# Password ditiadakan untuk menu umum (Produk & Profil)
menu = st.sidebar.radio("Pilih Menu:", ["🏠 Home & AI Services", "📦 Produk & Layanan", "👤 Profil Founder", "🔐 Admin Dashboard"])

# --- HALAMAN 1: HOME & AI SERVICES (FITUR PENDUKUNG LENGKAP) ---
if menu == "🏠 Home & AI Services":
    st.title("🛡️ V-Guard AI Systems")
    st.markdown("### *Next-Generation Financial Security & Fraud Prevention*")
    st.write("V-Guard AI hadir sebagai perantara (intermediary) cerdas antara teknologi keamanan tingkat tinggi dan kebutuhan bisnis Anda.")
    st.write("---")
    
    st.subheader("🚀 Fitur Unggulan Pendukung AI")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("**Real-time Anomaly Detection**")
        st.write("Mendeteksi pola transaksi mencurigakan dalam hitungan milidetik menggunakan algoritma pembelajaran mesin terbaru.")
    with c2:
        st.info("**End-to-End Intermediary**")
        st.write("Menghubungkan sistem internal Anda dengan jaringan intelijen fraud global secara otomatis.")
    with c3:
        st.info("**Predictive Risk Scoring**")
        st.write("Memberikan skor risiko pada setiap entitas baru sebelum mereka berinteraksi dengan ekosistem bisnis Anda.")

# --- HALAMAN 2: PRODUK & LAYANAN ---
elif menu == "📦 Produk & Layanan":
    st.title("📦 Paket Investasi Keamanan")
    st.write("Pilih perlindungan yang sesuai dengan skala operasional Anda.")
    
    pkgs = [
        {"T": "MIKRO", "N": "Basic Guard", "S": "2.5jt", "M": "500rb", "B": ["Fraud Dasar", "WA Support"]},
        {"T": "MENENGAH", "N": "Premium Shield", "S": "7.5jt", "M": "1.5jt", "B": ["Anomaly Detection", "Dashboard"]},
        {"T": "ENTERPRISE", "N": "Enterprise Vault", "S": "50jt", "M": "5jt", "B": ["Full Integration", "Audit Bulanan"]},
        {"T": "CORPORATE", "N": "Elite Managed", "S": "85jt", "M": "10jt", "B": ["24/7 Response", "Custom AI Training"]}
    ]
    
    cols = st.columns(4)
    for i, p in enumerate(pkgs):
        with cols[i]:
            st.subheader(f"🛡️ {p['T']}")
            st.write(f"Setup: **Rp {p['S']}**")
            st.write(f"Bulanan: **Rp {p['M']}**")
            for b in p['B']: st.write(f"✅ {b}")
            st.link_button(f"Pesan {p['T']}", wa_url, use_container_width=True)

# --- HALAMAN 3: PROFIL FOUNDER (BERSIH & PROFESIONAL) ---
elif menu == "👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
        else: st.subheader("Erwin Sinaga, Founder")
    with r:
        st.subheader("Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        st.write("""
        Bapak Erwin Sinaga adalah Senior Business Leader dengan pengalaman 10+ tahun sebagai CEO dan CSO di industri perbankan. 
        Beliau membangun V-Guard AI untuk mendemokratisasi akses teknologi keamanan finansial kelas dunia bagi UMKM maupun Korporat global.
        """)

# --- HALAMAN 4: ADMIN DASHBOARD (MENGGUNAKAN PASSWORD) ---
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
            
        st.subheader("📊 Laporan Keamanan Internal")
        df = pd.DataFrame({'Status':['Aman','Anomali'], 'Skor':[94, 6]})
        fig = px.pie(df, values='Skor', names='Status', hole=0.4, color_discrete_sequence=['#00CC96', '#EF553B'])
        st.plotly_chart(fig, use_container_width=True)

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
