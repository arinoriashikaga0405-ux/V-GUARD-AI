import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. KONFIGURASI UTAMA
st.set_page_config(page_title="V-Guard AI", layout="wide")
wa_url = "https://wa.me/6282122190885"

# 2. LOGIN SISTEM
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI LOGIN")
    pwd = st.text_input("Password Admin:", type="password")
    if st.button("Masuk"):
        if pwd == st.secrets["ADMIN_PASSWORD"]:
            st.session_state.auth = True
            st.rerun()
        else: st.error("❌ Password Salah.")
    st.stop()

# 3. NAVIGASI
menu = st.sidebar.radio("Navigasi Menu:", ["Dashboard", "Produk", "Profil Founder"])

# --- HALAMAN DASHBOARD ---
if menu == "Dashboard":
    st.header("📊 Monitoring Real-time")
    df = pd.DataFrame({'Status':['Aman','Anomali'], 'Skor':[94, 6]})
    fig = px.pie(df, values='Skor', names='Status', hole=0.3)
    st.plotly_chart(fig, use_container_width=True)

# --- HALAMAN PRODUK ---
elif menu == "Produk":
    st.header("📦 Produk & Layanan V-Guard AI")
    c1, c2 = st.columns(2)
    with c1:
        st.info("**Paket Mikro**")
        st.write("Setup: Rp 2.5jt")
        st.link_button("Hubungi WhatsApp", wa_url, use_container_width=True)
    with c2:
        st.info("**Paket Corporate**")
        st.write("Setup: Rp 85jt")
        st.link_button("Hubungi WhatsApp", wa_url, use_container_width=True)

# --- HALAMAN PROFIL (KATA-KATA LENGKAP & NO RED BOX) ---
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
        
        # KATA-KATA LENGKAP SESUAI PROFIL BAPAK
        deskripsi_lengkap = (
            "Bapak Erwin Sinaga adalah seorang Senior Business Leader visioner dengan rekam jejak impresif "
            "selama lebih dari 10 tahun di posisi krusial sebagai CEO dan CSO dalam industri perbankan "
            "serta manajemen aset. Pengalaman mendalam beliau dalam mengelola risiko operasional, "
            "memimpin transformasi digital, dan menjaga integritas aset bernilai tinggi menjadi pondasi "
            "kuat di balik berdirinya V-Guard AI Systems. Dengan latar belakang keahlian strategis yang "
            "komprehensif, Pak Erwin berdedikasi penuh untuk mendemokratisasi akses terhadap teknologi "
            "keamanan finansial kelas dunia. Beliau melihat celah krusial antara prototipe teknologi dengan "
            "solusi production-grade yang benar-benar siap menjawab tantangan pasar di tahun 2026. "
            "Komitmen utama beliau adalah membangun solusi 'End-to-End Intermediary' yang cerdas, adaptif, "
            "dan memiliki daya jual tinggi (high conversion), yang tidak hanya melindungi UMKM lokal dari "
            "kehancuran finansial akibat fraud, tetapi juga memberikan kepastian keamanan di tingkat Korporat global."
        )
        st.write(deskripsi_lengkap)
        
        # TOMBOL WHATSAPP ASLI (WARNA BIRU/HITAM STANDAR, BUKAN MERAH)
        st.link_button("📲 Hubungi Pak Erwin via WhatsApp", wa_url, type="primary", use_container_width=True)

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
