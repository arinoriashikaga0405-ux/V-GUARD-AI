import streamlit as st
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# API KEY & INTEGRASI CORE BRAIN
GEMINI_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"

# --- CSS CUSTOM ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .package-card { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 20px; min-height: 350px;}
    .stButton>button { width: 100%; border-radius: 5px; background-color: #238636; color: white; font-weight: bold; height: 50px; font-size: 1.1rem; }
    .feature-list { font-size: 0.85rem; color: #8b949e; line-height: 1.4; }
    .core-brain-box { background-color: #0d1117; padding: 15px; border: 1px solid #1f6feb; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR PROFIL ---
with st.sidebar:
    foto_path = "erwin.jpg"
    if os.path.exists(foto_path):
        st.image(foto_path, use_container_width=True)
    else:
        st.info("Upload 'erwin.jpg' untuk foto profil.")
    
    st.markdown("<div style='text-align:center;'><h3>Erwin Sinaga</h3><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Layanan & Investasi", "Portal Klien", "Admin Control Center"])

# --- 1. VISI & MISI (MINIMAL 200 KATA) ---
if menu == "Visi & Misi":
    st.header("Visi & Misi V-Guard AI Intelligence")
    col_v1, col_v2 = st.columns([1, 2])
    with col_v1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
    
    with col_v2:
        st.markdown("""
        <div style="text-align: justify; color: #8b949e; line-height: 1.8;">
        Sebagai seorang Senior Business Leader dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi produk, melainkan kepastian data dan eliminasi kebocoran internal (internal fraud). Di dunia digital yang serba cepat ini, kepercayaan atau <i>trust</i> tidak lagi cukup jika hanya berdasarkan janji atau intuisi semata; kepercayaan harus bisa diukur, diverifikasi secara matematis, dan didigitalisasi melalui teknologi kecerdasan buatan. Inilah alasan utama saya mendirikan V-Guard AI Intelligence sebagai benteng pertahanan bagi para pemilik bisnis di Indonesia agar aset mereka terlindungi sepenuhnya.<br><br>
        
        <b>Visi Kami:</b> Menjadi standar global dalam penyediaan ekosistem Digital Trust yang otonom, transparan, dan tak tergoyahkan. Kami bercita-cita membangun dunia di mana setiap interaksi digital didasari oleh bukti otentik yang dapat diverifikasi secara instan, menghilangkan ambiguitas dalam transaksi bisnis, dan memastikan integritas data menjadi aset yang paling berharga bagi setiap organisasi, mulai dari skala UMKM hingga korporasi multinasional. Kami percaya bahwa transparansi adalah hak setiap pemilik bisnis, dan teknologi kami hadir untuk menjamin hal tersebut terwujud tanpa kompromi sedikitpun di setiap lini perusahaan.<br><br>
        
        <b>Misi Kami:</b> Melaksanakan filosofi 'Eliminating Leakage' dengan dedikasi tinggi melalui integrasi kecerdasan buatan (AI) tingkat lanjut dan teknologi Computer Vision yang canggih. Kami berkomitmen untuk membangun sistem pertahanan prediktif yang mampu menghentikan pola kecurangan sebelum menjadi kerugian finansial yang signifikan bagi klien kami. Melalui prinsip 'Digitizing Trust', kami mengubah setiap titik data mentah menjadi bukti otentik yang tidak dapat dimanipulasi oleh oknum internal maupun eksternal. Kami berdedikasi untuk memberikan ketenangan pikiran bagi setiap pengusaha melalui audit otomatis yang jujur, akurat, dan real-time, demi masa depan ekonomi Indonesia yang lebih bersih, efisien, dan memiliki tingkat kepercayaan digital yang tinggi.
        </div>
        """, unsafe_allow_html=True)

# --- 2. LAYANAN & INVESTASI (KLIK NAMA = WA) ---
elif menu == "Layanan & Investasi":
    st.header("🛡️ Produk V-Guard AI (Klik Nama untuk Order)")
    
    # Perbaikan Fungsi Link WA
    wa_base = "https://wa.me/6282122190885?text="

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div class='package-card'>", unsafe_allow_html=True)
        st.link_button("📦 V-LITE", f"{wa_base}Halo%20Pak%20Erwin,%20saya%20mau%20order%20V-LITE")
        st.markdown("<p class='feature-list'><br>• AI Fraud Dasar<br>• Laporan Bulanan PDF<br>• Pemasangan: Rp 1.5jt</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='package-card'>", unsafe_allow_html=True)
        st.link_button("🛡️ V-PRO", f"{wa_base}Halo%20Pak%20Erwin,%20saya%20mau%20order%20V-PRO")
        st.markdown("<p class='feature-list'><br>• Real-Time Monitoring<br>• VCS Integrasi<br>• Pemasangan: Rp 3jt</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='package-card'>", unsafe_allow_html=True)
        st.link_button("👁️ V-SIGHT", f"{wa_base}Halo%20Pak%20Erwin,%20saya%20mau%20order%20V-SIGHT")
        st.markdown("<p class='feature-list'><br>• CCTV AI Behavior<br>• Visual Audit<br>• Pemasangan: Rp 5jt</p></div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='package-card'>", unsafe_allow_html=True)
        st.link_button("🏢 V-ENTERPRISE", f"{wa_base}Halo%20Pak%20Erwin,%20saya%20mau%20order%20V-ENTERPRISE")
        st.markdown("<p class='feature-list'><br>• Multi-Cabang Central<br>• Digital Forensik<br>• Custom Solution</p></div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📊 Analisis Potensi Penghematan (ROI)")
    r1, r2 = st.columns(2)
    with r1:
        st.markdown("<div class='core-brain-box'><h4>Estimasi Kerugian</h4>", unsafe_allow_html=True)
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
        leak = st.slider("Kebocoran (%)", 0, 20, 5)
        loss = omzet * (leak/100)
        st.error(f"Potensi Rugi: Rp {loss:,.0f} / bln")
        st.markdown("</div>", unsafe_allow_html=True)
    with r2:
        st.markdown("<div class='core-brain-box'><h4>Hasil V-Guard AI</h4>", unsafe_allow_html=True)
        st.success(f"Potensi Hemat: Rp {loss * 0.95:,.0f} / bln")
        st.info("Efisiensi 95% pada sistem operasional.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 3. PORTAL KLIEN ---
elif menu == "Portal Klien":
    st.header("Portal Klien")
    col_a, col_b = st.columns([1, 1.2])
    with col_a:
        st.subheader("📝 Form Order Baru")
        with st.container(border=True):
            n_u = st.text_input("Nama Usaha")
            p_u = st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.file_uploader("Upload KTP Pemilik", type=['jpg','png','pdf'])
            if st.button("Kirim Data Order"):
                st.link_button("Konfirmasi WA", f"{wa_base}Order%20{p_u}%20untuk%20{n_u}")

    with col_b:
        st.subheader("✅ Status User Aktif")
        lock = st.text_input("Password Akses Klien", type="password")
        if lock == "vguardklien2026":
            st.table([
                {"Nama Usaha": "Laundry Jaya", "Paket": "V-LITE", "Status": "AKTIF", "Password": "JAY-V1"},
                {"Nama Usaha": "Cafe Mantap", "Paket": "V-PRO", "Status": "AKTIF", "Password": "CAF-V2"}
            ])
        elif lock != "": st.error("Akses Ditolak")

# --- 4. ADMIN CONTROL CENTER ---
elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center - The Core Brain")
    adm_pw = st.text_input("Password Admin", type="password")
    if adm_pw == "adminvguard2026":
        t1, t2, t3 = st.tabs(["🚨 Alarms & Notifications", "🧠 Core Brain Analysis", "📊 Financial Planning"])
        with t1:
            st.warning("🚨 Alarm Fraud (MindBridge): Terdeteksi anomali pada V-PRO User.")
            st.info("📅 Invoice H-7: Notifikasi otomatis siap dikirim.")
            st.write("✅ VCS: Data Bank vs Kasir Sinkron.")
        with t2:
            st.subheader("Google Gemini AI Integration")
            st.write(f"Brain Core API: {GEMINI_API_KEY}")
            st.text_area("Input Analisis Forensik:")
            st.button("Jalankan Audit AI")
            st.info("YOLO Vision AI memantau pergerakan visual stok.")
        with t3:
            st.write("DataRobot: Prediksi resiko operasional aktif.")
            st.success("Numeric.ai: Notifikasi harian siap dikirim ke smartphone CEO.")
    elif adm_pw != "": st.error("Password Salah!")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>🛡️ V-Guard AI Intelligence | ©2026 | Founder: Erwin Sinaga | WA: 082122190885</div>", unsafe_allow_html=True)
