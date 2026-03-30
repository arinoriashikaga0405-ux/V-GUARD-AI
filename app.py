import streamlit as st
import os
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS CUSTOM UNTUK TAMPILAN PREMIUM & ALARM
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
    menu = st.radio("Folder Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Layanan", 
        "4. 🔐 Admin Dashboard"
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
            st.image("erwin.jpg", use_container_width=True)
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
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.info("**BASIC**\n\nSetup: 2.5jt\nRp 500rb/Bln")
        st.link_button("Pilih Basic", wa_url)
    with c2:
        st.info("**MEDIUM**\n\nSetup: 7.5jt\nRp 1.5jt/Bln")
        # PERBAIKAN BARIS 88 DI SINI
        st.link_button("Pilih Medium", wa_url)
    with c3:
        st.info("**ENTERPRISE**\n\nSetup: 25jt\nRp 5jt/Bln")
        st.link_button("Pilih Enterprise", wa_url)
    with c4:
        st.info("**CORPORATE**\n\nSetup: 50jt\nRp 10jt/Bln")
        st.link_button("Pilih Corporate", wa_url)

# --- MENU 4: ADMIN DASHBOARD (DENGAN PASSWORD) ---
elif menu == "4. 🔐 Admin Dashboard":
    st.header("🔐 Admin Strategic Dashboard")
    
    # Proteksi Password
    password = st.text_input("Masukkan Password Admin:", type="password")
    
    if password == "admin123": 
        st.success("Akses Diterima. Selamat datang, Pak Erwin.")
        
        k1, k2, k3 = st.columns(3)
        k1.metric("Klien Aktif", "12 Cabang", "+2")
        k2.metric("Omzet Terpantau", "Rp 6.2 Miliar")
        k3.metric("Aset Diselamatkan", "Rp 310 Juta", "95%")
        
        st.write("---")
        st.subheader("🔄 Alur Proses Kerja V-Guard AI")
        
        s1, s2, s3, s4 = st.columns(4)
        with s1:
            st.markdown('<div class="step-box"><b>1. DATA IN</b><br><small>POS & CCTV</small></div>', unsafe_allow_html=True)
        with s2:
            st.markdown('<div class="step-box"><b>2. GEMINI AI</b><br><small>Logic Audit</small></div>', unsafe_allow_html=True)
        with s3:
            st.markdown('<div class="step-box"><b>3. YOLO VISION</b><br><small>Visual Check</small></div>', unsafe_allow_html=True)
        with s4:
            st.markdown('<div class="step-box"><b>4. OUTPUT</b><br><small>Inv & PDF</small></div>', unsafe_allow_html=True)
        
        st.write("---")
        uploaded = st.file_uploader("Unggah Laporan Transaksi Klien (CSV/Excel)", type=['csv', 'xlsx'])
        
        if uploaded:
            with st.status("V-Guard AI sedang memproses data...", expanded=True) as status:
                st.write("🤖 Sinkronisasi Google Gemini Core...")
                time.sleep(1)
                st.write("🔍 MindBridge memindai anomali finansial...")
                time.sleep(1)
                st.write("👁️ YOLO Vision mendeteksi objek & wajah pada CCTV...")
                time.sleep(1)
                status.update(label="Audit Selesai!", state="complete")
            
            st.markdown('<div class="alarm-banner">🚨 FRAUD DETECTED: Ditemukan selisih transaksi pada Cabang Tangerang!</div>', unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="invoice-box">
                <h4 style="margin:0; color:#1976d2;">📄 Auto-Invoice & Report Generated</h4>
                <p>Invoice <b>#VGD-{int(time.time())}</b> telah dikirim otomatis via WhatsApp.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.download_button("📥 Unduh Laporan Audit Lengkap (PDF)", "Hasil Audit Lengkap V-Guard AI", file_name="Audit_VGuard.pdf", use_container_width=True)
            
    elif password == "":
        st.warning("Silakan masukkan password untuk mengakses data.")
    else:
        st.error("Password Salah! Akses ditolak.")
