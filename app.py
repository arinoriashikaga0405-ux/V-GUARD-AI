import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Ambil Password dari Secrets
try:
    # Memastikan sistem membaca ADMIN_PASSWORD dari menu Secrets
    CORRECT_PASSWORD = st.secrets["ADMIN_PASSWORD"]
except Exception:
    st.error("⚠️ Password belum terpasang di menu Secrets Streamlit!")
    st.stop()

# 2. Inisialisasi Status Login
if 'auth' not in st.session_state:
    st.session_state.auth = False

# 3. Tampilan Halaman Login
if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI SECURE LOGIN")
    st.subheader("Founder: Erwin Sinaga")
    
    # Input Password
    pwd_input = st.text_input("Masukkan Password Admin:", type="password")
    
    if st.button("Masuk Sekarang"):
        # Menghapus spasi yang mungkin tidak sengaja terketik user
        if pwd_input.strip() == CORRECT_PASSWORD.strip():
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("❌ Password Salah. Pastikan sama dengan di menu Secrets.")
    st.stop()

# 4. Tampilan Dashboard (Hanya muncul jika Login Sukses)
st.sidebar.title("V-Guard AI")
st.sidebar.write(f"👤 User: **Erwin Sinaga**")
if st.sidebar.button("Logout"):
    st.session_state.auth = False
    st.rerun()
# --- LANJUTKAN DARI BARIS 60 DENGAN KODE INI ---
st.write("---")
col_p1, col_p2 = st.columns([1, 2])

with col_p1:
    try:
        st.image("erwin.jpg", caption="Erwin Sinaga - Founder V-Guard AI", use_container_width=True)
    except:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)

with col_p2:
    st.markdown("""
    ### 👤 About the Founder
    **Erwin Sinaga** – *Senior Business Leader & CEO*
    
    Halo! Saya **Erwin Sinaga**, berdedikasi untuk memanfaatkan AI dalam menyelesaikan masalah nyata di bidang keuangan dan keamanan. Dengan pengalaman lebih dari **10 tahun** sebagai CEO & CSO di industri perbankan dan aset, saya mendirikan **V-Guard AI** untuk memberdayakan bisnis dengan solusi cerdas.
    """)

st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")d enable informed decision-making for businesses worldwide.")

# --- BARIS 85: PROFIL FOUNDER (ERWIN SINAGA) ---
st.write("---")
col_p1, col_p2 = st.columns([1, 2])

with col_p1:
    try:
        # Menggunakan file erwin.jpg yang sudah Bapak upload
        st.image("erwin.jpg", caption="Erwin Sinaga - Founder V-Guard AI", use_container_width=True)
    except:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)

with col_p2:
    st.markdown("""
    ### 👤 About the Founder
    **Erwin Sinaga** – *Senior Business Leader & CEO*
    
    Halo! Saya **Erwin Sinaga**, berdedikasi untuk memanfaatkan AI dalam menyelesaikan masalah nyata di bidang keuangan dan keamanan. Dengan pengalaman lebih dari **10 tahun** sebagai CEO & CSO di industri perbankan dan aset, saya mendirikan **V-Guard AI** untuk memberdayakan bisnis dengan solusi cerdas.
    """)

# --- BARIS TERAKHIR: FOOTER ---
st.write("---")
st.caption("© 2026 V-Guard AI Systems | Berdomisili di Tangerang, Indonesia")
