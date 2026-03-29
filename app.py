import streamlit as st
import pandas as pd
import google.generativeai as genai
import urllib.parse

# 1. KONFIGURASI SISTEM & API
st.set_page_config(page_title="V-GUARD AI - Revenue Protection", page_icon="🛡️", layout="wide")

# Masukkan API Key asli Anda di bawah ini
API_KEY = "ISI_KODE_AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# DATA KONTAK PAK ERWIN
WA_NOMOR = "6282122190885" 

# 2. LOGIKA LOGIN SESSIN STATE
if 'role' not in st.session_state:
    st.session_state.role = None

def login():
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔐 Akses Klien/Admin")
    user = st.sidebar.text_input("Username", key="login_user")
    pw = st.sidebar.text_input("Password", type="password", key="login_pw")
    if st.sidebar.button("Masuk", key="login_btn"):
        if user == "admin" and pw == "admin123":
            st.session_state.role = "admin"
            st.rerun()
        elif user == "klien" and pw == "klien123":
            st.session_state.role = "klien"
            st.rerun()
        else:
            st.sidebar.error("Akses Ditolak: Kredensial Salah")

# 3. CSS EXECUTIVE DESIGN (Lebih Bersih & Fokus Promosi)
st.markdown("""
    <style>
    .stApp { background-color: #f4f6f9; }
    
    /* Sidebar Styling - Khas V-GUARD */
    section[data-testid="stSidebar"] { 
        background-color: #0e1117 !important; 
        border-right: 3px solid #FFD700; 
    }
    
    /* Hero Section (Banner Utama) */
    .hero-bg { 
        background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); 
        padding: 40px; border-radius: 25px; color: white; text-align: center; 
        border-bottom: 8px solid #FFD700; box-shadow: 0 15px 35px rgba(0,0,0,0.3);
        margin-bottom: 30px;
    }
    .hero-bg h1 { font-size: 36px; color: #FFD700; margin-bottom: 10px; }
    .hero-bg p { font-size: 18px; color: #f8f9fa; font-weight: 300; }

    /* Kartu Layanan / Paket Promosi */
    .card-service { 
        background: white; padding: 20px; border-radius: 20px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.1); color: #0e1117; 
        border-top: 6px solid #FFD700; text-align: center;
        height: 320px; display: flex; flex-direction: column; justify-content: space-between;
        transition: transform 0.3s ease;
    }
    .card-service:hover { transform: translateY(-10px); }
    .card-service h4 { color: #0e1117; font-weight: bold; margin-bottom: 5px; }
    .card-service h3 { color: #b8860b; font-size: 28px; margin-top: 0px; }
    .card-service hr { border: 0.5px solid #eee; margin: 15px 0; }
    .card-service p { font-size: 14px; color: #555; line-height: 1.6; }

    /* Tombol WhatsApp (Gaya Eksekutif) */
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.
