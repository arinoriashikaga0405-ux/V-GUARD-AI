import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIG ---
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

# --- 3. HOME PAGE ---
if st.session_state.page == "Home":
    st.title("🛡️ VGUARD AI SYSTEMS")
    
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=200)
        st.info("Founder & CEO: Erwin Sinaga")
        
    with c2:
        st.subheader("👤 Profil & Filosofi")
        # Menggunakan Triple Quotes agar tidak Error
        deskripsi = """
        Erwin Sinaga adalah seorang pemimpin strategis dengan rekam jejak prestisius selama lebih dari sepuluh tahun sebagai eksekutif senior di industri perbankan nasional. Pengalaman panjang beliau di dunia finansial telah membentuk standar disiplin yang sangat ketat dalam hal akurasi data, integritas sistem, dan manajemen risiko yang komprehensif. Melalui VGUARD AI Systems, beliau mentransformasi keahlian audit perbankan ke dalam solusi teknologi cerdas untuk membantu pelaku bisnis mengamankan profit mereka dari ancaman kebocoran data serta kecurangan sistemik yang sering terjadi di lapangan.

        Filosofi kepemimpinan beliau berakar pada prinsip 'Presisi Tanpa Kompromi'. Bapak Erwin meyakini bahwa setiap rupiah dalam omzet bisnis klien adalah amanah besar yang harus dijaga dengan teknologi kecerdasan buatan paling mutakhir. VGUARD AI bukan sekadar alat audit digital biasa, melainkan perisai pertahanan strategis yang dirancang khusus untuk memberikan ketenangan pikiran bagi para pemilik bisnis modern agar tetap kompetitif dan berkembang sehat di era digital.
        """
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
    
    # Menggunakan teks sederhana untuk menghindari error
    p1.info("### 🔹 V-START\nRp 5 JT / Bln\nScan Harian & Report")
    p2.warning("### 🔶 V-GROW\nRp 15 JT / Bln\nReal-time AI & WA")
    p3.error("### 💎 V-PRIME\nCustom Price\nFull AI & Support")

# --- 4. ADMIN PAGE ---
elif st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.subheader("🔐 Executive Access")
        pwd = st.text_input("Password Admin:", type="password")
        if st.button("Masuk"):
            if pwd == "VGUARD2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Akses Ditolak!")
    else:
        st.header("💻 Command Center - Erwin Sinaga")
        t1, t2, t3, t4, t5 = st.tabs(["🔍 V-Scan", "📊 Monitoring", "📍 Map", "💰 Billing", "⚙️ Klien"])
        
        with t1:
            st.write("### 🚀 V-SCAN")
            st.file_uploader("Unggah Laporan Penjualan")
            st.button("Jalankan Audit AI")
        with t2:
            st.write("### 📅 MONITORING")
            st.table(pd.DataFrame({"Klien": ["Toko Maju", "Resto Jaya"], "Status": ["Aktif", "Audit Pending"]}))
