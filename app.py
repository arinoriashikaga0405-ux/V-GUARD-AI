import streamlit as st
import pandas as pd
import numpy as np

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Founder Erwin", page_icon="🛡️", layout="wide")

# --- 2. CSS CUSTOM ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stInfo, .stWarning, .stError, .stSuccess { border-radius: 10px; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGASI ---
with st.sidebar:
    try:
        st.image("erwin.jpg", width=200, caption="Erwin - Founder & CEO")
    except:
        st.write("👤 [Foto Erwin Belum Diupload]")
    st.title("🛡️ VGUARD AI")
    st.write("---")
    menu = st.radio("Navigasi Sistem", ["Beranda & Profil CEO", "Dashboard Performa", "AI Scanner Audit"])

# --- 4. LOGIKA MENU ---
if menu == "Beranda & Profil CEO":
    st.title("🛡️ VGUARD AI Systems")
    st.info('👉 "Digitizing Trust, Eliminating Leakage"')
    
    st.write("---")
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("erwin.jpg", width=250)
        except:
            st.error("Foto erwin.jpg tidak ditemukan.")
    with col2:
        st.write("#### PROFIL FOUNDER & CEO")
        st.write("Saya **Erwin**, Founder dan CEO VGUARD AI Systems. Fokus kami adalah mengamankan aset Anda.")
        st.write("#### FILOSOFI")
        st.write("Menghadirkan teknologi AI masa depan untuk mencegah kerugian secara sistemik.")

    st.write("---")
    st.write("### Pilih Solusi Keamanan Anda:")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.info("### V-START\n**Rp 2,5 Jt**\nAudit Harian")
    with c2:
        st.warning("### V-GROW\n**Rp 5 Jt**\nFraud Detection")
    with c3:
        st.error("### V-PRIME\n**Rp 10 Jt**\nMulti-Cabang")
    with c4:
        st.success("### V-CUSTOM\n**Negotiable**\nTailor-Made")

elif menu == "Dashboard Performa":
    st.title("📊 Dashboard Performa")
    st.line_chart(pd.DataFrame(np.random.randn(20, 2), columns=['Retail', 'Gudang']))

elif menu == "AI Scanner Audit":
    st.title("🔍 AI Scanner Audit")
    if st.button("Jalankan Analisis AI"):
        st.info("Sedang menganalisis data melalui VGUARD Engine...")

st.write("---")
st.caption("© 2026 VGUARD AI Systems | Tangerang, Indonesia")
