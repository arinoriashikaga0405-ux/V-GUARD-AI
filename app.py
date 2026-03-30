import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# CSS UNTUK ESTETIKA & PENYAJIAN SEJAJAR
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
        border-radius: 15px; margin-top: 30px; text-align: center; width: 100%;
    }
    .price-card {
        background: white; border-radius: 12px; border: 1px solid #eee;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); height: 500px;
        display: flex; flex-direction: column; transition: 0.3s;
    }
    .price-card:hover { transform: translateY(-5px); }
    .card-header {
        background: linear-gradient(135deg, #ff4b4b 0%, #a51d1d 100%);
        color: white; padding: 12px; text-align: center; font-weight: bold; border-radius: 12px 12px 0 0;
    }
    .card-body { padding: 15px; flex-grow: 1; font-size: 13px; }
    .tech-item {
        background: #f9f9f9; padding: 12px; border-radius: 8px;
        border-left: 4px solid #ff4b4b; margin-bottom: 10px; font-size: 14px;
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
    menu = st.radio("Navigasi Utama:", [
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
        Bapak Erwin Sinaga memiliki rekam jejak profesional yang sangat solid dengan dedikasi lebih dari 10 tahun di industri perbankan dan manajemen aset nasional. Beliau telah mendalami berbagai dinamika operasional perbankan, mulai dari manajemen risiko kredit hingga pengawasan integritas transaksi finansial yang kompleks. 
        
        Pengalaman luas beliau dalam menghadapi ancaman kebocoran dana dan manipulasi data di sektor keuangan formal menjadi alasan utama lahirnya V-Guard AI Systems. Bapak Erwin mengintegrasikan standar keamanan perbankan tingkat tinggi ke dalam ekosistem digital untuk menjamin keberlangsungan aset klien melalui transparansi dan akurasi AI.
        """)

# --- MENU 2: VISI, MISI & ROI (SEJAJAR SEMPURNA) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.markdown('<div class="main-header">🎯 Arah Strategis & Analisis Risiko</div>', unsafe_allow_html=True)
    
    # Visi & Misi Sejajar
    col_v, col_m = st.columns(2)
    with col_v:
        st.markdown("""<div class="vision-mission-card"><h3 style="color:#ff4b4b; margin-top:0;">🎯 Visi</h3>
        <p style="font-size:15px;">Menjadi pemimpin pasar dalam solusi keamanan audit berbasis AI di Indonesia, memastikan integritas finansial bisnis klien terjaga secara mutlak pada tahun 2026.</p></div>""", unsafe_allow_html=True)
    with col_m:
        st.markdown("""<div class="vision-mission-card"><h3 style="color:#ff4b4b; margin-top:0;">🚀 Misi</h3>
        <ul style="font-size:15px; padding-left:20px;">
            <li>Mengintegrasikan teknologi AI tercanggih untuk deteksi fraud.</li>
            <li>Memberikan laporan audit transparan bagi investor.</li>
            <li>Mengotomatisasi sistem pengawasan aset 24/7.</li>
        </ul></div>""", unsafe_allow_html=True)
    
    # ROI Kerugian di bawahnya (Lebar Penuh)
    st.markdown('<div class="roi-section">', unsafe_allow_html=True)
    st.subheader("📈 Kalkulator Penyelamatan Aset (ROI)")
    omzet = st.number_input("Input Omzet Bisnis Bulanan (Rp):", value=500000000, step=10000000)
    kerugian_val = omzet * 0.05
    st.markdown(f"""<h2 style="color:#ff4b4b; margin:10px 0;">Potensi Kerugian Tanpa AI: Rp {kerugian_val:,.0f} / Bulan</h2>
    <p style="color:#666; font-style:italic;">*Estimasi kebocoran fraud & operasional rata-rata 5% per bulan.</p></div>""", unsafe_allow_html=True)

# --- MENU 3: 4 PAKET LAYANAN (SEJAJAR & RAPI) ---
elif menu == "3. 📦 Paket Layanan":
    st.markdown('<div class="main-header">📦 Paket Solusi Keamanan Terintegrasi</div>', unsafe_allow_html=True)
    
    def draw_pkg(title, setup, monthly, features, key):
        f_list = "".join([f'<div style="margin-bottom:8px;">✅ {f}</div>' for f in features])
        st.markdown(f"""<div class="price-card">
            <div class="card-header">{title}</div>
            <div class="card-body">
                <h4 style="margin-bottom:5px;">Setup: Rp {setup}</h4>
                <p style="color:#ff4b4b; font-weight:bold; font-size:16px;">Bulanan: Rp {monthly}</p>
                <hr style="margin:10px 0;">
                {f_list}
            </div>
        </div>""", unsafe_allow_html=True)
        st.link_button(f"Pesan {title}", wa_url, use_container_width=True, key=key)

    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_pkg("BASIC (MIKRO)", "2.5jt", "500rb", ["Google Gemini AI Core", "Audit Transaksi Harian", "Laporan Mingguan via Email"], "pkg1")
    with c2: draw_pkg("MEDIUM (SME)", "7.5jt", "1.5jt", ["MindBridge Fraud Detection", "Sistem Alarm Aktif", "Otomasi Invoice Pro", "WA Priority Support"], "pkg2")
    with c3: draw_pkg("ENTERPRISE", "25jt", "5jt", ["YOLO CCTV AI Integration", "DataRobot Risk Alert", "Forecasting Bisnis", "Dedicated Manager"], "pkg3")
    with c4: draw_pkg("CORPORATE", "50jt", "10jt", ["Custom AI Training", "Full Workflow Automation", "Compliance Audit Mutlak", "24/7 Security Ops"], "pkg4")

# --- MENU 4: ADMIN PANEL (INTEGRASI TOTAL AI) ---
elif menu == "4. 🔐 Admin Panel (AI Center)":
    st.markdown('<div class="main-header">🔐 V-Guard Intelligence Center</div>', unsafe_allow_html=True)
    
    t1, t2, t3 = st.tabs(["⚙️ Sistem AI Terintegrasi", "📊 Monitoring & Audit", "💬 AI Support Chat"])
    
    with t1:
        st.info("Seluruh ekosistem AI di bawah ini bekerja secara simultan untuk melindungi aset klien.")
        
        tech_data = [
            ("🧠 Google Gemini AI (The Core Brain)", "Analis utama yang memproses data audit kompleks menjadi laporan bahasa manusia yang mudah dipahami."),
            ("🔍 MindBridge Analytics (Fraud Detection)", "Mendeteksi pola kecurangan akuntansi dan anomali transaksi keuangan yang tidak kasat mata."),
            ("📈 DataRobot (Forecasting & Risk Alerting)", "Melakukan prediksi risiko operasional di masa depan untuk mencegah kebocoran sebelum terjadi."),
            ("⚙️ Alteryx (Workflow Automation)", "Mengotomatisasi alur data dari CCTV dan POS tanpa campur tangan manusia untuk kepatuhan mutlak."),
            ("⏰ Workday Adaptive Planning", "Simulasi perencanaan finansial dan alarm cerdas jika biaya menyimpang dari skenario aman."),
            ("📱 Numeric.ai (Financial Notifications)", "Mengirimkan notifikasi kesehatan keuangan bisnis langsung ke smartphone investor."),
            ("📹 YOLO / Vision AI (Computer Vision)", "Mata digital memantau pergerakan stok dan kasir secara visual untuk validasi transaksi."),
            ("🤖 Fitur Pendukung V-Guard", "Integrasi OCR AI (Baca Nota), NLP WhatsApp Bot, dan Predictive Analytics.")
        ]
        
        for title, desc in tech_data:
            st.markdown(f'<div class="tech-item"><b>{title}:</b> {desc}</div>', unsafe_allow_html=True)

    with t2:
        st.subheader("📁 Input Data & Monitoring")
        st.file_uploader("Unggah Laporan atau CCTV Feed Klien", type=['csv','xlsx','jpg','png','mp4'])
        st.error("🚨 ALARM AKTIF: MindBridge mendeteksi anomali transaksi di Cabang Tangerang.")
        
    with t3:
        st.subheader("💬 Chat Box V-Guard")
        st.markdown("""<div style="background:#f1f1f1; padding:15px; border-radius:10px; margin-bottom:10px;">
        <b>V-Guard AI:</b> Selamat malam Pak Erwin. Analisis harian selesai. Efisiensi operasional meningkat 12% hari ini.</div>""", unsafe_allow_html=True)
        st.text_input("Ketik pertanyaan ke AI...")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Strategically Led by Erwin Sinaga")
