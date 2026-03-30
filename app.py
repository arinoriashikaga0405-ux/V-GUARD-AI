import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# CSS PREMIUM (Warna Merah Bold & Professional)
st.markdown("""
<style>
    .main-title { font-size: 30px; font-weight: 800; color: #1f1f1f; }
    .tech-card {
        background: #ffffff; border-radius: 12px; padding: 15px;
        border-left: 5px solid #ff4b4b; margin-bottom: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); transition: 0.3s;
    }
    .tech-card:hover { transform: scale(1.02); }
    .tech-title { font-weight: bold; color: #ff4b4b; font-size: 16px; margin-bottom: 5px; }
    .tech-desc { font-size: 13px; color: #444; line-height: 1.4; }
    .alarm-active {
        background: #ffe5e5; border: 2px solid #ff4b4b; padding: 15px;
        border-radius: 10px; color: #a51d1d; font-weight: bold;
        animation: blinker 1.5s linear infinite;
    }
    @keyframes blinker { 50% { opacity: 0.6; } }
    .chat-bubble {
        background: #f1f1f1; padding: 10px 15px; border-radius: 15px;
        margin-bottom: 10px; font-size: 14px; border-left: 4px solid #ff4b4b;
    }
    .price-card {
        background: white; border-radius: 15px; border: 1px solid #eee;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); height: 400px;
        display: flex; flex-direction: column; overflow: hidden;
    }
    .card-header {
        background: linear-gradient(135deg, #ff4b4b 0%, #a51d1d 100%);
        color: white; padding: 12px; text-align: center; font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 2. SIDEBAR NAVIGASI
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.error("Unggah foto 'erwin.jpg'")
    
    st.title("🛡️ V-Guard AI")
    st.write("---")
    menu = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🏠 Ekosistem Teknologi", 
        "3. 📦 Paket Solusi", 
        "4. 🔐 Admin Panel (Control)"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI Systems")

# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with r:
        st.subheader("Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        st.write("Bapak Erwin Sinaga adalah Senior Business Leader visioner dengan 10+ tahun pengalaman sebagai CEO/CSO di industri perbankan dan aset. Beliau membangun V-Guard AI sebagai benteng pertahanan finansial masa depan.")

# --- MENU 2: EKOSISTEM TEKNOLOGI ---
elif menu == "2. 🏠 Ekosistem Teknologi":
    st.markdown('<div class="main-title">🌐 Ekosistem Teknologi V-Guard AI</div>', unsafe_allow_html=True)
    st.write("V-Guard AI mengintegrasikan platform terbaik dunia untuk akurasi audit 99,9%.")
    
    techs = [
        ("🧠 Google Gemini AI (Core Brain)", "Analis utama yang memproses data audit kompleks menjadi laporan bahasa manusia yang mudah dipahami."),
        ("🔍 MindBridge Analytics (Fraud Detection)", "Mendeteksi pola kecurangan akuntansi dan anomali transaksi keuangan melalui Audit Alarms."),
        ("📈 DataRobot (Forecasting)", "Prediksi risiko operasional di masa depan berdasarkan data historis untuk mencegah kebocoran."),
        ("⚙️ Alteryx (Workflow Automation)", "Otomasi seluruh alur data dari CCTV dan mesin kasir (POS) tanpa campur tangan manusia."),
        ("⏰ Workday Adaptive (Scenario Alarms)", "Simulasi perencanaan finansial dan alarm cerdas jika biaya operasional menyimpang."),
        ("📱 Numeric.ai (Notifications)", "Notifikasi ringkas kesehatan keuangan bisnis langsung ke smartphone investor setiap hari."),
        ("📹 YOLO / Vision AI (Computer Vision)", "'Mata' digital memantau stok dan aktivitas kasir secara visual untuk validasi data.")
    ]
    
    c1, c2 = st.columns(2)
    for i, (title, desc) in enumerate(techs):
        with (c1 if i % 2 == 0 else c2):
            st.markdown(f"""<div class="tech-card"><div class="tech-title">{title}</div><div class="tech-desc">{desc}</div></div>""", unsafe_allow_html=True)

# --- MENU 3: PAKET SOLUSI ---
elif menu == "3. 📦 Paket Solusi":
    st.title("📦 Investasi Keamanan")
    col1, col2 = st.columns(2)
    def draw_pkg(title, setup, monthly, features, key):
        f_list = "".join([f'<div style="font-size:12px;">✅ {f}</div>' for f in features])
        st.markdown(f"""<div class="price-card"><div class="card-header">{title}</div><div style="padding:15px;">
        <h3>Rp {setup}</h3><p style="color:#ff4b4b;">Bulanan: Rp {monthly}</p><hr>{f_list}</div></div>""", unsafe_allow_html=True)
        st.link_button(f"Pilih {title}", wa_url, use_container_width=True, key=key)

    with col1: draw_pkg("Basic Guard", "2.5jt", "500rb", ["AI Fraud Dasar", "Email Support"], "b1")
    with col2: draw_pkg("Premium Shield", "7.5jt", "1.5jt", ["Alarm Aktif", "WA Priority"], "b2")

# --- MENU 4: ADMIN PANEL (LENGKAP) ---
elif menu == "4. 🔐 Admin Panel (Control)":
    st.title("🔐 Control Center")
    
    t1, t2, t3, t4 = st.tabs(["🚨 Alarm & Fraud", "📹 AI CCTV", "🧾 Invoice", "💬 Chat Box AI"])
    
    with t1:
        st.markdown('<div class="alarm-active">🚨 ALARM AKTIF: Terdeteksi Anomali Transaksi di Kasir 02 pukul 19:45!</div>', unsafe_allow_html=True)
        st.write("---")
        st.write("**Riwayat Temuan:**")
        st.table(pd.DataFrame({"Waktu": ["19:45", "18:20"], "Temuan": ["Selisih Stok Visual vs POS", "Double Entry Input"], "Status": ["🚨 Urgent", "✅ Resolved"]}))
        
    with t2:
        st.subheader("📹 Live AI Vision Feed (YOLO)")
        st.image("https://images.unsplash.com/photo-1557597774-9d2739f85a76?q=80&w=500", caption="Deteksi Objek & Gerakan Real-time")
        st.success("✅ CCTV AI Terkoneksi: Objek Manusia & Barang terdeteksi normal.")
        
    with t3:
        st.subheader("🧾 Billing & Invoices")
        st.info("Invoice #VG-MAR-2026: Rp 1,500,000 (Status: Sent to WhatsApp)")
        if st.button("Generate Invoice Baru"):
            st.success("Invoice berhasil dibuat dan dikirim otomatis via NLP Bot.")
            
    with t4:
        st.subheader("💬 V-Guard Intelligence Chat")
        st.markdown('<div class="chat-bubble"><b>V-Guard:</b> Selamat malam Pak Erwin. Ingin mengecek laporan fraud hari ini?</div>', unsafe_allow_html=True)
        st.markdown('<div class="chat-bubble"><b>V-Guard:</b> Saya menemukan 1 anomali di cabang Tangerang. Sudah saya kirimkan detailnya ke WhatsApp Anda.</div>', unsafe_allow_html=True)
        st.text_input("Tanya AI (Contoh: Berapa total transaksi aman hari ini?)")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Strategically Led by Erwin Sinaga")
