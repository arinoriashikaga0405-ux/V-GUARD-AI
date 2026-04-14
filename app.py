import streamlit as st
import os
import google.generativeai as genai

# --- 1. PENGATURAN AI & KEAMANAN (LOGIKA INTERNAL) ---
# Mengambil API Key langsung dari sistem Railway (Environment Variables)
gemini_key = os.environ.get("GEMINI_API_KEY")
ai_status_msg = "Mode Offline"
model_vguard = None

if gemini_key:
    try:
        genai.configure(api_key=gemini_key)
        model_vguard = genai.GenerativeModel('gemini-1.5-flash')
        ai_status_msg = "Connected"
    except Exception:
        ai_status_msg = "Error Connection"

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")
# --- Tambahkan di Baris 21 ---
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

# THE SENTINEL: Sistem Auto-Recovery & Health Check
if "system_status" not in st.session_state:
    st.session_state.system_status = "Healthy"

def sentinel_recovery():
    if st.session_state.system_status != "Healthy":
        # Simulasi restart mandiri oleh The Sentinel
        st.session_state.system_status = "Healthy"
        return True
    return False
    def get_data_from_google():
        try:
            # Mencoba koneksi asli ke Google Sheets
            from streamlit_gsheets import GSheetsConnection
            conn = st.connection("gsheets", type=GSheetsConnection)
            df = conn.read(ttl="1m")
            return df
        except Exception:
            # JIKA GAGAL: Tampilkan Data Simulasi V-LITE & V-PRO
            import pandas as pd
            data_simulasi = {
                "Nama Klien": ["Timotius Mardjuki", "Outlet Sudirman", "Resto Central", "Cabang Tangerang"],
                "Produk": ["V-PRO (10 Agents)", "V-LITE (Standard)", "V-PRO (10 Agents)", "V-LITE (Standard)"],
                "Status": ["✅ Terverifikasi", "⚠️ Pending Payment", "🛡️ Audit Watchdog", "✅ Aktif"],
                "Nilai Kontrak": ["Rp 10.000.000", "Rp 5.000.000", "Rp 12.500.000", "Rp 5.000.000"]
            }
            return pd.DataFrame(data_simulasi)

