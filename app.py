import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. SETTING DASAR
st.set_page_config(page_title="V-Guard AI Dashboard", page_icon="🛡️", layout="wide")
wa_num = "6282122190885"

# 2. LOGIN SYSTEM
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
            else:
                st.error("❌ Salah.")
        except:
            st.error("⚠️ Set ADMIN_PASSWORD di Secrets!")
    st.stop()

# 3. SIDEBAR
page = st.sidebar.radio("Menu:", ["🏠 Home", "📊 Monitoring", "📦 Products", "👤 Profile"])

# --- HALAMAN 1: HOME ---
if page == "🏠 Home":
    st.title("🛡️ Welcome to V-Guard AI")
    st.info("**Vision**: Menjadi penyedia solusi keamanan finansial berbasis AI terdepan.")

# --- HALAMAN 2: MONITORING ---
elif page == "📊 Monitoring":
    st.header("📊 Real-time Monitoring")
    df = pd.DataFrame({'Status': ['Aman', 'Anomali'], 'Skor': [94, 6]})
    fig = px.pie(df, values='Skor', names='Status', hole=0.3)
    st.plotly_chart(fig, use_container_width=True)

# --- HALAMAN 3: PRODUCTS ---
elif page == "📦 Products":
    st.header("📦 Our Packages")
    pkgs = [
        {"N": "Mikro", "P": "Basic", "S": "2.5jt"},
        {"N": "Corporate", "P": "Elite", "S": "85jt"}
    ]
    cols = st.columns(2)
    for i, p in enumerate(pkgs):
        with cols[i]:
            st.warning(f"**{p['N']}**")
            st.subheader(p['P'])
            st.write(f"Setup: {p['S']}")
            st.link_button("👉 Pesan", f"https://wa.me/{wa_num}")

# --- HALAMAN 4: PROFILE (DESKRIPSI & FOTO TETAP) ---
elif page == "👤 Profile":
    st.header("Strategic Leadership")
    c1, c2 = st.columns([1, 2])
    with c1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
        else:
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=200)
    with c2:
        st.markdown("### Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        st.markdown("""
Bapak Erwin Sinaga adalah seorang *Senior Business Leader* visioner dengan rekam jejak impresif selama lebih dari 10 tahun di posisi krusial sebagai CEO dan CSO dalam industri perbankan serta manajemen aset. Pengalaman mendalam beliau dalam mengelola risiko operasional, memimpin transformasi digital, dan menjaga integritas aset bernilai tinggi menjadi pondasi kuat di balik berdirinya **V-Guard AI Systems**.

Dengan latar belakang keahlian strategis yang komprehensif, Pak Erwin berdedikasi penuh untuk mendemokratisasi akses terhadap teknologi keamanan finansial kelas dunia. Beliau melihat celah krusial antara prototipe teknologi dengan solusi *production-grade* yang benar-benar siap menjawab tantangan pasar di tahun 2026. Komitmen utama beliau adalah membangun solusi 'End-to-End Intermediary' yang cerdas, adaptif, dan memiliki daya jual tinggi (*high conversion*), yang tidak hanya melindungi UMKM lokal dari kehancuran finansial akibat *fraud*, tetapi juga memberikan kepastian keamanan di tingkat Korporat global.
""")
        st.link_button("📲 Chat WhatsApp", f"https://wa.me/{wa_num}", type="primary")

st.caption("© 2026 V-Guard AI Systems | Tangerang")
