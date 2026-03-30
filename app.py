import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. SETUP & LOGIN
st.set_page_config(page_title="V-Guard AI", layout="wide")
wa_num = "6282122190885"

if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI SECURE GATE")
    pwd = st.text_input("Password Admin:", type="password")
    if st.button("Authorize Access"):
        try:
            if pwd.strip() == st.secrets["ADMIN_PASSWORD"].strip():
                st.session_state.auth = True
                st.rerun()
            else: st.error("❌ Salah.")
        except: st.error("⚠️ Set ADMIN_PASSWORD di Secrets!")
    st.stop()

# 2. MENU
page = st.sidebar.radio("Navigasi:", ["📊 Dashboard", "📦 Paket", "👤 Profil"])

# --- HALAMAN DASHBOARD ---
if page == "📊 Dashboard":
    st.header("📊 Monitoring Real-time")
    df = pd.DataFrame({'Status':['Aman','Anomali'], 'Skor':[94, 6]})
    fig = px.pie(df, values='Skor', names='Status', hole=0.3)
    st.plotly_chart(fig, use_container_width=True)

# --- HALAMAN PAKET ---
elif page == "📦 Paket":
    st.header("📦 Produk V-Guard AI")
    c1, c2 = st.columns(2)
    with c1:
        st.warning("**Paket Mikro**")
        st.write("Setup: Rp 2.5jt")
        st.link_button("👉 Pesan", f"https://wa.me/{wa_num}")
    with c2:
        st.warning("**Paket Corporate**")
        st.write("Setup: Rp 85jt")
        st.link_button("👉 Pesan", f"https://wa.me/{wa_num}")

# --- HALAMAN PROFIL (100% BERSIH DARI TULISAN MERAH) ---
elif page == "👤 Profil":
    st.header("Strategic Leadership")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
        else:
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=200)
    with col2:
        st.subheader("Erwin Sinaga")
        st.write("**Founder & Chief Executive Officer**")
        # Narasi profesional Bapak (Tetap dijaga 100+ kata)
        desc = (
            "Bapak Erwin Sinaga adalah seorang Senior Business Leader visioner dengan rekam "
            "jejak impresif selama lebih dari 10 tahun di posisi krusial sebagai CEO dan CSO "
            "dalam industri perbankan serta manajemen aset. Pengalaman mendalam beliau dalam "
            "mengelola risiko operasional, memimpin transformasi digital, dan menjaga integritas "
            "aset bernilai tinggi menjadi pondasi kuat di balik berdirinya V-Guard AI Systems. "
            "Dengan latar belakang keahlian strategis yang komprehensif, Pak Erwin berdedikasi "
            "penuh untuk mendemokratisasi akses terhadap teknologi keamanan finansial kelas dunia. "
            "Beliau melihat celah krusial antara prototipe teknologi dengan solusi production-grade "
            "yang benar-benar siap menjawab tantangan pasar di tahun 2026. Komitmen utama beliau "
            "adalah membangun solusi End-to-End Intermediary yang cerdas, adaptif, dan memiliki "
            "daya jual tinggi (high conversion), yang tidak hanya melindungi UMKM lokal dari "
            "kehancuran finansial akibat fraud, tetapi juga memberikan kepastian keamanan di tingkat Korporat global."
        )
        st.write(desc)
        st.link_button("📲 Chat WhatsApp", f"https://wa.me/{wa_num}", type="primary")

#
