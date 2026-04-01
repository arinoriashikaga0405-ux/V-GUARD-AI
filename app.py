import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "CEO", "Paket": "MASTER"},
        {"User ID": "siska", "Password": "p", "Level": "Klien", "Paket": "SMART"}
    ]
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 3. SIDEBAR (FOUNDER & CEO) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    
    st.markdown("### **Erwin Sinaga**")
    st.markdown("**Founder & CEO**")
    st.write("---")
    nav = st.radio("Menu Utama:", [
        "Profil Founder", 
        "ROI & Visi Misi", 
        "Layanan & Biaya", 
        "API Gateway",
        "Dashboard", 
        "Admin"
    ])
    st.write("---")
    st.link_button("💬 WhatsApp CEO", "https://wa.me/628212190885")

# --- 4. LOGIKA MENU ---

if nav == "Profil Founder":
    st.header("Profil Kepemimpinan")
    with st.container(border=True):
        st.write("""
        Bapak **Erwin Sinaga** adalah **Founder & CEO V-Guard AI** dengan pengalaman 
        lebih dari satu dekade memimpin operasional di industri perbankan dan aset manajemen. 
        Beliau membangun V-Guard AI untuk memberikan solusi perlindungan aset secara 
        real-time bagi pengusaha melalui teknologi kecerdasan buatan. 
        
        Berdomisili di Tangerang, beliau mendedikasikan kompetensinya untuk menciptakan 
        efisiensi bisnis bagi UMKM maupun korporasi nasional. Melalui V-Guard AI, 
        beliau memastikan bahwa setiap unit bisnis memiliki sistem pertahanan digital 
        yang mampu mendeteksi kebocoran finansial sebelum menjadi kerugian besar. 
        """)

elif nav == "ROI & Visi Misi":
    st.header("Visi, Misi & Simulasi ROI")
    st.info("**Visi:** Pelopor audit digital AI global untuk transparansi bisnis.")
    st.success("**Misi:** Deteksi fraud real-time dan proteksi aset UMKM.")
    st.write("---")
    
    oz = st.number_input("Input Omzet Bulanan (Rp):", value=100000000)
    rugi = oz * 0.07
    hemat = rugi * 0.9
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric("Potensi Rugi (7%)", f"Rp {rugi:,.0f}")
    with c2:
        st.metric("Aset Terselamatkan", f"Rp {hemat:,.0f}", delta="90% Efektif")

elif nav == "Layanan & Biaya":
    st.header("Paket Layanan & Biaya Bulanan")
    wa_ceo = "https://wa.me/628212190885?text=Halo%20CEO%20V-Guard%20AI,%20saya%20tertarik%20Paket%20"
    
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.subheader("BASIC")
            st.write("Rp 1.500.000 / bln")
            st.link_button("Pesan BASIC", wa_ceo + "BASIC")
    with c2:
        with st.container(border=True):
            st.subheader("SMART")
            st.write("Rp 2.500.000
