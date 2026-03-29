import streamlit as st
import os
from PIL import Image

# ==========================================
# 1. KONFIGURASI HALAMAN & LAYOUT (WAJIB PADA BARIS PERTAMA)
# ==========================================
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# INITIAL DATABASE SIMULATION
if 'role' not in st.session_state: st.session_state.role = None
if 'user_name' not in st.session_state: st.session_state.user_name = "Visitor"
if 'user_id' not in st.session_state: st.session_state.user_id = None
if 'db_klien' not in st.session_state:
    st.session_state.db_klien = {
        "klien_demo": {"paket": "V-LITE", "tagihan": 7500000, "due": "2026-04-05"}
    }

# FUNGSI PEMANGGIL FOTO (MEMASTIKAN FOTO TAMPIL TEPAT)
def get_foto(lebar, caption=None):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try: 
            img = Image.open('erwin.jpg')
            return st.image(img, width=lebar, caption=caption)
        except: return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# ==========================================
# 2. CSS STYLING: MENGIKUTI GAMBAR BAPAK (PRESTISIUS BLACK & GOLD)
# ==========================================
st.markdown("""
<style>
    /* Mengatur latar belakang halaman utama agar bersih */
    .stApp { background-color: #f4f6f9; }
    
    /* SIDEBAR: Menyamakan persis dengan warna hitam di gambar Bapak */
    [data-testid="stSidebar"] { 
        background-color: #0e1117 !important; 
        border-right: 2px solid #FFD700; 
        padding-top: 20px;
    }
    
    /* HERO HEADER: Spanduk atas warna hitam dengan garis emas */
    .hero-bg { 
        background-color: #0e1117; 
        padding: 50px 20px; 
        border-radius: 15px; 
        color: white; 
        text-align: center; 
        border-bottom: 5px solid #FFD700; 
        margin-bottom: 30px; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .hero-bg h1 { color: white; font-size: 3em; font-weight: bold; margin-bottom: 10px; }
    .hero-bg p { color: #FFD700; font-size: 1.2em; }

    /* Kotak About V-GUARD di kanan: Hitam dengan garis emas */
    .bio-section { 
        background-color: #0e1117; 
        color: white; 
        padding: 30px; 
        border-radius: 15px; 
        border-left: 8px solid #FFD700; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-top: 20px;
    }
    .bio-section h2 { color: #FFD700; margin-bottom: 15px; }

    /* Gaya Kalkulator ROI */
    .roi-section {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-top: 30px;
    }

    /* Red Alert Area */
    .red-alert { 
        background-color: #ff4b4b; 
        color: white; 
        padding: 20px; 
        border-radius: 10px; 
        border: 4px solid black; 
        text-align: center; 
        font-weight: bold; 
        animation: blinker 1.5s linear infinite; 
    }
    @keyframes blinker { 50% { opacity: 0.3; } }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. SIDEBAR NAVIGATION: MENYEMPURNAKAN TAMPILAN GAMBAR
# ==========================================
with st.sidebar:
    # Mengelompokkan logo dan status agar rapi di sidebar hitam
    col_logo, col_status = st.columns([1, 2])
    with col_logo:
        get_foto(80) # Foto profil kecil di sidebar
    with col_status:
        st.markdown(f"<b style='color:white; font-size: 1.2em;'>🛡️ V-GUARD</b><br><small style='color:#FFD700;'>{st.session_state.user_name}</small><br><small style='color:white;'>V-GUARD Ecosystem</small>", unsafe_allow_html=True)
    
    st.divider()
    
    # Navigasi Dinamis
    if st.session_state.role == "admin":
        menu = st.radio("FOUNDER MENU:", ["🌐 Beranda", "👥 Management Klien", "🤖 AI Fraud Scanner"])
    elif st.session_state.role == "klien":
        menu = st.radio("CLIENT DASHBOARD:", ["🌐 Beranda", "📅 Invoice & Payment"])
    else:
        # Menyamakan menu Visitor seperti di gambar Bapak
        menu = st.radio("VISITOR MENU:", ["🌐 Beranda", "🔑 Masuk Ke Sistem"])

    # Tombol Logout yang bersih
    if st.session_state.role and st.button("🚪 Logout", key="logout_btn"):
        st.session_state.role = None
        st.session_state.user_name = "Visitor"
        st.rerun()

# ==========================================
# 4. HALAMAN BERANDA (MENGEMBALIKAN LAYOUT PERSIS GAMBAR)
# ==========================================
if menu == "🌐 Beranda":
    # HEADER UTAMA (Spanduk Hitam Atas)
    st.markdown("""
    <div class="hero-bg">
        <h1>V-GUARD AI SYSTEMS</h1>
        <p>Mencegah Kerugian Owner Melalui Deteksi Proaktif</p>
    </div>
    """, unsafe_allow_html=True)
    
    # SECTION TENGAH: Foto Besar di Kiri, Teks di Kanan (MENGGUNAKAN COLUMNS YANG BENAR)
    col_foto, col_teks = st.columns([1.2, 1.8], gap="large")
    
    with col_foto:
        # Menampilkan foto besar Bapak yang ada di gambar (caption ditiadakan agar bersih)
        get_foto(420) 
        
    with col_teks:
        # Kotak About V-GUARD warna hitam dengan garis emas
        st.markdown("""
        <div class="bio-section">
            <h2>🛡️ About V-GUARD</h2>
            <p style="font-size: 1.1em; line-height: 1.7;">
                V-GUARD adalah platform deteksi fraud sistemik yang dibangun oleh <b>Erwin Sinaga</b> (Senior Business Executive). 
                Pengalaman perbankan 10+ tahun kami gunakan untuk memproteksi aset bisnis Anda dari kebocoran hingga 90%.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # SECTION BAWAH: Kalkulator ROI
    st.markdown('<div class="roi-section">', unsafe_allow_html=True)
    st.subheader("📊 Kalkulator ROI Fraud")
    
    c_omset, c_saved = st.columns(2, gap="medium")
    with c_omset:
        omset = st.number_input("Omset Bulanan Bisnis (Rp):", value=100000000, step=10000000)
    with c_saved:
        saved = omset * 0.027 # Estimasi 2.7%
        st.metric("Potensi Aset Terselamatkan /Bulan", f"Rp {saved:,.0f}", delta="90% Proteksi AI")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 5. HALAMAN LOGIN
# ==========================================
elif menu == "🔑 Masuk Ke Sistem":
    st.markdown('<div class="hero-bg"><h1>SECURITY LOGIN</h1><p>Masuk ke Founder Command Center</p></div>', unsafe_allow_html=True)
    
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
                st.error("Akses Ditolak. Periksa ID dan Key Bapak.")

# ==========================================
# 6. FITUR ADMIN (HANYA BISA DIAKSES OLEH BAPAK SEBAGAI ADMIN)
# ==========================================
elif menu == "👥 Management Klien":
    st.title("👥 Management Klien")
    new_u = st.text_input("User ID Klien Baru:")
    if st.button("Daftarkan"):
        st.session_state.db_klien[new_u] = {"paket": "V-START", "tagihan": 5000000, "due": "2026-05-01"}
        st.success(f"User {new_u} Berhasil Terdaftar!")

elif menu == "🤖 AI Fraud Scanner":
    st.markdown('<div class="red-alert">🚨 ALARM MERAH: SISTEM SIAP ANALISIS 🚨</div>', unsafe_allow_html=True)
    st.file_uploader("Upload Data untuk Audit AI")

elif menu == "📅 Invoice & Payment":
    st.title("📅 Dashboard Tagihan")
    data = st.session_state.db_klien.get(st.session_state.user_id, {})
    if data:
        st.metric("Total Tagihan Aktif", f"Rp {data.get('tagihan', 0):,}")
        st.write(f"Paket: {data
