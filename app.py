import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. SETUP UTAMA
st.set_page_config(page_title="V-Guard AI", layout="wide")
wa_url = "https://wa.me/6282122190885"

# 2. LOGIN (SESUAIKAN PASSWORD DI SECRETS)
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI LOGIN")
    pwd = st.text_input("Password Admin:", type="password")
    if st.button("Masuk"):
        if pwd == st.secrets["ADMIN_PASSWORD"]:
            st.session_state.auth = True
            st.rerun()
        else: st.error("Password Salah!")
    st.stop()

# 3. NAVIGASI MENU
menu = st.sidebar.radio("Menu:", ["Dashboard", "Produk & Layanan", "Profil Founder"])

# --- HALAMAN DASHBOARD ---
if menu == "Dashboard":
    st.header("📊 Monitoring Real-time")
    df = pd.DataFrame({'Status':['Aman','Anomali'], 'Skor':[94, 6]})
    fig = px.pie(df, values='Skor', names='Status', hole=0.3)
    st.plotly_chart(fig, use_container_width=True)

# --- HALAMAN PRODUK (4 PAKET LENGKAP KEMBALI) ---
elif menu == "Produk & Layanan":
    st.header("📦 Our Products & Services Packages")
    st.write("Silakan pilih paket investasi keamanan yang sesuai.")
    
    pkgs = [
        {"N": "Mikro", "P": "Basic Guard", "S": "2.5jt"},
        {"N": "Menengah", "P": "Premium Shield", "S": "7.5jt"},
        {"N": "Enterprise", "P": "Enterprise Vault", "S": "50jt"},
        {"N": "Corporate", "P": "Elite Managed", "S": "85jt"}
    ]
    
    cols = st.columns(4)
    for i, p in enumerate(pkgs):
        with cols[i]:
            st.warning(f"**{p['N']}**")
            st.subheader(p['P'])
            st.write(f"Setup: Rp {p['S']}")
            st.link_button("👉 Pesan via WA", wa_url, use_container_width=True)

# --- HALAMAN PROFIL (NARASI LENGKAP & GARIS MERAH DIHAPUS TOTAL) ---
elif menu == "Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): 
            st.image("erwin.jpg", use_container_width=True)
        else: 
            st.subheader("Erwin Sinaga, Founder")
    with r:
        st.subheader("Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        
        # Narasi Profesional Lengkap 100+ Kata
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
        
        # TOMBOL ASLI (DIJAMIN BUKAN MERAH)
        st.link_button("📲 Hubungi via WhatsApp", wa_url, type="primary", use_container_width=True)

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
