import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG: KONTAK & KEAMANAN ---
WHATSAPP_NUMBER = "628123456789" # <--- GANTI DENGAN NOMOR WA ASLI BAPAK
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

# --- 2. SETUP TEMA PREMIUM ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0a192f; color: #e6f1ff; }
    .price-box { 
        background-color: #112240; padding: 15px; border-radius: 12px; 
        border: 1px solid #233554; text-align: center; height: 100%;
    }
    .price-tag { color: #64ffda; font-size: 22px; font-weight: bold; }
    .wa-link { 
        color: #25D366; font-weight: bold; text-decoration: none; 
        border: 1px solid #25D366; padding: 5px 10px; border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: FOTO FOUNDER DI ATAS MENU ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", width=150)
    else:
        st.markdown("### 👨‍💼") # Placeholder jika erwin.jpg belum di-upload
        
    st.markdown("### **Erwin Sinaga**")
    st.caption("Founder & CEO V-Guard AI")
    st.divider()

    menu = st.radio("Folder Navigasi:", [
        "🏠 Home (Visi Founder)", 
        "📦 Produk & Harga", 
        "🔑 Portal Klien", 
        "🔐 Admin Panel"
    ])

# --- FUNGSI LINK WA ---
def wa_link(paket):
    msg = f"Halo Pak Erwin, saya tertarik dengan paket V-Guard {paket}. Mohon info pemasangannya."
    url = f"https://wa.me/{WHATSAPP_NUMBER}?text={msg.replace(' ', '%20')}"
    return url

# --- 📂 HALAMAN 1: HOME (FULL 200 KATA) ---
if menu == "🏠 Home (Visi Founder)":
    st.title("🛡️ V-Guard AI Intelligence")
    st.markdown("### *Digitizing Trust, Eliminating Leakage*")
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga", use_column_width=True)
        else:
            st.info("💡 Unggah file 'erwin.jpg' ke GitHub Bapak agar foto tampil di sini.")
            
    with col2:
        st.header("Visi & Misi")
        # NARASI UTUH 200 KATA TANPA DIKURANGI
        st.markdown("""
        Sebagai seorang **Senior Business Leader** dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, 
        saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi, melainkan **ketidakpastian data dan kebocoran internal**. 
        Di dunia digital yang serba cepat ini, kepercayaan (trust) tidak lagi cukup jika hanya didasarkan pada janji atau intuisi; 
        kepercayaan harus bisa diukur, diverifikasi, dan didigitalisasi. Inilah alasan utama saya mendirikan **V-Guard AI Intelligence**.

        Visi kami adalah menjadi standar global dalam **Digital Trust**. Kami percaya bahwa setiap pemilik bisnis—mulai dari tokoh retail 
        mandiri (V-LITE) hingga korporasi multinasional (V-ENTERPRISE)—berhak mendapatkan transparansi mutlak atas aset mereka. 
        Melalui prinsip **'Digitizing Trust'**, kami mengubah setiap titik data mentah dari CCTV, mesin kasir (POS), laporan stok gudang (VCS), 
        dan mutasi bank menjadi bukti otentik yang tidak dapat dimanipulasi oleh siapa pun.

        Misi utama kami, **'Eliminating Leakage'**, dijalankan dengan mengorkestrasikan 9 platform AI tercanggih di dunia (termasuk Gemini, 
        MindBridge, dan YOLO). Kami tidak hanya mendeteksi kecurangan (fraud) setelah terjadi
