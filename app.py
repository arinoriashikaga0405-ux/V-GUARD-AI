import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "Eksekutif", "Paket": "MASTER"}
    ]
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 3. CSS MODERN ---
st.markdown("""
<style>
    .stApp { background-color: #f4f7f6; }
    .founder-card { background-color: white; padding: 25px; border-radius: 15px; border-left: 5px solid #1e3a8a; margin-bottom: 20px; }
    .pricing-card { background-color: white; padding: 20px; border-radius: 15px; text-align: center; border: 1px solid #e2e8f0; height: 350px; }
    .wa-btn { background-color: #25d366; color: white !important; padding: 12px; border-radius: 8px; text-decoration: none; display: block; text-align: center; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR (Tanpa Angka) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    
    # Menu navigasi tanpa angka
    menu = [
        "Profil Kepemimpinan & ROI", 
        "Daftar Harga Modern", 
        "Register Pelanggan", 
        "Dashboard Login", 
        "Admin Panel"
    ]
    nav = st.radio("Navigasi Utama:", menu)
    st.write("---")
    st.markdown('<a href="https://wa.me/628212190885" class="wa-btn">💬 Hubungi Admin</a>', unsafe_allow_html=True)

# --- 5. LOGIKA MENU ---

if nav == "Profil Kepemimpinan & ROI":
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga — Founder")
    with col2:
        with st.container(border=True):
            st.write("""
            Bapak **Erwin Sinaga** adalah **Founder V-Guard AI** yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

            Melalui dedikasi yang tinggi terhadap transparansi, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan mendesak para pengusaha akan sistem perlindungan aset yang berbasis teknologi kecerdasan buatan mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif dan efisien. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit real-time yang mampu meminimalisir risiko kerugian modal secara signifikan bagi pelaku UMKM maupun korporasi nasional.
            """)
    
    st.write("---")
    st.subheader("Visi, Misi & Analisis ROI")
    v1, v2 = st.columns(2)
    with v1: st.info("**Visi:** Pelopor audit digital AI global.")
    with v2: st.success("**Misi:** Deteksi fraud & proteksi aset UMKM.")
    
    oz = st.number_input("Input Omzet Bulanan Bisnis (Rp):", value=100000000)
    rugi = oz * 0.07
    st.metric("Potensi Kerugian (7%)", f"Rp {rugi:,.0f}")
    st.metric("Aset Terselamatkan AI", f"Rp {rugi*0.9:,.0f}")

elif nav == "Daftar Harga Modern":
    st.header("Price List V-Guard AI")
    wa_adm = "https://wa.me/628212190885?text=Saya%20tertarik%20Paket%20"
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="pricing-card"><h3>BASIC</h3><h1>1.5jt</h1><p>/bulan</p><p>✓ Monitor Dasar<br>✓ Laporan Bulanan</p></div>', unsafe_allow_html=True)
        st.link_button("Pesan BASIC", wa_adm + "BASIC")
    with c2:
        st.markdown('<div class="pricing-card" style="border:2px solid #1e3a8a"><h3>SMART</h3><h1>2.5jt</h1><p>/bulan</p><p>✓ Real-Time Monitor<br>✓ VCS Integrasi</p></div>', unsafe_allow_html=True
