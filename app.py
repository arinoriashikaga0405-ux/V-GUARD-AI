import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from PIL import Image

# 1. KONFIGURASI UTAMA & AI
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# MASUKKAN API KEY BAPAK DI SINI
GOOGLE_API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("⚠️ API Key belum terpasang dengan benar.")

# Fungsi Foto (Baris 20-an)
def get_foto(lebar):
    try:
        if os.path.exists('erwin.jpg'):
            return st.image(Image.open('erwin.jpg'), width=lebar)
        else:
            return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)
    except:
        st.write("📸")

# 2. SISTEM LOGIN
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
                st.sidebar.error("Username/Password Salah")

# 3. CSS DESIGN
st.markdown("""<style>
    .stApp { background-color: #f4f6f9; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 3px solid #FFD700; }
    .hero-bg { background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); padding: 30px; border-radius: 20px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 25px; }
    .card-service { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); border-top: 5px solid #FFD700; text-align: center; height: 350px; }
</style>""", unsafe_allow_html=True)

# 4. SIDEBAR & NAVIGASI
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>🛡️ V-GUARD</h1>", unsafe_allow_html=True)
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(60)
    with col_n: st.markdown("<b style='color:white;'>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    st.divider()

    opsi = ["🌐 Beranda", "📝 Meeting Lab"]
    if st.session_state.role == "admin":
        opsi.insert(1, "🤖 AI Auditor (Admin)")
    elif st.session_state.role == "klien":
        opsi.insert(1, "📊 Dashboard Klien")
    
    menu = st.radio("NAVIGASI UTAMA:", opsi)

    if st.session_state.role:
        st.success(f"Mode: {st.session_state.role.upper()}")
        if st.button("🚪 Logout"):
            st.session_state.role = None
            st.rerun()
    else:
        login_vguard()

# ==========================================
# 5. HALAMAN BERANDA
# ==========================================
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(350)
    with c2:
        st.subheader("🛡️ Proteksi Aset & Deteksi Fraud")
        st.write("V-Guard hadir untuk menutup celah kebocoran operasional bisnis Anda dengan kecerdasan buatan.")
        omset = st.number_input("Omset Bulanan (Rp):", value=100000000)
        leak = st.slider("Estimasi Kebocoran (%):", 0, 15, 3)
        st.markdown(f"### Potensi Penyelamatan: :red[Rp {omset*(leak/100):,.0f}]")

    st.divider()
    p1, p2, p3 = st.columns(3)
    WA_LINK = "https://wa.me/6282122190885"
    with p1:
        st.markdown('<div class="card-service"><h4>📦 V-LITE</h4><h3>7,5 Jt</h3><hr><p>1 Outlet/Toko<br>• Laporan Harian</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI SAYA", WA_LINK)
    with p2:
        st.markdown('<div class="card-service" style="border:3px solid #FFD700"><h4>🚀 V-PRO</h4><h3>15 Jt</h3><hr><p>5 Outlet/Toko<br>• Deep Fraud Audit</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI SAYA", WA_LINK)
    with p3:
        st.markdown('<div class="card-service"><h4>🏢 CORPORATE</h4><h3>25 Jt</h3><hr><p>Unlimited Outlet<br>• Priority Support</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI SAYA", WA_LINK)

# ==========================================
# 6. HALAMAN MEETING LAB (DENGAN AI ASLI)
# ==========================================
elif menu == "📝 Meeting Lab":
    st.title("📝 AI Meeting Lab")
    st.write("AI akan merangkum poin strategis dari teks rapat Anda.")
    
    transkrip = st.text_area("Tempel transkrip rapat di sini:", height=300)
    
    if st.button("🚀 JALANKAN PROSES AI"):
        if not transkrip:
            st.warning("Masukkan teks terlebih dahulu.")
        elif GOOGLE_API_KEY == "PASTE_API_KEY_BAPAK_DI_SINI":
            st.error("API Key belum diisi!")
        else:
            with st.spinner("Sedang berpikir..."):
                prompt = f"Rangkumlah transkrip rapat berikut menjadi poin-poin strategis, rencana tindakan (action plan), dan mitigasi risiko fraud: {transkrip}"
                response = model.generate_content(prompt)
                st.subheader("💡 Hasil Analisis Strategis V-GUARD")
                st.info(response.text)

# HALAMAN ADMIN & KLIEN (Placeholder)
elif menu == "📊 Dashboard Klien":
    st.title("📊 Dashboard Laporan Klien")
    st.metric("Profit Aman", "Rp 158.000.000", "+8%")

elif menu == "🤖 AI Auditor (Admin)":
    st.title("🤖 AI Auditor (Admin)")
    st.file_uploader("Upload Transaksi untuk Audit AI")
