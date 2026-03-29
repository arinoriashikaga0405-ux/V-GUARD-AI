import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from PIL import Image

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# API KEY BAPAK
GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"

if GOOGLE_API_KEY:
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except:
        st.error("Koneksi AI Terputus.")

def get_foto(lebar):
    try:
        if os.path.exists('erwin.jpg'):
            return st.image(Image.open('erwin.jpg'), width=lebar)
        else:
            return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)
    except:
        st.write("📸")

# 2. STATUS LOGIN
if 'role' not in st.session_state:
    st.session_state.role = None

def login_vguard():
    st.sidebar.markdown("---")
    with st.sidebar.form("login_form"):
        u = st.text_input("Username").strip().lower()
        p = st.text_input("Password", type="password").strip()
        if st.form_submit_button("Masuk"):
            if u == "admin" and p == "Vguard2026":
                st.session_state.role = "admin"
                st.rerun()
            elif u == "klien" and p == "User2026":
                st.session_state.role = "klien"
                st.rerun()

# 3. CSS DESIGN (UKURAN KOTAK PROPORSIONAL)
st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    .hero-bg { background: #0e1117; padding: 25px; border-radius: 15px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 30px; }
    .card-v { 
        background: white; padding: 20px; border-radius: 12px; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 6px solid #FFD700; 
        height: 520px; display: flex; flex-direction: column; justify-content: space-between;
    }
    .card-v h4 { font-size: 20px; color: #1a1a1a; font-weight: 800; text-align: center; }
    .card-v .price { font-size: 26px; color: #d42f2f; font-weight: bold; text-align: center; margin-bottom: 10px; }
    .card-v .section-title { font-size: 13px; font-weight: bold; color: #888; text-transform: uppercase; margin-top: 8px; border-bottom:
