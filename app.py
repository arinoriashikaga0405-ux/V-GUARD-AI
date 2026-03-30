import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS UNTUK TAMPILAN PREMIUM & KARTU SEJAJAR
st.markdown("""
<style>
    .price-card {
        background: white; border-radius: 12px; border: 1px solid #eee;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); height: 500px;
        padding: 15px; display: flex; flex-direction: column;
    }
    .card-header {
        background: #ff4b4b; color: white; padding: 10px;
        text-align: center; font-weight: bold; border-radius: 8px;
        margin-bottom: 15px;
    }
    .vision-card {
        background: #f8f9fa; padding: 20px; border-radius: 12px;
        border-left: 5px solid #ff4b4b; height: 220px;
    }
    .roi-box {
        background: #fff5f5; border: 2px solid #ff4b4b; padding: 20px;
        border-radius: 12px; text-align: center; color: #a51d1d;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 3. SIDEBAR NAVIGASI DENGAN FOTO DI ATAS
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.warning("Unggah 'erwin.jpg' untuk melihat foto di sini.")
        
    st.title("🛡️ V-Guard AI")
    st.write("---")
    menu = st.radio("Pilih Folder Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Layanan", 
        "4. 🔐 Admin Panel"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI Systems | Tangerang")

# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("👤 Strategic Leadership")
    col_txt, col_img = st.columns([2, 1])
    with col_txt:
        st.subheader("Erwin Sinaga")
        st.markdown("""
        Bapak Erwin Sinaga adalah seorang Pemimpin Bisnis Senior dengan pengalaman lebih dari sepuluh tahun 
        di industri perbankan dan manajemen aset nasional. Beliau telah menguasai manajemen risiko kredit 
        dan strategi perlindungan aset korporasi skala besar. Melalui V-Guard AI, beliau menghadirkan 
        standar audit perbankan ke dalam sistem digital untuk mencegah kebocoran finansial bisnis klien 
        secara mutlak dan real-time.
        """)
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga", use_container_width=True)

# --- MENU 2: VISI, MISI & ROI (SESUAI IMAGE_0 & IMAGE_1) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.title("🎯 Strategi & Analisis Risiko")
    v, m = st.columns(2)
    with v:
        st.markdown('<div class="vision-card"><h3>🎯 Visi</h3><p>Menjadi pemimpin pasar dalam solusi keamanan audit berbasis AI di Indonesia pada 2026.</p></div>', unsafe_allow_html=True)
    with m:
        st.markdown('<div class="vision-card"><h3>🚀 Misi</h3><ul><li>Deteksi fraud otomatis.</li><li>Laporan audit transparan.</li><li>Otomasi pengawasan 24/7.</li></ul></div>', unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("📈 Analisis Potensi Kerugian Klien")
    col_roi1, col_roi2 = st.columns(2)
    with col_roi1:
        omzet = st.number_input("Omzet Bisnis Per Bulan (Rp):", value=500000000, step=10000000)
    with col_roi2:
        potensi_rugi = omzet * 0.05
        st.markdown(f"""<div class="roi-box">
        <h4>🚨 Potensi Kerugian Tanpa V-Guard:</h4>
        <h2 style="margin:0;">Rp {potensi_rugi:,.0f}</h2>
        <p style="font-size:12px;">*Estimasi kebocoran operasional & fraud rata-rata 5%</p>
        </div>""", unsafe_allow_html=True)

# --- MENU 3: PAKET LAYANAN (SEJAJAR & STABIL) ---
elif menu == "3. 📦 Paket Layanan":
    st.title("📦 Paket Proteksi V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown('<div class="price-card"><div class="card-header">BASIC (MIKRO)</div><b>Setup: 2.5jt</b><br><span style="color:red">500rb/Bln</span><hr>✅ Gemini AI Core<br>✅ Audit Harian<br>✅ Email Report</div>', unsafe_allow_html=True)
        st.link_button("Pilih Basic", wa_url, use_container_width=True)
    with c2:
        st.markdown('<div class="price-card"><div class="card-header">MEDIUM (SME)</div><b>Setup: 7.5jt</b><br><span style="color:red">1.5jt/Bln</span><hr>✅ MindBridge Fraud<br>✅ Alarm System<br>✅ Priority Support</div>', unsafe_allow_html=True)
        st.link_button("Pilih Medium", wa_url, use_container_width=True)
    with c3:
        st.markdown('<div class="price-card"><div class="card-header">ENTERPRISE</div><b>Setup: 25jt</b><br><span style="color:red">5jt/Bln</span><hr>✅ YOLO CCTV AI<br>✅ DataRobot Risk<br>✅ Forecasting</div>', unsafe_allow_html=True)
        st.link_button("Pilih Enterprise", wa_url, use_container_width=True)
    with c4:
        st.markdown('<div class="price-card"><div class="card-header">CORPORATE</div><b>Setup: 50jt</b><br><span style="color:red">10jt/Bln</span><hr>✅ Custom AI Training<br>✅ Full Automation<br>✅ Security Ops</div>', unsafe_allow_html=True)
        st.link_button("Pilih Corporate", wa_url, use_container_width=True)

# --- MENU 4: ADMIN PANEL ---
elif menu == "4. 🔐 Admin Panel":
    st.header("🔐 Intelligence Center")
    st.info("Input Data Klien untuk Analisis AI")
    uploaded_file = st.file_uploader("Unggah file transaksi (CSV/Excel)", type=['csv', 'xlsx'])
    if uploaded_file:
        st.success("File berhasil diterima. AI sedang memproses...")
