import streamlit as st
import os
from PIL import Image

# 1. KONFIGURASI DASAR
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# INITIAL DATABASE (Pastikan data paket ada di sini)
if 'role' not in st.session_state: st.session_state.role = None
if 'user_name' not in st.session_state: st.session_state.user_name = "Visitor"
if 'user_id' not in st.session_state: st.session_state.user_id = None
if 'db_klien' not in st.session_state:
    st.session_state.db_klien = {
        "klien_demo": {"paket": "V-LITE", "tagihan": 7500000, "due": "2026-04-05"}
    }

def get_foto(lebar):
    url_default = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    if os.path.exists('erwin.jpg'):
        try: return st.image(Image.open('erwin.jpg'), width=lebar)
        except: return st.image(url_default, width=lebar)
    return st.image(url_default, width=lebar)

# 2. CSS FIX (Kunci Warna & Box)
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    /* Box Hitam Utama */
    .vguard-card {
        background-color: #0e1117 !important;
        color: white !important;
        padding: 25px;
        border-radius: 15px;
        border-left: 10px solid #FFD700;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    .vguard-header {
        background: #0e1117;
        padding: 35px;
        border-radius: 12px;
        color: white;
        text-align: center;
        border-bottom: 5px solid #FFD700;
        margin-bottom: 30px;
    }
    h1, h2, h3 { color: white !important; margin-bottom: 10px !important; }
    p, li { color: #e0e0e0 !important; line-height: 1.6; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='color:#FFD700;'>🛡️ V-GUARD</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1: get_foto(65)
    with c2: st.markdown(f"<b style='color:white;'>{st.session_state.user_name}</b>", unsafe_allow_html=True)
    st.divider()
    
    if st.session_state.role == "admin":
        menu = st.radio("NAVIGASI:", ["🌐 Beranda", "👥 Management Klien", "🤖 AI Fraud Scanner"])
    elif st.session_state.role == "klien":
        menu = st.radio("NAVIGASI:", ["🌐 Beranda", "📅 Invoice & Payment"])
    else:
        menu = st.radio("NAVIGASI:", ["🌐 Beranda", "🔑 Masuk Ke Sistem"])

    if st.session_state.role and st.button("🚪 Logout"):
        st.session_state.role = None
        st.session_state.user_name = "Visitor"
        st.rerun()

# 4. HALAMAN BERANDA
if menu == "🌐 Beranda":
    st.markdown('<div class="vguard-header"><h1>V-GUARD AI SYSTEMS</h1><p style="color:#FFD700;">Mencegah Kerugian Owner Melalui Deteksi Proaktif</p></div>', unsafe_allow_html=True)
    
    col_foto, col_teks = st.columns([1.2, 1.8])
    with col_foto:
        get_foto(400)
    with col_teks:
        # Menggunakan Container Markdown untuk memastikan teks masuk ke dalam box
        with st.container():
            st.markdown(f"""
            <div class="vguard-card">
                <h2 style="color:#FFD700;">🛡️ About V-GUARD</h2>
                <p>Platform deteksi fraud sistemik yang dibangun oleh <b>Erwin Sinaga</b> (Senior Business Executive).</p>
                <p>Pengalaman perbankan 10+ tahun kami gunakan untuk memproteksi aset bisnis Anda dari kebocoran hingga 90%.</p>
                <hr style="border-color: #444;">
                <h3 style="color:#FFD700;">Filosofi</h3>
                <p>Kami memastikan setiap rupiah aset Anda terlindungi dengan standar keamanan tinggi dan audit AI proaktif.</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    st.subheader("📊 Kalkulator ROI Fraud")
    omset = st.number_input("Omset Bulanan Bisnis (Rp):", value=100000000)
    st.metric("Potensi Aset Terselamatkan /Bulan", f"Rp {omset * 0.027:,.0f}")

# 5. LOGIN SYSTEM
elif menu == "🔑 Masuk Ke Sistem":
    st.markdown('<div class="vguard-header"><h1>SECURITY LOGIN</h1></div>', unsafe_allow_html=True)
    with st.form("login_box"):
        u = st.text_input("User ID").lower().strip()
        p = st.text_input("Access Key", type="password")
        if st.form_submit_button("AUTHENTICATE"):
            if u == "admin" and p == "Vguard2026":
                st.session_state.role, st.session_state.user_name = "admin", "Erwin Sinaga"
                st.rerun()
            elif u in st.session_state.db_klien and p == "User2026":
                st.session_state.role, st.session_state.user_id, st.session_state.user_name = "klien", u, u.upper()
                st.rerun()
            else: st.error("Akses Ditolak.")

# 6. INVOICE & PAYMENT (Perbaikan Kotak Paket)
elif menu == "📅 Invoice & Payment":
    st.markdown('<div class="vguard-header"><h1>DASHBOARD TAGIHAN</h1></div>', unsafe_allow_html=True)
    uid = st.session_state.user_id
    if uid in st.session_state.db_klien:
        info = st.session_state.db_klien[uid]
        # Menggunakan format box yang sama dengan About
        st.markdown(f"""
        <div class="vguard-card">
            <h2 style="color:#FFD700;">Detail Layanan: {uid.upper()}</h2>
            <p><b>Jenis Paket:</b> {info['paket']}</p>
            <p><b>Total Tagihan:</b> Rp {info['tagihan']:,}</p>
            <p><b>Jatuh Tempo:</b> {info['due']}</p>
            <hr style="border-color: #444;">
            <p style="font-size: 0.9em; color: #FFD700;">Silakan lakukan pembayaran melalui transfer bank untuk menjaga aktivasi AI Scanner.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Data klien tidak ditemukan.")

elif menu == "👥 Management Klien":
    st.title("👥 Management Klien")
    st.write("Fitur kelola data klien.")

elif menu == "🤖 AI Fraud Scanner":
    st.title("🤖 AI Fraud Scanner")
    st.file_uploader("Unggah data transaksi")
