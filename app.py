import streamlit as st
import os
import pandas as pd

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# CSS PREMIUM
st.markdown("""
<style>
    .reportview-container { background: #f5f7f9; }
    .st-emotion-cache-1y4p8pa { padding-top: 1rem; }
    .vision-box {
        background: #ffffff; border-radius: 12px; padding: 20px;
        border-left: 5px solid #ff4b4b; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        height: 100%;
    }
    .price-card {
        background: white; border-radius: 15px; border: 1px solid #eee;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); height: 520px;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .card-header {
        background: linear-gradient(135deg, #ff4b4b 0%, #a51d1d 100%);
        color: white; padding: 15px; text-align: center; font-weight: bold;
        border-radius: 15px 15px 0 0; font-size: 18px;
    }
    .roi-box {
        background: #fff5f5; border: 2px solid #ff4b4b; padding: 20px;
        border-radius: 12px; text-align: center; color: #a51d1d;
    }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/6282122190885"

# 2. SIDEBAR NAVIGASI DENGAN FOTO DI ATAS NAMA
with st.sidebar:
    # Foto Founder di Atas Tulisan V-Guard AI
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.error("⚠️ Unggah 'erwin.jpg'")
        
    st.title("🛡️ V-Guard AI")
    st.write("---")
    
    menu = st.radio("Pilih Folder Menu:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI Kerugian", 
        "3. 📦 4 Paket Solusi", 
        "4. 🔐 Admin Panel (Upload)"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI Systems")

# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("👤 Strategic Leadership")
    
    col_txt, col_img = st.columns([2, 1])
    
    with col_txt:
        st.subheader("Erwin Sinaga")
        st.markdown("""
        Bapak Erwin Sinaga adalah seorang Pemimpin Bisnis Senior yang membawa dedikasi dan keahlian mendalam selama lebih dari satu dekade di industri perbankan dan manajemen aset nasional. Selama sepuluh tahun masa baktinya di sektor keuangan formal, beliau telah menguasai berbagai seluk-beluk manajemen risiko kredit, pengawasan kepatuhan operasional, hingga strategi perlindungan aset korporasi skala besar. <br><br>
        Pengalaman luas Bapak Erwin dalam menghadapi dinamika fraud dan celah kebocoran dana di sistem perbankan konvensional menjadi fondasi utama lahirnya ekosistem V-Guard AI. Melalui kepemimpinan strategisnya, beliau menjembatani standar audit ketat perbankan dengan teknologi Artificial Intelligence (AI) terkini, menciptakan sistem pertahanan digital yang holistik, transparan, dan mampu mencegah kebocoran finansial bisnis klien secara mutlak dan real-time.
        """, unsafe_allow_html=True)

    with col_img:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga", use_container_width=True)

# --- MENU 2: VISI, MISI & ROI KERUGIAN KLIEN ---
elif menu == "2. 🎯 Visi, Misi & ROI Kerugian":
    st.title("🎯 Strategi & Analisis Risiko")
    
    v, m = st.columns(2)
    with v:
        st.markdown("""<div class="vision-box"><h3>🎯 Visi</h3>
        <p>Menjadi pemimpin pasar dalam solusi keamanan audit berbasis AI di Indonesia, memastikan integritas finansial bisnis klien terjaga secara mutlak pada tahun 2026.</p></div>""", unsafe_allow_html=True)
    with m:
        st.markdown("""<div class="vision-box"><h3>🚀 Misi</h3>
        <ul>
            <li>Mengintegrasikan teknologi AI tercanggih untuk deteksi fraud otomatis.</li>
            <li>Memberikan laporan audit transparan dan real-time bagi investor.</li>
            <li>Mengotomatisasi sistem pengawasan aset operasional 24/7.</li>
        </ul></div>""", unsafe_allow_html=True)
        
    st.write("---")
    
    # Kalkulator ROI Kerugian Klien
    st.subheader("📈 Analisis Potensi Kerugian & Penyelamatan Aset Klien")
    col_roi1, col_roi2 = st.columns(2)
    with col_roi1:
        omzet = st.number_input("Input Omzet Bisnis Bulanan (Rp):", value=500000000, step=10000000)
        kerugian_persen = 0.05 # Estimasi kebocoran rata-rata 5%
    with col_roi2:
        potensi_rugi = omzet * kerugian_persen
        st.markdown(f"""<div class="roi-box">
        <h4>🚨 Potensi Kerugian Tanpa V-Guard:</h4>
        <h2 style="margin:0;">Rp {potensi_rugi:,.0f} / Bulan</h2>
        <p style="font-size:12px;">*(Estimasi rata-rata kebocoran operasional & fraud global 5%)</p>
        </div>""", unsafe_allow_html=True)

# --- MENU 3: 4 PAKET SOLUSI (SETUP, BULANAN & MANFAAT) ---
elif menu == "3. 📦 4 Paket Solusi":
    st.title("📦 Paket Proteksi & Deteksi Kebocoran")
    
    c1, c2, c3, c4 = st.columns(4)
    
    def draw_card(title, setup, monthly, features, key):
        f_html = "".join([f'<div style="font-size:12px; margin-bottom:5px;">✅ {f}</div>' for f in features])
        st.markdown(f"""<div class="price-card">
            <div class="card-header">{title}</div>
            <div style="padding:15px; flex-grow:1;">
                <h4 style="margin:0;">Setup: Rp {setup}</h4>
                <p style="color:#ff4b4b; font-weight:bold; font-size:15px;">Rp {monthly}/Bln</p>
                <hr style="margin:10px 0;">
                {f_html}
            </div>
        </div>""", unsafe_allow_html=True)
        st.link_button(f"Pilih {title}", wa_url, use_container_width=True, key=key)

    with c1: 
        draw_card("BASIC (MIKRO)", "2.5jt", "500rb", [
            "Gemini AI Core", "Audit Transaksi Harian", 
            "Laporan Mingguan via Email", "Support Chat Dasar"
        ], "p1")
    with c2: 
        draw_card("MEDIUM (SME)", "7.5jt", "1.5jt", [
            "MindBridge Fraud Detection", "Real-time Alarm System", 
            "Auto Invoice Pro", "WA Priority Support"
        ], "p2")
    with c3: 
        draw_card("ENTERPRISE", "25jt", "5jt", [
            "YOLO CCTV AI Integration", "DataRobot Risk Alerting", 
            "Workflow Automation (Alteryx)", "Dedicated Account Manager"
        ], "p3")
    with c4: 
        draw_card("CORPORATE", "50jt", "10jt", [
            "Custom AI Model Training", "Full Compliance Audit", 
            "Numeric.ai Financial Notif", "24/7 Security Operations Center"
        ], "p4")

# --- MENU 4: ADMIN PANEL (FITUR UNTUK ADMIN) ---
elif menu == "4. 🔐 Admin Panel (Upload)":
    st.title("🔐 V-Guard Admin Intelligence Center")
    
    # Fitur Input Data Klien
    st.subheader("📥 Unggah & Analisis Data Klien")
    col_up1, col_up2 = st.columns([2, 1])
    with col_up1:
        uploaded_file = st.file_uploader("Unggah Laporan Transaksi (Excel/CSV/JPG CCTV)", type=['csv','xlsx','jpg','png'])
        if uploaded_file is not None:
            st.success(f"File '{uploaded_file.name}' berhasil diunggah!")
            st.warning("🤖 AI V-Guard sedang menganalisis anomali... (Simulasi)")
    with col_up2:
        st.info("Pilih Jenis Data:\n1. POS Kasir\n2. Log CCTV\n3. Rekening Koran")

    st.write("---")
    st.subheader("📡 Status Monitoring")
    st.error("🚨 Deteksi Anomali: Cabang Tangerang memerlukan audit harian.")
