import streamlit as st
import pandas as pd
import os

# --- 1. SETTING HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATA KONTAK ---
num_wa = "628212190885"
wa_link = f"https://wa.me/{num_wa}?text=Halo%20CEO%20V-Guard%20AI,"

# --- 3. DATABASE ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "CEO", "Paket": "MASTER"},
        {"User ID": "siska", "Password": "p", "Level": "Klien", "Paket": "SMART"}
    ]
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 4. CSS TAMPILAN ---
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    .ceo-card { background-color: white; padding: 25px; border-radius: 15px; border-left: 5px solid #0f172a; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .metric-box { background-color: white; padding: 20px; border-radius: 12px; text-align: center; border: 1px solid #e2e8f0; }
    .price-card { background-color: white; padding: 25px; border-radius: 15px; text-align: center; border: 1px solid #e2e8f0; }
    .wa-btn { background-color: #25d366; color: white !important; padding: 10px; border-radius: 8px; text-decoration: none; display: block; text-align: center; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 5. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    
    st.markdown("### **Erwin Sinaga**")
    st.markdown("**Founder & CEO**")
    st.write("---")
    nav = st.radio("Menu Utama:", ["Profil Founder", "ROI & Visi Misi", "Layanan & Biaya", "Dashboard", "Admin"])
    st.write("---")
    st.markdown(f'<a href="{wa_link}" class="wa-btn">💬 WhatsApp CEO</a>', unsafe_allow_html=True)

# --- 6. LOGIKA MENU ---

if nav == "Profil Founder":
    st.header("Profil Kepemimpinan")
    with st.container():
        st.markdown('<div class="ceo-card">', unsafe_allow_html=True)
        # Teks profil dipotong agar tidak error saat copy-paste
        p1 = "Bapak **Erwin Sinaga** adalah **Founder & CEO V-Guard AI** dengan pengalaman "
        p2 = "lebih dari satu dekade memimpin operasional di industri perbankan dan aset manajemen. "
        p3
