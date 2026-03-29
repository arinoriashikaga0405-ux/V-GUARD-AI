import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Executive Platform", page_icon="🛡️", layout="wide")

# Inisialisasi State Navigasi
if 'demo_mode' not in st.session_state:
    st.session_state.demo_mode = "Home"

# --- 2. CSS CUSTOM EKSEKUTIF ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .header-box { text-align: center; padding: 15px 0; }
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
    .card-paket:hover { transform: translateY(-5px); box-shadow: 0 10px 15px rgba(0,0,0,0.1); }
    .feature-box {
        background-color: #f8fafc; padding: 15px; border-radius: 10px;
        border-left: 4px solid #1e3a8a; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
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
        st.image("erwin.jpg", width=70) 
    except:
        st.write("👤 PROFILE CEO")
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI Systems")
    st.write("---")
    if st.button("🏠 Beranda Utama"):
        st.session_state.demo_mode = "Home"

# --- 4. LOGIKA HALAMAN ---

# A. HALAMAN DEMO ADMIN (DENGAN PASSWORD)
if st.session_state.demo_mode == "Admin":
    st.title("💻 Keamanan Portal Admin")
    password = st.text_input("Masukkan Password Admin", type="password")
    
    if password == "vguard2026": # Password bisa Bapak ganti di sini
        st.success("Akses Diterima. Selamat datang, Bapak Erwin.")
        st.write("### Dashboard Audit Operasional")
        df_audit = pd.DataFrame({
            'Waktu': ['08:30', '09:15', '10:45', '11:20'],
            'Aktivitas': ['Login Kasir A', 'Penghapusan Item', 'Input Stok Manual', 'Void Nota'],
            'Status AI': ['✅ Normal', '⚠️ Flagged', '⚠️ Anomali', '✅ Normal']
        })
        st.table(df_audit)
        if st.button("Download Laporan Audit"):
            st.write("Menyiapkan file PDF...")
    elif password != "":
        st.error("Password Salah. Akses Ditolak.")

# B. HALAMAN DEMO KLIEN
elif st.session_state.demo_mode == "Klien":
    st.title("📱 Portal Dashboard Klien (Owner)")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Omzet", "Rp 150.000.000", "+12%")
    with col2:
        st.metric("Dana Diselamatkan", "Rp 7.500.000", "Safety On")
    st.line_chart(np.random.randn(20, 1))
    st.write("### Notifikasi Terakhir")
    st.info("WhatsApp Alert: Void transaksi terdeteksi pada Toko Cabang 01 jam 10:45.")

# C. HALAMAN UTAMA
else:
    st.markdown('<div class="header-box"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="mission-box"><p style="font-size:1.4rem; font-style:italic; color:#1e3a8a; margin:0;">"Digitizing Trust, Eliminating Leakage"</p></div>', unsafe_allow_html=True)

    # Profil & Filosofi (100+ Kata)
    st.write("---")
    col_img, col_txt = st.columns([1, 4])
    with col_img:
        try:
            st.image("erwin.jpg", width=130)
        except:
            st.info("Foto CEO")
    with col_txt:
        st.markdown("### PROFIL & FILOSOFI STRATEGIS")
        st.write("""
        Saya **Erwin**, Founder dan CEO VGUARD AI Systems, membangun platform ini atas dasar dedikasi dan integritas selama lebih dari **10 tahun berkarier profesional di industri perbankan**. Pengalaman satu dekade dalam mengelola risiko keuangan, audit sistem, dan pengawasan aset di sektor finansial telah memberikan saya perspektif mendalam bahwa kepercayaan bisnis hanya bisa dipertahankan melalui transparansi data yang akurat. 

        Filosofi kami, **"Perisai Digital"**, bukan sekadar slogan, melainkan janji perlindungan aset total. Kami percaya bahwa setiap kebocoran operasional adalah ancaman bagi keberlangsungan usaha. Terinspirasi dari ketatnya standar keamanan perbankan global, VGUARD AI hadir untuk mendigitalkan kepercayaan bagi para pelaku usaha. Kami berkomitmen untuk mengeliminasi segala bentuk kecurangan dan kebocoran instan melalui integrasi teknologi AI, guna memberikan ketenangan pikiran mutlak bagi para pemimpin bisnis dalam mengambil keputusan strategis.
        """)

    # Ekosistem Navigasi
    st.write("---")
    st.markdown("### 🌐 EKOSISTEM PENGGUNA")
    t1, t2 = st.tabs(["ADMIN SYSTEM", "CLIENT PORTAL"])
    with t1:
        st.write("Fitur Khusus Tim Operasional & Audit")
        if st.button("🔑 MASUK DASHBOARD ADMIN"):
            st.session_state.demo_mode = "Admin"
            st.rerun()
    with t2:
        st.write("Fitur Khusus Pemilik Bisnis (Owner)")
        if st.button("📱 MASUK PORTAL OWNER"):
            st.session_state.demo_mode = "Klien"
            st.rerun()

    # Kalkulator ROI
    st.write("---")
    st.markdown("### 📊 ANALISIS POTENSI PENCEGAHAN KEBOCORAN")
    with st.container():
        st.markdown('<div class="roi-calc-box">', unsafe_allow_html=True)
        omzet = st.number_input("Omzet Bulanan Bisnis (Rp)", value=100000000, step=1000000)
        leak_rate = st.slider("Estimasi Kebocoran (%)", 1, 20, 5)
        st.error(f"Potensi Kerugian/Bocor: Rp {(omzet * leak_rate/100):,.0f}")
        st.markdown('</div>', unsafe_allow_html=True)

    # LAYANAN PRODUK PAKET
    st.write("---")
    st.markdown("### 🏷️ LAYANAN PRODUK & PAKET")
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.markdown('<div class="card-paket"><b>V-START</b><h3 style="color:#1e3a8a">2.5 JT</h3><hr><p style="font-size:0.85rem; text-align:left;">• Audit Harian Retail<br>• Notifikasi WA Aktif<br>• Laporan Mingguan Dasar</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="card-paket"><b>V-GROW</b><h3 style="color:#1e3a8a">5 JT</h3><hr><p style="font-size:0.85rem; text-align:left;">• Semua Fitur V-START<br>• <b>AI Fraud Detection</b><br>• Integrasi Stok Otomatis</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="card-paket"><b>V-PRIME</b><h3 style="color:#1e3a8a">10 JT</h3><hr><p style="font-size:0.85rem; text-align:left;">• Semua Fitur V-GROW<br>• Audit Multi-Cabang<br>• <b>Prediksi AI</b></p></div>', unsafe_allow_html=True)
    with p4:
        st.markdown('<div class="card-paket"><b>V-CUSTOM</b><h3 style="color:#1e3a8a">NEGO</h3><hr><p style="font-size:0.85rem; text-align:left;">• Solusi Tailor-made<br>• Integrasi ERP/SAP<br>• Support Strategis 24/7</p></div>', unsafe_allow_html=True)

    st.write("---")
    if st.button("🛡️ KONSULTASI STRATEGIS SEKARANG"):
        st.success("Admin VGUARD AI akan segera menghubungi Bapak Erwin.")

# Footer
st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Strategically developed by Erwin")
