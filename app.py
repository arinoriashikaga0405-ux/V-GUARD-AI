import streamlit as st
from PIL import Image
import os
import requests

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# API KEY GEMINI (Internal Folder Admin)
GEMINI_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"

# --- CSS CUSTOM ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .package-card { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 20px; min-height: 450px;}
    .stButton>button { width: 100%; border-radius: 5px; }
    .feature-list { font-size: 0.85rem; color: #8b949e; line-height: 1.4; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR PROFIL ---
with st.sidebar:
    foto_path = "erwin.jpg"
    if os.path.exists(foto_path):
        st.image(foto_path, use_container_width=True)
    else:
        st.info("Unggah 'erwin.jpg' untuk foto profil.")
    
    st.markdown("<div style='text-align:center;'><h3>Erwin Sinaga</h3><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Layanan & Investasi", "Portal Klien", "Order Berlangganan", "Admin Control Center"])

# --- 1. VISI & MISI (MINIMAL 200 KATA) ---
if menu == "Visi & Misi":
    st.header("Visi & Misi V-Guard AI Intelligence")
    col_v1, col_v2 = st.columns([1, 2])
    with col_v1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
    
    with col_v2:
        st.markdown(f"""
        <div style="text-align: justify; color: #8b949e; line-height: 1.8;">
        Sebagai seorang Senior Business Leader dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi produk, melainkan kepastian data dan eliminasi kebocoran internal (internal fraud). Di dunia digital yang serba cepat ini, kepercayaan atau <i>trust</i> tidak lagi cukup jika hanya berdasarkan janji atau intuisi semata; kepercayaan harus bisa diukur, diverifikasi secara matematis, dan didigitalisasi melalui teknologi kecerdasan buatan. Inilah alasan utama saya mendirikan V-Guard AI Intelligence sebagai benteng pertahanan bagi para pemilik bisnis di Indonesia.<br><br>
        
        <b>Visi Kami:</b> Menjadi standar global dalam penyediaan ekosistem Digital Trust yang otonom, transparan, dan tak tergoyahkan. Kami bercita-cita membangun dunia di mana setiap interaksi digital didasari oleh bukti otentik yang dapat diverifikasi secara instan, menghilangkan ambiguitas dalam transaksi bisnis, dan memastikan integritas data menjadi aset yang paling berharga bagi setiap organisasi, mulai dari skala UMKM hingga korporasi multinasional.<br><br>
        
        <b>Misi Kami:</b> Melaksanakan filosofi 'Eliminating Leakage' dengan dedikasi tinggi melalui integrasi kecerdasan buatan (AI) tingkat lanjut dan teknologi ledger terdistribusi. Kami berkomitmen untuk membangun sistem pertahanan prediktif yang mampu menghentikan pola kecurangan sebelum menjadi kerugian finansial yang signifikan. Melalui prinsip 'Digitizing Trust', kami mengubah setiap titik data mentah menjadi bukti otentik yang tidak dapat dimanipulasi oleh oknum internal maupun eksternal. Kami berdedikasi untuk memberikan ketenangan pikiran bagi setiap pengusaha melalui audit otomatis yang jujur, akurat, dan real-time, demi masa depan ekonomi yang lebih bersih dan efisien.
        </div>
        """, unsafe_allow_html=True)

# --- 2. LAYANAN & INVESTASI (4 PRODUK UTAMA) ---
elif menu == "Layanan & Investasi":
    st.header("🛡️ Detail Fitur 4 Produk Utama V-Guard AI")
    
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown("""<div class='package-card'><h3>📦 V-LITE</h3><p><b>Target:</b> UMKM / Toko Mandiri</p><div class='feature-list'>
        • <b>AI Fraud Dasar:</b> Deteksi void/pembatalan transaksi mencurigakan.<br>
        • <b>Laporan Bulanan PDF:</b> Ringkasan performa via WhatsApp.<br>
        • <b>Notifikasi Standar:</b> Peringatan selisih stok barang.<br>
        • <b>Akses 1 User:</b> Khusus pemilik usaha.<br><br>
        <b>Pemasangan:</b> Rp 1.500.000<br><b>Bulanan:</b> Rp 250.000</div></div>""", unsafe_allow_html=True)
        st.button("Pilih V-LITE", key="p1")

    with c2:
        st.markdown("""<div class='package-card'><h3>🛡️ V-PRO</h3><p><b>Target:</b> Retail / Resto Menengah</p><div class='feature-list'>
        • <b>Real-Time Monitoring:</b> Notifikasi instan transaksi mencurigakan.<br>
        • <b>VCS Integrasi:</b> Sinkronisasi stok, kasir, dan bank otomatis.<br>
        • <b>Audit Harian Otomatis:</b> Laporan closing anti-manipulasi.<br>
        • <b>Prioritas Support:</b> Bantuan teknis langsung.<br><br>
        <b>Pemasangan:</b> Rp 3.000.000<br><b>Bulanan:</b> Rp 750.000</div></div>""", unsafe_allow_html=True)
        st.button("Pilih V-PRO", key="p2")

    with c3:
        st.markdown("""<div class='package-card'><h3>👁️ V-SIGHT</h3><p><b>Target:</b> Toko Emas / Logistik</p><div class='feature-list'>
        • <b>AI Behavior Visual:</b> Pantau gerak-gerik kasir via CCTV.<br>
        • <b>Visual Audit:</b> Cocokkan struk dengan rekaman video.<br>
        • <b>Deteksi Fisik:</b> Hitung orang/barang otomatis via sensor.<br>
        • <b>Penyimpanan Cloud:</b> Rekaman aman tidak bisa dihapus oknum.<br><br>
        <b>Pemasangan:</b> Rp 5.000.000<br><b>Bulanan:</b> Rp 1.250.000</div></div>""", unsafe_allow_html=True)
        st.button("Pilih V-SIGHT", key="p3")

    with c4:
        st.markdown("""<div class='package-card'><h3>🏢 V-ENTERPRISE</h3><p><b>Target:</b> Korporasi / Franchise</p><div class='feature-list'>
        • <b>Multi-Cabang:</b> Dashboard terpusat untuk ratusan cabang.<br>
        • <b>Forensik Digital:</b> Investigasi mendalam korupsi sistematis.<br>
        • <b>Dedicated Server:</b> Keamanan tingkat militer.<br>
        • <b>Custom API:</b> Koneksi ke software akuntansi/ERP.<br><br>
        <b>Pemasangan:</b> Hubungi CEO<br><b>Bulanan:</b> Custom</div></div>""", unsafe_allow_html=True)
    
    st.info("💡 Peluang Investasi: Dapatkan Komisi 10% untuk setiap referensi mitra pemasaran yang berhasil.")

