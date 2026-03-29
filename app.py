import streamlit as st
import google.generativeai as genai

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# CSS UNTUK TAMPILAN PROFESIONAL
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .hero-bg { background-color: #0e1117; padding: 50px; border-radius: 20px; color: white; text-align: center; margin-bottom: 30px; border-bottom: 5px solid #FFD700; }
    .card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center; color: black; height: 100%; }
    </style>
    """, unsafe_allow_html=True)

# 2. MENU NAVIGASI (SIDEBAR)
with st.sidebar:
    st.markdown("### 🧭 MENU NAVIGASI")
    # Menu dibagi menjadi 3 sesuai permintaan Bapak
    halaman = st.radio("Pilih Halaman:", ["🌐 Promosi & Umum", "👥 Area Klien", "🔐 Panel Admin"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: PROMOSI & UMUM (UNTUK SEMUA ORANG)
# ==========================================
if halaman == "🌐 Promosi & Umum":
    st.markdown("""
        <div class="hero-bg">
            <h1 style='font-size: 45px;'>🛡️ V-GUARD AI SYSTEMS</h1>
            <p style='font-size: 20px;'>Hentikan Kebocoran Finansial Bisnis Anda Hari Ini.</p>
            <p style='font-size: 16px; opacity: 0.7;'>Audit Otonom Berbasis AI sesuai Standar POJK No. 56/2016.</p>
        </div>
        """, unsafe_allow_html=True)

    col_wa1, col_wa2, col_wa3 = st.columns([1,1,1])
    with col_wa2:
        st.link_button("🟢 KONSULTASI GRATIS (WHATSAPP)", "https://wa.me/6281234567890", use_container_width=True)

    st.write("---")
    
    # Bagian Profil & Produk
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250)
    with c2:
        st.markdown("## FILOSOFI & LAYANAN")
        st.write("V-GUARD adalah mitra keamanan finansial mandiri yang menjaga integritas aset Anda.")
        
    st.write("### Daftar Layanan & Harga")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="card"><h3>📦 LITE</h3><h2>7,5 Jt</h2><p>Audit Harian<br>Laporan WA</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="card" style="border: 2px solid #FFD700;"><h3>🚀 PRO</h3><h2>15 Jt</h2><p>Predictive Risk Alarm<br>Tren Mingguan</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="card"><h3>🏢 ENTERPRISE</h3><h2>25 Jt</h2><p>Vision AI Monitoring<br>Strategis Senior</p></div>', unsafe_allow_html=True)

# ==========================================
# HALAMAN 2: AREA KLIEN (KHUSUS PENGGUNA)
# ==========================================
elif halaman == "👥 Area Klien":
    st.title("👥 Selamat Datang, Klien V-GUARD")
    st.info("Halaman ini khusus untuk melihat laporan audit bisnis Anda secara eksklusif.")
    
    st.write("### Status Sistem Anda:")
    col_status1, col_status2 = st.columns(2)
    col_status1.success("✅ Mesin AI Aktif")
    col_status2.success("✅ Monitoring POJK Aktif")
    
    st.divider()
    st.write("Silakan hubungi Admin melalui menu WhatsApp untuk mendapatkan kode akses laporan bulanan Anda.")

# ==========================================
# HALAMAN 3: PANEL ADMIN (RAHASIA BAPAK)
# ==========================================
elif halaman == "🔐 Panel Admin":
    st.title("🔐 Panel Kendali Admin V-GUARD")
    pw = st.text_input("Masukkan Password Admin:", type="password")
    
    if pw == "vguard2026":
        st.success("Akses Diterima. Selamat bekerja, Pak Erwin.")
        st.divider()
        
        # Area Audit AI
        st.subheader("🛠️ Jalankan Audit AI Profesional")
        data_audit = st.text_area("Masukkan Data Transaksi/Masalah:", placeholder="Contoh: Selisih kas 500rb...")
        
        if st.button("PROSES DENGAN AI"):
            with st.spinner("Menganalisis..."):
                # Di sini logika AI Bapak akan berjalan
                st.write("### HASIL ANALISIS INVESTIGASI:")
                st.write("1. Temuan: Ada anomali di shift siang...")
                st.write("2. Rekomendasi: Cek rekaman CCTV kasir nomor 2.")
    elif pw != "":
        st.error("Akses Ditolak!")
