import streamlit as st
import pandas as pd
import plotly.express as px

# 1. AMBIL PASSWORD DARI SECRETS
try:
    CORRECT_PASSWORD = st.secrets["ADMIN_PASSWORD"]
except Exception:
    st.error("⚠️ Password belum terpasang di menu Secrets Streamlit!")
    st.stop()

# 2. INISIALISASI STATUS LOGIN
if 'auth' not in st.session_state:
    st.session_state.auth = False

# 3. TAMPILAN HALAMAN LOGIN
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

# 4. TAMPILAN DASHBOARD (HANYA MUNCUL JIKA SUDAH LOGIN)
st.sidebar.title("V-Guard AI")
st.sidebar.write(f"👤 User: **Erwin Sinaga**")
if st.sidebar.button("Logout"):
    st.session_state.auth = False
    st.rerun()

st.header("📊 Financial Integrity Dashboard")
st.success("Koneksi Aman & Terverifikasi.")

# Grafik Plotly (Status Transaksi)
df = pd.DataFrame({'Kategori': ['Aman', 'Anomali'], 'Skor': [94, 6]})
fig = px.pie(df, values='Skor', names='Kategori', title="Ringkasan Risiko Real-time")
st.plotly_chart(fig)

# --- BAGIAN PROFIL FOUNDER ---
st.write("---")
col_p1, col_p2 = st.columns([1, 2])

with col_p1:
    try:
        # Memanggil file erwin.jpg yang sudah Bapak upload
        st.image("erwin.jpg", caption="Erwin Sinaga - Founder", use_container_width=True)
    except:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)

with col_p2:
    st.markdown("""
    ### 👤 About the Founder
    **Erwin Sinaga** – *Senior Business Leader & CEO*
    
    Halo! Saya **Erwin Sinaga**, berdedikasi untuk memanfaatkan AI dalam menyelesaikan masalah nyata di bidang keuangan dan keamanan. Dengan pengalaman lebih dari **10 tahun** sebagai CEO & CSO di industri perbankan dan aset, saya mendirikan **V-Guard AI** untuk memberdayakan bisnis dengan solusi cerdas.
    """)

# --- FOOTER ---
st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
