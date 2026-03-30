import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. SETUP AWAL
st.set_page_config(page_title="V-Guard AI", layout="wide")
wa_num = "6282122190885"

# 2. LOGIN (PASTIKAN PASSWORD SESUAI SECRETS)
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI SECURE GATE")
    pwd = st.text_input("Password Admin:", type="password")
    if st.button("Masuk"):
        try:
            if pwd.strip() == st.secrets["ADMIN_PASSWORD"].strip():
                st.session_state.auth = True
                st.rerun()
            else: st.error("❌ Password Salah.")
        except: st.error("⚠️ Atur Password di Secrets!")
    st.stop()

# 3. NAVIGASI
menu = ["📊 Dashboard", "📦 Paket", "👤 Profil"]
page = st.sidebar.radio("Navigasi:", menu)

# --- HALAMAN DASHBOARD ---
if page == "📊 Dashboard":
    st.header("📊 Monitoring Real-time")
    data = {'Status':['Aman','Anomali'], 'Skor':[94, 6]}
    df = pd.DataFrame(data)
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

# --- HALAMAN PROFIL (TULISAN MERAH SUDAH DIHAPUS TOTAL) ---
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
        # Narasi dipecah agar tidak panjang ke samping (Anti-Error)
        desc = (
            "Bapak Erwin Sinaga adalah seorang Senior Business Leader visioner "
            "dengan rekam jejak impresif selama lebih dari 10 tahun di posisi "
            "CEO dan CSO dalam industri perbankan serta manajemen aset. "
            "Pengalaman beliau dalam mengelola risiko operasional dan "
            "transformasi digital menjadi pondasi kuat V-Guard AI Systems. "
            "Beliau berdedikasi mendemokratisasi akses teknologi keamanan "
            "finansial kelas dunia untuk menjawab tantangan pasar tahun 2026. "
            "Komitmen utama beliau adalah membangun solusi End-to-End "
            "Intermediary yang cerdas, adaptif, dan memiliki daya jual tinggi, "
            "guna melindungi UMKM dan Korporat dari risiko fraud global."
        )
        st.write(desc)
        st.link_button("📲 Chat Pak Erwin", f"https://wa.me/{wa_num}", type="primary")

# --- FOOTER ---
st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang")
