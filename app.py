import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. SETUP
st.set_page_config(page_title="V-Guard AI", layout="wide")
wa = "6282122190885"

# 2. LOGIN
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI SECURE GATE")
    pwd = st.text_input("Password:", type="password")
    if st.button("Masuk"):
        if pwd == st.secrets["ADMIN_PASSWORD"]:
            st.session_state.auth = True
            st.rerun()
        else: st.error("Salah!")
    st.stop()

# 3. MENU
page = st.sidebar.radio("Menu:", ["Monitoring", "Paket", "Profil"])

if page == "Monitoring":
    st.header("📊 Monitoring")
    df = pd.DataFrame({'St':['Aman','Anomali'], 'Sk':[94, 6]})
    fig = px.pie(df, values='Sk', names='St', hole=0.3)
    st.plotly_chart(fig, use_container_width=True)

elif page == "Paket":
    st.header("📦 Produk V-Guard")
    c1, c2 = st.columns(2)
    with c1:
        st.info("Paket Mikro - Rp 2.5jt")
        st.link_button("Pesan Mikro", f"https://wa.me/{wa}")
    with c2:
        st.info("Paket Corporate - Rp 85jt")
        st.link_button("Pesan Corporate", f"https://wa.me/{wa}")

elif page == "Profil":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
        else: st.write("Founder Erwin Sinaga")
    with r:
        st.subheader("Erwin Sinaga")
        st.write("**Founder & CEO**")
        st.write("Bapak Erwin Sinaga adalah Senior Business Leader dengan pengalaman 10+ tahun sebagai CEO/CSO di perbankan. Beliau membangun V-Guard AI untuk melindungi UMKM dan Korporat dari fraud global melalui solusi intermediary yang cerdas dan adaptif.")
        st.link_button("📲 Chat WhatsApp", f"https://wa.me/{wa}")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang")
