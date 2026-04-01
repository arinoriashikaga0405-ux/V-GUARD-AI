import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG: NOMOR WA & KEAMANAN ---
WHATSAPP_NUMBER = "628123456789" 
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

# --- 2. SETUP TEMA ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0a192f; color: #e6f1ff; }
    .price-box { 
        background-color: #112240; padding: 15px; border-radius: 12px; 
        border: 1px solid #233554; text-align: center; height: 100%;
    }
    .price-tag { color: #64ffda; font-size: 20px; font-weight: bold; }
    .wa-link { 
        color: #25D366; font-weight: bold; text-decoration: none; 
        border: 1px solid #25D366; padding: 5px 10px; border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: FOTO & MENU ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", width=150)
    else:
        st.markdown("### 👨‍💼")
        
    st.markdown("### **Erwin Sinaga**")
    st.caption("Founder & CEO V-Guard AI")
    st.divider()

    menu = st.sidebar.radio("Folder Navigasi:", [
        "🏠 Home (Profil Founder)", 
        "📦 Produk & Harga", 
        "🔑 Portal Klien", 
        "🔐 Admin Panel"
    ])

# --- FUNGSI PESAN WA ---
def get_wa_url(paket):
    msg = f"Halo Pak Erwin, saya tertarik paket V-Guard {paket}."
    clean_msg = msg.replace(" ", "%20")
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={clean_msg}"

# --- 📂 FOLDER 1: HOME (VISI MISI 200 KATA) ---
if menu == "🏠 Home (Profil Founder)":
    st.title("🛡️ V-Guard AI Intelligence")
    st.markdown("### *Digitizing Trust, Eliminating Leakage*")
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga", use_column_width=True)
        else:
            st.info("💡 Unggah 'erwin.jpg' ke GitHub.")
            
    with col2:
        st.header("Visi & Misi")
        # NARASI 200 KATA UTUH TANPA DIKURANGI
        narasi = """
        Sebagai seorang **Senior Business Leader** dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, 
        saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi, melainkan **ketidakpastian data dan kebocoran internal**. 
        Di dunia digital yang serba cepat ini, kepercayaan (trust) tidak lagi cukup jika hanya berdasarkan janji atau intuisi; 
        kepercayaan harus bisa diukur, diverifikasi, dan didigitalisasi. Inilah alasan utama saya mendirikan **V-Guard AI Intelligence**.

        Visi kami adalah menjadi standar global dalam **Digital Trust**. Kami percaya bahwa setiap pemilik bisnis—mulai dari tokoh retail 
        mandiri (V-LITE) hingga korporasi multinasional (V-ENTERPRISE)—berhak mendapatkan transparansi mutlak atas aset mereka. 
        Melalui prinsip **'Digitizing Trust'**, kami mengubah setiap titik data mentah dari CCTV, mesin kasir (POS), laporan stok gudang (VCS), 
        dan mutasi bank menjadi bukti otentik yang tidak dapat
