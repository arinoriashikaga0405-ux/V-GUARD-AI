import streamlit as st
import os
import pandas as pd

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# CSS PREMIUM
st.markdown("""
<style>
    .reportview-container { background: #f5f7f9; }
    .st-emotion-cache-1y4p8pa { padding-top: 2rem; }
    .vision-box {
        background: #ffffff; border-radius: 12px; padding: 25px;
        border-left: 6px solid #ff4b4b; box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    .price-card {
        background: white; border-radius: 15px; border: 1px solid #eee;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); height: 450px;
        display: flex; flex-direction: column; overflow: hidden;
    }
    .card-header {
        background: linear-gradient(135deg, #ff4b4b 0%, #a51d1d 100%);
        color: white; padding: 15px; text-align: center; font-weight: bold; font-size: 18px;
    }
    .feature-item { font-size: 13px; color: #444; margin-bottom: 6px; }
    .roi-box {
        background: #fff5f5; border: 1px solid #ff4b4b; padding: 20px;
        border-radius: 12px; color: #a51d1d; margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 2. SIDEBAR NAVIGASI
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.error("Unggah foto 'erwin.jpg'")
    
    st.title("🛡️ V-Guard AI")
    st.write("---")
    menu = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi & Misi", 
        "3. 📦 Paket Solusi & ROI", 
        "4. 🔐 Admin Panel (Upload)"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI Systems")

# --- MENU 1: PROFIL FOUNDER (100+ KATA) ---
if menu == "1. 👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with r:
        st.subheader("Erwin Sinaga")
        st.write("""
        Bapak Erwin Sinaga memiliki rekam jejak profesional yang sangat solid dengan dedikasi lebih dari 10 tahun di industri perbankan dan manajemen aset nasional. Selama satu dekade tersebut, beliau telah mendalami berbagai dinamika operasional perbankan, mulai dari manajemen risiko kredit hingga pengawasan integritas transaksi finansial yang kompleks. Pengalaman luas beliau dalam menghadapi ancaman kebocoran dana dan manipulasi data di sektor keuangan formal menjadi alasan utama lahirnya V-Guard AI Systems. 
        
        Melalui pemahaman mendalam mengenai pola-pola fraud yang sering luput dari audit konvensional, Bapak Erwin mengintegrasikan standar keamanan perbankan tingkat tinggi ke dalam ekosistem digital yang lebih luas. Beliau percaya bahwa teknologi AI bukan sekadar alat bantu, melainkan benteng pertahanan utama yang harus dimiliki setiap pelaku bisnis untuk menjamin keberlangsungan aset. Kepemimpinan beliau di V-Guard berfokus pada transparansi, akurasi, dan penyediaan proteksi finansial yang setara dengan sistem pertahanan bank global, namun dapat diakses oleh UMKM maupun korporasi modern.
        """)

# --- MENU 2: VISI & MISI ---
elif menu == "2. 🎯 Visi & Misi":
    st.title("🎯 Arah Strategis Perusahaan")
    v, m = st.columns(2)
    with v:
        st.markdown("""<div class="vision-box"><h3>🎯 Visi</h3>
        <p>Menjadi pionir penyedia infrastruktur keamanan berbasis AI yang tak tertembus di Asia Tenggara, memberikan kepastian audit bagi investor dan pemilik bisnis melalui integrasi teknologi real-time pada tahun 2026.</p></div>""", unsafe_allow_html=True)
    with m:
        st.markdown("""<div class="vision-box"><h3>🚀 Misi</h3>
        <ul>
            <li>Menghentikan kebocoran aset bisnis klien melalui sistem deteksi fraud otomatis.</li>
            <li>Mengotomatisasi kepatuhan operasional (compliance) tanpa campur tangan manusia.</li>
            <li>Memberikan laporan kesehatan finansial yang akurat dan mudah dipahami secara instan.</li>
        </ul></div>""", unsafe_allow_html=True)

# --- MENU 3: PAKET SOLUSI & ROI ---
elif menu == "3. 📦 Paket Solusi & ROI":
    st.title("📦 Solusi Keamanan & Analisis ROI")
    
    # Kalkulator ROI Kerugian
    st.subheader("📈 Analisis Potensi Kerugian Klien")
    col_roi1, col_roi2 = st.columns(2)
    with col_roi1:
        omzet = st.number_input("Omzet Bisnis Per Bulan (Rp):", min_value=10000000, value=500000000, step=10000000)
        margin_fraud = 0.05 # Estimasi rata-rata kebocoran 5% tanpa sistem AI
    with col_roi2:
        st.markdown(f"""<div class="roi-box">
        <h4>🚨 Potensi Kerugian Tanpa V-Guard:</h4>
        <h2 style="margin:0;">Rp {(omzet * margin_fraud):,.0f}</h2>
        <p style="font-size:12px;">*Estimasi kebocoran operasional & fraud rata-rata 5% per bulan.</p>
        </div>""", unsafe_allow_html=True)
    
    st.write("---")
    
    # Tabel Paket
    c1, c2 = st.columns(2)
    def draw_pkg(title, setup, monthly, features, key):
        f_list = "".join([f'<div class="feature-item">✅ {f}</div>' for f in features])
        st.markdown(f"""<div class="price-card"><div class="card-header">{title}</div><div style="padding:20px; flex-grow:1;">
        <h3>Setup: Rp {setup}</h3><p style="color:#ff4b4b; font-weight:bold;">Bulanan: Rp {monthly}</p><hr>{f_list}</div></div>""", unsafe_allow_html=True)
        st.link_button(f"PILIH {title}", wa_url, use_container_width=True, key=key)

    with c1: 
        draw_pkg("BASIC GUARD", "2.5jt", "500rb", [
            "Google Gemini AI Core", "Audit Transaksi Harian", 
            "Laporan Mingguan via Email", "Support Chat Dasar"
        ], "p1")
    with c2: 
        draw_pkg("PREMIUM SHIELD", "7.5jt", "1.5jt", [
            "MindBridge Fraud Detection", "Real-time Audit Alarm", 
            "Auto Invoice Pro", "WA Priority Support", "CCTV AI Integration"
        ], "p2")

# --- MENU 4: ADMIN PANEL (UNGGAH DATA) ---
elif menu == "4. 🔐 Admin Panel (Upload)":
    st.title("🔐 Control Center: Input Data Klien")
    
    st.info("Gunakan menu ini untuk mengunggah data mentah dari klien agar dianalisis oleh V-Guard AI.")
    
    with st.container():
        uploaded_file = st.file_uploader("Unggah Laporan Transaksi (Excel/CSV/PDF)", type=['csv', 'xlsx', 'pdf', 'jpg', 'png'])
        if uploaded_file is not None:
            st.success(f"File '{uploaded_file.name}' berhasil diterima!")
            st.warning("🤖 AI V-Guard sedang memindai anomali... (Simulasi)")
            
    st.write("---")
    st.subheader("🚨 Monitoring Terakhir")
    st.error("19:30 - Deteksi Anomali pada Transaksi Kasir 01 (Selisih Rp 450,000)")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Strategically Led by Erwin Sinaga")
