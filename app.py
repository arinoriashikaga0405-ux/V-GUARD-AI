import streamlit as st
import os
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS UNTUK ALARM & NOTIFIKASI
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
    .founder-text {
        font-size: 16px; line-height: 1.7; text-align: justify;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 3. SIDEBAR NAVIGASI DENGAN FOTO DI ATAS
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.write("---")
    menu = st.radio("Folder Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi & ROI Kerugian", 
        "3. 📦 Paket Layanan", 
        "4. 🔐 Intelligence Center"
    ])
    st.write("---")
    st.info("📡 **Sistem Status:**\n- Gemini AI: Connected\n- MindBridge: Connected\n- YOLO Vision: Connected")
    st.caption("Lokasi: Tangerang")

# --- MENU 1: PROFIL FOUNDER (FOTO DI KIRI) ---
if menu == "1. 👤 Profil Founder":
    st.header("👤 Strategic Leadership")
    col_img, col_txt = st.columns([1, 2])
    
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga", use_container_width=True)
        else:
            st.warning("⚠️ Foto 'erwin.jpg' tidak ditemukan.")
            
    with col_txt:
        st.subheader("Erwin Sinaga")
        st.markdown(f"""
        <div class="founder-text">
        Bapak Erwin Sinaga adalah seorang Pemimpin Bisnis Senior dengan pengalaman lebih dari sepuluh tahun 
        di industri perbankan dan manajemen aset nasional. Selama masa baktinya di sektor keuangan formal, 
        beliau telah menguasai berbagai seluk-beluk manajemen risiko kredit, pengawasan kepatuhan operasional, 
        hingga strategi perlindungan aset korporasi skala besar.<br><br>
        Pengalaman luas Bapak Erwin dalam menghadapi dinamika fraud di perbankan konvensional menjadi fondasi 
        utama lahirnya ekosistem V-Guard AI. Melalui kepemimpinan strategisnya, beliau menjembatani standar 
        audit perbankan dengan teknologi AI terkini (Gemini, MindBridge, YOLO) untuk mencegah kebocoran 
        finansial bisnis klien secara mutlak dan real-time.
        </div>
        """, unsafe_allow_html=True)

# --- MENU 2: VISI & ROI ---
elif menu == "2. 🎯 Visi & ROI Kerugian":
    st.header("📈 Analisis ROI & Penyelamatan Aset")
    omzet = st.number_input("Input Omzet Bulanan Klien (Rp):", value=500000000, step=10000000)
    potensi_rugi = omzet * 0.05
    st.error(f"🚨 Estimasi Kebocoran Aset (Fraud/Error): Rp {potensi_rugi:,.0f} / Bulan")
    st.
