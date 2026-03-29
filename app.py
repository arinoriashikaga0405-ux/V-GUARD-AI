import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os
from datetime import datetime

# 1. KONFIGURASI SISTEM (Anti-Error)
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Masukkan kembali API Key Bapak di sini
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. CSS TAMPILAN MEWAH (Warna Biru Navy & Emas)
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
    .invoice-box { border: 2px solid #e0e0e0; padding: 20px; border-radius: 10px; background-color: #fff; color: #000; }
    </style>
    """, unsafe_allow_html=True)

# 3. FUNGSI AMBIL FOTO (Penyelamat Error)
def tampilkan_foto(lebar):
    # Mencari file bapak_erwin.jpg sesuai yang ada di GitHub Bapak
    if os.path.exists('bapak_erwin.jpg'):
        st.image(Image.open('bapak_erwin.jpg'), width=lebar)
    else:
        # Ikon cadangan jika file tidak ditemukan agar web tidak crash
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)

# 4. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD NAVIGASI")
    col_f1, col_f2 = st.columns([1, 2])
    with col_f1:
        tampilkan_foto(80)
    with col_f2:
        st.markdown("<p style='font-weight: bold; margin-top: 10px;'>Erwin Sinaga</p><p style='color: #FFD700; font-size: 12px;'>Founder V-GUARD</p>", unsafe_allow_html=True)
        
    st.divider()
    halaman = st.radio("Pilih Halaman:", ["🌐 Promosi & Umum", "👥 Monitoring Klien", "🔐 Admin & Invoice"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: PROMOSI (LANDING PAGE)
# ==========================================
if halaman == "🌐 Promosi & Umum":
    st.markdown("""
        <div class="hero-bg">
            <h1 style='color: #FFD700;'>V-GUARD AI SYSTEMS</h1>
            <h3>Hentikan Kebocoran Finansial Bisnis Anda.</h3>
            <p>Sistem Audit Otonom Berbasis AI | Standar POJK No. 56/2016.</p>
        </div>
        """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 2])
    with c1:
        tampilkan_foto(350)
    with c2:
        st.markdown("## FILOSOFI & PROFIL")
        st.write("V-GUARD hadir sebagai solusi audit transparan di bawah kepemimpinan Erwin Sinaga.")
        st.info("Senior Leader dengan pengalaman 10+ tahun dalam manajemen strategis.")
        st.write("### Daftar Layanan")
        p1, p2, p3 = st.columns(3)
        p1.markdown('<div class="card-service"><b>📦 LITE</b><br>7,5 Jt</div>', unsafe_allow_html=True)
        p2.markdown('<div class="card-service" style="border:1px solid #FFD700"><b>🚀 PRO</b><br>15 Jt</div>', unsafe_allow_html=True)
        p3.markdown('<div class="card-service"><b>🏢 ENTERPRISE</b><br>25 Jt</div>', unsafe_allow_html=True)

# ==========================================
# HALAMAN 2: MONITORING KLIEN
# ==========================================
elif halaman == "👥 Monitoring Klien":
    st.title("👥 Dashboard Monitor Klien")
    df = pd.DataFrame({
        "Nama Bisnis": ["Resto BSD", "Retail Tangerang", "Cafe Serpong"],
        "Paket": ["PRO", "LITE", "ENTERPRISE"],
        "Status AI": ["🛡️ Aman", "⚠️ Cek Selisih", "🛡️ Aman"]
    })
    st.table(df)

# ==========================================
# HALAMAN 3: ADMIN & INVOICE
# ==========================================
else:
    st.title("🔐 Panel Admin & Penagihan")
    pw = st.text_input("Password Admin:", type="password")
    
    if pw == "vguard2026":
        tab_audit, tab_invoice = st.tabs(["📊 Audit AI", "🧾 Buat Invoice"])
        
        with tab_audit:
            data_input = st.text_area("Tempel Data Transaksi Klien:")
            if st.button("JALANKAN AUDIT AI"):
                res = model.generate_content("Analisis data ini: " + data_input)
                st.markdown(res.text)
        
        with tab_invoice:
            with st.form("inv"):
                klien = st.text_input("Nama Klien:")
                pkt = st.selectbox("Paket:", ["LITE", "PRO", "ENTERPRISE"])
                if st.form_submit_button("Generate Invoice"):
                    st.markdown(f"""
                    <div class='invoice-box'>
                        <h3 style='text-align: center;'>INVOICE V-GUARD</h3>
                        <p><b>Kepada:</b> {klien}</p>
                        <p><b>Layanan:</b> Paket {pkt}</p>
                        <p><b>Tanggal:</b> {datetime.now().strftime('%d/%m/%Y')}</p>
                    </div>
                    """, unsafe_allow_html=True)
    elif pw != "":
        st.error("Password Salah!")
