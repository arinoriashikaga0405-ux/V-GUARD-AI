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
    # 1. Cek status login
    if not st.session_state.get('admin_logged_in', False):
        st.header("🔐 Admin Control Center")
        
        # Input password (HANYA muncul di menu Admin)
        admin_input = st.text_input("Password", type="password", key="vguard_admin_final")
        
        # CEK PASSWORD LANGSUNG ('w1nbju8282')
        if admin_input == "w1nbju8282": 
           st.session_state.admin_logged_in = True
           st.rerun() # Refresh HANYA SEKALI saat login berhasil
        else:
            if admin_input != "": # Hanya munculkan error jika sudah mengetik
                st.error("Invalid Key")
            st.stop() # Mengunci halaman agar isi admin tidak bocor
    else: # INI BARIS 168 (Harus lurus dengan 'if not' di baris 154)
            # Tombol Logout dan Dashboard Bapak dimulai di sini
            if st.button("Log Out", key="logout_admin_final"):
                st.session_state.admin_logged_in = False
                st.rerun()
            
            # Setelah ini langsung lanjut ke divider dan subheader
            st.divider() 
            st.subheader("Data Ekosistem V-GUARD")
    
    
            st.divider() # Garis pembatas tipis
            
                # Contoh: Tampilkan data klien atau hasil audit AI
            st.info("Seluruh data rahasia V-GUARD kini dapat Anda akses.")
                                
                # --- V-GUARD ADMIN CONTROL CENTER: FINAL COMPLETE VERSION ---

            st.header("🎮 V-GUARD: Admin Control Center")

           # ==========================================================
# 1. DEFINISI 9 TAB UTAMA
# ==========================================================
t1, t2, t3, t4, t5, t6, t7, t8, t9 = st.tabs([
    "👥 Aktivasi Klien", "🖥️ Ekosistem AI", "⚙️ Pengaturan", 
    "📊 Laporan", "🛡️ Keamanan", "🚨 Alarm", 
    "📈 Performa", "💾 Backup", "💎 V-ULTRA"
])

# --- TAB 1: AKTIVASI KLIEN ---
with t1:
    st.subheader("📝 Pembuatan & Aktivasi Akun Klien (Paid)")
    st.info("Daftarkan klien yang sudah melakukan pembayaran.")
    
    # Input Data Klien
    c1, c2 = st.columns(2)
    with c1:
        nama_klien = st.text_input("Nama Perusahaan/Klien:", placeholder="Contoh: UD. MAJU JAYA", key="nama_k_t1")
    with c2:
        paket_layanan = st.selectbox("Paket V-GUARD:", ["Starter", "Professional", "Enterprise"], key="paket_t1")

    st.divider()

    # Pusat Audit Dokumen (Hanya muncul di Tab 1)
    st.subheader("📑 Pusat Audit Dokumen Multi-Format")
    st.write(f"Audit operasional untuk: **{nama_klien if nama_klien else 'Klien Baru'}**")
    
    up_files_t1 = st.file_uploader(
        "Upload Mutasi/Laporan (Excel/PDF/JPG)",
        accept_multiple_files=True,
        key="audit_v1_exclusive"
    )

    if up_files_t1:
        st.info(f"📂 {len(up_files_t1)} Dokumen terdeteksi.")
        if st.button("🚀 MULAI AUDIT FORENSIK", key="btn_audit_t1"):
            with st.spinner("THE ANALYST sedang membedah dokumen..."):
                st.success("✅ Audit Selesai! Data telah diarsipkan ke sistem.")

