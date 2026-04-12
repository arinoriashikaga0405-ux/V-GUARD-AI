import streamlit as st
import os
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE & SECURITY ---
GEMINI_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
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
    st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")
# --- DI BARIS 23 ---
if "auth_status" not in st.session_state: 
    st.session_state.auth_status = False

if "client_info" not in st.session_state:
    st.session_state.client_info = None
    st.markdown("""
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
    st.header("Visi & Misi Digitizing Trust, Eliminating Leakage")
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

elif menu == "ROI Kerugian Klien":
    st.header("📊 Analisis Potensi Kerugian vs ROI")
    col_a, col_b = st.columns(2)
    with col_a:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
        leak = st.slider("Estimasi Kebocoran (%)", 1, 20, 5)
        loss = omzet * (leak / 100)
        st.error(f"Potensi Kerugian: Rp {loss:,.0f} / bulan")

eelif menu == "Portal Klien":
    st.header("Portal Klien V-Guard AI")
    
    # URL Google Sheets Bapak
    url_cloud = "https://docs.google.com/spreadsheets/d/1SWK7sELm1jvnu7Mw3srrpqAMFaG8XfcvY1dWKZzzYZg/edit"

    if not st.session_state.auth_status:
        c_reg, c_log = st.columns(2)
        
        with c_reg:
            st.subheader("📝 Registrasi & Order")
            with st.container(border=True):
                  nama = st.text_input("Nama Pelanggan")
                  usaha = st.text_input("Nama Usaha")
                  paket = st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
                
                if st.button("Kirim Registrasi"):
                    try:
                        from streamlit_gsheets import GSheetsConnection
                        conn = st.connection("gsheets", type=GSheetsConnection)
                        # Data dikirim ke Excel dengan status 'Waiting Activation'
                        new_data = pd.DataFrame([{"Nama": nama, "Usaha": usaha, "Paket": paket, "Status": "Waiting Activation"}])
                        conn.create(spreadsheet=url_cloud, data=new_data)
                        st.success("✅ Terdaftar di Cloud! Silakan hubungi Admin untuk aktivasi.")
                    except:
                        st.error("Gagal koneksi ke Cloud Excel.")

        with c_log:
            st.subheader("🔑 Login Klien")
            with st.container(border=True):
                u_user = st.text_input("ID Klien (Nama)")
                u_pass = st.text_input("Token / Password", type="password")
                
                if st.button("Connect to Dashboard"):
                    try:
                        from streamlit_gsheets import GSheetsConnection
                        conn = st.connection("gsheets", type=GSheetsConnection)
                        df_cloud = conn.read(spreadsheet=url_cloud)
                        
                        # Cek apakah User ada, Password 'vguardklien2026', dan Status 'Aktif'
                        check = df_cloud[(df_cloud['Nama'] == u_user) & (df_cloud['Status'] == 'Aktif')]
                        
                        if not check.empty and u_pass == "vguardklien2026":
                            st.session_state.auth_status = True
                            st.session_state.client_info = check.iloc[0].to_dict()
                            st.rerun()
                        else:
                            st.warning("Akses Ditolak. Pastikan status Akun 'Aktif' di Excel Admin.")
                    except:
                        st.error("Gagal verifikasi Cloud.")

    # --- TAMPILAN DASHBOARD (JIKA SUDAH AKTIF) ---
    else:
        info = st.session_state.client_info
        st.subheader(f"📊 Dashboard {info['Paket']} - {info['Nama']}")
        st.write(f"Selamat Datang, data Anda terhubung langsung ke Cloud Server.")
        
        # Dashboard Spesifik Paket
        st.info(f"Fitur Khusus {info['Paket']} telah diaktifkan oleh Admin.")
        
        if st.button("🔌 Logout"):
            st.session_state.auth_status = False
            st.rerun()

elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center")

    # 1. Cek status login di session state
    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False

    # 2. Kotak Login
    if not st.session_state.admin_logged_in:
        admin_input = st.text_input("Administrator Password", type="password", key="admin_pwd_field")
        if admin_input == "w1nbju8282":
            st.session_state.admin_logged_in = True
            st.rerun()
        elif admin_input != "":
            st.error("Password Salah. Akses Ditolak.")
    
    # 3. Dashboard Admin (Muncul setelah password benar)
    else:
        col_header, col_logout = st.columns([5, 1])
        with col_header:
            st.success("Akses Eksekutif Aktif")
        with col_logout:
            if st.button("Log Out"):
                st.session_state.admin_logged_in = False
                st.rerun()

        # --- FITUR BARU: MONITORING BIAYA API & AI SQUAD ---
        st.markdown("### 📊 Ringkasan Eksekutif & AI Squad")
        
        # Panel Biaya API & Efisiensi
        c_api1, c_api2, c_api3 = st.columns(3)
        with c_api1:
            st.metric("Anggaran API Bulanan", "Rp 10.000.000")
        with c_api2:
            # Simulasi biaya terpakai (contoh 1.2jt dari 10jt = 12%)
            st.metric("Biaya API Terpakai", "Rp 1.200.000", delta="-15% (Hemat)", delta_color="normal")
        with c_api3:
            st.metric("Efisiensi Sistem", "88%", delta="Target > 80%")
        
        st.progress(0.12, text="Penggunaan Kuota API Cloud: 12%")

        st.divider()

        # UI untuk AI Squad Agent
        st.subheader("🤖 V-Guard AI Squad Agents")
        st.caption("Agen AI otonom yang bekerja mengawasi ekosistem bisnis Anda 24/7.")
        
        sq1, sq2, sq3, sq4 = st.columns(4)
        with sq1:
            with st.container(border=True):
                st.markdown("🕵️ **Agent: Sentinel**")
                st.caption("Status: Memantau Fraud")
                st.write("Menganalisa anomali transaksi kasir.")
        with sq2:
            with st.container(border=True):
                st.markdown("💰 **Agent: Auditor**")
                st.caption("Status: VCS Sync")
                st.write("Sinkronisasi mutasi bank & laporan POS.")
        with sq3:
            with st.container(border=True):
                st.markdown("📦 **Agent: Stocker**")
                st.caption("Status: Visual Check")
                st.write("Cek stok fisik gudang melalui CCTV AI.")
        with sq4:
            with st.container(border=True):
                st.markdown("📄 **Agent: Invoicer**")
                st.caption("Status: H-7 Ready")
                st.write("Otomatisasi pengiriman invoice klien.")

        st.divider()

        # Tab Menu Admin
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = st.tabs([
            "👤 Aktivasi Klien", "🖥️ Ekosistem AI", "⚙️ Pengaturan", "📊 Laporan", 
            "🛡️ Keamanan", "💾 Backup", "🌐 Jaringan", "📈 Performa", "💎 V-ULTRA"
        ])

        with t1:
            st.subheader("📝 Pembuatan & Aktivasi Akun Klien (Paid)")
            with st.container(border=True):
                col1, col2 = st.columns(2)
                with col1:
                    new_user = st.text_input("Username Klien")
                    new_mail = st.text_input("Email Bisnis")
                with col2:
                    paket_pilihan = st.selectbox("Paket yang Dibayar", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
                    tgl_bayar = st.date_input("Tanggal Pembayaran")
                if st.button("Aktifkan Akun & Kirim Kredensial"):
                    st.success(f"Akun {new_user} paket {paket_pilihan} BERHASIL DIAKTIFKAN.")

        with t2:
            st.subheader("🌐 V-Guard Global AI Ecosystem")
            c1, c2 = st.columns(2)
            with c1:
                with st.container(border=True):
                    st.markdown("### 🧠 Google Gemini AI")
                    st.write("Analis utama yang memproses data audit kompleks.")
            with c2:
                with st.container(border=True):
                    st.markdown("### 👁️ YOLO / Vision AI")
                    st.write("'Mata' digital yang memantau pergerakan visual.")

        # Tab-tab lainnya tetap menggunakan kode asli Anda
        with t5:
            st.subheader("👁️ V-SIGHT: AI Visual Command Center")
            c_vid1, c_vid2 = st.columns(2)
            with c_vid1:
                st.image("https://img.freepik.com/free-photo/security-camera-detecting-thief-store_23-2150914187.jpg", caption="CCTV 01 - Area Kasir")
            with c_vid2:
                st.image("https://img.freepik.com/free-photo/warehouse-management-system-concept_23-2148923140.jpg", caption="CCTV 02 - Rak Gudang")

        with t9:
            st.header("💎 V-ULTRA: Enterprise Command Center")
            col_u1, col_u2 = st.columns(2)
            with col_u1:
                st.success("🧠 **The Core Brain (AI Central)**")
                st.progress(100)
            with col_u2:
                st.info("🖥️ **Dedicated Server Status**")
                st.code("IP: 10.0.88.24\nUptime: 99.99%")
            st.divider()
            st.metric("ROI Penyelamatan Aset", "Rp 1.250.000.000 / Tahun", delta="Efisiensi 35%")

        st.markdown("---")
        st.markdown("<center><small>V-Guard AI Intelligence | ©2026</small></center>", unsafe_allow_html=True)
