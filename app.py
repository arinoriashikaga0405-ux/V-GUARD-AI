import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# CSS UNTUK TAMPILAN PREMIUM & SEJAJAR
st.markdown("""
<style>
    .main-header { font-size: 28px; font-weight: bold; color: #1f1f1f; margin-bottom: 20px; }
    .vision-mission-card {
        background: white; border-radius: 12px; padding: 20px;
        border-top: 5px solid #ff4b4b; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        height: 280px; display: flex; flex-direction: column;
    }
    .roi-section {
        background: #fff5f5; border: 2px solid #ff4b4b; padding: 25px;
        border-radius: 15px; margin-top: 30px; text-align: center;
    }
    .price-card {
        background: white; border-radius: 12px; border: 1px solid #eee;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); height: 520px;
        display: flex; flex-direction: column; justify-content: space-between;
        transition: 0.3s;
    }
    .price-card:hover { border-color: #ff4b4b; transform: translateY(-5px); }
    .card-header {
        background: linear-gradient(135deg, #ff4b4b 0%, #a51d1d 100%);
        color: white; padding: 15px; text-align: center; font-weight: bold;
        border-radius: 12px 12px 0 0; font-size: 16px;
    }
    .card-body { padding: 15px; flex-grow: 1; font-size: 13px; color: #444; }
    .tech-item {
        background: #f9f9f9; padding: 12px; border-radius: 8px;
        border-left: 4px solid #ff4b4b; margin-bottom: 10px; font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 2. SIDEBAR (NAVIGASI)
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    st.write("---")
    menu = st.radio("Pilih Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Layanan", 
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
        Bapak Erwin Sinaga memiliki rekam jejak profesional yang solid dengan pengalaman lebih dari 10 tahun di industri perbankan nasional. 
        Beliau mengintegrasikan standar keamanan perbankan tingkat tinggi ke dalam V-Guard AI Systems untuk menjamin keberlangsungan aset klien melalui transparansi dan akurasi AI.
        """)

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.markdown('<div class="main-header">🎯 Strategi & Analisis Risiko</div>', unsafe_allow_html=True)
    cv, cm = st.columns(2)
    with cv:
        st.markdown("""<div class="vision-mission-card"><h3 style="color:#ff4b4b;">🎯 Visi</h3>
        <p>Menjadi pemimpin pasar dalam solusi keamanan audit berbasis AI di Indonesia pada tahun 2026.</p></div>""", unsafe_allow_html=True)
    with cm:
        st.markdown("""<div class="vision-mission-card"><h3 style="color:#ff4b4b;">🚀 Misi</h3>
        <ul style="padding-left:20px;">
            <li>Integrasi AI tercanggih untuk deteksi fraud.</li>
            <li>Laporan audit transparan bagi investor.</li>
            <li>Otomasi pengawasan aset 24/7.</li>
        </ul></div>""", unsafe_allow_html=True)
    
    st.markdown('<div class="roi-section">', unsafe_allow_html=True)
    st.subheader("📈 Kalkulator Penyelamatan Aset (ROI)")
    omzet = st.number_input("Omzet Bisnis Bulanan (Rp):", value=500000000, step=10000000)
    st.markdown(f"""<h2 style="color:#ff4b4b;">Potensi Kerugian: Rp {omzet * 0.05:,.0f} / Bulan</h2>
    <p style="color:#666;">(Berdasarkan rata-rata kebocoran operasional global 5%)</p></div>""", unsafe_allow_html=True)

# --- MENU 3: PAKET LAYANAN (SEJAJAR & RAPI) ---
elif menu == "3. 📦 Paket Layanan":
    st.markdown('<div class="main-header">📦 Paket Solusi Keamanan</div>', unsafe_allow_html=True)
    
    def draw_pkg(title, setup, monthly, features, key):
        f_list = "".join([f'<div style="margin-bottom:8px;">✅ {f}</div>' for f in features])
        st.markdown(f"""<div class="price-card">
            <div class="card-header">{title}</div>
            <div class="card-body">
                <h4 style="margin-bottom:5px;">Setup: Rp {setup}</h4>
                <p style="color:#ff4b4b; font-weight:bold;">Rp {monthly}/Bln</p>
                <hr>{f_list}
            </div>
        </div>""", unsafe_allow_html=True)
        st.link_button(f"Pilih {title}", wa_url, use_container_width=True, key=key)

    # Grid 4 Kolom Sejajar
    p1, p2, p3, p4 = st.columns(4)
    with p1: draw_pkg("BASIC (MIKRO)", "2.5jt", "500rb", ["Gemini AI Core", "Audit Harian", "Laporan Mingguan"], "k1")
    with p2: draw_pkg("MEDIUM (SME)", "7.5jt", "1.5jt", ["MindBridge Fraud", "Alarm System", "Auto Invoice"], "k2")
    with p3: draw_pkg("ENTERPRISE", "25jt", "5jt", ["YOLO CCTV AI", "DataRobot Risk", "Forecasting Bisnis"], "k3")
    with p4: draw_pkg("CORPORATE", "50jt", "10jt", ["Full Automation", "Custom AI Training", "Dedicated Manager"], "k4")

# --- MENU 4: ADMIN PANEL (INTEGRASI AI) ---
elif menu == "4. 🔐 Admin Panel (AI Center)":
    st.title("🔐 V-Guard Intelligence Center")
    t1, t2 = st.tabs(["⚙️ Sistem AI", "📊 Input Data"])
    with t1:
        techs = [
            ("🧠 Google Gemini AI", "Memproses data audit kompleks menjadi laporan bahasa manusia."),
            ("🔍 MindBridge Analytics", "Deteksi pola kecurangan akuntansi dan anomali transaksi."),
            ("📈 DataRobot", "Prediksi risiko operasional untuk mencegah kebocoran."),
            ("⚙️ Alteryx", "Otomasi data CCTV dan POS tanpa campur tangan manusia."),
            ("⏰ Workday Adaptive", "Alarm cerdas jika biaya operasional menyimpang."),
            ("📱 Numeric.ai", "Notifikasi kesehatan keuangan harian ke smartphone."),
            ("📹 YOLO / Vision AI", "Mata digital memantau stok dan kasir secara visual."),
            ("🤖 OCR & WhatsApp Bot", "Baca nota otomatis dan kirim notifikasi via WhatsApp.")
        ]
        for title, desc in techs:
            st.markdown(f'<div class="tech-item"><b>{title}:</b> {desc}</div>', unsafe_allow_html=True)
    with t2:
        st.subheader("📥 Unggah Data Klien")
        st.file_uploader("Upload File (CSV, JPG, MP4)", type=['csv','xlsx','jpg','png','mp4'])
        st.error("🚨 ALARM FRAUD: Deteksi anomali pada Cabang Tangerang.")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Strategically Led by Erwin Sinaga")
