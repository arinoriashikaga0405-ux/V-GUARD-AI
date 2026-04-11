import streamlit as st
import os
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE AI ---
# Masukkan API Key Anda di sini
GEMINI_API_KEY = "ISI_API_KEY_ANDA_DI_SINI" 
genai.configure(api_key=GEMINI_API_KEY)
model_gemini = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Premium Eksekutif
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; height: 45px; }
    .mission-box { 
        text-align: justify; line-height: 1.8; font-size: 16px; color: #d1d5db;
        background-color: #1e293b; padding: 35px; border-radius: 15px; border-left: 10px solid #238636;
    }
    .card-produk {
        background-color: #1e293b; padding: 20px; border-radius: 10px; border: 1px solid #334155; height: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Fungsi Menampilkan Foto dengan Proteksi Error
def tampilkan_foto_aman(file_path):
    try:
        if os.path.exists(file_path):
            st.image(file_path, use_container_width=True)
        else:
            st.info("👤 Foto Founder (erwin.jpg)")
    except:
        st.warning("⚠️ File foto bermasalah")

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    tampilkan_foto_aman("erwin.jpg")
    st.markdown("<div style='text-align:center;'><p style='color:white; font-weight:bold; margin-bottom:0;'>Erwin Sinaga</p><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    menu = st.radio("STRATEGIC NAVIGATOR", [
        "Visi & Misi", 
        "Produk & Layanan", 
        "Analisis ROI", 
        "Portal Klien", 
        "Admin Control Center"
    ])

# --- 4. LOGIKA HALAMAN ---

# A. VISI & MISI (250 KATA)
if menu == "Visi & Misi":
    st.header("Visi & Misi: Fondasi Integritas Digital")
    col_img, col_txt = st.columns([1, 2.5])
    with col_img:
        tampilkan_foto_aman("erwin.jpg")
    with col_txt:
        st.markdown("""
        <div class="mission-box">
        <b>Visi Strategis: Menjadi Jangkar Kepercayaan Global (Digitizing Trust)</b><br>
        V-Guard AI Intelligence hadir sebagai jawaban atas kerentanan sistem operasional bisnis di era transformasi digital yang serba cepat. Visi kami adalah menciptakan ekosistem bisnis global yang sepenuhnya transparan, aman, dan berintegritas tinggi melalui digitalisasi kepercayaan. Kami percaya bahwa setiap pemilik bisnis, mulai dari UMKM hingga korporasi besar, berhak menjalankan usaha mereka dengan ketenangan pikiran total. V-Guard bercita-cita menjadi standar emas dalam "Integrity Assurance", di mana kejujuran sistem tidak lagi menjadi variabel yang diragukan, melainkan sebuah kepastian matematis yang divalidasi oleh kecerdasan buatan otonom secara real-time. Dengan visi ini, kami memastikan setiap keputusan bisnis didasarkan pada data yang murni dan tidak termanipulasi untuk keberlanjutan jangka panjang.<br><br>
        
        <b>Misi Operasional: Eliminasi Kebocoran & Perlindungan Aset (Eliminating Leakage)</b><br>
        Misi kami didorong oleh pengalaman mendalam selama lebih dari sepuluh tahun di industri perbankan dan manajemen risiko finansial. Pertama, kami berkomitmen untuk membangun infrastruktur integritas digital yang mampu mengonversi setiap etika operasional menjadi data terukur yang tidak dapat dimanipulasi secara real-time. Kedua, kami menerapkan teknologi Edge Filtering presisi tinggi untuk mendeteksi anomali finansial tepat di titik kejadian (Point of Truth), memastikan tidak ada satu Rupiah pun yang hilang akibat kelalaian atau kecurangan sistemik. Ketiga, V-Guard berfokus pada efisiensi teknologi yang berkelanjutan; melalui optimalisasi pemrosesan data lokal, kami menekan biaya infrastruktur server hingga 20%, memberikan margin keuntungan yang lebih tinggi bagi mitra kami tanpa mengorbankan kecepatan akses. Keempat, kami memberikan kedaulatan penuh kepada pemilik bisnis melalui Command Center terenkripsi, memberikan visibilitas 100% terhadap aktivitas operasional nasional dari mana saja. Terakhir, kami menjaga disiplin tinggi dalam pengembangan perangkat lunak sesuai standar operasional baku (SOP) V-Guard, memastikan inovasi kami melampaui standar audit konvensional untuk menjaga warisan bisnis Anda tetap utuh.
        </div>
        """, unsafe_allow_html=True)

# B. PRODUK & LAYANAN
elif menu == "Produk & Layanan":
    st.header("🛡️ Portfolio Layanan V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    packs = {
        "V-LITE": ["Retail Mikro", "1.5 Jt", "750 rb", "Fraud Detector Dasar"],
        "V-PRO": ["Retail Modern", "3 Jt", "1.5 Jt", "VCS & Audit Bank"],
        "V-SIGHT": ["Gudang/Distribusi", "7.5 Jt", "3.5 Jt", "AI Behavior & Alarm"],
        "V-ULTRA": ["Enterprise", "15 Jt", "10 Jt", "Forensic AI & Server"]
    }
    for i, (name, d) in enumerate(packs.items()):
        with [c1, c2, c3, c4][i]:
            st.markdown(f"""<div class="card-produk">
            <h3>{name}</h3><p>{d[0]}</p><hr>
            <b>Pasang: {d[1]}</b><br><b>Bulan: {d[2]}</b><br><small>{d[3]}</small>
            </div>""", unsafe_allow_html=True)

# C. ANALISIS ROI
elif menu == "Analisis ROI":
    st.header("📊 Analisis Penghematan (ROI)")
    omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
    leak = st.slider("Estimasi Kebocoran (%)", 1, 20, 5)
    loss = omzet * (leak / 100)
    st.error(f"Potensi Kerugian: Rp {loss:,.0f}")
    st.success(f"Profit Diselamatkan AI: Rp {loss * 0.8:,.0f}")

# D. PORTAL KLIEN
elif menu == "Portal Klien":
    st.header("🔑 Client Access Portal")
    with st.container(border=True):
        st.text_input("Username / Client ID")
        st.text_input("Password", type="password")
        st.button("Login Ke Dashboard")

# E. ADMIN CENTER
elif menu == "Admin Control Center":
    st.header("🔒 Executive Command Center")
    pwd = st.text_input("Master Password", type="password")
    if pwd == "w1nbju8282":
        col_a, col_b = st.columns(2)
        with col_a:
            st.success("📉 Efisiensi Server & API: 20% ACTIVE")
        with col_b:
            st.error("🚨 V-GUARD FIRE ALARM: STANDBY")
        
        st.divider()
        st.subheader("🤖 AI Squad Monitoring (Powered by Gemini)")
        
        # Contoh pengecekan status API di dashboard admin
        if GEMINI_API_KEY != "ISI_API_KEY_ANDA_DI_SINI":
            st.write("Status Engine AI: **ONLINE**")
        else:
            st.warning("Status Engine AI: **API KEY BELUM TERPASANG**")
            
        st.metric("Dana Terlindungi", "Rp 1.250.000.000", delta="Efisiensi 20%")

st.markdown("---")
st.markdown("<center><small>© 2026 V-GUARD AI | Digital Integrity Powered by Erwin Sinaga</small></center>", unsafe_allow_html=True)
