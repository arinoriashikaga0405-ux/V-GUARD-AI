import streamlit as st
import os
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS UNTUK TAMPILAN DASHBOARD & ALARM
st.markdown("""
<style>
    .alarm-banner {
        background-color: #ff4b4b; color: white; padding: 15px;
        border-radius: 10px; text-align: center; font-weight: bold;
        border: 2px solid white; animation: blinker 1s linear infinite;
        margin-bottom: 20px;
    }
    @keyframes blinker { 50% { opacity: 0.2; } }
    .invoice-box {
        background: #e3f2fd; border-left: 8px solid #1976d2;
        padding: 20px; border-radius: 10px; margin-top: 15px;
    }
    .step-box {
        background: #f8f9fa; border: 1px solid #dee2e6;
        padding: 10px; border-radius: 8px; text-align: center;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 3. SIDEBAR NAVIGASI
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.write("---")
    menu = st.radio("Pilih Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Layanan", 
        "4. 🔐 Admin Dashboard"
    ])
    st.write("---")
    st.markdown("""
    **📡 Sistem Status:**
    * Gemini AI: Connected
    * MindBridge: Connected
    * YOLO Vision: Connected
    """)
    st.caption("Lokasi: Tangerang")

# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("👤 Strategic Leadership")
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga", use_container_width=True)
    with col_txt:
        st.subheader("Erwin Sinaga")
        st.markdown("""
        <div style="text-align: justify;">
        Bapak Erwin Sinaga adalah seorang Pemimpin Bisnis Senior yang membawa dedikasi dan keahlian mendalam selama lebih dari satu dekade di industri perbankan dan manajemen aset nasional. Selama sepuluh tahun masa baktinya di sektor keuangan formal, beliau telah menguasai berbagai seluk-beluk manajemen risiko kredit, pengawasan kepatuhan operasional, hingga strategi perlindungan aset korporasi skala besar. <br><br>
        Pengalaman luas Bapak Erwin dalam menghadapi dinamika fraud dan celah kebocoran dana di sistem perbankan konvensional menjadi fondasi utama lahirnya ekosistem V-Guard AI. Melalui kepemimpinan strategisnya, beliau menjembatani standar audit ketat perbankan dengan teknologi Artificial Intelligence (AI) terkini, menciptakan sistem pertahanan digital yang holistik, transparan, dan mampu mencegah kebocoran finansial bisnis klien secara mutlak dan real-time.
        </div>
        """, unsafe_allow_html=True)

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Strategi & Analisis Risiko")
    v, m = st.columns(2)
    with v:
        st.info("### 🎯 Visi\nMenjadi pemimpin pasar dalam solusi keamanan audit berbasis AI di Indonesia pada tahun 2026.")
    with m:
        st.info("### 🚀 Misi\n1. Integrasi AI untuk deteksi fraud otomatis.\n2. Laporan audit transparan & real-time.\n3. Otomasi pengawasan aset 24/7.")
    
    st.write("---")
    st.subheader("📈 Kalkulator Penyelamatan Aset")
    omzet = st.number_input("Input Omzet Bulanan Klien (Rp):", value=500000000, step=10000000)
    potensi_rugi = omzet * 0.05
    st.error(f"🚨 Estimasi Kebocoran Aset Tanpa V-Guard: Rp {potensi_rugi:,.0f} / Bulan")
    st.success(f"🛡️ Target Penyelamatan Aset (90%): Rp {potensi_rugi * 0.9:,.0f} / Bulan")

# --- MENU 3: PAKET LAYANAN ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Proteksi V-Guard AI")
    # PERBAIKAN: Definisi kolom harus lengkap
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.info("**BASIC**\n\nSetup: 2.5jt\nRp 500rb/Bln")
        st.link_button("Pilih Basic", wa_url)
    with c2:
        st.info("**MEDIUM**\n\nSetup: 7.5jt\nRp 1.5jt/Bln")
        st.link_button("Pilih Medium", wa_url)
    with c3:
        st.info("**ENTERPRISE**\n\nSetup: 25jt\nRp 5jt/Bln")
        st.link_button("Pilih Enterprise", wa_url)
    with c4:
        st.info("**CORPORATE**\n\nSetup: 50jt\nRp 10jt/Bln")
        st.link_button("Pilih Corporate", wa_url)

# --- MENU 4: ADMIN DASHBOARD ---
elif menu == "4. 🔐 Admin Dashboard":
    st.header("🔐 Admin Strategic Dashboard")
    
    # Metrik Ringkasan
    k1, k2, k3 = st.columns(3)
    k1.metric("Klien Aktif", "12 Cabang", "+2")
    k2.metric("Omzet Terpantau", "Rp 6.2 Miliar")
    k3.metric("Aset Diselamatkan", "Rp 310 Juta", "95%")
    
    st.write("---")
    st.subheader("🔄 Alur Audit Real-Time")
    
    # Simulasi Alur
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown('<div class="step-box"><b>1. DATA IN</b><br><small>POS & CCTV</small></div>', unsafe_allow_html=True)
    with s2:
        st.markdown('<div class="step-box"><b>2. AI AUDIT</b><br><small>Gemini Analysis</small></div>', unsafe_allow_html=True)
    with s3:
        st.markdown('<div class="step-box"><b>3. FRAUD SCAN</b><br><small>YOLO Vision Check</small></div>', unsafe_allow_html=True)
    with s4:
        st.markdown('<div class="step-box"><b>4. OUTPUT</b><br><small>Invoice & PDF</small></div>', unsafe_allow_html=True)
    
    st.write("---")
    uploaded = st.file_uploader("Unggah Laporan Transaksi Klien (CSV/Excel)", type=['csv', 'xlsx'])
    
    if uploaded:
        with st.status("V-
