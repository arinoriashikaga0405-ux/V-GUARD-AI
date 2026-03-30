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
    pwd = st.text_input("Password Admin:", type="password")
    if st.button("Login"):
        try:
            if pwd.strip() == st.secrets["ADMIN_PASSWORD"].strip():
                st.session_state.auth = True
                st.rerun()
            else: st.error("❌ Salah.")
        except: st.error("⚠️ Set ADMIN_PASSWORD di Secrets!")
    st.stop()

# 3. NAVIGASI
page = st.sidebar.radio("Menu:", ["🏠 Home", "📊 Monitoring", "📦 Products", "👤 Profile"])

if page == "🏠 Home":
    st.title("🛡️ Welcome to V-Guard AI")
    st.info("**Vision**: Menjadi penyedia solusi keamanan finansial berbasis AI terdepan.")

elif page == "📊 Monitoring":
    st.header("📊 Real-time Monitoring")
    df = pd.DataFrame({'Status': ['Aman', 'Anomali'], 'Skor': [94, 6]})
    fig = px.pie(df, values='Skor', names='Status', hole=0.3)
    st.plotly_chart(fig, use_container_width=True)

elif page == "📦 Products":
    st.header("📦 Our Packages")
    cols = st.columns(2)
    with cols[0]:
        st.warning("**Mikro**")
        st.write("Setup: 2.5jt")
        st.link_button("👉 Pesan", f"https://wa.me/{wa_num}")
    with cols[1]:
        st.warning("**Corporate**")
        st.write("Setup: 85jt")
        st.link_button("👉 Pesan", f"https://wa.me/{wa_num}")

elif page == "👤 Profile":
    st.header("Strategic Leadership")
    c1, c2 = st.columns([1, 2])
    with c1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
        else:
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=200)
    with c2:
        st.subheader("Erwin Sinaga")
        st.write("**Founder & Chief Executive Officer**")
        # Deskripsi menggunakan string biasa agar tidak kena SyntaxError lagi
        desc = "Bapak Erwin Sinaga adalah seorang Senior Business Leader visioner dengan rekam jejak impresif selama lebih dari 10 tahun di posisi krusial sebagai CEO dan CSO dalam industri perbankan serta manajemen aset. Pengalaman mendalam beliau dalam mengelola risiko operasional, memimpin transformasi digital, dan menjaga integritas aset bernilai tinggi menjadi pondasi kuat di balik berdirinya V-Guard AI Systems. Dengan latar belakang keahlian strategis yang komprehensif, Pak Erwin berdedikasi penuh untuk mendemokratisasi akses terhadap teknologi keamanan finansial kelas dunia. Beliau melihat celah krusial antara prototipe teknologi dengan solusi production-grade yang benar-benar siap menjawab tantangan pasar di tahun 2026. Komitmen utama beliau adalah membangun solusi End-to-End Intermediary yang cerdas, adaptif, dan memiliki daya jual tinggi (high conversion), yang tidak hanya melindungi UMKM lokal dari kehancuran finansial akibat fraud, tetapi juga memberikan kepastian keamanan di tingkat Korporat global."
        st.write(desc)
        st.link_button("📲 Hubungi via WhatsApp", f"https://wa.me/{wa_num}", type="primary")

st.caption("© 2026 V-Guard AI Systems
