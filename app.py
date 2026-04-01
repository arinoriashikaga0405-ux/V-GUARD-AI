import streamlit as st
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG & KEAMANAN ---
WHATSAPP_NUMBER = "6282122190885" 
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

# Database Sederhana untuk Lisensi Client Aktif (Contoh: Client ID)
# Bapak bisa menambah daftar ID di sini nanti
CLIENT_LICENSES = ["VGUARD-2026-001", "VGUARD-VIP-ERWIN", "VGUARD-PRO-JAYA"]

if 'auth_vguard' not in st.session_state:
    st.session_state['auth_vguard'] = False
if 'client_authenticated' not in st.session_state:
    st.session_state['client_authenticated'] = False

# --- 2. PREMIUM UI DESIGN ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #1e293b; border-right: 1px solid #334155; }
    .founder-name { text-align: center; font-weight: 800; font-size: 24px; color: white; margin-top: 10px; }
    .founder-title { text-align: center; color: #38bdf8; font-size: 14px; margin-top: -10px; font-weight: 500; }
    .product-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 25px; border-radius: 20px; border: 1px solid #334155; height: 100%;
    }
    .price-tag { color: #34d399; font-size: 24px; font-weight: bold; }
    .wa-btn {
        display: block; text-align: center; background-color: #059669; color: white !important;
        padding: 12px; border-radius: 12px; text-decoration: none; font-weight: bold;
    }
    .visi-teks { line-height: 1.8; text-align: justify; color: #cbd5e1; }
    .locked-card { 
        background-color: #1e293b; padding: 40px; border-radius: 15px; 
        border: 2px dashed #334155; text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_column_width=True)
    
    st.markdown('<p class="founder-name">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p class="founder-title">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.divider()

    nav_options = ["🏠 Home", "📦 Produk & Investasi", "🔑 Portal Klien", "🔐 Admin Panel"]
    if st.session_state['auth_vguard']:
        nav_options.insert(1, "🧠 Ekosistem 9 AI Engine")

    menu = st.radio("NAVIGASI SISTEM:", nav_options)
    st.divider()
    st.markdown("### 🤖 V-Guard NLP Bot")
    st.text_input("Interaksi Teks...", placeholder="Cek audit hari ini?")

# --- FUNGSI WHATSAPP ---
def get_wa_url(paket, harga):
    msg = f"Halo Pak Erwin, saya ingin daftar V-Guard paket {paket} (Investasi {harga})."
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={msg.replace(' ', '%20')}"

# --- 📂 FOLDER 1: HOME (VISI MISI UTUH) ---
if menu == "🏠 Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.subheader("Digitizing Trust, Eliminating Leakage")
    st.divider()
    
    col_a, col_b = st.columns([1, 2])
    with col_a:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_column_width=True)
    
    with col_b:
        st.header("Visi & Misi")
        st.markdown("""
        <div class="visi-teks">
        Sebagai seorang <b>Senior Business Leader</b> dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, 
        saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi, melainkan <b>ketidakpastian data dan kebocoran internal</b>. 
        Di dunia digital yang serba cepat ini, kepercayaan (trust) tidak lagi cukup jika hanya berdasarkan janji atau intuisi; 
        kepercayaan harus bisa diukur, diverifikasi, dan didigitalisasi. Inilah alasan utama saya mendirikan <b>V-Guard AI Intelligence</b>.<br><br>

        Visi kami adalah menjadi standar global dalam <b>Digital Trust</b>. Kami percaya bahwa setiap pemilik bisnis—mulai dari tokoh retail 
        mandiri (V-LITE) hingga korporasi multinasional (V-ENTERPRISE)—berhak mendapatkan transparansi mutlak atas aset mereka. 
        Melalui prinsip <b>'Digitizing Trust'</b>, kami mengubah setiap titik data mentah dari CCTV, mesin kasir (POS), laporan stok gudang (VCS), 
        dan mutasi bank menjadi bukti otentik yang tidak dapat dimanipulasi oleh siapa pun.<br><br>

        Misi utama kami, <b>'Eliminating Leakage'</b>, dijalankan dengan mengorkestrasikan 9 platform AI tercanggih di dunia (termasuk Gemini, 
        MindBridge, dan YOLO). Kami tidak hanya mendeteksi kecurangan (fraud) setelah terjadi, tetapi kami membangun benteng pertahanan 
        prediktif untuk menghentikan pola kebocoran sebelum menjadi kerugian finansial yang signifikan. Dengan V-Guard AI, kami mengembalikan 
        kendali penuh ke tangan pemilik usaha, memberikan ketenangan pikiran (<i>peace of mind</i>), dan memastikan setiap rupiah yang Anda investasikan 
        bekerja secara jujur dan optimal untuk masa depan bisnis Anda.
        </div>
        """, unsafe_allow_html=True)
        st.caption("— **Erwin Sinaga**, Founder V-Guard AI Intelligence")

# --- 📂 FOLDER 2: PRODUK ---
elif menu == "📦 Produk & Investasi":
    st.title("🛡️ 4 Produk Utama V-Guard")
    p1, p2, p3, p4 = st.columns(4)
    products = [
        ("V-LITE", "1.5M", "250rb", "• AI Fraud Dasar<br>• Laporan PDF WA"),
        ("V-PRO", "3.5M", "750rb", "• Real-Time Monitor<br>• VCS Automate"),
        ("V-SIGHT", "5.0M", "1.2jt", "• Behavior Visual<br>• Video Audit Struk"),
        ("V-ENTERPRISE", "CUSTOM", "Custom", "• Multi-Cabang Central<br>• Custom ERP")
    ]
    cols = [p1, p2, p3, p4]
    for i, (name, price, monthly, desc) in enumerate(products):
        with cols[i]:
            st.markdown(f'<div class="product-card"><h3>{name}</h3><div class="price-tag">Rp {price}</div><small>Bulanan: {monthly}</small><hr><p style="font-size:12px; color:#cbd5e1;">{desc}</p><br><a href="{get_wa_url(name, price)}" class="wa-btn">Daftar Sekarang</a></div>', unsafe_allow_html=True)

# --- 📂 FOLDER 3: PORTAL KLIEN (TERKUNCI) ---
elif menu == "🔑 Portal Klien":
    st.title("🔑 Portal Khusus Pelanggan")
    
    tab_reg, tab_active = st.tabs(["📝 Pendaftaran Baru", "🔓 Akses Client Aktif"])
    
    with tab_reg:
        st.subheader("Form Aktivasi Layanan")
        c_p1, c_p2 = st.columns(2)
        with c_p1:
            st.text_input("Nama Lengkap Pelanggan", key="reg_nama")
            st.text_input("Nama Bisnis / Toko", key="reg_bisnis")
        with c_p2:
            st.selectbox("Paket yang Dipilih", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.text_input("Harga Investasi (Rp)", key="reg_harga")
        if st.button("🚀 Kirim Data Pendaftaran"):
            st.success("Data diterima. Admin akan memberikan ID Lisensi setelah pembayaran diverifikasi.")

    with tab_active:
        if not st.session_state['client_authenticated']:
            st.markdown("""
            <div class="locked-card">
                <h2 style="color:#64ffda;">🔓 Area Terproteksi</h2>
                <p>Khusus pelanggan yang sudah melakukan pembayaran.<br>Masukkan ID Lisensi V-Guard Anda untuk membuka dashboard audit AI.</p>
            </div>
            """, unsafe_allow_html=True)
            
            client_key = st.text_input("Masukkan ID Lisensi Pelanggan", type="password")
            if st.button("Buka Dashboard"):
                if client_key in CLIENT_LICENSES:
                    st.session_state['client_authenticated'] = True
                    st.rerun()
                else:
                    st.error("ID Lisensi tidak valid atau belum aktif. Hubungi Admin Pak Erwin.")
        else:
            st.success("✅ Akses Diterima. Selamat Datang di Dashboard Audit Anda.")
            st.subheader("📊 Laporan Real-Time & Audit AI")
            st.info("Menampilkan hasil orkestrasi 9 Engine AI untuk bisnis Anda.")
            # Di sini nanti bisa Bapak isi dengan dashboard grafik atau hasil audit
            if st.button("🔒 Keluar Dashboard"):
                st.session_state['client_authenticated'] = False
                st.rerun()

# --- 📂 FOLDER 4: ADMIN PANEL ---
elif menu == "🔐 Admin Panel":
    st.header("🔐 CEO Command Center")
    if not st.session_state['auth_vguard']:
        pwd = st.text_input("Sandi Founder", type="password")
        if st.button("Login Admin"):
            if hashlib.sha256(pwd.encode()).hexdigest() == ADMIN_PWD_HASH:
                st.session_state['auth_vguard'] = True
                st.rerun()
            else: st.error("Akses Ditolak.")
    else:
        st.success("Selamat Datang, Pak Erwin.")
        st.subheader("📁 Folder Internal: Kirim ke Engine AI")
        with st.expander("Klik untuk Proses Audit Client"):
            st.file_uploader("Upload Data (VCS/Excel)", type=['csv','xlsx'])
            if st.button("🚀 JALANKAN AUDIT"): st.info("Memproses...")
        
        if st.button("Logout Admin"):
            st.session_state['auth_vguard'] = False
            st.rerun()

st.divider()
st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI | @{datetime.now().year} | Erwin Sinaga</p>', unsafe_allow_html=True)
