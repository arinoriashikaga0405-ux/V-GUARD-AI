import streamlit as st
import pandas as pd
import google.generativeai as genai

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# CSS UNTUK TAMPILAN MEWAH & TABEL BERSIH
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .hero-bg { background-color: #0e1117; padding: 50px; border-radius: 20px; color: white; text-align: center; margin-bottom: 30px; border-bottom: 5px solid #FFD700; }
    .card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center; color: black; height: 100%; }
    .stTable { background-color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. MENU NAVIGASI (SIDEBAR)
with st.sidebar:
    st.markdown("### 🧭 MENU UTAMA")
    halaman = st.radio("Pilih Tampilan:", ["🌐 Promosi & Umum", "👥 Area Layanan Klien", "🔐 Panel Admin"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: PROMOSI & UMUM (LANDING PAGE)
# ==========================================
if halaman == "🌐 Promosi & Umum":
    st.markdown("""
        <div class="hero-bg">
            <h1 style='font-size: 45px;'>🛡️ V-GUARD AI SYSTEMS</h1>
            <p style='font-size: 20px;'>Hentikan Kebocoran Finansial Bisnis Anda Hari Ini.</p>
            <p style='font-size: 16px; opacity: 0.7;'>Audit Otonom Berbasis AI | Standar POJK No. 56/2016.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("### Daftar Layanan & Investasi")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="card"><h3>📦 LITE</h3><h2 style="color: #1f77b4;">7,5 Jt</h2><p>Audit Harian<br>Laporan WA Otomatis</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="card" style="border: 2px solid #FFD700;"><h3>🚀 PRO</h3><h2 style="color: #2ca02c;">15 Jt</h2><p><b>Fitur LITE Lengkap</b><br>Predictive Risk Alarm</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="card"><h3>🏢 ENTERPRISE</h3><h2 style="color: #ff7f0e;">25 Jt</h2><p><b>Fitur PRO Lengkap</b><br>Vision AI Monitoring</p></div>', unsafe_allow_html=True)

# ==========================================
# HALAMAN 2: AREA LAYANAN KLIEN (TABEL DATA)
# ==========================================
elif halaman == "👥 Area Layanan Klien":
    st.title("👥 Dashboard Layanan Klien")
    st.write("Berikut adalah rangkuman status langganan dan proteksi bisnis Anda:")
    
    # Membuat Data Tabel untuk Klien
    data_klien = {
        "Nama Bisnis": ["Resto BSD Utama", "Retail Tangerang", "Cafe Serpong", "Gudang Logistik"],
        "Paket Langganan": ["V-GUARD PRO", "V-GUARD LITE", "V-GUARD PRO", "ENTERPRISE"],
        "Status Sistem": ["🛡️ Aktif", "🛡️ Aktif", "🛡️ Aktif", "🛡️ Aktif"],
        "Masa Berlaku": ["12 Jan 2027", "05 Mar 2027", "20 Feb 2027", "15 Jun 2027"],
        "Update Terakhir": ["1 Jam Lalu", "3 Jam Lalu", "30 Menit Lalu", "Real-time"]
    }
    
    df = pd.DataFrame(data_klien)
    
    # Menampilkan Tabel yang Rapi
    st.table(df)
    
    st.info("💡 Klik menu WhatsApp di halaman utama jika Anda ingin melakukan upgrade paket atau klaim laporan audit.")

# ==========================================
# HALAMAN 3: PANEL ADMIN (RAHASIA BAPAK)
# ==========================================
elif halaman == "🔐 Panel Admin":
    st.title("🔐 Panel Kendali Admin V-GUARD")
    pw = st.text_input("Masukkan Password Admin:", type="password")
    
    if pw == "vguard2026":
        st.success("Selamat bekerja, Pak Erwin.")
        st.divider()
        st.subheader("🛠️ Jalankan Audit AI")
        data_audit = st.text_area("Masukkan data untuk dianalisis:")
        if st.button("Proses Audit"):
            st.write("Menganalisis data...")
    elif pw != "":
        st.error("Akses Ditolak!")
