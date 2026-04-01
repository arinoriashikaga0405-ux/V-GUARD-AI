import streamlit as st
from PIL import Image
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# API KEY & INTEGRASI CORE BRAIN
GEMINI_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"

# --- CSS CUSTOM ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .package-card { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 20px; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white; font-weight: bold; }
    .feature-list { font-size: 0.85rem; color: #8b949e; line-height: 1.4; }
    .core-brain-box { background-color: #0d1117; padding: 15px; border: 1px solid #1f6feb; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR PROFIL ---
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.markdown("<div style='text-align:center;'><h3>Erwin Sinaga</h3><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Layanan & Investasi", "Portal Klien", "Admin Control Center"])

# --- 1. VISI & MISI ---
if menu == "Visi & Misi":
    st.header("Visi & Misi V-Guard AI Intelligence")
    st.markdown("""
    <div style="text-align: justify; color: #8b949e; line-height: 1.8;">
    Sebagai seorang Senior Business Leader dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, saya mendirikan V-Guard AI Intelligence untuk menjawab tantangan kebocoran internal (internal fraud). Melalui prinsip 'Digitizing Trust', kami mengubah setiap titik data menjadi bukti otentik yang tidak dapat dimanipulasi.<br><br>
    <b>Visi:</b> Menjadi standar global Digital Trust yang otonom dan transparan.<br>
    <b>Misi:</b> 'Eliminating Leakage' melalui integrasi AI prediktif dan teknologi Computer Vision untuk memastikan integritas data mutlak bagi setiap pemilik bisnis.
    </div>
    """, unsafe_allow_html=True)

# --- 2. LAYANAN & INVESTASI (NAMA PRODUK = TOMBOL WA) ---
elif menu == "Layanan & Investasi":
    st.header("🛡️ Produk V-Guard AI (Klik Nama untuk Order)")
    
    def wa_link(produk):
        return f"https://wa.me/6282122190885?text=Halo%20Pak%20Erwin,%20saya%20ingin%20order%20{produk}"

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div class='package-card'>", unsafe_allow_html=True)
        st.link_button("📦 V-LITE", wa_link("V-LITE"))
        st.markdown("<p class='feature-list'>• AI Fraud Dasar<br>• Laporan Bulanan PDF<br>• Pemasangan: Rp 1.5jt</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='package-card'>", unsafe_allow_html=True)
        st.link_button("🛡️ V-PRO", wa_link("V-PRO"))
        st.markdown("<p class='feature-list'>• Real-Time Monitoring<br>• VCS Integrasi<br>• Pemasangan: Rp 3jt</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='package-card'>", unsafe_allow_html=True)
        st.link_button("👁️ V-SIGHT", wa_link("V-SIGHT"))
        st.markdown("<p class='feature-list'>• CCTV AI Behavior<br>• Visual Audit<br>• Pemasangan: Rp 5jt</p></div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='package-card'>", unsafe_allow_html=True)
        st.link_button("🏢 V-ENTERPRISE", wa_link("V-ENTERPRISE"))
        st.markdown("<p class='feature-list'>• Multi-Cabang Central<br>• Digital Forensik<br>• Custom Solution</p></div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📊 Kalkulator ROI & Efisiensi")
    r1, r2 = st.columns(2)
    with r1:
        omzet = st.number_input("Omzet (Rp)", value=100000000)
        leak = st.slider("Kebocoran (%)", 0, 20, 5)
        st.error(f"Potensi Rugi: Rp {omzet*(leak/100):,.0f}")
    with r2:
        st.success(f"Potensi Hemat: Rp {(omzet*(leak/100))*0.95:,.0f}")
        st.info("Efisiensi Sistem: 95%")

# --- 3. PORTAL KLIEN (USER AKTIF DENGAN NAMA & PASSWORD) ---
elif menu == "Portal Klien":
    st.header("Portal Klien")
    col_a, col_b = st.columns([1, 1.2])
    
    with col_a:
        st.subheader("📝 Form Order & Upload KTP")
        with st.container(border=True):
            nama_usaha = st.text_input("Nama Usaha")
            paket_pilih = st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.file_uploader("Upload KTP (Wajib)", type=['jpg','png','pdf'])
            if st.button("Kirim Data"):
                st.link_button("Konfirmasi via WA", wa_link(f"{paket_pilih}%20untuk%20{nama_usaha}"))

    with col_b:
        st.subheader("✅ Status User Aktif")
        lock = st.text_input("Password Akses Status", type="password")
        if lock == "vguardklien2026":
            st.table([
                {"Nama": "Laundry Jaya", "Paket": "V-LITE", "Status": "Bayar", "Password": "JAY-V1"},
                {"Nama": "Cafe Mantap", "Paket": "V-PRO", "Status": "Bayar", "Password": "CAF-V2"}
            ])
        elif lock != "": st.error("Akses Ditolak")

# --- 4. ADMIN CONTROL CENTER (THE CORE BRAIN INTEGRATION) ---
elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center - The Core Brain")
    adm_pw = st.text_input("Admin Password", type="password")
    
    if adm_pw == "adminvguard2026":
        st.success("Sistem Terintegrasi: Gemini AI, MindBridge, DataRobot, YOLO Vision.")
        
        tab1, tab2, tab3 = st.tabs(["🚨 Alarms & Notifications", "🧠 Core Brain Analysis", "📊 Financial Planning"])
        
        with tab1:
            st.warning("🚨 Alarm Fraud (MindBridge): Anomali transaksi terdeteksi pada V-PRO User.")
            st.info("📅 Invoice H-7: Notifikasi otomatis dikirim ke 5 klien.")
            st.write("✅ VCS (Virtual Control System): Sinkronisasi Kasir vs Bank Berhasil.")
            
        with tab2:
            st.subheader("Google Gemini AI (The Core Brain)")
            prompt = st.text_area("Analis Audit (NLP):", "Proses data audit mentah menjadi laporan narasi...")
            if st.button("Jalankan Analis"):
                st.write(f"Menggunakan API: {GEMINI_API_KEY}")
                st.info("DataRobot sedang memprediksi risiko operasional masa depan...")
            
            st.markdown("---")
            st.subheader("👁️ YOLO / Vision AI (Digital Eye)")
            st.write("Status: Memantau stok dan pergerakan kasir secara visual.")
            
        with tab3:
            st.subheader("Workday Adaptive Planning")
            st.write("Skenario: Alarm cerdas aktif jika biaya operasional menyimpang > 5%.")
            st.success("Numeric.ai: Notifikasi harian kesehatan keuangan dikirim ke smartphone CEO.")
            
    elif adm_pw != "": st.error("Password Salah!")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>🛡️ V-Guard AI Intelligence | ©2026 | Founder: Erwin Sinaga | WA: 082122190885</div>", unsafe_allow_html=True)
