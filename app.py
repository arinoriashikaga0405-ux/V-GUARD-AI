import streamlit as st
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG & KEAMANAN ---
WHATSAPP_NUMBER = "6282122190885" 
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# --- 2. SETUP TEMA PREMIUM ---
st.set_page_config(page_title="V-Guard AI | Founder", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0a192f; color: #e6f1ff; }
    .sidebar .sidebar-content { background-image: linear-gradient(#0a192f, #112240); }
    .founder-name { 
        text-align: center; font-weight: bold; font-size: 24px; 
        color: white; margin-top: 15px; margin-bottom: 0px; 
    }
    .founder-title { 
        text-align: center; color: #8892b0; font-size: 14px; margin-top: 0px; 
    }
    .price-box { 
        background-color: #112240; padding: 20px; border-radius: 15px; 
        border: 1px solid #233554; text-align: center; 
    }
    .ai-card {
        background-color: #0d1b2a; padding: 12px; border-left: 4px solid #64ffda;
        margin-bottom: 10px; border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: LAYOUT RAPI ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_column_width=True)
    
    # NAMA SEJAJAR RAPI
    st.markdown('<p class="founder-name">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p class="founder-title">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.markdown("<hr style='border: 0.2px solid #233554;'>", unsafe_allow_html=True)

    # NAVIGASI DENGAN PROTEKSI EKOSISTEM
    nav_options = ["🏠 Home", "📦 Produk & Layanan", "🔑 Portal Klien", "🔐 Admin Panel"]
    
    # Hanya tampil jika admin sudah login
    if st.session_state['authenticated']:
        nav_options.insert(1, "🧠 Ekosistem 9 AI Engine")

    menu = st.radio("NAVIGASI SISTEM:", nav_options)
    
    # PINDAHKAN CHATBOT KE BAWAH SEKALI
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.divider()
    st.markdown("### 🤖 V-Guard NLP Bot")
    st.text_input("Interaksi Teks...", placeholder="Audit hari ini?")

# --- FUNGSI PESAN WA ---
def get_wa_url(paket):
    msg = f"Halo Pak Erwin, saya tertarik paket {paket}. Mohon infonya."
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={msg.replace(' ', '%20')}"

# --- 📂 HALAMAN 1: HOME ---
if menu == "🏠 Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.subheader("Digitizing Trust, Eliminating Leakage")
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_column_width=True)
            
    with col2:
        st.header("Visi & Misi")
        st.markdown("""
        Sebagai seorang **Senior Business Leader** dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, 
        saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi, melainkan **ketidakpastian data dan kebocoran internal**. 
        Di dunia digital yang serba cepat ini, kepercayaan (trust) tidak lagi cukup jika hanya berdasarkan janji atau intuisi; 
        kepercayaan harus bisa diukur, diverifikasi, dan didigitalisasi. Inilah alasan utama saya mendirikan **V-Guard AI Intelligence**.

        Visi kami adalah menjadi standar global dalam **Digital Trust**. Kami percaya bahwa setiap pemilik bisnis—mulai dari tokoh retail 
        mandiri (V-LITE) hingga korporasi multinasional (V-ENTERPRISE)—berhak mendapatkan transparansi mutlak atas aset mereka. 
        Melalui prinsip **'Digitizing Trust'**, kami mengubah setiap titik data mentah dari CCTV, mesin kasir (POS), laporan stok gudang (VCS), 
        dan mutasi bank menjadi bukti otentik yang tidak dapat dimanipulasi oleh siapa pun.

        Misi utama kami, **'Eliminating Leakage'**, dijalankan dengan mengorkestrasikan 9 platform AI tercanggih di dunia (termasuk Gemini, 
        MindBridge, dan YOLO). Kami tidak hanya mendeteksi kecurangan (fraud) setelah terjadi, tetapi kami membangun benteng pertahanan 
        prediktif untuk menghentikan pola kebocoran sebelum menjadi kerugian finansial yang signifikan. Dengan V-Guard AI, kami mengembalikan 
        kendali penuh ke tangan pemilik usaha, memberikan ketenangan pikiran (*peace of mind*), dan memastikan setiap rupiah yang Anda investasikan 
        bekerja secara jujur dan optimal untuk masa depan bisnis Anda.
        """)
        st.caption("— Erwin Sinaga, Founder V-Guard AI")

# --- 📂 HALAMAN 2: EKOSISTEM (CONFIDENTIAL) ---
elif menu == "🧠 Ekosistem 9 AI Engine":
    st.header("🧠 Multi-AI Engine Integration (Internal Only)")
    st.info("Akses Terproteksi: Komponen ini disembunyikan dari akses publik.")
    ca1, ca2 = st.columns(2)
    with ca1:
        st.markdown('<div class="ai-card"><b>1. Google Gemini AI</b><br>Core Analyser data kompleks.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>2. MindBridge</b><br>Fraud Detection akuntansi.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>3. DataRobot</b><br>Risk Forecasting.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>4. YOLO Vision</b><br>Monitoring stok visual.</div>', unsafe_allow_html=True)
    with ca2:
        st.markdown('<div class="ai-card"><b>5. Alteryx</b><br>Workflow Automation.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>6. Workday Adaptive</b><br>Scenario Planning.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>7. Numeric.ai</b><br>Smart Notification.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>8. OCR & NLP Bot</b><br>Digitalisasi dokumen.</div>', unsafe_allow_html=True)

# --- 📂 HALAMAN 3: PRODUK ---
elif menu == "📦 Produk & Layanan":
    st.header("Layanan & Skema Investasi")
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.markdown(f'<div class="price-box"><b>V-LITE</b><br><hr>Pasang: 1.5M<br>Bulanan: 250rb<br><br><a href="{get_wa_url("V-LITE")}" style="color:#25D366;text-decoration:none;font-weight:bold;">💬 Chat WA</a></div>', unsafe_allow_html=True)
    with p2:
        st.markdown(f'<div class="price-box"><b>V-PRO</b><br><hr>Pasang: 3.5M<br>Bulanan: 750rb<br><br><a href="{get_wa_url("V-PRO")}" style="color:#25D366;text-decoration:none;font-weight:bold;">💬 Chat WA</a></div>', unsafe_allow_html=True)
    with p3:
        st.markdown(f'<div class="price-box"><b>V-SIGHT</b><br><hr>Pasang: 5.0M<br>Bulanan: 1.2jt<br><br><a href="{get_wa_url("V-SIGHT")}" style="color:#25D366;text-decoration:none;font-weight:bold;">💬 Chat WA</a></div>', unsafe_allow_html=True)
    with p4:
        st.markdown(f'<div class="price-box"><b>V-ENTERPRISE</b><br><hr>CUSTOM<br>Full Ecosystem<br><br><a href="{get_wa_url("V-ENTERPRISE")}" style="color:#25D366;text-decoration:none;font-weight:bold;">💬 Chat WA</a></div>', unsafe_allow_html=True)

# --- 📂 HALAMAN 4: PORTAL KLIEN ---
elif menu == "🔑 Portal Klien":
    st.header("🔑 Secure Upload Center")
    with st.form("u_form"):
        st.text_input("Nama Bisnis")
        st.file_uploader("Upload Data Audit")
        if st.form_submit_button("🚀 Proses"):
            st.success("Data berhasil masuk ke antrean AI.")

# --- 📂 HALAMAN 5: ADMIN PANEL ---
elif menu == "🔐 Admin Panel":
    st.header("🔐 CEO Command Center")
    if not st.session_state['authenticated']:
        pwd = st.text_input("Masukkan Sandi Founder", type="password")
        if st.button("Login"):
            if hashlib.sha256(pwd.encode()).hexdigest() == ADMIN_PWD_HASH:
                st.session_state['authenticated'] = True
                st.rerun()
            else:
                st.error("Sandi Salah.")
    else:
        st.success("Selamat Datang, Pak Erwin. Menu 'Ekosistem' sekarang terbuka.")
        st.metric("Leakage Prevented", "Rp 125.5M")
        if st.button("Logout"):
            st.session_state['authenticated'] = False
            st.rerun()

# --- FOOTER ---
st.divider()
st.markdown(f'<div style="text-align:center; color:#8892b0; font-size:12px;">🛡️ V-Guard AI | @copyright {datetime.now().year} | Erwin Sinaga</div>', unsafe_allow_html=True)
