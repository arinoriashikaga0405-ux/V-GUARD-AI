import streamlit as st
from PIL import Image

# 1. Pastikan Streamlit di-import dengan benar
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# 2. FUNGSI UNTUK MENAMPILKAN FOTO BAPAK
def tampilkan_foto(lebar):
    try:
        # Ganti 'foto_erwin.jpg' sesuai nama file foto yang Bapak upload di GitHub
        img = Image.open('foto_erwin.jpg') 
        st.image(img, width=lebar)
    except:
        # Jika foto belum ketemu, muncul ikon standar dulu supaya tidak error
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)

# 3. SIDEBAR (MENU SAMPING)
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD MENU")
    tampilkan_foto(120) # Muncul di sidebar
    st.markdown("<center><b>Erwin Sinaga</b><br>Founder V-GUARD</center>", unsafe_allow_html=True)
    st.divider()
    halaman = st.radio("Pilih Halaman:", ["🌐 Landing Page", "👥 Area Klien", "🔐 Admin"])

# 4. HALAMAN UTAMA
if halaman == "🌐 Landing Page":
    st.markdown("<h1 style='text-align: center;'>V-GUARD AI SYSTEMS</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        tampilkan_foto(300) # Muncul foto besar di Landing Page
    with col2:
        st.markdown("## Profil & Filosofi")
        st.write("V-GUARD adalah sistem audit AI masa depan untuk mengamankan aset bisnis Anda.")
        st.info("Founder: Erwin Sinaga - Senior Business Leader (Tangerang)")

# Silakan lanjutkan kode halaman lainnya di bawah sini...
