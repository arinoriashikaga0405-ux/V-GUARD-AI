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
    # 1. Cek status login (Pastikan IF ini di posisi awal)
    if not st.session_state.get('admin_logged_in', False):
        st.header("🔐 Admin Control Center")
        
        # Input password
        admin_input = st.text_input("Password", type="password", key="vguard_admin_main")
        
        if admin_input == "w1nbju8282": 
            st.session_state.admin_logged_in = True
            st.rerun()
        elif admin_input != "":
            st.error("Invalid Key")
        st.stop() # Mengunci halaman jika belum login

    # 2. SEJAJARKAN ELSE INI DENGAN 'if not' DI ATAS (Baris 164)
    else: 
        # Tombol Logout di pojok kanan atas
        c_out1, c_out2 = st.columns([9, 1])
        with c_out2:
            if st.button("🚪 Out", key="logout_btn"):
                st.session_state.admin_logged_in = False
                st.rerun()
        
        st.header("🎮 V-GUARD: Admin Control Center")
        # ... lanjut ke Tab dan isi lainnya ...
        
        st.header("🎮 V-GUARD: Admin Control Center")
        st.divider()

        # --- DEFINISI 9 TAB UTAMA ---
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = st.tabs([
            "👥 Aktivasi", "🖥️ AI Squad", "⚙️ Integrasi", 
            "📊 Audit", "🛡️ V-SIGHT", "🚨 Alarm", 
            "📈 Profit", "💾 Owner", "💎 V-ULTRA"
        ])

        # --- TAB 1: AKTIVASI KLIEN ---
        # --- TAB 1: AKTIVASI KLIEN ---
        with t1:
            st.subheader("📝 Registrasi & Aktivasi Klien")
            
            # 1. LETAKKAN CSS DI SINI (Di dalam 'with t1')
            st.markdown("""
                <style>
                
                }
                div.stButton > button:hover {
                    background-color: #f0f0f0 !important;
                    color: black !important;
                }
                </style>
            """, unsafe_allow_html=True)

            ca, cb = st.columns(2)
            with ca:
                nama_k = st.text_input("Nama Perusahaan:", key="nk_t1")
                wa_k = st.text_input("WhatsApp (62...):", key="wa_t1")
            with cb:
                prod_v = st.selectbox("Pilih Produk:", ["🛡️ V-LITE", "👁️ V-PRO", "🚨 V-SIGHT", "💎 V-ULTRA"], key="prod_t1")
                st.date_input("Tanggal Aktivasi", key="tgl_t1")

            # 2. HAPUS EMOJI ROKET DI SINI
            if st.button("Aktivasi & Kirim Akses", key="btn_act"):
                if nama_k and wa_k:
                    msg = f"Halo {nama_k}, Akun V-GUARD {prod_v} Anda AKTIF."
                    st.success(f"✅ Akun {nama_k} Aktif!")
                    st.markdown(f"[👉 KIRIM WA](https://wa.me/{wa_k}?text={msg.replace(' ', '%20')})")

        # --- TAB 2: 10 AI AGENT SQUAD ---
        with t2:
            st.subheader("🖥️ V-GUARD Elite Squad (10 Agents Active)")
            agents = [
                ("👁️ Visionary", "CCTV Monitoring"), ("👂 Concierge", "Client Support"),
                ("👄 Growth", "Revenue Boost"), ("🤝 Liaison", "API & Connections"),
                ("🧠 Analyst", "Data Forensic"), ("📈 Strategist", "Business Plan"),
                ("🐕 Watchdog", "Fraud Detection"), ("🛡️ Sentinel", "System Security"),
                ("⚖️ Legalist", "Compliance"), ("💰 Treasurer", "Cashflow Audit")
            ]
            
            # Grid 5 Kolom agar rapi
            cols = st.columns(5)
            for i, (n, task) in enumerate(agents):
                with cols[i % 5]:
                    st.info(f"**{n}**\n\n`{task}`")
            
            st.divider()
            q_ai = st.text_input("Command Center (Instruksi ke Semua Agent):", key="q_admin")
            if st.button("Jalankan Operasi AI", key="btn_q"):
                st.write(vguard_ai_engine("V-GUARD COMMANDER", q_ai))

        # --- TAB 3: INTEGRASI API (THE LIAISON) ---
        with t3:
            st.subheader("⚙️ API Bridge: Bank & POS Integration")
            col_api1, col_api2 = st.columns(2)
            with col_api1:
                provider = st.selectbox("Pilih Koneksi:", ["BCA Business", "Moka POS", "Majoo", "Mandiri API"])
            with col_api2:
                st.text_input("API Key", type="password", value="HIDDEN_KEY_12345")
            
            if st.button("🔌 Hubungkan Sekarang", key="btn_api"):
                st.success(f"**THE LIAISON:** Berhasil menghubungkan database {provider} ke V-GUARD.")

        # --- TAB 5: V-SIGHT (THE VISIONARY) ---
        with t5:
            st.subheader("👁️ V-SIGHT: Visual Behavior AI")
            c_vid1, c_vid2 = st.columns(2)
            with c_vid1:
                st.image("https://img.freepik.com/free-photo/security-camera-detecting-thief-store_23-2150914187.jpg", caption="LIVE: Kasir Utama")
            with c_vid2:
                st.image("https://img.freepik.com/free-photo/warehouse-management-system-concept_23-2148923140.jpg", caption="LIVE: Gudang A")
            
            st.warning("**THE VISIONARY:** Mendeteksi pembukaan laci kasir tanpa input transaksi pada 14:05.")

        # --- TAB 8: OWNER (KODE: w1nw1n8282) ---
        with t8:
            st.header("💾 Owner Strategic Center")
            o_key = st.text_input("Kode Otoritas:", type="password", key="okey_t8")
            if o_key == "w1nw1n8282":
                st.success("Halo Pak Erwin Sinaga.")
                omz = st.number_input("Input Omzet:", value=100000000)
                st.metric("Profit Bersih Bapak (Net 60%)", f"Rp {omz * 0.60:,.0f}")
                if st.button("📊 Analisis THE STRATEGIST"):
                    st.info(vguard_ai_engine("THE STRATEGIST", f"Omzet {omz}, berikan strategi profit."))
            elif o_key != "": st.error("Akses Ditolak.")

        # --- TAB LAINNYA (PLACEHOLDER) ---
        with t4: st.write("Pusat Audit Dokumen Aktif.")
        with t6: st.write("🚨 Alarm: Tidak ada anomali kritis.")
        with t7: st.write("📈 Performa: Efisiensi meningkat 12%.")
        with t9: st.write("💎 V-ULTRA: Dedicated Server Active.")
