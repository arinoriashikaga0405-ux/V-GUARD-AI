import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI
st.set_page_config(page_title="V-Guard AI", page_icon="🛡️", layout="wide")

# 2. LOGIN
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI LOGIN")
    pwd_input = st.text_input("Password Admin:", type="password")
    if st.button("Masuk"):
        try:
            if pwd_input.strip() == st.secrets["ADMIN_PASSWORD"].strip():
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Salah!")
        except:
            st.error("Setting Secrets di Streamlit Cloud dulu!")
    st.stop()

# 3. NAVIGASI
page = st.sidebar.radio("Menu:", ["Home", "Dashboard", "Packages", "About"])
if st.sidebar.button("Logout"):
    st.session_state.auth = False
    st.rerun()

# --- HALAMAN 1: HOME ---
if page == "Home":
    st.title("🛡️ V-Guard AI")
    st.subheader("Empowering Businesses Through Intelligent Protection")
    st.info("Vision: Leading AI-powered financial security globally.")

# --- HALAMAN 2: DASHBOARD ---
elif page == "Dashboard":
    st.header("📊 Monitoring")
    df = pd.DataFrame({'Cat': ['Safe', 'Risk'], 'Val': [94, 6]})
    fig = px.pie(df, values='Val', names='Cat', hole=0.3)
    st.plotly_chart(fig)

# --- HALAMAN 3: PACKAGES ---
elif page == "Packages":
    st.header("📦 Product Packages")
    wa = "6282122190885"
    pkgs = [
        {"N": "Mikro", "S": "2.5jt", "B": "750rb", "F": "Basic AI"},
        {"N": "Menengah", "S": "7.5jt", "B": "2.5jt", "F": "WA Alert"},
        {"N": "Enterprise", "S": "50jt", "B": "8.5jt", "F": "CCTV AI"},
        {"N": "Corporate", "S": "85jt", "B": "15jt", "F": "CSO Advisory"}
    ]
    cols = st.columns(4)
    for i, p in enumerate(pkgs):
        with cols[i]:
            st.info(p['N'])
            st.write(f"Setup: {p['S']}")
            st.write(f"Monthly: {p['B']}")
            st.write(f"Feature: {p['F']}")
            url = f"https://wa.me/{wa}?text=Minat%20Paket%20{p['N']}"
            st.link_button(f"Pesan {p['N']}", url, use_container_width=True)

# --- HALAMAN 4: ABOUT ---
elif page == "About":
    st.header("👤 Founder")
    st.write("**Erwin Sinaga** - Senior Business Leader")
    st.write("10+ years exp as CEO & CSO in Banking/Asset industry.")

st.write("---")
st.caption("© 2026 V-Guard AI | Tangerang")
