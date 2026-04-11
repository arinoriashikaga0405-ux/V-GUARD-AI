import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE AI ---
GEMINI_API_KEY = "ISI_API_KEY_ANDA_DI_SINI" 
genai.configure(api_key=GEMINI_API_KEY)

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Profesional (Bersih, Tanpa Kotak Norak)
st.markdown("""
    <style>
    .main-text { text-align: justify; line-height: 1.8; font-size: 16px; color: #1e293b; }
    .product-header { font-size: 20px; font-weight: bold; color: #1e3a8a; margin-bottom: 5px; }
    .price-text { color: #2563eb; font-weight: 700; font-size: 18px; }
    .login-sidebar { background-color: #f1f5f9; padding: 20px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Fungsi Anti-Crash Foto
def safe_image_load(path):
    if os.path.exists(path):
        try:
            return Image.open(path)
        except:
            return None
    return None

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("### 🛡️ V-Guard AI")
    img = safe_image_load("erwin.jpg")
    if img:
        st.image(img, use_container_width=True)
    st.markdown("**Erwin Sinaga**\nFounder & CEO")
    st.write("---")
    menu = st.radio("STRATEGIC MENU", [
        "Visi & Misi", 
        "Produk & Layanan", 
        "Analisis ROI Kerugian", 
        "Portal Klien", 
        "Admin Control Center"
    ])

# --- 4. LOGIKA HALAMAN ---

if menu == "Visi & Misi":
    st.header("Visi & Misi Strategis")
    st.markdown('<div class="main-text">', unsafe_allow_html=True)
    st.write("""
    **Visi: Menjadi Jangkar Kepercayaan Digital Global** V-Guard AI Intelligence bervisi menciptakan ekosistem bisnis yang sepenuhnya transparan, aman, dan berintegritas tinggi melalui inovasi teknologi digital terdepan. Kami hadir bukan sekadar sebagai penyedia solusi perangkat lunak, melainkan sebagai jangkar kepercayaan (Digitizing Trust) bagi setiap pemilik bisnis di era ketidakpastian global yang serba cepat ini. Kami memastikan setiap pemilik usaha memiliki ketenangan pikiran total (Total Peace of Mind) melalui validasi kejujuran sistem secara real-time, di mana data operasional tidak lagi bisa dimanipulasi oleh kepentingan pribadi. Kami bercita-cita menjadi standar emas global dalam layanan "Integrity Assurance", di mana teknologi kecerdasan buatan otonom kami mampu menghapuskan segala bentuk keraguan operasional serta manipulasi finansial dalam dunia bisnis yang bergerak serba cepat dan kompetitif.  

    **Misi: Eliminasi Kebocoran & Perlindungan Aset Strategis** Misi kami adalah memberikan perlindungan aset yang tak tertembus melalui lima pilar transformasi digital yang radikal. Pertama, membangun infrastruktur integritas digital yang mampu mengubah etika kerja menjadi data terukur secara akurat, menciptakan budaya kejujuran berbasis teknologi. Kedua, menerapkan teknologi Edge Filtering yang mutakhir untuk deteksi dini anomali finansial tepat di titik kejadian transaksi, mencegah kebocoran sebelum terjadi. **Ketiga, memastikan efisiensi biaya infrastruktur server hingga 20% bagi seluruh mitra kami** melalui optimasi komputasi lokal yang cerdas, memastikan teknologi canggih tetap terjangkau dan efisien secara operasional. Keempat, memberikan kedaulatan akses penuh bagi pemilik usaha melalui Command Center terenkripsi tingkat militer yang dapat dipantau secara nasional maupun global dari genggaman tangan Anda. Terakhir, kami berkomitmen menjaga disiplin pengembangan perangkat lunak yang sangat ketat sesuai standar operasional baku V-Guard, guna menjaga warisan bisnis Anda dari risiko kecurangan sistemik, serangan siber, maupun kelalaian manusia selamanya. Kami berjanji untuk terus berinovasi tanpa henti, memastikan setiap rupiah aset Anda terlindungi oleh kecerdasan buatan yang jujur dan objektif.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "Produk & Layanan":
    st.header("Daftar Produk & Layanan")
    cols = st.columns(5)
    packages = [
        ("V-LITE", "Mikro", "750 RB", "350 RB"),
        ("V-PRO", "Retail", "1.5 JT", "800 RB"),
        ("V-SIGHT", "Gudang", "7.5 JT", "3.5 JT"),
        ("V-ENTERPRISE", "Besar", "15 JT", "10 JT"),
        ("V-ULTRA", "High-Sec", "Custom", "Custom")
    ]
    for i, (name, target, akt, bln) in enumerate(packages):
        with cols[i]:
            st.markdown(f"<div class='product-header'>{name}</div>", unsafe_allow_html=True)
            st.write(f"Target: {target}")
            st.write(f"Aktivasi: {akt}")
            st.markdown(f"<div class='price-text'>Bln: {bln}</div>", unsafe_allow_html=True)
            st.button(f"Pesan {name}", key=name)

elif menu == "Portal Klien":
    st.header("Portal Klien: Onboarding & Aktivasi")
    col_form, col_login = st.columns([2, 1], gap="large")
    
    with col_form:
        st.subheader("📝 Registrasi & Order")
        st.text_input("Nama Lengkap")
        st.text_input("Nama Usaha")
        st.selectbox("Pilih Produk", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE", "V-ULTRA"])
        st.file_uploader("Upload KTP (Persyaratan SOP)")
        st.button("Kirim Form Pemesanan")

    with col_login:
        st.markdown('<div class="login-sidebar">', unsafe_allow_html=True)
        st.subheader("🔑 Login Aktivasi")
        st.write("Masukkan kredensial yang telah diaktivasi Admin.")
        st.text_input("Client ID")
        st.text_input("Password", type="password")
        st.button("Login Command Center", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif menu == "Analisis ROI Kerugian":
    st.header("Analisis ROI & Efisiensi")
    omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
    st.metric("Pencegahan Kebocoran", f"Rp {(omzet * 0.05):,.0f}")
    st.metric("Efisiensi Biaya Server", "20% Terjamin")

elif menu == "Admin Control Center":
    st.header("🔒 Admin Center")
    if st.text_input("Password", type="password") == "w1nbju8282":
        st.success("Akses Diterima.")
        st.metric("Dana Terlindungi", "Rp 1.250.000.000", delta="Efisiensi 20%")
