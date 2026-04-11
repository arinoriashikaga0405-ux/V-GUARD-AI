import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE AI ---
GEMINI_API_KEY = "ISI_API_KEY_ANDA_DI_SINI" 
genai.configure(api_key=GEMINI_API_KEY)

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Minimalis Profesional
st.markdown("""
    <style>
    .justified-text { text-align: justify; line-height: 1.8; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# Fungsi Penanganan Foto (Anti-Crash)
def load_founder_image(image_path):
    if os.path.exists(image_path):
        try:
            img = Image.open(image_path)
            return img
        except Exception:
            return None
    return None

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    
    founder_img = load_founder_image("erwin.jpg")
    if founder_img:
        st.image(founder_img, use_container_width=True)
    else:
        st.warning("👤 Foto Founder belum terunggah/format salah.")
        
    st.markdown("**Erwin Sinaga** \nFounder & CEO")
    st.write("---")
    menu = st.radio("NAVIGATION", [
        "Visi & Misi", 
        "Produk & Layanan", 
        "Analisis ROI Kerugian", 
        "Portal Klien", 
        "Admin Control Center"
    ])

# --- 4. LOGIKA HALAMAN ---

if menu == "Visi & Misi":
    st.header("Visi & Misi Strategis")
    st.markdown('<div class="justified-text">', unsafe_allow_html=True)
    st.write("""
    **Visi: Menjadi Jangkar Kepercayaan Digital Global** V-Guard AI Intelligence bervisi menciptakan ekosistem bisnis yang sepenuhnya transparan, aman, dan berintegritas tinggi melalui inovasi teknologi digital terdepan. Kami hadir bukan sekadar sebagai penyedia solusi perangkat lunak, melainkan sebagai jangkar kepercayaan (Digitizing Trust) bagi setiap pemilik bisnis di era ketidakpastian global yang serba cepat ini. Kami memastikan setiap pemilik usaha memiliki ketenangan pikiran total (Total Peace of Mind) melalui validasi kejujuran sistem secara real-time, di mana data operasional tidak lagi bisa dimanipulasi oleh kepentingan pribadi. Kami bercita-cita menjadi standar emas global dalam layanan "Integrity Assurance", di mana teknologi kecerdasan buatan otonom kami mampu menghapuskan segala bentuk keraguan operasional serta manipulasi finansial dalam dunia bisnis yang bergerak serba cepat dan kompetitif.  

    **Misi: Eliminasi Kebocoran & Perlindungan Aset Strategis** Misi kami adalah memberikan perlindungan aset yang tak tertembus melalui lima pilar transformasi digital yang radikal. Pertama, membangun infrastruktur integritas digital yang mampu mengubah etika kerja menjadi data terukur secara akurat, menciptakan budaya kejujuran berbasis teknologi. Kedua, menerapkan teknologi Edge Filtering yang mutakhir untuk deteksi dini anomali finansial tepat di titik kejadian transaksi, mencegah kebocoran sebelum terjadi. **Ketiga, memastikan efisiensi biaya infrastruktur server hingga 20% bagi seluruh mitra kami** melalui optimasi komputasi lokal yang cerdas, memastikan teknologi canggih tetap terjangkau dan efisien secara operasional. Keempat, memberikan kedaulatan akses penuh bagi pemilik usaha melalui Command Center terenkripsi tingkat militer yang dapat dipantau secara nasional maupun global dari genggaman tangan Anda. Terakhir, kami berkomitmen menjaga disiplin pengembangan perangkat lunak yang sangat ketat sesuai standar operasional baku V-Guard, guna menjaga warisan bisnis Anda dari risiko kecurangan sistemik, serangan siber, maupun kelalaian manusia selamanya. Kami berjanji untuk terus berinovasi tanpa henti, memastikan setiap rupiah aset Anda terlindungi oleh kecerdasan buatan yang jujur dan objektif.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "Produk & Layanan":
    st.header("Daftar Produk & Layanan")
    st.table([
        {"Produk": "V-LITE", "Target": "Mikro / 1 Kasir", "Aktivasi": "750 RB", "Bulanan": "350 RB"},
        {"Produk": "V-PRO", "Target": "Retail & Kafe", "Aktivasi": "1.5 JT", "Bulanan": "800 RB"},
        {"Produk": "V-SIGHT", "Target": "Gudang & Toko", "Aktivasi": "7.5 JT", "Bulanan": "3.5 JT"},
        {"Produk": "V-ENTERPRISE", "Target": "Korporasi / Besar", "Aktivasi": "15 JT", "Bulanan": "10 JT"},
        {"Produk": "V-ULTRA", "Target": "High-Security", "Aktivasi": "Custom", "Bulanan": "Custom"},
    ])

elif menu == "Portal Klien":
    st.header("Portal Onboarding & Akses Klien")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Pemesanan Baru")
        st.text_input("Nama Lengkap")
        st.text_input("Nama Usaha")
        st.selectbox("Produk", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE", "V-ULTRA"])
        st.file_uploader("Upload KTP")
        st.button("Kirim Pesanan")

    with col2:
        st.subheader("Aktivasi & Login")
        st.text_input("ID Klien")
        st.text_input("Password", type="password")
        st.button("Masuk Command Center")

elif menu == "Analisis ROI Kerugian":
    st.header("Analisis ROI")
    omzet = st.number_input("Omzet Bulanan (Rp)", value=100000000)
    st.write(f"Efisiensi Server: **20%**")
    st.write(f"Estimasi Dana Diselamatkan: **Rp {(omzet * 0.05):,.0f}** /bulan")

elif menu == "Admin Control Center":
    st.header("Admin Control")
    if st.text_input("Master Password", type="password") == "w1nbju8282":
        st.metric("Status Server", "Efisiensi 20% Active")
        st.metric("Aset Terpantau", "Rp 1.250.000.000")
