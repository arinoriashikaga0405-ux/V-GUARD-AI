import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "Eksekutif", "Paket": "MASTER"}
    ]
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 3. CSS MODERN ---
st.markdown("""
<style>
    .stApp { background-color: #f4f7f6; }
    .pricing-card { 
        background-color: white; 
        padding: 20px; 
        border-radius: 15px; 
        text-align: center; 
        border: 1px solid #e2e8f0; 
        height: 350px; 
    }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR (Tanpa Angka) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    
    menu = [
        "Profil Kepemimpinan & ROI", 
        "Daftar Harga Modern", 
        "Register Pelanggan", 
        "Dashboard Login", 
        "Admin Panel"
    ]
    nav = st.radio("Navigasi Utama:", menu)
    st.write("---")
    st.markdown('<a href="https://wa.me/628212190885" target="_blank" style="background-color: #25d366; color: white; padding: 12px; border-radius: 8px; text-decoration: none; display: block; text-align: center; font-weight: bold;">💬 Hubungi Admin</a>', unsafe_allow_html=True)

# --- 5. LOGIKA MENU ---

if nav == "Profil Kepemimpinan & ROI":
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga — Founder")
    with col2:
        with st.container(border=True):
            st.write("""
            Bapak **Erwin Sinaga** adalah **Founder V-Guard AI** yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem konvensional. 

            Melalui dedikasi yang tinggi terhadap transparansi, beliau membangun V-Guard AI untuk memberikan rasa aman bagi pemilik bisnis melalui penerapan audit real-time yang mampu meminimalisir risiko kerugian modal secara signifikan bagi pelaku UMKM maupun korporasi nasional.
            """)
    
    st.write("---")
    st.subheader("Visi, Misi & Analisis ROI")
    v1, v2 = st.columns(2)
    with v1: st.info("**V
