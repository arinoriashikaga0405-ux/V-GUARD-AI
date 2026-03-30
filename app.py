import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. SETTING DASAR ---
st.set_page_config(page_title="VGUARD AI - Erwin Sinaga", layout="wide")

if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

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
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # Foto Profil
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250)
        st.info("Founder & CEO: Erwin Sinaga")
        
    with col2:
        st.subheader("👤 Profil & Filosofi")
        # Narasi Profil > 100 kata
        st.write("""
        **Erwin Sinaga** adalah seorang pemimpin strategis dengan rekam jejak prestisius selama lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan nasional**. Pengalaman panjang beliau di dunia finansial telah membentuk standar disiplin yang sangat ketat dalam hal akurasi data, integritas sistem, dan manajemen risiko yang komprehensif. Melalui **VGUARD AI Systems**, beliau mentransformasi keahlian audit perbankan ke dalam solusi teknologi cerdas untuk membantu pelaku bisnis mengamankan profit mereka dari ancaman kebocoran data serta kecurangan sistemik yang sering terjadi di lapangan.

        Filosofi kepemimpinan beliau berakar pada prinsip **"Presisi Tanpa Kompromi"**. Bapak Erwin meyakini bahwa setiap rupiah dalam omzet bisnis klien adalah amanah besar yang harus dijaga dengan teknologi kecerdasan buatan paling mutakhir. VGUARD AI bukan sekadar alat audit digital biasa, melainkan perisai pertahanan strategis yang dirancang khusus untuk memberikan ketenangan pikiran bagi para pemilik bisnis modern di era digital. Keamanan aset klien adalah prioritas utama yang tidak dapat ditawar dalam setiap aspek pengembangan VGUARD demi kesuksesan jangka panjang mitra bisnis kami.
        """)
        if st.button("🚀 BUKA COMMAND CENTER (ADMIN)"):
            st.session_state.page = "Admin"
            st.rerun()

    st.divider()
    
    # Kalkulator ROI
    st.subheader("📊 Analisis Proteksi Profit")
    c1, c2 = st.columns(2)
    with c1:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=250000000)
    with c2:
        bocor = st.slider("Estimasi Kebocoran (%)", 1, 15, 3)
    
    hasil = omzet * (bocor/100) * 0.95
    st.success(f"Potensi Profit Diselamatkan V-GUARD: Rp {hasil:,.0f} / bln")

    # Paket Layanan
    st.divider()
    st.subheader("🏷️ Paket Layanan Strategis")
    p1, p2, p3 = st.columns(3)
    p1.info("🔹 **V-START**\n\nRp 5 JT / Bln\n\nScan Harian & Report")
    p2.warning("🔶 **V-GROW**\n\nRp 15 JT / Bln\n\nReal-time AI & WA")
    p3.error("💎 **V-PRIME**\n\nCustom Price\n\nFull AI & Support")

# --- 4. HALAMAN ADMIN ---
elif st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.subheader("🔐 Executive Access")
        pwd = st.text_input("Password Admin:", type="password")
        if st.button("Masuk"):
            if pwd == "VGUARD2026":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        st.header("💻 Command Center - Erwin Sinaga")
        t1, t2, t3, t4, t5 = st.tabs(["🔍 V-Scan", "📊 Monitoring", "📍 Map", "💰 Billing", "⚙️ Klien"])
        
        with t1:
            st.write("### 🚀 V-SCAN: ANALISA FRAUD")
            st.file_uploader("Unggah Laporan")
            st.button("Mulai Scan")
        with t2:
            st.write("### 📅 MONITORING KEPATUHAN")
            st.table(pd.DataFrame({"Klien": ["Toko Maju"], "Status": ["Aktif"]}))
            st.button("Kirim Reminder WA")
        with t3:
            st.write("### 📍 GEOLOKASI KLIEN")
            st.map()
        with t4:
            st.write("### 💰 BILLING & AR")
            st.metric("Piutang Berjalan", "Rp 45.000.000")
        with t5:
            st.write("### ⚙️ MANAJEMEN KLIEN")
            st.text_input("Nama Perusahaan")
            if st.button("Daftarkan"): st.success("Klien Terdaftar")

st.divider()
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Built by Erwin Sinaga")
