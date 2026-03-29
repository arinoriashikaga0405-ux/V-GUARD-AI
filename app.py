import streamlit as st
import pandas as pd

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# CSS UNTUK TAMPILAN PROFESIONAL
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .hero-bg { background-color: #0e1117; padding: 50px; border-radius: 20px; color: white; text-align: center; margin-bottom: 30px; border-bottom: 5px solid #FFD700; }
    .card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center; color: black; }
    </style>
    """, unsafe_allow_html=True)

# 2. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("### 🧭 MENU NAVIGASI")
    halaman = st.radio("Pilih Halaman:", ["🌐 Promosi & Umum", "👥 Area Layanan Klien", "🔐 Panel Admin"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: PROMOSI & UMUM
# ==========================================
if halaman == "🌐 Promosi & Umum":
    st.markdown("""
        <div class="hero-bg">
            <h1 style='font-size: 45px;'>🛡️ V-GUARD AI SYSTEMS</h1>
            <p style='font-size: 20px;'>Hentikan Kebocoran Finansial Bisnis Anda Hari Ini.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center;'>Daftar Layanan</h2>", unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="card"><h3>📦 LITE</h3><h2>7,5 Jt</h2><p>Audit Harian<br>Laporan WA</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="card" style="border: 2px solid #FFD700;"><h3>🚀 PRO</h3><h2>15 Jt</h2><p>Predictive Risk Alarm<br>Tren Mingguan</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="card"><h3>🏢 ENTERPRISE</h3><h2>25 Jt</h2><p>Vision AI Monitoring<br>Strategis Senior</p></div>', unsafe_allow_html=True)

# ==========================================
# HALAMAN 2: AREA LAYANAN KLIEN (TABEL DATA)
# ==========================================
elif halaman == "👥 Area Layanan Klien":
    st.markdown("## 👥 Selamat Datang, Klien V-GUARD")
    st.info("Halaman ini khusus untuk melihat status langganan dan proteksi bisnis Anda secara eksklusif.")
    
    # 1. Status Ringkasan
    col_status1, col_status2 = st.columns(2)
    col_status1.success("✅ Mesin AI Aktif")
    col_status2.success("✅ Monitoring POJK Aktif")
    
    st.write("### 📋 Detail Langganan & Produk")
    
    # 2. MEMBUAT TABEL DATA KLIEN
    # Bapak bisa mengubah nama-nama di bawah ini sesuai klien Bapak
    data_klien = {
        "Nama Bisnis": ["Resto BSD Utama", "Retail Tangerang Central", "Cafe Serpong Jaya", "Gudang Logistik Karawaci"],
        "Produk Terpasang": ["V-GUARD PRO", "V-GUARD LITE", "V-GUARD PRO", "V-GUARD ENTERPRISE"],
        "Status Audit": ["🛡️ Aktif", "🛡️ Aktif", "🛡️ Aktif", "🛡️ Aktif"],
        "Masa Berlaku": ["12 Jan 2027", "05 Mar 2027", "20 Feb 2027", "15 Jun 2027"],
        "Keterangan": ["Lancar", "Cek Shift Malam", "Lancar", "Optimal"]
    }
    
    df = pd.DataFrame(data_klien)
    
    # Menampilkan Tabel di Streamlit
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.write("---")
    st.markdown("⚠️ *Jika ada ketidaksesuaian data, silakan hubungi Admin melalui tombol WhatsApp di halaman Promosi.*")

# ==========================================
# HALAMAN 3: PANEL ADMIN
# ==========================================
elif halaman == "🔐 Panel Admin":
    st.title("🔐 Panel Kendali Admin V-GUARD")
    pw = st.text_input("Masukkan Password Admin:", type="password")
    if pw == "vguard2026":
        st.success("Akses Diterima, Pak Erwin.")
        # Isi dashboard admin Bapak di sini...
    elif pw != "":
        st.error("Akses Ditolak!")
