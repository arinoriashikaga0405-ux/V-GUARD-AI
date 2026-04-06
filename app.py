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
    st.info("Formulir pendaftaran klien baru dan pengiriman akses.")
    c1, c2 = st.columns(2)
    with c1:
        nama_klien = st.text_input("Nama Perusahaan / Pemilik:", key="nk_t1")
        wa_klien = st.text_input("Nomor WhatsApp (Contoh: 62812...):", key="wa_t1")
    with c2:
        produk_v = st.selectbox("Pilih Layanan V-GUARD:", [
            "🛡️ V-GUARD POS & API Integration", 
            "👁️ V-SIGHT Visual Behavior AI", 
            "🚨 V-WATCHDOG Fraud Detection", 
            "💎 V-ULTRA Enterprise Solution"
        ], key="prod_t1")
        tgl_b = st.date_input("Tanggal Aktivasi:", key="tgl_t1")

    st.divider()
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        if st.button("🏗️ Buatkan Akun & Database", key="btn_acc"):
            if nama_klien and wa_klien:
                st.success(f"✅ Akun {nama_klien} Berhasil Dibuat!")
            else: st.error("Lengkapi Nama & WA.")
    with col_a2:
        if st.button("📲 Kirim Link Aktivasi WA", key="btn_wa"):
            if wa_klien:
                pesan = f"Halo {nama_klien}, Akun V-GUARD {produk_v} Anda sudah Aktif. Silakan login di: https://vguard-ai.com"
                st.markdown(f"[👉 KLIK UNTUK KIRIM WHATSAPP](https://wa.me/{wa_klien}?text={pesan.replace(' ', '%20')})")

    st.divider()
    st.subheader("📑 Pusat Audit Dokumen")
    st.file_uploader("Upload Bukti Bayar / Dokumen", accept_multiple_files=True, key="up_t1")

# --- TAB 2 SAMPAI TAB 7 (DIISI RINGKAS AGAR TIDAK BOCOR) ---
with t2:
    st.header("🖥️ Ekosistem AI")
    st.write("Daftar Agent AI aktif sedang memantau sistem.")

with t3:
    st.header("⚙️ Pengaturan")
    st.write("Konfigurasi koneksi API Bank dan POS.")

with t4:
    st.header("📊 Laporan")
    st.write("Halaman khusus laporan hasil audit dokumen.")

with t5:
    st.header("🛡️ Keamanan")
    st.write("Monitoring CCTV dan perilaku mencurigakan.")

with t6:
    st.header("🚨 Alarm")
    st.write("Log peringatan fraud dan anomali.")

with t7:
    st.header("📈 Performa")
    st.write("Statistik laba dan dana yang diselamatkan.")

# --- TAB 8: BACKUP & OWNER (AREA PRIVATE PAK ERWIN) ---
with t8:
    st.header("💾 Backup & Strategic Management")
    if st.button("Jalankan Manual Backup", key="btn_b_t8"):
        st.success("Backup Selesai.")
    st.divider()
    st.subheader("🔒 Owner Intelligence")
    okey = st.text_input("Kode Otoritas:", type="password", key="lock_t8")
    if okey == "w1nw1n8282":
        st.success("Halo Pak Erwin.")
        omz = st.number_input("Estimasi Omzet:", value=100000000, key="omz_t8")
        st.metric("Laba Bersih (Setelah Potongan 40%)", f"Rp {omz * 0.60:,.0f}")
    elif okey != "":
        st.error("Akses Ditolak.")

# --- TAB 9: V-ULTRA ---
with t9:
    st.header("💎 V-ULTRA: Command Center")
    st.code("IP Server: 10.0.88.24\nEncryption: AES-256\nStatus: Secure")
    st.progress(100)

# --- FOOTER (DI LUAR TAB) ---
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence ©2026</small></center>", unsafe_allow_html=True)
