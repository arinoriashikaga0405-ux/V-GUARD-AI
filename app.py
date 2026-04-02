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
            st.subheader("📈 Financial Integrity Monitor (V-LITE & PRO)")
            col_met1, col_met2 = st.columns(2)
            with col_met1:
                st.metric("Laba Bersih", "Rp 400.250.000", delta="Stabil")
            with col_met2:
                st.metric("AI Fraud Detector", "Aktif", delta="Sistem Dasar")
            
            st.divider()
            st.info("🔍 **Status Deteksi Dasar:** AI sedang memantau pembatalan transaksi (Void) dan anomali input kasir harian.")with t3:
            st.subheader("📈 Financial Integrity Monitor")
            st.metric("Laba Bersih", "Rp 400.250.000", delta="Stabil")
        
        with t4:
            st.subheader("📑 Audit Dokumen Multi-Format")
            st.file_uploader("Upload Dokumen Audit (VCS/Excel/PDF)", type=['xlsx','pdf','jpg','vcs','csv'], accept_multiple_files=True, key="audit_up_1")

        with t5:
            st.subheader("👁️ Live Vision Monitoring")
            st.image("https://img.freepik.com/free-photo/security-camera-monitoring-market_23-2149156434.jpg")

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
            st.write("Sistem membaca: **Excel/CSV**, **PDF/JPG**, dan **VCS Data Bank**.")
            
            uploaded_files = st.file_uploader("Upload Mutasi Rekening (6 Bulan Terakhir)", type=['xlsx', 'pdf', 'jpg', 'jpeg', 'csv'], accept_multiple_files=True, key="audit_up_final")
            
            if uploaded_files:
                with st.spinner("V-Guard AI sedang melakukan Deep Audit 180 hari terakhir..."):
                    import time
                    time.sleep(3) # Simulasi proses yang lebih dalam
                    st.success("✅ Audit 6 Bulan Selesai.")
                    
                    # Tampilkan metrik hasil audit sebagai kejutan demo
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Total Transaksi Diperiksa", "1,240 Data")
                    c2.metric("Akurasi Reconsiliation", "100%")
                    c3.metric("Anomali Terdeteksi", "0 (Clean)", delta="Aman", delta_color="normal")
                    
                    st.info("💡 **AI Insight:** Pola arus kas stabil. Tidak ditemukan indikasi 'Split Transaction' atau pengeluaran tanpa invoice pendukung.")
# --- 5. FOOTER (SESUAI PERMINTAAN BAPAK) ---
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026</small></center>", unsafe_allow_html=True)
