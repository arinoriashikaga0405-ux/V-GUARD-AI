import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. SETUP DASAR
st.set_page_config(page_title="V-Guard AI", layout="wide")
wa_url = "https://wa.me/6282122190885"

# 2. LOGIN (SESUAIKAN DENGAN SECRETS BAPAK)
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
menu = st.sidebar.radio("Menu:", ["Dashboard", "Produk", "Profil Founder"])

if menu == "Dashboard":
    st.header("📊 Monitoring Real-time")
    df = pd.DataFrame({'Status':['Aman','Anomali'], 'Skor':[94, 6]})
    fig = px.pie(df, values='Skor', names='Status', hole=0.3)
    st.plotly_chart(fig, use_container_width=True)

elif menu == "Produk":
    st.header("📦 Produk & Layanan")
    c1, c2 = st.columns(2)
    with c1:
        st.info("**Paket Mikro**")
        st.link_button("Hubungi via WhatsApp", wa_url)
    with c2:
        st.info("**Paket Corporate**")
        st.link_button("Hubungi via WhatsApp", wa_url)

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
        
        # Narasi profesional Bapak Erwin Sinaga
        deskripsi = (
            "Bapak Erwin Sinaga adalah seorang Senior Business Leader visioner dengan rekam jejak impresif "
            "selama lebih dari 10 tahun di posisi CEO dan CSO dalam industri perbankan serta manajemen aset. "
            "Pengalaman mendalam beliau dalam mengelola risiko operasional dan memimpin transformasi digital "
            "menjadi pondasi kuat V-Guard AI Systems. Pak Erwin berdedikasi mendemokratisasi akses terhadap "
            "teknologi keamanan finansial kelas dunia untuk melindungi UMKM dan Korporat dari fraud global."
        )
        st.write(deskripsi)
        
        # TOMBOL STANDAR (DIJAMIN BUKAN MERAH)
        st.link_button("📲 Hubungi via WhatsApp", wa_url, type="primary")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
