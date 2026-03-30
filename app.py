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

st.header("📊 Financial Integrity Dashboard")
st.success("Koneksi Aman & Terverifikasi.")

# Grafik Plotly (Dukungan dari requirements.txt Bapak)
df = pd.DataFrame({'Kategori': ['Aman', 'Anomali'], 'Skor': [94, 6]})
fig = px.pie(df, values='Skor', names='Kategori', title="Ringkasan Risiko Real-time")
st.plotly_chart(fig)
# ... (Baris 1-40: Kode Login & Grafik Plotly yang sudah kita buat) ...

# # --- BARIS 50: PEMBATAS & PROFIL ---
st.write("---") 
col1, col2 = st.columns([1, 2])

with col1:
    # Menggunakan file erwin.jpg yang sudah Bapak upload ke GitHub
    try:
        st.image("erwin.jpg", caption="Erwin Sinaga - Founder", use_container_width=True)
    except:
        # Cadangan jika file erwin.jpg belum terbaca sempurna oleh server
        st.warning("Memuat foto 'erwin.jpg'...")
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)

with col2:
    st.markdown("""
    ### 👤 Mengenal Founder V-Guard AI
    **Erwin Sinaga** – *Senior Business Leader & Founder*
    
    Halo! Saya **Erwin Sinaga**, berdedikasi untuk memanfaatkan AI dalam menyelesaikan masalah nyata di bidang keuangan . Dengan pengalaman lebih dari **10 tahun** di industri perbankan dan aset, saya mendirikan **V-Guard AI** untuk memberdayakan UMKM dengan solusi cerdas.
    """)

# --- FOOTER ---
st.write("---")
st.caption("© 2026 V-Guard AI Systems | Berdomisili di Tangerang, Indonesia")

# --- BARIS 67: FOOTER AKHIR ---
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
