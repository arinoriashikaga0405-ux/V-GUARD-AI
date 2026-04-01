import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "Eksekutif", "Paket": "MASTER"},
        {"User ID": "siska", "Password": "p", "Level": "Klien", "Paket": "SMART"}
    ]
if 'client_logged_in' not in st.session_state: st.session_state.client_logged_in = False

# --- 3. CSS ---
st.markdown("""
<style>
    .status-box { background-color: #e3f2fd; padding: 15px; border-radius: 8px; color: #1e3a8a; font-weight: bold; margin-bottom: 5px; }
    .package-box { background-color: #fff3e0; padding: 8px 15px; border-radius: 8px; color: #e65100; font-weight: bold; display: inline-block; margin-bottom: 20px; }
    .wa-button { background-color: #25d366; color: white; padding: 10px 20px; border-radius: 50px; text-decoration: none; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR NAVIGASI ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Erwin Sinaga")
    st.markdown("**Erwin Sinaga**\nSenior Business Leader")
    st.write("---")
    nav = st.radio("Menu Utama:", ["1. Profil Founder", "2. Visi Misi ROI", "3. Layanan Produk", "4. Registrasi Dashboard", "5. Akses Admin"])
    st.write("---")
    st.markdown('<a href="https://wa.me/628212190885" class="wa-button">💬 Chat WhatsApp</a>', unsafe_allow_html=True)

# --- 5. LOGIKA MENU ---

if nav == "1. Profil Founder":
    st.header("Profil Kepemimpinan")
    st.write("""Bapak **Erwin Sinaga** adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Beliau memahami bahwa di era digital saat ini, integritas data dan keamanan aset adalah fondasi utama bagi setiap unit bisnis untuk dapat tumbuh secara berkelanjutan. 

Melalui dedikasi yang tinggi terhadap transparansi, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan mendesak para pengusaha akan sistem perlindungan aset yang berbasis teknologi kecerdasan buatan mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif dan efisien. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit real-time yang mampu meminimalisir risiko kerugian modal secara signifikan.""")

elif nav == "2. Visi Misi ROI":
    st.header("Visi, Misi & ROI")
    with st.expander("Visi & Misi", expanded=True):
        st.write("**Visi:** Menjadi pelopor global audit digital berbasis AI.")
        st.write("**Misi:** Mengintegrasikan AI untuk deteksi fraud real-time dan
