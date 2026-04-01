import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE USER (Password Admin: w1nbju8282) ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "Eksekutif", "Paket": "MASTER"},
        {"User ID": "siska", "Password": "p", "Level": "Klien", "Paket": "SMART"}
    ]
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 3. SIDEBAR (FOTO & WA) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    # Bagian Foto: Pastikan file bernama 'erwin.jpg' ada di folder yang sama
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Erwin Sinaga", use_container_width=True)
    else:
        st.info("Simpan foto Bapak dengan nama 'erwin.jpg' di folder aplikasi agar muncul di sini.")
    
    st.markdown("### **Erwin Sinaga**")
    st.caption("Senior Business Leader")
    st.write("---")
    nav = st.radio("Menu Utama:", [
        "👤 Profil Founder", 
        "🎯 Visi, Misi & ROI", 
        "💎 Produk & Layanan", 
        "📝 Register & Dashboard", 
        "🔐 Akses Admin"
    ])
    st.write("---")
    st.link_button("💬 Hubungi Saya (WhatsApp)", "https://wa.me/628212190885", use_container_width=True)

# --- 4. LOGIKA MENU ---

if nav == "👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    with st.container(border=True):
        st.write("""Bapak **Erwin Sinaga** adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Beliau memahami bahwa di era digital saat ini, integritas data dan keamanan aset adalah fondasi utama bagi setiap unit bisnis untuk dapat tumbuh secara berkelanjutan. Melalui dedikasi yang tinggi terhadap transparansi, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan mendesak para pengusaha akan sistem perlindungan aset yang berbasis teknologi kecerdasan buatan mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif dan efisien. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit real-time yang mampu meminimalisir risiko kerugian modal secara signifikan.""")

elif nav == "🎯 Visi, Misi & ROI":
    st.header("Visi, Misi & ROI")
    c1, c2 = st.columns(2)
    with c1: st.info("**👁️ Visi Kami**\n\nMenjadi pelopor global audit digital berbasis AI.")
    with c2: st.success("**🚀 Misi Kami**\n\nIntegrasi AI deteksi fraud & pemberdayaan UMKM.")
    st.write("---")
    with st.container(border=True):
        oz = st.number_input("Input Omzet Bulanan (Rp):", value=100000000)
        leak = oz * 0.07
        st.error(f"Potensi Kerugian (7%): Rp {leak:,.0f}")
        st.success(f"Potensi Penyelamatan: Rp {leak * 0.85:,.0f}")

elif nav == "💎
