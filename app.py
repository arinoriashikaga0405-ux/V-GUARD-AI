import streamlit as st
import os
import pandas as pd
from datetime import datetime
import google.generativeai as genai

# --- 1. CONFIG & ENGINE AI ---
K_V = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=K_V)
    v_ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE & SESSION STATE ---
if 'db_n' not in st.session_state:
    st.session_state.db_n = [
        {"ID": "CL-101", "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Usaha": "F&B", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": "CL-102", "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Usaha": "Otomotif", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]

if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "p", "Level": "Eksekutif"},
        {"User ID": "siska", "Password": "p", "Level": "Klien"}
    ]

if 'auth_vguard' not in st.session_state:
    st.session_state.auth_vguard = False

if 'client_logged_in' not in st.session_state:
    st.session_state.client_logged_in = False

# --- 3. CSS PREMIUM ---
st.markdown("""
<style>
    .fraud-header { background-color: #ff7675; color: white; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 15px; font-size: 16px; }
    .service-card { background-color: #ffffff; padding: 15px; border-radius: 12px; border: 1px solid #e0e0e0; box-shadow: 2px 2px 8px rgba(0,0,0,0.05); text-align: center; height: 400px; }
    .client-box { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #1e3a8a; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.markdown("**Erwin Sinaga - Senior Business Leader**")
    st.write("---")
    nav = st.radio("Navigasi Utama:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 💎 Layanan Produk", "4. 📝 Registrasi & Upload", "5. 🔐 Akses Terbatas"])
    st.write("---")
    st.caption("© 2026 V-Guard AI Intelligence")

# --- 5. LOGIKA HALAMAN ---

if nav == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2.5])
    with c1:
        if os.path.exists("er
