import streamlit as st
import google.generativeai as genai

# ==========================================
# 1. KONFIGURASI SISTEM & KEAMANAN
# ==========================================
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Masukkan API Key Bapak di sini
API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA" 
PASSWORD_ADMIN = "vguard2026" # Ganti password sesuai keinginan

# Konfigurasi AI
try:
    genai.configure(api_key=API_KEY)
    # PERBAIKAN: Menggunakan model terbaru gemini-1.5-flash
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Gagal konfigurasi AI. Cek API Key. Error: {e}")

# CSS UNTUK TAMPILAN MEWAH (Sesuai image_3.png)
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .hero-bg { 
        background-color: #0e1117; 
        padding: 60px; 
        border-radius: 20px; 
        color: white; 
        text-align: center;
        margin-bottom: 30px;
        border-bottom: 5px solid #FFD700;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }
    .card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
        height: 100%;
        border: 1px solid #eee;
    }
    .section-title {
        text-align: center;
        color: #0e1117;
        margin-top: 40px;
        margin-bottom: 20px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. SIDEBAR NAVIGATION
# ==========================================
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD MENU")
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100) # Ikon Profil
    halaman = st.radio("Navigasi:", ["🌐 Landing Page", "🔐 Admin Dashboard"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# ==========================================
# 3. HALAMAN 1: LANDING PAGE
# ==========================================
if halaman == "🌐 Landing Page":
    st.markdown("""
        <div class="hero-bg">
            <h1 style='font-size: 50px; margin-bottom: 10px;'>🛡️ V-GUARD AI SYSTEMS</h1>
            <p style='font-size: 22px; opacity: 0.9;'>Hentikan Kebocoran Finansial Bisnis Anda Hari Ini.</p>
            <p style='font-size: 16px; opacity: 0.7;'>Sistem Audit Otonom Berbasis AI untuk Transparansi Mutlak 24/7.</p>
        </div>
        """, unsafe_allow_html=True)
    
    col_wa1, col_wa2, col_wa3 = st.columns([1,1,1])
    with col_wa2:
        # Ganti dengan nomor WhatsApp Bapak
        st.link_button("🟢 KONSULTASI AUDIT GRATIS (WA)", "https://wa.me/6281234567890", use_container_width=True)

    st.write("###")

    # Profil Founder
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=280) # Ganti foto asli
    with col2:
        st.markdown("<h2 style='margin-top:0;'>FILOSOFI KAMI</h2>", unsafe_allow_html=True)
        st.write("""
        V-GUARD AI Systems lahir dari pengalaman kepemimpinan strategis selama lebih dari satu dekade. 
        Kami memahami bahwa musuh terbesar pertumbuhan bisnis adalah kebocoran yang tidak terdeteksi.
        
        Mengacu pada standar **POJK No. 56/2016**, kami hadir sebagai mitra audit mandiri 
        yang menjaga integritas aset Anda dengan kecerdasan AI tingkat tinggi.
        """)

    st.write("---")

    # Daftar Layanan
    st.markdown("<h2 class='section-title'>DAFTAR LAYANAN</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""<div class="card"><h3>📦 LITE</h3><h2 style='color: #1f77b4;'>7,5 Jt <small>/thn</small></h2><p>• Audit Transaksi Harian<br>• Laporan WA Otomatis<br>• Deteksi Selisih Kas</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="card" style='border: 2px solid #FFD700;'><h3>🚀 PRO</h3><h2 style='color: #2ca02c;'>15 Jt <small>/thn</small></h2><p>• <b>Semua Fitur LITE</b><br>• Predictive Risk Alarm<br>• Analisis Tren Mingguan</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="card"><h3>🏢 ENTERPRISE</h3><h2 style='color: #ff7f0e;'>25 Jt <small>/thn</small></h2><p>• <b>Semua Fitur PRO</b><br>• Visual Guard Monitoring<br>• Konsultasi Strategis Senior</p></div>""", unsafe_allow_html=True)

# ==========================================
# 4. HALAMAN 2: ADMIN DASHBOARD (Proteksi Password)
# ==========================================
else:
    st.title("🔐 Panel Admin - Jalankan Audit")
    
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

    if not st.session_state['authenticated']:
        # Form Login
        pwd_input = st.text_input("Masukkan Password Admin:", type="password")
        if st.button("Login"):
            if pwd_input == PASSWORD_ADMIN:
                st.session_state['authenticated'] = True
                st.rerun()
            else:
                st.error("Password Salah.")
    else:
        # Tampilan Admin Jika Sudah Login
        st.success(f"Akses Diterima. Selamat bekerja, Pak Erwin.")
        if st.button("Logout"):
            st.session_state['authenticated'] = False
            st.rerun()
            
        st.divider()
        
        # AREA INPUT AUDIT
        st.subheader("🛠️ Input Data untuk Analisis AI")
        prompt_audit = st.text_area("Tempel data transaksi atau jelaskan masalah (misal: selisih kas):", height=150, placeholder="Contoh: Terjadi selisih kas kekurangan 500rb di cabang Tangerang shift siang...")
        
        if st.button("JALANKAN AUDIT V-GUARD"):
            if prompt_audit:
                with st.spinner("V-GUARD AI sedang menganalisis kebocoran..."):
                    try:
                        # PERBAIKAN: Menambahkan context agar AI bertindak sebagai Auditor
                        context = "Anda adalah V-GUARD AI, sistem audit profesional. Berikan analisis mendalam, potensi penyebab, dan langkah rekomendasi mitigasi untuk masalah berikut: "
                        response = model.generate_content(context + prompt_audit)
                        
                        st.markdown("---")
                        st.markdown("### 📊 HASIL ANALISIS V-GUARD AI")
                        # PERBAIKAN: Menggunakan markdown agar hasil rapi seperti image_1.png
                        st.markdown(response.text)
                        st.success("Analisis Selesai.")
                    except Exception as e:
                        st.error(f"Terjadi kendala teknis saat memanggil AI: {e}")
                        st.warning("Pastikan API Key Bapak aktif dan memiliki kuota.")
            else:
                st.warning("Silakan masukkan data audit terlebih dahulu.")
