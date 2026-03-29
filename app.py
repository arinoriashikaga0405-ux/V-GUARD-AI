import streamlit as st
import pandas as pd
import google.generativeai as genai
import urllib.parse
import os

# 1. KONFIGURASI SISTEM
st.set_page_config(page_title="V-GUARD AI - Revenue Protection", page_icon="🛡️", layout="wide")

# Konfigurasi AI - Ganti API_KEY dengan milik Anda yang valid
API_KEY = "ISI_KODE_API_GEMINI_ANDA_DI_SINI" 
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("API Key AI belum terkonfigurasi dengan benar.")

# DATA KONTAK
WA_NOMOR = "6282122190885" 

# 2. LOGIKA LOGIN (SESSION STATE)
if 'role' not in st.session_state:
    st.session_state.role = None

def login():
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔐 Akses Sistem")
    user = st.sidebar.text_input("Username")
    pw = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Masuk"):
        if user == "admin" and pw == "admin123":
            st.session_state.role = "admin"
            st.rerun()
        elif user == "klien" and pw == "klien123":
            st.session_state.role = "klien"
            st.rerun()
        else:
            st.sidebar.error("Username atau Password Salah")

# 3. CSS EXECUTIVE DESIGN (Landing Page Promosi)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    section[data-testid="stSidebar"] { 
        background-color: #0e1117 !important; 
        border-right: 3px solid #FFD700; 
    }
    .hero-bg { 
        background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); 
        padding: 40px; border-radius: 25px; color: white; text-align: center; 
        border-bottom: 8px solid #FFD700; box-shadow: 0 15px 35px rgba(0,0,0,0.3);
        margin-bottom: 30px;
    }
    .hero-bg h1 { font-size: 36px; color: #FFD700; }
    .card-service { 
        background: white; padding: 20px; border-radius: 20px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.1); color: #0e1117; 
        border-top: 6px solid #FFD700; text-align: center;
        height: 320px; display: flex; flex-direction: column; justify-content: space-between;
    }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(45deg, #FFD700, #b8860b) !important; 
        color: #0e1117 !important; font-weight: bold; border: none;
    }
    .roi-box {
        background-color: #fffde6; padding: 25px; border-radius: 15px;
        border: 2px solid #FFD700; text-align: center;
    }
    .sidebar-user {
        background: rgba(255,255,255,0.1); padding: 10px; border-radius: 8px;
        color: white; border-left: 3px solid #FFD700;
    }
</style>
""", unsafe_allow_html=True)

# 4. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #FFD700; margin-bottom:0px;'>🛡️ V-GUARD</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; font-size:12px;'>Revenue Protection Intelligence</p>", unsafe_allow_html=True)
    st.divider()

    if st.session_state.role:
        st.markdown(f"""<div class='sidebar-user'><b>User:</b> {st.session_state.role.upper()}<br><b>Status:</b> Active</div>""", unsafe_allow_html=True)
        if st.button("🚪 Logout"):
            st.session_state.role = None
            st.rerun()
        st.divider()

    halaman = st.radio("MENU UTAMA:", ["🌐 Beranda & Layanan", "🤖 AI Auditor", "📝 AI Meeting Lab"])
    
    if st.session_state.role is None:
        login()

# ==========================================
# HALAMAN 1: BERANDA & PROMOSI
# ==========================================
if halaman == "🌐 Beranda & Layanan":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Solusi Cerdas Mencegah Kebocoran Omset Bisnis Anda.</p></div>', unsafe_allow_html=True)
    
    st.markdown("### 🛡️ Mengapa V-GUARD?")
    st.write("V-Guard adalah sistem berbasis AI yang didesain khusus untuk mendeteksi anomali transaksi dan mencegah fraud internal secara real-time.")
    
    st.divider()
    
    # KALKULATOR ROI
    st.markdown("<h3 style='text-align: center;'>🧮 Kalkulator Penyelamatan Aset</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        omset = st.number_input("Omset Bulanan (Rp):", min_value=0, value=100000000, step=10000000)
        leakage = st.slider("Estimasi Kebocoran (%):", 0, 15, 3)
    with col2:
        potensi_rugi = omset * (leakage / 100)
        st.markdown(f"""
            <div class="roi-box">
                <p style="margin:0; font-size:16px;">Potensi Kerugian yang Dapat Dicegah:</p>
                <h1 style="color: #d42f2f; margin:10px 0;">Rp {potensi_rugi:,.0f}</h1>
                <p style="font-size: 12px; color: #555;">Tingkatkan profitabilitas Anda dengan menutup celah fraud.</p>
            </div>
        """, unsafe_allow_html=True)

    st.divider()
    
    # PAKET LAYANAN
    st.markdown("<h3 style='text-align: center;'>Pilih Paket Strategis</h3>", unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    
    def wa_link(paket):
        pesan = f"Halo Pak Erwin, saya ingin konsultasi paket V-GUARD {paket}."
        return f"https://wa.me/{WA_NOMOR}?text={urllib.parse.quote(pesan)}"

    with p1:
        st.markdown('<div class="card-service"><div><h4>📦 V-LITE</h4><h3 style="color:#d4af37">7,5 Jt</h3><hr><p>1 Outlet<br>Daily Alarm WA<br>Summary Mingguan</p></div></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI SAYA", wa_link("V-LITE"))
    with p2:
        st.markdown('<div class="card-service" style="border: 3px solid #FFD700;"><div><h4>🚀 V-PRO</h4><h3 style="color:#d4af37">15 Jt</h3><hr><p>5 Outlet<br><b>AI Deep Audit</b><br>Priority Support</p></div></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI SAYA", wa_link("V-PRO"))
    with p3:
        st.markdown('<div class="card-service"><div><h4>🏢 CORPORATE</h4><h3 style="color:#d4af37">25 Jt</h3><hr><p>Unlimited Outlet<br>Custom API<br>Dedicated Manager</p></div></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI SAYA", wa_link("CORPORATE"))

# ==========================================
# HALAMAN 2: AI AUDITOR (ADMIN ONLY)
# ==========================================
elif halaman == "🤖 AI Auditor":
    st.title("🤖 AI Auditor Engine")
    if st.session_state.role != "admin":
        st.warning("⚠️ Akses terbatas. Silakan login sebagai ADMIN untuk menggunakan fitur ini.")
    else:
        uploaded_file = st.file_uploader("Unggah file transaksi (CSV/XLSX)", type=["csv", "xlsx"])
        if uploaded_file:
            try:
                df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
                st.subheader("Pratinjau Data")
                st.dataframe(df.head())
                if st.button("Jalankan Analisis Anomali"):
                    with st.spinner("Menganalisis..."):
                        if 'nominal' in df.columns:
                            mean_val = df['nominal'].mean()
                            anomalies = df[df['nominal'] > (mean_val * 3)]
                            st.success(f"Ditemukan {len(anomalies)} anomali transaksi.")
                            st.table(anomalies)
                        else:
                            st.error("Kolom 'nominal' tidak ditemukan.")
            except Exception as e:
                st.error(f"Eror: {e}")

# ==========================================
# HALAMAN 3: MEETING LAB
# ==========================================
elif halaman == "📝 AI Meeting Lab":
    st.title("📝 AI Meeting Summarizer")
    st.info("Fitur rangkuman rapat strategis (Segera Hadir).")
