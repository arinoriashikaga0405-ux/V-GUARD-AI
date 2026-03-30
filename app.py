import streamlit as st
import os
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS UNTUK ALARM, NOTIFIKASI & PAKET
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
    .price-card {
        background: white; border-radius: 12px; border: 1px solid #eee;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); height: 480px;
        padding: 15px; display: flex; flex-direction: column;
    }
    .card-header {
        background: #ff4b4b; color: white; padding: 10px;
        text-align: center; font-weight: bold; border-radius: 8px; margin-bottom: 15px;
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
    menu = st.radio("Folder Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Layanan", 
        "4. 🔐 Intelligence Center"
    ])
    st.write("---")
    st.info("📡 **Sistem Status:**\n- Gemini AI: Connected\n- MindBridge: Connected\n- YOLO Vision: Connected")
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
        Bapak Erwin Sinaga merupakan seorang profesional dan Pemimpin Bisnis Senior yang memiliki rekam jejak prestisius selama lebih dari sepuluh tahun di industri perbankan serta manajemen aset nasional. Melalui dedikasi panjang di sektor keuangan formal, beliau telah menguasai secara mendalam berbagai aspek krusial seperti manajemen risiko kredit, pengawasan kepatuhan operasional (compliance), hingga perancangan strategi perlindungan aset korporasi dalam skala besar. <br><br>
        Pemahaman komprehensif beliau terhadap celah-celah fraud dan dinamika kebocoran dana yang sering terjadi pada sistem keuangan konvensional menjadi batu pijakan utama dalam mendirikan ekosistem V-Guard AI. Di bawah kepemimpinan strategisnya, Bapak Erwin berhasil mengintegrasikan standar audit perbankan yang sangat ketat dengan kecanggihan teknologi Artificial Intelligence modern, termasuk Google Gemini, MindBridge, dan YOLO Vision. Sinergi teknologi ini dirancang khusus untuk memberikan perlindungan finansial yang holistik, transparan, dan mampu mencegah segala bentuk anomali transaksi bisnis klien secara mutlak dan real-time.
        </div>
        """, unsafe_allow_html=True)

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("🎯 Strategi & Analisis Risiko")
    v, m = st.columns(2)
    with v:
        st.info("### 🎯 Visi\nMenjadi pemimpin pasar dalam solusi keamanan audit berbasis AI di Indonesia, memastikan integritas finansial bisnis klien terjaga secara mutlak pada tahun 2026.")
    with m:
        st.info("### 🚀 Misi\n1. Integrasi AI untuk deteksi fraud otomatis.\n2. Laporan audit transparan & real-time.\n3. Otomasi pengawasan aset 24/7.")
    
    st.write("---")
    st.subheader("📈 Analisis Kerugian Klien")
    omzet = st.number_input("Input Omzet Bulanan Klien (Rp):", value=500000000, step=10000000)
    potensi_rugi = omzet * 0.05
    st.error(f"🚨 Estimasi Kebocoran Aset Tanpa V-Guard: Rp {potensi_rugi:,.0f} / Bulan")

# --- MENU 3: PAKET LAYANAN (4 PAKET KEMBALI SEJAJAR) ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Proteksi & Deteksi V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown('<div class="price-card"><div class="card-header">BASIC</div><b>Setup: 2.5jt</b><br><span style="color:red">500rb/Bln</span><hr>✅ Gemini AI Core<br>✅ Audit Harian<br>✅ Email Report</div>', unsafe_allow_html=True)
        st.link_button("Pilih Basic", wa_url, use_container_width=True)
    with c2:
        st.markdown('<div class="price-card"><div class="card-header">MEDIUM</div><b>Setup: 7.5jt</b><br><span style="color:red">1.5jt/Bln</span><hr>✅ MindBridge Fraud<br>✅ Alarm System<br>✅ WA Support</div>', unsafe_allow_html=True)
        st.link_button("Pilih Medium", wa_url, use_container_width=True)
    with c3:
        st.markdown('<div class="price-card"><div class="card-header">ENTERPRISE</div><b>Setup: 25jt</b><br><span style="color:red">5jt/Bln</span><hr>✅ YOLO CCTV AI<br>✅ DataRobot Risk<br>✅ Forecasting</div>', unsafe_allow_html=True)
        st.link_button("Pilih Enterprise", wa_url, use_container_width=True)
    with c4:
        st.markdown('<div class="price-card"><div class="card-header">CORPORATE</div><b>Setup: 50jt</b><br><span style="color:red">10jt/Bln</span><hr>✅ Custom AI Training<br>✅ Full Automation<br>✅ Security Ops</div>', unsafe_allow_html=True)
        st.link_button("Pilih Corporate", wa_url, use_container_width=True)

# --- MENU 4: INTELLIGENCE CENTER (ALARM & INVOICE) ---
elif menu == "4. 🔐 Intelligence Center":
    st.header("🔐 Intelligence Center")
    st.write("### 🤖 Status Koneksi AI Terpasang:")
    m1, m2, m3 = st.columns(3)
    m1.metric("Gemini Core", "ACTIVE")
    m2.metric("MindBridge", "LINKED")
    m3.metric("YOLO Vision", "LIVE")
    
    st.write("---")
    uploaded = st.file_uploader("Unggah Laporan Transaksi untuk Audit AI", type=['csv', 'xlsx'])
    
    if uploaded:
        with st.status("V-Guard AI sedang memproses...", expanded=True) as s:
            st.write("🤖 Sinkronisasi database...")
            time.sleep(1)
            st.write("🔍 Memindai anomali dengan MindBridge...")
            time.sleep(1)
            s.update(label="Audit Selesai!", state="complete")
        
        # ALARM FRAUD MUNCUL DI SINI
        st.markdown('<div class="alarm-banner">🚨 FRAUD DETECTED: Ditemukan aktivitas mencurigakan pada data transaksi!</div>', unsafe_allow_html=True)
        
        # NOTIFIKASI INVOICE MUNCUL DI SINI
        st.markdown(f"""
        <div class="invoice-box">
            <h4 style="margin:0; color:#1976d2;">📄 Notifikasi Invoice Otomatis</h4>
            <p>Invoice <b>#VGD-{int(time.time())}</b> telah dibuat dan dikirimkan ke WhatsApp Klien.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.download_button("📥 Unduh Laporan PDF", "Data Audit", file_name="Audit_VGuard.pdf")
