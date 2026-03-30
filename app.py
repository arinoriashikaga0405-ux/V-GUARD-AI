import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI", page_icon="🛡️")

# 2. AMBIL PASSWORD DARI SECRETS
try:
    CORRECT_PASSWORD = st.secrets["ADMIN_PASSWORD"]
except Exception:
    st.error("⚠️ Password belum terpasang di menu Secrets Streamlit!")
    st.stop()

# 3. STATUS LOGIN
if 'auth' not in st.session_state:
    st.session_state.auth = False

# 4. HALAMAN LOGIN
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

# 5. SIDEBAR & LOGOUT
st.sidebar.title("V-Guard AI")
st.sidebar.write("👤 User: **Erwin Sinaga**")
if st.sidebar.button("Logout"):
    st.session_state.auth = False
    st.rerun()

# 6. DASHBOARD UTAMA (GRAFIK)
st.header("📊 Financial Integrity Dashboard")
df = pd.DataFrame({'Kategori': ['Aman', 'Anomali'], 'Skor': [94, 6]})
fig = px.pie(df, values='Skor', names='Kategori', title="Ringkasan Risiko Real-time", hole=0.3)
st.plotly_chart(fig)

# 7. FILOSOFI (OUR PHILOSOPHY)
st.write("---")
st.header("🛡️ Our Philosophy")
st.write("At V-Guard AI, our philosophy is simple yet profound: **Empowering Businesses Through Intelligent Protection**.")
st.write("We believe that every business deserves protection against financial threats and operational inefficiencies. Our mission is to harness the power of Artificial Intelligence to provide proactive, reliable, and accessible solutions that safeguard assets, optimize processes, and foster sustainable growth.")
st.write("In a world increasingly driven by data, we aim to make cutting-edge AI technology accessible to all, ensuring that businesses of all sizes can thrive in the digital age.")

# 8. VISI & MISI
st.write("---")
st.subheader("🎯 Vision & Mission")
st.markdown("- **Vision**: To become the leading provider of AI-powered financial security solutions globally.")
st.markdown("- **Mission**: To develop innovative AI technologies that anticipate risks, automate defenses, and enable informed decision-making for businesses worldwide.")

# 9. PROFIL FOUNDER
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

# 10. FOOTER
st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