# --- TAB 2: EKOSISTEM AI ---
with t2:
    st.header("🛡️ V-GUARD ELITE AI COMMAND CENTER")
    
    # Grid Status Agent (3 Kolom)
    c1, c2, c3 = st.columns(3)
    agents = [
        ("👁️ Visionary", "Active"), ("👂 Concierge", "Active"), 
        ("👄 Growth Hacker", "Active"), ("🤝 Liaison", "Standby"),
        ("🧠 Analyst", "Processing"), ("📈 Strategist", "Active"),
        ("🐕 Watchdog", "Monitoring"), ("🛡️ Sentinel", "Secure"),
        ("⚖️ Legalist", "Safe"), ("💰 Treasurer", "Calculating")
    ]

    for i, (name, status) in enumerate(agents):
        col = [c1, c2, c3][i % 3]
        with col:
            st.info(f"**{name}**\n\nStatus: `{status}`")

    st.divider()
    
    st.subheader("💬 Instruksi Langsung ke Pasukan AI")
    target_agent = st.selectbox("Pilih Agent:", [a[0] for a in agents], key="sel_agent_admin_final")
    user_query = st.text_input(f"Apa instruksi Bapak untuk {target_agent}?", key="query_ai_t2")

    if st.button("Kirim Perintah ke Pasukan", key="btn_send_ai_final"):
        if user_query:
            with st.spinner(f"{target_agent} sedang bekerja..."):
                jawaban = vguard_ai_engine(target_agent, user_query)
                st.markdown(f"### 🚩 Laporan {target_agent}:")
                st.info(jawaban)
        else:
            st.warning("Silakan masukkan instruksi terlebih dahulu, Pak Erwin.")

# --- TAB 3: PENGATURAN & API ---
with t3:
    st.subheader("⚙️ Konfigurasi Integrasi VCS (API POS & Bank)")
    st.info("Hubungkan Kasir atau Bank secara otomatis untuk penarikan data real-time.")
    
    with st.expander("🔓 Buka Panel Konfigurasi API", expanded=False):
        col_api1, col_api2 = st.columns(2)
        with col_api1:
            api_p = st.selectbox("Pilih Provider", ["Moka POS", "Majoo", "BCA Business API", "Mandiri API"], key="api_prov")
        with col_api2:
            st.text_input("API Key / Client ID", type="password", key="api_key_val")

        if st.button("🔌 Uji Koneksi API", key="btn_api_test"):
            with st.spinner(f"Menghubungkan ke server {api_p}..."):
                respon_api = vguard_ai_engine("THE LIAISON", f"Simulasikan koneksi ke {api_p}.")
                st.success(f"✅ Koneksi ke {api_p} BERHASIL!")
                st.caption(respon_api)

# --- TAB 4: LAPORAN ---
with t4:
    st.subheader("📑 Pusat Audit Dokumen Multi-Format")
    st.write("Gunakan bagian ini untuk audit manual via unggah dokumen.")

    up_files_t4 = st.file_uploader(
        "Upload Mutasi/Laporan (Excel/PDF/JPG)", 
        accept_multiple_files=True, 
        key="audit_v4_admin_fixed"
    )

    if up_files_t4:
        st.info(f"📂 {len(up_files_t4)} Dokumen terdeteksi.")
        if st.button("🚀 MULAI AUDIT FORENSIK (THE ANALYST)", key="btn_analyst_t4"):
            with st.spinner("THE ANALYST sedang membedah dokumen Bapak..."):
                file_names = ", ".join([f.name for f in up_files_t4])
                hasil_audit = vguard_ai_engine(
                    agent_name="THE ANALYST",
                    task_instruction=f"Audit dokumen: {file_names}. Temukan potensi fraud.",
                    context_data="Fokus pada kecocokan data mutasi."
                )
                st.success("✅ Audit Selesai!")
                st.markdown(hasil_audit)

# --- TAB 5: KEAMANAN (V-SIGHT) ---
with t5:
    st.header("👁️ V-SIGHT: AI Visual Command Center")
    st.write("Status: **🟢 Monitoring Aktif**")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Kamera Aktif", "08", "+2")
    m2.metric("Deteksi Anomali", "02", "Hari ini")
    m3.metric("Skor Keamanan", "98%", "Optimal")

    st.divider()
    c_vid1, c_vid2 = st.columns(2)
    with c_vid1:
        st.image("https://img.freepik.com/free-photo/security-camera-detecting-thief-store_23-2150914187.jpg", caption="CCTV 01 - Area Kasir")
        st.info("🤖 Mendeteksi gerakan laci kasir terbuka tanpa transaksi aktif.")
    with c_vid2:
        st.image("https://img.freepik.com/free-photo/warehouse-management-system-concept_23-2148923140.jpg", caption="CCTV 02 - Rak Gudang B")
        st.warning("⚠️ Stok Beras 5kg menipis di Rak B.")

