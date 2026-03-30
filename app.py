import streamlit as st
import pandas as pd
import plotly.express as px

# 1. AMBIL PASSWORD DARI SECRETS
try:
    CORRECT_PASSWORD = st.secrets["ADMIN_PASSWORD"]
except Exception:
    st.error("⚠️ Password belum terpasang di menu Secrets Streamlit!")
    st.stop()

# 2. STATUS LOGIN
if 'auth' not in st.session_state:
    st.session_state.auth = False

# 3. HALAMAN LOGIN
if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI SECURE LOGIN")
    st.subheader("Founder: Erwin Sinaga")
    pwd_input = st.text_input("Masukkan Password Admin:", type="password")
    if st.button("Masuk Sekarang"):
        if pwd_input.strip() == CORRECT_PASSWORD.strip():
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("❌ Password Salah.")
    st.stop()

# 4. DASHBOARD UTAMA
st.sidebar.title("V-Guard AI")
st.sidebar.write("👤 User: **Erwin Sinaga**")
if st.sidebar.button("Logout"):
    st.session_state.auth = False
    st.rerun()

st.header("📊 Financial Integrity Dashboard")
st.success("Koneksi Aman & Terverifikasi.")

# GRAFIK
df = pd.DataFrame({'Kategori': ['Aman', 'Anomali'], 'Skor': [94, 6]})
fig = px.pie(df, values='Skor', names='Kategori', title="Ringkasan Risiko Real-time")
st.plotly_chart(fig)

# 5. VISI & MISI
st.write("---")
st.subheader("🎯 Vision & Mission")
col_v, col_m = st.columns(2)
with col_v:
    st.info("**Vision**: To become the leading provider of AI-powered financial security solutions globally.")
with col_m:
    st.info("**Mission**: To develop innovative AI technologies that anticipate risks and automate defenses.")

# 6. PROFIL FOUNDER (VERSI AMAN TANPA TANDA KUTIP TIGA YANG ERROR)
st.write("---")
col_p1, col_p2 = st.columns([1, 2])
with col_p1:
    try:
        st.image("erwin.jpg", caption="Erwin Sinaga", use_container_width=True)
    except:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)

with col_p2:
    st.markdown("### 👤 About the Founder")
    st.write("**Erwin Sinaga** – *Senior Business Leader & CEO*")
    st.write("Berdedikasi memanfaatkan AI untuk keamanan finansial. Dengan pengalaman 10+ tahun di perbankan dan aset sebagai CEO & CSO, saya mendirikan V-Guard AI untuk solusi cerdas UMKM.")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
