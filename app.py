import streamlit as st
import os
import google.generativeai as genai
# --- 1. KONFIGURASI ENGINE AI ---
from dotenv import load_dotenv
load_dotenv() # Ini perintah untuk membaca file .env

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model_gemini = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")
# --- 1.1 FUNGSI PUSAT 10 AI AGENT V-GUARD ---
def vguard_ai_engine(agent_name, task_instruction, context_data=""):
    """Fungsi tunggal untuk memanggil 10 Agent V-GUARD"""
    system_prompt = f"""
    ROLE: Anda adalah {agent_name} dari V-GUARD AI Squad.
    INSTRUKSI KHUSUS: {task_instruction}
    KONTEKS DATA: {context_data}
    STYLE: Profesional, tegas, fokus pada integritas & profit.
    Hapus semua penyebutan pihak ketiga, gunakan identitas V-GUARD AI.
    """
    response = model_gemini.generate_content(system_prompt)
    return response.text
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
            "750 rb", 
            "AI Fraud Detector Dasar, Daily WA/Email Summary, Monthly PDF Report"
        ],
        "V-PRO": [
            "Retail & Kafe", 
            "3 Jt", 
            "1.5 Jt", 
            "VCS Integration, Bank Statement Audit, Input Excel/CSV/PDF, H-7 Auto-Invoice"
        ],
        "V-SIGHT": [
            "Gudang & Toko", 
            "7,5 Jt", 
            "3,5 Jt", 
            "CCTV AI Behavior, Visual Cashier Audit, Real-Time Stock, Fraud Alarm (🚨)"
        ],
        "V-ENTERPRISE": [
            "Korporasi", 
            "15 Jt", 
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
    | **Biaya Pemasaran** | 1.5 Jt | 3 Jt | 5 Jt | 15 Jt |
    | **Biaya Langganan** | 750 rb | 1.5 Jt | 3,5 Jt | 10 Jt |
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
            opsi_biaya = {
                "Rp 1.000.000 (V-LITE)": 1000000,
                "Rp 2.500.000 (V-STANDARD)": 2500000,
                "Rp 5.000.000 (V-PRO)": 5000000,
                "Rp 10.000.000 (V-ULTRA)": 10000000
                    }
        pilihan_label = st.selectbox("Pilih Paket Investasi", list(opsi_biaya.keys()))
        biaya = opsi_biaya[pilihan_label]
        st.success(f"💰 Profit Diselamatkan: Rp {loss - biaya:,.0f} / bln")

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
    # --- 1. PENGUNCI FOLDER (FOLDER LOCK) ---
    if not st.session_state.get('admin_logged_in', False):
        st.subheader("🔐 V-GUARD Secure Folder")
        admin_input = st.text_input("Password Folder:", type="password", key="vguard_folder_lock")
        if admin_input == "w1nbju8282": 
            st.session_state.admin_logged_in = True
            st.rerun()
        elif admin_input != "":
            st.error("Password Salah.")
        st.stop() 

    else: 
        # Header & Tombol Lock
        c_out1, c_out2 = st.columns([9, 1])
        with c_out2:
            if st.button("🔒 Lock", key="logout_btn"):
                st.session_state.admin_logged_in = False
                st.rerun()
        
        st.header("🎮 V-GUARD: Admin Control Center")
        st.divider()

        # CSS GLOBAL: Tombol Putih & Tag Status
        st.markdown("""
            <style>
            div.stButton > button { background-color: white !important; color: black !important; border: 1px solid #dcdcdc !important; border-radius: 4px; font-weight: 500; }
            .status-tag { padding: 2px 8px; border-radius: 10px; font-size: 0.75rem; font-weight: bold; border: 1px solid #dcdcdc; }
            </style>
        """, unsafe_allow_html=True)

        # 10 TAB EKSEKUTIF
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10 = st.tabs([
            "👥 Aktivasi", "🖥️ AI Squad", "⚙️ Integrasi", 
            "📊 Audit", "🛡️ V-SIGHT", "🚨 Alarm", 
            "📈 Profit", "💾 Backup", "💎 V-ULTRA", "👑 Owner"
        ])

        # --- TAB 1: CLIENT MANAGEMENT & BILLING ---
        with t1:
            st.subheader("👥 Client Management & Account Activation")
            
            # Form Input Data
            ca, cb = st.columns(2)
            with ca:
                nama_k = st.text_input("Nama Perusahaan:", key="nk_t1")
                wa_k = st.text_input("WhatsApp (62...):", key="wa_t1", help="Gunakan format 628xxx")
            with cb:
                prod_v = st.selectbox("Produk:", ["🛡️ V-LITE", "👁️ V-PRO", "🚨 V-SIGHT", "💎 V-ULTRA"], key="prod_t1")
                tgl_exp = st.date_input("Tanggal Jatuh Tempo", key="tgl_t1")

            # Tombol Aktivasi Utama
            if st.button("🚀 Aktivasi & Buat Akun Klien", key="btn_act_clean"):
                if nama_k and wa_k:
                    # Simulasi Pembuatan Akun Otomatis
                    username_client = nama_k.lower().replace(" ", "") + "_vguard"
                    pass_client = "VG-" + wa_k[-4:] # Password default 4 digit terakhir WA
                    
                    st.success(f"✅ Akun untuk {nama_k} Berhasil Dibuat!")
                    
                    # Kotak Informasi Akun untuk dikirim ke Klien
                    st.markdown(f"""
                    > **🔑 KREDENSIAL LOGIN KLIEN:**
                    > * **Portal:** `https://v-guard.ai/client-login`
                    > * **Username:** `{username_client}`
                    > * **Password:** `{pass_client}`
                    """)
                    
                    # Fitur Kirim Link via WhatsApp
                    link_akses = f"https://wa.me/{wa_k}?text=Halo%20{nama_k},%20Akun%20V-GUARD%20Anda%20telah%20aktif.%0A%0AUsername:%20{username_client}%0APassword:%20{pass_client}%0ASilakan%20login%20di%20portal%20kami."
                    st.markdown(f'<a href="{link_akses}" target="_blank"><button style="background-color: #25D366; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;">📲 Kirim Link Akses via WhatsApp</button></a>', unsafe_allow_html=True)
                else:
                    st.error("Mohon isi Nama Perusahaan dan WhatsApp terlebih dahulu.")

            # --- FITUR FILE UPLOAD (DOKUMEN KLIEN) ---
            st.divider()
            st.subheader("📁 Client Document & Data Center")
            st.markdown("Unggah bukti bayar atau dokumen legalitas klien di sini.")
            
            uploaded_files = st.file_uploader(
                "Upload Bukti Transfer / PDF Data:", 
                type=['csv', 'jpg', 'jpeg', 'png', 'pdf'], 
                accept_multiple_files=True,
                key="client_file_uploader"
            )

            if uploaded_files:
                for uploaded_file in uploaded_files:
                    st.write(f"📄 **File:** {uploaded_file.name}")
                    if uploaded_file.name.endswith('.pdf'):
                        st.success(f"Analyst Agent: PDF {uploaded_file.name} terekam.")
                    elif uploaded_file.name.endswith(('.jpg', '.jpeg', '.png')):
                        st.image(uploaded_file, width=250)
                
                if st.button("Simpan & Sinkronisasi Dokumen", key="btn_save_docs"):
                    st.toast("Semua file tersimpan di server V-GUARD.")
        # --- TAB 2: AI SQUAD (EKSEKUSI AGENT & 24/7 SERVICE) ---
        with t2:
            st.subheader("🖥️ V-GUARD Elite AI Squad (Eksekusi Agent)")
            cmd_ai = st.text_area("Instruksi Operasional:", placeholder="Misal: Jalankan kampanye digital marketing untuk minggu depan...")
            
            if st.button("Jalankan Operasi AI Agent"):
                if cmd_ai:
                    with st.spinner("AI Squad sedang bekerja..."):
                        res = vguard_ai_engine("COMMANDER", cmd_ai)
                        st.info(res)

            st.divider()
            st.markdown("### 👥 Deployment Status (24/7 Service)")
            # 10 Agent termasuk Concierge 24/7 dan Digital Marketing (Growth)
            agents = [
                ("👁️ Visionary", "CCTV/YOLO", "Online"), ("👂 Concierge", "24/7 Support", "Active"), 
                ("👄 Growth", "Digital Marketing", "Online"), ("🤝 Liaison", "API Bridge", "Online"), 
                ("🧠 Analyst", "Forensic Data", "Processing"), ("📈 Strategist", "Business Plan", "Online"),
                ("🐕 Watchdog", "Fraud Scan", "Online"), ("🛡️ Sentinel", "System Security", "Online"), 
                ("⚖️ Legalist", "Contract/Law", "Idle"), ("💰 Treasurer", "Finance/Billing", "Online")
            ]
            
            for i in range(0, 10, 5):
                cols = st.columns(5)
                for j, (name, task, status) in enumerate(agents[i:i+5]):
                    with cols[j]:
                        st.markdown(f"**{name}**")
                        st.caption(f"`{task}`")
                        st.markdown(f"<span class='status-tag'>{status}</span>", unsafe_allow_html=True)

        # --- TAB 3: INTEGRASI (API KASIR & BANK) ---
        with t3:
            st.subheader("⚙️ Integrasi: API Kasir & Bank Bridge")
            pos_p = st.selectbox("Pilih POS/Bank:", ["Moka POS", "Majoo", "ESB", "BCA Business API"])
            col_api1, col_api2 = st.columns(2)
            with col_api1:
                if st.button("🔗 Hubungkan API"):
                    st.success(f"LIAISON: API {pos_p} Terkoneksi Real-time.")
            with col_api2:
                st.info("**Sync Status:** Last sync 1 menit yang lalu.")

        # --- TAB 4: AUDIT (FORENSIK KEUANGAN) ---
        with t4:
            st.subheader("📊 Audit: Financial Forensic")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                st.date_input("Periode Audit Forensik")
                if st.button("Jalankan Audit Anomali"):
                    st.warning("WATCHDOG: Terdeteksi 2 transaksi void mencurigakan di Cabang A.")
            with col_f2:
                st.metric("Fraud Score", "0.02%", "-0.01%")
                st.file_uploader("Upload Laporan Kasir (.csv)")

        # --- TAB 5: V-SIGHT (VISION AI INTELLIGENCE) ---
        with t5:
            st.subheader("🛡️ V-SIGHT: Visual AI Intelligence (YOLO)")
            st.image("https://img.freepik.com/free-photo/security-camera-detecting-thief-store_23-2150914187.jpg", caption="Live Vision Analytics")
            cv1, cv2, cv3 = st.columns(3)
            with cv1:
                if st.button("Aktifkan YOLO Scanner"):
                    st.success("YOLOv8 Active: Detecting Person & Assets.")
            with cv2:
                if st.button("Generate Heatmap"):
                    st.info("Area teramai: Meja Kasir Utama.")
            with cv3:
                st.button("Capture Security Log")

        # --- TAB 6 s/d 9: FUNGSI OPERASIONAL ---
        with t6:
            st.subheader("🚨 Alarm & WhatsApp Billing")
            if st.button("Kirim Invoice H-7 Otomatis"):
                st.toast("Notifikasi terkirim ke 5 klien.")
        with t7:
            st.subheader("📈 Profit Support Tools")
            st.line_chart([100, 120, 150, 140, 180])
        with t8:
            st.subheader("💾 Cloud Backup Center")
            st.button("Sync Database Sekarang")
       # --- TAB 9: V-ULTRA (NATIONAL COMMAND CENTER & ENTERPRISE SOLUTION) ---
        with t9:
            st.header("💎 V-ULTRA: The Ultimate Enterprise Solution")
            st.markdown("""
                *V-ULTRA: Kontrol penuh Multi-Cabang, Automated Billing Nasional, & Global Security.*
            """)
            
            # 1. Dashboard Ringkasan Nasional
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Total Cabang", "150+", "Nasional")
            m2.metric("Uptime Server", "100%", "Dedicated")
            m3.metric("Security Alerts", "0", "Safe")
            m4.metric("Data Sync Speed", "0.2s", "Real-time")

            st.divider()

            # 2. FITUR ALARM & INVOICE H-7 NASIONAL
            st.subheader("🚨 Enterprise Alarm & Automated Billing")
            col_inv1, col_inv2 = st.columns(2)
            
            with col_inv1:
                st.write("**📅 Automated Billing System (H-7)**")
                st.info("Sistem mendeteksi 12 cabang akan jatuh tempo dalam 7 hari.")
                if st.button("🚀 Blast Invoice H-7 Ke Seluruh Cabang"):
                    st.success("TREASURER AGENT: 12 Invoice WhatsApp & Email berhasil dikirim secara serentak!")
            
            with col_inv2:
                st.write("**🛡️ Global Alarm Watchdog**")
                st.error("Status: Monitoring 150+ CCTV & Sensor AI Nasional")
                if st.button("🔔 Test Global Alarm"):
                    st.toast("🚨 EMERGENCY: Alarm aktif di seluruh pusat komando wilayah.")

            st.divider()

            # 3. Peta Pemantauan Nasional
            st.subheader("🌐 National Monitoring Map")
            map_data = {
                'city': ['Jakarta', 'Tangerang', 'Surabaya', 'Medan', 'Bali', 'Makassar'],
                'lat': [-6.2088, -6.1702, -7.2575, 3.5952, -8.4095, -5.1476],
                'lon': [106.8456, 106.6303, 112.7521, 98.6722, 115.1889, 119.4327]
            }
            import pandas as pd
            df_map = pd.DataFrame(map_data)
            st.map(df_map)

            # 4. KONTROL CABANG STRATEGIS
            st.divider()
            st.subheader("🕹️ Regional Command & Control")
            col_ctrl1, col_ctrl2 = st.columns([2, 1])
            with col_ctrl1:
                pilih_wilayah = st.selectbox("Pilih Wilayah Operasional:", 
                                           ["Jabodetabek", "Jawa Timur", "Sumatera Utara", "Bali & Nusa Tenggara"])
                if st.button(f"🔴 Live Feed CCTV Wilayah {pilih_wilayah}"):
                    st.success(f"Menghubungkan ke 25+ kamera di {pilih_wilayah}...")
            
            with col_ctrl2:
                st.write("**V-ULTRA Power**")
                st.button("🛡️ Deep Shield Anti-Fraud")
                st.button("📡 Emergency Lockdown (All)")

            # 5. ANALISIS ENTERPRISE
            st.divider()
            st.subheader("📈 Enterprise Business Intelligence")
            if st.button("Generate National Growth Report"):
                with st.spinner("AI menganalisis data nasional..."):
                    st.info("**STRATEGIST AGENT:** Rekomendasi ekspansi ke Jawa Tengah berdasarkan tren penjualan nasional.")

            st.divider()
            st.caption("V-ULTRA: Global Command for Business Leaders.")
        # --- TAB 10: OWNER (STRATEGI EKSEKUTIF) ---
        with t10:
            st.header("👑 Owner Strategic Center")
            o_key = st.text_input("Owner Master Key:", type="password", key="owner_master")
            if o_key == "w1nw1n8282":
                st.success("Selamat Datang, Pak Erwin Sinaga.")
                m1, m2 = st.columns(2)
                m1.metric("Total Revenue", "Rp 1.2M", "12%")
                m2.metric("Customer Satisfaction", "98%", "Stable")
                
                st.divider()
                st.markdown("#### Digital Marketing ROI Simulator")
                budget = st.slider("Budget Iklan (Juta IDR):", 0, 50, 10)
                st.info(f"Prediksi Growth Agent: Kenaikan Omzet sebesar {budget * 2}%")
            elif o_key != "":
                st.error("Access Denied.")
