import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI ---
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

# --- 4. CSS TAMPILAN PREMIUM ---
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    .ceo-card { background-color: white; padding: 25px; border-radius: 15px; border-left: 5px solid #0f172a; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .metric-box { background-color: white; padding: 20px; border-radius: 12px; text-align: center; border: 1px solid #e2e8f0; }
    .price-card { background-color: white; padding: 25px; border-radius: 15px; text-align: center; border: 1px solid #e2e8f0; transition: 0.3s; }
    .price-card:hover { border: 2px solid #0f172a; transform: translateY(-5px); }
    .wa-btn { background-color: #25d366; color: white !important; padding: 10px; border-radius: 8px; text-decoration: none; display: block; text-align: center; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 5. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder & CEO")
    else:
        st.info("Simpan foto Bapak dengan nama erwin.jpg")
    
    st.markdown("### **Erwin Sinaga**")
    st.markdown("**Founder & CEO**")
    st.write("---")
    nav = st.radio("Navigasi Utama:", ["Profil Founder", "Visi Misi & ROI", "Layanan & Biaya", "Dashboard", "Admin"])
    st.write("---")
    st.markdown(f'<a href="{wa_link}" class="wa-btn">💬 WhatsApp CEO</a>', unsafe_allow_html=True)

# --- 6. LOGIKA MENU ---

if nav == "Profil Founder":
    st.header("Profil Kepemimpinan")
    with st.container():
        st.markdown('<div class="ceo-card">', unsafe_allow_html=True)
        st.write("""Bapak **Erwin Sinaga** adalah **Founder & CEO V-Guard AI** yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Sebagai pemimpin tertinggi di V-Guard AI, beliau memahami bahwa di era digital saat ini, integritas data dan keamanan aset adalah fondasi utama bagi setiap unit bisnis untuk dapat tumbuh secara berkelanjutan. Melalui dedikasi yang tinggi terhadap transparansi, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan mendesak para pengusaha akan sistem perlindungan aset yang berbasis teknologi kecerdasan buatan mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif dan efisien bagi pelaku UMKM maupun korporasi nasional.""")
        st.markdown('</div>', unsafe_allow_html=True)

elif nav == "Visi Misi & ROI":
    st.header("Strategi Perlindungan Aset")
    c1, c2 = st.columns(2)
    with c1: st.info("**👁️ Visi CEO:** Menjadi pelopor global audit digital berbasis AI.")
    with c2: st.success("**🚀 Misi CEO:** Deteksi fraud real-time & proteksi aset UMKM.")
    
    st.write("---")
    st.subheader("Simulasi ROI Kerugian Klien")
    oz = st.number_input("Input Omzet Bulanan (Rp):", value=100000000)
    rugi = oz * 0.07
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="metric-box"><p>Potensi Kerugian (7%)</p><h2 style="color:red">Rp {rugi:,.0f}</h2></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-box"><p>Aset Terselamatkan AI</p><h2 style="color:green">Rp {rugi*0.9:,.0
