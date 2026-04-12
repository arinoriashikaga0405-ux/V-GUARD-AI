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

if menu == "Home":
    st.header("🛡️ V-Guard AI Intelligence")
    st.subheader("Digitizing Trust, Eliminating Leakage")
    
    st.markdown("---")
    
    # Bagian Visi & Misi
    col_v, col_m = st.columns(2)
    with col_v:
        st.markdown("### 🎯 Visi")
        st.write("Menjadi standar global dalam otomatisasi integritas bisnis melalui teknologi AI yang jujur, transparan, dan efisien.")
    
    with col_m:
        st.markdown("### 🚀 Misi")
        st.write("Menghilangkan kebocoran operasional secara real-time dan membangun kepercayaan digital bagi para pelaku usaha.")

    st.divider()

    # Profil Founder di bawah Visi & Misi
    col_profile1, col_profile2 = st.columns([1, 2])
    
    with col_profile1:
        # Menggunakan file erwin.jpg yang sudah Bapak siapkan
        try:
            st.image("erwin.jpg", caption="Erwin Sinaga - Founder & CEO")
        except:
            st.warning("Foto 'erwin.jpg' belum ditemukan di folder GitHub. Pastikan nama file sudah benar.")
        
    with col_profile2:
        st.subheader("Profil Founder")
        st.markdown("""
        **Erwin Sinaga** adalah Founder & CEO dari **V-Guard AI Intelligence**. 
        Beliau membangun V-Guard dengan filosofi *"Digitizing Trust"*, di mana teknologi 
        bukan sekadar alat, melainkan fondasi kepercayaan dalam setiap transaksi bisnis.
        
        Dengan fokus pada *Eliminating Leakage*, beliau merancang sistem yang mampu 
        mendeteksi anomali secara otonom, memastikan setiap rupiah dan aset milik 
        pengusaha terlindungi 24/7 tanpa beban biaya Cloud yang berlebihan.
        
        V-Guard adalah manifestasi dari pengalaman beliau dalam menyatukan 
        strategi produk yang tajam dengan efisiensi teknologi masa depan.
        """)

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
