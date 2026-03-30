import streamlit as st
import os
import pandas as pd

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# CSS UNTUK UKURAN KARTU DAN ROI YANG SERAGAM
st.markdown("""
<style>
    .reportview-container { background: #f5f7f9; }
    .price-card {
        background: white; border-radius: 12px; border: 1px solid #eee;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); height: 480px;
        display: flex; flex-direction: column; overflow: hidden; margin-bottom: 20px;
    }
    .card-header {
        background: linear-gradient(135deg, #ff4b4b 0%, #a51d1d 100%);
        color: white; padding: 12px; text-align: center; font-weight: bold; font-size: 16px;
    }
    .card-body { padding: 15px; flex-grow: 1; }
    .feature-list { font-size: 12px; color: #444; margin-bottom: 5px; }
    .roi-container {
        background: #fff5f5; border: 2px solid #ff4b4b; padding: 25px;
        border-radius: 15px; text-align: center; margin-bottom: 30px;
    }
    .tech-pill {
        background: #fdfdfd; border: 1px solid #ddd; padding: 10px;
        border-radius: 8px; border-left: 4px solid #ff4b4b; margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 2. SIDEBAR DENGAN FOTO FOUNDER NOMOR 1
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.write("---")
    menu = st.radio("Navigasi:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi & Misi", 
        "3. 📦 4 Paket & ROI", 
        "4. 🔐 Admin Panel (AI Center)"
    ])
    st.caption("© 2026 V-Guard AI Systems")

# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with r:
        st.subheader("Erwin Sinaga")
        st.write("""
        Bapak Erwin Sinaga memiliki rekam jejak profesional yang sangat solid dengan dedikasi lebih dari 10 tahun di industri perbankan dan manajemen aset nasional. Selama satu dekade tersebut, beliau telah mendalami berbagai dinamika operasional perbankan, mulai dari manajemen risiko kredit hingga pengawasan integritas transaksi finansial yang kompleks. Pengalaman luas beliau dalam menghadapi ancaman kebocoran dana dan manipulasi data di sektor keuangan formal menjadi alasan utama lahirnya V-Guard AI Systems. 
        
        Melalui pemahaman mendalam mengenai pola-pola fraud yang sering luput dari audit konvensional, Bapak Erwin mengintegrasikan standar keamanan perbankan tingkat tinggi ke dalam ekosistem digital. Beliau berfokus pada transparansi, akurasi, dan penyediaan proteksi finansial yang setara dengan sistem pertahanan bank global untuk menjamin keberlangsungan aset klien.
        """)

# --- MENU 2: VISI & MISI ---
elif menu == "2. 🎯 Visi & Misi":
    st.title("🎯 Visi & Misi Perusahaan")
    c1, c2 = st.columns(2)
    with c1:
        st.info("### 🎯 Visi\nMenjadi pemimpin pasar dalam solusi keamanan audit berbasis AI di Indonesia, memastikan integritas finansial bisnis klien terjaga secara mutlak pada tahun 2026.")
    with c2:
        st.success("### 🚀 Misi\n1. Mengintegrasikan teknologi AI tercanggih untuk deteksi fraud.\n2. Memberikan laporan audit transparan bagi investor.\n3. Mengotomatisasi sistem pengawasan aset 24/7.")

# --- MENU 3: 4 PAKET & ROI ---
elif menu == "3. 📦 4 Paket & ROI":
    st.title("📊 Analisis Potensi Kerugian & Solusi")
    
    # ROI SECTION
    st.subheader("📈 Kalkulator Penyelamatan Aset")
    omzet = st.number_input("Input Omzet Bisnis Bulanan (Rp):", value=500000000, step=10000000)
    kerugian = omzet * 0.05
    st.markdown(f"""<div class="roi-container">
        <h4 style="color:#a51d1d;">🚨 Estimasi Potensi Kerugian Tanpa AI:</h4>
        <h1 style="color:#ff4b4b; margin:0;">Rp {kerugian:,.0f} / Bulan</h1>
        <p style="font-size:14px; color:#666;">(Berdasarkan rata-rata kebocoran operasional global sebesar 5%)</p>
    </div>""", unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("📦 Pilih Paket Layanan")
    
    # 4 PAKET LAYANAN
    def draw_card(title, setup, monthly, features, key):
        f_html = "".join([f'<div class="feature-list">✅ {f}</div>' for f in features])
        st.markdown(f"""<div class="price-card"><div class="card-header">{title}</div>
        <div class="card-body"><h4>Setup: Rp {setup}</h4><p style="color:#ff4b4b; font-weight:bold;">Rp {monthly} / Bln</p><hr>{f_html}</div></div>""", unsafe_allow_html=True)
        st.link_button(f"Pesan {title}", wa_url, use_container_width=True, key=key)

    p1, p2, p3, p4 = st.columns(4)
    with p1: draw_card("Basic (MIKRO)", "2.5jt", "500rb", ["Gemini AI Core", "Audit Transaksi", "Email Report"], "m1")
    with p2: draw_card("Medium (SME)", "7.5jt", "1.5jt", ["MindBridge Fraud", "Alarm System", "Auto Invoice Pro"], "m2")
    with p3: draw_card("Enterprise", "25jt", "5jt", ["YOLO CCTV AI", "DataRobot Risk", "Priority Support"], "m3")
    with p4: draw_card("Corporate", "50jt", "10jt", ["Custom AI Training", "Full Automation", "Dedicated Manager"], "m4")

# --- MENU 4: ADMIN PANEL DENGAN EKOSISTEM AI ---
elif menu == "4. 🔐 Admin Panel (AI Center)":
    st.title("🔐 Control Center: Integrated Ecosystem")
    
    tab1, tab2, tab3 = st.tabs(["📂 Upload & Audit", "📡 Real-time Monitoring", "💬 AI Support Center"])
    
    with tab1:
        st.subheader("📥 Input Data Klien")
        st.file_uploader("Upload Laporan Transaksi/CCTV Feed (CSV, JPG, MP4)", type=['csv','xlsx','jpg','png','mp4'])
        st.write("---")
        st.subheader("🛠️ Teknologi Audit Aktif:")
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.markdown('<div class="tech-pill"><b>🧠 Google Gemini AI:</b> Analis utama laporan kompleks ke bahasa manusia.</div>', unsafe_allow_html=True)
            st.markdown('<div class="tech-pill"><b>🔍 MindBridge:</b> Deteksi pola kecurangan akuntansi secara instan.</div>', unsafe_allow_html=True)
            st.markdown('<div class="tech-pill"><b>📈 DataRobot:</b> Prediksi risiko masa depan untuk cegah kebocoran.</div>', unsafe_allow_html=True)
            st.markdown('<div class="tech-pill"><b>🤖 OCR AI:</b> Membaca struk fisik dan nota secara otomatis.</div>', unsafe_allow_html=True)
        with col_t2:
            st.markdown('<div class="tech-pill"><b>⚙️ Alteryx:</b> Otomasi alur kerja data CCTV & POS tanpa manusia.</div>', unsafe_allow_html=True)
            st.markdown('<div class="tech-pill"><b>⏰ Workday Adaptive:</b> Alarm cerdas jika biaya operasional menyimpang.</div>', unsafe_allow_html=True)
            st.markdown('<div class="tech-pill"><b>📱 Numeric.ai:</b> Notifikasi kesehatan keuangan harian ke Smartphone.</div>', unsafe_allow_html=True)
            st.markdown('<div class="tech-pill"><b>📲 WhatsApp Bot:</b> Pengiriman notifikasi otomatis via NLP.</div>', unsafe_allow_html=True)

    with tab2:
        st.error("🚨 ALARM FRAUD: Terdeteksi selisih stok di Cabang A pukul 19:30")
        st.info("📹 LIVE FEED: YOLO AI sedang memantau area kasir...")
        st.image("https://images.unsplash.com/photo-1557597774-9d2739f85a76?q=80&w=500", width=400)

    with tab3:
        st.subheader("💬 V-Guard Chat Box")
        st.write("AI: *Selamat malam Pak Erwin, hasil audit MindBridge menunjukkan efisiensi naik 12%.*")
        st.text_input("Tanya V-Guard AI...")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Strategically Led by Erwin Sinaga")
