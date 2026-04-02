import streamlit as st
import os
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE AI ---
GEMINI_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
genai.configure(api_key=GEMINI_API_KEY)
model_gemini = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Premium
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;'><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGASI UTAMA", [
        "Visi & Misi", 
        "Arsitektur AI",
        "Produk & Layanan", 
        "Analisis ROI Kerugian", 
        "Portal Klien (VCS)", 
        "Admin Control Center"
    ])

# --- 4. LOGIKA MENU ---

if menu == "Visi & Misi":
    st.header("Visi & Misi V-Guard AI Intelligence")
    st.markdown("""
    <div style="text-align: justify; line-height: 1.6;">
    V-Guard AI Intelligence lahir dari urgensi integritas finansial di era transformasi digital. Sebagai entitas yang dipimpin oleh profesional dengan pengalaman lebih dari satu dekade di industri perbankan dan manajemen aset, kami memahami bahwa celah terkecil dalam sistem operasional adalah potensi kerugian fatal bagi sebuah bisnis. Misi utama kami adalah mendigitalisasi kepercayaan (Digital Trust) melalui pembuktian matematis dan audit cerdas yang bekerja secara otonom 24 jam nonstop.<br><br>
    Kami percaya bahwa kejujuran sistem tidak boleh bergantung pada pengawasan manusia yang terbatas, melainkan harus dibangun di atas fondasi teknologi AI yang presisi. Melalui ekosistem V-Guard, kami mengintegrasikan analisis data perbankan (VCS), visi komputer (YOLO), dan deteksi anomali prediktif untuk menciptakan lingkungan bisnis yang bersih dari kecurangan (Fraud).<br><br>
    Visi kami adalah menjadi standar global dalam "Integrity Assurance", di mana setiap pemilik bisnis, mulai dari UMKM hingga korporasi besar, dapat tidur dengan tenang karena mengetahui setiap Rupiah dalam operasional mereka diawasi oleh kecerdasan buatan yang tak kenal lelah. V-Guard bukan sekadar software, melainkan benteng pertahanan terakhir bagi aset dan masa depan bisnis Anda. Kami hadir untuk mengeliminasi kebocoran, mengoptimalkan profit, dan menjaga warisan bisnis Anda tetap utuh melalui transparansi yang mutlak.
    </div>
    """, unsafe_allow_html=True)

elif menu == "Arsitektur AI":
    st.header("🧠 The Core Brain & AI Ecosystem")
    st.info("Integrasi 7 Engine AI Global dalam satu Dashboard:")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- **Google Gemini AI**: Analis utama laporan kompleks.\n- **MindBridge**: Deteksi pola fraud akuntansi.\n- **DataRobot**: Forecasting risiko operasional.\n- **Alteryx**: Otomasi alur data CCTV & POS.")
    with col2:
        st.markdown("- **Workday Adaptive**: Simulasi finansial cerdas.\n- **Numeric.ai**: Notifikasi kesehatan harian.\n- **YOLO / Vision AI**: Mata digital kasir visual.\n- **NLP Bot**: Chatbox audit otomatis.")

elif menu == "Produk & Layanan":
    st.header("🛡️ Portfolio Layanan V-Guard AI Intelligence")
    wa_number = "6282122190885"
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        with st.container(border=True):
            st.markdown("### 📦 V-LITE")
            st.caption("🎯 Target: Mikro / 1 Kasir")
            st.markdown("- AI Fraud Dasar\n- Daily Summary\n- PDF Report\n- Cloud 30 Hari")
            st.info("**Pasang:** 1.5 Jt\n**Bulan:** 1 Jt")
            st.link_button("Pilih V-LITE", f"https://wa.me/{wa_number}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20V-LITE")

    with c2:
        with st.container(border=True):
            st.markdown("### 📦 V-PRO")
            st.caption("🎯 Target: Retail & Kafe")
            st.markdown("- VCS Integration\n- Bank Statement Audit\n- Input Excel/CSV/PDF\n- H-7 Auto-Invoice")
            st.info("**Pasang:** 3 Jt\n**Bulan:** 2.5 Jt")
            st.link_button("Pilih V-PRO", f"https://wa.me/{wa_number}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20V-PRO")

    with c3:
        with st.container(border=True):
            st.markdown("### 📦 V-SIGHT")
            st.caption("🎯 Target: Gudang & Toko")
            st.markdown("- CCTV AI Behavior\n- Visual Cashier Audit\n- Real-Time Stock\n- Fraud Alarm (🚨)")
            st.info("**Pasang:** 5 Jt\n**Bulan:** 5 Jt")
            st.link_button("Pilih V-SIGHT", f"https://wa.me/{wa_number}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20V-SIGHT")

    with c4:
        with st.container(border=True):
            st.markdown("### 📦 V-ENTERPRISE")
            st.caption("🎯 Target: Korporasi")
            st.markdown("- The Core Brain\n- Forensic AI (1 Thn)\n- Dedicated Server\n- Custom AI SOP")
            st.info("**Pasang:** 10 Jt\n**Bulan:** 10 Jt")
            st.link_button("Pilih V-ENTERPRISE", f"https://wa.me/{wa_number}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20V-ENTERPRISE")

elif menu == "Analisis ROI Kerugian":
    st.header("📊 Analisis Potensi Kerugian vs ROI")
    col_a, col_b = st.columns(2)
    with col_a:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000, step=10000000)
        leak = st.slider("Estimasi Kebocoran / Fraud (%)", 1, 20, 5)
        loss = omzet * (leak / 100)
        st.error(f"Potensi Kerugian: Rp {loss:,.0f} / bulan")
    with col_b:
        biaya = st.selectbox("Pilih Rencana Investasi Paket", [1000000, 2500000, 5000000, 10000000])
        saved = loss - biaya
        st.success(f"Profit Diselamatkan: Rp {saved:,.0f} / bln")
        roi_val = (saved/biaya)*100 if saved > 0 else 0
        st.metric("ROI Investasi", f"{roi_val:.0f}%")

elif menu == "Portal Klien (VCS)":
    st.header("Portal Klien & Audit VCS")
    col_order, col_upload = st.columns(2)
    with col_order:
        st.subheader("📝 Form Order & Registrasi")
        with st.container(border=True):
            st.text_input("Nama Usaha")
            st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.button("Kirim Registrasi")
    with col_upload:
        st.subheader("📤 Upload Data Mentah (Audit)")
        st.info("Mendukung format: JPG, PDF, Excel (XLSX/CSV), VCS Data")
        uploaded = st.file_uploader("Seret file ke sini", type=['jpg','pdf','xlsx','xls','csv'], accept_multiple_files=True)
        if uploaded:
            st.success(f"{len(uploaded)} File siap diproses oleh AI Audit.")

elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center - The Core Brain")
    admin_input = st.text_input("Administrator Password", type="password")
    if admin_input == "adminvguard2026":
        t1, t2, t3 = st.tabs(["📊 VCS Dashboard", "👤 Kelola User", "🚨 Alarm"])
        with t1:
            st.metric("Total Kasir", "Rp 125.450.000")
            st.metric("Dana Bank (VCS Sinkron)", "Rp 125.450.000", delta="Sinkron 100%")
        with t2:
            st.text_input("ID Klien Baru")
            st.button("Aktifkan Akun")
        with t3:
            st.error("🚨 Alarm Fraud Digital: AKTIF")
    elif admin_input != "":
        st.error("Password Salah.")

# --- 5. FOOTER ---
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026 | Built for Digital Trust Integrity</small></center>", unsafe_allow_html=True)
