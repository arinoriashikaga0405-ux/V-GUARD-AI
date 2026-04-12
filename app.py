import streamlit as st

# --- 1. KONFIGURASI HALAMAN (Wajib di Paling Atas) ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# --- 2. INITIALIZE SESSION STATE (Agar tidak AttributeError) ---
if 'auth_status' not in st.session_state:
    st.session_state.auth_status = False

if 'admin_logged_in' not in st.session_state:
    st.session_state.admin_logged_in = False

if 'client_info' not in st.session_state:
    st.session_state.client_info = {"nama": "User", "paket": "V-LITE"}

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Main Menu", ["Home", "Produk & Layanan", "Portal Klien", "Admin Control Center"])
    st.divider()
    st.caption("V-Guard Intelligence v1.0")

# --- 4. LOGIKA MENU ---

if menu == "Visi & Misi":
    # 1. Header & Slogan Utama
    st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <h1 style="color: #white; margin-bottom: 0;">🛡️ V-Guard AI Intelligence</h1>
            <h3 style="color: #238636; font-style: italic; font-weight: 400; margin-top: 5px;">
                "Digitizing Trust, Eliminating Leakage"
            </h3>
        </div>
        <hr style="border: 0.5px solid #30363d;">
    """, unsafe_allow_html=True)

    # 2. Konten Utama (Foto & Narasi)
    col_img, col_txt = st.columns([1, 2], gap="large")
    
    with col_img:
        if os.path.exists("erwin.jpg"):
            # Bingkai foto agar terlihat lebih premium
            st.markdown("""
                <div style="border: 2px solid #238636; border-radius: 15px; padding: 5px;">
            """, unsafe_allow_html=True)
            st.image("erwin.jpg", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("""
                <div style="text-align: center; margin-top: 10px;">
                    <h4 style="margin-bottom: 0; color: white;">Erwin Sinaga</h4>
                    <p style="color: #8892b0; font-size: 14px;">Founder & CEO V-Guard AI</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.info("File erwin.jpg tidak ditemukan.")

    with col_txt:
        # Narasi Profil & Visi dengan styling tipografi yang kuat
        st.markdown("""
            <div style="text-align: justify; line-height: 1.8; font-size: 17px; color: #e6f1ff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                <p>
                <span style="font-size: 24px; color: #238636; font-weight: bold;">V-Guard AI Intelligence</span> lahir dari urgensi integritas finansial di era transformasi digital. 
                Sebagai entitas yang dipimpin oleh profesional dengan pengalaman lebih dari satu dekade di industri perbankan dan manajemen aset, 
                kami memahami bahwa celah terkecil dalam sistem operasional adalah potensi kerugian fatal bagi sebuah bisnis.
                </p>
                
                <p>
                Misi utama kami adalah <b>mendigitalisasi kepercayaan (Digital Trust)</b> melalui pembuktian matematis dan audit cerdas 
                 yang bekerja secara otonom 24 jam nonstop tanpa kompromi. Kami percaya bahwa kejujuran sistem tidak boleh hanya bergantung 
                 pada pengawasan manusia yang memiliki keterbatasan, melainkan harus dibangun di atas fondasi teknologi AI yang presisi.
                </p>
                
                <p style="background-color: #112240; padding: 15px; border-radius: 10px; border-left: 4px solid #238636;">
                <i>"V-Guard bukan sekadar perangkat lunak, melainkan benteng pertahanan terakhir bagi aset dan masa depan investasi Anda."</i>
                </p>
                
                <p>
                Visi kami adalah menjadi standar global dalam <b>"Eliminating Leakage"</b>, di mana setiap pemilik bisnis—mulai dari UMKM hingga 
                korporasi besar—dapat menjalankan operasional mereka dengan tenang karena setiap Rupiah diawasi oleh kecerdasan buatan yang tak kenal lelah. 
                Kami hadir untuk mengeliminasi kebocoran, mengoptimalkan profitabilitas, dan menjaga warisan bisnis Anda tetap utuh melalui inovasi 
                teknologi yang melampaui standar audit konvensional.
                </p>
            </div>
        """, unsafe_allow_html=True)

    # 3. Footer Tambahan
    st.divider()
    st.caption("Filosofi V-Guard AI: Integritas Matematis untuk Keberlanjutan Bisnis.")

    st.info("💡 Gunakan menu di samping untuk mengeksplorasi fitur Dashboard dan Portal Klien.")

elif menu == "Produk & Layanan":
    st.header("📦 Paket Layanan V-Guard AI")
    
    # Tabel Perbandingan Eksekutif
    st.markdown("---")
    st.subheader("📊 Tabel Perbandingan Eksekutif")
    st.markdown("""
| Fitur Utama | V-LITE | V-PRO | V-SIGHT | V-ULTRA |
| :--- | :---: | :---: | :---: | :---: |
| **Integrasi Bank (VCS)** | - | ✅ Ya | ✅ Ya | ✅ Ya |
| **Analisa Fraud AI** | Dasar | Menengah | Tinggi | Real-time |
""")
    st.caption("Semua paket sudah termasuk update sistem keamanan secara berkala.")

