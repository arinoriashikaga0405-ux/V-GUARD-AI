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

# --- 3. CSS TAMPILAN KEREN & MODERN ---
st.markdown("""
<style>
    .main { background-color: #f0f2f6; }
    .stApp { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
    .card {
        background-color: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px;
        border-left: 5px solid #1e3a8a;
    }
    .feature-list { color: #444; font-size: 0.9em; line-height: 1.6; }
    .wa-btn {
        background-color: #25d366; color: white !important;
        padding: 12px 25px; border-radius: 30px;
        text-decoration: none; font-weight: bold;
        display: inline-block; text-align: center; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR NAVIGASI ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    # FOTO FOUNDER
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    else:
        st.warning("Unggah file 'erwin.jpg' ke folder VGUARD_AI_APP agar foto muncul.")
    
    st.markdown("### **Erwin Sinaga**")
    st.caption("Senior Business Leader")
    st.write("---")
    nav = st.radio("Navigasi Utama:", [
        "👤 Profil Founder", 
        "🎯 Visi, Misi & ROI", 
        "💎 Produk & Layanan", 
        "📝 Register & Dashboard", 
        "🔐 Akses Admin"
    ])
    st.write("---")
    # TOMBOL WHATSAPP
    st.markdown('<a href="https://wa.me/628212190885" class="wa-btn">💬 Chat WhatsApp</a>', unsafe_allow_html=True)

# --- 5. LOGIKA MENU ---

if nav == "👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("""Bapak **Erwin Sinaga** adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Beliau memahami bahwa di era digital saat ini, integritas data dan keamanan aset adalah fondasi utama bagi setiap unit bisnis untuk dapat tumbuh secara berkelanjutan. Melalui dedikasi yang tinggi terhadap transparansi, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan mendesak para pengusaha akan sistem perlindungan aset yang berbasis teknologi kecerdasan buatan mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif dan efisien. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit real-time yang mampu meminimalisir risiko kerugian modal secara signifikan.""")
    st.markdown('</div>', unsafe_allow_html=True)

elif nav == "🎯 Visi, Misi & ROI":
    st.header("Strategi & Analisis ROI")
    
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("👁️ Visi Kami", expanded=True):
            st.info("Menjadi pelopor global audit digital berbasis AI yang menjamin transparansi mutlak.")
    with col2:
        with st.expander("🚀 Misi Kami", expanded=True):
            st.success("Integrasi AI deteksi fraud real-time & pemberdayaan UMKM dengan sistem aman.")

    st.write("---")
    st.subheader("📊 Simulasi ROI Kerugian Klien")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    oz = st.number_input("Masukkan Total Omzet Bulanan (Rp):", value=100000000)
    leakage = oz * 0.07
    st.error(f"Potensi Kerugian Akibat Kebocoran (7%): Rp {leakage:,.0f}")
    st.info(f"Penyelamatan Aset Bulanan: Rp {leakage * 0.85:,.0f}")
    st.markdown('</div>', unsafe_allow_html=True)

elif nav == "💎 Produk & Layanan":
    st.header("Paket Layanan Unggulan")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="card"><h3>📦 BASIC</h3><p><b>Rp 1.500.000</b></p><hr><div class="feature-list">• AI Monitor Dasar<br>• Laporan Bulanan<br>• Notifikasi Fraud SMS</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="