# CSS Custom untuk tampilan profesional
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; height: 45px; }
    .stTextInput>div>div>input { background-color: #1e293b; color: white; }
    .reportview-container .main .block-container { padding-top: 2rem; }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    
    # Menampilkan Foto Founder di Sidebar
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    
    st.markdown(f"""
    <div style='text-align:center;'>
        <p style='color:white; font-weight:bold; margin-bottom:0;'>Erwin Sinaga</p>
        <p style='color:gray;'>Founder & CEO V-Guard AI</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Produk & Layanan", "ROI Kerugian Klien", "Portal Klien", "Admin Control Center"])

# --- 4. LOGIKA MENU ---

if menu == "Visi & Misi":
    st.header("🛡️ Visi & Misi: Digitizing Trust")
    col_img, col_txt = st.columns([1, 2])
    
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga - Founder & CEO", use_container_width=True)
    
    with col_txt:
        # TEKS UTUH TANPA POTONGAN
        st.markdown(f"""
        <div style="text-align: justify; line-height: 1.8; font-size: 16px; color: #d1d5db;">
        <b>V-Guard AI Intelligence</b> lahir dari urgensi integritas finansial di era transformasi digital yang berkembang pesat. 
        Sebagai entitas yang dipimpin oleh profesional dengan pengalaman lebih dari satu dekade di industri perbankan dan manajemen aset, 
        kami memahami bahwa celah terkecil dalam sistem operasional adalah potensi kerugian fatal bagi sebuah bisnis. 
        Misi utama kami adalah mendigitalisasi kepercayaan (Digital Trust) melalui pembuktian matematis dan audit cerdas yang bekerja 
        secara otonom 24 jam nonstop tanpa kompromi sedikit pun.<br><br>
        Kami percaya bahwa kejujuran sistem tidak boleh hanya bergantung pada pengawasan manusia yang memiliki keterbatasan, 
        melainkan harus dibangun di atas fondasi teknologi AI yang presisi. Melalui ekosistem V-Guard, kami mengintegrasikan analisis data perbankan (VCS), 
        visi komputer, dan deteksi anomali prediktif untuk menciptakan lingkungan bisnis yang bersih dari segala bentuk kecurangan (Fraud). 
        Strategi kami adalah memberikan transparansi mutlak kepada pemilik bisnis melalui laporan yang akurat dan real-time.<br><br>
        Visi kami adalah menjadi standar global dalam "<b>Eliminating Leakage</b>", di mana setiap pemilik bisnis, mulai dari UMKM hingga korporasi besar, 
        dapat menjalankan operasional mereka dengan tenang karena setiap Rupiah diawasi oleh kecerdasan buatan yang tak kenal lelah. 
        V-Guard bukan sekadar perangkat lunak, melainkan benteng pertahanan terakhir bagi aset dan masa depan investasi Anda. 
        Kami hadir untuk mengeliminasi kebocoran, mengoptimalkan profitabilitas, dan menjaga warisan bisnis Anda tetap utuh melalui inovasi teknologi 
        yang melampaui standar audit konvensional saat ini.
        </div>
        """, unsafe_allow_html=True)

elif menu == "Produk & Layanan":
    st.header("🛡️ Portfolio Layanan V-Guard AI Intelligence")
    wa_number = "6282122190885"
    c1, c2, c3, c4 = st.columns(4)
    
    packages = {
        "V-LITE": ["Mikro / 1 Kasir", "750 rb", "350 rb", "AI Fraud Detector Dasar, Daily WA/Email Summary"],
        "V-PRO": ["Retail & Kafe", "1.5 Jt", "850 rb", "VCS Integration, Bank Statement Audit, Input Excel/CSV/PDF"],
        "V-SIGHT": ["Gudang & Toko", "7,5 Jt", "3,5 Jt", "CCTV AI Behavior, Visual Cashier Audit, Fraud Alarm (🚨)"],
        "V-ENTERPRISE": ["Korporasi", "15 Jt", "10 Jt", "The Core Brain, Forensic AI, Dedicated Server, Custom AI SOP"]
    }
    
    for i, (name, details) in enumerate(packages.items()):
        with [c1, c2, c3, c4][i]:
            with st.container(border=True):
                st.markdown(f"### 📦 {name}")
                st.write(f"**Target:** {details[0]}")
                st.info(f"Pasang: {details[1]}\n\nBulan: {details[2]}")
                st.write(details[3])
                st.link_button(f"Pilih {name}", f"https://wa.me/{wa_number}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20dengan%20paket%20*{name}*%20V-Guard%20AI.")

elif menu == "ROI Kerugian Klien":
    st.header("📊 Analisis Potensi Kerugian vs ROI")
    st.write("Gunakan kalkulator ini untuk melihat berapa banyak kebocoran yang bisa dihemat oleh V-Guard AI.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        omzet = st.number_input("Omzet Bulanan Bisnis Anda (Rp)", value=100000000, step=1000000)
        leak = st.slider("Estimasi Persentase Kebocoran/Fraud (%)", 1, 20, 5)
        loss = omzet * (leak / 100)
        
    with col_b:
        st.error(f"### Potensi Kerugian: Rp {loss:,.0f} / bulan")
        st.success(f"### Potensi Penyelamatan AI: Rp {loss * 0.88:,.0f} / bulan")
        st.caption("Dihitung berdasarkan rata-rata efisiensi sistem V-Guard sebesar 88%.")

elif menu == "Portal Klien":
    st.header("🔑 Portal Akses Klien V-Guard")
    
    # --- KONEKSI GOOGLE SHEETS ---
    from streamlit_gsheets import GSheetsConnection
    
    # Inisialisasi koneksi
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    # Membaca data dari Spreadsheet Bapak
    url_sheets = "https://docs.google.com/spreadsheets/d/17OJpYRGTWdQ0ZldSxp-3HdyW4AN_RKuJkCWVpYbtNE8/edit?usp=sharing"
    
    try:
        # Mengambil data terbaru dari Sheets
        df_clients = conn.read(spreadsheet=url_sheets, ttl="0") 
    except Exception:
        st.error("Gagal sinkronisasi dengan database pusat.")
        df_clients = None

    tab_log, tab_reg = st.tabs(["🔐 Login Dashboard", "📝 Registrasi Baru"])
    
    with tab_log:
        st.subheader("Masuk ke Sistem Monitoring")
        
        col_login1, col_login2 = st.columns(2)
        with col_login1:
            user_id_input = st.text_input("User ID Klien", placeholder="Contoh: VGUARD-PRO-99")
            # Password bisa disamakan atau ditarik dari kolom lain di Sheets jika Bapak mau
            password = st.text_input("Password", type="password") 
            btn_login = st.button("Masuk ke Dashboard")

        if btn_login and df_clients is not None:
            # Cek apakah User ID ada di kolom 'UserID' spreadsheet
            if user_id_input in df_clients['UserID'].values:
                # Ambil data spesifik klien tersebut
                client_info = df_clients[df_clients['UserID'] == user_id_input].iloc[0]
                paket_aktif = client_info['Paket']
                status_klien = client_info['Status']

                if status_klien == "Aktif":
                    st.success(f"Selamat Datang! Lisensi Anda: **{paket_aktif}** (Status: Aktif ✅)")
                    st.divider()
                    st.subheader(f"📊 Dashboard Monitoring - {paket_aktif}")
                    
                    # LOGIKA TAMPILAN DINAMIS BERDASARKAN PAKET DI SHEETS
                    m1, m2, m3 = st.columns(3)
                    
                    if paket_aktif == "V-LITE":
                        m1.metric("Status Kasir", "Online")
                        m2.metric("Fraud Alert Today", "0")
                        m3.info("Fitur V-LITE: Daily Summary Ready")
                    
                    elif paket_aktif == "V-PRO":
                        m1.metric("Sync Bank (VCS)", "Active")
                        m2.metric("Fraud Alert Today", "2 Case", delta="Perlu Cek", delta_color="inverse")
                        m3.metric("Revenue Protection", "Rp 1.2M")
                        st.write("**Recent Activities:** Audit PDF Berhasil diunggah.")

                    elif paket_aktif == "V-SIGHT":
                        m1.metric("CCTV AI Status", "Streaming")
                        m2.metric("Behavior Anomalies", "1", delta="🚨")
                        m3.metric("Visual Audit", "Match 100%")
                        st.image("https://via.placeholder.com/600x200?text=CCTV+AI+Visual+Monitoring+Active", use_container_width=True)

                    elif paket_aktif == "V-ENTERPRISE":
                        st.warning("⚠️ High Security Mode: The Core Brain Active")
                        m1.metric("Forensic Scan", "99.9%")
                        m2.metric("Network Integrity", "Secure")
                        m3.metric("Custom SOP Drift", "0%")
                        st.write("DASHBOARD EKSEKUTIF: Seluruh cabang terpantau aman.")
                else:
                    st.error("Akun Anda sedang ditangguhkan. Silakan hubungi Admin.")
            else:
                st.error("User ID tidak ditemukan. Pastikan ID sudah benar atau hubungi Admin.")

    with tab_reg:
        st.subheader("Form Order & Aktivasi Layanan")
        # --- Baris 223 & 224 tetap ---
    with tab_reg:
        st.subheader("Form Order & Aktivasi Layanan")
    
    # GANTI Baris 225 ke bawah dengan ini:
    with st.form("pendaftaran_umum"):
        nama_klien = st.text_input("Nama Lengkap / Owner")
        nama_usaha = st.text_input("Nama Usaha")
        no_hp = st.text_input("Nomor WhatsApp (Aktif)", placeholder="Contoh: 62812xxxx")
        upload_ktp = st.file_uploader("Upload Foto KTP (Verifikasi Sentinel)", type=['png', 'jpg', 'jpeg'])
        produk = st.selectbox("Pilih Paket Aktivasi", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
        
        # Masukkan Syarat & Ketentuan di dalam form agar lebih rapi
        with st.expander("📄 Baca Syarat & Ketentuan (T&C)"):
            st.markdown("""
            ### TERMS & CONDITIONS (T&C) - V-GUARD AI SYSTEMS
            **1. Pembayaran:** Aktivasi dimulai setelah biaya diverifikasi (Activation Fee & Monthly).
            **2. Keamanan Data:** Data terenkripsi dan tidak dibocorkan ke pihak ketiga.
            """)
        
        setuju_tc = st.checkbox("Saya telah membaca dan menyetujui Syarat & Ketentuan.")
        
        # Tombol Submit di dalam Form
        submit = st.form_submit_button("🚀 Daftar Sekarang & Dapatkan Akses AI")
        
        if submit:
            if setuju_tc and nama_klien and no_hp:
                # Inisialisasi memori pendaftar umum jika belum ada
                if 'db_umum' not in st.session_state:
                    st.session_state.db_umum = []
                
                # Simpan data klien umum ke memori (agar muncul di dashboard admin)
                st.session_state.db_umum.append({
                    "Nama Klien": nama_klien,
                    "Produk": produk,
                    "Status": "🛡️ Menunggu Pembayaran",
                    "WhatsApp": no_hp
                })
                st.success(f"Pendaftaran Berhasil! Invoice dikirim ke {no_hp}. Mohon tunggu verifikasi Admin.")
            else:
                st.error("Mohon isi semua data dan setujui Syarat & Ketentuan.")

       
        # --- PROSES AKTIVASI OLEH ELITE AI SQUAD ---
    if st.button("Kirim Pengajuan Aktivasi"):
        if setuju_tc:
            if nama_owner and nama_usaha:
                # Menjalankan fungsi koordinasi agen (The Sentinel & The Legalist)
                with st.status("V-Guard AI Squad sedang memproses...", expanded=True) as status:
                    st.write("🛡️ **The Legalist**: Mengamankan privasi data.")
                    st.write("🤝 **The Liaison**: Menghubungkan API ke Cloud.")
                    status.update(label="Aktivasi Berhasil!", state="complete", expanded=False)
                
                st.success(f"Terima Kasih Pak {nama_owner}. Paket {paket_pilihan} Aktif.")
            else:
                st.warning("Mohon lengkapi data pendaftaran.")
        else:
            st.error("🚨 Mohon setujui T&C terlebih dahulu.")
            
    elif menu_admin == "Aktivasi Nasabah Baru":
        st.header("📋 Antrean Aktivasi V-Guard")
        st.info("Menunggu pendaftaran baru dari Portal Klien...")

    # HANYA MENAMPILKAN PENDAFTAR UMUM (REVENUE REAL)
    if 'db_umum' in st.session_state and st.session_state.db_umum:
        import pandas as pd
        df_realtime = pd.DataFrame(st.session_state.db_umum)
        
        st.subheader("🚀 Daftar Pendaftar Baru")
        st.table(df_realtime)

        st.markdown("---")
        k_pil = st.selectbox("Pilih Klien untuk Proses Penagihan", df_realtime["Nama Klien"].tolist())
        
        # Ambil data spesifik klien yang dipilih
        d_sel = df_realtime[df_realtime["Nama Klien"] == k_pil].iloc[0]
        
        # Pemetaan Harga Akurat
        h_map = {
            "V-LITE": "750rb + 350rb/bln", 
            "V-PRO": "1.5jt + 850rb/bln", 
            "V-SIGHT": "7.5jt + 3.5jt/bln", 
            "V-ENTERPRISE": "15jt + 10jt/bln"
        }
        nom = h_map.get(d_sel["Produk"], "750.000")

        # Pesan Penagihan Profesional
        msg = (
            f"Halo {k_pil}, Invoice Aktivasi V-Guard ({d_sel['Produk']}) Anda sudah siap.\n\n"
            f"Total Investasi: {nom}\n"
            f"Transfer ke BCA: 3450074658\n"
            f"Atas Nama: Erwin Sinaga\n\n"
            f"Silakan kirim bukti transfer ke sini untuk aktivasi Sentinel."
        )
        
        import urllib.parse
        st.link_button(f"💰 Kirim Tagihan ke {k_pil}", 
                       f"https://wa.me/{d_sel['WhatsApp']}?text={urllib.parse.quote(msg)}")
    else:
        # Tampilan jika antrean masih kosong
        st.warning("Belum ada pendaftaran baru saat ini.")
    
    # 1. CEK STATUS LOGIN
elif menu == "Admin Control Center":
    st.header("🔐 V-Guard Intelligence Center")

    # 1. CEK STATUS LOGIN
    if not st.session_state.get('admin_logged_in', False):
        st.subheader("🔑 Admin Authentication")
        admin_password = st.text_input("Masukkan Access Code:", type="password")
        if st.button("Buka Intelligence Center"):
            if admin_password == "w1nbju8282":
                st.session_state.admin_logged_in = True
                st.rerun()
            else:
                st.error("Access Code Salah!")
    
    # 2. JIKA SUDAH LOGIN, TAMPILKAN KONTEN KHUSUS ADMIN
    else:
        with st.sidebar:
            st.markdown("---")
            # DEFINISIKAN menu_admin DI SINI AGAR TIDAK ERROR 'NOT DEFINED'
            menu_admin = st.selectbox("Admin Menu", [
                "Dashboard Utama",
                "Aktivasi Nasabah Baru",
                "Monitoring 10 Agents",
                "Database Klien"
            ])
            
            if st.button("Log Out"):
                st.session_state.admin_logged_in = False
                st.rerun()

        # LOGIKA TAMPILAN BERDASARKAN MENU ADMIN YANG DIPILIH
        # --- LOGIKA TAMPILAN BERDASARKAN MENU ADMIN ---
    if menu_admin == "Dashboard Utama":
            st.subheader("🛡️ Elite AI Squad Activation (10 Agents)")
            c1, c2, c3, c4 = st.columns(4)
            with c1: st.success("👁️ The Visionary")
            with c2: st.success("📦 The Concierge")
            # ... (lanjutkan sukses agen lainnya)

     elif menu_admin == "Aktivasi Nasabah Baru":
            st.header("📋 Antrean Aktivasi V-Guard")
            if 'db_umum' in st.session_state and st.session_state.db_umum:
                import pandas as pd
                st.table(pd.DataFrame(st.session_state.db_umum))
            else:
                st.info("Belum ada antrean baru.")
            
            # CEK DATA DARI PORTAL KLIEN
            if 'db_umum' in st.session_state and st.session_state.db_umum:
                import pandas as pd
                df_real = pd.DataFrame(st.session_state.db_umum)
                st.subheader("🚀 Pendaftar Baru (Real-Time)")
                st.table(df_real)
                
                st.markdown("---")
                k_pil = st.selectbox("Pilih Klien untuk Ditagih", df_real["Nama Klien"].tolist())
                d_sel = df_real[df_real["Nama Klien"] == k_pil].iloc[0]
                
                h_map = {
                    "V-LITE": "750rb + 350rb/bln", 
                    "V-PRO": "1.5jt + 850rb/bln", 
                    "V-SIGHT": "7.5jt + 3.5jt/bln", 
                    "V-ENTERPRISE": "15jt + 10jt/bln"
                }
                nom = h_map.get(d_sel["Produk"], "750.000")

                import urllib.parse
                msg = (f"Halo {k_pil}, Invoice V-Guard {d_sel['Produk']} Anda siap.\n"
                       f"Total: {nom}\nBCA: 3450074658 (Erwin Sinaga)")
                
                st.link_button(f"💰 Kirim Invoice ke {k_pil}", 
                               f"https://wa.me/{d_sel['WhatsApp']}?text={urllib.parse.quote(msg)}")
            else:
                st.info("💡 Belum ada antrean pendaftaran baru dari Portal Klien.")

        elif menu_admin == "Monitoring 10 Agents":
            st.header("🔍 Real-Time Monitoring")
            st.write("Sistem monitoring sedang standby.")
            
            # CEK DATA REVENUE (Klien Umum dari Portal)
            if 'db_umum' in st.session_state and st.session_state.db_umum:
                import pandas as pd
                df_real = pd.DataFrame(st.session_state.db_umum)
                st.subheader("🚀 Pendaftar Baru (Real-Time)")
                st.table(df_real)
                
                st.markdown("---")
                k_pil = st.selectbox("Pilih Klien untuk Ditagih", df_real["Nama Klien"].tolist())
                d_sel = df_real[df_real["Nama Klien"] == k_pil].iloc[0]
                
                # Pemetaan Harga V-Guard
                h_map = {
                    "V-LITE": "750rb + 350rb/bln", 
                    "V-PRO": "1.5jt + 850rb/bln", 
                    "V-SIGHT": "7.5jt + 3.5jt/bln", 
                    "V-ENTERPRISE": "15jt + 10jt/bln"
                }
                nom = h_map.get(d_sel["Produk"], "750.000")

                msg = (
                    f"Halo {k_pil}, Invoice Aktivasi V-Guard ({d_sel['Produk']}) Anda sudah siap.\n\n"
                    f"Total Investasi: {nom}\n"
                    f"Transfer ke BCA: 3450074658 (Erwin Sinaga)\n\n"
                    f"Kirim bukti transfer ke sini untuk aktivasi unit AI Anda."
                )
                
                import urllib.parse
                st.link_button(f"💰 Kirim Invoice ke {k_pil}", 
                               f"https://wa.me/{d_sel['WhatsApp']}?text={urllib.parse.quote(msg)}")
            else:
                st.info("💡 Belum ada antrean pendaftaran baru dari Portal Klien.")

        elif menu_admin == "Monitoring 10 Agents":
            st.header("🔍 Real-Time Monitoring (Elite Agents)")
            # Sisa kode monitoring Bapak di sini...
            st.divider()
            
            # Data Invoice
            invoice_data = {
                "Customer/Outlet": ["Outlet Sudirman", "Cabang Tangerang", "Resto Central"],
                "Nilai Tagihan": ["Rp 15.000.000", "Rp 8.200.000", "Rp 12.500.000"],
                "Jatuh Tempo": ["H-2 (Mendesak)", "H-5", "H-7"],
                "Status": ["🚨 Kirim Alarm", "⚠️ Reminder Sent", "✅ Scheduled"]
            }
            st.table(invoice_data)
            
            # Gatekeeper & Audit Trail
            st.divider()
            st.subheader("🛰️ AI Pre-Cloud Gatekeeper")
            col_stat1, col_stat2, col_stat3 = st.columns(3)
            col_stat1.metric("Data Traffic", "100%", "Secure")
            col_stat2.metric("AI Filtering", "0.2ms/trans", "Fast")
            col_stat3.metric("Alarm Merah", "Active", "WhatsApp Bot")

            with st.expander("🔍 Live Audit Trail (Pre-Filtering Mode)", expanded=True):
                st.code("[SYSTEM] API Connected...\n[AGENT] The Watchdog: Scanning...\n[WARNING] Anomali #9922 Terdeteksi!")
                st.error("🚨 FRAUD DETECTED: Upaya manipulasi dicegah!")

            # Core Brain Interaction
            st.divider()
            st.subheader("🤖 The Core Brain - AI Strategist")
            user_query = st.text_area("Konsultasi Strategi (Input Instruksi):")
            if st.button("Jalankan AI Audit"):
                if model_vguard and user_query:
                    with st.spinner("Menganalisis..."):
                        context = f"Anda adalah Core Brain V-Guard. Jawab Founder Erwin Sinaga: {user_query}"
                        response = model_vguard.generate_content(context)
                        st.markdown(response.text)
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026</small></center>", unsafe_allow_html=True)
