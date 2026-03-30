import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. SETUP
st.set_page_config(page_title="V-Guard AI", layout="wide")
wa_url = "https://wa.me/6282122190885"

# 2. LOGIN (Simple & Fast)
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI LOGIN")
    pwd = st.text_input("Password:", type="password")
    if st.button("Masuk"):
        if pwd == st.secrets["ADMIN_PASSWORD"]:
            st.session_state.auth = True
            st.rerun()
        else: st.error("Salah!")
    st.stop()

# 3. MENU
menu = st.sidebar.radio("Navigasi:", ["Dashboard", "Paket", "Profil"])

if menu == "Dashboard":
    st.header("📊 Monitoring")
    df = pd.DataFrame({'St':['Aman','Anomali'], 'Sk':[94, 6]})
    fig = px.pie(df, values='Sk', names='St', hole=0.3)
    st.plotly_chart(fig, use_container_width=True)

elif menu == "Paket":
    st.header("📦 Produk V-Guard")
    c1, c2 = st.columns(2)
    with c1:
        st.info("Paket Mikro")
        st.link_button("Chat WA", wa_url)
    with c2:
        st.info("Paket Corporate")
        st.link_button("Chat WA", wa_url)

elif menu == "Profil":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
        else: st.subheader("Founder Erwin Sinaga")
    with r:
        st.subheader("Erwin Sinaga")
        st.write("**Founder & CEO**")
        st.write("Bapak Erwin Sinaga adalah Senior Business Leader visioner dengan pengalaman 10+ tahun sebagai CEO/CSO di industri perbankan. Beliau membangun V-Guard AI untuk melindungi bisnis dari fraud melalui solusi AI yang cerdas.")
        # TOMBOL ASLI STREAMLIT (DIJAMIN BUKAN MERAH)
        st.link_button("📲 Hubungi via WhatsApp", wa_url, type="primary")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang")
