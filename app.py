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
    .package-card { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 20px; min-height: 450px;}
    .stButton>button { width: 100%; border-radius: 5px; }
    .feature-list { font-size: 0.85rem; color: #8b949e; line-height: 1.4; }
    .roi-section { background-color: #1c2128; padding: 30px; border-radius: 15px; border: 1px dashed #444c56; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR PROFIL ---
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    
    st.markdown("<div style='text-align:center;'><h3>Erwin Sinaga</h3><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Layanan & Investasi", "Portal Klien", "Order Berlangganan", "Admin Control Center"])

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

# --- 2. LAYANAN & INVESTASI (PRODUK & ROI) ---
elif menu == "Layanan & Investasi":
    st.header("🛡️ Paket Layanan V-Guard AI")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div class='package-card'><h3>📦 V-LITE</h3><div class='feature-list'>• AI Fraud Dasar<br>• Laporan Bulanan PDF<br>• Notifikasi Standar<br>• Akses 1 User<br><br><b>Pemasangan:</b> Rp 1.500.000<br><b>Bulanan:</b> Rp 250.000</div></div>", unsafe_allow_html=True)
        if st.button("Pilih V-LITE"): st.info("Silakan lanjut ke menu Order Berlangganan")
    with c2:
        st.markdown("<div class='package-card'><h3>🛡️ V-PRO</h3><div class='feature-list'>• Real-Time Monitoring<br>• VCS Integrasi<br>• Audit Harian Otomatis<br>• Prioritas Support<br><br><b>Pemasangan:</b> Rp 3.000.000<br><b>Bulanan:</b> Rp 750.000</div></div>", unsafe_allow_html=True)
        if st.button("Pilih V-PRO"): st.info("Silakan lanjut ke menu Order Berlangganan")
    with c3:
        st.markdown("<div class='package-card'><h3>👁️ V-SIGHT</h3><div class='feature-list'>• AI Behavior Visual<br>• Visual Audit<br>• Deteksi Fisik<br>• Penyimpanan Cloud<br><br><b>Pemasangan:</b> Rp 5.000.000<br><b>Bulanan:</b> Rp 1.250.000</div></div>", unsafe_allow_html=True)
        if st.button("Pilih V-SIGHT"): st.info("Silakan lanjut ke menu Order Berlangganan")
    with c4:
        st.markdown("<div class='package-card'><h3>🏢 V-ENTERPRISE</h3><div class='feature-list'>• Multi-Cabang Centralized<br>• Forensik Digital Full<br>• Dedicated Server<br>• Custom API Integration<br><br><b>Pemasangan:</b> Hubungi Admin<br><b>Bulanan:</b> Custom</div></div>", unsafe_allow_html=True)
        st.link_button("Pilih V-ENTERPRISE", "https://wa.me/6282122190885?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20dengan%20paket%20V-ENTERPRISE")

    # --- ROI DI BAWAH PRODUK (2 BAGIAN) ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📊 Kalkulator ROI (Return on Investment)")
    roi_col1, roi_col2 = st.columns(2)
    
    with roi_col1:
        st.markdown("<div class='roi-section'><h4>Estimasi Kebocoran Bisnis</h4>", unsafe_allow_html=True)
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
        leakage_rate = st.slider("Persentase Kebocoran (%)", 0, 20, 5)
        loss = omzet * (leakage_rate/100)
        st.error(f"Potensi Rugi: Rp {loss:,.0f} / bln")
        st.markdown("</div>", unsafe_allow_html=True)

    with roi_col2:
        st.markdown("<div class='roi-section'><h4>Efisiensi V-Guard AI</h4>", unsafe_allow_html=True)
        savings = loss * 0.95
        st.success(f"Potensi Penghematan: Rp {savings:,.0f} / bln")
        st.info("V-Guard AI memangkas hingga 95% resiko fraud internal.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 3. PORTAL KLIEN ---
elif menu == "Portal Klien":
    st.header("Portal Klien")
    tab_order, tab_status = st.tabs(["📝 Form Order Baru", "✅ Status User Aktif"])
    
    with tab_order:
        st.subheader("Pendaftaran Layanan")
        nama_u = st.text_input("Nama Usaha")
        paket_u = st.selectbox("Pilih Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
        harga_u = st.text_input("Harga Kesepakatan (Rp)")
        ktp_u = st.file_uploader("Upload KTP Pemilik", type=['jpg','png','pdf'])
        
        if st.button("Kirim Data Order"):
            if nama_u and ktp_u:
                msg = f"Halo Pak Erwin, saya {nama_u} ingin order {paket_u} dengan harga {harga_u}."
                st.link_button("Konfirmasi Kirim via WhatsApp", f"https://wa.me/6282122190885?text={msg}")
            else:
                st.warning("Mohon isi nama usaha dan upload KTP.")

    with tab_status:
        st.subheader("Daftar User Aktif")
        st.table([
            {"Nama Usaha": "Laundry Jaya", "Paket": "V-LITE", "Status": "Aktif", "Password": "JAY-V1"},
            {"Nama Usaha": "Cafe Mantap", "Paket": "V-PRO", "Status": "Aktif", "Password": "CAF-V2"}
        ])

# --- 4. ORDER BERLANGGANAN (RINGKASAN) ---
elif menu == "Order Berlangganan":
    st.header("Ringkasan Pembayaran")
    st.info("Invoice H-7 akan otomatis dikirimkan ke nomor terdaftar.")
    st.write("Silakan hubungi WhatsApp 082122190885 untuk konfirmasi pembayaran.")

# --- 5. ADMIN CONTROL CENTER (LAPORAN RUGI LABA PINDAH KE SINI) ---
elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center")
    pw = st.text_input("Password Admin", type="password")
    
    if pw == "adminvguard2026":
        st.success("Akses Diterima")
        a_tab1, a_tab2 = st.tabs(["📉 Laporan Rugi Laba & Audit", "🤖 V-Guard AI Assistant"])
        
        with a_tab1:
            st.subheader("Laporan Keuangan & Audit Fraud")
            st.warning("🚨 Alarm Fraud: Terdeteksi 2 Void mencurigakan pada User 'Cafe Mantap'.")
            st.table([
                {"Tanggal": "01/04/2026", "Klien": "Laundry Jaya", "Profit": "Rp 15jt", "Audit": "Clear"},
                {"Tanggal": "01/04/2026", "Klien": "Cafe Mantap", "Profit": "Rp 45jt", "Audit": "Flagged"}
            ])
            
        with a_tab2:
            st.write("### AI Pendukung (Google Gemini)")
            prompt = st.text_area("Input Analisis Keamanan:", "Analisis trend fraud bulan ini...")
            if st.button("Jalankan AI"):
                st.info("Menghubungkan ke Gemini API: AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA...")
                st.write("Hasil analisis sedang diproses...")
    elif pw != "":
        st.error("Password Salah!")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>🛡️ V-Guard AI Intelligence | ©2026 | WA: 082122190885</div>", unsafe_allow_html=True)
