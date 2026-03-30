import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS UNTUK TAMPILAN PREMIUM & SEJAJAR
st.markdown("""
<style>
    .main-header { font-size: 24px; font-weight: bold; color: #1f1f1f; margin-bottom: 20px; }
    .price-card {
        background: white; border-radius: 12px; border: 1px solid #eee;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); height: 450px;
        padding: 20px; display: flex; flex-direction: column; justify-content: space-between;
    }
    .card-header {
        background: #ff4b4b; color: white; padding: 10px;
        text-align: center; font-weight: bold; border-radius: 8px; margin-bottom: 10px;
    }
    .vision-card {
        background: #f8f9fa; padding: 20px; border-radius: 12px;
        border-left: 5px solid #ff4b4b; height: 220px;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 3. SIDEBAR NAVIGASI (URUTAN BARU)
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Pilih Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Layanan", 
        "4. 🔐 Admin Panel"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI Systems | Tangerang")

# --- MENU 1: PROFIL FOUNDER (PINDAH KE NOMOR 1) ---
if menu == "1. 👤 Profil Founder":
    st.header("👤 Strategic Leadership")
    col_txt, col_img = st.columns([2, 1])
    with col_txt:
        st.subheader("Erwin Sinaga")
        st.write("""
        Bapak Erwin Sinaga adalah seorang Pemimpin Bisnis Senior dengan pengalaman lebih dari 10 tahun 
        di industri perbankan dan manajemen aset nasional. Melalui V-Guard AI, beliau menghadirkan 
        standar audit perbankan ke dalam ekosistem digital untuk mencegah kebocoran aset secara mutlak.
        """)

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.markdown('<div class="main-header">Strategi & Analisis Risiko</div>', unsafe_allow_html=True)
    v, m = st.columns(2)
    with v:
        st.markdown('<div class="vision-card"><h3>🎯 Visi</h3><p>Menjadi pemimpin pasar solusi audit AI di Indonesia pada 2026.</p></div>', unsafe_allow_html=True)
    with m:
        st.markdown('<div class="vision-card"><h3>🚀 Misi</h3><ul><li>Integrasi AI untuk deteksi fraud harian.</li><li>Otomasi pengawasan aset 24/7.</li></ul></div>', unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("📈 Kalkulator ROI (Penyelamatan Aset)")
    omzet = st.number_input("Input Omzet Bulanan (Rp):", value=500000000, step=10000000)
    st.error(f"Potensi Kebocoran Aset: Rp {omzet * 0.05:,.0f} / Bulan")

# --- MENU 3: PAKET LAYANAN (SEJAJAR & RAPI) ---
elif menu == "3. 📦 Paket Layanan":
    st.markdown('<div class="main-header">📦 Paket Proteksi V-Guard AI</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown('<div class="price-card"><div class="card-header">BASIC</div><b>Setup: 2.5jt</b><br><span style="color:#ff4b4b;">500rb/Bln</span><hr>✅ Gemini AI Core<br>✅ Audit Harian<br>✅ Email Report</div>', unsafe_allow_html=True)
        st.link_button("Pilih Basic", wa_url, use_container_width=True)
    
    with c2:
        st.markdown('<div class="price-card"><div class="card-header">MEDIUM</div><b>Setup: 7.5jt</b><br><span style="color:#ff4b4b;">1.5jt/Bln</span><hr>✅ MindBridge Fraud<br>✅ Alarm System<br>✅ Priority Support</div>', unsafe_allow_html=True)
        st.link_button("Pilih Medium", wa_url, use_container_width=True)
        
    with c3:
        st.markdown('<div class="price-card"><div class="card-header">ENTERPRISE</div><b>Setup: 25jt</b><br><span style="color:#ff4b4b;">5jt/Bln</span><hr>✅ YOLO CCTV AI<br>✅ DataRobot Risk<br>✅ Forecasting</div>', unsafe_allow_html=True)
        st.link_button("Pilih Enterprise", wa_url, use_container_width=True)
        
    with c4:
        st.markdown('<div class="price-card"><div class="card-header">CORPORATE</div><b>Setup: 50jt</b><br><span style="color:#ff4b4b;">10jt/Bln</span><hr>✅ Custom AI Training<br>✅ Full Automation<br>✅ Security Ops</div>', unsafe_allow_html=True)
        st.link_button("Pilih Corporate", wa_url, use_container_width=True)

# --- MENU 4: ADMIN PANEL ---
elif menu == "4. 🔐 Admin Panel":
    st.header("🔐 Intelligence Center")
    st.info("Status Sistem: Aktif Memantau")
    st.write("Teknologi yang sedang berjalan:")
    st.code("1. Google Gemini AI\n2. MindBridge Fraud Detection\n3. YOLO Vision Analytics")
    st.error("🚨 Deteksi Anomali: Cabang Tangerang memerlukan audit harian.")
