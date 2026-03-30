import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. KONFIGURASI DASAR
st.set_page_config(page_title="V-Guard AI", layout="wide")
wa = "6282122190885"

# 2. SISTEM LOGIN
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI SECURE GATE")
    pwd = st.text_input("Password:", type="password")
    if st.button("Masuk"):
        if pwd == st.secrets["ADMIN_PASSWORD"]:
            st.session_state.auth = True
            st.rerun()
        else: st.error("Password Salah!")
    st.stop()

# 3. MENU NAVIGASI
pilih = st.sidebar.radio("Navigasi:", ["Monitoring", "Paket", "Profil"])

# --- DASHBOARD ---
if pilih == "Monitoring":
    st.header("📊 Monitoring Real-time")
    df = pd.DataFrame({'Status':['Aman','Anomali'], 'Skor':[94, 6]})
    fig = px.pie(df, values='Skor', names='Status', hole=0.3)
    st.plotly_chart(fig, use_container_width=True)

# --- PAKET PRODUK (TULISAN MERAH DIHAPUS) ---
elif pilih == "Paket":
    st.header("📦 Produk V-Guard AI")
    c1, c2 = st.columns(2)
    with c1:
        st.info("**Paket Mikro**")
        st.write("Setup: Rp 2.5jt")
        st.link_button("Pesan via WA", f"https://wa.me/{wa}")
    with c2:
        st.info("**Paket Corporate**")
        st.write("Setup: Rp 85jt")
        st.link_button("Pesan via WA", f"https://wa.me/{wa}")

# --- PROFIL (FOTO & DESKRIPSI TETAP AMAN) ---
elif pilih == "Profil":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
        else: st.write("Founder Erwin Sinaga")
    with r:
        st.subheader("Erwin Sinaga")
        st.write("**Founder & Chief Executive Officer**")
        # Narasi profesional Bapak tanpa risiko SyntaxError
        txt = (
            "Bapak Erwin Sinaga adalah Senior Business Leader visioner dengan "
            "pengalaman 10+ tahun sebagai CEO/CSO di industri perbankan. "
            "Beliau membangun V-Guard AI untuk melindungi bisnis dari fraud "
            "melalui solusi AI intermediary yang cerdas dan adaptif. "
            "Fokus beliau adalah memberikan keamanan finansial kelas dunia "
            "bagi UMKM maupun Korporat di pasar global tahun 2026."
        )
        st.write(txt)
        st.link_button("📲 Hubungi Pak Erwin", f"https://wa.me/{wa}", type="primary")

# --- FOOTER ---
st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang")
