import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG: KEAMANAN & KONTAK ---
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()
WHATSAPP_NUMBER = "628123456789" # Ganti dengan nomor WA Bapak (pake kode negara)

# --- 2. SETUP TEMA PREMIUM CORPORATE ---
st.set_page_config(page_title="V-Guard AI Intelligence | Erwin Sinaga", page_icon="🛡️", layout="wide")

# CSS untuk tampilan Dark Mode Premium
st.markdown("""
    <style>
    /* Mengubah warna background utama */
    .main { background-color: #0a192f; color: #e6f1ff; }
    
    /* Mengubah warna sidebar */
    .css-1r6slb0 { background-color: #00122e; } 
    
    /* Tombol Kontak WA */
    .stButton>button { 
        background-color: #25D366; color: white; 
        font-weight: bold; border-radius: 25px; border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #128C7E; transform: scale(1.05); }
    
    /* Tombol Login Admin */
    div[data-testid="stSidebar"] .stButton>button {
        background-color: #64ffda; color: #0a192f;
        border-radius: 5px;
    }

    /* Style untuk Kotak Harga */
    .price-box {
        background-color: #112240; padding: 20px; border-radius: 15px;
        border: 1px solid #233554; text-align: center; margin-bottom: 20px;
    }
    .price-header { color: #64ffda; font-size: 20px; font-weight: bold; }
    .price-tag { color: white; font-size: 28px; font-weight: bold; margin: 10px 0; }
    .price-desc { color: #8892b0; font-size: 14px; }
    
    h1, h2, h3 { color: #ccd6f6; font-family: 'Inter', sans-serif; }
    .footer { text-align: center; color: #8892b0; padding: 20px; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION & FOTO FOUNDER ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 📸 TAMPILKAN FOTO FOUNDER DI ATAS MENU
