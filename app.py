import streamlit as st
import os
import google.generativeai as genai
 
# --- 1. KONFIGURASI ENGINE & SECURITY ---
# API Key sudah dimasukkan langsung sesuai permintaan
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
   system_instruction="Analisa transaksi. Jika Fraud/Anomali atau biaya OPEX > 20% laba balas 'ALERT'. Jika normal balas 'PASS'."
)
 
# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")
 
st.markdown("""
<style>
    .main { background-color: #0e1117; }
   .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; height: 45px; }
   .stTextInput>div>div>input { background-color: #1e293b; color: white; }
</style>
""", unsafe_allow_html=True)
 
# --- 3. LOGIKA V-GUARD (PENYARING BIAYA API & OPEX 20%) ---
def proses_transaksi(total_biaya, laba_kotor, data_input):
    # Logika Pengurangan OPEX maksimal 20% dari Laba Kotor
    batas_aman = laba_kotor * 0.20
    
    if total_biaya > batas_aman:
        return f"ALERT: Biaya (Rp {total_biaya:,.0f}) Melebihi 20% Laba Kotor!", True
        
    if total_biaya < 5000000:
        return "PASS (Auto)", False
        
    response = model_gemini.generate_content(f"Cek: {data_input} | Biaya: {total_biaya} | Laba: {laba_kotor}")
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
 
   st.caption("Semua paket sudah termasuk update sistem keamanan secara berkala.")
 
elif menu == "ROI Kerugian Klien":
   st.header("📊 Analisis Potensi Kerugian vs ROI")
   col_a, col_b = st.columns(2)
   with col_a:
       omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
       leak = st.slider("Estimasi Kebocoran (%)", 1, 20, 5)
       loss = omzet * (leak / 100)
       st.error(f"Potensi Kerugian: Rp {loss:,.0f} / bulan")
 
elif menu == "Portal Klien":
    st.header("Portal Klien V-Guard AI")
    
    if "klien_aktif" not in st.session_state:
        st.session_state.klien_aktif = False
        st.session_state.paket_aktif = "V-PRO" # Default paket

    if not st.session_state.klien_aktif:
        c_reg, c_log = st.columns(2)
        with c_reg:
            st.subheader("📝 Form Order Baru")
            with st.container(border=True):
                st.text_input("Nama Pelanggan")
                st.text_input("Nama Usaha")
                # Pilihan Paket sesuai Produk Bapak
                st.session_state.paket_aktif = st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
                st.text_input("Harga Paket (Rp)")
                st.file_uploader("Upload KTP")
                st.button("Kirim Registrasi")
        
        with c_log:
            st.subheader("🔑 Akses User Aktif")
            with st.container(border=True):
                st.text_input("Username")
                pw = st.text_input("Password", type="password")
                if st.button("Masuk"):
                    if pw == "vguardklien2026": 
                        st.session_state.klien_aktif = True
                        st.rerun()
                    else: 
                        st.error("Password Salah.")
    else:
        # --- DASHBOARD DINAMIS SESUAI PRODUK ---
        p = st.session_state.paket_aktif
        col_head, col_out = st.columns([5, 1])
        col_head.subheader(f"🛡️ Dashboard Management - {p}")
        if col_out.button("Keluar"):
            st.session_state.klien_aktif = False
            st.rerun()
        
        # Logika Tab berdasarkan Fitur Produk Bapak
        tabs_list = ["📊 Summary"]
        if p in ["V-PRO", "V-SIGHT", "V-ENTERPRISE"]:
            tabs_list.append("💰 VCS Bank Sync")
        if p in ["V-SIGHT", "V-ENTERPRISE"]:
            tabs_list.append("👁️ Visual AI")
        if p == "V-ENTERPRISE":
            tabs_list.append("🧠 Forensic AI")

        my_tabs = st.tabs(tabs_list)

        # 1. Tab Summary (Semua Paket: V-LITE, V-PRO, dll)
        with my_tabs[0]:
            st.markdown(f"### Performa {p}")
            c1, c2 = st.columns(2)
            c1.metric("Omzet Harian", "Rp 12,500,000", delta="+5%")
            c2.metric("Leakage Saved", "Rp 1,200,000", delta="Aman")
            
            st.markdown("**Log Fraud Detector Dasar**")
            st.table([
                {"Waktu": "10:15", "Tipe": "Void", "Nilai": "Rp 500,000", "Status": "⚠️ ALERT"},
                {"Waktu": "12:05", "Tipe": "Normal", "Nilai": "Rp 75,000", "Status": "PASS"},
            ])
            if p == "V-LITE":
                st.info("💡 Paket V-LITE: Laporan harian akan dikirim via WA/Email.")

        # 2. Tab VCS (V-PRO ke atas)
        if "💰 VCS Bank Sync" in tabs_list:
            with my_tabs[tabs_list.index("💰 VCS Bank Sync")]:
                st.subheader("VCS: Bank Statement Audit")
                st.write("Sinkronisasi otomatis mutasi bank dengan laporan kasir.")
                st.metric("Akurasi Dana", "100%", delta="Match Verified")
                st.success("H-7 Auto-Invoice: System Ready")

        # 3. Tab Visual (V-SIGHT ke atas)
        if "👁️ Visual AI" in tabs_list:
            with my_tabs[tabs_list.index("👁️ Visual AI")]:
                st.subheader("CCTV AI Behavior Analysis")
                st.image("https://img.freepik.com/free-photo/security-camera-detecting-thief-store_23-2150914187.jpg", width=500)
                st.warning("Visual Cashier Audit: Monitoring Real-Time Stock...")

        # --- TAB 4: FORENSIC (Khusus ENTERPRISE) ---
        if "🧠 Forensic AI" in tabs_list:
            idx = tabs_list.index("🧠 Forensic AI")
            with my_tabs[idx]:
                st.subheader("V-ENTERPRISE: Core Brain Forensic")
                st.code("Otonom Audit: Analisis Data Historis 1 Tahun Aktif.")
                st.write("Dedicated Server IP: 10.0.88.24")

