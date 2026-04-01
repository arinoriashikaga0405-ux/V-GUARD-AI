import streamlit as st
from PIL import Image
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="V-Guard AI Intelligence - Digital Trust Solution",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INISIALISASI SESSION STATE ---
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'Dashboard Home'

def nav_page(page_name):
    st.session_state['current_page'] = page_name
    st.rerun()

# --- SIDEBAR ---
with st.sidebar:
    foto_path = "erwin.jpg" 
    
    # PERBAIKAN: Menggunakan try-except agar tidak error jika file rusak
    try:
        if os.path.exists(foto_path):
            img = Image.open(foto_path)
            st.image(img, use_container_width=True)
        else:
            st.warning("Foto 'erwin.jpg' tidak ditemukan.")
    except Exception:
        st.error("File 'erwin.jpg' rusak/tidak terbaca.")
        st.info("Silakan unggah ulang file foto erwin.jpg ke GitHub.")

    st.markdown(f"""
    <div style="text-align: center; color: white;">
        <h3 style="margin-bottom: 0px;">Erwin Sinaga</h3>
        <p style="color: #6d7d8e; margin-top: 0px;">Founder & CEO V-Guard AI</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<p style='color: #6d7d8e; font-size: 0.8rem; font-weight: bold;'>NAVIGASI UTAMA</p>", unsafe_allow_html=True)
    
    pages = [
        {"name": "Dashboard Home", "icon": "🏠"},
        {"name": "Layanan & Investasi", "icon": "💼"},
        {"name": "Portal Klien", "icon": "🔐"},
        {"name": "Admin Control Center", "icon": "⚙️"}
    ]
    
    for page in pages:
        if st.session_state['current_page'] == page["name"]:
            if st.button(f"{page['icon']} {page['name']}", key=page["name"], use_container_width=True, type="primary"):
                nav_page(page["name"])
        else:
            if st.button(f"{page['icon']} {page['name']}", key=page["name"], use_container_width=True):
                nav_page(page["name"])

# --- KONTEN UTAMA ---
st.markdown("""
<div style="display: flex; align-items: center; margin-bottom: 20px;">
    <img src="https://img.icons8.com/fluency/96/security-checked.png" alt="shield logo" width="50" style="margin-right: 15px;"/>
    <h1 style="margin: 0; font-weight: bold;">V-Guard AI Intelligence</h1>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

if st.session_state['current_page'] == 'Dashboard Home':
    st.header("Visi & Misi")
    
    st.markdown("""
    <p style="color: #6d7d8e; font-size: 1.1rem;">
    Sebagai seorang Senior Business Leader dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, 
    saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi, melainkan kepastian data dan kebocoran internal. 
    Di dunia digital yang serba cepat ini, kepercayaan (trust) tidak lagi cukup jika hanya berdasarkan janji atau intuisi; 
    kepercayaan harus bisa diukur, diverifikasi, dan didigitalisasi. Inilah alasan utama saya mendirikan V-Guard AI Intelligence.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    col_img, col_txt = st.columns([1, 2])
    
    with col_img:
        try:
            if os.path.exists("erwin.jpg"):
                st.image("erwin.jpg", use_container_width=True)
        except:
            pass # Melewati tampilan gambar jika file bermasalah

    with col_txt:
        st.subheader("🎯 Visi Kami")
        st.markdown("""
        <p style="color: #b0b3b8; line-height: 1.8;">
        Menjadi pemimpin global yang diakui dalam menginisiasi, mengembangkan, dan menerapkan solusi Digital Trust yang didukung 
        oleh Kecerdasan Buatan (AI). Kami menciptakan fondasi yang tidak dapat dipalsukan untuk transaksi digital yang aman, 
        transparan, dan otonom, sehingga memberdayakan bisnis di seluruh dunia untuk beroperasi dengan keyakinan mutlak 
        dalam integritas data mereka. Kami percaya bahwa setiap pemilik bisnis berhak mendapatkan transparansi mutlak atas aset mereka.
        </p>
        """, unsafe_allow_html=True)

        st.subheader("🚀 Misi Kami")
        st.markdown("""
        <p style="color: #b0b3b8; line-height: 1.8;">
        Misi kami adalah 'Eliminating Leakage', sebuah komitmen tak tergoyahkan untuk membangun benteng pertahanan digital yang 
        cerdas dan prediktif. Dengan memanfaatkan AI dan teknologi canggih, kami berdedikasi untuk secara proaktif mendeteksi, 
        memprediksi, dan menghentikan potensi kebocoran data sebelum menjadi kerugian finansial atau reputasi yang signifikan. 
        Kami mengubah integritas data menjadi aset strategis, serta memberdayakan pemilik bisnis dengan transparansi mutlak 
        melalui bukti otentik yang tidak dapat dimanipulasi di setiap lini operasional.
        </p>
        """, unsafe_allow_html=True)

elif st.session_state['current_page'] == 'Layanan & Investasi':
    st.header("Layanan & Investasi")
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Produk Layanan Utama")
        st.markdown("* 🛡️ V-Guard Core AI\n* 🔍 Data Integrity Audit\n* 🌐 Digital Trust API")
    with col4:
        st.subheader("Program Kemitraan")
        st.success("**Komisi 10%** untuk pemasaran yang berhasil.")
    st.markdown("---")
    st.subheader("Hubungi Kami")
    st.markdown(f"### 📞 WhatsApp: [0821-2219-0885](https://wa.me/6282122190885)")

# Halaman lain tetap sama tanpa perubahan
elif st.session_state['current_page'] == 'Portal Klien':
    st.header("Portal Klien")
    st.info("Fitur dalam pengembangan.")

elif st.session_state['current_page'] == 'Admin Control Center':
    st.header("Admin Control Center")
    st.warning("Area terbatas.")

# --- FOOTER ---
st.markdown("---")
st.markdown('<div style="text-align: center; color: #6d7d8e; font-size: 0.8rem;">🛡️ V-Guard AI | ©2026 | Founder: Erwin Sinaga</div>', unsafe_allow_html=True)
