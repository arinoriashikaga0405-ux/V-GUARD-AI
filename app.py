import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATA CONSTANTS ---
num_wa_adm = "628212190885" # Nomor WA Admin
wa_base_adm = f"https://wa.me/{num_wa_adm}?text=Halo%20Admin%20V-Guard%20AI,%20saya%20tertarik%20"

# --- 3. DATABASE (Siska Sudah Dihapus) ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "Eksekutif", "Paket": "MASTER"}
    ]
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 4. CSS TAMPILAN PREMIUM & MODEREN ---
st.markdown("""
<style>
    /* Global Styles */
    .stApp { background-color: #f4f7f6; }
    div.stButton > button:first-child { background-color: #1e3a8a; color: white; border-radius: 8px; border: none; padding: 10px 20px; font-weight: bold; }
    div.stButton > button:first-child:hover { background-color: #152b61; color: white; border: none; }
    h1, h2, h3 { color: #1e3a8a; font-family: 'Helvetica Neue', sans-serif; }

    /* Card Founder */
    .founder-card { background-color: white; padding: 30px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); border-left: 5px solid #1e3a8a; margin-bottom: 25px; }
    .founder-text { font-size: 1.1em; color: #444; line-height: 1.8; text-align: justify; }

    /* ROI Metric Cards */
    .metric-container { background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.03); text-align: center; margin-bottom: 20px; border: 1px solid #e0e0e0; }
    .metric-title { font-size: 0.9em; color: #666; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; }
    .metric-value { font-size: 2.2em; color: #1e3a8a; font-weight: 800; margin: 10px 0; }
    .metric-rugi { color: #dc2626 !important; }

    /* Pricing Table Keren & Menarik */
    .pricing-card { background-color: white; padding: 30px; border-radius: 15px; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.05); height: 480px; border: 1px solid #e0e0e0; transition: transform 0.3s; }
    .pricing-card:hover { transform: translateY(-10px); box-shadow: 0 15px 35px rgba(0,0,0,0.1); border: 2px solid #1e3a8a; }
    .price-title { font-size: 1.5em; color: #1e3a8a; font-weight: bold; text-transform: uppercase; letter-spacing: 1.5px; }
    .price-tag { font-size: 2.8em; color: #333; font-weight: 800; margin: 15px 0; }
    .price-sub { font-size: 0.9em; color: #888; margin-top: -10px; margin-bottom: 20px;}
    .feature-list { text-align: left; color: #555; font-size: 0.95em; line-height: 2.1; margin-bottom: 25px; list-style-type: none; padding: 0; }
    .feature-list li:before { content: "✓ "; color: #1e3a8a; font-weight: bold; }
    .pricing-btn { background-color: #25d366; color: white !important; padding: 12px 25px; border-radius: 50px; text-decoration: none; font-weight: bold; display: inline-block; width: 100%; transition: background 0.3s; }
    .pricing-btn:hover { background-color: #1a9e4d; }
    .master-btn { background-color: #0f172a !important; }
    .master-btn:hover { background-color: #1a233a !important; }
</style>
""", unsafe_allow_html=True)

# --- 5. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    # FOTO FOUNDER
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    
    #branding Sejajar: Erwin Sinaga - Founder (CEO Dihapus)
    st.markdown('<p style="font-size:15px; color:#64748b; font-weight:500;">Erwin Sinaga — Founder</p>', unsafe_allow_html=True)
    
    st.write("---")
    menu = [
        "1. Profil Kepemimpinan",
        "2. Daftar Harga Modern",
        "3. ROI & Visi Misi",
        "4. Register Pelanggan",
        "5. Dashboard Login",
        "6. Admin Panel"
    ]
    nav = st.radio("Navigasi:", menu)
    st.write("---")
    st.markdown(f'<a href="https://wa.me/{num_wa_adm}" target="_blank" style="background-color: #25d366; color: white; padding: 12px 25px; border-radius: 8px; text-decoration: none; font-weight: bold; display: block; text-align: center;">💬 Hubungi Admin</a>', unsafe_allow_html=True)

# --- 6. LOGIKA MENU ---

if nav == "1. Profil Kepemimpinan":
    st.header("Profil Kepemimpinan")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # Menambahkan Foto Bapak di dalam isi profil
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga — Founder V-Guard AI", use_container_width=True)
    with col2:
        st.markdown('<div class="founder-card"><div class="founder-text">', unsafe_allow_html=True)
        # Teks 200 Kata Profesional
        st.write("""Bapak **Erwin Sinaga** adalah **Founder V-Guard AI** yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Beliau memahami bahwa di era digital saat ini, integritas data dan keamanan aset adalah fondasi utama bagi setiap unit bisnis untuk dapat tumbuh secara berkelanjutan.

Melalui dedikasi yang tinggi terhadap transparansi, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan mendesak para pengusaha akan sistem perlindungan aset yang berbasis teknologi kecerdasan buatan mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif dan efisien. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit real-time yang mampu meminimalisir risiko kerugian modal secara signifikan bagi pelaku UMKM maupun korporasi nasional. Beliau dikenal sebagai pemimpin yang inovatif dan berkomitmen penuh pada pemberdayaan industri melalui integrasi teknologi pertahanan digital.""")
        st.markdown('</div></div>', unsafe_allow_html=True)

elif nav == "2. Daftar Harga Modern":
    st.header("Price List V-Guard AI (Premium)")
    st.write("Silakan pilih paket investasi perlindungan aset yang sesuai dengan skala bisnis Anda.")
    
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.markdown('<div class="pricing-card"><div class="price-title">BASIC</div><div class="price-tag">Rp 1.5jt</div><div class="price-sub">/ bulan</div><hr><ul class="feature-list"><li>AI Monitor Dasar</li><li>Laporan Bulanan</li><li>Notifikasi Fraud SMS</li><li>UMKM Kecil (1 Cabang)</li><li>Support via Email</li></ul></div>', unsafe_allow_html=True)
        st.markdown(f'<a href="{wa_base_adm}Paket%20BASIC" target="_blank" class="pricing-btn">💬 Pesan BASIC</a>', unsafe_allow_html=True)
            
    with col_b:
        # Tampilan menonjol untuk paket terpopuler
        st.markdown('<div class="pricing-card" style="border: 2px solid #1e3a8a;"><div class="price-title">SMART</div><div class="price-tag">Rp 2.5jt</div><div class="price-sub">/ bulan</div>
