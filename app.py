import streamlit as st
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# --- 2. CSS CUSTOM (PREMIUM DARK MODE & CLEAN INTERFACE) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .package-card { 
        background-color: #161b22; padding: 25px; border-radius: 12px; border: 1px solid #30363d; 
        margin-bottom: 20px; min-height: 480px; color: #c9d1d9;
    }
    .package-title { color: #58a6ff; font-size: 1.5rem; font-weight: bold; margin-bottom: 10px; }
    .price-tag { font-size: 1.3rem; color: #ffffff; font-weight: bold; margin: 15px 0; padding: 10px; border-top: 1px solid #333; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; height: 45px; border: none; }
    .stButton>button:hover { background-color: #2ea043; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR PROFIL (DENGAN FOTO PROTEKSI) ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    foto_path = "erwin.jpg"
    if os.path.exists(foto_path):
        try: st.image(foto_path, use_container_width=True)
        except: st.info("Profil: Erwin Sinaga")
    st.markdown(f"<div style='text-align:center;'><b>Erwin Sinaga</b><br><small>Founder & CEO V-Guard AI</small></div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Produk & Layanan", "Analisis ROI Kerugian", "Portal Klien", "Admin Control Center"])

# --- 4. LOGIKA MENU ---

# MENU 1: VISI & MISI (NARASI PROFESIONAL 250+ KATA)
if menu == "Visi & Misi":
    st.header("Visi & Misi V-Guard AI Intelligence")
    col_v1, col_v2 = st.columns([1, 2])
    with col_v1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", caption="Erwin Sinaga - Founder V-Guard AI")
    with col_v2:
        st.markdown("""
        <div style="text-align: justify; color: #c9d1d9; line-height: 1.8;">
        Sebagai seorang Senior Business Leader dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi produk, melainkan kepastian data dan eliminasi kebocoran internal (internal fraud). Dalam perjalanan profesional saya, saya sering mengamati bagaimana bisnis yang sangat potensial hancur bukan karena persaingan pasar, melainkan karena kelemahan sistem pengawasan internal. Kepercayaan atau <i>trust</i> tidak lagi cukup jika hanya berdasarkan janji atau intuisi semata; kepercayaan harus bisa diukur, diverifikasi secara matematis, dan didigitalisasi melalui teknologi kecerdasan buatan. Inilah alasan utama saya mendirikan V-Guard AI Intelligence sebagai benteng pertahanan bagi para pemilik bisnis di Indonesia agar aset mereka terlindungi sepenuhnya dari tindakan tidak bertanggung jawab.<br><br>
        
        <b>Visi Kami:</b> Menjadi standar global dalam penyediaan ekosistem <i>Digital Trust</i> yang otonom, transparan, dan tak tergoyahkan. Kami bercita-cita membangun dunia di mana setiap interaksi bisnis didasari oleh bukti otentik yang dapat diverifikasi secara instan. Kami ingin menghilangkan segala bentuk ambiguitas dalam transaksi dan memastikan bahwa integritas data menjadi aset yang paling berharga bagi setiap organisasi, mulai dari skala UMKM hingga korporasi multinasional. Kami percaya bahwa transparansi adalah hak mutlak setiap pemilik modal, dan teknologi kami hadir untuk menjamin hak tersebut terwujud tanpa kompromi sedikitpun di setiap lini operasional perusahaan. Kami berkomitmen untuk terus berinovasi dalam menciptakan lingkungan bisnis yang sehat dan bebas dari manipulasi data.<br><br>
        
        <b>Misi Kami:</b> Melaksanakan filosofi 'Eliminating Leakage' dengan dedikasi tinggi melalui integrasi kecerdasan buatan (AI) tingkat lanjut dan teknologi Computer Vision yang canggih. Kami berkomitmen untuk membangun sistem pertahanan prediktif yang mampu mendeteksi dan menghentikan pola kecurangan sebelum menjadi kerugian finansial yang signifikan bagi klien kami. Melalui prinsip 'Digitizing Trust', kami mengubah setiap titik data mentah menjadi bukti otentik yang tidak dapat dimanipulasi oleh oknum internal maupun eksternal. Kami berdedikasi untuk memberikan ketenangan pikiran bagi setiap pengusaha melalui audit otomatis yang jujur dan real-time, demi terciptanya masa depan ekonomi Indonesia yang lebih bersih, efisien, dan memiliki tingkat kepercayaan digital yang tinggi di kancah persaingan global.
        </div>
        """, unsafe_allow_html=True)

# MENU 2: PRODUK & LAYANAN (HARGA MINIMAL 1JT, TANPA INSTRUKSI TAMBAHAN)
elif menu == "Produk & Layanan":
    st.header("🛡️ Produk & Layanan V-Guard AI")
    wa_base = "https://wa.me/6282122190885?text=Halo%20Pak%20Erwin,%20saya%20order%20"
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div class='package-card'><div class='package-title'>📦 V-LITE</div>• AI Fraud Dasar<br>• Laporan Bulanan PDF<br>• Notifikasi Standar<div class='price-tag'>Rp 1.000.000 / bln</div>", unsafe_allow_html=True)
        st.link_button("Pilih V-LITE", f"{wa_base}V-LITE")
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='package-card'><div class='package-title'>🛡️ V-PRO</div>• Real-Time Monitoring<br>• VCS Integrasi Bank<br>• Audit Harian Otomatis<div class='price-tag'>Rp 2.500.000 / bln</div>", unsafe_allow_html=True)
        st.link_button("Pilih V-PRO", f"{wa_base}V-PRO")
        st.markdown("</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='package-card'><div class='package-title'>👁️ V-SIGHT</div>• CCTV AI Behavior<br>• Visual Audit Kasir<br>• Deteksi Stok Real-time<div class='price-tag'>Rp 5.000.000 / bln</div>", unsafe_allow_html=True)
        st.link_button("Pilih V-SIGHT", f"{wa_base}V-SIGHT")
        st.markdown("</div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='package-card'><div class='package-title'>🏢 V-ENTERPRISE</div>• Multi-Cabang Central<br>• Digital Forensik AI<br>• Dedicated Server<div class='price-tag'>Rp 10.000.000 / bln</div>", unsafe_allow_html=True)
        st.link_button("Pilih V-ENTERPRISE", f"{wa_base}V-ENTERPRISE")
        st.markdown("</div>", unsafe_allow_html=True)

# MENU 3: ANALISIS ROI KERUGIAN
elif menu == "Analisis ROI Kerugian":
    st.header("📊 Analisis Kerugian vs ROI")
    col_a, col_b = st.columns(2)
    with col_a:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000, step=10000000)
        leak = st.slider("Estimasi Kebocoran / Fraud (%)", 1, 20, 5)
        loss = omzet * (leak / 100)
        st.error(f"Potensi Kerugian: Rp {loss:,.0f} / bln")
    with col_b:
        biaya = st.selectbox("Pilih Paket Layanan", [1000000, 2500000, 5000000, 10000000])
        saved = loss - biaya
        st.success(f"Profit Diselamatkan: Rp {saved:,.0f} / bln")
        st.metric("ROI Investasi", f"{(saved/biaya)*100 if saved>0 else 0:.0f}%")

# MENU 4: PORTAL KLIEN (ORDER & LOGIN USER)
elif menu == "Portal Klien":
    st.header("Portal Klien V-Guard AI")
    col_order, col_login = st.columns(2)
    with col_order:
        st.subheader("📝 Form Order Baru")
        with st.container(border=True):
            st.text_input("Nama Usaha")
            st.selectbox("Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.file_uploader("Upload KTP Pemilik", type=['jpg', 'png', 'pdf'])
            st.button("Kirim Data Order")
    with col_login:
        st.subheader("🔑 Login User Berlangganan")
        with st.container(border=True):
            u_id = st.text_input("Nama User / ID")
            u_pw = st.text_input("Password", type="password")
            if st.button("Masuk"):
                if u_pw == "vguardklien2026": st.success(f"Selamat Datang {u_id}")
                else: st.error("Password Salah")

# MENU 5: ADMIN (CORE BRAIN + VCS + USER BARU + ALARM + INVOICE)
elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center - The Core Brain")
    if st.text_input("Admin Password", type="password") == "adminvguard2026":
        t1, t2, t3 = st.tabs(["📊 VCS Dashboard", "👤 Akun User Baru", "🚨 Alarm & Notifikasi"])
        with t1:
            st.metric("Total Kasir", "Rp 125.450.000")
            st.metric("Dana Bank (VCS Sinkron)", "Rp 125.450.000", delta="Sinkron 100%")
        with t2:
            st.subheader("Registrasi User Baru")
            st.text_input("ID Klien Baru")
            st.selectbox("Set Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.button("Aktifkan Akun")
        with t3:
            st.warning("📅 Invoice H-7 Otomatis: AKTIF")
            st.error("🚨 Alarm Fraud Digital: AKTIF")
            st.info("V-Guard Core Brain: MindBridge & YOLO Vision Online")
    elif st.session_state.get('p_admin') != "": st.warning("Masukkan Password Admin.")

# --- 5. FOOTER ---
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026 | Founder: Erwin Sinaga | WA: 082122190885</small></center>", unsafe_allow_html=True)
