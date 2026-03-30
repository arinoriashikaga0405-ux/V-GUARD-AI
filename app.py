import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI ---
st.set_page_config(page_title="VGUARD AI - Erwin Sinaga", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- 2. SIDEBAR ---
with st.sidebar:
    st.header("👤 CEO: ERWIN SINAGA")
    if st.button("🏠 Beranda Utama"):
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.auth:
        if st.button("🔓 Keluar Admin"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()

# --- 3. HALAMAN BERANDA ---
if st.session_state.page == "Home":
    st.title("🛡️ VGUARD AI SYSTEMS")
    
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=200)
        st.info("Founder & CEO: Erwin Sinaga")
        
    with c2:
        st.subheader("👤 Profil & Filosofi")
        # Narasi Profil > 100 kata
        deskripsi = (
            "Erwin Sinaga adalah seorang pemimpin strategis dengan rekam jejak prestisius selama "
            "lebih dari sepuluh tahun sebagai eksekutif senior di industri perbankan nasional. "
            "Pengalaman panjang beliau di dunia finansial telah membentuk standar disiplin yang "
            "sangat ketat dalam hal akurasi data, integritas sistem, dan manajemen risiko yang "
            "komprehensif. Melalui VGUARD AI Systems, beliau mentransformasi keahlian audit "
            "perbankan ke dalam solusi teknologi cerdas untuk membantu pelaku bisnis mengamankan "
            "profit mereka dari ancaman kebocoran data serta kecurangan sistemik yang sering terjadi. "
            "\n\nFilosofi kepemimpinan beliau berakar pada prinsip 'Presisi Tanpa Kompromi'. "
            "Bapak Erwin meyakini bahwa setiap rupiah dalam omzet bisnis klien adalah amanah "
            "besar yang harus dijaga dengan teknologi kecerdasan buatan paling mutakhir. "
            "VGUARD AI bukan sekadar alat audit digital biasa, melainkan perisai pertahanan "
            "strategis yang dirancang khusus untuk memberikan ketenangan pikiran bagi para "
            "pemilik bisnis modern agar tetap kompetitif."
        )
        st.write(deskripsi)
        if st.button("🚀 BUKA COMMAND CENTER (ADMIN)"):
            st.session_state.page = "Admin"
            st.rerun()

    st.divider()
    st.subheader("📊 Analisis Proteksi Profit")
    ca, cb = st.columns(2)
    with ca:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=250000000)
    with cb:
        bocor = st.slider("Estimasi Kebocoran (%)", 1, 15, 3)
    
    hasil = omzet * (bocor/100) * 0.95
    st.success(f"Potensi Profit Diselamatkan: Rp {hasil:,.0f} / bln")

    st.divider()
    st.subheader("🏷️ Paket Layanan")
    p1, p2, p3 = st.columns(3)
    p1.info("### 🔹 V-START\n
