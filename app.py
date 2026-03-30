import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. SETUP HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide")
wa_url = "https://wa.me/6282122190885"

# 2. SISTEM LOGIN
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

# 3. NAVIGASI SIDEBAR
menu = st.sidebar.radio("Navigasi Utama:", ["Dashboard", "Produk & Layanan", "Profil Founder"])

# --- HALAMAN 1: DASHBOARD ---
if menu == "Dashboard":
    st.header("📊 Real-time Security Monitoring")
    df = pd.DataFrame({'Status':['Aman','Anomali'], 'Skor':[94, 6]})
    fig = px.pie(df, values='Skor', names='Status', hole=0.3, color_discrete_sequence=['#00CC96', '#EF553B'])
    st.plotly_chart(fig, use_container_width=True)

# --- HALAMAN 2: PRODUK & LAYANAN ---
elif menu == "Produk & Layanan":
    st.title("📦 Our Security Solution Packages")
    st.write("Solusi perlindungan finansial berbasis AI untuk berbagai skala bisnis.")
    st.write("---")
    
    pkgs = [
        {
            "tier": "MIKRO", "name": "Basic Guard", 
            "setup": "2.5 Juta", "monthly": "500 Ribu",
            "benefits": ["Proteksi Fraud Dasar", "Laporan Mingguan", "Support Chat WA"]
        },
        {
            "tier": "MENENGAH", "name": "Premium Shield", 
            "setup": "7.5 Juta", "monthly": "1.5 Juta",
            "benefits": ["AI Anomaly Detection", "Dashboard Real-time", "Priority Support"]
        },
        {
            "tier": "ENTERPRISE", "name": "Enterprise Vault", 
            "setup": "50 Juta", "monthly": "5 Juta",
            "benefits": ["Full AI Integration", "Audit Keamanan Bulanan", "Dedicated Analyst"]
        },
        {
            "tier": "CORPORATE", "name": "Elite Managed", 
            "setup": "85 Juta", "monthly": "10 Juta",
            "benefits": ["End-to-End Intermediary", "Custom AI Training", "24/7 Response"]
        }
    ]
    
    cols = st.columns(4)
    for i, p in enumerate(pkgs):
        with cols[i]:
            st.subheader(f"🛡️ {p['tier']}")
            st.markdown(f"**{p['name']}**")
            st.write(f"Setup: **Rp {p['setup']}**")
            st.write(f"Bulanan: **Rp {p['monthly']}**")
            for b in p['benefits']:
                st.write(f"✅ {b}")
            st.link_button(f"Pesan {p['tier']}", wa_url, use_container_width=True)

# --- HALAMAN 3: PROFIL FOUNDER (TOMBOL WHATSAPP SUDAH DIHAPUS) ---
elif menu == "Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): 
            st.image("erwin.jpg", use_container_width=True)
        else: 
            st.subheader("Founder Erwin Sinaga")
    with r:
        st.subheader("Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        
        # Narasi Lengkap Bapak Erwin Sinaga
        deskripsi = (
            "Bapak Erwin Sinaga adalah seorang Senior Business Leader visioner dengan rekam jejak impresif "
            "selama lebih dari 10 tahun di posisi krusial sebagai CEO dan CSO dalam industri perbankan "
            "serta manajemen aset. Pengalaman mendalam beliau dalam mengelola risiko operasional, "
            "memimpin transformasi digital, dan menjaga integritas aset bernilai tinggi menjadi pondasi "
            "kuat di balik berdirinya V-Guard AI Systems. Pak Erwin berdedikasi penuh untuk "
            "mendemokratisasi akses terhadap teknologi keamanan finansial kelas dunia. "
            "Beliau melihat celah krusial antara prototipe teknologi dengan solusi production-grade "
            "yang benar-benar siap menjawab tantangan pasar di tahun 2026. "
            "Komitmen utama beliau adalah membangun solusi 'End-to-End Intermediary' yang cerdas, "
            "adaptif, dan memiliki daya jual tinggi (high conversion), guna melindungi UMKM lokal "
            "maupun Korporat global dari kehancuran finansial akibat fraud."
        )
        st.write(deskripsi)

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
