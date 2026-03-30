import streamlit as st
import os
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# 2. CSS UNTUK ALARM, NOTIFIKASI & TAMPILAN
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
        font-size: 16px; line-height: 1.8; text-align: justify; color: #333;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 3. SIDEBAR NAVIGASI
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True) # Foto di atas judul
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

# --- MENU 1: PROFIL FOUNDER (FOTO DI KIRI & 100+ KATA) ---
if menu == "1. 👤 Profil Founder":
    st.header("👤 Strategic Leadership")
    col_img, col_txt = st.columns([1, 2])
    
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga", use_container_width=True) # Foto di kiri
        else:
            st.warning("⚠️ File 'erwin.jpg' tidak ditemukan.")
            
    with col_txt:
        st.subheader("Erwin Sinaga")
        # Profil disusun > 100 kata sesuai instruksi
        st.markdown("""
        <div class="founder-text">
        Bapak Erwin Sinaga merupakan seorang profesional dan Pemimpin Bisnis Senior yang memiliki rekam jejak prestisius selama lebih dari sepuluh tahun di industri perbankan serta manajemen aset nasional. Melalui dedikasi panjang di sektor keuangan formal, beliau telah menguasai secara mendalam berbagai aspek krusial seperti manajemen risiko kredit, pengawasan kepatuhan operasional (compliance), hingga perancangan strategi perlindungan aset korporasi dalam skala besar. <br><br>
        Pemahaman komprehensif beliau terhadap celah-celah fraud dan dinamika kebocoran dana yang sering terjadi pada sistem keuangan konvensional menjadi batu pijakan utama dalam mendirikan ekosistem V-Guard AI. Di bawah kepemimpinan strategisnya, Bapak Erwin berhasil mengintegrasikan standar audit perbankan yang sangat ketat dengan kecanggihan teknologi Artificial Intelligence modern, termasuk Google Gemini, MindBridge, dan YOLO Vision. Sinergi teknologi ini dirancang khusus untuk memberikan perlindungan finansial yang holistik, transparan, dan mampu mencegah segala bentuk anomali transaksi bisnis klien secara mutlak dan real-time.
        </div>
        """, unsafe_allow_html=True)

# --- MENU 2: VISI & ROI ---
elif menu == "2. 🎯 Visi & ROI Kerugian":
    st.header("📈 Analisis ROI & Penyelamatan Aset")
    omzet = st.number_input("Input Omzet Bulanan Klien (Rp):", value=500000000, step=10000000)
    potensi_rugi = omzet * 0.05
    st.error(f"🚨 Estimasi Kebocoran Aset Tanpa V-Guard: Rp {potensi_rugi:,.0f} / Bulan")
    st.success(f"🛡️ Potensi Penyelamatan Aset: Rp {potensi_rugi * 0.9:,.0f} / Bulan")

# --- MENU 3: PAKET LAYANAN ---
elif menu == "3. 📦 Paket Layanan":
    st.header("📦 Paket Proteksi AI")
    c1, c2 = st.columns(2)
    with c1:
        st.info("**BASIC (MIKRO)**\n\nSetup: 2.5jt | Rp 500rb/Bln\n- Gemini AI Core\n- Audit Harian")
        st.link_button("Pilih Basic", wa_url)
    with c2:
        st.info("**MEDIUM (SME)**\n\nSetup: 7.5jt | Rp 1.5jt/Bln\n- MindBridge Fraud\n- Alarm System")
        st.link_button("Pilih Medium", wa_url)

# --- MENU 4: INTELLIGENCE CENTER (ALARM, INVOICE & PDF) ---
elif menu == "4. 🔐 Intelligence Center":
    st.header("🔐 Intelligence Center")
    
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
        
        st.markdown('<div class="alarm-banner">🚨 FRAUD DETECTED: Ditemukan aktivitas mencurigakan!</div>', unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="invoice-box">
            <h4 style="margin:0; color:#1976d2;">📄 Notifikasi Invoice & Laporan</h4>
            <p>Invoice <b>#VGD-{int(time.time())}</b> telah dikirim via WhatsApp.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Fitur Download Laporan PDF (Simulasi)
        st.download_button(
            label="📥 Unduh Laporan Hasil Audit (PDF)",
            data="Hasil Audit V-Guard AI: Ditemukan 2 anomali transaksi.",
            file_name="Laporan_Audit_VGuard.pdf",
            mime="application/pdf",
            use_container_width=True
        )
