import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from PIL import Image

# 1. KONFIGURASI UTAMA & SLOT API
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# --- TEMPELKAN API KEY BAPAK DI SINI ---
GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"

if GOOGLE_API_KEY != "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA":
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
# Cek apakah API Key sudah diisi (tidak kosong)
if GOOGLE_API_KEY and GOOGLE_API_KEY != "ISI_API_KEY_BAPAK_DI_SINI":
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
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

# 3. CSS DESIGN (Executive Style)
# GANTI CSS INI (Pada Bagian Konfigurasi CSS di atas kode Navigasi)
    .card-service { 
        background: white; 
        padding: 15px; # padding diperkecil
        border-radius: 12px; # radius lebih lancip
        box-shadow: 0 3px 10px rgba(0,0,0,0.08); # shadow lebih halus
        border-top: 4px solid #FFD700; # border diperkecil
        text-align: center; 
        height: 250px; # TINGGI DIPERKECIL DRASTIS (Sebelumnya ~400px)
        display: flex; 
        flex-direction: column; 
        justify-content: space-between;
        font-size: 13px; # UKURAN TULISAN DESKRIPSI DIPERKECIL
    }
    .card-service h4 { font-size: 16px; margin-bottom: 5px; } # Judul diperkecil
    .card-service h3 { font-size: 20px; color: #0e1117; margin: 10px 0; } # Harga diperkecil
    .card-service hr { margin: 10px 0; border: 0; border-top: 1px solid #eee; }
    .stLinkButton button { width: 100%; padding: 5px; font-size: 12px; } # Tombol diperkecil

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
# 5. HALAMAN BERANDA (PENJELASAN PAKET)
# ==========================================
if menu == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1><p>Revenue Protection Intelligence</p></div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(350)
    with c2:
        st.subheader("🛡️ Proteksi Aset & Deteksi Fraud")
        st.write("V-Guard hadir untuk menutup celah kebocoran operasional bisnis Anda dengan kecerdasan buatan.")
        st.markdown("<div class='roi-box'>", unsafe_allow_html=True)
        omset = st.number_input("Omset Bulanan (Rp):", value=100000000)
        leak = st.slider("Estimasi Kebocoran (%):", 0, 15, 3)
        st.markdown(f"<h4>Potensi Penyelamatan:</h4><h2 style='color:#d42f2f;'>Rp {omset*(leak/100):,.0f}</h2>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.divider()
    
    st.markdown("<h2 style='text-align:center;'>Pilihan Layanan Strategis</h2>", unsafe_allow_html=True)
    WA_LINK = "https://wa.me/6282122190885"
    
    # Baris 1
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="card-service"><h4>🌱 V-START</h4><h3>3,5 Jt</h3><hr><p align="left"><b>UMKM Mandiri</b><br>Audit mingguan otomatis untuk deteksi stok & kas secara general. Cocok untuk pemula.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA_LINK)
    with p2:
        st.markdown('<div class="card-service"><h4>📦 V-LITE</h4><h3>7,5 Jt</h3><hr><p align="left"><b>1 Outlet/Toko</b><br>Kontrol penuh harian tanpa harus di lokasi. Laporan audit harian via notifikasi WhatsApp.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA_LINK)
    with p3:
        st.markdown('<div class="card-service" style="border:3px solid #FFD700"><h4>🚀 V-PRO</h4><h3>15 Jt</h3><hr><p align="left"><b>Hingga 5 Outlet</b><br>AI Deep Fraud Audit untuk menganalisis perilaku kasir dan pola kebocoran antar cabang.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA_LINK)

    st.markdown("<br>", unsafe_allow_html=True)

    # Baris 2
    p4, p5 = st.columns(2)
    with p4:
        st.markdown('<div class="card-service"><h4>🏢 CORPORATE</h4><h3>25 Jt</h3><hr><p align="left"><b>Unlimited Outlet</b><br>Skalabilitas tanpa batas dengan review strategis bulanan dan dukungan prioritas teknis.</p></div>', unsafe_allow_html=True)
        st.link_button("AMBIL PAKET", WA_LINK)
    with p5:
        st.markdown('<div class="card-service" style="background-color: #0e1117; color: white;"><h4>💎 V-ENTERPRISE</h4><h3>Custom</h3><hr><p align="left"><b>Tailor-made Solution</b><br>Integrasi on-site, model AI khusus, dan pendampingan dedicated Data Scientist.</p></div>', unsafe_allow_html=True)
        st.link_button("HUBUNGI CEO", WA_LINK)

# ==========================================
# 6. HALAMAN MEETING LAB (AI AKTIF)
# ==========================================
elif menu == "📝 Meeting Lab":
    st.title("📝 AI Meeting Lab")
    st.write("AI akan merangkum poin strategis dari teks rapat Anda.")
    
    transkrip = st.text_area("Tempel transkrip rapat di sini:", height=300)
    
    if st.button("🚀 JALANKAN PROSES AI"):
        if not transkrip:
            st.warning("Masukkan teks terlebih dahulu.")
        elif GOOGLE_API_KEY == "ISI_API_KEY_BAPAK_DI_SINI":
            st.error("⚠️ API Key belum diisi di kode app.py!")
        else:
            with st.spinner("Sedang menganalisis strategis..."):
                try:
                    prompt = f"Rangkumlah transkrip rapat berikut menjadi poin strategis, action plan, dan mitigasi risiko: {transkrip}"
                    response = model.generate_content(prompt)
                    st.subheader("💡 Hasil Analisis Strategis V-GUARD")
                    st.info(response.text)
                except Exception as e:
                    st.error(f"Terjadi kesalahan pada API: {e}")

# HALAMAN LAIN (Dashboard Klien & Admin)
elif menu == "📊 Dashboard Klien":
    st.title("📊 Dashboard Laporan Klien")
    st.metric("Profit Aman", "Rp 158.000.000", "+8%")

elif menu == "🤖 AI Auditor (Admin)":
    st.title("🤖 AI Auditor (Admin)")
    st.file_uploader("Upload Transaksi untuk Audit AI")
