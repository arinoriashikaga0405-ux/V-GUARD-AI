import streamlit as st
import pandas as pd
import os
from PIL import Image

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Fungsi Foto agar tidak ada NameError lagi
def get_foto(lebar):
    try:
        if os.path.exists('erwin.jpg'):
            return st.image(Image.open('erwin.jpg'), width=lebar)
        else:
            return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)
    except:
        st.write("📸")

# 2. STATUS LOGIN
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

# 3. TAMPILAN SIDEBAR & NAVIGASI
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>🛡️ V-GUARD</h1>", unsafe_allow_html=True)
    
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(60)
    with col_n: st.markdown("<b style='color:white;'>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    
    st.divider()
    
    # LOGIKA MENU: Menentukan menu apa saja yang muncul
    if st.session_state.role == "admin":
        opsi = ["🌐 Beranda", "🤖 AI Auditor (Admin)", "📝 Meeting Lab"]
    elif st.session_state.role == "klien":
        opsi = ["🌐 Beranda", "📊 Dashboard Klien", "📝 Meeting Lab"]
    else:
        opsi = ["🌐 Beranda", "📝 Meeting Lab"]
    
    # Tombol Menu Utama
    menu = st.radio("NAVIGASI UTAMA:", opsi)

    st.divider()

    if st.session_state.role:
        st.success(f"Mode: {st.session_state.role.upper()}")
        if st.button("🚪 Logout"):
            st.session_state.role = None
            st.rerun()
    else:
        login_vguard()

# 4. ISI HALAMAN (PENTING: Logika ini yang mengganti tampilan Beranda)
# ==========================================

# CSS UNTUK TAMPILAN EXECUTIVE
st.markdown("""<style>
    .stApp { background-color: #f4f6f9; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 3px solid #FFD700; }
    .hero-bg { background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); padding: 30px; border-radius: 20px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 25px; }
    .card-box { background: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); border-top: 5px solid #FFD700; }
</style>""", unsafe_allow_html=True)

if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(350)
    with c2:
        st.subheader("🛡️ Proteksi Aset & Deteksi Fraud")
        st.write("Sistem cerdas untuk menutup celah kebocoran operasional bisnis Anda.")
        # Kalkulator ROI Beranda
        omset = st.number_input("Omset Bulanan (Rp):", value=100000000, step=10000000)
        leak = st.slider("Estimasi Kebocoran (%):", 0, 15, 3)
        st.markdown(f"### Potensi Penyelamatan: :red[Rp {omset*(leak/100):,.0f}]")

elif menu == "📊 Dashboard Klien":
    st.title("📊 Landing Page Klien")
    st.markdown("---")
    k1, k2, k3 = st.columns(3)
    k1.metric("Omset Terproteksi", "Rp 5,2 Miliar", "Safe")
    k2.metric("Anomali Terdeteksi", "24 Kasus", "-12%")
    k3.metric("Profit Terselamatkan", "Rp 158 Juta", "+8%")
    
    st.write("### Grafik Keamanan Real-Time")
    chart_data = pd.DataFrame({'Hari': ['Sen', 'Sel', 'Rab', 'Kam', 'Jum'], 'Data': [10, 15, 12, 18, 20]})
    st.line_chart(chart_data.set_index('Hari'))

elif menu == "🤖 AI Auditor (Admin)":
    st.title("🤖 Landing Page Admin")
    st.info("Pusat Kendali Audit Strategis.")
    f = st.file_uploader("Upload Transaksi Global", type=['csv','xlsx'])
    if f:
        st.success("File siap di-audit.")

elif menu == "📝 Meeting Lab":
    st.title("📝 AI Meeting Lab")
    txt = st.text_area("Tempel hasil rapat di sini:", height=200)
    if st.button("Buat Ringkasan AI"):
        st.info("Fitur sedang memproses transkrip Anda...")