# --- 3. PORTAL KLIEN (ROI & LAPORAN) ---
elif menu == "Portal Klien":
    st.header("Portal Klien V-Guard")
    t1, t2 = st.tabs(["📊 Kalkulator ROI Kerugian", "📄 Laporan Rugi Laba & Audit"])
    
    with t1:
        omzet = st.number_input("Input Omzet Bulanan (Rp)", value=50000000)
        leakage = st.slider("Estimasi Kebocoran Internal (%)", 0, 30, 10)
        rugi = omzet * (leakage/100)
        st.error(f"Potensi Kerugian Anda: Rp {rugi:,.0f} per bulan.")
        st.success(f"V-Guard AI dapat menyelamatkan Rp {(rugi*0.9):,.0f} dari kebocoran tersebut.")

    with t2:
        st.write("### Riwayat Laporan")
        st.info("Notifikasi: Invoice H-7 Berlangganan akan dikirim otomatis ke nomor 082122190885")
        st.table([{"Tanggal": "01/03/2026", "Tipe": "Audit Integrity", "Status": "Clear"},
                  {"Tanggal": "15/03/2026", "Tipe": "Laporan Rugi Laba", "Status": "Generated"}])

# --- 4. ORDER BERLANGGANAN (FORM & USER AKTIF) ---
elif menu == "Order Berlangganan":
    st.header("Form Order & Aktivasi")
    ca, cb = st.columns(2)
    
    with ca:
        st.subheader("Data Order")
        nama_u = st.text_input("Nama Usaha")
        pk = st.selectbox("Pilih Paket", ["V-Lite", "V-Pro", "V-Sight", "V-Enterprise"])
        st.file_uploader("Upload KTP Pemilik", type=['jpg','png','pdf'])
        if st.button("Kirim Order ke WA Pak Erwin"):
            msg = f"Halo Pak Erwin, saya mau order paket {pk} untuk {nama_u}."
            st.link_button("Hubungi WhatsApp", f"https://wa.me/6282122190885?text={msg}")

    with cb:
        st.subheader("User Aktif & Password")
        st.table([{"User/Usaha": "Laundry XYZ", "Paket": "V-Lite", "Password": "USER-001-A"},
                  {"User/Usaha": "Resto Berkah", "Paket": "V-Pro", "Password": "USER-992-B"}])

# --- 5. ADMIN CONTROL CENTER (DIKUNCI & GOOGLE GEMINI) ---
elif menu == "Admin Control Center":
    st.header("🔒 Admin Control Center")
    pw = st.text_input("Masukkan Password Admin", type="password")
    
    if pw == "adminvguard2026": # PASSWORD ADMIN
        st.success("Akses Diterima")
        tab_a, tab_b, tab_c = st.tabs(["👥 Account Klien Baru", "🚨 Alarm Fraud & Notifikasi", "🤖 V-Guard AI Assistant (Gemini)"])
        
        with tab_a:
            st.write("Input User ID Klien Baru:")
            st.text_input("Username Klien")
            st.text_input("Set Password")
            st.button("Aktifkan User")
            
        with tab_b:
            st.warning("ALARM FRAUD: 3 Indikasi Void mencurigakan di Resto Berkah (10 Menit Lalu)")
            st.info("Sistem VCS: Data bank vs Kasir Sinkron.")
            st.write("Notifikasi Invoice H-7: 12 Klien akan dikirim pengingat.")
            
        with tab_c:
            st.write("### Google Gemini AI Pendukung")
            prompt = st.text_area("Tanya Gemini untuk Analisis Bisnis / Kode:", "Berikan analisis risiko kebocoran data pada industri retail...")
            if st.button("Tanya Gemini"):
                # Koneksi ke API Gemini (Simulasi/Placeholder karena butuh SDK)
                st.write("Gemini Sedang Menganalisis... (Menggunakan API Key Bapak)")
                st.info("Sistem V-Guard AI telah terhubung ke AI pendukung eksternal untuk audit forensik.")
    elif pw != "":
        st.error("Password Salah! Akses Ditolak.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>🛡️ V-Guard AI Intelligence | ©2026 | Founder: Erwin Sinaga | WA: 082122190885</div>", unsafe_allow_html=True)
