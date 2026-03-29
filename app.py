import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Strategic Platform", page_icon="🛡️", layout="wide")

# --- 2. CSS CUSTOM EKSEKUTIF ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stApp { color: #1e293b; }
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
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .card-paket:hover { transform: translateY(-5px); box-shadow: 0 10px 15px rgba(0,0,0,0.1); }
    .feature-box {
        background-color: #ffffff; padding: 15px; border-radius: 10px;
        border: 1px solid #cbd5e1; margin-bottom: 10px;
    }
    .roi-calc-box {
        background-color: #f1f5f9; padding: 25px; border-radius: 15px;
        border: 2px solid #1e3a8a; margin-top: 20px;
    }
    .stButton>button { background-color: #1e3a8a; color: white; border-radius: 8px; width: 100%; font-weight: bold; height: 3.5em; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (FOTO TETAP KECIL 70PX) ---
with st.sidebar:
    try:
        st.image("erwin.jpg", width=70) 
    except:
        st.write("👤 PROFILE CEO")
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI Systems")
    st.write("---")
    menu = st.radio("NAVIGASI", ["Beranda Eksekutif", "Fitur Admin & Klien", "Dashboard Performa"])

# --- 4. LOGIKA MENU ---
if menu == "Beranda Eksekutif":
    # Header & Misi
    st.markdown('<div class="header-box"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="mission-box"><p style="font-size:1.4rem; font-style:italic; color:#1e3a8a; margin:0;">"Digitizing Trust, Eliminating Leakage"</p></div>', unsafe_allow_html=True)

    # Profil & Filosofi (Terkunci: 10 Tahun Perbankan)
    st.write("---")
    col_img, col_txt = st.columns([1, 4])
    with col_img:
        try:
            st.image("erwin.jpg", width=130) 
        except:
            st.info("Upload foto erwin.jpg")
    with col_txt:
        st.markdown("### PROFIL & VISI STRATEGIS")
        st.write("Saya **Erwin**, Founder dan CEO VGUARD AI Systems, membawa lebih dari **10 tahun pengalaman profesional di industri perbankan** dalam membangun fondasi sistem keamanan ini. Dedikasi satu dekade di sektor finansial telah membentuk keahlian saya dalam manajemen risiko, kepatuhan, dan pengawasan aset yang ketat. Kini, visi saya adalah mentransformasikan standar keamanan perbankan tersebut ke dalam ekosistem bisnis Anda.")
        st.markdown("### FILOSOFI PERISAI DIGITAL")
        st.write("VGUARD AI hadir sebagai 'Perisai Digital' yang bekerja 24/7 tanpa henti untuk mengawal integritas operasional bisnis Anda. Misi kami bukan sekadar menyediakan perangkat lunak, melainkan memberikan ketenangan pikiran bagi para pimpinan perusahaan.")

    # FITUR TETAP: KALKULATOR ROI INTERAKTIF
    st.write("---")
    st.markdown("### 📊 KALKULATOR ESTIMASI KERUGIAN & ROI")
    with st.container():
        st.markdown('<div class="roi-calc-box">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            omzet = st.number_input("Masukkan Omzet Bulanan Bisnis Anda (Rp)", min_value=0, value=100000000, step=1000000)
            leakage_rate = st.slider("Estimasi Persentase Kebocoran (%)", 1.0, 20.0, 5.0)
        with c2:
            total_loss = omzet * (leakage_rate / 100)
            saved_by_ai = total_loss * 0.90
            st.write("#### Hasil Analisis Strategis:")
            st.error(f"Potensi Kerugian/Bocor: Rp {total_loss:,.0f}")
            st.success(f"Dana Diselamatkan VGUARD AI: Rp {saved_by_ai:,.0f}")
            roi_times = saved_by_ai / 5000000 if saved_by_ai > 0 else 0
            st.info(f"Efisiensi Investasi: {roi_times:.1f}x lipat dari biaya sistem")
        st.markdown('</div>', unsafe_allow_html=True)

    # FITUR TETAP: LAYANAN PRODUK & FITUR
    st.write("---")
    st.write("### LAYANAN PRODUK & FITUR")
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.markdown('<div class="card-paket"><b>V-START</b><h3 style="color:#1e3a8a">2.5 JT</h3><hr><p style="font-size:0.85rem; text-align:left;">• Audit Harian Retail<br>• Notifikasi WA Aktif<br>• Laporan Mingguan Dasar</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="card-paket"><b>V-GROW</b><h3 style="color:#1e3a8a">5 JT</h3><hr><p style="font-size:0.85rem; text-align:left;">• Semua Fitur V-START<br>• <b>AI Fraud Detection</b><br>• Integrasi Stok Otomatis</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="card-paket"><b>V-PRIME</b><h3 style="color:#1e3a8a">10 JT</h3><hr><p style="font-size:0.85rem; text-align:left;">• Semua Fitur V-GROW<br>• Audit Multi-Cabang<br>• <b>Prediksi Kerugian AI</b></p></div>', unsafe_allow_html=True)
    with p4:
        st.markdown('<div class="card-paket"><b>V-CUSTOM</b><h3 style="color:#1e3a8a">NEGO</h3><hr><p style="font-size:0.85rem; text-align:left;">• Solusi Tailor-made<br>• Integrasi ERP/SAP<br>• Support Strategis 24/7</p></div>', unsafe_allow_html=True)

    st.write("---")
    if st.button("🛡️ KONSULTASI STRATEGIS SEKARANG"):
        st.success("Permintaan diterima. Admin VGUARD AI akan segera menghubungi Bapak Erwin.")

elif menu == "Fitur Admin & Klien":
    st.title("🌐 Ekosistem Fitur VGUARD AI")
    st.write("Simulasi operasional sistem untuk dua level pengguna utama.")
    
    tab1, tab2 = st.tabs(["💻 PORTAL ADMIN (OPERASIONAL)", "📱 PORTAL KLIEN (OWNER)"])
    
    with tab1:
        st.markdown("### Alat Kerja Tim Audit & Admin")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            <div class="feature-box">
            <b>🔍 AI Audit Scanner</b><br>
            Mendeteksi anomali pada ribuan entri data dalam hitungan detik.
            </div>
            <div class="feature-box">
            <b>📦 Auto-Reconciliation</b><br>
            Sinkronisasi otomatis antara stok gudang dan laporan penjualan.
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class="feature-box">
            <b>📑 Fraud Reporting</b><br>
            Menyusun laporan bukti digital jika ditemukan indikasi kebocoran.
            </div>
            <div class="feature-box">
            <b>🛡️ Security Log</b><br>
            Mencatat setiap perubahan data untuk menjaga integritas sistem.
            </div>
            """, unsafe_allow_html=True)
            
    with tab2:
        st.markdown("### Kontrol Eksklusif Pemilik Bisnis")
        c3, c4 = st.columns(2)
        with c3:
            st.markdown("""
            <div class="feature-box">
            <b>📊 Executive Dashboard</b><br>
            Visualisasi laba-rugi bersih secara real-time di genggaman Anda.
            </div>
            <div class="feature-box">
            <b>💬 WhatsApp Alert</b><br>
            Notifikasi langsung ke HP Anda saat ada transaksi mencurigakan.
            </div>
            """, unsafe_allow_html=True)
        with c4:
            st.markdown("""
            <div class="feature-box">
            <b>📈 ROI Analytics</b><br>
            Laporan efisiensi: Berapa banyak uang yang diselamatkan setiap bulan.
            </div>
            <div class="feature-box">
            <b>🌍 Multi-Store Control</b><br>
            Kelola banyak cabang tanpa harus berpindah lokasi.
            </div>
            """, unsafe_allow_html=True)

elif menu == "Dashboard Performa":
    st.title("📊 Dashboard Performa")
    st.line_chart(np.random.randn(20, 2))

# --- 5. FOOTER ---
st.write("---")
st.caption(f"© {datetime.now().year} VGUARD AI Systems | Tangerang, Indonesia")
