import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE USER & SESSION ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "Eksekutif", "Paket": "MASTER"},
        {"User ID": "siska", "Password": "p", "Level": "Klien", "Paket": "SMART"}
    ]
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 3. SIDEBAR (FOTO & WHATSAPP) ---
with st.sidebar:
    st.title("V-GUARD AI")
    # Pastikan file foto Bapak bernama 'erwin.jpg' ada di folder yang sama dengan app.py
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Erwin Sinaga")
    else:
        st.warning("Foto 'erwin.jpg' tidak ditemukan di folder.")
    
    st.markdown("### **Erwin Sinaga**")
    st.caption("Senior Business Leader")
    st.write("---")
    
    # Navigasi Tanpa Emoji untuk menghindari SyntaxError
    nav = st.radio("Menu Utama:", [
        "Profil Founder", 
        "Visi Misi dan ROI", 
        "Produk dan Layanan", 
        "Register dan Dashboard", 
        "Akses Admin"
    ])
    
    st.write("---")
    st.link_button("Hubungi Saya (WhatsApp)", "https://wa.me/628212190885")

# --- 4. LOGIKA MENU ---

if nav == "Profil Founder":
    st.header("Profil Kepemimpinan")
    with st.container(border=True):
        st.write("""Bapak **Erwin Sinaga** adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Beliau memahami bahwa di era digital saat ini, integritas data dan keamanan aset adalah fondasi utama bagi setiap unit bisnis untuk dapat tumbuh secara berkelanjutan. Melalui dedikasi yang tinggi terhadap transparansi, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan mendesak para pengusaha akan sistem perlindungan aset yang berbasis teknologi kecerdasan buatan mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif dan efisien. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit real-time yang mampu meminimalisir risiko kerugian modal secara signifikan.""")

elif nav == "Visi Misi dan ROI":
    st.header("Visi, Misi & Analisis ROI")
    c1, c2 = st.columns(2)
    with c1:
        st.info("**Visi Kami**\n\nMenjadi pelopor global audit digital berbasis AI yang menjamin transparansi mutlak.")
    with c2:
        st.success("**Misi Kami**\n\nIntegrasi AI deteksi fraud real-time & pemberdayaan UMKM dengan sistem aman.")
    
    st.write("---")
    st.subheader("Simulasi ROI Kerugian Klien")
    with st.container(border=True):
        oz = st.number_input("Masukkan Total Omzet Bulanan (Rp):", value=100000000)
        leakage = oz * 0.07
        st.error(f"Potensi Kerugian Akibat Kebocoran (7%): Rp {leakage:,.0f}")
        st.success(f"Penyelamatan Aset Bulanan: Rp {leakage * 0.85:,.0f}")

elif nav == "Produk dan Layanan":
    st.header("Paket Layanan & Pemesanan")
    st.write("Silakan pilih paket. Tombol akan langsung terhubung ke WhatsApp Bapak.")
    
    # Link WhatsApp Otomatis
    wa_base = "https://wa.me/628212190885?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20"
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        with st.container(border=True):
            st.subheader("BASIC")
            st.write("**Rp 1.500.000**")
            st.write("- AI Monitor Dasar\n- Laporan Bulanan")
            st.link_button("Pesan Paket BASIC", wa_base + "Paket%20BASIC")
            
    with col_b:
        with st.container(border=True):
            st.subheader("SMART")
            st.write("**Rp 2.500.000**")
            st.write("- Monitoring Real-Time\n- VCS System Integrasi")
            st.link_button("Pesan Paket SMART", wa_base + "Paket%20SMART")
            
    with col_c:
        with st.container(border=True):
            st.subheader("PRO")
            st.write("**Rp 5.000.000**")
            st.write("- Forensik Digital Full\n- Multi-Cabang Sinkron")
            st.link_button("Pesan Paket PRO", wa_base + "Paket%
