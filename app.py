import streamlit as st
import os
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE & SECURITY ---
i# GANTI KODE LAMA:
# if "GEMINI_API_KEY" in st.secrets:

# MENJADI KODE INI:
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model_vguard = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.warning("⚠️ API Key tidak ditemukan di Variables Railway.")
except Exception:
    st.warning("⚠️ Variabel sistem (Secrets) belum dikonfigurasi di Railway.")

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

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
    st.header("Visi & Misi: Digitizing Trust, Eliminating Leakage")
    
    # Layout Kolom untuk Foto dan Deskripsi (250+ kata)
    col_img, col_txt = st.columns([1, 2])
    
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga - Founder & CEO", use_container_width=True)
        else:
            st.info("File erwin.jpg tidak ditemukan.")

    with col_txt:
        st.markdown("""
        <div style="text-align: justify; line-height: 1.7; font-size: 16px; color: #d1d5db;">
        <b>V-Guard AI Intelligence</b> lahir dari urgensi integritas finansial di era transformasi digital yang berkembang pesat. Sebagai entitas yang dipimpin oleh profesional dengan pengalaman mendalam di industri perbankan dan manajemen aset, kami memahami bahwa setiap celah terkecil dalam sistem operasional merupakan potensi kerugian fatal bagi keberlangsungan sebuah bisnis. Misi utama kami adalah mendigitalisasi kepercayaan (Digital Trust) melalui pembuktian matematis dan audit cerdas yang bekerja secara otonom 24 jam nonstop tanpa kompromi sedikit pun.<br><br>
        Kami percaya bahwa kejujuran sistem tidak boleh hanya bergantung pada pengawasan manusia yang secara alami memiliki keterbatasan fisik dan kognitif, melainkan harus dibangun di atas fondasi teknologi AI yang presisi dan tidak memihak. Melalui ekosistem V-Guard, kami mengintegrasikan analisis data perbankan (VCS), visi komputer tingkat lanjut, dan deteksi anomali prediktif untuk menciptakan lingkungan bisnis yang bersih dari segala bentuk kecurangan (Fraud). Strategi kami adalah memberikan transparansi mutlak kepada pemilik bisnis melalui laporan yang akurat, terverifikasi, dan disajikan secara real-time.<br><br>
        Visi besar kami adalah menjadi standar global dalam kampanye "Eliminating Leakage", di mana setiap pemilik bisnis—mulai dari skala UMKM hingga korporasi multinasional—dapat menjalankan operasional mereka dengan ketenangan pikiran total karena mengetahui bahwa setiap Rupiah yang masuk diawasi oleh kecerdasan buatan yang tak kenal lelah. V-Guard bukan sekadar perangkat lunak manajemen, melainkan benteng pertahanan terakhir bagi aset berharga dan masa depan investasi Anda. Kami hadir untuk mengeliminasi kebocoran, mengoptimalkan profitabilitas, dan menjaga warisan bisnis Anda tetap utuh melalui inovasi teknologi yang melampaui standar audit konvensional yang ada saat ini. Kami berkomitmen untuk memastikan bahwa investasi Anda terlindungi dari segala bentuk anomali yang merugikan.
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

elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center")

    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False

    if not st.session_state.admin_logged_in:
        admin_input = st.text_input("Administrator Password", type="password")
        if admin_input == "w1nbju8282":
            st.session_state.admin_logged_in = True
            st.rerun()
        elif admin_input != "":
            st.error("Akses Ditolak.")
    
    else:
        # Dashboard Dashboard Khusus Admin
        st.success("Akses Eksekutif Aktif: Selamat Datang Pak Erwin")
        
        st.markdown("### 📊 Ringkasan Eksekutif & AI Squad")
        
        # Metrik Utama (Sesuai SOP)
        c_api1, c_api2, c_api3 = st.columns(3)
        with c_api1:
            st.metric("Anggaran API Bulanan", "Rp 10.000.000")
        with c_api2:
            st.metric("Biaya API Terpakai", "Rp 2.000.000", delta="-20% (Optimized)", delta_color="normal")
        with c_api3:
            st.metric("Efisiensi Sistem", "88%", delta="Sesuai Target")
        
        # Progress Bar Kuota API 20%
        st.write("**Monitoring Kuota API Cloud**")
        st.progress(0.20, text="Penggunaan Kuota: 20%")

        st.divider()
        
        # AI Squad Agent Monitoring
        st.subheader("🤖 V-Guard AI Squad Status")
        sq1, sq2, sq3, sq4 = st.columns(4)
        with sq1:
            st.info("🕵️ **Sentinel**\n\nStatus: Monitoring Fraud")
        with sq2:
            st.info("💰 **Auditor**\n\nStatus: VCS Sync Active")
        with sq3:
            st.info("📦 **Stocker**\n\nStatus: Visual AI Check")
        with sq4:
            st.info("📄 **Invoicer**\n\nStatus: H-7 Ready")

        if st.button("Log Out"):
            st.session_state.admin_logged_in = False
            st.rerun()

st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026</small></center>", unsafe_allow_html=True)
