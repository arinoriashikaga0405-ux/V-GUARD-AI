import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os
from datetime import datetimeimport streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os
from datetime import datetime
import urllib.parse
import io

# 1. KONFIGURASI SISTEM
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")
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

# Konfigurasi AI (Masukkan kembali API Key Bapak di sini)
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
        box-shadow: 0 4px 15px rgba(0,0,0,0.2); text-align: left; height: 100%; color: #0e1117;
        border-top: 5px solid #FFD700;
    }
    .card-title { color: #0e1117; font-size: 20px; font-weight: bold; margin-bottom: 10px; text-align: center; }
    .card-price { color: #d4af37; font-size: 24px; font-weight: bold; text-align: center; margin-bottom: 15px; }
    .founder-text { display: flex; flex-direction: column; justify-content: center; height: 80px; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #FFD700; color: #0e1117; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. FUNGSI AMBIL FOTO (Kunci ke erwin.jpg)
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
    halaman = st.radio("Navigasi:", ["🌐 Beranda & Layanan", "🤖 AI Auditor (Upload Data)", "🔐 Panel Kontrol WA"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: BERANDA & DETAIL LAYANAN
# ==========================================
if halaman == "🌐 Beranda & Layanan":
    st.markdown("""
        <div class="hero-bg">
            <h1 style='color: #FFD700;'>V-GUARD AI SYSTEMS</h1>
            <h3>AI Auditor Terpercaya untuk Bisnis Anda.</h3>
            <p>Mendeteksi Kebocoran | Menagih Piutang | Laporan Otomatis.</p>
        </div>
        """, unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c1:
        get_foto(350) 
    with c2:
        st.markdown("## SOLUSI V-GUARD")
        st.write("""
        **V-Guard** hadir sebagai tameng finansial bagi pemilik bisnis (SME/UMKM). Kami menggunakan kecerdasan buatan 
        untuk memastikan setiap rupiah di bisnis Anda terlindungi dari manipulasi atau kelalaian.
        """)
        
        st.markdown("### ✨ Fitur Utama Produk:")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("- **🚨 Alarm Merah:** Notifikasi instan via WA saat terdeteksi selisih transaksi.")
            st.markdown("- **🤖 AI Deep Audit:** Analisis data transaksi otomatis untuk mencari pola fraud.")
        with col_b:
            st.markdown("- **🧾 WA Invoice:** Penagihan piutang otomatis yang terintegrasi.")
            st.markdown("- **📊 Weekly Insight:** Laporan kinerja keuangan mingguan langsung ke HP Anda.")

    st.divider()
    st.markdown("<h2 style='text-align: center;'>Paket Langganan V-GUARD</h2>", unsafe_allow_html=True)
    
    # DETAIL PAKET LANGGANAN
    p1, p2, p3 = st.columns(3)
    
    with p1:
        st.markdown("""
            <div class="card-service">
                <div class="card-title">📦 V-LITE</div>
                <div class="card-price">Rp 7,5 Jt <small>/bln</small></div>
                <ul>
                    <li>Monitoring 1 Outlet</li>
                    <li>Notifikasi Alarm Merah (WA)</li>
                    <li>Laporan Mingguan Dasar</li>
                    <li>Support Chat 24/7</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with p2:
        st.markdown("""
            <div class="card-service" style="background-color: #fdfdfd; transform: scale(1.05);">
                <div class="card-title">🚀 V-PRO</div>
                <div class="card-price">Rp 15 Jt <small>/bln</small></div>
                <p style="text-align:center; font-size:12px; color:orange;"><b>PALING POPULER</b></p>
                <ul>
                    <li>Monitoring s/d 5 Outlet</li>
                    <li><b>AI Deep Audit Analysis</b></li>
                    <li>Penagihan Invoice Otomatis</li>
                    <li>Laporan Analitik Mendalam</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with p3:
        st.markdown("""
            <div class="card-service">
                <div class="card-title">🏢 V-ENTERPRISE</div>
                <div class="card-price">Rp 25 Jt <small>/bln</small></div>
                <ul>
                    <li>Multi-Outlet (Unlimited)</li>
                    <li>Integrasi API Custom</li>
                    <li>Dedicated AI Consultant</li>
                    <li>Prioritas Penanganan Fraud</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# HALAMAN 2 & 3 (FUNGSI TETAP SAMA)
# ==========================================
elif halaman == "🤖 AI Auditor (Upload Data)":
    st.title("🤖 Analisis Data AI Auditor")
    uploaded_file = st.file_uploader("Pilih File Laporan Transaksi (Excel/CSV)", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        st.success("File Berhasil di-upload. Klik 'Jalankan Audit' di bawah.")
        if st.button("JALANKAN AUDIT AI SEKARANG"):
            st.info("AI sedang menganalisis kecurangan...")

elif halaman == "🔐 Panel Kontrol WA":
    st.title("🔐 Panel Komunikasi V-GUARD")
    pw = st.text_input("Password Admin:", type="password")
    if pw == "vguard2026":
        st.success("Akses Diterima.")
        st.tabs(["🚨 Alarm Merah", "🧾 Penagihan WA", "📊 Laporan Mingguan"])
# Konfigurasi AI (Masukkan kembali API Key Bapak di sini)
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
        box-shadow: 0 4px 15px rgba(0,0,0,0.2); text-align: left; height: 100%; color: #0e1117;
        border-top: 5px solid #FFD700;
    }
    .card-title { color: #0e1117; font-size: 20px; font-weight: bold; margin-bottom: 10px; text-align: center; }
    .card-price { color: #d4af37; font-size: 24px; font-weight: bold; text-align: center; margin-bottom: 15px; }
    .founder-text { display: flex; flex-direction: column; justify-content: center; height: 80px; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #FFD700; color: #0e1117; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. FUNGSI AMBIL FOTO (Kunci ke erwin.jpg)
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
    halaman = st.radio("Navigasi:", ["🌐 Beranda & Layanan", "🤖 AI Auditor (Upload Data)", "🔐 Panel Kontrol WA"])
    st.divider()
    st.write("📍 Tangerang, Indonesia")

# ==========================================
# HALAMAN 1: BERANDA & DETAIL LAYANAN
# ==========================================
if halaman == "🌐 Beranda & Layanan":
    st.markdown("""
        <div class="hero-bg">
            <h1 style='color: #FFD700;'>V-GUARD AI SYSTEMS</h1>
            <h3>AI Auditor Terpercaya untuk Bisnis Anda.</h3>
            <p>Mendeteksi Kebocoran | Menagih Piutang | Laporan Otomatis.</p>
        </div>
        """, unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c1:
        get_foto(350) 
    with c2:
        st.markdown("## SOLUSI V-GUARD")
        st.write("""
        **V-Guard** hadir sebagai tameng finansial bagi pemilik bisnis (SME/UMKM). Kami menggunakan kecerdasan buatan 
        untuk memastikan setiap rupiah di bisnis Anda terlindungi dari manipulasi atau kelalaian.
        """)
        
        st.markdown("### ✨ Fitur Utama Produk:")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("- **🚨 Alarm Merah:** Notifikasi instan via WA saat terdeteksi selisih transaksi.")
            st.markdown("- **🤖 AI Deep Audit:** Analisis data transaksi otomatis untuk mencari pola fraud.")
        with col_b:
            st.markdown("- **🧾 WA Invoice:** Penagihan piutang otomatis yang terintegrasi.")
            st.markdown("- **📊 Weekly Insight:** Laporan kinerja keuangan mingguan langsung ke HP Anda.")

    st.divider()
    st.markdown("<h2 style='text-align: center;'>Paket Langganan V-GUARD</h2>", unsafe_allow_html=True)
    
    # DETAIL PAKET LANGGANAN
    p1, p2, p3 = st.columns(3)
    
    with p1:
        st.markdown("""
            <div class="card-service">
                <div class="card-title">📦 V-LITE</div>
                <div class="card-price">Rp 7,5 Jt <small>/bln</small></div>
                <ul>
                    <li>Monitoring 1 Outlet</li>
                    <li>Notifikasi Alarm Merah (WA)</li>
                    <li>Laporan Mingguan Dasar</li>
                    <li>Support Chat 24/7</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with p2:
        st.markdown("""
            <div class="card-service" style="background-color: #fdfdfd; transform: scale(1.05);">
                <div class="card-title">🚀 V-PRO</div>
                <div class="card-price">Rp 15 Jt <small>/bln</small></div>
                <p style="text-align:center; font-size:12px; color:orange;"><b>PALING POPULER</b></p>
                <ul>
                    <li>Monitoring s/d 5 Outlet</li>
                    <li><b>AI Deep Audit Analysis</b></li>
                    <li>Penagihan Invoice Otomatis</li>
                    <li>Laporan Analitik Mendalam</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with p3:
        st.markdown("""
            <div class="card-service">
                <div class="card-title">🏢 V-ENTERPRISE</div>
                <div class="card-price">Rp 25 Jt <small>/bln</small></div>
                <ul>
                    <li>Multi-Outlet (Unlimited)</li>
                    <li>Integrasi API Custom</li>
                    <li>Dedicated AI Consultant</li>
                    <li>Prioritas Penanganan Fraud</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# HALAMAN 2 & 3 (FUNGSI TETAP SAMA)
# ==========================================
elif halaman == "🤖 AI Auditor (Upload Data)":
    st.title("🤖 Analisis Data AI Auditor")
    uploaded_file = st.file_uploader("Pilih File Laporan Transaksi (Excel/CSV)", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        st.success("File Berhasil di-upload. Klik 'Jalankan Audit' di bawah.")
        if st.button("JALANKAN AUDIT AI SEKARANG"):
            st.info("AI sedang menganalisis kecurangan...")

elif halaman == "🔐 Panel Kontrol WA":
    st.title("🔐 Panel Komunikasi V-GUARD")
    pw = st.text_input("Password Admin:", type="password")
    if pw == "vguard2026":
        st.success("Akses Diterima.")
        st.tabs(["🚨 Alarm Merah", "🧾 Penagihan WA", "📊 Laporan Mingguan"])
import urllib.parse
import io

# 1. KONFIGURASI SISTEM
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Konfigurasi AI (Masukkan kembali API Key Bapak di sini)
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. CSS TAMPILAN PREMIUM (Navy, Gold, White)
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

# 4. SIDEBAR NAVIGATION (With Logo, Foto, Name in Column)
with st.sidebar:
    # --- MENAMBAHKAN LOGO DI ATAS FOTO ---
    st.markdown("### 🛡️ V-GUARD SYSTEMS")
    
    # Grid Kolom agar Foto & Nama Sejajar Ke Samping
    col_f, col_n = st.columns([1, 2])
    
    with col_f:
        get_foto(80) # Foto Erwin Sinaga
        
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
# HALAMAN 1: BERANDA (DESAIN DIKUNCI MATI)
# ==========================================
if halaman == "🌐 Beranda & Filosofi":
    st.markdown("""
        <div class="hero-bg">
            <h1 style='color: #FFD700;'>V-GUARD AI SYSTEMS</h1>
            <h3>Hentikan Kebocoran Finansial Bisnis Anda.</h3>
            <p>Sistem Audit Otonom Berbasis AI | Standar POJK No. 56/2016.</p>
        </div>
        """, unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c1:
        get_foto(350) # Foto Besar Bapak di Landing Page
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
# HALAMAN 2: AI AUDITOR (INTEGRASI PENUH)
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
# HALAMAN 3: PANEL KONTROL WA (FULL SUPPORT)
# ==========================================
elif halaman == "🔐 Panel Kontrol WA":
    st.title("🔐 Panel Komunikasi V-GUARD")
    pw = st.text_input("Password Admin:", type="password")
    
    if pw == "vguard2026":
        t1, t2, t3 = st.tabs(["🚨 Alarm Merah", "🧾 Penagihan WA", "📊 Laporan Mingguan"])
        
        with t1:
            st.subheader("Kirim Alarm Merah (Fraud Deteksi)")
            wa1 = st.text_input("No WA Owner (628...):")
            txt1 = st.text_area("Detail Temuan Kecurangan:")
            msg1 = f"*[🚨 V-GUARD ALARM MERAH]*\n\nSistem mendeteksi anomali serius: {txt1}\nMohon segera lakukan investigasi internal.\n\n- Erwin Sinaga"
            if st.button("Generate Link WA Alarm"):
                st.link_button("🚀 Buka WhatsApp Sekarang", f"https://wa.me/{wa1}?text={urllib.parse.quote(msg1)}")
        
        with t2:
            st.subheader("Penagihan WA Jatuh Tempo")
            wa2 = st.text_input("No WA Klien (Invoice):")
            nom = st.text_input("Nominal Tagihan V-GUARD:")
            msg2 = f"*[🛡️ V-GUARD BILLING]*\n\nHalo,\nTagihan layanan V-GUARD sebesar Rp {nom} telah jatuh tempo.\nMohon diselesaikan hari ini agar proteksi AI tetap berjalan.\n\n- Erwin Sinaga"
            if st.button("Generate Link WA Billing"):
                st.link_button("🧾 Buka WhatsApp Tagihan", f"https://wa.me/{wa2}?text={urllib.parse.quote(msg2)}")
                
        with t3:
            st.subheader("Kirim Laporan Mingguan Klien")
            wa3 = st.text_input("No WA Klien (Laporan):")
            b_n = st.text_input("Nama Bisnis Klien:")
            p_n = st.text_input("Periode Audit (Contoh: 23-29 Mar):")
            s_a = st.selectbox("Status Minggu Ini:", ["🛡️ AMAN", "⚠️ NORMAL", "🚨 TERDETEKSI SELISIH"])
            c_a = st.text_area("Ringkasan AI V-GUARD:")
            msg3 = f"*[🛡️ LAPORAN MINGGUAN V-GUARD]*\n\nBisnis: {b_n}\nPeriode: {p_n}\n\nStatus: {s_a}\nRingkasan Audit AI: {c_a}\nAset Anda dalam pengawasan penuh.\n\n- Erwin Sinaga"
            if st.button("Generate Link WA Laporan"):
                st.link_button("📊 Buka WhatsApp Laporan", f"https://wa.me/{wa3}?text={urllib.parse.quote(msg3)}")
else:
    st.title("👥 Monitoring Klien")
    st.info("Sistem AI memantau anomali secara real-time.")
