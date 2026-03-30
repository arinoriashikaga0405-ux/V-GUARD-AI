import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI - Erwin Sinaga", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- 2. MENU SAMPING (SIDEBAR) ---
with st.sidebar:
    st.header("👤 CEO: ERWIN SINAGA")
    st.write("---")
    if st.button("🏠 Beranda Utama"):
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.auth:
        if st.button("🔓 Keluar Admin"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()

# --- 3. TAMPILAN BERANDA ---
if st.session_state.page == "Home":
    st.title("🛡️ VGUARD AI SYSTEMS")
    
    col_foto, col_bio = st.columns([1, 2])
    
    with col_foto:
        # Menampilkan foto profil (placeholder stabil)
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=200)
        st.info("Founder & CEO: Erwin Sinaga")
        
    with col_bio:
        st.subheader("👤 Profil & Filosofi Kepemimpinan")
        # Narasi Profil > 100 kata
        st.write("""
        **Erwin Sinaga** adalah seorang pemimpin strategis dengan rekam jejak prestisius selama lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan nasional**. Pengalaman panjang beliau di dunia finansial dan pengelolaan aset telah membentuk standar disiplin yang sangat ketat dalam hal akurasi data, integritas sistem, dan manajemen risiko yang komprehensif. Melalui **VGUARD AI Systems**, beliau mentransformasi keahlian audit perbankan ke dalam solusi teknologi cerdas untuk membantu pelaku bisnis menengah dan UMKM mengamankan profit mereka dari ancaman kebocoran data serta kecurangan sistemik yang sering terjadi di lapangan.

        Filosofi kepemimpinan beliau berakar pada prinsip **"Presisi Tanpa Kompromi"**. Bapak Erwin meyakini bahwa setiap rupiah dalam omzet bisnis klien adalah amanah besar yang harus dijaga dengan teknologi kecerdasan buatan paling mutakhir. VGUARD AI bukan sekadar alat audit digital biasa, melainkan perisai pertahanan strategis yang dirancang khusus untuk memberikan ketenangan pikiran bagi para pemilik bisnis modern di era digital yang kompetitif. Keamanan aset klien adalah prioritas utama yang tidak dapat ditawar dalam setiap aspek pengembangan VGUARD demi kesuksesan jangka panjang mitra bisnis kami.
        """)
        
        if st.button("🚀 BUKA COMMAND CENTER (ADMIN)"):
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    
    # Kalkulator ROI
    st.subheader("📊 Analisis Proteksi Profit")
    c1, c2 = st.columns(2)
    with c1:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=250000000)
    with c2:
        bocor = st.slider("Estimasi Kebocoran (%)", 1, 15, 3)
    
    profit_saved = omzet * (bocor/100) * 0.95
    st.success(f"Potensi Profit Diselamatkan V-GUARD: Rp {profit_saved:,.0f} / bln")

    st.write("---")
    
    # Paket Layanan (Format stabil)
    st.subheader("🏷️ Paket Layanan Strategis")
    p1, p2, p3 = st.columns(3)
    p1.info("### 🔹 V-START\n**Rp 5 JT / Bln**\n\nScan Harian & Report Mingguan")
    p2.warning("### 🔶 V-GROW\n**Rp 15 JT / Bln**\n\nReal-time AI & Notifikasi WA")
    p3.error("### 💎 V-PRIME\n**Custom Price**\n\nFull
