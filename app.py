import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os

# 1. KONFIGURASI SISTEM (Anti-Error Baris 4 & 8)
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Masukkan kembali API Key Bapak di sini
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. CSS TAMPILAN MEWAH (Warna Biru Navy & Emas)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; color: white !important; }
    section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] p { color: white !important; }
    .hero-bg { 
        background-color: #0e1117; padding: 50px; border-radius: 20px; color: white; 
        text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px;
    }
    .card-service {
        background-color: white; padding: 25px; border-radius: 15px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center; height: 100%; color: #0e1117;
    }
    .package-pro { border: 2px solid #FFD700; transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD NAVIGASI")
    
    # Grid untuk foto & nama Founder
    col_f1, col_f2 = st.columns([1, 2])
    with col_f1:
        # Menggunakan foto profesional Bapak
        img = Image.open('image_9.png')
        st.image(img, use_container_width=True)
    with col_f2:
        st.markdown("""
            <div style='padding-top: 10px;'>
                <p style='color: white; font-weight: bold; margin-bottom: 0px;'>Erwin Sinaga</p>
                <p style='color: #FFD700; font-size: 12px;'>Founder V-GUARD</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.divider()
    halaman = st.radio("Pilih Halaman:", ["🌐 Promosi & Umum", "👥 Area Layanan Klien", "🔐 Panel Admin"])
    st.divider()
    st.write("📍 Tangerang, Banten, Indonesia")

# ==========================================
# HALAMAN 1: PROMOSI & UMUM (Fitur Kembali!)
# ==========================================
if halaman == "🌐 Promosi & Umum":
    st.markdown("""
        <div class="hero-bg">
            <h1 style='color: #FFD700;'>V-GUARD AI SYSTEMS</h1>
            <h3>Hentikan Kebocoran Finansial Bisnis Anda.</h3>
            <p>Sistem Audit Otonom Berbasis AI | Standar POJK No. 56/2016.</p>
        </div>
        """, unsafe_allow_html=True)

    col_w1, col_w2, col_w3 = st.columns([1,1,1])
    with col_w2:
        st.link_button("🟢 KONSULTASI AUDIT VIA WHATSAPP", "https://wa.me/6281234567890", use_container_width=True)

    st.write("###")
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image(Image.open('image_9.png'), width=300)
    with c2:
        st.markdown("## FILOSOFI & PROFIL FOUNDER")
        st.write("""
        V-GUARD AI Systems hadir sebagai solusi audit masa depan yang transparan dan akurat. 
        Dibawah kepemimpinan Erwin Sinaga, kami berkomitmen menjaga integritas aset bisnis Anda 
        dengan teknologi AI tercanggih.
        """)
        st.info("📍 Senior Business Leader (Tangerang)")

    st.write("### Daftar Layanan Investasi")
    p1, p2, p3 = st.columns(3)
    p1.markdown('<div class="card-service"><h3>📦 LITE</h3><h2>7,5 Jt</h2><p>Audit Angka Dasar</p></div>', unsafe_allow_html=True)
    p2.markdown('<div class="card-service package-pro"><h3>🚀 PRO</h3><h2 style="color: #FFD700;">15 Jt</h2><p><b>Fitur LITE +</b><br>Investigasi Fraud AI</p></div>', unsafe_allow_html=True)
    p3.markdown('<div class="card-service"><h3>🏢 ENTERPRISE</h3><h2>25 Jt</h2><p><b>Fitur PRO +</b><br>Konsultasi Strategis</p></div>', unsafe_allow_html=True)

# ==========================================
# HALAMAN 2: AREA LAYANAN KLIEN (Fitur Kembali!)
# ==========================================
elif halaman == "👥 Area Layanan Klien":
    st.title("👥 Dashboard Monitor Klien V-GUARD")
    st.info("Sistem AI memantau data bisnis Bapak secara real-time.")
    
    data_klien = {
        "Nama Bisnis": ["Resto BSD Utama", "Retail Tangerang Central", "Cafe Serpong", "Gudang Logistik"],
        "Paket": ["V-GUARD PRO", "V-GUARD LITE", "V-GUARD PRO", "ENTERPRISE"],
        "Status": ["🛡️ Aman", "⚠️ Cek Selisih", "🛡️ Aman", "🛡️ Aman"]
    }
    st.table(pd.DataFrame(data_klien))

# ==========================================
# HALAMAN 3: PANEL ADMIN (Fitur Audit AI & Invoice Kembali!)
# ==========================================
else:
    st.title("🔐 Panel Kendali Admin V-GUARD")
    pw = st.text_input("Password Admin:", type="password")
    
    if pw == "vguard2026":
        st.success("Akses Diterima.")
        tab_audit, tab_invoice = st.tabs(["📊 Jalankan Audit AI", "🧾 Buat Invoice"])
        
        with tab_audit:
            st.subheader("🛠️ Sistem Audit AI Otonom")
            data_audit = st.text_area("Tempel Data Transaksi Klien di sini:")
            if st.button("JALANKAN AUDIT AI"):
                with st.spinner("AI sedang memproses..."):
                    try:
                        res = model.generate_content("Analisis data ini untuk mencari fraud atau selisih: " + data_audit)
                        st.markdown(res.text)
                        st.balloons()
                    except:
                        st.error("Gagal terhubung ke AI. Cek API Key Anda.")
        
        with tab_invoice:
            st.subheader("🧾 Generator Invoice V-GUARD")
            with st.form("invoice_form"):
                col_i1, col_i2 = st.columns(2)
                with col_i1:
                    nama_klien_inv = st.text_input("Nama Klien:")
                    paket_inv = st.selectbox("Pilih Paket:", ["LITE", "PRO", "ENTERPRISE"])
                with col_i2:
                    tgl_inv = st.date_today()
                submit_inv = st.form_submit_button("Generate Tampilan Invoice")
                
                if submit_inv:
                    st.markdown(f"""
                    <div style='border: 1px solid #ccc; padding: 20px; border-radius: 10px; background-color: #fff;'>
                        <h3 style='text-align: center; color: #0e1117;'>INVOICE V-GUARD</h3>
                        <hr>
                        <p><b>Kepada:</b> {nama_klien_inv}</p>
                        <p><b>Tanggal:</b> {tgl_inv}</p>
                        <p><b>Deskripsi:</b> Langganan Sistem Audit V-GUARD (Paket {paket_inv})</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.warning("Screenshot bagian ini untuk dikirim ke klien.")
                    
    elif pw != "":
        st.error("Akses Ditolak!")
