import streamlit as st
import os
import google.generativeai as genai

# --- 1. KONFIGURASI ENGINE AI (SOP: KEY API) ---
GEMINI_API_KEY = "ISI_API_KEY_ANDA_DI_SINI" 
genai.configure(api_key=GEMINI_API_KEY)

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# CSS Premium (SOP: UI Modern & Professional)
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    .product-card {
        background-color: #ffffff; padding: 25px; border-radius: 15px;
        border: 1px solid #e2e8f0; text-align: center; height: 100%;
        display: flex; flex-direction: column; justify-content: space-between;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); color: #1e293b;
    }
    .mission-box { 
        text-align: justify; line-height: 1.8; font-size: 15px; color: #d1d5db;
        background-color: #1e293b; padding: 30px; border-radius: 15px; border-left: 10px solid #238636;
    }
    .order-container {
        background-color: #ffffff; padding: 30px; border-radius: 15px; border: 1px solid #e2e8f0;
    }
    .activation-box {
        background-color: #1e3a8a; padding: 30px; border-radius: 15px; color: white; height: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    
    if os.path.exists("erwin.jpg"):
        try:
            st.image("erwin.jpg", use_container_width=True)
        except:
            st.info("👤 Erwin Sinaga\nFounder & CEO")
    else:
        st.info("👤 Erwin Sinaga\nFounder & CEO")
        
    st.markdown("<div style='text-align:center;'><b>Erwin Sinaga</b><br><small>Founder & CEO</small></div>", unsafe_allow_html=True)
    st.write("---")
    
    menu = st.radio("STRATEGIC NAVIGATOR", [
        "Visi & Misi", 
        "Produk & Layanan", 
        "Analisis ROI Kerugian", 
        "Portal Klien", 
        "Admin Control Center"
    ])

# --- 4. LOGIKA HALAMAN ---

if menu == "Visi & Misi":
    st.header("Visi & Misi Strategis (250+ Kata)")
    col_img, col_txt = st.columns([1, 2.5])
    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
    with col_txt:
        st.markdown("""
        <div class="mission-box">
        <b>Visi: Menjadi Jangkar Kepercayaan Digital Global</b><br>
        V-Guard AI Intelligence bervisi menciptakan ekosistem bisnis yang sepenuhnya transparan, aman, dan berintegritas tinggi melalui inovasi teknologi digital terdepan. Kami hadir bukan sekadar sebagai penyedia solusi perangkat lunak, melainkan sebagai jangkar kepercayaan (Digitizing Trust) bagi setiap pemilik bisnis di era ketidakpastian global yang serba cepat ini. Kami memastikan setiap pemilik usaha memiliki ketenangan pikiran total (Total Peace of Mind) melalui validasi kejujuran sistem secara real-time, di mana data operasional tidak lagi bisa dimanipulasi oleh kepentingan pribadi. Kami bercita-cita menjadi standar emas global dalam layanan "Integrity Assurance", di mana teknologi kecerdasan buatan otonom kami mampu menghapuskan segala bentuk keraguan operasional serta manipulasi finansial dalam dunia bisnis yang bergerak serba cepat dan kompetitif.<br><br>
        
        <b>Misi: Eliminasi Kebocoran & Perlindungan Aset Strategis</b><br>
        Misi kami adalah memberikan perlindungan aset yang tak tertembus melalui lima pilar transformasi digital yang radikal. Pertama, membangun infrastruktur integritas digital yang mampu mengubah etika kerja menjadi data terukur secara akurat, menciptakan budaya kejujuran berbasis teknologi. Kedua, menerapkan teknologi Edge Filtering yang mutakhir untuk deteksi dini anomali finansial tepat di titik kejadian transaksi, mencegah kebocoran sebelum terjadi. <b>Ketiga, memastikan efisiensi biaya infrastruktur server hingga 20% bagi seluruh mitra kami</b> melalui optimasi komputasi lokal yang cerdas, memastikan teknologi canggih tetap terjangkau dan efisien secara operasional. Keempat, memberikan kedaulatan akses penuh bagi pemilik usaha melalui Command Center terenkripsi tingkat militer yang dapat dipantau secara nasional maupun global dari genggaman tangan Anda. Terakhir, kami berkomitmen menjaga disiplin pengembangan perangkat lunak yang sangat ketat sesuai standar operasional baku V-Guard, guna menjaga warisan bisnis Anda dari risiko kecurangan sistemik, serangan siber, maupun kelalaian manusia selamanya.
        </div>
        """, unsafe_allow_html=True)

elif menu == "Produk & Layanan":
    st.header("🏷️ LAYANAN PRODUK & PAKET")
    # Daftar paket tetap konsisten
    packages = {
        "V-LITE": {"akt": "750 RB", "bln": "350 RB", "feat": "AI Fraud Detector Dasar"},
        "V-PRO": {"akt": "1.5 JT", "bln": "800 RB", "feat": "VCS Integration"},
        "V-SIGHT": {"akt": "7,5 JT", "bln": "3,5 JT", "feat": "CCTV AI Behavior"},
        "V-ENTERPRISE": {"akt": "15 JT", "bln": "10 JT", "feat": "Forensic AI (1 Year)"},
        "V-ULTRA": {"akt": "Custom", "bln": "Custom", "feat": "Military Grade Encryption"}
    }
    cols = st.columns(5)
    for i, (name, info) in enumerate(packages.items()):
        with cols[i]:
            st.markdown(f"""<div class="product-card"><div><b>{name}</b><br><small>{info['feat']}</small></div><div class="price-box">Akt: {info['akt']}<br><b>Bln: {info['bln']}</b></div></div>""", unsafe_allow_html=True)

elif menu == "Portal Klien":
    st.header("📱 Portal Onboarding & Aktivasi Klien")
    
    col_order, col_active = st.columns([2, 1])
    
    with col_order:
        st.markdown('<div class="order-container">', unsafe_allow_html=True)
        st.subheader("📝 Form Pemesanan Baru")
        with st.form("order_form"):
            c1, c2 = st.columns(2)
            with c1:
                nama = st.text_input("Nama Lengkap")
                nama_usaha = st.text_input("Nama Usaha / PT")
            with c2:
                produk = st.selectbox("Pilih Produk", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE", "V-ULTRA"])
                st.info("Harga akan menyesuaikan pilihan produk")
            
            ktp = st.file_uploader("Upload KTP (JPG/PNG)", type=["jpg", "png", "jpeg"])
            
            submitted = st.form_submit_button("Kirim Pesanan & Lanjut Pembayaran")
            if submitted:
                st.success(f"Terima kasih {nama}! Pesanan {produk} untuk {nama_usaha} telah diterima. Silakan hubungi Admin untuk instruksi pembayaran.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_active:
        st.markdown('<div class="activation-box">', unsafe_allow_html=True)
        st.subheader("🔑 Aktivasi Klien")
        st.write("Jika sudah membayar, masukkan kredensial Anda:")
        client_id = st.text_input("Client ID")
        client_pwd = st.text_input("Password", type="password")
        if st.button("Login Command Center"):
            if client_id and client_pwd:
                st.success("Akses Diterima! Mengalihkan ke Command Center...")
            else:
                st.warning("Silakan masukkan ID dan Password.")
        st.markdown('</div>', unsafe_allow_html=True)

elif menu == "Analisis ROI Kerugian":
    st.header("📊 Analisis ROI")
    omzet = st.number_input("Omzet Bulanan", value=100000000)
    st.metric("Efisiensi Server", "20%", delta="V-Guard Active")

elif menu == "Admin Control Center":
    st.header("🔒 Admin Control")
    pwd = st.text_input("Password", type="password")
    if pwd == "w1nbju8282":
        st.success("Efisiensi 20% Active")
