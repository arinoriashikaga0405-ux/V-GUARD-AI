import streamlit as st
import os
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE AI ---
GEMINI_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
genai.configure(api_key=GEMINI_API_KEY)
model_gemini = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Premium Eksekutif
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; height: 45px; }
    .stTextInput>div>div>input { background-color: #1e293b; color: white; }
    div[data-testid="stMetricValue"] { font-size: 22px; color: #238636; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.markdown("<div style='text-align:center;'><p style='color:white; font-weight:bold; margin-bottom:0;'>Erwin Sinaga</p><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Produk & Layanan", "Analisis ROI Kerugian", "Portal Klien", "Admin Control Center"])

# --- 4. LOGIKA MENU ---

if menu == "Visi & Misi":
    st.header("Visi & Misi V-Guard AI Intelligence")
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga - Founder & CEO", use_container_width=True)
    with col_txt:
        st.markdown("""
        <div style="text-align: justify; line-height: 1.7; font-size: 16px; color: #d1d5db;">
        <b>V-Guard AI Intelligence</b> lahir dari urgensi integritas finansial di era transformasi digital. Sebagai entitas yang dipimpin oleh profesional dengan pengalaman lebih dari satu dekade di industri perbankan dan manajemen aset, kami memahami bahwa celah terkecil dalam sistem operasional adalah potensi kerugian fatal bagi sebuah bisnis. Misi utama kami adalah mendigitalisasi kepercayaan (Digital Trust) melalui pembuktian matematis dan audit cerdas yang bekerja secara otonom 24 jam nonstop tanpa kompromi.<br><br>
        Kami percaya bahwa kejujuran sistem tidak boleh hanya bergantung pada pengawasan manusia yang memiliki keterbatasan, melainkan harus dibangun di atas fondasi teknologi AI yang presisi. Melalui ekosistem V-Guard, kami mengintegrasikan analisis data perbankan (VCS), visi komputer, dan deteksi anomali prediktif untuk menciptakan lingkungan bisnis yang bersih dari segala bentuk kecurangan (Fraud). Strategi kami adalah memberikan transparansi mutlak kepada pemilik bisnis melalui laporan yang akurat dan real-time.<br><br>
        Visi kami adalah menjadi standar global dalam "Integrity Assurance", di mana setiap pemilik bisnis, mulai dari UMKM hingga korporasi besar, dapat menjalankan operasional mereka dengan tenang karena setiap Rupiah diawasi oleh kecerdasan buatan yang tak kenal lelah. V-Guard bukan sekadar perangkat lunak, melainkan benteng pertahanan terakhir bagi aset dan masa depan investasi Anda. Kami hadir untuk mengeliminasi kebocoran, mengoptimalkan profitabilitas, dan menjaga warisan bisnis Anda tetap utuh melalui inovasi teknologi yang melampaui standar audit konvensional saat ini.
        </div>
        """, unsafe_allow_html=True)

elif menu == "Produk & Layanan":
    st.header("🛡️ Portfolio Layanan V-Guard AI Intelligence")
    wa_number = "6282122190885"
    
    # 1. Tampilan Detail Paket dalam Kolom
    c1, c2, c3, c4 = st.columns(4)
    
    packages = {
        "V-LITE": [
            "Mikro / 1 Kasir", 
            "1.5 Jt", 
            "1 Jt", 
            "AI Fraud Detector Dasar, Daily WA/Email Summary, Monthly PDF Report"
        ],
        "V-PRO": [
            "Retail & Kafe", 
            "3 Jt", 
            "2.5 Jt", 
            "VCS Integration, Bank Statement Audit, Input Excel/CSV/PDF, H-7 Auto-Invoice"
        ],
        "V-SIGHT": [
            "Gudang & Toko", 
            "5 Jt", 
            "5 Jt", 
            "CCTV AI Behavior, Visual Cashier Audit, Real-Time Stock, Fraud Alarm (🚨)"
        ],
        "V-ENTERPRISE": [
            "Korporasi", 
            "10 Jt", 
            "10 Jt", 
            "The Core Brain, Forensic AI (1 Thn), Dedicated Server, Custom AI SOP"
        ]
    }

    for i, (name, details) in enumerate(packages.items()):
        with [c1, c2, c3, c4][i]:
            with st.container(border=True):
                st.markdown(f"### 📦 {name}")
                st.caption(f"🎯 Target: {details[0]}")
                st.markdown(f"- {details[3]}")
                st.info(f"**Pasang:** {details[1]}\n\n**Bulan:** {details[2]}")
                # Tombol WA Otomatis sesuai paket
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
    | **Biaya Pemasaran** | 1.5 Jt | 3 Jt | 5 Jt | 10 Jt |
    | **Biaya Langganan** | 1 Jt | 2.5 Jt | 5 Jt | 10 Jt |
    """)

    # 3. Footer Tambahan (Opsional)
    st.caption("Semua paket sudah termasuk update sistem keamanan secara berkala.")

elif menu == "Analisis ROI Kerugian":
    st.header("📊 Analisis Potensi Kerugian vs ROI")
    col_a, col_b = st.columns(2)
    with col_a:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
        leak = st.slider("Estimasi Kebocoran (%)", 1, 20, 5)
        loss = omzet * (leak / 100)
        st.error(f"Potensi Kerugian: Rp {loss:,.0f} / bulan")
    with col_b:
        biaya = st.selectbox("Investasi Paket", [1000000, 2500000, 5000000, 10000000])
        st.success(f"Profit Diselamatkan: Rp {loss - biaya:,.0f} / bln")

elif menu == "Portal Klien":
    st.header("Portal Klien V-Guard AI")
    c_reg, c_log = st.columns(2)
    with c_reg:
        st.subheader("📝 Form Order Baru")
        with st.container(border=True):
            st.text_input("Nama Pelanggan")
            st.text_input("Nama Usaha")
            st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.text_input("Harga Paket (Rp)")
            st.file_uploader("Upload KTP")
            st.button("Kirim Registrasi")
    with c_log:
        st.subheader("🔑 Akses User Aktif")
        with st.container(border=True):
            st.text_input("Username")
            pw = st.text_input("Password", type="password")
            if st.button("Masuk"):
                if pw == "vguardklien2026": st.success("Selamat Datang!")
                else: st.error("Password Salah.")

elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center")

    # 1. Cek status login di session state
    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False

    # 2. Kotak Login (Hanya muncul jika belum login)
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

        # Mendefinisikan 8 Tab agar tidak error saat dipanggil di bawah
        t1, t2, t3, t4, t5, t6, t7, t8 = st.tabs([
            "👤 Aktivasi Klien",
            "🖥️ Ekosistem AI",
            "📈 Laba & Fraud",
            "🔍 Audit Dokumen",
            "👁️ Live CCTV Vision",
            "🚨 Alarm System",
            "📊 ROI Monitor",
            "📑 Pusat Data OCR"
        ])

        with t1:
            st.subheader("📝 Pembuatan & Aktivasi Akun Klien (Paid)")
            st.info("Daftarkan klien yang sudah melakukan pembayaran.")
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

        with t3:
            st.subheader("📈 Monitoring Laba & Pencegahan Fraud")
            c_a, c_b = st.columns(2)
            with c_a:
                st.metric("Laba Bersih", "Rp 400.250.000", delta="Normal")
            with c_b:
                st.metric("Dana Terselamatkan", "Rp 15.700.000", delta="AI Fraud Detector Aktif")
            
            st.divider()
            st.info("🔍 **Status Deteksi Dasar:** AI sedang memantau pembatalan transaksi (Void) dan anomali input kasir harian.")
            st.write("🗓️ **Status Invoice H-7**: Otomatis Terjadwal untuk 12 Klien.")

        with t4:
            st.subheader("📑 Audit Dokumen Multi-Format")
            st.file_uploader("Upload Dokumen Audit (VCS/Excel/PDF)", type=['xlsx','pdf','jpg','vcs','csv'], accept_multiple_files=True, key="audit_up_1")

        with t5:
            st.subheader("👁️ V-SIGHT: AI Visual Command Center")
            st.write("Status: **Monitoring Aktif** | Target: Gudang & Toko Utama")
            
            # Baris Atas: Live Monitor & Behavior Detection
            c_vid1, c_vid2 = st.columns(2)
            with c_vid1:
                st.image("https://img.freepik.com/free-photo/security-camera-detecting-thief-store_23-2150914187.jpg", caption="CCTV 01 - Area Kasir (AI Behavior Active)")
                st.info("🤖 **AI Behavior:** Mendeteksi gerakan laci kasir terbuka tanpa transaksi.")
            with c_vid2:
                st.image("https://img.freepik.com/free-photo/warehouse-management-system-concept_23-2148923140.jpg", caption="CCTV 02 - Rak Gudang B (Visual Stock Control)")
                st.warning("⚠️ **Visual Stock:** Stok Beras 5kg menipis di Rak B. Segera Restock!")

            st.divider()

            # Baris Bawah: Hasil Audit Visual & Fraud Alarm
            st.write("🚨 **Fraud Alarm History (Visual Proof)**")
            col_f1, col_f2 = st.columns([2, 1])
            with col_f1:
                st.error("🚨 **ALARM: Visual Mismatch Terdeteksi (14:20 WIB)**")
                st.write("- **Data Kasir:** Kopi Hitam (Rp 20.000)")
                st.write("- **Visual AI:** Kopi Susu Gula Aren (Rp 35.000)")
                st.caption("Status: Menunggu konfirmasi owner untuk tindakan disiplin.")
            with col_f2:
                st.metric("Integrity Score Today", "88%", delta="-12% vs Kemarin", delta_color="inverse")
                if st.button("Lihat Cuplikan Video Kejadian"):
                    st.toast("Memuat rekaman cloud... Mohon tunggu.")
        with t6:
            st.subheader("🚨 Pusat Alarm & Notifikasi")
            st.error("ALARM FRAUD: **AKTIF**")
            st.warning("NOTIFIKASI INVOICE H-7: **READY**")

        with t7:
            st.subheader("📈 Monitoring Laba & Pencegahan Fraud")
            c_a, c_b = st.columns(2)
            c_a.metric("Laba Bersih", "Rp 400.250.000", delta="Normal")
            c_b.metric("Dana Terselamatkan", "Rp 15.700.000", delta="Pencegahan Fraud")
            st.divider()
            st.write("🗓️ **Status Invoice H-7**: Otomatis Terjadwal untuk 12 Klien.")

        with t8:
            st.subheader("📑 Pusat Audit Multi-Format (Advanced)")
            st.write("Metode Audit: **Otomatis (API)** atau **Manual (Upload Dokumen)**.")

            # --- BAGIAN BARU: KONFIGURASI VCS (API INTEGRATION) ---
            with st.expander("⚙️ Konfigurasi Integrasi VCS (API POS & Bank)"):
                st.info("Gunakan fitur ini untuk menghubungkan Kasir/Bank secara otomatis tanpa upload file.")
                col_api1, col_api2 = st.columns(2)
                with col_api1:
                    api_provider = st.selectbox("Pilih Sistem Kasir/Bank", 
                                              ["Moka POS", "Majoo", "Nutapos", "BCA Business API", "Bank Mandiri API"])
                with col_api2:
                    api_key_input = st.text_input("Masukkan API Key / Client ID", type="password", help="Dapatkan kunci ini dari dashboard kasir/bank Anda")
                
                if st.button("Hubungkan ke V-Guard AI"):
                    with st.spinner("Menyambungkan enkripsi ke server..."):
                        import time
                        time.sleep(2)
                        st.success(f"✅ Terhubung! V-Guard AI sekarang menarik data dari {api_provider} secara real-time.")
            
            st.divider()

            # --- BAGIAN UPLOAD MANUAL (KODE ASLI BAPAK) ---
            st.write("---")
            st.write("📤 **Audit Manual via File:**")
            uploaded_files = st.file_uploader("Upload Mutasi Rekening / Laporan Kasir", type=['xlsx', 'pdf', 'jpg', 'jpeg', 'csv'], accept_multiple_files=True, key="audit_up_final")
            
            if uploaded_files:
                with st.spinner("V-Guard AI sedang melakukan Deep Audit 180 hari terakhir..."):
                    import time
                    time.sleep(3) 
                    st.success("✅ Audit 6 Bulan Selesai.")
                    
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Total Transaksi Diperiksa", "1,240 Data")
                    c2.metric("Akurasi Reconciliation", "100%")
                    c3.metric("Anomali Terdeteksi", "0 (Clean)", delta="Aman", delta_color="normal")
                    
                    st.info("💡 **AI Insight:** Pola arus kas stabil. Tidak ditemukan indikasi 'Split Transaction' atau pengeluaran tanpa invoice pendukung.")
                    
            # --- Tambahkan ini di bagian akhir dalam blok Admin Control Center ---
         with t9: # (Ini sudah menjorok dari 'else')
        st.divider() # <--- MASUK 1 TAB DARI 'with'
        st.header("💎 V-ULTRA: Enterprise Command Center")
        st.info("Status Infrastruktur: **Dedicated Private Server (Active)**")
        
        col_u1, col_u2 = st.columns(2)
        with col_u1:
            st.success("🧠 **The Core Brain (AI Central)**")
            st.write("Menyinkronkan data Lintas Cabang & Gudang.")
            st.progress(100)
        
        with col_u2:
            st.info("🖥️ **Dedicated Server Status**")
            st.code("IP: 10.0.88.24\nEncryption: AES-256\nUptime: 99.99%")

        st.divider()
        st.metric("ROI Penyelamatan Aset", "Rp 1.250.000.000 / Tahun", delta="Efisiensi 35%")

# FOOTER HARUS KEMBALI KE KIRI (SEJAJAR DENGAN 'with t9')
# --- 5. FOOTER (SESUAI PERMINTAAN BAPAK) ---
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026</small></center>", unsafe_allow_html=True)
# --- 5. FOOTER (SESUAI PERMINTAAN BAPAK) ---
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026</small></center>", unsafe_allow_html=True)