# --- BARIS INI HARUS MEPET KE KIRI (SEJAJAR DENGAN MENU LAIN) ---
elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center")
    
    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False

    if not st.session_state.admin_logged_in:
        admin_input = st.text_input("Admin Password", type="password", key="admin_pass")
        if st.button("Log In Admin"):
            if admin_input == "w1nbju8282":
                st.session_state.admin_logged_in = True
                st.rerun()
            else:
                st.error("Akses Ditolak.")
    else:
        st.success("Mode Eksekutif Aktif")
        
        # --- BAGIAN RINGKASAN EKSEKUTIF (PINDAH KE SINI AGAR TIDAK ERROR) ---
        st.markdown("### 📊 Ringkasan Eksekutif & AI Squad")
        
        # Panel Biaya API & Efisiensi
        c_api1, c_api2, c_api3 = st.columns(3)
        with c_api1:
            st.metric("Anggaran API Bulanan", "Rp 10.000.000")
        with c_api2:
            st.metric("Biaya API Terpakai", "Rp 1.200.000", delta="-15% (Hemat)")
        with c_api3:
            st.metric("Efisiensi Sistem", "88%", delta="Target > 80%")
            
        st.progress(0.12, text="Penggunaan Kuota API Cloud: 20%")
        st.divider()

        if st.button("Log Out Admin"):
            st.session_state.admin_logged_in = False
            st.rerun()

# --- FOOTER PINDAH KE PALING BAWAH SEKALI ---
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026</small></center>", unsafe_allow_html=True)
st.subheader("🤖 V-Guard AI Squad Agents") 
sq1.metric("V-LITE AI", "Active")
sq2.metric("V-PRO AI", "Active")
sq3.metric("V-SIGHT AI", "Standby")
sq4.metric("CORE AI", "Active")

if st.button("Log Out Admin"):
    st.session_state.admin_logged_in = False
    st.rerun()

# --- FOOTER PALING BAWAH ---
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026</small></center>", unsafe_allow_html=True)
       t.markdown("#### 🤖 Status V-Guard AI Agent Squad")
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
                st.markdown("📑 **Agent: Invoicer**")
                st.caption("Status: H-7 Ready")
                st.write("Otomatisasi pengiriman invoice klien.")

        if st.button("Log Out Admin"):
            st.session_state.admin_logged_in = False
            st.rerun()

# --- FOOTER PALING BAWAH (SEJAJAR PINGGIR KIRI) ---
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026</small></center>", unsafe_allow_html=True)
 
       st.divider()
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
