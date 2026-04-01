import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG: NOMOR WA & KEAMANAN ---
# Masukkan nomor WA Bapak di sini (Gunakan kode negara 62)
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
    .price-tag { color: #64ffda; font-size: 22px; font-weight: bold; }
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

    menu = st.radio("Folder Navigasi:", [
        "🏠 Home (Profil Founder)", 
        "📦 Produk & Harga", 
        "🔑 Portal Klien", 
        "🔐 Admin Panel"
    ])

# --- FUNGSI PESAN WA ---
def get_wa_url(paket):
    msg = f"Halo Pak Erwin, saya tertarik dengan paket V-Guard {paket}. Mohon info pemasangannya."
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={msg.replace(' ', '%20')}"

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
            st.info("💡 Unggah 'erwin.jpg' ke GitHub Bapak.")
            
    with col2:
        st.header("Visi & Misi")
        # NARASI 200 KATA UTUH
        narasi = """
        Sebagai seorang **Senior Business Leader** dengan pengalaman lebih dari satu dekade di industri perbankan dan pengelolaan aset, 
        saya memahami bahwa pondasi pertumbuhan bisnis bukanlah sekadar inovasi, melainkan **ketidakpastian data dan kebocoran internal**. 
        Di dunia digital yang serba cepat ini, kepercayaan (trust) tidak lagi cukup jika hanya berdasarkan janji atau intuisi; 
        kepercayaan harus bisa diukur, diverifikasi, dan didigitalisasi. Inilah alasan utama saya mendirikan **V-Guard AI Intelligence**.

        Visi kami adalah menjadi standar global dalam **Digital Trust**. Kami percaya bahwa setiap pemilik bisnis—mulai dari tokoh retail 
        mandiri (V-LITE) hingga korporasi multinasional (V-ENTERPRISE)—berhak mendapatkan transparansi mutlak atas aset mereka. 
        Melalui prinsip **'Digitizing Trust'**, kami mengubah setiap titik data mentah dari CCTV, mesin kasir (POS), laporan stok gudang (VCS), 
        dan mutasi bank menjadi bukti otentik yang tidak dapat dimanipulasi oleh siapa pun.

        Misi utama kami, **'Eliminating Leakage'**, dijalankan dengan mengorkestrasikan 9 platform AI tercanggih di dunia (termasuk Gemini, 
        MindBridge, dan YOLO). Kami tidak hanya mendeteksi kecurangan (fraud) setelah terjadi, tetapi kami membangun benteng pertahanan 
        prediktif untuk menghentikan pola kebocoran sebelum menjadi kerugian finansial yang signifikan. Dengan V-Guard AI, kami mengembalikan 
        kendali penuh ke tangan pemilik usaha, memberikan ketenangan pikiran (*peace of mind*), dan memastikan setiap rupiah yang Anda investasikan 
        bekerja secara jujur dan optimal untuk masa depan bisnis Anda.
        """
        st.markdown(narasi)
        st.caption("— **Erwin Sinaga**, Founder V-Guard AI Intelligence")

# --- 📂 FOLDER 2: PRODUK & HARGA ---
elif menu == "📦 Produk & Harga":
    st.header("Skema Investasi & Layanan")
    st.divider()
    
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown(f'<div class="price-box"><b>V-LITE</b><br><small>UMKM</small><hr>Pemasangan: <br><span class="price-tag">Rp 1.5M</span><br>Bulanan: 250rb<br><br><a href="{get_wa_url("V-LITE")}" class="wa-link">💬 Chat WA</a></div>', unsafe_allow_html=True)

    with c2:
        st.markdown(f'<div class="price-box"><b>V-PRO</b><br><small>Retail/Resto</small><hr>Pemasangan: <br><span class="price-tag">Rp 3.5M</span><br>Bulanan: 750rb<br><br><a href="{get_wa_url("V-PRO")}" class="wa-link">💬 Chat WA</a></div>', unsafe_allow_html=True)

    with c3:
        st.markdown(f'<div class="price-box"><b>V-SIGHT</b><br><small>Keamanan Visual</small><hr
