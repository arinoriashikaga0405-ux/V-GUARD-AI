import streamlit as st
import pandas as pd
import google.generativeai as genai

# 1. KONFIGURASI SISTEM & TEMA
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# API KEY & MODEL (Ganti dengan API Key Bapak)
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# CSS TAMPILAN MEWAH (BIRU NAVY & EMAS)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; color: white; }
    .hero-bg { 
        background-color: #0e1117; padding: 50px; border-radius: 20px; color: white; 
        text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px;
    }
    .card-service {
        background-color: white; padding: 25px; border-radius: 15px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center; height: 100%;
    }
    .package-pro { border: 2px solid #FFD700; transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

# 2. MENU NAVIGASI (SIDEBAR)
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD NAVIGASI")
    # Link Foto Bapak (Ganti dengan link foto baru Bapak jika sudah ada)
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
    st.markdown("<center><b>Erwin Sinaga</b><br>Founder & Senior Leader</center>", unsafe_allow_html=True)
    st.divider()
    halaman = st.radio("Pilih Halaman:", ["🌐 Promosi & Umum", "👥 Area Layanan Klien", "🔐 Panel Admin"])
    st.divider()
    st.write("📍 Tangerang, Banten")

# ==========================================
# HALAMAN 1: PROMOSI & UMUM (LANDING PAGE)
# ==========================================
if halaman == "🌐 Promosi & Umum":
    st.markdown("""
        <div class="hero-bg">
            <h1 style='color: #FFD700;'>V-GUARD AI SYSTEMS</h1>
            <h3>Hentikan Kebocoran Finansial Bisnis Anda.</h3>
            <p>Sistem Audit Otonom Berbasis AI | Standar POJK No. 56/2016.</p>
        </div>
        """, unsafe_allow_html=True)

    col_wa1, col_wa2, col_wa3 = st.columns([1,1,1])
    with col_wa2:
        st.link_button("🟢 KONSULTASI AUDIT GRATIS", "https://wa.me/6281234567890", use_container_width=True)

    st.write("###")
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=300)
    with c2:
        st.markdown("## FILOSOFI & PROFIL")
        st.write("""
        V-GUARD AI Systems lahir dari pengalaman kepemimpinan strategis selama lebih dari satu dekade 
        dalam manajemen operasional dan optimasi pendapatan. Kami hadir untuk memberikan 
        transparansi mutlak bagi pemilik bisnis melalui teknologi Audit AI.
        """)
        st.info("📍 Berdomisili di Tangerang, melayani klien nasional.")

    st.write("### Daftar Layanan Investasi")
    p1, p2, p3 = st.columns(3)
    p1.markdown('<div class="card-service"><h3>📦 LITE</h3><h2>7,5 Jt</h2><p>Audit Harian<br>Laporan WhatsApp</p></div>', unsafe_allow_html=True)
    p2.markdown('<div class="card-service package-pro"><h3>🚀 PRO</h3><h2 style="color: #FFD700;">15 Jt</h2><p><b>Fitur LITE +</b><br>Investigasi Fraud AI</p></div>', unsafe_allow_html=True)
    p3.markdown('<div class="card-service"><h3>🏢 ENTERPRISE</h3><h2>25 Jt</h2><p><b>Fitur PRO +</b><br>Konsultasi Senior Strategis</p></div>', unsafe_allow_html=True)

# ==========================================
# HALAMAN 2: AREA LAYANAN KLIEN (TABEL)
# ==========================================
elif halaman == "👥 Area Layanan Klien":
    st.title("👥 Dashboard Monitor Klien")
    st.info("Data ini diperbarui setiap 1 jam untuk akurasi audit.")
    
    data_klien = {
        "Nama Bisnis": ["Resto BSD Utama", "Retail Tangerang Central", "Cafe Serpong", "Gudang Logistik"],
        "Paket": ["V-GUARD PRO", "V-GUARD LITE", "V-GUARD PRO", "ENTERPRISE"],
        "Status": ["🛡️ Aman", "⚠️ Cek Selisih", "🛡️ Aman", "🛡️ Aman"],
        "Update": ["10:30 WIB", "09:15 WIB", "11:00 WIB", "Real-time"]
    }
    st.table(pd.DataFrame(data_klien))
    st.success("Sistem AI V-GUARD sedang memantau 4 bisnis Anda di atas.")

# ==========================================
# HALAMAN 3: PANEL ADMIN (SISTEM AUDIT AI)
# ==========================================
else:
    st.title("🔐 Panel Kendali Admin V-GUARD")
    pw = st.text_input("Password Admin:", type="password")
    
    if pw == "vguard2026":
        st.divider()
        st.subheader("🛠️ Konfigurasi Audit Klien")
        
        col_adm1, col_adm2 = st.columns(2)
        with col_adm1:
            nama_klien = st.text_input("Nama Klien:")
        with col_adm2:
            paket = st.selectbox("Pilih Paket Layanan:", ["LITE", "PRO", "ENTERPRISE"])
            
        data_input = st.text_area("Masukkan Data Transaksi/Log Masalah:", height=200)
        
        if st.button("JALANKAN AUDIT V-GUARD AI"):
            # LOGIKA INSTRUKSI RAHASIA BERDASARKAN PAKET
            if paket == "LITE":
                prompt_sys = "Anda adalah Auditor Dasar V-GUARD. Tugas Anda mencocokkan angka. Fokus pada selisih saja."
            elif paket == "PRO":
                prompt_sys = "Anda adalah Investigator V-GUARD. Cari pola fraud, curigai void transaksi, sarankan cek CCTV."
            else:
                prompt_sys = "Anda adalah Konsultan Senior V-GUARD. Berikan analisis strategis, manajemen risiko, dan optimasi profit."
            
            with st.spinner(f"Memproses Audit Mode {paket}..."):
                try:
                    res = model.generate_content(prompt_sys + data_input)
                    st.markdown("### 📊 HASIL ANALISIS INVESTIGASI")
                    st.markdown(res.text)
                    st.balloons()
                except Exception as e:
                    st.error(f"Error: {e}")
    elif pw != "":
        st.error("Akses Ditolak!")
