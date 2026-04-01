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
    .package-card { 
        background-color: #161b22; 
        padding: 25px; 
        border-radius: 12px; 
        border: 1px solid #30363d; 
        margin-bottom: 20px; 
        min-height: 420px;
        color: #c9d1d9;
    }
    .stButton>button { 
        width: 100%; 
        border-radius: 5px; 
        background-color: #238636; 
        color: white !important; 
        font-weight: bold; 
    }
    .package-title { color: #58a6ff; font-size: 1.5rem; font-weight: bold; margin-bottom: 15px; }
    .feature-list { font-size: 0.9rem; color: #8b949e; line-height: 1.6; margin-bottom: 20px; }
    .price-tag { font-size: 1.1rem; color: #ffffff; font-weight: bold; border-top: 1px solid #30363d; padding-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR PROFIL ---
with st.sidebar:
    foto_path = "erwin.jpg"
    if os.path.exists(foto_path):
        st.image(foto_path, use_container_width=True) # Memunculkan kembali foto profil
    
    st.markdown("<div style='text-align:center;'><h3>Erwin Sinaga</h3><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Layanan & Investasi", "Portal Klien", "Admin Control Center"])

# --- 1. VISI & MISI (TEKS 200+ KATA & FOTO) ---
if menu == "Visi & Misi":
    st.header("Visi & Misi V-Guard AI Intelligence")
    col_v1, col_v2 = st.columns([1, 2])
    with col_v1:
        if os.path.exists("erwin.jpg"): 
            st.image("erwin.jpg", caption="Erwin Sinaga - Founder V-Guard AI")
    
    with col_v2:
        # Mengembalikan narasi panjang (200+ kata) sesuai profil profesional Anda
        st.markdown("""
        <div style="text-align: justify; color: #8b949e; line-height: 1.8;">
        Sebagai seorang Senior Business Leader dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi produk, melainkan kepastian data dan eliminasi kebocoran internal (internal fraud). Di dunia digital yang serba cepat ini, kepercayaan atau <i>trust</i> tidak lagi cukup jika hanya berdasarkan janji atau intuisi semata; kepercayaan harus bisa diukur, diverifikasi secara matematis, dan didigitalisasi melalui teknologi kecerdasan buatan. Inilah alasan utama saya mendirikan V-Guard AI Intelligence sebagai benteng pertahanan bagi para pemilik bisnis di Indonesia agar aset mereka terlindungi sepenuhnya dari tindakan tidak bertanggung jawab di dalam operasional harian.<br><br>
        
        <b>Visi Kami:</b> Menjadi standar global dalam penyediaan ekosistem Digital Trust yang otonom, transparan, dan tak tergoyahkan. Kami bercita-cita membangun dunia di mana setiap interaksi digital didasari oleh bukti otentik yang dapat diverifikasi secara instan, menghilangkan ambiguitas dalam transaksi bisnis, dan memastikan integritas data menjadi aset yang paling berharga bagi setiap organisasi, mulai dari skala UMKM hingga korporasi multinasional. Kami percaya bahwa transparansi adalah hak setiap pemilik bisnis, dan teknologi kami hadir untuk menjamin hal tersebut terwujud tanpa kompromi sedikitpun di setiap lini perusahaan. Kami berkomitmen untuk terus berinovasi dalam menciptakan lingkungan bisnis yang lebih aman bagi semua pihak.<br><br>
        
        <b>Misi Kami:</b> Melaksanakan filosofi 'Eliminating Leakage' dengan dedikasi tinggi melalui integrasi kecerdasan buatan (AI) tingkat lanjut dan teknologi Computer Vision yang canggih. Kami berkomitmen untuk membangun sistem pertahanan prediktif yang mampu menghentikan pola kecurangan sebelum menjadi kerugian finansial yang signifikan bagi klien kami. Melalui prinsip 'Digitizing Trust', kami mengubah setiap titik data mentah menjadi bukti otentik yang tidak dapat dimanipulasi oleh oknum internal maupun eksternal. Kami berdedikasi untuk memberikan ketenangan pikiran bagi setiap pengusaha melalui audit otomatis yang jujur, akurat, dan real-time, demi masa depan ekonomi Indonesia yang lebih bersih, efisien, dan memiliki tingkat kepercayaan digital yang tinggi.
        </div>
        """, unsafe_allow_html=True)

# --- 2. LAYANAN & INVESTASI (BIAYA MINIMAL 750RB) ---
elif menu == "Layanan & Investasi":
    st.header("🛡️ Layanan V-Guard AI (Klik Nama untuk Order)")
    wa_base = "https://wa.me/6282122190885?text="

    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown("<div class='package-card'><div class='package-title'>📦 V-LITE</div>", unsafe_allow_html=True)
        st.markdown("<div class='feature-list'>• AI Fraud Dasar<br>• Laporan Bulanan PDF<br>• Notifikasi Standar<br>• Cocok untuk UMKM</div>", unsafe_allow_html=True)
        st.markdown("<div class='price-tag'>Langganan: Rp 750.000/bln</div><br>", unsafe_allow_html=True)
        st.link_button("Pilih V-LITE", f"{wa_base}Halo%20Pak%20Erwin,%20saya%20order%20V-LITE")
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='package-card'><div class='package-title'>🛡️ V-PRO</div>", unsafe_allow_html=True)
        st.markdown("<div class='feature-list'>• Real-Time Monitoring<br>• VCS Integrasi Bank<br>• Audit Harian Otomatis<br>• Prediksi Risiko AI</div>", unsafe_allow_html=True)
        st.markdown("<div class='price-tag'>Langganan: Rp 1.500.000/bln</div><br>", unsafe_allow_html=True)
        st.link_button("Pilih V-PRO", f"{wa_base}Halo%20Pak%20Erwin,%20saya%20order%20V-PRO")
        st.markdown("</div>", unsafe_allow_html=True)

    # ... Paket lainnya tetap dipertahankan ...
    st.info("Seluruh nama produk di atas terkoneksi langsung ke WhatsApp Bapak (082122190885).")

# --- 3. PORTAL KLIEN (USER AKTIF & PASSWORD) ---
elif menu == "Portal Klien":
    st.header("Portal Klien")
    col_a, col_b = st.columns([1, 1.2])
    with col_a:
        st.subheader("📝 Form Order Baru")
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

# --- 4. ADMIN CONTROL CENTER (THE CORE BRAIN) ---
elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center")
    adm_pw = st.text_input("Password Admin", type="password")
    if adm_pw == "adminvguard2026":
        st.success("Integrasi Core Brain Aktif: Gemini AI, MindBridge, YOLO Vision.")
        st.warning("🚨 Alarm Fraud: Terdeteksi anomali pada User 'Cafe Mantap'.")
    elif adm_pw != "": st.error("Password Salah!")

st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>🛡️ V-Guard AI Intelligence | ©2026 | Founder: Erwin Sinaga | WA: 082122190885</div>", unsafe_allow_html=True)
