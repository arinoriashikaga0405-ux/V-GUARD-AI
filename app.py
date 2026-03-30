import streamlit as st
import os
import pandas as pd

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# CSS UNTUK ESTETIKA & PENYAJIAN SEJAJAR
st.markdown("""
<style>
    .main-header { font-size: 28px; font-weight: bold; color: #1f1f1f; margin-bottom: 20px; }
    .vision-mission-card {
        background: white; border-radius: 12px; padding: 20px;
        border-top: 5px solid #ff4b4b; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        height: 250px;
    }
    .roi-section {
        background: #fff5f5; border: 2px solid #ff4b4b; padding: 20px;
        border-radius: 15px; margin-top: 30px; text-align: center;
    }
    .price-card {
        background: white; border-radius: 12px; border: 1px solid #eee;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); height: 460px;
        display: flex; flex-direction: column; transition: 0.3s;
    }
    .price-card:hover { transform: translateY(-5px); }
    .card-header {
        background: linear-gradient(135deg, #ff4b4b 0%, #a51d1d 100%);
        color: white; padding: 12px; text-align: center; font-weight: bold;
    }
    .card-body { padding: 15px; flex-grow: 1; font-size: 13px; }
    .tech-item {
        background: #f9f9f9; padding: 12px; border-radius: 8px;
        border-left: 4px solid #ff4b4b; margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 2. SIDEBAR (FOTO FOUNDER NOMOR 1)
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.write("---")
    menu = st.radio("Navigasi:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 📦 Paket Layanan", "4. 🔐 Admin Panel (AI Center)"])
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
        Bapak Erwin Sinaga memiliki rekam jejak profesional yang sangat solid dengan dedikasi lebih dari 10 tahun di industri perbankan dan manajemen aset nasional. Beliau telah mendalami berbagai dinamika operasional perbankan, mulai dari manajemen risiko kredit hingga pengawasan integritas transaksi finansial yang kompleks. 
        
        Pengalaman luas beliau dalam menghadapi ancaman kebocoran dana dan manipulasi data di sektor keuangan formal menjadi alasan utama lahirnya V-Guard AI Systems. Bapak Erwin mengintegrasikan standar keamanan perbankan tingkat tinggi ke dalam ekosistem digital untuk menjamin keberlangsungan aset klien melalui transparansi dan akurasi AI.
        """)

# --- MENU 2: VISI, MISI & ROI (SEJAJAR & TERPADU) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.markdown('<div class="main-header">🎯 Arah Strategis & Analisis Risiko</div>', unsafe_allow_html=True)
    
    # Visi & Misi Sejajar
    col_v, col_m = st.columns(2)
    with col_v:
        st.markdown("""<div class="vision-mission-card"><h3 style="color:#ff4b4b;">🎯 Visi</h3>
        <p>Menjadi pemimpin pasar dalam solusi keamanan audit berbasis AI di Indonesia, memastikan integritas finansial bisnis klien terjaga secara mutlak pada tahun 2026.</p></div>""", unsafe_allow_html=True)
    with col_m:
        st.markdown("""<div class="vision-mission-card"><h3 style="color:#ff4b4b;">🚀 Misi</h3>
        <ol><li>Mengintegrasikan teknologi AI tercanggih untuk deteksi fraud.</li><li>Memberikan laporan audit transparan bagi investor.</li><li>Mengotomatisasi sistem pengawasan aset 24/7.</li></ol></div>""", unsafe_allow_html=True)
    
    # ROI Kerugian di bawahnya
    st.markdown('<div class="roi-section">', unsafe_allow_html=True)
    st.subheader("📈 Kalkulator Penyelamatan Aset (ROI)")
    omzet = st.number_input("Input Omzet Bisnis Bulanan (Rp):", value=500000000, step=10000000)
    st.markdown(f"""<h2 style="color:#ff4b4b; margin:10px 0;">Potensi Kerugian: Rp {omzet * 0.05:,.0f} / Bulan</h2>
    <p style="color:#666;">(Estimasi kebocoran fraud & operasional 5%)</p></div>""", unsafe_allow_html=True)

