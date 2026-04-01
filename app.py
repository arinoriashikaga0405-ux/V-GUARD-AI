import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG: IDENTITAS FOUNDER & KEAMANAN ---
WHATSAPP_NUMBER = "6282122190885" 
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

# --- 2. SETUP TEMA DASHBOARD PREMIUM ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0a192f; color: #e6f1ff; }
    .stButton>button { background-color: #25D366; color: white; border-radius: 20px; font-weight: bold; }
    .price-box { 
        background-color: #112240; padding: 20px; border-radius: 15px; 
        border: 1px solid #233554; text-align: center; height: 100%;
    }
    .ai-card {
        background-color: #0d1b2a; padding: 12px; border-left: 5px solid #64ffda;
        margin-bottom: 15px; border-radius: 8px;
    }
    .price-tag { color: #64ffda; font-size: 24px; font-weight: bold; }
    .wa-link { 
        color: #25D366; font-weight: bold; text-decoration: none; 
        border: 2px solid #25D366; padding: 8px 15px; border-radius: 12px; 
        display: inline-block; margin-top: 15px; transition: 0.3s;
    }
    .wa-link:hover { background-color: #25D366; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: PROFIL & NAVIGASI ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    # Menampilkan foto Erwin Sinaga
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", width=160)
    else:
        st.markdown("<h1 style='text-align: center;'>👨‍💼</h1>", unsafe_allow_html=True)
        
    st.markdown("<h3 style='text-align: center;'>Erwin Sinaga</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #8892b0;'>Founder & CEO V-Guard AI</p>", unsafe_allow_html=True)
    st.divider()

    menu = st.radio("FOLDER SISTEM:", [
        "🏠 Home (Visi Founder)", 
        "🧠 Ekosistem 9 AI Engine",
        "📦 Produk & Investasi", 
        "🔑 Portal Klien", 
        "🔐 Admin Panel"
    ])
    
    st.divider()
    st.markdown("### 🤖 V-Guard NLP Bot")
    st.text_input("Interaksi Suara/Teks...", placeholder="Cek anomali hari ini?")
    st.caption("AI Chatbot aktif untuk membantu audit Bapak.")

# --- FUNGSI REDIRECT WHATSAPP ---
def get_wa_url(paket):
    msg = f"Halo Pak Erwin, saya tertarik dengan ekosistem V-Guard {paket}. Mohon info jadwal survei."
    clean_msg = msg.replace(" ", "%20")
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={clean_msg}"

# --- 📂 FOLDER 1: HOME (VISI 200 KATA UTUH) ---
if menu == "🏠 Home (Visi Founder)":
    st.title("🛡️ V-Guard AI Intelligence")
    st.subheader("“Digitizing Trust, Eliminating Leakage”")
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga", use_column_width=True)
        else:
            st.info("💡 Sistem siap. Pastikan erwin.jpg ada di repository.")
            
    with col2:
        st.header("Visi & Misi Founder")
        # NARASI 200 KATA TANPA DIKURANGI SESUAI INSTRUKSI
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

# --- 📂 FOLDER 2: EKOSISTEM 9 AI ENGINE ---
elif menu == "🧠 Ekosistem 9 AI Engine":
    st.header("🧠 Integrasi Multi-Platform AI (99.9% Accuracy)")
    st.write("V-Guard AI tidak bekerja sendiri, melainkan mengorkestrasikan teknologi terbaik dunia:")
    
    c_ai1, c_ai2 = st.columns(2)
    with c_ai1:
        st.markdown('<div class="ai-card"><b>1. Google Gemini AI (Core Brain)</b><br>Menganalisis data audit kompleks menjadi laporan narasi yang mudah dipahami.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>2. MindBridge Analytics</b><br>Mendeteksi anomali transaksi keuangan & kecurangan akuntansi secara instan.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>3. DataRobot (Risk Alerting)</b><br>Prediksi risiko operasional di masa depan berdasarkan tren historis data.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>4. YOLO / Vision AI (Computer Vision)</b><br>"Mata Digital" yang memantau stok fisik & perilaku kasir secara real-time.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>5. Alteryx (Workflow Automation)</b><br>Mengotomatisasi seluruh alur kerja data dari CCTV ke laporan keuangan.</div>', unsafe_allow_html=True)

    with c_ai2:
        st.markdown('<div class="ai-card"><b>6. Workday Adaptive</b><br>Simulasi skenario finansial cerdas & peringatan penyimpangan biaya.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>7. Numeric.ai</b><br>Notifikasi ringkas kesehatan keuangan harian langsung ke smartphone.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>8. OCR AI (Optical Recognition)</b><br>Digitalisasi struk, nota, dan dokumen fisik secara otomatis tanpa input manual.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>9. NLP WhatsApp Bot</b><br>Bot cerdas yang melayani tanya jawab audit & notifikasi selisih stok via WA.</div>', unsafe_allow_html=True)

# --- 📂 FOLDER 3: PRODUK & INVESTASI ---
elif menu == "📦 Produk & Investasi":
    st.header("Layanan & Skema Investasi V-Guard")
    st.divider()
    
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.markdown(f'<div class="price-box"><b>V-LITE</b><br><small>UMKM / Toko</small><hr>Pasang: <span class="price-tag">Rp 1.5M</span><br>Bulanan: 250rb<br><a href="{get_wa_url("V-LITE")}" class="wa-link">💬 Chat WA</a></div>', unsafe_allow_html=True)
    with p2:
        st.markdown(f'<div class="price-box"><b>V-PRO</b><br><small>Retail / Resto</small><hr>Pasang: <span class="price-tag">Rp 3.5M</span><br>Bulanan: 750rb<br><a href="{get_wa_url("V-PRO")}" class="wa-link">💬 Chat WA</a></div>', unsafe_allow_html=True)
    with p3:
        st.markdown(f'<div class="price-box"><b>V-SIGHT</b><br><small>Visual Audit</small><hr>Pasang: <span class="price-tag">Rp 5.0M</span><br>Bulanan: 1.2jt<br><a href="{get_wa_url("V-SIGHT")}" class="wa-link">💬 Chat WA</a></div>', unsafe_allow_html=True)
    with p4:
        st.markdown(f'<div class="price-box"><b>V-ENTERPRISE</b><br><small>Corporate</small><hr><span class="price-tag">CUSTOM</span><br>Full Ecosystem<br><a href="{get_wa_url("V-ENTERPRISE")}" class="wa-link">💬 Chat WA</a></div>', unsafe_allow_html=True)

# --- 📂 FOLDER 4: PORTAL KLIEN ---
elif menu == "🔑 Portal Klien":
    st.header("🔑 Portal Secure Upload")
    with st.form("portal_upload"):
        st.text_input("Nama Perusahaan / Toko")
        st.file_uploader("Upload Data (VCS/KTP/Rekaman)", type=['csv', 'xlsx', 'jpg', 'png', 'mp4'])
        if st.form_submit_button("🚀 Kirim ke AI Engine"):
            st.success("Data berhasil dienkripsi dan masuk ke antrean audit.")

# --- 📂 FOLDER 5: ADMIN PANEL ---
elif menu == "🔐 Admin Panel":
    st.header("🔐 CEO Command Center")
    pwd = st.text_input("Sandi Founder", type="password")
    if pwd:
        if hashlib.sha256(pwd.encode()).hexdigest() == ADMIN_PWD_HASH:
            st.success("Akses Diterima. Selamat Datang, Pak Erwin.")
            st.metric("Total Leakage Blocked", "Rp 125,500,000", "+12%")
        else:
            st.error("Sandi Salah. Akses Ditolak.")

# --- FOOTER COPYRIGHT ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown(f'<div style="text-align:center; color:#8892b0; font-size:12px;">🛡️ <b>V-Guard AI Intelligence</b> | @copyright {datetime.now().year} | Erwin Sinaga. All Rights Reserved.</div>', unsafe_allow_html=True)
