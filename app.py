import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from PIL import Image

# 1. KONFIGURASI UTAMA
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# API KEY BAPAK
GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"

if GOOGLE_API_KEY:
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except:
        st.error("Gagal mengonfigurasi AI.")

def get_foto(lebar):
    try:
        if os.path.exists('erwin.jpg'):
            return st.image(Image.open('erwin.jpg'), width=lebar)
        else:
            return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)
    except:
        st.write("📸")

# 2. SISTEM LOGIN
if 'role' not in st.session_state:
    st.session_state.role = None

def login_vguard():
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔐 Login Akses")
    with st.sidebar.form("login_form"):
        u = st.text_input("Username").strip().lower()
        p = st.text_input("Password", type="password").strip()
        submit = st.form_submit_button("Masuk Ke Sistem")
        if submit:
            if u == "admin" and p == "Vguard2026":
                st.session_state.role = "admin"
                st.rerun()
            elif u == "klien" and p == "User2026":
                st.session_state.role = "klien"
                st.rerun()
            else:
                st.sidebar.error("Username/Password Salah")

# 3. CSS DESIGN (UKURAN BESAR & ELEGAN)
st.markdown("""<style>
    .stApp { background-color: #f4f6f9; }
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 3px solid #FFD700; }
    .hero-bg { background: linear-gradient(135deg, #0e1117 0%, #1c1f26 100%); padding: 30px; border-radius: 20px; color: white; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 25px; }
    .card-service { 
        background: white; 
        padding: 30px; 
        border-radius: 15px; 
        box-shadow: 0 8px 20px rgba(0,0,0,0.1); 
        border-top: 8px solid #FFD700; 
        text-align: center; 
        height: 380px; 
        display: flex; 
        flex-direction: column; 
        justify-content: space-between;
    }
    .card-service h4 { font-size: 24px; font-weight: bold; color: #1a1a1a; margin-bottom: 10px; }
    .card-service
