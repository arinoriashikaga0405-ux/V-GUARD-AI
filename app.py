import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. SETTING DASAR ---
st.set_page_config(page_title="VGUARD AI - Erwin Sinaga", layout="wide")

# Inisialisasi status halaman
if 'page' not in st.session_state: st.session_state.page = "Home"
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.header("👤 CEO: ERWIN SINAGA")
    st.write("---")
    if st.button("🏠 Halaman Beranda"):
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
    
    col_foto, col_bio = st.columns([1, 2])
    
    with col_foto:
        # Menampilkan foto profil
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250)
        st.info("Founder & CEO: Erwin Sinaga")
        
    with col_bio:
        st.subheader("👤 Profil & Filosofi Kepemimpinan")
        # Narasi Profil > 100 kata sesuai permintaan
        st.write("""
        **Erwin Sinaga** adalah seorang pemimpin strategis dengan rekam jejak prestisius selama lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan nasional**. Pengalaman panjang beliau di dunia finansial dan pengelolaan aset telah membentuk standar disiplin yang sangat ketat dalam hal akurasi data, integritas sistem, dan manajemen risiko yang komprehensif. Melalui **VGUARD AI Systems**, beliau mentransformasi keahlian audit perbankan ke dalam solusi teknologi cerdas untuk membantu pelaku bisnis menengah dan UMKM mengamankan profit mereka dari ancaman kebocoran data serta kecurangan sistemik yang sering terjadi di lapangan.

        Filosofi kepemimpinan beliau berakar pada prinsip **"Presisi Tanpa Kompromi"**. Bapak Erwin meyakini bahwa setiap rupiah dalam omzet bisnis klien adalah amanah besar yang harus dijaga dengan teknologi kecerdasan buatan paling mutakhir. VGUARD AI bukan sekadar alat audit digital biasa, melainkan perisai pertahanan strategis yang dirancang khusus untuk memberikan ketenangan pikiran bagi para pemilik bisnis modern di era digital yang kompetitif. Dengan visi menciptakan ekosistem bisnis yang transparan dan aman, beliau berkomitmen penuh bahwa keamanan aset klien adalah prioritas utama yang tidak dapat ditawar dalam setiap aspek pengembangan VGUARD demi kesuksesan jangka panjang mitra bisnis kami.
        """)
        
        if st.button("🚀 MASUK KE COMMAND CENTER (ADMIN)"):
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    
    # Kalkulator ROI Sederhana
    st.subheader("📊 Analisis Proteksi Profit Bisnis")
    c1, c2 = st.columns(2)
    with c1:
        omzet = st.number_input("Omzet Bulanan Bisnis (Rp)", value=250000000)
    with c2:
        kebocoran = st.slider("Estimasi Kebocoran/Fraud (%)", 1, 15, 3)
    
    saved = omzet * (kebocoran/100) * 0.95
    st.success(f"Potensi Profit Diselamatkan V-GUARD (Efisiensi 95%): Rp {saved:,.0f} / bln")

    st.write("---")
    
    # Paket Layanan (Tanpa HTML rumit agar tidak error)
    st.subheader("🏷️ Paket Layanan Strategis")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.info("### 🔹 V-START\n**UMKM & Ritel**\n\n**Rp 5 JT / Bulan**\n\n- Scan Harian\n- Report Mingguan")
    with p2:
        st.success("### 🔶 V-GROW\n**Multi-Cabang**\n\n**Rp 15 JT / Bulan**\n\n- Real-time AI Scan\n- Notifikasi WA Otomatis")
    with p3:
        st.error("### 💎 V-PRIME\n**Korporasi**\n\n**Custom Price**\n\n- Dedicated AI Support\n- Audit Trail Perbankan")

# --- 4. HALAMAN ADMIN (COMMAND CENTER) ---
elif st.session_state.page == "Admin":
    if not st.session_state.auth:
        st.subheader("🔐 Executive Access")
        password = st.text_input("Password Admin:", type="password")
        if st.button("Verifikasi Akses"):
            if password == "VGUARD2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Akses Ditolak! Password Salah.")
    else:
        st.header("💻 Command Center - Erwin Sinaga")
        
        # 5 Tab Fitur Admin Sesuai Permintaan
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🔍 V-Scan", 
            "📊 Monitoring", 
            "📍 Map Klien", 
            "💰 Billing AR", 
            "⚙️ Manajemen"
        ])
        
        with tab1:
            st.write("### 🚀 V-SCAN: ANALISA FRAUD")
            st.file_uploader("Unggah Laporan Penjualan (CSV/Excel)")
            if st.button("Mulai Analisa Sistem"):
                st.warning("Menunggu Unggahan File...")
                
        with tab2:
            st.write("### 📅 MONITORING KEPATUHAN")
            data_klien = {"Nama Klien": ["Toko Maju", "Resto Jaya"], "Status": ["Aktif", "Audit Pending"]}
            st.table(pd.DataFrame(data_klien))
            st.button("Kirim Reminder WhatsApp")
            
        with tab3:
            st.write("### 📍 SEBARAN GEOLOKASI KLIEN")
            st.map()
            
        with tab4:
            st.write("### 💰 BILLING & AR CONTROL")
            st.metric("Total Piutang Berjalan", "Rp 45.000.000", "+5%")
            
        with tab5:
            st.write("### ⚙️ MANAJEMEN KLIEN BARU")
            st.text
