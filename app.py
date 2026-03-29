import streamlit as st
import pandas as pd
import numpy as np

# --- 1. KONFIGURASI HALAMAN & BRANDING ---
st.set_page_config(page_title="VGUARD AI Systems", page_icon="🛡️", layout="wide")

# Custom CSS untuk tampilan Executive
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_name_containing_id=True)

# --- 2. SIDEBAR NAVIGASI (Agar Fitur Tidak Hilang) ---
st.sidebar.image("https://www.freeiconspng.com/uploads/security-icon-png-15.png", width=100)
st.sidebar.title("VGUARD AI")
menu = st.sidebar.radio("Navigasi Sistem", ["Dashboard Performa", "AI Scanner Audit", "Paket Layanan", "Kontak Admin"])

# --- 3. LOGIKA MENU ---

if menu == "Dashboard Performa":
    st.title("🛡️ VGUARD AI Systems")
    st.subheader("Intelligence for Your Business Security")
    st.write("---")
    
    # Ringkasan Statistik
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Audit", "1,284", "+12%")
    col2.metric("Anomali Terdeteksi", "14", "-5%")
    col3.metric("Efisiensi Sistem", "98.2%", "+2.1%")

    # Grafik Performa (Fitur yang tadi sempat hilang)
    st.write("### Grafik Trend Keamanan Operasional")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Retail', 'Gudang', 'Logistik'])
    st.line_chart(chart_data)

elif menu == "AI Scanner Audit":
    st.title("🔍 AI Scanner Audit")
    st.write("Gunakan fitur ini untuk mendeteksi kecurangan atau kebocoran sistem.")
    
    # Memanggil API Key secara aman dari Secrets
    try:
        api_key = st.secrets["MY_API_KEY"]
        st.success("Sistem Terkoneksi: API VGUARD Aktif")
    except:
        st.error("Sistem Offline: API Key belum dikonfigurasi di Secrets.")

    input_data = st.text_area("Masukkan Data Transaksi/Log untuk Diaudit:")
    if st.button("Jalankan Analisis AI"):
        with st.spinner('Menganalisis data...'):
            st.info("Hasil Audit: Data sedang diproses oleh Engine VGUARD AI.")
            # Logika AI Bapak di sini

elif menu == "Paket Layanan":
    st.title("📦 Katalog Layanan VGUARD AI Systems")
    st.write("Pilih proteksi yang sesuai dengan skala bisnis Anda.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("### V-START")
        st.write("**Investasi: Rp 2,5 Juta**")
        st.write("Maintenance: Rp 1 Juta/Bulan")
        st.write("- Audit Transaksi Harian\n- Bot Notifikasi WA\n- Laporan Mingguan")
        st.button("Pilih V-START", key="btn1")

    with c2:
        st.warning("### V-GROW")
        st.write("**Investasi: Rp 5 Juta**")
        st.write("Maintenance: Rp 2,5 Juta/Bulan")
        st.write("- Semua Fitur V-START\n- AI Fraud Detection\n- Integrasi Stok Barang")
        st.button("Pilih V-GROW", key="btn2")

    with c3:
        st.error("### V-PRIME")
        st.write("**Investasi: Rp 10 Juta**")
        st.write("Maintenance: Rp 5 Juta/Bulan")
        st.write("- Semua Fitur V-GROW\n- Audit Multi-Cabang\n- Prediksi Kerugian AI")
        st.button("Pilih V-PRIME", key="btn3")

elif menu == "Kontak Admin":
    st.title("📞 Hubungi VGUARD AI Systems")
    st.write("**Founder & CEO: Pak Erwin**")
    st.write("Lokasi Operasional: Tangerang, Banten")
    st.write("WhatsApp: [Klik di Sini untuk Konsultasi](https://wa.me/628123456789)") # Ganti nomor Bapak

# --- 4. FOOTER ---
st.write("---")
st.caption("© 2026 VGUARD AI Systems Indonesia | Intelligence for Your Business Security")
