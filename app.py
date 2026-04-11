import streamlit as st
import os
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE & SECURITY ---
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
    system_instruction="Analisa transaksi. Jika Fraud/Anomali balas 'ALERT'. Jika normal balas 'PASS'."
)

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; height: 45px; }
    .stTextInput>div>div>input { background-color: #1e293b; color: white; }
    div[data-testid="stMetricValue"] { font-size: 28px; color: #e74c3c; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA V-GUARD (PENYARING BIAYA API 20%) ---
def proses_transaksi(total, data_input):
    if total < 5000000:
        return "PASS (Auto)", False
    response = model_gemini.generate_content(f"Cek: {data_input}")
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
        "V-LITE": ["Mikro / 1 Kasir", "1.5 Jt", "750 rb", "AI Fraud Detector Dasar, Daily WA/Email Summary, Monthly PDF Report"],
        "V-PRO": ["Retail & Kafe", "3 Jt", "1.5 Jt", "VCS Integration, Bank Statement Audit, Input Excel/CSV/PDF, H-7 Auto-Invoice"],
        "V-SIGHT": ["Gudang & Toko", "7,5 Jt", "3,5 Jt", "CCTV AI Behavior, Visual Cashier Audit, Real-Time Stock, Fraud Alarm (🚨)"],
        "V-ENTERPRISE": ["Korporasi", "15 Jt", "10 Jt", "The Core Brain, Forensic AI (1 Thn), Dedicated Server, Custom AI SOP"]
    }
    
    for i, (name, details) in enumerate(packages.items()):
        with [c1, c2, c3, c4][i]:
            with st.container(border=True):
                st.markdown(f"### 📦 {name}")
                st.caption(f"🎯 Target: {details[0]}")
                st.markdown(f"- {details[3]}")
                st.info(f"**Pasang:** {details[1]}\n\n**Bulan:** {details[2]}")
                st.link_button(f"Pilih {name}", f"https://wa.me/{wa_number}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20dengan%20paket%20*{name}*%20V-Guard%20AI.")

    st.markdown("---")
    st.subheader("📊 Tabel Perbandingan Eksekutif")
    st.markdown("""
    | Fitur Utama | V-LITE | V-PRO | V-SIGHT | V-ENTERPRISE |
    | :--- | :---: | :---: | :---: | :---: |
    | **Level Audit AI** | Standar | Advanced | Visual AI | Forensic |
    | **Integrasi Bank (VCS)** | - | ✅ Ya | ✅ Ya | ✅ Ya |
    | **Input Excel/PDF** | - | ✅ Ya | ✅ Ya | ✅ Ya |
    | **CCTV Vision AI** | - | - | ✅ Ya | ✅ Ya |
    | **Biaya Pemasaran** | 1.5 Jt | 3 Jt | 7.5 Jt | 15 Jt |
    | **Biaya Langganan** | 750 rb | 1.5 Jt | 3,5 Jt | 10 Jt |
    """)

elif menu == "ROI Kerugian Klien":
    st.header("📊 Analisis Potensi Kerugian vs ROI")
    col_a, col_b = st.columns(2)
    with col_a:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
        leak = st.slider("Estimasi Kebocoran (%)", 1, 20, 5)
        loss = omzet * (leak / 100)
        st.error(f"Potensi Kerugian: Rp {loss:,.0f} / bulan")
    with col_b:
        opsi_biaya = {
            "Rp 750.000 (V-LITE)": 750000,
            "Rp 1.500.000 (V-PRO)": 1500000,
            "Rp 3.500.000 (V-SIGHT)": 3500000,
            "Rp 10.000.000 (V-ENTERPRISE)": 10000000
        }
        pilihan_label = st.selectbox("Pilih Paket Investasi (Biaya Langganan)", list(opsi_biaya.keys()))
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
    st.header("⚙️ Admin Control Center")
    admin_pass = st.text_input("Admin Password", type="password")
    if admin_pass == "w1nbju8282":
        st.success("Akses Diterima")
        nominal = st.number_input("Total Transaksi", value=0)
        detail = st.text_input("Detail Barang")
        if st.button("Proses Analisis"):
            hasil, panggil_ai = proses_transaksi(nominal, detail)
            st.subheader(f"Status: {hasil}")
            if panggil_ai: st.caption("Analisis AI Aktif (Biaya API Terpakai)")
            else: st.caption("Filter Lokal (Hemat Biaya API 100%)")
    else:
        st.warning("Silakan masukkan password admin.")
