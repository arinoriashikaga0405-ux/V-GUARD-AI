import streamlit as st
import google.generativeai as genai

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# API KEY BAPAK (Pastikan sudah benar)
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)

# 2. MENU NAVIGASI (SIDEBAR)
with st.sidebar:
    st.title("🛡️ V-GUARD Menu")
    halaman = st.radio("Navigasi:", ["🌐 Landing Page (Klien)", "🔐 Admin Dashboard"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# --- HALAMAN 1: LANDING PAGE (TAMPILAN UTAMA KLIEN) ---
if halaman == "🌐 Landing Page (Klien)":
    # Hero Section
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>Hentikan Kebocoran Finansial Bisnis Anda Hari Ini.</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Sistem Audit Otonom Berbasis AI untuk Transparansi Mutlak 24/7.</h4>", unsafe_allow_html=True)
    
    st.write("")
    col_wa1, col_wa2, col_wa3 = st.columns([1,1,1])
    with col_wa2:
        st.link_button("🟢 KONSULTASI AUDIT GRATIS", "https://wa.me/6281234567890", use_container_width=True)

    st.divider()

    # Profil Founder
    col_prof1, col_prof2 = st.columns([1, 2])
    with col_prof1:
        st.image("https://via.placeholder.com/300", caption="Erwin Sinaga - Founder V-GUARD")
    with col_prof2:
        st.markdown("""
        ### **FILOSOFI KAMI**
        V-GUARD AI Systems lahir dari pengalaman kepemimpinan strategis selama lebih dari satu dekade. 
        Kami memahami bahwa musuh terbesar pertumbuhan bisnis adalah kebocoran yang tidak terdeteksi.
        
        Mengacu pada standar **POJK No. 56/2016**, kami hadir sebagai mitra audit mandiri 
        yang menjaga integritas aset Anda dengan kecerdasan AI tingkat tinggi.
        """)

    st.divider()

    # Pricing Table
    st.markdown("<h3 style='text-align: center;'>Daftar Layanan V-GUARD</h3>", unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    with p1:
        st.info("### **V-GUARD LITE**\n**Rp 7.500.000 / thn**\n- Audit Transaksi Harian\n- Laporan WA Otomatis\n- Deteksi Selisih Kas")
    with p2:
        st.success("### **V-GUARD PRO**\n**Rp 15.000.000 / thn**\n- **Semua Fitur LITE**\n- Predictive Risk Alarm\n- Analisis Tren Mingguan")
    with p3:
        st.warning("### **ENTERPRISE**\n**Rp 25.000.000 / thn**\n- **Semua Fitur PRO**\n- Visual Guard Monitoring\n- Konsultasi Strategis Senior")

# --- HALAMAN 2: ADMIN DASHBOARD (TAMPILAN INTERNAL BAPAK) ---
elif halaman == "🔐 Admin Dashboard":
    st.title("🔐 Panel Kendali Admin V-GUARD")
    
    # Keamanan Password
    pw = st.text_input("Masukkan Password Admin:", type="password")
    if pw == "vguard2026":
        st.success("Akses Diterima. Selamat bekerja, Pak Erwin.")
        st.divider()
        
        # Area Kerja Audit
        st.subheader("🛠️ Jalankan Analisis Audit AI")
        data_input = st.text_area("Tempel Data Transaksi/Masalah di sini:", placeholder="Contoh: Selisih kas 500rb di cabang Tangerang...")
        
        if st.button("PROSES AUDIT SEKARANG"):
            if data_input:
                with st.spinner("AI sedang menganalisis data..."):
                    try:
                        model = genai.GenerativeModel('gemini-1.5-flash')
                        prompt = f"Sebagai sistem audit V-GUARD, berikan analisis profesional untuk masalah ini: {data_input}"
                        response = model.generate_content(prompt)
                        st.markdown("### 📊 Hasil Analisis V-GUARD:")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Gagal memproses AI: {e}")
            else:
                st.warning("Silakan masukkan data terlebih dahulu.")
    elif pw != "":
        st.error("Password Salah!")
