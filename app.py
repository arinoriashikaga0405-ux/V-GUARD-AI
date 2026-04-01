import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG: IDENTITAS & KEAMANAN ---
WHATSAPP_NUMBER = "6282122190885" 
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

# Cek Status Login untuk menyembunyikan Ekosistem
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- 2. SETUP TEMA DASHBOARD ---
st.set_page_config(page_title="V-Guard AI | Founder Dashboard", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0a192f; color: #e6f1ff; }
    .price-box { 
        background-color: #112240; padding: 20px; border-radius: 15px; 
        border: 1px solid #233554; text-align: center; height: 100%;
    }
    .ai-card {
        background-color: #0d1b2a; padding: 12px; border-left: 5px solid #64ffda;
        margin-bottom: 15px; border-radius: 8px;
    }
    .price-tag { color: #64ffda; font-size: 22px; font-weight: bold; }
    .wa-link { 
        color: #25D366; font-weight: bold; text-decoration: none; 
        border: 2px solid #25D366; padding: 8px 15px; border-radius: 12px; 
        display: inline-block; margin-top: 15px;
    }
    /* Memperbaiki jarak antar elemen di sidebar */
    [data-testid="stSidebarNav"] { padding-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: LAYOUT RAPI ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Foto & Nama Sejajar Sejajar (Rapi)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", width=220)
    
    st.markdown("<h2 style='text-align: center; margin-top: -10px; color: white;'>Erwin Sinaga</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #8892b0; font-size: 14px;'>Founder & CEO V-Guard AI</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 0.5px solid #233554; margin: 20px 0;'>", unsafe_allow_html=True)

    # Navigasi Folder
    list_menu = ["🏠 Home", "📦 Produk & Investasi", "🔑 Portal Klien", "🔐 Admin Panel"]
    
    # Ekosistem 9 AI hanya muncul jika sudah login admin
    if st.session_state['logged_in']:
        list_menu.insert(1, "🧠 Ekosistem 9 AI Engine")

    menu = st.radio("FOLDER SISTEM:", list_menu)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.divider()
    
    # Relokasi Chatbot ke bagian paling bawah agar tidak mengganggu navigasi
    st.markdown("### 🤖 V-Guard NLP")
    st.text_input("Interaksi Teks...", placeholder="Cek audit...")
    st.caption("AI Chatbot aktif di latar belakang.")

# --- FUNGSI WHATSAPP ---
def get_wa_url(paket):
    msg = f"Halo Pak Erwin, saya tertarik dengan V-Guard {paket}. Mohon info lanjut."
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={msg.replace(' ', '%20')}"

# --- 📂 FOLDER 1: HOME ---
if menu == "🏠 Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.subheader("“Digitizing Trust, Eliminating Leakage”")
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
        st.caption("— **Erwin Sinaga**, Founder V-Guard AI Intelligence")

# --- 📂 FOLDER 2: EKOSISTEM (HIDDEN/PROTECTED) ---
elif menu == "🧠 Ekosistem 9 AI Engine":
    st.header("🧠 Engine Integrasi (Confidential)")
    st.info("Halaman ini bersifat rahasia dan hanya dapat diakses oleh Founder.")
    
    c_ai1, c_ai2 = st.columns(2)
    with c_ai1:
        st.markdown('<div class="ai-card"><b>1. Google Gemini AI</b><br>Core Analisis data audit.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>2. MindBridge</b><br>Deteksi anomali finansial.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>3. DataRobot</b><br>Forecasting risiko kebocoran.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>4. YOLO / Vision AI</b><br>Monitoring visual stok & kasir.</div>', unsafe_allow_html=True)
    with c_ai2:
        st.markdown('<div class="ai-card"><b>5. Alteryx</b><br>Workflow automation.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>6. Workday Adaptive</b><br>Scenario-based alarms.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>7. Numeric.ai</b><br>Financial notifications.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>8. OCR & NLP Bot</b><br>Digitalisasi struk & WhatsApp interaction.</div>', unsafe_allow_html=True)

# --- 📂 FOLDER 3: PRODUK ---
elif menu == "📦 Produk & Investasi":
    st.header("Layanan & Skema Investasi")
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.markdown(f'<div class="price-box"><b>V-LITE</b><br><small>UMKM</small><hr>Pasang: <br><span class="price-tag">Rp 1.5M</span><br>Bulanan: 250rb<br><a href="{get_wa_url("V-LITE")}" class="wa-link">💬 Chat WA</a></div>', unsafe_allow_html=True)
    with p2:
        st.markdown(f'<div class="price-box"><b>V-PRO</b><br><small>Retail/Resto</small><hr>Pasang: <br><span class="price-tag">Rp 3.5M</span><br>Bulanan: 750rb<br><a href="{get_wa_url("V-PRO")}" class="wa-link">💬 Chat WA</a></div>', unsafe_allow_html=True)
    with p3:
        st.markdown(f'<div class="price-box"><b>V-SIGHT</b><br><small>Visual</small><hr>Pasang: <br><span class="price-tag">Rp 5.0M</span><br>Bulanan: 1.2jt<br><a href="{get_wa_url("V-SIGHT")}" class="wa-link">💬 Chat WA</a></div>', unsafe_allow_html=True)
    with p4:
        st.markdown(f'<div class="price-box"><b>V-ENTERPRISE</b><br><small>Corporate</small><hr><span class="price-tag">CUSTOM</span><br>Full Ecosystem<br><a href="{get_wa_url("V-ENTERPRISE")}" class="wa-link">💬 Chat WA</a></div>', unsafe_allow_html=True)

# --- 📂 FOLDER 4: PORTAL KLIEN ---
elif menu == "🔑 Portal Klien":
    st.header("🔑 Client Upload Center")
    with st.form("u_form"):
        st.text_input("Nama Bisnis")
        st.file_uploader("Data Audit")
        if st.form_submit_button("🚀 Proses AI"):
            st.success("Data masuk antrean audit.")

# --- 📂 FOLDER 5: ADMIN PANEL ---
elif menu == "🔐 Admin Panel":
    st.header("🔐 CEO Command Center")
    if not st.session_state['logged_in']:
        pwd = st.text_input("Sandi Founder", type="password")
        if st.button("Login"):
            if hashlib.sha256(pwd.encode()).hexdigest() == ADMIN_PWD_HASH:
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Akses Ditolak.")
    else:
        st.success("Mode Admin Aktif. Menu 'Ekosistem' kini muncul di navigasi.")
        st.metric("Total Leakage Blocked", "Rp 125,500,000")
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown(f'<div style="text-align:center; color:#8892b0; font-size:12px;">🛡️ <b>V-Guard AI Intelligence</b> | @copyright {datetime.now().year} | Erwin Sinaga. All Rights Reserved.</div>', unsafe_allow_html=True)
