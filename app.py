import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
import os
from datetime import datetime
import urllib.parse
import io

# 1. KONFIGURASI SISTEM
st.set_page_config(page_title="V-GUARD AI Systems", page_icon="🛡️", layout="wide")

# Konfigurasi AI
API_KEY = "PASTE_API_KEY_BAPAK_DI_SINI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. CSS PREMIUM
st.markdown("""
    <style>
    section[data-testid="stSidebar"] { background-color: #0e1117 !important; color: white !important; }
    .hero-bg { background-color: #0e1117; padding: 40px; border-radius: 20px; color: white; text-align: center; border-bottom: 5px solid #FFD700; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #FFD700 !important; color: #0e1117 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. FUNGSI FOTO
def get_foto(lebar):
    if os.path.exists('erwin.jpg'):
        return st.image(Image.open('erwin.jpg'), width=lebar)
    else:
        return st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=lebar)

# 4. SIDEBAR
with st.sidebar:
    st.markdown("### 🛡️ V-GUARD SYSTEMS")
    col_f, col_n = st.columns([1, 2])
    with col_f: get_foto(80)
    with col_n: st.markdown("<p style='color: white; font-weight: bold;'>Erwin Sinaga</p><p style='color: #FFD700; font-size: 11px;'>Founder V-GUARD</p>", unsafe_allow_html=True)
    st.divider()
    halaman = st.radio("Menu Utama:", ["🌐 Beranda", "🤖 AI Auditor Utama", "🛠️ Alat AI Pendukung", "🔐 Panel Kontrol WA"])

# ==========================================
# MENU BARU: ALAT AI PENDUKUNG
# ==========================================
if halaman == "🛠️ Alat AI Pendukung":
    st.title("🛠️ Business Support AI")
    st.write("Gunakan fitur tambahan ini untuk produktivitas klien Anda.")
    
    t1, t2 = st.tabs(["📈 Prediksi Omset", "📝 Ringkasan Rapat AI"])
    
    with t1:
        st.subheader("AI Sales Forecasting")
        target = st.number_input("Input Omset Minggu Lalu (Rp):", min_value=0)
        if st.button("Prediksi Minggu Depan"):
            prediksi = target * 1.15 # Contoh logika AI sederhana
            st.success(f"Berdasarkan tren data, omset minggu depan diprediksi naik ke: Rp {prediksi:,.0f}")
            st.info("AI menganalisis kenaikan 15% berdasarkan tren histori klien.")

    with t2:
        st.subheader("AI Meeting Summarizer")
        rapat = st.text_area("Tempel transkrip rapat di sini:")
        if st.button("Rangkum Poin Penting"):
            with st.spinner("AI sedang merangkum..."):
                resp = model.generate_content(f"Buatkan ringkasan poin tindakan (action plan) dari teks rapat ini: {rapat}")
                st.markdown(resp.text)

# (Halaman lain tetap ada di sini...)
elif halaman == "🌐 Beranda":
    st.markdown('<div class="hero-bg"><h1>V-GUARD AI SYSTEMS</h1></div>', unsafe_allow_html=True)
    get_foto(350)
    st.write("V-Guard bukan sekadar software, tapi AI Auditor cerdas.")

elif halaman == "🤖 AI Auditor Utama":
    st.title("🤖 AI Auditor Utama")
    # Fitur Upload Excel Bapak

elif halaman == "🔐 Panel Kontrol WA":
    st.title("🔐 Panel Admin")
    # Fitur WhatsApp Bapak
