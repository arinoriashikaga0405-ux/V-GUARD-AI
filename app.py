import streamlit as st
import os
from PIL import Image

# 1. KONFIGURASI HALAMAN UTAMA (TERKUNCI)
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# INITIAL DATABASE SIMULATION
if 'role' not in st.session_state: st.session_state.role = None
if 'user_name' not in st.session_state: st.session_state.user_name = "Visitor"
if 'user_id' not in st.session_state: st.session_state.user_id = None
if 'db_klien' not in st.session_state:
    st.session_state.db_klien = {
        "klien_demo": {"paket": "V-LITE", "tagihan": 7500000, "due": "2026-04-05"}
    }

# FUNGSI FOTO PROFIL (SELALU PRIORITASKAN FOTO BAPAK)
def get_foto(lebar, caption=None):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try: 
            img = Image.open('erwin.jpg')
            return st.image(img, width=lebar, caption=caption)
        except: return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# ==========================================
# 2. CSS STYLING PRESTISIUS (BLACK & GOLD)
# ==========================================
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    .hero-bg { background-color: #0e1117; padding: 40px; border-radius: 12px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    .hero-bg h1 { color: white; font-size: 3em; margin-bottom: 10px; }
    .hero-bg p { color: #FFD700; font-size: 1.2em; }
    .bio-section { background-color: #0e1117; color: white; padding: 30px; border-radius: 15px; border-left: 8px solid #FFD700; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. SIDEBAR NAVIGATION
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='color: #FFD700; text-align:center;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    f_col, n_col = st.columns([1, 2])
    with f_col:
        get_foto(70) # Foto profil kecil
    with n_col: 
        st.markdown(f"<b style='color:white; font-size: 1.2em;'>{st.session_state.user_name}</b>", unsafe_allow_html=True)
        st.markdown("<small style='color:#FFD700; font-weight:bold;'>FOUNDER - CEO</small>", unsafe_allow_html=True)
    st.divider()
    
    # Navigasi Dinamis
    if st.session_state.role == "admin":
        menu = st.radio("FOUNDER MENU:", ["🌐 Beranda", "👥 Management Klien", "🤖 AI Fraud Scanner"])
    elif st.session_state.role == "klien":
        menu = st.radio("CLIENT DASHBOARD:", ["🌐 Beranda", "📅 Invoice & Payment"])
    else:
        menu = st.radio("VISITOR MENU:", ["🌐 Beranda", "🔑 Masuk Ke Sistem"])

    if st.session_state.role and st.button("🚪 Logout", key="logout_btn"):
        st.session_state.role = None
        st.session_state.user_name = "Visitor"
        st.session_state.user_id = None
        st.rerun()

# ==========================================
# 4. HALAMAN BERANDA (STATE LOCKED - SELALU RAPI)
# ==========================================
if menu == "🌐 Beranda":
    # Header Utama (Banner Hitam Atas)
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Mencegah Kerugian Owner Melalui Deteksi Proaktif</p></div>', unsafe_allow_html=True)
    
    # Section Tengah: Foto Besar di Kiri, About & Filosofi di Kanan (MENGGUNAKAN COLUMNS YANG BENAR)
    col_foto, col_teks = st.columns([1.2, 1.8])
    
    with col_foto:
        # Menampilkan foto besar Bapak yang ada di gambar (menggunakan lebar 420 agar besar dan gagah)
        get_foto(420) 
        
    with col_teks:
        # Kotak About V-GUARD & Filosofi (Hitam dengan garis emas)
        st.markdown(f"""
        <div class="bio-section">
            <h2 style="color:#FFD700;">🛡️ About V-GUARD</h2>
            <p style="font-size: 1.1em; line-height: 1.7;">
                V-GUARD adalah platform deteksi fraud sistemik yang dibangun oleh <b>Erwin Sinaga</b> (Senior Business Executive). 
                Pengalaman perbankan 10+ tahun kami gunakan untuk memproteksi aset bisnis Anda dari kebocoran hingga 90%.
            </p>
            <hr style="border-color: #444;">
            <h3 style="color:#FFD700;">Filosofi V-GUARD</h3>
            <p style="font-size: 1em;">
                Dengan pengalaman perbankan lebih dari 10 tahun, kami memastikan setiap rupiah aset Anda terlindungi. 
                Sistem kami dirancang untuk memberikan <b>Alarm Merah</b> seketika saat kecurangan terdeteksi.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Kalkulator ROI (Bagian Bawah)
    st.subheader("📈 Kalkulator ROI Fraud")
    col_1, col_2 = st.columns(2)
    with col_1:
        omset = st.number_input("Omset Bulanan Bisnis (Rp):", value=100000000, step=10000000)
    with col_2:
        saved = omset * 0.027 # Estimasi 2.7%
        st.metric("Potensi Aset Terselamatkan /Bulan", f"Rp {saved:,.0f}", delta="90% Proteksi AI")

# ==========================================
# 5. HALAMAN LOGIN
# ==========================================
elif menu == "🔑 Masuk Ke Sistem":
    st.markdown('<div class="hero-bg"><h1>SECURITY LOGIN</h1></div>', unsafe_allow_html=True)
    with st.form("login_form"):
        u = st.text_input("User ID").lower().strip()
        p = st.text_input("Access Key", type="password")
        if st.form_submit_button("AUTHENTICATE"):
            if u == "admin" and p == "Vguard2026":
                st.session_state.role, st.session_state.user_name = "admin", "Erwin Sinaga"
                st.rerun()
            elif u in st.session_state.db_klien and p == "User2026":
                st.session_state.role, st.session_state.user_id, st.session_state.user_name = "klien", u, u.upper()
                st.rerun()
            else:
                st.error("User ID atau Password Salah.")

# ==========================================
# 6. FITUR ADMIN (Management Klien & Scanner)
# ==========================================
