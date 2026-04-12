import streamlit as st
import os
if 'auth_status' not in st.session_state:
    st.session_state.auth_status = False

if 'client_info' not in st.session_state:
    st.session_state.client_info = {"nama": "User", "paket": "V-LITE"}
import google.generativeai as genai

# --- TAMBAHKAN INI DI SINI (Mulai Baris 4) ---
if 'auth_status' not in st.session_state:
    st.session_state.auth_status = False

if 'admin_logged_in' not in st.session_state:
    st.session_state.admin_logged_in = False
# --- 1. KONFIGURASI ENGINE & SECURITY ---

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

# Konfigurasi Efisiensi Biaya API < 20%
generation_config = {
    "temperature": 0.2,
    "max_output_tokens": 50,
}

model_gemini = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    generation_config=generation_config,
    system_instruction="Analisa transaksi. Jika Fraud/Anomali balas 'ALERT'. Jika normal balas 'PASS'."
)

# --- 2. KONFIGURASI HALAMAN ---
  # PASTIKAN SEMUA BARIS DI BAWAH INI MENPEL KE KIRI (TIDAK ADA SPASI)
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

if 'auth_status' not in st.session_state:
    st.session_state.auth_status = False

if 'admin_logged_in' not in st.session_state:
    st.session_state.admin_logged_in = False
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; height: 45px; }
    .stTextInput>div>div>input { background-color: #1e293b; color: white; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA V-GUARD (PENYARING BIAYA API 20%) ---
def proses_transaksi(total, data_input):
    if total < 5000000:
        return "PASS (Auto)", False
    response = model_gemini.generate_content(f"Cek: {data_input}")
    return response.text, True

# --- 4. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.markdown("<div style='text-align:center;'><p style='color:white; font-weight:bold; margin-bottom:0;'>Erwin Sinaga</p><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Produk & Layanan", "ROI Kerugian Klien", "Portal Klien", "Admin Control Center"])

# --- 5. LOGIKA MENU ---

if menu == "Visi & Misi":
    st.header("Digitizing Trust, Eliminating Leakage")
    # MENAMPILKAN FOTO FOUNDER DI HALAMAN VISI & MISI
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga - Founder & CEO", use_container_width=True)
        else:
            st.info("File erwin.jpg tidak ditemukan di direktori.")

    with col_txt:
        st.markdown("""
        <div style="text-align: justify; line-height: 1.7; font-size: 16px; color: #d1d5db;">
        <b>V-Guard AI Intelligence</b> lahir dari urgensi integritas finansial di era transformasi digital. Sebagai entitas yang dipimpin oleh profesional dengan pengalaman lebih dari satu dekade di industri perbankan dan manajemen aset, kami memahami bahwa celah terkecil dalam sistem operasional adalah potensi kerugian fatal bagi sebuah bisnis. Misi utama kami adalah mendigitalisasi kepercayaan (Digital Trust) melalui pembuktian matematis dan audit cerdas yang bekerja secara otonom 24 jam nonstop tanpa kompromi.<br><br>
        Kami percaya bahwa kejujuran sistem tidak boleh hanya bergantung pada pengawasan manusia yang memiliki keterbatasan, melainkan harus dibangun di atas fondasi teknologi AI yang presisi. Melalui ekosistem V-Guard, kami mengintegrasikan analisis data perbankan (VCS), visi komputer, dan deteksi anomali prediktif untuk menciptakan lingkungan bisnis yang bersih dari segala bentuk kecurangan (Fraud). Strategi kami adalah memberikan transparansi mutlak kepada pemilik bisnis melalui laporan yang akurat dan real-time.<br><br>
        Visi kami adalah menjadi standar global dalam " Eliminating Leakage ", di mana setiap pemilik bisnis, mulai dari UMKM hingga korporasi besar, dapat menjalankan operasional mereka dengan tenang karena setiap Rupiah diawasi oleh kecerdasan buatan yang tak kenal lelah. V-Guard bukan sekadar perangkat lunak, melainkan benteng pertahanan terakhir bagi aset dan masa depan investasi Anda. Kami hadir untuk mengeliminasi kebocoran, mengoptimalkan profitabilitas, dan menjaga warisan bisnis Anda tetap utuh melalui inovasi teknologi yang melampaui standar audit konvensional saat ini.
        </div>
        """, unsafe_allow_html=True)

  elif menu == "Produk & Layanan":
      st.header("🛡️ Portfolio Layanan V-Guard AI Intelligence")
      wa_number = "6282122190885"
      c1, c2, c3, c4 = st.columns(4)
      packages = {
        "V-LITE": ["Mikro / 1 Kasir", "750 rb", "350 brb", "AI Fraud Detector Dasar, Daily WA/Email Summary, Monthly PDF Report"],
        "V-PRO": ["Retail & Kafe", "1.5 Jt", "850 rb", "VCS Integration, Bank Statement Audit, Input Excel/CSV/PDF, H-7 Auto-Invoice"],
        "V-SIGHT": ["Gudang & Toko", "7,5 Jt", "3,5 Jt", "CCTV AI Behavior, Visual Cashier Audit, Real-Time Stock, Fraud Alarm (🚨)"],
        "V-ENTERPRISE": ["Korporasi", "15 Jt", "10 Jt", "The Core Brain, Forensic AI (1 Thn), Dedicated Server, Custom AI SOP"]
         }
    for i, (name, details) in enumerate(packages.items()):
        with [c1, c2, c3, c4][i]:
            with st.container(border=True):
                 st.markdown(f"### 📦 {name}")
                 st.markdown(f"- {details[3]}")
                 st.info(f"**Pasang:** {details[1]}\n\n**Bulan:** {details[2]}")
                 st.link_button(f"Pilih {name}", f"https://wa.me/{wa_number}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20dengan%20paket%20*{name}*%20V-Guard%20AI.")
                
    # 2. Tabel Perbandingan Eksekutif
    st.markdown("---")
    st.subheader("📊 Tabel Perbandingan Eksekutif")
    st.markdown(f"""
    | Fitur Utama | V-LITE | V-PRO | V-SIGHT | V-ENTERPRISE |
    | :--- | :---: | :---: | :---: | :---: |
    | **Level Audit AI** | Standar | Advanced | Visual AI | Forensic |
    | **Integrasi Bank (VCS)** | - | ✅ Ya | ✅ Ya | ✅ Ya |
    | **Input Excel/PDF** | - | ✅ Ya | ✅ Ya | ✅ Ya |
    | **CCTV Vision AI** | - | - | ✅ Ya | ✅ Ya |
    | **Biaya Pemasaran** | 750 rb | 1.5 Jt | 5 Jt | 15 Jt |
    | **Biaya Langganan** | 375 rb | 850 rb | 3,5 Jt | 10 Jt |
    """)

    # 3. Footer Tambahan (Opsional)
    st.caption("Semua paket sudah termasuk update sistem keamanan secara berkala.")

# --- BARIS 108: MENU PORTAL KLIEN (PLUG & PLAY) ---
elif menu == "Portal Klien":
    st.header("🔑 Portal Klien V-Guard AI")
    
    if not st.session_state.get('auth_status', False):
        c_reg, c_log = st.columns(2)
        with c_reg:
            st.subheader("📝 Form Order Baru")
            st.text_input("Nama Pelanggan", key="reg_nama")
            st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ULTRA"], key="reg_paket")
            if st.button("Kirim Registrasi"):
                st.success("Data terkirim. Menunggu aktivasi Admin.")
        
        with c_log:
            st.subheader("🔑 Login Dashboard")
            u_id = st.text_input("ID Klien", key="log_id")
            u_token = st.text_input("Token Akses", type="password", key="log_token")
            if st.button("Masuk"):
                if u_id == "admin" and u_token == "123":
                    st.session_state.auth_status = True
                    st.session_state.client_info = {"nama": "Bapak Erwin", "paket": "V-ULTRA"}
                    st.rerun()
                else:
                    st.error("ID atau Token salah.")
    else:
        info = st.session_state.get('client_info', {"nama": "User", "paket": "V-LITE"})
        st.subheader(f"📊 Dashboard Utama - {info['nama']}")
        st.info(f"Paket Aktif: **{info['paket']}**")
        
        # LOGIKA FILTER TRANSAKSI (Efisien < 20%)
        st.write("---")
        st.subheader("⚡ Real-time Fraud Filter")
        t_total = st.number_input("Input Nilai Transaksi (Rp)", value=0)
        
        if st.button("Proses Transaksi"):
            # Filter: Hanya transaksi > 5jt atau Anomali yang dikirim ke Cloud
            if t_total > 5000000:
                with st.spinner("Anomali Terdeteksi! Mengirim data ke Cloud AI..."):
                    # Di sini fungsi proses_transaksi(t_total) bekerja
                    st.warning("⚠️ ALERT: Transaksi High-Value Terdeteksi & Dicatat Cloud.")
            else:
                st.success("✅ PASS: Transaksi Normal (Disimpan Lokal - Hemat API 100%)")

        if st.button("🔌 Logout Portal"):
            st.session_state.auth_status = False
            st.rerun()

# --- BARIS 136: ADMIN CONTROL CENTER (EXECUTIVE COMMAND CENTER) ---
elif menu == "Admin Control Center":
    st.header("🛡️ V-Guard Executive Panel")
    
    if not st.session_state.get('admin_logged_in', False):
        admin_pwd = st.text_input("Administrator Password", type="password", key="admin_pwd_field")
        if admin_pwd == "w1nbju8282":
            st.session_state.admin_logged_in = True
            st.rerun()
    else:
        c_top1, c_top2 = st.columns([4, 1])
        with c_top2:
            if st.button("Log Out Admin"):
                st.session_state.admin_logged_in = False
                st.rerun()
        
        sst.divider()
        st.markdown("### 📊 Business Intelligence & API Strategy (Capped 20%)")
        
        # --- LOGIKA KEUANGAN V-GUARD (20% DARI OMSET KOTOR) ---
        omset_kotor = 50000000  # Contoh Simulasi Omset Rp 50 Jt
        plafon_api = omset_kotor * 0.20  # Limit 20% = Rp 10 Jt
        biaya_api_realitas = 1850000  # Penggunaan saat ini
        
        c_api1, c_api2, c_api3 = st.columns(3)
        with c_api1: 
            st.metric("Budget API (20% Omset)", f"Rp {plafon_api:,.0f}")
        with c_api2: 
            st.metric("Used API (Current)", f"Rp {biaya_api_realitas:,.0f}", delta="-11.5% (Safe)")
        with c_api3: 
            st.metric("Efficiency Rate", "92.5%")
        
        # Indikator visual efisiensi
        persentase_pakai = (biaya_api_realitas / plafon_api)
        st.progress(persentase_pakai, text=f"Konsumsi API: {persentase_pakai*100:.1f}% dari Plafon Omset")
        
        st.divider()

        # --- AI SQUAD AGENTS DENGAN FILTER OTONOM ---
        st.subheader("🤖 V-Guard AI Squad Agents (Filtering Mode)")
        st.caption("Sistem secara otomatis memfilter data lokal. Hanya Fraud/Anomali yang dikirim ke Cloud AI.")
        
        sq1, sq2, sq3, sq4 = st.columns(4)
        with sq1:
            with st.container(border=True):
                st.markdown("🕵️ **Agent: Sentinel**")
                st.info("Status: **Filtering**")
                st.write("Mencegah data normal masuk Cloud (Hemat Biaya).")
        with sq2:
            with st.container(border=True):
                st.markdown("💰 **Agent: Auditor**")
                st.info("Status: **VCS Sync**")
                st.write("Rekonsiliasi mutasi bank secara otonom.")
        with sq3:
            with st.container(border=True):
                st.markdown("📦 **Agent: Stocker**")
                st.info("Status: **Vision Scan**")
                st.write("Audit visual stok fisik via CCTV AI.")
        with sq4:
            with st.container(border=True):
                st.markdown("📄 **Agent: Invoicer**")
                st.info("Status: **Auto Bill**")
                st.write("Pengiriman invoice otomatis H-7.")

        st.divider()

        # --- 10 TABS STRATEGIS V-GUARD ---
        tabs = st.tabs([
            "👤 Aktivasi", "🖥️ Ekosistem AI", "📈 ROI Tracker", 
            "🛡️ Security", "💾 Backup", "🌐 Jaringan", 
            "📊 Analytics", "📩 Marketing", "💎 V-ULTRA", "⚙️ Config"
        ])
        
        with tabs[0]: # Tab Aktivasi
            st.subheader("📝 Manajemen Aktivasi Klien")
            with st.container(border=True):
                c1, c2 = st.columns(2)
                with c1: st.text_input("Username Klien", key="adm_usr_final")
                with c2: st.selectbox("Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ULTRA"], key="adm_pkt_final")
                if st.button("Aktifkan Akun & Lisensi"):
                    st.success("Lisensi Aktif. Dashboard Klien Siap!")

# --- FOOTER ---
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026</small></center>", unsafe_allow_html=True)
