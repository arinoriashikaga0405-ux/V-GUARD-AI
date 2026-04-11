import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# --- BAGIAN 0: KONFIGURASI API KEY ---
GEMINI_API_KEY = "ISI_API_KEY_ANDA_DI_SINI" 

try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Koneksi AI Terganggu: {e}")

# --- BAGIAN 1: KONFIGURASI HALAMAN & CSS ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .justified-text { text-align: justify; line-height: 1.8; font-size: 16px; }
    .roi-container {
        background-color: #ffffff; padding: 30px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #1e3a8a;
    }
    .product-box {
        border: 1px solid #e2e8f0; border-radius: 10px; padding: 15px;
        text-align: center; height: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BAGIAN 2: SIDEBAR (PROFIL & NAVIGASI) ---
with st.sidebar:
    # Judul V-Guard AI di tengah atas kepala foto
    st.markdown("<h2 style='text-align:center; margin-bottom: -10px;'>V-Guard AI</h2>", unsafe_allow_html=True)
    
    if os.path.exists("erwin.jpg"):
        try:
            img = Image.open("erwin.jpg")
            st.image(img, use_container_width=True)
        except:
            st.info("👤 Foto Founder")
    else:
        st.info("👤 Foto Founder")
        
    # Hanya Founder - CEO di bawah foto
    st.markdown("<div style='text-align:center; font-weight:bold;'>Founder - CEO</div>", unsafe_allow_html=True)
    st.write("---")
    
    menu = st.radio("STRATEGIC NAVIGATOR", [
        "Visi & Misi", 
        "Produk & Layanan", 
        "Analisis ROI Kerugian", 
        "Portal Klien", 
        "Admin Control Center"
    ])

# --- BAGIAN 3: LOGIKA HALAMAN ---

if menu == "Visi & Misi":
    st.header("Visi & Misi Strategis")
    col_img, col_txt = st.columns([1, 2.5])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col_txt:
        st.markdown('<div class="justified-text">', unsafe_allow_html=True)
        st.write("""
        **Visi: Menjadi Jangkar Kepercayaan Digital Global** V-Guard AI Intelligence bervisi menciptakan ekosistem bisnis yang sepenuhnya transparan, aman, dan berintegritas tinggi melalui inovasi teknologi digital terdepan. Kami hadir bukan sekadar sebagai penyedia solusi perangkat lunak, melainkan sebagai jangkar kepercayaan bagi setiap pemilik bisnis di era ketidakpastian global yang serba cepat ini. Kami memastikan setiap pemilik usaha memiliki ketenangan pikiran total melalui validasi kejujuran sistem secara real-time, di mana data operasional tidak lagi bisa dimanipulasi oleh kepentingan pribadi. Kami bercita-cita menjadi standar emas global dalam layanan Integrity Assurance, di mana teknologi kecerdasan buatan otonom kami mampu menghapuskan segala bentuk keraguan operasional serta manipulasi finansial dalam dunia bisnis yang kompetitif.  

        **Misi: Eliminasi Kebocoran & Perlindungan Aset Strategis** Misi kami adalah memberikan perlindungan aset yang tak tertembus melalui lima pilar transformasi digital. Pertama, membangun infrastruktur integritas digital yang mampu mengubah etika kerja menjadi data terukur secara akurat. Kedua, menerapkan teknologi Edge Filtering yang mutakhir untuk deteksi dini anomali finansial tepat di titik kejadian transaksi, mencegah kebocoran sebelum terjadi. **Ketiga, memastikan efisiensi biaya infrastruktur server hingga 20% bagi seluruh mitra kami** melalui optimasi komputasi lokal yang cerdas, memastikan teknologi canggih tetap terjangkau dan efisien secara operasional. Keempat, memberikan kedaulatan akses penuh bagi pemilik usaha melalui Command Center terenkripsi tingkat militer yang dapat dipantau secara nasional maupun global. Terakhir, kami berkomitmen menjaga disiplin pengembangan perangkat lunak yang sangat ketat sesuai standar operasional baku V-Guard, guna menjaga warisan bisnis Anda dari risiko kecurangan sistemik, serangan siber, maupun kelalaian manusia selamanya.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

elif menu == "Produk & Layanan":
    st.header("🏷️ Daftar Produk & Paket")
    pkgs = {
        "V-LITE": {"akt": "1.5 Jt", "bln": "750 rb", "target": "Mikro / 1 Kasir"},
        "V-PRO": {"akt": "3 Jt", "bln": "1.5 Jt", "target": "Retail & Kafe"},
        "V-SIGHT": {"akt": "7,5 Jt", "bln": "3,5 Jt", "target": "Gudang & Toko"},
        "V-ENTERPRISE": {"akt": "15 Jt", "bln": "10 Jt", "target": "Korporasi"},
        "V-ULTRA": {"akt": "25 Jt", "bln": "14.9 Jt", "target": "Investor/VIP"}
    }
    cols = st.columns(5)
    for i, (name, info) in enumerate(pkgs.items()):
        with cols[i]:
            st.markdown(f"""
            <div class="product-box">
                <div style="font-weight: bold; color: #1e3a8a;">{name}</div>
                <small>{info['target']}</small><br><br>
                <small>Aktivasi: {info['akt']}</small><br>
                <b style="color: #2563eb;">Bln: {info['bln']}</b>
            </div>
            """, unsafe_allow_html=True)
            st.button(f"Pilih {name}", key=name, use_container_width=True)

elif menu == "Analisis ROI Kerugian":
    st.header("📊 Dashboard Penyelamatan Aset")
    st.markdown('<div class="roi-container">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        omzet = st.number_input("Input Omzet Bulanan (Rp)", value=100000000, step=10000000)
        leak = st.slider("Asumsi Kebocoran (%)", 1, 15, 5)
    with c2:
        saved = (omzet * leak / 100)
        st.metric("Dana Diselamatkan", f"Rp {saved:,.0f}", delta="Potensi Per Bulan")
        st.metric("Efisiensi Server", "20% Active", delta_color="normal")
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "Portal Klien":
    st.header("📱 Portal Onboarding")
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.subheader("Form Order")
        st.text_input("Nama Lengkap")
        st.text_input("Nama Usaha")
        st.selectbox("Paket", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE", "V-ULTRA"])
        st.file_uploader("Upload KTP")
    with col_b:
        st.subheader("Aktivasi")
        st.text_input("ID Klien")
        st.text_input("Password", type="password")
        st.button("Login Center", use_container_width=True)

elif menu == "Admin Control Center":
    st.header("🔒 Admin Center")
    if st.text_input("Master Password", type="password") == "w1nbju8282":
        st.metric("Efisiensi Infrastruktur", "20% Active")
        st.metric("Total Dana Terlindungi", "Rp 1.250.000.000")
