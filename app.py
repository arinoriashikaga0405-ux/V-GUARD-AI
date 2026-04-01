import streamlit as st
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# --- 2. CSS CUSTOM (TAMPILAN BERSIH & KONTRAS) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .package-card { 
        background-color: #161b22; padding: 25px; border-radius: 12px; border: 1px solid #30363d; 
        margin-bottom: 20px; min-height: 480px; color: #c9d1d9;
    }
    .package-title { color: #58a6ff; font-size: 1.5rem; font-weight: bold; margin-bottom: 10px; }
    .price-tag { font-size: 1.2rem; color: #ffffff; font-weight: bold; margin: 15px 0; padding: 10px; border-top: 1px solid #333; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white !important; font-weight: bold; height: 45px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR PROFIL ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    foto_path = "erwin.jpg"
    if os.path.exists(foto_path):
        try: st.image(foto_path, use_container_width=True)
        except: st.info("Profil: Erwin Sinaga")
    st.markdown(f"<div style='text-align:center;'><b>Erwin Sinaga</b><br><small>Founder & CEO V-Guard AI</small></div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Layanan & Investasi", "Portal Klien", "Admin Control Center"])

# --- 4. LOGIKA MENU ---

# MENU 1: VISI & MISI (NARASI PROFESIONAL 250+ KATA)
if menu == "Visi & Misi":
    st.header("Visi & Misi V-Guard AI Intelligence")
    col_v1, col_v2 = st.columns([1, 2])
    with col_v1:
        if os.path.exists("erwin.jpg"): 
            st.image("erwin.jpg", caption="Erwin Sinaga - Founder V-Guard AI")
    with col_v2:
        st.markdown("""
        <div style="text-align: justify; color: #c9d1d9; line-height: 1.8;">
        Sebagai seorang Senior Business Leader dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi produk, melainkan kepastian data dan eliminasi kebocoran internal (internal fraud). Dalam perjalanan profesional saya, saya sering mengamati bagaimana bisnis yang sangat potensial hancur bukan karena persaingan pasar, melainkan karena kelemahan sistem pengawasan internal. Kepercayaan atau <i>trust</i> tidak lagi cukup jika hanya berdasarkan janji atau intuisi semata; kepercayaan harus bisa diukur, diverifikasi secara matematis, dan didigitalisasi melalui teknologi kecerdasan buatan. Inilah alasan utama saya mendirikan V-Guard AI Intelligence sebagai benteng pertahanan bagi para pemilik bisnis di Indonesia agar aset mereka terlindungi sepenuhnya dari tindakan tidak bertanggung jawab.<br><br>
        
        <b>Visi Kami:</b> Menjadi standar global dalam penyediaan ekosistem <i>Digital Trust</i> yang otonom, transparan, dan tak tergoyahkan. Kami bercita-cita membangun dunia di mana setiap interaksi bisnis didasari oleh bukti otentik yang dapat diverifikasi secara instan. Kami ingin menghilangkan segala bentuk ambiguitas dalam transaksi dan memastikan bahwa integritas data menjadi aset yang paling berharga bagi setiap organisasi, mulai dari skala UMKM hingga korporasi multinasional. Kami percaya bahwa transparansi adalah hak mutlak setiap pemilik modal, dan teknologi kami hadir untuk menjamin hak tersebut terwujud tanpa kompromi sedikitpun di setiap lini operasional perusahaan. Kami berkomitmen untuk terus berinovasi dalam menciptakan lingkungan bisnis yang sehat dan bebas dari manipulasi data.<br><br>
        
        <b>Misi Kami:</b> Melaksanakan filosofi 'Eliminating Leakage' dengan dedikasi tinggi melalui integrasi kecerdasan buatan (AI) tingkat lanjut dan teknologi Computer Vision yang canggih. Kami berkomitmen untuk membangun sistem pertahanan prediktif yang mampu mendeteksi dan menghentikan pola kecurangan sebelum menjadi kerugian finansial yang signifikan bagi klien kami. Melalui prinsip 'Digitizing Trust', kami mengubah setiap titik data mentah menjadi bukti otentik yang tidak dapat dimanipulasi oleh oknum internal maupun eksternal. Kami berdedikasi untuk memberikan ketenangan pikiran bagi setiap pengusaha melalui audit otomatis yang jujur dan real-time, demi terciptanya masa depan ekonomi Indonesia yang lebih bersih, efisien, dan memiliki tingkat kepercayaan digital yang tinggi di kancah persaingan global.
        </div>
        """, unsafe_allow_html=True)

# MENU 2: LAYANAN (HARGA MINIMAL 750RB)
elif menu == "Layanan & Investasi":
    st.header("🛡️ Produk & Layanan (Klik Nama untuk Order)")
    wa_base = "https://wa.me/6282122190885?text=Halo%20Pak%20Erwin,%20saya%20order%20"
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div class='package-card'><div class='package-title'>📦 V-LITE</div>• AI Fraud Dasar<br>• Laporan Bulanan PDF<br>• Notifikasi Standar<div class='price-tag'>Rp 750.000 / bln</div>", unsafe_allow_html=True)
        st.link_button("Pilih V-LITE", f"{wa_base}V-LITE")
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='package-card'><div class='package-title'>🛡️ V-PRO</div>• Real-Time Monitoring<br>• VCS Integrasi Bank<br>• Audit Harian Otomatis<div class='price-tag'>Rp 1.500.000 / bln</div>", unsafe_allow_html=True)
        st.link_button("Pilih V-PRO", f"{wa_base}V-PRO")
        st.markdown("</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='package-card'><div class='package-title'>👁️ V-SIGHT</div>• CCTV AI Behavior<br>• Visual Audit Kasir<br>• Deteksi Stok Real-time<div class='price-tag'>Rp 2.500.000 / bln</div>", unsafe_allow_html=True)
        st.link_button("Pilih V-SIGHT", f"{wa_base}V-SIGHT")
        st.markdown("</div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='package-card'><div class='package-title'>🏢 V-ENTERPRISE</div>• Multi-Cabang Central<br>• Digital Forensik AI<br>• Dedicated Server<div class='price-tag'>Hubungi CEO</div>", unsafe_allow_html=True)
        st.link_button("Hubungi Kami", f"{wa_base}V-ENTERPRISE")
        st.markdown("</div>", unsafe_allow_html=True)

# MENU 3: PORTAL KLIEN (FORM ORDER & LOGIN USER BERLANGGANAN)
elif menu == "Portal Klien":
    st.header("Portal Klien V-Guard AI")
    col_order, col_login = st.columns(2)
    
    with col_order:
        st.subheader("📝 Form Order Baru")
        with st.container(border=True):
            nama_u = st.text_input("Nama Usaha")
            paket_u = st.selectbox("Pilih Paket / Harga", [
                "V-LITE - Rp 750.000/bln", 
                "V-PRO - Rp 1.500.000/bln", 
                "V-SIGHT - Rp 2.500.000/bln", 
                "V-ENTERPRISE - Custom"
            ])
            st.file_uploader("Upload KTP Pemilik", type=['jpg', 'png', 'pdf'])
            if st.button("Kirim Data Order"):
                st.success(f"Order {paket_u} untuk {nama_u} terkirim!")
                st.info("Konfirmasi manual ke WA: 082122190885")

    with col_login:
        st.subheader("🔑 User Berlangganan")
        with st.container(border=True):
            user_id = st.text_input("Nama User / ID")
            user_pass = st.text_input("Password User", type="password")
            if st.button("Masuk Ke Sistem"):
                if user_pass == "vguardklien2026":
                    st.success(f"Akses Diterima. Selamat Datang {user_id}!")
                else:
                    st.error("Password Salah.")

# MENU 4: ADMIN CONTROL CENTER (VCS & INTERNAL)
elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center")
    if st.text_input("Administrator Password", type="password") == "adminvguard2026":
        tab1, tab2, tab3 = st.tabs(["📊 VCS Dashboard", "👤 Registrasi Internal", "🧠 AI Core"])
        with tab1:
            st.metric("Saldo Kasir", "Rp 45.200.000")
            st.metric("Saldo Bank (VCS Sinkron)", "Rp 45.200.000", delta="100% Sinkron")
            st.success("Audit MindBridge: Clear")
        with tab2:
            st.write("Form Pendaftaran Klien Baru oleh Admin.")
            st.text_input("Input ID Klien Baru")
            st.button("Daftarkan Akun")
        with tab3:
            st.info("Integrasi YOLO Vision & Gemini AI Aktif.")
    elif st.session_state.get('p_admin') != "": st.warning("Masukkan Password Admin.")

# --- 5. FOOTER ---
st.markdown("---")
st.markdown("<center><small>V-Guard AI Intelligence | ©2026 | Founder: Erwin Sinaga | WA: 082122190885</small></center>", unsafe_allow_html=True)
