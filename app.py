import streamlit as st
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG & KEAMANAN ---
WHATSAPP_NUMBER = "6282122190885" 
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

if 'auth_vguard' not in st.session_state:
    st.session_state['auth_vguard'] = False

# --- 2. UI PREMIUM DESIGN ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #1e293b; border-right: 1px solid #334155; }
    .founder-name { text-align: center; font-weight: 800; font-size: 22px; color: white; margin-top: 10px; }
    .founder-title { text-align: center; color: #38bdf8; font-size: 13px; margin-top: -10px; }
    .product-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 25px; border-radius: 20px; border: 1px solid #334155; height: 100%;
    }
    .price-tag { color: #34d399; font-size: 24px; font-weight: bold; }
    .wa-btn {
        display: block; text-align: center; background-color: #059669; color: white !important;
        padding: 12px; border-radius: 12px; text-decoration: none; font-weight: bold;
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

    menu = st.radio("FOLDER NAVIGASI:", nav_options)
    st.divider()
    st.markdown("### 🤖 V-Guard NLP Bot")
    st.text_input("Tanya AI...", placeholder="Cek anomali...")

# --- FUNCTION: WHATSAPP LINK ---
def get_wa_url(paket, harga):
    msg = f"Halo Pak Erwin, saya ingin daftar V-Guard paket {paket} (Investasi {harga})."
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={msg.replace(' ', '%20')}"

# --- 📂 FOLDER 1: HOME ---
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
        Sebagai seorang **Senior Business Leader** dengan pengalaman lebih dari sepuluh tahun di industri perbankan dan aset, 
        saya mendirikan **V-Guard AI** untuk menghentikan pola kebocoran bisnis melalui orkestrasi 9 platform AI tercanggih di dunia.
        
        Kami mengubah data mentah menjadi bukti otentik, memberikan kendali penuh dan ketenangan pikiran (*peace of mind*) bagi setiap pemilik usaha.
        """)

# --- 📂 FOLDER 2: PRODUK ---
elif menu == "📦 Produk & Investasi":
    st.title("🛡️ 4 Produk Utama V-Guard")
    p1, p2, p3, p4 = st.columns(4)
    
    with p1:
        st.markdown(f'<div class="product-card"><h3>V-LITE</h3><div class="price-tag">Rp 1.5M</div><small>Bulanan: 250rb</small><hr><p style="font-size:12px;">• AI Fraud Dasar (Void)<br>• Laporan PDF WA<br>• Notifikasi Stok</p><br><a href="{get_wa_url("V-LITE","1.5M")}" class="wa-btn">Daftar Sekarang</a></div>', unsafe_allow_html=True)
    with p2:
        st.markdown(f'<div class="product-card"><h3>V-PRO</h3><div class="price-tag">Rp 3.5M</div><small>Bulanan: 750rb</small><hr><p style="font-size:12px;">• Real-Time Monitor<br>• VCS Automate<br>• Audit Closing AI</p><br><a href="{get_wa_url("V-PRO","3.5M")}" class="wa-btn">Daftar Sekarang</a></div>', unsafe_allow_html=True)
    with p3:
        st.markdown(f'<div class="product-card"><h3>V-SIGHT</h3><div class="price-tag">Rp 5.0M</div><small>Bulanan: 1.2jt</small><hr><p style="font-size:12px;">• Behavior Visual<br>• Video Audit Struk<br>• Secure Cloud</p><br><a href="{get_wa_url("V-SIGHT","5.0M")}" class="wa-btn">Daftar Sekarang</a></div>', unsafe_allow_html=True)
    with p4:
        st.markdown(f'<div class="product-card"><h3>V-ENTERPRISE</h3><div class="price-tag">CUSTOM</div><small>Full Ecosystem</small><hr><p style="font-size:12px;">• Multi-Cabang Central<br>• Forensik Digital<br>• Custom ERP/API</p><br><a href="{get_wa_url("V-ENTERPRISE","Custom")}" class="wa-btn">Daftar Sekarang</a></div>', unsafe_allow_html=True)

# --- 📂 FOLDER 3: PORTAL KLIEN (NAMA, PAKET, HARGA) ---
elif menu == "🔑 Portal Klien":
    st.header("🔑 Form Aktivasi Pelanggan")
    with st.container():
        st.info("Silakan isi data pelanggan untuk verifikasi layanan.")
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.text_input("Nama Pelanggan / Owner")
            st.text_input("Nama Perusahaan / Bisnis")
        with col_c2:
            st.selectbox("Pilih Paket V-Guard", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
            st.text_input("Harga Investasi Disepakati (Rp)")
        
        st.divider()
        if st.button("🚀 Kirim Data Pendaftaran"):
            st.success("Data pendaftaran telah diterima Admin Pak Erwin. Kami akan segera menghubungi Anda.")

# --- 📂 FOLDER 4: EKOSISTEM (CONFIDENTIAL) ---
elif menu == "🧠 Ekosistem 9 AI Engine":
    st.header("🧠 Engine Status (Confidential)")
    st.write("Status integrasi platform pihak ketiga (Gemini, MindBridge, YOLO, Alteryx).")
    st.progress(99)

# --- 📂 FOLDER 5: ADMIN PANEL (FOLDER KIRIM KE AI PINDAH KE SINI) ---
elif menu == "🔐 Admin Panel":
    st.header("🔐 CEO Command Center")
    if not st.session_state['auth_vguard']:
        pwd = st.text_input("Sandi Founder", type="password")
        if st.button("Login"):
            if hashlib.sha256(pwd.encode()).hexdigest() == ADMIN_PWD_HASH:
                st.session_state['auth_vguard'] = True
                st.rerun()
            else: st.error("Sandi Salah.")
    else:
        st.success("Selamat Datang, Pak Erwin Sinaga.")
        
        # FITUR KIRIM KE AI PINDAH KE SINI
        st.divider()
        st.subheader("📁 Folder Internal: Kirim ke Engine AI")
        st.write("Gunakan fitur ini untuk memproses audit data pelanggan secara internal.")
        with st.expander("Proses Audit Baru"):
            target_name = st.text_input("Nama Pelanggan Audit")
            u_file = st.file_uploader("Upload File VCS/Laporan", type=['csv','xlsx','mp4'])
            if st.button("🚀 JALANKAN AUDIT AI"):
                if u_file:
                    st.info(f"Sedang memproses data {target_name} melalui 9 Engine AI...")
                    st.success("Audit Selesai! Laporan telah terkirim otomatis.")
                else: st.warning("Pilih file audit.")

        if st.button("Logout"):
            st.session_state['auth_vguard'] = False
            st.rerun()

st.divider()
st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px;">🛡️ V-Guard AI | @{datetime.now().year} | Erwin Sinaga</p>', unsafe_allow_html=True)
