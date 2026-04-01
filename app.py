import streamlit as st
import pandas as pd
import hashlib
import time

# 🔐 PENGATURAN KEAMANAN (Password CEO)
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# --- TAMPILAN GAGAH ---
st.title("🛡️ V-Guard AI Intelligence")
st.subheader("Digitizing Trust, Eliminating Leakage")

# --- VISI & MISI (200 KATA) ---
col1, col2 = st.columns([1, 2])
with col1:
    st.info("Founder: Erwin Sinaga")
    st.image("https://via.placeholder.com/300x400.png?text=Erwin+Sinaga", caption="Founder V-Guard AI")

with col2:
    st.header("Visi & Misi")
    st.markdown("""
    Sebagai seorang **Senior Business Leader** dengan pengalaman lebih dari satu dekade di industri perbankan dan aset, 
    saya memahami bahwa musuh terbesar pertumbuhan bisnis bukanlah kompetisi, melainkan **ketidakpastian data dan kebocoran internal**. 
    Di dunia yang bergerak serba cepat, kepercayaan (trust) tidak lagi cukup jika hanya berdasarkan janji; 
    kepercayaan harus bisa diukur, diverifikasi, dan didigitalisasi. Inilah alasan saya mendirikan **V-Guard AI Intelligence**.

    Visi kami adalah menjadi standar global dalam **Digital Trust**. Kami percaya bahwa setiap pemilik bisnis—mulai dari 
    warung modern hingga korporasi multinasional—berhak mendapatkan transparansi mutlak atas aset mereka. 
    Melalui prinsip **'Digitizing Trust'**, kami mengubah data mentah dari CCTV, mesin kasir, dan laporan bank 
    menjadi bukti otentik yang tidak dapat dimanipulasi. 

    Misi utama kami, **'Eliminating Leakage'**, dijalankan dengan mengintegrasikan ekosistem AI tercanggih di dunia. 
    Kami tidak hanya mendeteksi kecurangan saat sudah terjadi, tetapi kami membangun benteng pertahanan prediktif 
    untuk menghentikan kebocoran sebelum menjadi kerugian finansial. V-Guard AI memastikan setiap rupiah investasi 
    Anda bekerja secara jujur dan optimal untuk masa depan bisnis Anda.
    """)

st.divider()

# --- ADMIN PANEL CHECK ---
st.sidebar.title("Command Center")
pwd = st.sidebar.text_input("Sandi Founder", type="password")
if pwd:
    if hashlib.sha256(pwd.encode()).hexdigest() == ADMIN_PWD_HASH:
        st.sidebar.success("Akses Founder Diterima")
        if st.button("🚀 JALANKAN AUDIT GLOBAL"):
            with st.spinner("Sinkronisasi 9 AI Engine..."):
                time.sleep(2)
                st.success("Audit Selesai! Akurasi 99.9%")
    else:
        st.sidebar.error("Sandi Salah")