# --- MENU 3: 4 PAKET LAYANAN (RAPI) ---
elif menu == "3. 📦 Paket Layanan":
    st.markdown('<div class="main-header">📦 Paket Solusi Keamanan</div>', unsafe_allow_html=True)
    
    def draw_pkg(title, setup, monthly, features, key):
        f_list = "".join([f'<div style="margin-bottom:5px;">✅ {f}</div>' for f in features])
        st.markdown(f"""<div class="price-card"><div class="card-header">{title}</div>
        <div class="card-body"><b>Setup: Rp {setup}</b><br><span style="color:#ff4b4b; font-weight:bold;">Rp {monthly}/Bln</span><hr>{f_list}</div></div>""", unsafe_allow_html=True)
        st.link_button(f"Pesan {title}", wa_url, use_container_width=True, key=key)

    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_pkg("BASIC (MIKRO)", "2.5jt", "500rb", ["Gemini AI Core", "Audit Harian", "Email Report"], "k1")
    with c2: draw_pkg("MEDIUM (SME)", "7.5jt", "1.5jt", ["MindBridge Fraud", "Alarm System", "Auto Invoice"], "k2")
    with c3: draw_pkg("ENTERPRISE", "25jt", "5jt", ["YOLO CCTV AI", "DataRobot Risk", "Priority Support"], "k3")
    with p4 if 'p4' in locals() else c4: draw_pkg("CORPORATE", "50jt", "10jt", ["Custom AI Training", "Full Automation", "Dedicated Manager"], "k4")

# --- MENU 4: ADMIN PANEL (INTEGRASI TOTAL AI) ---
elif menu == "4. 🔐 Admin Panel (AI Center)":
    st.title("🔐 V-Guard Intelligence Center")
    
    t1, t2 = st.tabs(["⚙️ Sistem AI Terintegrasi", "📡 Monitoring & Chat"])
    
    with t1:
        st.info("Seluruh ekosistem AI di bawah ini bekerja secara simultan untuk melindungi aset klien.")
        
        tech_data = [
            ("🧠 Google Gemini AI", "Analis utama yang memproses data audit kompleks menjadi laporan bahasa manusia."),
            ("🔍 MindBridge Analytics", "Mendeteksi pola kecurangan akuntansi dan anomali transaksi melalui Audit Alarms."),
            ("📈 DataRobot", "Prediksi risiko operasional masa depan berdasarkan data historis untuk cegah kebocoran."),
            ("⚙️ Alteryx", "Otomasi seluruh alur data dari CCTV dan POS tanpa campur tangan manusia."),
            ("⏰ Workday Adaptive", "Alarm cerdas jika biaya operasional menyimpang dari skenario bisnis aman."),
            ("📱 Numeric.ai", "Notifikasi personal kesehatan keuangan harian langsung ke smartphone."),
            ("📹 YOLO / Vision AI", "Mata digital yang memantau pergerakan stok dan aktivitas kasir secara visual."),
            ("🤖 OCR & NLP Bot", "Membaca nota otomatis dan mengirimkan notifikasi via WhatsApp Bot.")
        ]
        
        for title, desc in tech_data:
            st.markdown(f'<div class="tech-item"><b>{title}:</b> {desc}</div>', unsafe_allow_html=True)

    with t2:
        st.subheader("💬 AI Chat Box & Live Feed")
        st.error("🚨 ALARM: MindBridge mendeteksi anomali di Cabang A pukul 19:35.")
        st.text_input("Tanya V-Guard AI (Contoh: Berapa total efisiensi bulan ini?)")
        st.button("Generate Laporan Gemini AI")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Strategically Led by Erwin Sinaga")
