import streamlit as st
import os
import pandas as pd

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Custom Eksekutif
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; height: 45px; }
    .mission-box { 
        text-align: justify; line-height: 1.8; font-size: 16px; color: #d1d5db;
        background-color: #1e293b; padding: 35px; border-radius: 15px; border-left: 10px solid #238636;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.markdown("<div style='text-align:center;'><p style='color:white; font-weight:bold; margin-bottom:0;'>Erwin Sinaga</p><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    menu = st.radio("NAVIGASI UTAMA", [
        "Visi & Misi", 
        "Produk & Layanan", 
        "Analisis ROI Kerugian", 
        "Portal Klien", 
        "Admin Control Center"
    ])

# --- 3. LOGIKA MENU UTAMA ---

# A. VISI & MISI (EKSPANSI 250 KATA)
if menu == "Visi & Misi":
    st.header("Visi & Misi Strategis: Fondasi Integritas Digital")
    col_img, col_txt = st.columns([1, 2.5])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga - Founder & CEO", use_container_width=True)
    with col_txt:
        st.markdown("""
        <div class="mission-box">
        <b>Visi Strategis: Menjadi Jangkar Kepercayaan Global (Digitizing Trust)</b><br>
        V-Guard AI Intelligence hadir sebagai jawaban atas kerentanan sistem operasional bisnis di era transformasi digital yang serba cepat. Visi kami adalah menciptakan ekosistem bisnis global yang sepenuhnya transparan, aman, dan berintegritas tinggi melalui digitalisasi kepercayaan. Kami percaya bahwa setiap pemilik bisnis, mulai dari UMKM hingga korporasi besar, berhak menjalankan usaha mereka dengan ketenangan pikiran total. V-Guard bercita-cita menjadi standar emas dalam "Integrity Assurance", di mana kejujuran sistem tidak lagi menjadi variabel yang diragukan, melainkan sebuah kepastian matematis yang divalidasi oleh kecerdasan buatan otonom secara real-time.<br><br>
        
        <b>Misi Operasional: Eliminasi Kebocoran & Perlindungan Aset (Eliminating Leakage)</b><br>
        Misi kami didorong oleh pengalaman mendalam selama lebih dari sepuluh tahun di industri perbankan dan manajemen risiko. Pertama, kami berkomitmen untuk membangun infrastruktur integritas digital yang mampu mengonversi setiap etika operasional menjadi data terukur yang tidak dapat dimanipulasi. Kedua, kami menerapkan teknologi Edge Filtering presisi tinggi untuk mendeteksi anomali finansial tepat di titik kejadian (Point of Truth), memastikan tidak ada satu Rupiah pun yang hilang akibat kelalaian atau kecurangan sistemik. Ketiga, V-Guard berfokus pada efisiensi teknologi; melalui optimalisasi pemrosesan data lokal, kami menekan biaya infrastruktur server hingga 20%, memberikan margin keuntungan yang lebih tinggi bagi mitra kami. Keempat, kami memberikan kedaulatan penuh kepada pemilik bisnis melalui Command Center terenkripsi, memberikan visibilitas 100% terhadap aktivitas operasional nasional. Terakhir, kami menjaga disiplin tinggi dalam pengembangan perangkat lunak (SOP V-Guard), memastikan inovasi kami melampaui standar audit konvensional untuk menjaga warisan bisnis Anda tetap utuh bagi generasi mendatang.
        </div>
        """, unsafe_allow_html=True)

# B. PRODUK & LAYANAN
elif menu == "Produk & Layanan":
    st.header("🛡️ Portfolio Layanan V-Guard AI")
    wa_number = "6282122190885"
    c1, c2, c3, c4 = st.columns(4)
    packages = {
        "V-LITE": ["Mikro", "1.5 Jt", "750 rb", "AI Fraud Detector Dasar, Laporan WA"],
        "V-PRO": ["Retail", "3 Jt", "1.5 Jt", "VCS Integration, Bank Statement Audit"],
        "V-SIGHT": ["Gudang", "7.5 Jt", "3.5 Jt", "CCTV AI Behavior, Real-Time Stock"],
        "V-ENTERPRISE": ["Korporasi", "15 Jt", "10 Jt", "Forensic AI, Dedicated Server"]
    }
    for i, (name, details) in enumerate(packages.items()):
        with [c1, c2, c3, c4][i]:
            with st.container(border=True):
                st.markdown(f"### 📦 {name}")
                st.info(f"**Pasang:** {details[1]}\n\n**Bulan:** {details[2]}")
                st.write(f"Fitur: {details[3]}")
                st.link_button(f"Pilih {name}", f"https://wa.me/{wa_number}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20dengan%20paket%20*{name}*")

# C. ANALISIS ROI
elif menu == "Analisis ROI Kerugian":
    st.header("📊 Analisis Potensi Kerugian vs ROI")
    omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
    leak = st.slider("Estimasi Kebocoran (%)", 1, 20, 5)
    loss = omzet * (leak / 100)
    st.error(f"Potensi Kerugian: Rp {loss:,.0f} / bulan")
    st.success(f"Profit Diselamatkan (ROI): Rp {loss * 0.8:,.0f} / bln")

# D. PORTAL KLIEN
elif menu == "Portal Klien":
    st.header("🔑 Portal Klien V-Guard AI")
    with st.container(border=True):
        st.text_input("Username")
        st.text_input("Password", type="password")
        st.button("Masuk Portal")

# E. ADMIN CONTROL CENTER (DENGAN INDIKATOR EFISIENSI & ALARM)
elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center")
    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False
    
    if not st.session_state.admin_logged_in:
        admin_input = st.text_input("Administrator Password", type="password")
        if admin_input == "w1nbju8282":
            st.session_state.admin_logged_in = True
