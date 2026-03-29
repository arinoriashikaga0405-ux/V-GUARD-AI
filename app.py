import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Founder Platform", page_icon="🛡️", layout="wide")

# Inisialisasi State Navigasi & Password
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM EKSEKUTIF ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .header-box { text-align: center; padding: 20px 0; }
    .main-title { font-size: 3rem !important; font-weight: 800; color: #1e3a8a; margin-bottom: 0; }
    .mission-box { 
        background-color: #ffffff; padding: 20px; border-radius: 12px; 
        border-left: 8px solid #1e3a8a; box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
        text-align: center; margin: 20px auto; max-width: 900px;
    }
    .card-paket {
        background-color: #ffffff; padding: 20px; border-radius: 15px; 
        border: 1px solid #e2e8f0; height: 380px; transition: 0.3s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02); text-align: center;
    }
    .feature-card {
        background-color: #ffffff; padding: 15px; border-radius: 10px;
        border-top: 4px solid #1e3a8a; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .roi-calc-box {
        background-color: #f1f5f9; padding: 25px; border-radius: 15px;
        border: 2px solid #1e3a8a; margin-top: 20px;
    }
    .stButton>button { background-color: #1e3a8a; color: white; border-radius: 8px; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    try:
        st.image("erwin.jpg", width=80) 
    except:
        st.write("👤 CEO PROFILE")
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI")
    st.write("---")
    if st.button("🏠 Kembali ke Beranda"):
        st.session_state.page = "Home"
    st.write("---")
    st.info("Sistem ini mengadopsi standar audit perbankan 10 tahun pengalaman CEO.")

# --- 4. LOGIKA NAVIGASI ---

# A. PORTAL ADMIN (DENGAN PASSWORD & FITUR NYATA)
if st.session_state.page == "Admin":
    st.title("💻 Command Center - Admin Audit")
    pwd = st.text_input("Masukkan Kode Otoritas Admin", type="password")
    
    if pwd == "vguard2026":
        st.success("Akses Otoritas Diterima.")
        
        col_act1, col_act2 = st.columns([2, 1])
        with col_act1:
            st.subheader("🔍 Real-Time Audit Feed")
            data = {
                'ID': ['TX-99', 'TX-102', 'TX-105'],
                'Indikasi': ['Void Tidak Wajar', 'Harga Manual', 'Selisih Stok'],
                'Skor Risiko': ['🔴 High', '🟡 Medium', '🔴 High']
            }
            st.table(pd.DataFrame(data))
        
        with col_act2:
            st.subheader("🛠️ Tindakan Admin")
            if st.button("🚀 Jalankan Scan AI"):
                st.write("AI sedang menyisir kebocoran...")
            if st.button("🔒 Freeze User Suspicious"):
                st.warning("User 'Kasir_02' telah dinonaktifkan sementara.")
            if st.button("📝 Terbitkan Laporan Temuan"):
                st.info("Laporan telah dikirim ke Dashboard Owner.")

    elif pwd != "":
        st.error("Kode Salah!")

# B. PORTAL KLIEN (OWNER VIEW)
elif st.session_state.page == "Klien":
    st.title("📱 Owner Dashboard - VGUARD AI")
    st.write("Selamat Datang, Bapak Erwin (Client View)")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Omzet Terkunci", "Rp 85M", "+12%")
    m2.metric("Kebocoran Dicegah", "Rp 1.2M", "Safe", delta_color="normal")
    m3.metric("Skor Integritas Toko", "98/100")
    
    st.subheader("📈 Tren Efisiensi")
    st.line_chart(np.random.randn(20, 1))

# C. BERANDA UTAMA (PROFIL & PRODUK)
else:
    st.markdown('<div class="header-box"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="mission-box"><p style="font-size:1.4rem; font-style:italic; color:#1e3a8a; margin:0;">"Digitizing Trust, Eliminating Leakage"</p></div>', unsafe_allow_html=True)

    # Profil & Filosofi (Min. 100 Kata)
    st.write("---")
    c_img, c_txt = st.columns([1, 4])
    with c_img:
        try: st.image("erwin.jpg", width=140)
        except: st.info("CEO Photo")
    with c_txt:
        st.markdown("### PROFIL FOUNDER & FILOSOFI PERISAI DIGITAL")
        st.write("""
        Saya **Erwin**, Founder dan CEO VGUARD AI Systems, menghadirkan solusi ini berdasarkan pengalaman mendalam selama lebih dari **10 tahun berkarier profesional di industri perbankan nasional**. Selama satu dekade di sektor finansial, saya telah melihat bagaimana integritas sistem menjadi fondasi utama bagi keberlangsungan sebuah institusi. Keahlian saya dalam manajemen risiko, audit operasional, dan mitigasi fraud inilah yang saya transformasikan menjadi algoritma cerdas di VGUARD AI.

        Filosofi kami adalah **"Digitizing Trust, Eliminating Leakage"**. Kami percaya bahwa di era digital ini, kepercayaan tidak lagi bisa hanya berdasarkan kata-kata, melainkan harus dibuktikan dengan data yang transparan dan tidak dapat dimanipulasi. VGUARD AI hadir sebagai "Perisai Digital" bagi para pelaku usaha kecil hingga menengah (UMKM) agar mereka dapat mengelola bisnis dengan standar keamanan perbankan tanpa biaya yang membebani. Kami berkomitmen untuk membantu pemilik bisnis tidur lebih nyenyak dengan memastikan setiap rupiah yang masuk tetap terjaga integritasnya.
        """)

    # Navigasi Ekosistem
    st.write("---")
    st.markdown("### 🌐 AKSES EKOSISTEM")
    col_adm, col_cli = st.columns(2)
    with col_adm:
        st.markdown('<div class="feature-card"><b>DASHBOARD ADMIN</b><br>Alat audit, validasi data, dan kontrol operasional.</div>', unsafe_allow_html=True)
        if st.button("Masuk Admin Portal"):
            st.session_state.page = "Admin"
            st.rerun()
    with col_cli:
        st.markdown('<div class="feature-card"><b>DASHBOARD OWNER</b><br>Pantau profit, grafik leakage, dan notifikasi WhatsApp.</div>', unsafe_allow_html=True)
        if st.button("Masuk Client Portal"):
            st.session_state.page = "Klien"
            st.rerun()

    # ROI CALCULATOR
    st.write("---")
    st.markdown("### 📊 ESTIMASI PENCEGAHAN KEBOCORAN")
    with st.container():
        st.markdown('<div class="roi-calc-box">', unsafe_allow_html=True)
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000, step=5000000)
        leak = st.slider("Estimasi Kebocoran (%)", 1, 25, 5)
        st.error(f"Potensi Uang Hilang: Rp {(omzet * leak/100):,.0f}")
        st.success(f"Dapat Diselamatkan AI: Rp {(omzet * leak/100 * 0.9):,.0f}")
        st.markdown('</div>', unsafe_allow_html=True)

    # PRODUK & PAKET (KEMBALI HADIR)
    st.write("---")
    st.markdown("### 🏷️ LAYANAN PRODUK & PAKET")
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.markdown('<div class="card-paket"><b>V-START</b><h3 style="color:#1e3a8a">2.5 JT</h3><hr><p>• Audit Harian<br>• Notifikasi WA<br>• Laporan Mingguan</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="card-paket"><b>V-GROW</b><h3 style="color:#1e3a8a">5 JT</h3><hr><p>• Fitur V-START<br>• <b>AI Fraud Detection</b><br>• Sinkron Stok</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="card-paket"><b>V-PRIME</b><h3 style="color:#1e3a8a">10 JT</h3><hr><p>• Fitur V-GROW<br>• Multi-Cabang<br>• <b>Predictive AI</b></p></div>', unsafe_allow_html=True)
    with p4:
        st.markdown('<div class="card-paket"><b>V-CUSTOM</b><h3 style="color:#1e3a8a">NEGO</h3><hr><p>• Solusi Khusus<br>• Integrasi ERP/SAP<br>• Support 24/7</p></div>', unsafe_allow_html=True)

    if st.button("🛡️ KONSULTASI STRATEGIS"):
        st.success("Admin kami akan segera menghubungi Bapak Erwin.")

# Footer
st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically Built by Erwin (10yr Banking Experience)")
