import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
from PIL import Image

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# --- KONEKSI AI GEMINI ---
GOOGLE_API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Koneksi AI Terputus.")

# --- SISTEM LOGIN STATE ---
if 'role' not in st.session_state:
    st.session_state.role = None

# --- DESIGN TAMPILAN (CSS) ---
st.markdown("""
<style>
    .stApp { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #0e1117 !important; border-right: 2px solid #FFD700; }
    [data-testid="stSidebar"] .stMarkdown b { color: white !important; }
    .hero-bg { background: #0e1117; padding: 20px; border-radius: 12px; color: white; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 20px; }
    .card-v { 
        background: white; padding: 15px; border-radius: 10px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 5px solid #FFD700; 
        height: 380px; display: flex; flex-direction: column; justify-content: space-between;
    }
    .card-v h4 { font-size: 16px; font-weight: 800; color: #111; text-align: center; margin: 0; }
    .card-v .price { font-size: 20px; color: #d42f2f; font-weight: bold; text-align: center; }
    .stLinkButton button { width: 100%; background-color: #FFD700 !important; color: #000 !important; font-weight: bold; border-radius: 8px; }
    .fraud-card { background: #fff5f5; border-left: 5px solid #d42f2f; padding: 15px; border-radius: 8px; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)
