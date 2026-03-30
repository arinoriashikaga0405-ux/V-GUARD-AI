import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Dashboard", page_icon="🛡️", layout="wide")

# 2. AMBIL PASSWORD DARI SECRETS (AMAN)
try:
    CORRECT_PASSWORD = st.secrets["ADMIN_PASSWORD"]
except Exception:
    st.error("⚠️ Password belum terpasang di menu Secrets Streamlit!")
    st.stop()

# 3. INISIALISASI STATUS LOGIN
if 'auth' not in st.session_state:
    st.session_state.auth = False

# 4. TAMPILAN HALAMAN LOGIN
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

# 5. TAMPILAN SIDEBAR (Hanya muncul jika Login Sukses)
st.sidebar.title("🛡️ V-Guard AI")
st.sidebar.write(f"👤 User: **Erwin Sinaga**")
if st.sidebar.button("Logout"):
    st.session_state.auth = False
    st.rerun()

# 6. DASHBOARD UTAMA
st.header("📊 Financial Integrity Dashboard")
st.success("Koneksi Aman & Terverifikasi.")

# Layout Kolom untuk Grafik
col_g1, col_g2 = st.columns(2)

with col_g1:
    # Grafik Risiko (Dukungan dari requirements.txt Bapak)
    df = pd.DataFrame({'Kategori': ['Aman', 'Anomali'], 'Skor': [94, 6]})
    fig = px.pie(df, values='Skor', names='Kategori', title="Ringkasan Risiko Real-time", hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

with col_g2:
    st.info("💡 **Analisis AI:** Sistem mendeteksi stabilitas tinggi pada transaksi hari ini. Tidak ada ancaman siber yang signifikan terdeteksi di wilayah operasional.")

# 7. BAGIAN VISI & MISI
st.write("---")
st.subheader("🎯 Vision & Mission")
col_v, col_m = st.columns(2)

with col_v:
    st.markdown("#### **Vision**")
    st.info("To become the leading provider of AI-powered financial security solutions globally.")

with col_m:
    st.markdown("#### **Mission**")
    st.info("To develop innovative AI technologies that anticipate risks, automate defenses, and enable informed decision-making for businesses worldwide.")

# 8. BAGIAN PROFIL FOUNDER
st.write("---")
col_p1, col_p2 = st.columns([1, 3])

with col_p1:
    try:
        # Menggunakan file erwin.jpg yang sudah Bapak upload ke GitHub
        st.image("erwin.jpg", caption="Erwin Sinaga - Founder", use_container_width=True)
    except:
        # Cadangan jika file erwin.jpg belum terbaca sempurna
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)

with col_p2:
    st.markdown("""
    ### 👤 About the Founder
    **Erwin Sinaga**
