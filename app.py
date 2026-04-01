import streamlit as st
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# --- 2. CSS CUSTOM (PREMIUM DARK MODE) ---
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

# --- 3. SIDEBAR PROFIL ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    foto_path = "erwin.jpg"
    if os.path.exists(foto_path):
        try: st.image(foto_path, use_container_width=True)
        except: st.info("Founder & CEO")
    st.markdown("<div style='text-align:center;'><p style='color:gray;'>Founder & CEO V-Guard AI</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGASI UTAMA", ["Visi & Misi", "Produk & Layanan", "Analisis ROI Kerugian", "Portal Klien", "Admin Control Center"])

# --- 4. LOGIKA MENU ---

# MENU 1: VISI & MISI (NARASI PROFESIONAL 250+ KATA)
if menu == "Visi & Misi":
    st.header("Visi & Misi V-Guard AI Intelligence")
    col_v1, col_v2 = st.columns([1, 2])
    with col_v1:
        if os.path.exists("erwin.jpg"): 
            st.image("erwin.jpg", caption="Founder & CEO V-Guard AI")
    with col_v2:
        st.markdown("""
        <div style="text-align: justify; color: #c9d1d9; line-height: 1.8;">
        Berangkat dari pengalaman luas sebagai pemimpin bisnis senior selama lebih dari sepuluh tahun di sektor perbankan dan manajemen aset, saya menyadari bahwa tantangan terbesar dalam pertumbuhan usaha bukanlah sekadar kompetisi pasar, melainkan risiko kebocoran internal (internal fraud) yang seringkali tidak terdeteksi. Dalam perjalanan profesional tersebut, saya sering mengamati bagaimana bisnis yang sangat potensial hancur bukan karena faktor eksternal, melainkan karena kelemahan sistem pengawasan internal yang bisa dimanipulasi. Kepercayaan konvensional yang hanya berlandaskan komitmen verbal kini tidak lagi memadai dalam ekosistem ekonomi digital yang kompleks. Diperlukan sebuah sistem di mana kepercayaan tersebut dapat diukur, diverifikasi secara matematis, dan didigitalisasi untuk menciptakan transparansi mutlak bagi setiap pemilik modal.<br><br>
        
        <b>Visi Kami:</b> Menjadi standar global utama dalam penyediaan ekosistem <i>Digital Trust</i> yang sepenuhnya otonom, transparan, dan tidak dapat dimanipulasi oleh pihak mana pun. Kami bertekad membangun dunia bisnis di mana setiap interaksi dan transaksi didasari oleh bukti otentik yang dapat diverifikasi secara instan. Kami bercita-cita untuk menghilangkan segala bentuk ambiguitas operasional dan memastikan bahwa integritas data menjadi pilar utama serta aset yang paling berharga bagi setiap organisasi, mulai dari sektor UMKM hingga korporasi besar, demi menciptakan iklim usaha yang bersih, sehat, dan memiliki tingkat kepercayaan digital yang tinggi di kancah persaingan global.<br><br>
        
        <b>Misi Kami:</b> Kami berdedikasi untuk mengimplementasikan filosofi 'Eliminating Leakage' secara disiplin melalui integrasi mendalam antara kecerdasan buatan (AI) prediktif dan teknologi Computer Vision mutakhir. Misi kami adalah membangun sistem pertahanan berlapis yang mampu mengidentifikasi serta menghentikan pola kecurangan sebelum berkembang menjadi kerugian finansial yang nyata bagi klien kami. Melalui prinsip 'Digitizing Trust', kami berkomitmen mengubah data mentah menjadi bukti digital yang sah dan permanen. Kami hadir untuk memberikan ketenangan pikiran bagi setiap pengusaha melalui sistem audit otomatis yang jujur, akurat, dan bekerja secara <i>real-time</i> selama 24 jam penuh untuk memastikan setiap rupiah aset Anda terlindungi dengan sempurna.
        </div>
        """, unsafe_allow_html=True)

# MENU 2: PRODUK & LAYANAN (HARGA MINIMAL 1JT, TANPA INFO KONTAK PRIBADI)
elif menu == "Produk & Layanan":
    st.header("🛡️ Produk & Layanan V-Guard AI")
    wa_base = "https://wa.me/?text=Halo,%20saya%20ingin%20order%20"
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
    st.header("📊 Analisis Potensi Kerugian vs ROI")
    col_a, col_b = st.columns(2)
    with col_a:
        omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000, step=10000000)
        leak = st.slider("Estimasi Kebocoran / Fraud (%)", 1, 20, 5)
        loss = omzet * (leak / 100)
        st.error(f"Potensi Kerugian: Rp {loss:,.0f} / bulan")
    with col_b:
        biaya = st.selectbox("Pilih Rencana Investasi Paket", [1000000, 2500000, 5000000, 10000000])
        saved = loss - biaya
        st.success(f"Profit yang Diselamatkan: Rp {saved:,.0f} / bln")
        st.metric("Estimasi ROI", f"{(saved/biaya)*100 if saved>0 else 0:.0f}%")

# MENU 4: PORTAL KLIEN
elif menu == "Portal Klien":
    st.header("Portal Klien V-Guard AI")
    col_order, col_login = st.columns(2)
    with col_order:
        st.subheader("📝 Form Order Baru")
        with st.container(border=True):
            nama_u = st.text_input("Nama Usaha / Perusahaan")
            paket_u = st.selectbox("Paket yang Dipilih", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.file_uploader("Upload KTP Pemilik Bisnis", type=['jpg', 'png', 'pdf'])
            if st.button("Kirim Data Registrasi"):
                st.success("Data telah masuk ke sistem. Sil