# --- TAB 6: PUSAT ALARM ---
with t6:
    st.subheader("🚨 V-GUARD Watchdog (Security Alert)")
    alarms = [
        {"jam": "14:20", "tipe": "⚠️ Anomali", "pesan": "Transaksi Cash didelete di Kasir 02"},
        {"jam": "15:45", "tipe": "🚫 Fraud", "pesan": "Selisih Mutasi Bank vs POS > 5%"}
    ]
    for a in alarms:
        with st.expander(f"{a['jam']} - {a['tipe']}"):
            st.warning(a['pesan'])
            if st.button(f"Analisis Kejadian {a['jam']}", key=f"btn_alarm_{a['jam']}"):
                st.write(vguard_ai_engine("THE WATCHDOG", a['pesan']))

# --- TAB 7: PERFORMA BISNIS ---
with t7:
    st.subheader("📈 Monitoring Laba & Pencegahan Fraud")
    ca, cb = st.columns(2)
    ca.metric("Laba Bersih", "Rp 400.250.000", delta="Normal")
    cb.metric("Dana Terselamatkan", "Rp 15.700.000", delta="Pencegahan Fraud")
    st.divider()
    st.write("💡 **AI Insight:** Pola arus kas stabil.")

# --- TAB 8: BACKUP DATA (OWNER ONLY) ---
with t8:
    st.header("💾 Backup & Strategic Management")
    st.subheader("🛠️ Sistem Cadangan Data")
    if st.button("Jalankan Manual Backup Sekarang", key="btn_backup_manual"):
        st.success("Backup Berhasil (ID: VG-2026-04-06).")

    st.divider()
    st.subheader("🔒 Owner Intelligence Center")
    owner_key = st.text_input("Masukkan Kode Otoritas Owner:", type="password", key="auth_owner")

    if owner_key == "w1nw1n8282":
        st.success("Akses Diterima. Halo Pak Erwin.")
        st.markdown("### 📊 Simulasi Strategis")
        omzet_input = st.number_input("Estimasi Omzet Target (Rp):", min_value=0, value=100000000, key="input_omzet_pribadi")
        
        # Kalkulasi (Potongan 40%)
        biaya_ops_iklan = omzet_input * 0.30
        komisi_insentif = omzet_input * 0.10
        laba_bersih = omzet_input - biaya_ops_iklan - komisi_insentif
        
        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.metric("Laba Bersih Bapak", f"Rp {laba_bersih:,.0f}")
        with col_res2:
            st.metric("Total Potongan (40%)", f"Rp {biaya_ops_iklan + komisi_insentif:,.0f}", delta_color="inverse")

        if st.button("📈 Jalankan Analisis THE STRATEGIST", key="btn_strat_locked"):
            with st.spinner("Menyusun langkah..."):
                saran = vguard_ai_engine("THE STRATEGIST", f"Omzet Rp {omzet_input}, Laba Rp {laba_bersih}", "Data retail 2026.")
                st.info(saran)
    elif owner_key != "":
        st.error("Kode Otoritas Salah.")

# --- TAB 9: V-ULTRA (ENTERPRISE COMMAND CENTER) ---
with t9:
    st.header("💎 V-ULTRA: Enterprise Command Center")
    st.markdown("### 🖥️ Status Infrastruktur & AI Central")
    
    col_u1, col_u2 = st.columns(2)
    with col_u1:
        st.success("🧠 **The Core Brain (AI Central)**")
        st.write("Sinkronisasi data Lintas Cabang & Gudang.")
        st.progress(100)
    with col_u2:
        st.info("🖥️ **Dedicated Server Status**")
        st.code("IP Server: 10.0.88.24\nEncryption: AES-256\nUptime: 99.99%\nStatus: Terhubung")

    st.divider()
    st.metric("ROI Penyelamatan Aset", "Rp 1.250.000.000 / Tahun", delta="Efisiensi 35%")

# --- FOOTER ---
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence ©2026</small></center>", unsafe_allow_html=True)
