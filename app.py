import streamlit as st
import pandas as pd
import google.generativeai as genai
import urllib.parse
import os
from PIL import Image

# 1. KONFIGURASI SISTEM
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Masukkan API Key Bapak di sini
API_KEY = "ISI_KODE_API_BAPAK" 
try:
    genai.configure(api_key=API_KEY)
except:
    st.error("Konfigurasi API AI gagal.")

WA_NOMOR = "6282122190885" 

# 2. LOGIKA LOGIN STABIL
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
            # Menggunakan kredensial baru yang lebih aman
            if u == "admin" and p == "Vguard2026":
                st.session_state.role = "admin"
                st.rerun()
            elif u == "klien" and p == "User2026":
                st.session_state.role = "klien"
                st.rerun()
            else:
                st.error("Login Gagal: Periksa kembali!")

# 3. FUNGSI FOTO
def get_foto(w):
    if os.path.exists('erwin.jpg'):
        return st.image(Image.open('erwin.jpg'), width=w)
    else:
        return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=w)

# 4. CSS DESIGN
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 3px solid #FFD700; }
    .hero-bg { background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); padding: 30px; border-radius: 20px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 25px; }
    .hero-bg h1 { color: #FFD700; }
    .card-service { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); border-top: 5px solid #FFD700; text-align: center; height: 300px; display: flex; flex-direction: column; justify-content: space-between; }
    .roi-box { background-color: #fffde6; padding: 20px; border-radius: 15px; border: 2px solid #FFD700; text-align: center; }
</style>
""", unsafe_allow_html=True)

# 5. SIDEBAR
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>🛡️ V-GUARD</h1>", unsafe_allow_html=True)
    
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(60)
    with col_n: st.markdown("<b style='color:white;'>Erwin Sinaga</b><br><small style='color:#FFD700;'>Founder & CEO</small>", unsafe_allow_html=True)
    
    st.divider()
    
    if st.session_state.role:
        st.success(f"Login: {st.session_state.role.upper()}")
        if st.button("🚪 Keluar"):
            st.session_state.role = None
            st.rerun()
    
    menu = st.radio("NAVIGASI:", ["🌐 Beranda", "🤖 AI Auditor", "📝 Meeting Lab"])
    
    if not st.session_state.role:
        login_vguard()

# ==========================================
# ISI HALAMAN
# ==========================================
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(350)
    with c2:
        st.subheader("🛡️ Proteksi Aset & Deteksi Fraud")
        st.write("V-Guard hadir untuk menutup celah kebocoran operasional bisnis Anda dengan kecerdasan buatan.")
        
        # Kalkulator ROI
        st.markdown("<div class='roi-box'>", unsafe_allow_html=True)
        omset = st.number_input("Omset Bulanan (Rp):", value=100000000, step=10000000)
        leak = st.slider("Estimasi Kebocoran (%):", 0, 15, 3)
        rugi = omset * (leak / 100)
        st.markdown(f"<h4>Potensi Penyelamatan:</h4><h2 style='color:#d42f2f;'>Rp {rugi:,.0f}</h2>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.divider()
    
    # Layanan Promosi
    p1, p2, p3 = st.columns(3)
    def wa(pkt): return f"https://wa.me/{WA_NOMOR}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20{pkt}"
    
    with p1:
        st.markdown('<div class="card-service"><h4>📦 V-LITE</h4><h3>7,5 Jt</h3><p>1 Outlet<br>Daily WA Alarm</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI SAYA", wa("V-LITE"))
    with p2:
        st.markdown('<div class="card-service" style="border:3px solid #FFD700"><h4>🚀 V-PRO</h4><h3>15 Jt</h3><p>5 Outlet<br>AI Deep Audit</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI SAYA", wa("V-PRO"))
    with p3:
        st.markdown('<div class="card-service"><h4>🏢 CORPORATE</h4><h3>25 Jt</h3><p>Unlimited<br>Priority Support</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI SAYA", wa("CORPORATE"))

elif menu == "🤖 AI Auditor":
    st.title("🤖 AI Auditor Engine")
    if st.session_state.role != "admin":
        st.warning("⚠️ Fitur ini hanya untuk ADMIN. Silakan login.")
    else:
        st.success("Selamat Datang, Admin!")
        f = st.file_uploader("Upload Data Transaksi", type=['csv','xlsx'])
        if f:
            df = pd.read_csv(f) if f.name.endswith('.csv') else pd.read_excel(f)
            st.write(df.head())
            if st.button("Jalankan Audit"):
                st.info("Menganalisis anomali data...")

elif menu == "📝 Meeting Lab":
    st.title("📝 AI Meeting Lab")
    st.info("Fitur ringkuman rapat akan segera hadir.")
