import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG: NOMOR WA BAPAK ---
WHATSAPP_NUMBER = "628123456789" # <--- GANTI DENGAN NOMOR WA ASLI BAPAK
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

# --- 2. SETUP TEMA PREMIUM ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0a192f; color: #e6f1ff; }
    .stButton>button { background-color: #25D366; color: white; border-radius: 20px; font-weight: bold; }
    .price-box { background-color: #112240; padding: 20px; border-radius: 15px; border: 1px solid #233554; text-align: center; }
    .price-tag { color: #64ffda; font-size: 24px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: FOTO FOUNDER DI ATAS ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Coba tampilkan foto erwin.jpg, jika gagal tampilkan ikon
    try:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", width=150)
        else:
            st.markdown("### 👨‍💼")
    except:
        st.markdown("### 🛡️")
        
    st.markdown("**Erwin Sinaga**")
    st.caption("Founder & CEO V-Guard AI")
    st.divider()

    menu = st.radio("Folder Navigasi:", ["🏠 Home", "📦 Produk & Harga", "🔑 Portal Klien", "🔐 Admin Panel"])

# --- FUNGSI PESAN WA ---
def wa_button(paket, harga):
    msg = f"Halo Pak Erwin, saya tertarik paket {paket} (Pasang: {harga}). Mohon infonya."
    url = f"https://wa.me/{WHATSAPP_NUMBER}?text={msg.replace(' ', '%20')}"
    st.markdown(f'[@ Hubungi WA Pak Erwin]({url})', unsafe_allow_html=True)

# --- 📂 HALAMAN 1: HOME ---
if menu == "🏠 Home":
    st.title("🛡️ V-Guard AI Intelligence")
    st.markdown("### Digitizing Trust, Eliminating Leakage")
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga", use_column_width=True)
        else:
            st.info("Unggah erwin.jpg ke GitHub untuk ganti foto ini.")
            
    with col2:
        st.markdown("""
        Sebagai **Senior Business Leader** dengan 10+ tahun pengalaman perbankan, saya membangun V-Guard AI untuk memberikan transparansi mutlak bagi pemilik bisnis. 
        
        Melalui prinsip **'Digitizing Trust'**, kami mengubah data CCTV, Kasir, dan Bank menjadi bukti otentik yang tidak bisa dimanipulasi. Kami menghentikan kebocoran (**Eliminating Leakage**) sebelum menjadi kerugian finansial besar.
        """)

# --- 📂 HALAMAN 2: PRODUK & HARGA ---
elif menu == "📦 Produk & Harga":
    st.header("Skema Investasi V-Guard AI")
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown('<div class="price-box"><b>V-LITE</b><br>Pemasangan: <span class="price-tag">1.5M</span><br>Bulanan: 250rb</div>', unsafe_allow_html=True)
        wa_button("V-LITE", "1.5M")
    with c2:
        st.markdown('<div class="price-box"><b>V-PRO</b><br>Pemasangan: <span class="price-tag">3.5M</span><br>Bulanan: 750rb</div>', unsafe_allow_html=True)
        wa_button("V-PRO", "3.5M")
    with c3:
        st.markdown('<div class="price-box"><b>V-SIGHT</b><br>Pemasangan: <span class="price-tag">5.0M</span><br>Bulanan: 1.2jt</div>', unsafe_allow_html=True)
        wa_button("V-SIGHT", "5.0M")
    with c4:
        st.markdown('<div class="price-box"><b>V-ENTERPRISE</b><br><span class="price-tag">CUSTOM</span><br>Solusi Korporasi</div>', unsafe_allow_html=True)
        wa_button("V-ENTERPRISE", "Custom")

# --- 📂 HALAMAN 3: PORTAL KLIEN ---
elif menu == "🔑 Portal Klien":
    st.header("🔑 Client Upload Center")
    st.text_input("Nama Bisnis")
    st.file_uploader("Upload Data Audit")
    if st.button("Kirim Data"):
        st.success("Data terkirim aman.")

# --- 📂 HALAMAN 4: ADMIN PANEL ---
elif menu == "🔐 Admin Panel":
    st.header("🔐 Executive Dashboard")
    pwd = st.text_input("Founder Password", type="password")
    if pwd:
        if hashlib.sha256(pwd.encode()).hexdigest() == ADMIN_PWD_HASH:
            st.success("Welcome, Pak Erwin.")
            st.metric("Leakage Prevented", "Rp 125.5M")
        else:
            st.error("Sandi Salah.")

# --- FOOTER ---
st.divider()
st.markdown(f'<div style="text-align:center; color:#8892b0;">🛡️ V-Guard AI Intelligence | @copyright {datetime.now().year} | Erwin Sinaga</div>', unsafe_allow_html=True)
