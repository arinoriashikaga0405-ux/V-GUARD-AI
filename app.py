import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os
from datetime import datetime
import urllib.parse
import io

# 1. KONFIGURASI SISTEM
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Konfigurasi AI (Pastikan API Key Bapak sudah benar)
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. CSS TAMPILAN PREMIUM
st.markdown("""
    <style>
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; color: white !important; }
    .hero-bg { 
        background-color: #0e1117; padding: 50px; border-radius: 20px; color: white; 
        text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px;
    }
    .card-service {
        background-color: white; padding: 25px; border-radius: 15px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center; height: 100%; color: #0e1117;
    }
    .founder-text { display: flex; flex-direction: column; justify-content: center; height: 80px; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #FFD700; color: #0e1117; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. FUNGSI PENDUKUNG (Foto & AI)
def get_foto(lebar):
    if os.path.exists('erwin.jpg'):
        return st.image(Image.open('erwin.jpg'), width=lebar)
    else:
        return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)

# 4. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD SYSTEMS")
    col_f, col_n = st.columns([1, 2])
    with col_f:
        get_foto(80)
    with col_n:
        st.markdown(f"""
            <div class='founder-text'>
                <p style='color: white; font-weight: bold; margin-bottom: 0px;'>Erwin Sinaga</p>
                <p style='color: #FFD700; font-size: 11px;'>Founder V-GUARD</p>
            </div>
        """, unsafe_allow_html=True)
    st.divider()
    halaman = st.radio("Navigasi:", ["🌐 Beranda & Filosofi", "🤖 AI Auditor (Upload Data)", "🔐 Panel Kontrol WA"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: BERANDA
# ==========================================
if halaman == "🌐 Beranda & Filosofi":
    st.markdown("""
        <div class="hero-bg">
            <h1 style='color: #FFD700;'>V-GUARD AI SYSTEMS</h1>
            <h3>Hentikan Kebocoran Finansial Bisnis Anda Sekarang.</h3>
            <p>Sistem Audit Otonom | Deteksi Fraud Real-time | Standar POJK No. 56/2016.</p>
        </div>
        """, unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c1:
        get_foto(350) 
    with c2:
        st.markdown("## V-GUARD: BUKAN SEKADAR SOFTWARE")
        st.write("""
        V-Guard adalah **AI Auditor** cerdas yang memberikan **Alarm Merah** langsung ke Business Owner. 
        Sistem kami secara otomatis mendeteksi kebocoran dana, menagih piutang lewat integrasi WhatsApp, 
        dan mengirimkan laporan mingguan yang komprehensif.
        """)
        st.success("🛡️ Fokus pada Profit, Biarkan V-Guard Menjaga Aset Anda.")
        
        st.write("### Pilihan Paket Proteksi")
        p1, p2, p3 = st.columns(3)
        p1.markdown('<div class="card-service"><b>📦 LITE</b><br>7,5 Jt/bln</div>', unsafe_allow_html=True)
        p2.markdown('<div class="card-service" style="border: 2px solid #FFD700"><b>🚀 PRO</b><br>15 Jt/bln</div>', unsafe_allow_html=True)
        p3.markdown('<div class="card-service"><b>🏢 ENTERPRISE</b><br>25 Jt/bln</div>', unsafe_allow_html=True)

# ==========================================
# HALAMAN 2: AI AUDITOR (INTEGRASI BARU)
# ==========================================
elif halaman == "🤖 AI Auditor (Upload Data)":
    st.title("🤖 Analisis Data AI Auditor")
    st.write("Unggah file transaksi (Excel/CSV) untuk mendeteksi potensi kebocoran.")
    
    uploaded_file = st.file_uploader("Pilih File Laporan Transaksi", type=['csv', 'xlsx'])
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            st.write("### Pratinjau Data:")
            st.dataframe(df.head())
            
            if st.button("JALANKAN AUDIT AI SEKARANG"):
                with st.spinner("AI sedang menganalisis pola transaksi..."):
                    # Integrasi ke Gemini AI untuk analisis data
                    prompt = f"Analisis data transaksi berikut dan cari potensi kecurangan atau anomali: {df.to_string(index=False)}"
                    response = model.generate_content(prompt)
                    
                    st.markdown("### 📋 Hasil Temuan AI Auditor:")
                    st.write(response.text)
                    st.warning("Gunakan hasil ini sebagai dasar pengiriman Alarm Merah ke Klien.")
        except Exception as e:
            st.error(f"Gagal memproses file: {e}")

# ==========================================
# HALAMAN 3: PANEL KONTROL WA
# ==========================================
elif halaman == "🔐 Panel Kontrol WA":
    st.title("🔐 Panel Komunikasi V-GUARD")
    pw = st.text_input("Password Admin:", type="password")
    
    if pw == "vguard2026":
        t1, t2, t3 = st.tabs(["🚨 Alarm Merah", "🧾 Penagihan WA", "📊 Laporan Mingguan"])
        
        with t1:
            wa1 = st.text_input("No WA Owner (628...):")
            txt1 = st.text_area("Detail Temuan Kecurangan:")
            msg1 = f"*[🚨 V-GUARD ALARM MERAH]*\n\nSistem mendeteksi anomali: {txt1}\nSegera lakukan investigasi internal.\n\n- Erwin Sinaga"
            if st.button("Kirim Alarm Merah"):
                st.link_button("🚀 Kirim ke WhatsApp", f"https://wa.me/{wa1}?text={urllib.parse.quote(msg1)}")
        
        with t2:
            wa2 = st.text_input("No WA Klien (Invoice):")
            nom = st.text_input("Nominal Tagihan:")
            msg2 = f"*[🛡️ V-GUARD BILLING]*\n\nTagihan Anda sebesar Rp {nom} telah jatuh tempo.\nMohon diselesaikan hari ini.\n\n- Erwin Sinaga"
            if st.button("Kirim Invoice"):
                st.link_button("🧾 Kirim Penagihan", f"https://wa.me/{wa2}?text={urllib.parse.quote(msg2)}")
                
        with t3:
            wa3 = st.text_input("No WA Klien (Laporan):")
            cat = st.text_area("Ringkasan Audit Minggu Ini:")
            msg3 = f"*[🛡️ LAPORAN MINGGUAN V-GUARD]*\n\nRingkasan: {cat}\nAset Anda dalam pengawasan penuh.\n\n- Erwin Sinaga"
            if st.button("Kirim Laporan"):
                st.link_button("📊 Kirim Laporan Mingguan", f"https://wa.me/{wa3}?text={urllib.parse.quote(msg3)}")
