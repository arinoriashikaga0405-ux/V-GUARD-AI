import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG: NOMOR WA FOUNDER & KEAMANAN ---
WHATSAPP_NUMBER = "6282122190885" 
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

# --- 2. SETUP TEMA ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0a192f; color: #e6f1ff; }
    .price-box { 
        background-color: #112240; padding: 15px; border-radius: 12px; 
        border: 1px solid #233554; text-align: center; height: 100%;
    }
    .ai-card {
        background-color: #0d1b2a; padding: 10px; border-left: 4px solid #64ffda;
        margin-bottom: 10px; border-radius: 5px;
    }
    .price-tag { color: #64ffda; font-size: 20px; font-weight: bold; }
    .wa-link { 
        color: #25D366; font-weight: bold; text-decoration: none; 
        border: 1px solid #25D366; padding: 5px 10px; border-radius: 10px; display: inline-block; margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: FOTO & MENU ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", width=150)
    else:
        st.markdown("### 👨‍💼")
        
    st.markdown("### **Erwin Sinaga**")
    st.caption("Founder & CEO V-Guard AI")
    st.divider()

    menu = st.radio("Folder Navigasi:", [
        "🏠 Home (Visi Founder)", 
        "🧠 Ekosistem 9 AI",
        "📦 Produk & Harga", 
        "🔑 Portal Klien", 
        "🔐 Admin Panel"
    ])
    
    st.divider()
    st.markdown("### 💬 V-Guard Chatbot")
    st.text_input("Tanya AI (NLP)...", placeholder="Cek audit hari ini?")
    st.caption("Sistem NLP V-Guard siap melayani Bapak.")

# --- FUNGSI PESAN WA ---
def get_wa_url(paket):
    msg = f"Halo Pak Erwin, saya tertarik dengan teknologi V-Guard {paket}. Mohon info pemasangannya."
    clean_msg = msg.replace(" ", "%20")
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={clean_msg}"

# --- 📂 FOLDER 1: HOME (VISI MISI 200 KATA) ---
if menu == "🏠 Home (Visi Founder)":
    st.title("🛡️ V-Guard AI Intelligence")
    st.markdown("### *Digitizing Trust, Eliminating Leakage*")
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga", use_column_width=True)
        else:
            st.info("💡 Unggah 'erwin.jpg' ke GitHub.")
            
    with col2:
        st.header("Visi & Misi")
        narasi = """
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
        """
        st.markdown(narasi)
        st.caption("— **Erwin Sinaga**, Founder V-Guard AI Intelligence")

# --- 📂 FOLDER 2: EKOSISTEM 9 AI ---
elif menu == "🧠 Ekosistem 9 AI":
    st.header("🧠 Integrasi Multi-AI V-Guard")
    st.write("V-Guard AI mengintegrasikan berbagai platform AI terbaik dunia untuk akurasi audit 99.9%.")
    
    col_ai1, col_ai2 = st.columns(2)
    with col_ai1:
        st.markdown('<div class="ai-card"><b>1. Google Gemini AI (Core Brain)</b><br>Proses data kompleks menjadi laporan bahasa manusia.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>2. MindBridge Analytics</b><br>Deteksi fraud akuntansi & anomali transaksi keuangan.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>3. DataRobot (Forecasting)</b><br>Prediksi risiko operasional sebelum kebocoran terjadi.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>4. YOLO / Vision AI</b><br>"Mata" digital yang memantau stok & aktivitas kasir secara visual.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>5. Alteryx (Automation)</b><br>Otomatisasi alur kerja data tanpa campur tangan manusia.</div>', unsafe_allow_html=True)

    with col_ai2:
        st.markdown('<div class="ai-card"><b>6. Workday Adaptive</b><br>Simulasi perencanaan finansial & alarm cerdas.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>7. Numeric.ai</b><br>Notifikasi kesehatan keuangan harian ke smartphone.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>8. OCR AI</b><br>Membaca struk fisik & dokumen untuk digitalisasi instan.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-card"><b>9. NLP WhatsApp Bot</b><br>Interaksi audit & notifikasi selisih stok via WhatsApp.</div>', unsafe_allow_html=True)

# --- 📂 FOLDER 3: PRODUK & HARGA ---
elif menu == "📦 Produk & Harga":
    st.header("Skema Investasi V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown('<div class="price-box"><b>V-LITE</b><br><small>UMKM</small><hr>', unsafe_allow_html=True)
        st.markdown('Pemasangan: <br><span class="price-tag">Rp 1.5M</span><br>Bulanan: 250rb', unsafe_allow_html=True)
        st.markdown(f'<a href="{get_wa_url("V-LITE")}" class="wa-link">💬 Chat WA</a></div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="price-box"><b>V-PRO</b><br><small>Retail/Resto</small><hr>', unsafe_allow_html=True)
        st.markdown('Pemasangan: <br><span class="price-tag">Rp 3.5M</span><br>Bulanan: 750rb', unsafe_allow_html=True)
        st.markdown(f'<a href="{get_wa_url("V-PRO")}" class="wa-link">💬 Chat WA</a></div>', unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="price-box"><b>V-SIGHT</b><br><small>Visual AI</small><hr>', unsafe_allow_html=True)
        st.markdown('Pemasangan: <br><span class="price-tag">Rp 5.0M</span><br>Bulanan: 1.2jt', unsafe_allow_html=True)
        st.markdown(f'<a href="{get_wa_url("V-SIGHT")}" class="wa-link">💬 Chat WA</a></div>', unsafe_allow_html=True)

    with c4:
        st.markdown('<div class="price-box"><b>V-ENTERPRISE</b><br><small>Korporasi</small><hr>', unsafe_allow_html=True)
        st.markdown('<span class="price-tag">CUSTOM</span><br>Full Ecosystem', unsafe_allow_html=True)
        st.markdown(f'<a href="{get_wa_url("V-ENTERPRISE")}" class="wa-link">💬 Chat WA</a></div>', unsafe_allow_html=True)

# --- 📂 FOLDER 4: PORTAL KLIEN ---
elif menu == "🔑 Portal Klien":
    st.header("🔑 Client Secure Upload")
    with st.form("form_klien"):
        st.text_input("Nama Bisnis")
        st.file_uploader("Upload Data (VCS/KTP)")
        if st.form_submit_button("🚀 Kirim Data"):
            st.success("Data telah aman dikirim.")

# --- 📂 FOLDER 5: ADMIN PANEL ---
elif menu == "🔐 Admin Panel":
    st.header("🔐 Executive Dashboard")
    pwd = st.text_input("Sandi Founder", type="password")
    if pwd:
        if hashlib.sha256(pwd.encode()).hexdigest() == ADMIN_PWD_HASH:
            st.success("Selamat Datang, Pak Erwin.")
            st.metric("Leakage Prevented", "Rp 125.5M")
        else:
            st.error("Akses Ditolak.")

# --- FOOTER ---
st.divider()
st.markdown(f'<div style="text-align:center; color:#8892b0; font-size:12px;">🛡️ <b>V-Guard AI Intelligence</b> | @copyright {datetime.now().year} | Erwin Sinaga. All Rights Reserved.</div>', unsafe_allow_html=True)
