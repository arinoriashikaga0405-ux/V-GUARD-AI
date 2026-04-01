import streamlit as st
from PIL import Image
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# API KEY GEMINI (Folder Admin)
GEMINI_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"

# --- CSS CUSTOM ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .package-card { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 20px; min-height: 400px;}
    .stButton>button { width: 100%; border-radius: 5px; }
    .feature-list { font-size: 0.85rem; color: #8b949e; line-height: 1.4; }
    .roi-section { background-color: #1c2128; padding: 20px; border-radius: 15px; border: 1px dashed #444c56; }
    .status-box { background-color: #0d1117; padding: 15px; border-radius: 10px; border: 1px solid #238636; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR PROFIL ---
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    
    st.markdown("<div style='text-align:center;'><h3>Erwin Sinaga</h3><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # MENU SESUAI INSTRUKSI (HAPUS ORDER BERLANGGANAN)
    menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Layanan & Investasi", "Portal Klien", "Admin Control Center"])

# --- 1. VISI & MISI ---
if menu == "Visi & Misi":
    st.header("Visi & Misi V-Guard AI Intelligence")
    col_v1, col_v2 = st.columns([1, 2])
    with col_v1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
    
    with col_v2:
        st.markdown("""
        <div style="text-align: justify; color: #8b949e; line-height: 1.8;">
        Sebagai seorang Senior Business Leader dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi produk, melainkan kepastian data dan eliminasi kebocoran internal (internal fraud). Di dunia digital yang serba cepat ini, kepercayaan atau <i>trust</i> tidak lagi cukup jika hanya berdasarkan janji atau intuisi semata; kepercayaan harus bisa diukur, diverifikasi secara matematis, dan didigitalisasi melalui teknologi kecerdasan buatan. Inilah alasan utama saya mendirikan V-Guard AI Intelligence sebagai benteng pertahanan bagi para pemilik bisnis di Indonesia.<br><br>
        
        <b>Visi Kami:</b> Menjadi standar global dalam penyediaan ekosistem Digital Trust yang otonom, transparan, dan tak tergoyahkan. Kami bercita-cita membangun dunia di mana setiap interaksi digital didasari oleh bukti otentik yang dapat diverifikasi secara instan, menghilangkan ambiguitas dalam transaksi bisnis, dan memastikan integritas data menjadi aset yang paling berharga bagi setiap organisasi, mulai dari skala UMKM hingga korporasi multinasional.<br><br>
        
        <b>Misi Kami:</b> Melaksanakan filosofi 'Eliminating Leakage' dengan dedikasi tinggi melalui integrasi kecerdasan buatan (AI) tingkat lanjut dan teknologi ledger terdistribusi. Kami berkomitmen untuk membangun sistem pertahanan prediktif yang mampu menghentikan pola kecurangan sebelum menjadi kerugian finansial yang signifikan. Melalui prinsip 'Digitizing Trust', kami mengubah setiap titik data mentah menjadi bukti otentik yang tidak dapat dimanipulasi oleh oknum internal maupun eksternal. Kami berdedikasi untuk memberikan ketenangan pikiran bagi setiap pengusaha melalui audit otomatis yang jujur, akurat, dan real-time, demi masa depan ekonomi yang lebih bersih dan efisien.
        </div>
        """, unsafe_allow_html=True)

# --- 2. LAYANAN & INVESTASI ---
elif menu == "Layanan & Investasi":
    st.header("🛡️ Paket Layanan V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div class='package-card'><h3>📦 V-LITE</h3><div class='feature-list'>• AI Fraud Dasar<br>• Laporan Bulanan PDF<br>• Notifikasi Standar<br><br><b>Pemasangan:</b> Rp 1.500.000<br><b>Bulanan:</b> Rp 250.000</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='package-card'><h3>🛡️ V-PRO</h3><div class='feature-list'>• Real-Time Monitoring<br>• VCS Integrasi<br>• Audit Harian Otomatis<br><br><b>Pemasangan:</b> Rp 3.000.000<br><b>Bulanan:</b> Rp 750.000</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='package-card'><h3>👁️ V-SIGHT</h3><div class='feature-list'>• AI Behavior Visual<br>• Visual Audit<br>• Penyimpanan Cloud<br><br><b>Pemasangan:</b> Rp 5.000.000<br><b>Bulanan:</b> Rp 1.250.000</div></div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='package-card'><h3>🏢 V-ENTERPRISE</h3><div class='feature-list'>• Multi-Cabang Centralized<br>• Forensik Digital Full<br>• Custom API Integration<br><br><b>Pemasangan:</b> Kontak Admin<br><b>Bulanan:</b> Custom</div></div>", unsafe_allow_html=True)
        st.link_button("Hubungi CEO", "https://wa.me/6282122190885")

    st.markdown("---")
    st.subheader("📊 Analisis Potensi Penghematan (ROI)")
    r1, r2 = st.columns(2)
    with r1:
        st.markdown("<div class='roi-section'><h4>Estimasi Kerugian</h4>", unsafe_allow_html=True)
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
        leak = st.slider("Kebocoran (%)", 0, 20, 5)
        loss = omzet * (leak/100)
        st.error(f"Rugi: Rp {loss:,.0f}/bln")
        st.markdown("</div>", unsafe_allow_html=True)
    with r2:
        st.markdown("<div class='roi-section'><h4>Hasil V-Guard AI</h4>", unsafe_allow_html=True)
        st.success(f"Hemat: Rp {loss * 0.95:,.0f}/bln")
        st.info("Efisiensi 95% pada sistem operasional.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 3. PORTAL KLIEN (ORDER & USER AKTIF) ---
elif menu == "Portal Klien":
    st.header("Portal Klien")
    
    # 2 BAGIAN BERSAMPINGAN
    col_order, col_status = st.columns([1, 1.2])
    
    with col_order:
        st.subheader("📝 Form Order Baru")
        with st.container(border=True):
            n_u = st.text_input("Nama Usaha")
            p_u = st.selectbox("Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            h_u = st.text_input("Kesepakatan Harga (Rp)")
            k_u = st.file_uploader("Upload KTP (JPG/PDF)")
            if st.button("Kirim Pesanan"):
                if n_u and k_u:
                    text = f"Halo Pak Erwin, saya {n_u} ingin berlangganan paket {p_u}."
                    st.link_button("Konfirmasi ke WhatsApp", f"https://wa.me/6282122190885?text={text}")
                else:
                    st.error("Lengkapi data dan Upload KTP.")

    with col_status:
        st.subheader("✅ Status User Aktif")
        # KUNCI MENU DENGAN PASSWORD
        lock_pw = st.text_input("Masukkan Password Akses Klien", type="password", key="client_lock")
        
        if lock_pw == "vguardklien2026": # PASSWORD UNTUK LIHAT DATA AKTIF
            st.markdown("<div class='status-box'>", unsafe_allow_html=True)
            st.write("Daftar User yang Sudah Aktif & Bayar:")
            st.table([
                {"Nama Usaha": "Laundry Jaya", "Paket": "V-LITE", "Status": "LUNAS", "Password": "JAY-V1-2026"},
                {"Nama Usaha": "Cafe Mantap", "Paket": "V-PRO", "Status": "LUNAS", "Password": "CAF-V2-9921"},
                {"Nama Usaha": "Toko Emas Antam", "Paket": "V-SIGHT", "Status": "LUNAS", "Password": "ANT-V3-0012"}
            ])
            st.markdown("</div>", unsafe_allow_html=True)
            st.info("Notifikasi: Invoice H-7 Berlangganan dikirim ke WhatsApp terdaftar.")
        elif lock_pw != "":
            st.error("Password Akses Salah.")

# --- 4. ADMIN CONTROL CENTER ---
elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center")
    adm_pw = st.text_input("Password Administrator", type="password")
    if adm_pw == "adminvguard2026":
        t1, t2 = st.tabs(["📉 Laporan Audit & Rugi Laba", "🤖 V-Guard AI (Gemini)"])
        with t1:
            st.warning("🚨 Alarm Fraud: Indikasi Void mencurigakan di 'Cafe Mantap'.")
            st.table([{"Tanggal": "01/04", "User": "Cafe Mantap", "Audit": "Flagged", "Rugi Laba": "Profit Rp 45jt"}])
        with t2:
            st.write("AI Assistant Terkoneksi: AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA")
            st.text_area("Gemini Analysis Prompt")
            st.button("Proses Analisis")
    elif adm_pw != "":
        st.error("Akses Admin Ditolak.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>🛡️ V-Guard AI Intelligence | ©2026 | Founder: Erwin Sinaga | WA: 082122190885</div>", unsafe_allow_html=True)
