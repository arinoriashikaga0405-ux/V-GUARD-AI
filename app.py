import streamlit as st
import pandas as pd
import google.generativeai as genai
import urllib.parse
import os
from PIL import Image

# 1. KONFIGURASI UTAMA
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Fungsi Foto agar tidak NameError
def get_foto(lebar):
    try:
        if os.path.exists('erwin.jpg'):
            return st.image(Image.open('erwin.jpg'), width=lebar)
        else:
            return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)
    except:
        st.write("📸")

# 2. SISTEM LOGIN & SESSION
if 'role' not in st.session_state:
    st.session_state.role = None

def login_vguard():
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔐 Login Akses")
    with st.sidebar.form("login_form"):
        u = st.text_input("Username").strip().lower()
        p = st.text_input("Password", type="password").strip()
        submit = st.form_submit_button("Masuk Ke Sistem")
        if submit:
            if u == "admin" and p == "Vguard2026":
                st.session_state.role = "admin"
                st.rerun()
            elif u == "klien" and p == "User2026":
                st.session_state.role = "klien"
                st.rerun()
            else:
                st.sidebar.error("Login Gagal!")

# 3. CSS DESIGN (Tampilan Dashboard)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 3px solid #FFD700; }
    .hero-bg { background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); padding: 30px; border-radius: 20px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 25px; }
    .card-service { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); border-top: 5px solid #FFD700; text-align: center; height: 320px; }
    .roi-box { background-color: #fffde6; padding: 20px; border-radius: 15px; border: 2px solid #FFD700; text-align: center; }
</style>
""", unsafe_allow_html=True)

# 4. SIDEBAR & NAVIGASI DINAMIS (MEMPERBAIKI MENU HILANG)
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>🛡️ V-GUARD</h1>", unsafe_allow_html=True)
    
    # Header Profil
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(60)
    with col_n: st.markdown("<b style='color:white;'>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    
    st.divider()
    
    # Penentuan Menu (AI Lab sekarang selalu ada di daftar)
    menu_list = ["🌐 Beranda", "📝 Meeting Lab"]
    
    if st.session_state.role == "admin":
        menu_list.insert(1, "🤖 AI Auditor (Admin)")
    elif st.session_state.role == "klien":
        menu_list.insert(1, "📊 Dashboard Klien")
    
    # Membuat radio button navigasi
    menu = st.radio("NAVIGASI UTAMA:", menu_list)

    st.divider()

    if st.session_state.role:
        st.success(f"Mode Aktif: {st.session_state.role.upper()}")
        if st.button("🚪 Logout"):
            st.session_state.role = None
            st.rerun()
    else:
        login_vguard()

# ==========================================
# 5. LOGIKA HALAMAN (LANDING PAGES)
# ==========================================

# HALAMAN BERANDA
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(350)
    with c2:
        st.subheader("🛡️ Proteksi Aset & Deteksi Fraud")
        st.write("V-Guard menutup celah kebocoran operasional bisnis Anda dengan kecerdasan buatan.")
        
        st.markdown("<div class='roi-box'>", unsafe_allow_html=True)
        omset = st.number_input("Omset Bulanan (Rp):", value=100000000, step=10000000)
        leak = st.slider("Estimasi Kebocoran (%):", 0, 15, 3)
        rugi = omset * (leak / 100)
        st.markdown(f"<h4>Potensi Penyelamatan:</h4><h2 style='color:#d42f2f;'>Rp {rugi:,.0f}</h2>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# HALAMAN DASHBOARD KLIEN (Landing Page Klien)
elif menu == "📊 Dashboard Klien":
    st.title("📊 Dashboard Laporan Klien")
    st.subheader(f"Selamat Datang, Mitra V-GUARD")
    
    k1, k2, k3 = st.columns(3)
    k1.metric("Omset Terproteksi", "Rp 5,2 Miliar", "Aman")
    k2.metric("Anomali Dicegah", "24 Kasus", "-12%")
    k3.metric("Efisiensi Profit", "8.5%", "+2%")
    
    st.divider()
    st.write("### Grafik Keamanan Transaksi Mingguan")
    chart_data = pd.DataFrame({'Hari': ['Sen', 'Sel', 'Rab', 'Kam', 'Jum', 'Sab', 'Min'], 'Data': [10, 15, 8, 22, 18, 25, 20]})
    st.line_chart(chart_data.set_index('Hari'))

# HALAMAN AI AUDITOR (Landing Page Admin)
elif menu == "🤖 AI Auditor (Admin)":
    st.title("🤖 AI Auditor Engine")
    st.success("Akses Admin Terverifikasi.")
    f = st.file_uploader("Upload Data Transaksi", type=['csv','xlsx'])
    if f:
        df = pd.read_csv(f) if f.name.endswith('.csv') else pd.read_excel(f)
        st.write("### Pratinjau Data")
        st.dataframe(df.head())
        if st.button("Jalankan Audit AI"):
            st.info("Menganalisis potensi fraud pada data...")

# HALAMAN MEETING LAB (AI Lab)
elif menu == "📝 Meeting Lab":
    st.title("📝 AI Meeting Lab")
    st.write("Gunakan fitur ini untuk merangkum poin-poin strategis dari rapat Anda.")
    
    transkrip = st.text_area("Tempel transkrip rapat di sini:", height=200)
    if st.button("Hasilkan Summary Strategis"):
        if transkrip:
            st.success("Analisis AI Berhasil:")
            st.markdown("1. **Poin Utama**: Optimalisasi omset bulan depan.\n2. **Tindakan**: Audit harian pada outlet cabang Tangerang.")
        else:
            st.warning("Silakan masukkan teks terlebih dahulu.")
