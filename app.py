import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. INITIALIZE SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="VGUARD AI Systems - CEO Erwin Sinaga", page_icon="🛡️", layout="wide")

# --- 3. PREMIUM CSS ---
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { background: #1e3a8a !important; color: white !important; border-radius: 8px; font-weight: bold; width: 100%; height: 48px; }
    .roi-section { background: #ffffff; padding: 30px; border-radius: 15px; border: 2px dashed #1e3a8a; margin: 20px 0; }
    .package-card { background: white; padding: 25px; border-radius: 15px; border: 1px solid #e2e8f0; text-align: center; height: 100%; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .header-text { color: #1e3a8a; font-weight: bold; border-left: 5px solid #1e3a8a; padding-left: 12px; margin: 15px 0; }
    .profile-box { background: #f1f5f9; padding: 25px; border-radius: 15px; border-left: 8px solid #1e3a8a; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("### 👤 CEO: ERWIN SINAGA")
    st.write("---")
    if st.button("🏠 Kembali ke Beranda"):
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.auth:
        if st.button("🔓 Keluar Sistem"):
            st.session_state.auth = False
            st.session_state.page = "Home"
            st.rerun()

# --- 5. LOGIKA HALAMAN ---
if st.session_state.page == "Home":
    st.markdown('<h1 style="text-align:center; color:#1e3a8a;">🛡️ VGUARD AI SYSTEMS</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2.2])
    with col1:
        # Menggunakan link foto profil yang representatif
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", caption="Erwin Sinaga - Founder & CEO", use_container_width=True)
    with col2:
        st.markdown('<div class="profile-box">', unsafe_allow_html=True)
        st.subheader("👤 Profil & Filosofi: Erwin Sinaga")
        st.write("""
        **Erwin Sinaga** adalah seorang pemimpin strategis dengan rekam jejak prestisius selama lebih dari **sepuluh tahun sebagai eksekutif senior di industri perbankan nasional**. Pengalaman panjang beliau di dunia finansial dan perbankan aset membentuk standar disiplin yang sangat ketat dalam hal akurasi data, integritas sistem, dan manajemen risiko yang komprehensif. Melalui **VGUARD AI Systems**, beliau mentransformasi keahlian audit perbankan ke dalam solusi teknologi cerdas untuk membantu pelaku bisnis menengah dan UMKM mengamankan profit mereka dari ancaman kebocoran data serta kecurangan sistemik.

        Filosofi kepemimpinan beliau berakar pada prinsip **"Presisi Tanpa Kompromi"**. Bapak Erwin meyakini bahwa setiap rupiah dalam omzet bisnis klien adalah amanah besar yang harus dijaga dengan teknologi kecerdasan buatan paling mutakhir. VGUARD AI bukan sekadar alat audit digital, melainkan perisai pertahanan strategis yang dirancang khusus untuk memberikan ketenangan pikiran bagi para pemilik bisnis modern di era digital. Dengan visi menciptakan ekosistem bisnis yang transparan dan aman, beliau berkomitmen penuh bahwa keamanan aset klien adalah prioritas utama yang tidak dapat ditawar dalam setiap aspek pengembangan VGUARD.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.write("")
        if st.button("🚀 BUKA COMMAND CENTER (ADMIN)"):
            st.session_state.page = "Admin"
            st.rerun()

    st.write("---")
    
    # --- CALCULATOR ROI ---
    st.markdown('<h3 style="color:#1e3a8a;">ANALISIS POTENSI KERUGIAN & PROTEKSI PROFIT</h3>', unsafe_allow_html=True)
    st.markdown('<div class="roi-section">', unsafe_allow_html=True)
    oz = st.number_input("Omzet Bulanan Bisnis (Rp)", value=250000000)
    kb = st.slider("Estimasi Kebocoran/Fraud (%)", 1, 15, 3)
    
    loss = oz * (kb/100)
    saved = loss * 0.95
    
    st.error(f"Potensi Kerugian Akibat Fraud: Rp {loss:,.0f} / bln")
    st.success(f"Profit Diselamatkan V-GUARD (Efisiensi 95%): Rp {saved:,.0f} / bln")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- PAKET LAYANAN ---
    st.write("---")
    st.subheader("🏷️ PAKET LAYANAN STRATEGIS")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="package-card"><h3>🔹 V-START</h3><p>Ritel & UMKM</p><h1>Rp 5 JT</h1><p>/ bulan</p><hr><p>Scan Harian<br>Report Mingguan</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="package-card" style="border: 2px solid #1e3a8a;"><h3>🔶 V-GROW</h3><p>Bisnis Multi-Cabang</p><h1>Rp 15 JT</h1><p>/ bulan</p><hr><p>Real-time Scan<br>Notifikasi WA Otomatis</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="package-card"><h3>💎 V-PRIME</h3><p>Korporasi / Nasional</p><h1>Custom</h1><p>Value