elif menu == "Portal Klien":
    st.header("🔑 Portal Klien V-Guard AI")
    
    if not st.session_state.get('auth_status', False):
        c_reg, c_log = st.columns(2)
        with c_reg:
            st.subheader("📝 Form Order Baru")
            st.text_input("Nama Pelanggan", key="reg_nama")
            st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ULTRA"], key="reg_paket")
            if st.button("Kirim Registrasi"):
                st.success("Data terkirim. Menunggu aktivasi Admin.")
        
        with c_log:
            st.subheader("🔑 Login Dashboard")
            u_id = st.text_input("ID Klien", key="log_id")
            u_token = st.text_input("Token Akses", type="password", key="log_token")
            if st.button("Masuk"):
                if u_id == "admin" and u_token == "123":
                    st.session_state.auth_status = True
                    st.session_state.client_info = {"nama": "Bapak Erwin", "paket": "V-ULTRA"}
                    st.rerun()
                else:
                    st.error("ID atau Token salah.")
    else:
        info = st.session_state.get('client_info')
        st.subheader(f"📊 Dashboard Utama - {info['nama']}")
        st.info(f"Paket Aktif: **{info['paket']}**")
        
        # LOGIKA FILTER TRANSAKSI (Efisien < 20%)
        st.write("---")
        st.subheader("⚡ Real-time Fraud Filter")
        t_total = st.number_input("Input Nilai Transaksi (Rp)", value=0)
        
        if st.button("Proses Transaksi"):
            if t_total > 5000000:
                with st.spinner("Anomali Terdeteksi! Mengirim data ke Cloud AI..."):
                    st.warning("⚠️ ALERT: Transaksi High-Value Terdeteksi & Dicatat Cloud.")
            else:
                st.success("✅ PASS: Transaksi Normal (Disimpan Lokal - Hemat API 100%)")

        if st.button("🔌 Logout Portal"):
            st.session_state.auth_status = False
            st.rerun()

elif menu == "Admin Control Center":
    st.header("🛡️ V-Guard Executive Panel")
    
    if not st.session_state.get('admin_logged_in', False):
        admin_pwd = st.text_input("Administrator Password", type="password", key="admin_pwd_field")
        if admin_pwd == "w1nbju8282":
            st.session_state.admin_logged_in = True
            st.rerun()
        elif admin_pwd != "":
            st.error("Password Salah")
    else:
        c_top1, c_top2 = st.columns([4, 1])
        with c_top2:
            if st.button("Log Out Admin"):
                st.session_state.admin_logged_in = False
                st.rerun()
        
        st.divider()
        st.markdown("### 📊 Business Intelligence & API Strategy (Capped 20%)")
        
        omset_kotor = 50000000 
        plafon_api = omset_kotor * 0.20 
        biaya_api_realitas = 1850000 
        
        c_api1, c_api2, c_api3 = st.columns(3)
        with c_api1: st.metric("Budget API (20% Omset)", f"Rp {plafon_api:,.0f}")
        with c_api2: st.metric("Used API (Current)", f"Rp {biaya_api_realitas:,.0f}", delta="-11.5% (Safe)")
        with c_api3: st.metric("Efficiency Rate", "92.5%")
        
        persentase_pakai = (biaya_api_realitas / plafon_api)
        st.progress(persentase_pakai, text=f"Konsumsi API: {persentase_pakai*100:.1f}% dari Plafon Omset")
        
        st.divider()
        st.subheader("🤖 V-Guard AI Squad Agents (Filtering Mode)")
        
        sq1, sq2, sq3, sq4 = st.columns(4)
        with sq1:
            with st.container(border=True):
                st.markdown("🕵️ **Sentinel**")
                st.info("Filtering")
        with sq2:
            with st.container(border=True):
                st.markdown("💰 **Auditor**")
                st.info("VCS Sync")
        with sq3:
            with st.container(border=True):
                st.markdown("📦 **Stocker**")
                st.info("Vision Scan")
        with sq4:
            with st.container(border=True):
                st.markdown("📄 **Invoicer**")
                st.info("Auto Bill")

        st.divider()

        # --- 10 TABS STRATEGIS ---
        tabs = st.tabs(["👤 Aktivasi", "🖥️ Ekosistem AI", "📈 ROI Tracker", "🛡️ Security", "💾 Backup", "🌐 Jaringan", "📊 Analytics", "📩 Marketing", "💎 V-ULTRA", "⚙️ Config"])
        
        with tabs[0]:
            st.subheader("Manajemen Aktivasi Klien")
            c1, c2 = st.columns(2)
            with c1: st.text_input("Username Klien")
            with c2: st.selectbox("Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ULTRA"])
            if st.button("Aktifkan Akun & Lisensi"):
                st.success("Lisensi Aktif!")

# --- FOOTER ---
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026</small></center>", unsafe_allow_html=True)
