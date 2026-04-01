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

# --- 3. CSS MODERN (DIPECAH AGAR AMAN) ---
st.markdown("""
<style>
    .stApp { background-color: #f4f7f6; }
    .founder-card { background-color: white; padding: 25px; border-radius: 15px; border-left: 5px solid #1e3a8a; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
    .pricing-card { background-color: white; padding: 20px; border-radius: 15px; text-align: center; border: 1px solid #e0e0e0; height: 400px; }
    .price-tag { font-size: 2.5em; font-weight: bold; color: #1e3a8a; }
    .wa-btn { background-color: #25d366; color: white !important; padding: 12px; border-radius: 8px; text-decoration: none; display: block; text-align: center; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    
    # Branding: Erwin Sinaga - Founder
    st.caption("Erwin Sinaga — Founder")
    
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
    st.markdown('<a href="https://wa.me/628212190885" class="wa-btn">💬 Hubungi Admin</a>', unsafe_allow_html=True)

# --- 5. LOGIKA MENU ---

if nav == "1. Profil Kepemimpinan":
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga — Founder", use_container_width=True)
    with col2:
        with st.container(border=True):
            st.write("""
            Bapak **Erwin Sinaga** adalah **Founder V-Guard AI** yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Beliau memahami bahwa di era digital saat ini, integritas data dan keamanan aset adalah fondasi utama bagi setiap unit bisnis untuk dapat tumbuh secara berkelanjutan.

            Melalui dedikasi yang tinggi terhadap transparansi, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan mendesak para pengusaha akan sistem perlindungan aset yang berbasis teknologi kecerdasan buatan mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif dan efisien. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit real-time yang mampu meminimalisir risiko kerugian modal secara signifikan bagi pelaku UMKM maupun korporasi nasional. Beliau dikenal sebagai pemimpin yang inovatif dan berkomitmen penuh pada pemberdayaan industri melalui integrasi teknologi pertahanan digital.
            """)

elif nav == "2. Daftar Harga Modern":
    st.header("Price List V-Guard AI")
    wa_adm = "https://wa.me/628212190885?text=Saya%20tertarik%20Paket%20"
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="pricing-card"><h3>BASIC</h3><div class="price-tag">1.5jt</div><p>/bulan</p><p>✓ Monitor Dasar<br>✓ Laporan Bulanan</p></div>', unsafe_allow_html=True)
        st.link_button("Pesan BASIC", wa_adm + "BASIC")
    with c2:
        st.markdown('<div class="pricing-card" style="border:2px solid #1e3a8a"><h3>SMART</h3><div class="price-tag">2.5jt</div><p>/bulan</p><p>✓ Real-Time Monitor<br>✓ VCS Integrasi</p></div>', unsafe_allow_html=True)
        st.link_button("Pesan SMART", wa_adm + "SMART")
    with c3:
        st.markdown('<div class="pricing-card"><h3>MASTER</h3><div class="price-tag">PRO</div><p>Dedicated</p><p>✓ Full Audit AI<br>✓ Multi-Cabang</p></div>', unsafe_allow_html=True)
        st.link_button("Hubungi Admin", wa_adm + "MASTER")

elif nav == "3. ROI & Visi Misi":
    st.header("Analisis Strategis")
    st.info("**Visi:** Pelopor audit digital AI global.")
    st.success("**Misi:** Deteksi fraud & proteksi aset UMKM.")
    oz = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    rugi = oz * 0.07
    st.metric("Potensi Rugi (7%)", f"Rp {rugi:,.0f}")
    st.metric("Aset Aman AI", f"Rp {rugi*0.9:,.0f}")

elif nav == "4. Register Pelanggan":
    st.header("Pendaftaran Pelanggan")
    with st.form("f_reg"):
        st.text_input("Nama Pemilik:")
        st.text_input("Nama Usaha:")
        st.selectbox("Paket:", ["BASIC", "SMART", "MASTER"])
        if st.form_submit_button("Daftar Sekarang"):
            st.success("Terkirim ke Admin!")

elif nav == "5. Dashboard Login":
    st.header("Portal Klien")
    if not st.session_state.cl_in:
        u = st.text_input("User ID:")
        p = st.text_input("Password:", type="password")
        if st.button("Masuk"):
            user = next((c for c
