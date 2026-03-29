import streamlit as st
import google.generativeai as genai

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# CSS UNTUK TAMPILAN PROFESIONAL (Sesuai Screenshot Terakhir Bapak)
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
    }
    .card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
        text-align: center;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. SIDEBAR (Hanya untuk Admin)
with st.sidebar:
    st.markdown("### 🛡️ AKSES INTERNAL")
    akses_admin = st.checkbox("Buka Panel Admin")
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# --- BAGIAN 1: LANDING PAGE (SELALU MUNCUL DI ATAS) ---
if not akses_admin:
    # TAMPILAN UNTUK KLIEN
    st.markdown("""
        <div class="hero-bg">
            <h1 style='font-size: 50px;'>🛡️ V-GUARD AI SYSTEMS</h1>
            <p style='font-size: 22px;'>Hentikan Kebocoran Finansial Bisnis Anda Hari Ini.</p>
            <p style='font-size: 16px; opacity: 0.7;'>Sistem Audit Otonom Berbasis AI untuk Transparansi Mutlak 24/7.</p>
        </div>
        """, unsafe_allow_html=True)

    col_wa1, col_wa2, col_wa3 = st.columns([1,1,1])
    with col_wa2:
        st.link_button("🟢 KONSULTASI AUDIT GRATIS", "https://wa.me/6281234567890", use_container_width=True)

    st.write("---")

    # Profil & Filosofi
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250)
    with c2:
        st.markdown("## FILOSOFI KAMI")
        st.write("""
        **V-GUARD AI Systems** lahir dari pengalaman kepemimpinan strategis selama lebih dari satu dekade. 
        Kami memahami bahwa musuh terbesar pertumbuhan bisnis adalah kebocoran yang tidak terdeteksi.
        
        Mengacu pada standar **POJK No. 56/2016**, kami hadir sebagai mitra audit mandiri 
        yang menjaga integritas aset Anda dengan kecerdasan AI tingkat tinggi.
        """)

    st.write("---")

    # Daftar Harga
    st.markdown("<h2 style='text-align: center;'>DAFTAR LAYANAN</h2>", unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="card"><h3>📦 LITE</h3><h2>7,5 Jt</h2><p>Audit Transaksi Harian<br>Laporan WA Otomatis</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="card" style="border: 2px solid #FFD700;"><h3>🚀 PRO</h3><h2>15 Jt</h2><p><b>Fitur LITE Lengkap</b><br>Predictive Risk Alarm</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="card"><h3>🏢 ENTERPRISE</h3><h2>25 Jt</h2><p><b>Fitur PRO Lengkap</b><br>Konsultasi Strategis Senior</p></div>', unsafe_allow_html=True)

# --- BAGIAN 2: ADMIN DASHBOARD (HANYA MUNCUL JIKA CHECKBOX DIKLIK) ---
else:
    st.title("🔐 Panel Kendali Admin V-GUARD")
    pw = st.text_input("Masukkan Password Admin:", type="password")
    
    if pw == "vguard2026":
        st.success("Akses Diterima, Pak Erwin.")
        st.divider()
        st.subheader("🛠️ Jalankan Audit AI")
        # Tambahkan form audit Bapak di sini
        st.text_area("Masukkan data audit...")
        st.button("Proses Audit")
    elif pw != "":
        st.error("Password Salah!")
