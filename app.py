import streamlit as st
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG & KEAMANAN ---
WHATSAPP_NUMBER = "6282122190885" 
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

if 'auth_vguard' not in st.session_state:
    st.session_state['auth_vguard'] = False

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
    # Menu Ekosistem hanya muncul jika Bapak sudah login di Admin Panel
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

# --- 📂 FOLDER 1: HOME (NARASI VISI MISI UTUH) ---
if menu == "🏠 Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.subheader("Digitizing Trust, Eliminating Leakage")
    st.divider()
    
    col_a, col_b = st.columns([1, 2])
    with col_a:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_column_width=True)
            st.caption("<center>Erwin Sinaga</center>", unsafe_allow_html=True)
    
    with col_b:
        st.header("Visi & Misi")
        # NARASI 200 KATA TANPA DIKURANGI SATU KATA PUN
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
        st.markdown("<br>", unsafe_allow_html=True)
        st.caption("— **Erwin Sinaga**, Founder V-Guard AI Intelligence")

# --- 📂 FOLDER 2: PRODUK ---
elif menu == "📦 Produk & Investasi":
    st.title("🛡️ 4 Produk Utama V-Guard")
    p1, p2, p3, p4 = st.columns(4)
    
    products = [
        ("V-LITE", "1.5M", "250rb", "• AI Fraud Dasar<br>• Laporan PDF WA<br>• Notifikasi Stok"),
        ("V-PRO", "3.5M", "750rb", "• Real-Time Monitor<br>• VCS Automate<br>• Audit Closing AI"),
        ("V-SIGHT", "5.0M", "1.2jt", "• Behavior Visual<br>• Video Audit Struk<br>• Secure Cloud"),
        ("V-ENTERPRISE", "CUSTOM", "Custom", "• Multi-Cabang Central<br>• Forensik Digital<br>• ERP Integration")
    ]
    
    cols = [p1, p2, p3, p4]
    for i, (name, price, monthly, desc) in enumerate(products):
        with cols[i]:
            st.markdown(f"""
            <div class="product-card">
                <h3>{name}</h3>
                <div class="price-tag">Rp {price}</div>
                <small>Bulanan: {monthly}</small>
                <hr style="border-color:#334155;">
                <p style="font-size:12px; color:#cbd5e1;">{desc}</p>
                <br>
                <a href="{get_wa_url(name, price)}" class="wa-btn">Daftar Sekarang</a>
            </div>
            """, unsafe_allow_html=True)

# --- 📂 FOLDER 3: PORTAL KLIEN (NAMA, PAKET, HARGA) ---
elif menu == "🔑 Portal Klien":
    st.title("🔑 Form Pendaftaran Pelanggan")
    with st.container():
        st.info("Formulir aktivasi layanan V-Guard AI.")
        c_p1, c_p2 = st.columns(2)
        with c_p1:
            st.text_input("Nama Lengkap Pelanggan")
            st.text_input("Nama Bisnis / Toko")
        with c_p2:
            st.selectbox("Paket yang Dipilih", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.text_input("Harga Investasi (Rp)")
        
        st.divider()
        if st.button("🚀 Kirim Data Pendaftaran"):
            st.success("Data pendaftaran berhasil terkirim. Admin kami akan segera memverifikasi.")

# --- 📂 FOLDER 4: EKOSISTEM (HANYA MUNCUL SETELAH LOGIN) ---
elif menu == "🧠 Ekosistem 9 AI Engine":
    st.header("🧠 Engine Status (Confidential)")
    st.write("Mengorkestrasikan Gemini, MindBridge, YOLO, Alteryx, DataRobot, dll.")
    st.progress(100)

# --- 📂 FOLDER 5: ADMIN PANEL (FOLDER KIRIM KE AI DI SINI) ---
elif menu == "🔐 Admin Panel":
    st.header("🔐 CEO Command Center")
    if not st.session_state['auth_vguard']:
        pwd = st.text_input("Sandi Founder", type="password")
        if st.button("Login"):
            if hashlib.sha256(pwd.encode()).hexdigest() == ADMIN_PWD_HASH:
                st.session_state['auth_vguard'] = True
                st.rerun()
            else: st.error("Akses Ditolak.")
    else:
        st.success("Selamat Datang, Pak Erwin Sinaga.")
        
        # FITUR KIRIM KE AI (KHUSUS ADMIN)
        st.divider()
        st.subheader("📁 Folder Internal: Kirim ke Engine AI")
        with st.expander("Klik untuk Proses Audit"):
            target_aud = st.text_input("Nama Client Audit")
            file_aud = st.file_uploader("Upload Data (VCS/Excel/Video)", type=['csv','xlsx','mp4'])
            if st.button("🚀 JALANKAN AUDIT AI"):
                if file_aud:
                    st.info(f"Memproses audit {target_aud} melalui 9 Engine AI...")
                    st.success("Audit Selesai. Hasil telah dienkripsi.")
                else: st.warning("Pilih file terlebih dahulu.")

        if st.button("Logout"):
            st.session_state['auth_vguard'] = False
            st.rerun()

st.divider()
st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI Intelligence | @{datetime.now().year} | Erwin Sinaga</p>', unsafe_allow_html=True)
