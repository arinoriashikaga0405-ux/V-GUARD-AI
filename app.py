import streamlit as st

# 1. SETUP MENU DI SIDEBAR
st.sidebar.title("🧭 Navigasi V-GUARD")
halaman = st.sidebar.radio("Pilih Tampilan:", ["Landing Page (Klien)", "Admin Dashboard (Internal)"])

# --- HALAMAN 1: LANDING PAGE (UNTUK PUBLIK) ---
if halaman == "Landing Page (Klien)":
    st.markdown("<h1 style='text-align: center;'>🛡️ V-GUARD AI Systems</h1>", unsafe_allow_html=True)
    st.markdown("### Hentikan Kebocoran Finansial Bisnis Anda Hari Ini.")
    
    # Masukkan konten promosi, profil Bapak (10thn+ pengalaman), dan harga di sini
    st.write("---")
    st.write("**PROFIL PENDIRI:** Erwin Sinaga (Senior Business Leader)")
    st.info("V-GUARD adalah mitra keamanan finansial mandiri sesuai standar POJK No. 56/2016.")
    
    st.subheader("Daftar Layanan")
    col1, col2, col3 = st.columns(3)
    col1.metric("LITE", "Rp 7,5 Juta", "Audit Harian")
    col2.metric("PRO", "Rp 15 Juta", "Risk Predictor")
    col3.metric("ENTERPRISE", "Rp 25 Juta", "Full Audit")
    
    st.link_button("🟢 Hubungi Kami via WhatsApp", "https://wa.me/6281234567890")

# --- HALAMAN 2: ADMIN DASHBOARD (UNTUK BAPAK) ---
elif halaman == "Admin Dashboard (Internal)":
    st.title("🔐 Panel Kendali Admin V-GUARD")
    
    # Sistem Keamanan Sederhana
    password = st.text_input("Masukkan Password Admin:", type="password")
    
    if password == "vguard2026": # Ganti password sesuka Bapak
        st.success("Akses Diterima. Selamat bekerja, Pak Erwin.")
        st.divider()
        
        # Di sini tempat Bapak memasukkan data audit klien untuk dianalisis AI
        st.subheader("Input Data Audit Klien")
        input_data = st.text_area("Tempel data transaksi/kasir di sini:", placeholder="Contoh: Selisih kas 500rb...")
        
        if st.button("Jalankan Audit AI"):
            with st.spinner("Sedang menganalisis kebocoran..."):
                # Di sini logika AI Bapak akan bekerja (menggunakan API Key yang sudah aktif)
                st.write("### HASIL ANALISIS V-GUARD:")
                st.write("1. Periksa shift kasir jam 14:00...")
                st.write("2. Ada ketidakcocokan antara stok fisik dan sistem...")
    else:
        st.warning("Silakan masukkan password untuk mengakses fitur audit.")
