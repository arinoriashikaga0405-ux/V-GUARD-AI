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
    st.markdown("---")
    # Membuat dua kolom: Kolom 1 untuk Foto, Kolom 2 untuk Teks Visi & Misi
    col_foto, col_teks = st.columns([1, 2.5])

    with col_foto:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga - Founder & CEO", use_container_width=True)
        else:
            st.info("Foto 'erwin.jpg' tidak ditemukan")

    with col_teks:
        st.subheader("Visi & Misi: Digitizing Trust, Eliminating Leakage")
        # Narasi 250 Kata mencakup semua sektor usaha
        st.markdown(f"""
        <div style="text-align: justify; line-height: 1.7; color: #d1d5db; font-size: 15px;">
        <b>V-GUARD AI Intelligence</b> didirikan atas dasar keyakinan bahwa kepercayaan di era digital 
        harus didukung oleh data yang objektif dan transparan. Visi utama kami, <b>Digitizing Trust, 
        Eliminating Leakage</b>, bukan sekadar semboyan, melainkan komitmen kami untuk memberikan 
        kepastian operasional bagi para pemimpin bisnis. Kami memahami bahwa tantangan terbesar dalam 
        setiap organisasi adalah menjaga integritas di setiap lini. Oleh karena itu, kami hadir untuk 
        mendigitalisasi kepercayaan tersebut, memastikan bahwa setiap interaksi dan proses bisnis 
        tercatat dengan presisi yang tidak dapat dimanipulasi.
        <br><br>
        Misi strategis kami melampaui batasan industri tradisional; kami merancang solusi cerdas yang dapat 
        diadaptasi oleh <b>seluruh sektor jenis usaha</b>, mulai dari manufaktur, ritel, jasa, hingga 
        pengelolaan properti skala besar. Melalui teknologi deteksi visual tingkat lanjut, kami bertekad 
        menghilangkan segala bentuk kebocoran (leakage)—baik itu kebocoran finansial, inefisiensi tenaga kerja, 
        maupun potensi kehilangan aset fisik. Kami mengubah sistem keamanan yang awalnya bersifat pasif 
        menjadi asisten analitik proaktif yang bekerja 24/7.
        <br><br>
        Dengan membangun infrastruktur digital yang kokoh di tingkat nasional, V-GUARD AI berkomitmen 
        untuk mengoptimalkan profitabilitas klien kami melalui eliminasi celah operasional secara total. 
        Kami percaya bahwa melalui transparansi data yang dihasilkan oleh AI, setiap pemilik usaha dapat 
        mengambil keputusan strategis dengan tingkat keyakinan yang lebih tinggi. Kami adalah mitra 
        strategis Anda dalam menjaga masa depan bisnis yang bersih, efisien, dan berkelanjutan 
        di seluruh pelosok nusantara.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

import streamlit as st

def show_produk_layanan():
    st.title("🛡️ Daftar Layanan V-GUARD AI Systems")
    st.write("Solusi kecerdasan buatan untuk keamanan transaksi dan optimalisasi profit bisnis Anda.")
    st.markdown("---")

    # CSS Khusus agar kartu rapi, profesional, dan tinggi menyesuaikan isi
    st.markdown("""
        <style>
        [data-testid="stVerticalBlock"] > div:has(div.pk-card) {
            background-color: #ffffff;
            border: 1px solid #e6e9ef;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
            display: flex;
            flex-direction: column;
            height: 100%;
        }
        .price-box {
            background-color: #f0f4f0;
            padding: 12px;
            border-radius: 8px;
            border-left: 5px solid #2e7d32;
            margin: 15px 0;
            font-weight: bold;
            color: #1e4620;
        }
        .sales-pitch {
            font-style: italic;
            color: #555;
            border-top: 1px dashed #ccc;
            padding-top: 10px;
            margin-top: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # BARIS 1: V-LITE & V-PRO
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="pk-card">', unsafe_allow_html=True)
        st.subheader("1. V-LITE (Entry Level)")
        st.caption("Target: Toko Kelontong, Butik Kecil, Kedai Kopi (1 Kasir)")
        st.write("**Fungsi Utama:** CCTV Digital Transaksi")
        st.markdown("""
        * ✅ **AI Fraud Detector Dasar**: Deteksi transaksi tak wajar (barang keluar tanpa input).
        * ✅ **Daily WA/Email Summary**: Laporan ringkas harian langsung ke HP Owner.
        * ✅ **Monthly PDF Recap**: Rekapitulasi bulanan untuk evaluasi keuntungan.
        """)
        st.markdown('<div class="price-box">💰 Aktivasi: 1.5jt | Rp 550rb/bln</div>', unsafe_allow_html=True)
        st.markdown('<p class="sales-pitch">"Murah, Praktis, Aman. Cocok buat yang baru mulai bisnis dan ingin tidur nyenyak tanpa takut uang laci dicuri."</p>', unsafe_allow_html=True)
        st.link_button("Konsultasi V-LITE", "https://wa.me/6282122190885?text=Halo%20Admin,%20V-LITE", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="pk-card">', unsafe_allow_html=True)
        st.subheader("2. V-PRO (Growth Level)")
        st.caption("Target: Restoran, Kafe Menengah, Retail Stok Banyak")
        st.write("**Fungsi Utama:** Otomasi Audit & Keuangan")
        st.markdown("""
        * ✅ **VCS Integration**: Sinkronisasi stok dengan catatan kasir otomatis.
        * ✅ **Bank Statement Audit**: Cocokkan uang bank dengan laporan (Anti-manipulasi).
        * ✅ **H-7 Auto-Invoice**: Pengingat otomatis tagihan/pembayaran supplier.
        """)
        st.markdown('<div class="price-box">💰 Aktivasi: 3jt | Rp 1.5jt/bln</div>', unsafe_allow_html=True)
        st.markdown('<p class="sales-pitch">"Ganti admin manual Bapak/Ibu dengan AI. Lebih cepat, lebih akurat, dan anti-salah hitung."</p>', unsafe_allow_html=True)
        st.link_button("Konsultasi V-PRO", "https://wa.me/6282122190885?text=Halo%20Admin,%20V-PRO", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("---")

    # BARIS 2: V-SIGHT & V-ENTERPRISE
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown('<div class="pk-card">', unsafe_allow_html=True)
        st.subheader("3. V-SIGHT (Monitoring)")
        st.caption("Target: Gudang Distributor, Minimarket, Toko Emas")
        st.write("**Fungsi Utama:** CCTV Pintar & Visual AI")
        st.markdown("""
        * ✅ **CCTV AI Behavior**: Deteksi gerak mencurigakan di area terlarang.
        * ✅ **Visual Cashier Audit**: Bandingkan wajah staf dengan data transaksi.
        * ✅ **Fraud Alarm**: Notifikasi instan (sirine/HP) saat terjadi potensi pencurian.
        """)
        st.markdown('<div class="price-box">💰 Aktivasi: 7.5jt | Rp 2.9jt/bln</div>', unsafe_allow_html=True)
        st.markdown('<p class="sales-pitch">"Bukan sekadar rekam, tapi mengawasi. V-SIGHT adalah satpam digital 24 jam yang tidak pernah mengantuk."</p>', unsafe_allow_html=True)
        st.link_button("Konsultasi V-SIGHT", "https://wa.me/6282122190885?text=Halo%20Admin,%20V-SIGHT", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="pk-card">', unsafe_allow_html=True)
        st.subheader("4. V-ENTERPRISE (Ultimate)")
        st.caption("Target: Perusahaan Besar, Jaringan Ritel Nasional, Pabrik")
        st.write("**Fungsi Utama:** Kontrol Total Infrastruktur & SOP")
        st.markdown("""
        * ✅ **The Core Brain**: Olah ribuan data banyak cabang sekaligus.
        * ✅ **Forensic AI (1 Thn)**: Lacak data setahun ke belakang untuk investigasi.
        * ✅ **Dedicated Server**: Server private (VPS KVM 2) agar data sangat aman.
        * ✅ **Custom AI SOP**: AI didesain khusus mengikuti aturan unik perusahaan.
        """)
        st.markdown('<div class="price-box">💰 Aktivasi: 10jt | Rp 6.9jt/bln</div>', unsafe_allow_html=True)
        st.markdown('<p class="sales-pitch">"Solusi kasta tertinggi untuk proteksi aset milyaran rupiah. Eksklusif, sangat aman, dan sepenuhnya kustom."</p>', unsafe_allow_html=True)
        st.link_button("Konsultasi V-ENTERPRISE", "https://wa.me/6282122190885?text=Halo%20Admin,%20V-ENTERPRISE", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("---")

    # BARIS 3: V-ULTRA (FULL WIDTH - LEGENDARY LEVEL)
        st.subheader("5. V-ULTRA (Legendary Level)")
    with st.container(border=True):
        u1, u2 = st.columns([1, 1])
        with u1:
            st.caption("Target: Investor Multi-Cabang, Pemilik Jaringan Hotel/Resort")
            st.write("**Fungsi:** Decision Support System (DSS) Prediktif")
            st.markdown("""
            * ✅ **Multi-Branch Executive Dashboard**: Rekap performa seluruh cabang dalam satu layar.
            * ✅ **Leakage Heatmap**: Peta titik panas lokasi paling rawan kebocoran.
            * ✅ **Profit Optimizer**: Saran stok & operasional berbasis tren pembelian.
            """)
        with u2:
         st.markdown("""
            * ✅ **White-Label Branding**: Gunakan logo & nama perusahaan Anda sendiri.
            * ✅ **VIP Priority Support**: Respons tim ahli < 15 menit & Monitoring 24/7.
            * ✅ **H-7 Multi-Vendor Invoice**: Kontrol tagihan lintas vendor otomatis.
            """)
         st.info("💰 Aktivasi: 25jt | Rp 14.9jt/bln")
         st.link_button("Hubungi Eksklusif V-ULTRA", "https://wa.me/6282122190885?text=Halo%20Founder,%20V-ULTRA", use_container_width=True)
            
elif menu == "Analisis ROI Kerugian":
    st.header("📊 Analisis Potensi Kerugian vs ROI")
    col_a, col_b = st.columns(2)
    
     with col_a:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100_000_000)
        leak = st.slider("Estimasi Kebocoran (%)", 1, 20, 5)
        loss = omzet * (leak / 100)
        st.error(f"Potensi Kerugian: Rp {loss:,.0f} / bulan")
        
    with col_b:
        st.subheader("💡 Solusi V-GUARD")
        st.write("Dengan menutup celah kebocoran ini, investasi Anda akan kembali dalam waktu singkat.")
        # Tambahkan logika perhitungan BEP di sini jika perlu

elif menu == "Dashboard Client":
    st.info("Halaman ini dalam tahap pengembangan.")
    pass

    st.caption("V-GUARD AI: Secure Your Business, Optimize Your Profit.")
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
        # --- TAB 2: AI SQUAD (COMMAND & OVERRIDE) ---
        # --- TAB 2: AI SQUAD (COMMAND, OVERRIDE & GROWTH) ---
        with t2:
            st.subheader("🖥️ V-GUARD Elite AI Squad")
            
            # 1. Command Input
            cmd_ai = st.text_area("Instruksi Strategis Admin:", placeholder="Contoh: Analyst, audit transaksi Cabang Medan jam 10 pagi tadi...", key="cmd_t2")
            if st.button("Kirim Perintah ke Squad", key="btn_cmd_t2"):
                if cmd_ai:
                    with st.spinner("Executing Command..."):
                        # Fungsi simulasi response AI
                        st.info(f"SQUAD RESPONSE: Menjalankan perintah '{cmd_ai}'. Laporan akan muncul di Tab Audit.")

            st.divider()

            # 2. LIVE CHAT MONITORING & OVERRIDE
            st.markdown("### 👁️ Live Chat (24/7)")
            chat_container = st.container(border=True)
            with chat_container:
                st.caption("🔴 LIVE: Interaksi Klien #8829 (Cabang Surabaya)")
                st.chat_message("user").write("Halo, sistem V-SIGHT saya tidak muncul notifikasi di HP.")
                st.chat_message("assistant").write("Mohon maaf atas ketidaknyamanannya. Saya Concierge Agent. Sedang memeriksa sinkronisasi perangkat Anda...")
            
            st.write("**🕹️ Manual Override Mode**")
            msg_override = st.text_input("Balas sebagai Admin:", placeholder="Ketik pesan Bapak di sini...", key="ov_t2")
            
            c_ov1, c_ov2 = st.columns([1, 4])
            with c_ov1:
                if st.button("📤 Kirim Pesan", key="btn_ov_t2"):
                    if msg_override:
                        st.success("Pesan Terkirim via WA.")
            with c_ov2:
                st.info("💡 Override aktif: AI akan berhenti merespons sesi ini agar Bapak bisa bicara langsung.")

            st.divider()
            
            # 3. Status Agent (Visual Grid) - Dibuat Ringkas 5 Kolom
            st.markdown("### 👥 Squad AI AGENT")
            agents = [
                ("👁️ Visionary", "Online"), ("👂 Concierge", "Active"), 
                ("👄 Growth", "Online"), ("🤝 Liaison", "Online"), 
                ("🧠 Analyst", "Processing"), ("📈 Strategist", "Online"),
                ("🐕 Watchdog", "Online"), ("🛡️ Sentinel", "Online"), 
                ("⚖️ Legalist", "Idle"), ("💰 Treasurer", "Online")
            ]
            
            for i in range(0, 10, 5):
                cols = st.columns(5)
                for j, (name, status) in enumerate(agents[i:i+5]):
                    with cols[j]:
                        st.metric(name, status)

            st.divider()

            # 4. DIGITAL MARKETING COMMAND (Bapak minta ditaruh di sini)
            # Menggunakan expander agar hemat tempat
            with st.expander("🚀 GROWTH & MARKETING CENTER (FB, TikTok, IG, LinkedIn)", expanded=False):
                st.markdown("### 📢 Multi-Channel Marketing Control")
                
                # Baris Statistik Iklan
                m1, m2, m3 = st.columns(3)
                m1.metric("Ad Spend (MTD)", "Rp 4.5M", "-5%")
                m2.metric("Total Reach", "850K", "+15%")
                m3.metric("New Leads", "142", "+22%")

                st.divider()

                # Pengaturan & Leads
                col_grow_l, col_grow_r = st.columns([2, 1])
                
                with col_grow_l:
                    p_ads = st.multiselect("Target Platform:", ["FB", "IG", "TikTok", "LinkedIn", "Google"], 
                                         default=["FB", "TikTok"], key="p_t2_grow")
                    t_ads = st.text_input("Target Audience:", "Owner Franchise, Retailer Nasional", key="target_t2_grow")
                    b_ads = st.slider("Budget Harian (Rp):", 100000, 2000000, 500000, key="budget_t2_grow")
                    
                    if st.button("🔥 Jalankan Kampanye Sekarang", key="btn_run_t2_grow"):
                        st.success(f"Growth Agent: Kampanye aktif di {', '.join(p_ads)}!")

                with col_grow_r:
                    st.write("**🎯 Top Leads Today**")
                    st.caption("1. Bpk Andi - 62812xxx")
                    st.caption("2. Ibu Shinta - 62819xxx")
                    if st.button("📲 Auto Follow-up Leads", key="btn_af_t2_grow"):
                        st.toast("Concierge sedang mengirim perkenalan via WA...")

                # Preview Mini
                st.markdown("---")
                st.write("**🎨 Creative Preview**")
                pt1, pt2, pt3 = st.tabs(["Facebook", "TikTok", "LinkedIn"])
                with pt1:
                    st.caption("Copy: 'Pantau 100 cabang tanpa ribet. V-ULTRA Enterprise.'")
                with pt2:
                    st.caption("Video: CCTV deteksi fraud 3 detik (Ready)")
                with pt3:
                    st.caption("Chart: ROI V-GUARD untuk korporasi.")

            st.divider()
            st.caption("V-GUARD Unified Dashboard - Mr. Erwin Sinaga Executive Access")
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
        # --- TAB 10: OWNER COMMAND - NATIONAL REVENUE & PROFIT SHARING ---
        with t10:
            st.header("🏢 V-GUARD National Financial Control")
            st.markdown("Pusat pantauan omset nasional dan pembagian profit otomatis (Potongan 30% Ops di awal).")

            # 1. INPUT PENJUALAN NASIONAL (SIMULASI)
            with st.expander("📝 Input Penjualan Kolektif Nasional", expanded=True):
                c_in1, c_in2, c_in3, c_in4 = st.columns(4)
                v_lite = c_in1.number_input("Unit V-LITE:", min_value=0, value=10)
                v_pro = c_in2.number_input("Unit V-PRO:", min_value=0, value=5)
                v_sight = c_in3.number_input("Unit V-SIGHT:", min_value=0, value=2)
                v_ultra = c_in4.number_input("Unit V-ULTRA:", min_value=0, value=1)
                
                tipe_fee = st.selectbox("Pilih Jenis Transaksi:", ["Setup Fee (Pasang Baru)", "Monthly Recurring (Langganan)"])

            # 2. DATA HARGA & LOGIKA (REFERENSI EXCEL)
            if tipe_fee == "Setup Fee (Pasang Baru)":
                prices = {"lite": 1500000, "pro": 3000000, "sight": 7500000, "ultra": 15000000}
                net_profit_pct = 0.50 # 50% dari sisa setelah potongan 30%
                porsi_tim = {
                    "CEO (Erwin Sinaga)": 0.25, "CSO (Christin)": 0.20, "CTO (Technical)": 0.15,
                    "COO (Ops)": 0.10, "Manager": 0.10, "Digital Marketing": 0.10, "Admin": 0.10
                }
            else:
                prices = {"lite": 750000, "pro": 1500000, "sight": 3500000, "ultra": 10000000}
                net_profit_pct = 0.80 # 80% dari sisa setelah potongan 30%
                porsi_tim = {
                    "CEO (Erwin Sinaga)": 0.60, "CSO (Christin)": 0.05, "CTO (Technical)": 0.10,
                    "COO (Ops)": 0.05, "Manager": 0.10, "Digital Marketing": 0.05, "Admin": 0.05
                }

            # 3. KALKULASI WATERFALL (STRATEGI PAK ERWIN)
            gross_nasional = (v_lite * prices["lite"]) + (v_pro * prices["pro"]) + \
                             (v_sight * prices["sight"]) + (v_ultra * prices["ultra"])
            
            # POTONG 30% DARI OMSET KOTOR (UNTUK SERVER, IKLAN, CASH V-GUARD)
            biaya_ops_30 = gross_nasional * 0.30
            sisa_setelah_ops = gross_nasional - biaya_ops_30
            
            # TOTAL PROFIT YANG SIAP DIBAGIKAN KE TIM
            total_profit_sharing = sisa_setelah_ops * net_profit_pct

            # 4. TAMPILAN DASHBOARD UTAMA
            st.divider()
            m1, m2, m3 = st.columns(3)
            m1.metric("TOTAL OMSET NASIONAL", f"Rp {gross_nasional:,.0f}")
            m2.metric("CADANGAN V-GUARD (30%)", f"Rp {biaya_ops_30:,.0f}", delta="-30% Fixed", delta_color="inverse")
            m3.metric("TOTAL PROFIT SHARING", f"Rp {total_profit_sharing:,.0f}")

            # 5. RINCIAN BAGI HASIL TIM
            st.subheader("👥 Distribusi Profit Sharing Tim")
            data_tim = []
            for role, pct in porsi_tim.items():
                nominal = total_profit_sharing * pct
                data_tim.append({
                    "Posisi": role,
                    "Porsi (%)": f"{pct*100:.0f}%",
                    "Penerimaan Bersih": f"Rp {nominal:,.0f}"
                })
            st.table(data_tim)

            # 6. KESIMPULAN OWNER
            st.info(f"**Total Pendapatan Pak Erwin (CEO):** Rp { (total_profit_sharing * porsi_tim['CEO (Erwin Sinaga)']) + biaya_ops_30 :,.0f} (Termasuk Cadangan Ops)")
            # Tambahkan ini di bagian paling akhir kode Python Anda

   # --- FOOTER COPYRIGHT (Muncul di Semua Halaman) ---
st.markdown("<br><br>", unsafe_allow_html=True) # Memberi jarak agar tidak menempel ke konten
st.markdown(
    """
    <div style="text-align: center; color: #666; font-size: 12px; padding-bottom: 20px;">
        © 2026 V-GUARD AI Intelligence | Digitizing Trust, Eliminating Leakage
    </div>
    """, 
    unsafe_allow_html=True
)
