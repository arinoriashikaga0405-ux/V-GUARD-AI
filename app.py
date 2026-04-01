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

if 'client_logged_in' not in st.session_state: st.session_state.client_logged_in = False
if 'auth_admin' not in st.session_state: st.session_state.auth_admin = False

# --- 3. CSS TAMPILAN PREMIUM ---
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .status-box { background-color: #e3f2fd; padding: 15px; border-radius: 8px; color: #1e3a8a; font-weight: bold; margin-bottom: 5px; }
    .package-box { background-color: #fff3e0; padding: 8px 15px; border-radius: 8px; color: #e65100; font-weight: bold; display: inline-block; margin-bottom: 20px; border: 1px solid #ffe0b2; }
    .service-card { background-color: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #e0e0e0; text-align: center; height: 380px; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .wa-button { background-color: #25d366; color: white; padding: 10px 20px; border-radius: 50px; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR NAVIGASI 1-5 ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Erwin Sinaga")
    st.markdown("**Erwin Sinaga**\nSenior Business Leader")
    st.write("---")
    nav = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 💎 Layanan & Produk", 
        "4. 📝 Registrasi & Dashboard", 
        "5. 🔐 Akses Terbatas"
    ])
    st.write("---")
    st.markdown(f'<a href="https://wa.me/628212190885" class="wa-button">💬 Chat WhatsApp</a>', unsafe_allow_html=True)

# --- 5. LOGIKA MENU ---

if nav == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", use_container_width=True)
        else:
            st.info("Letakkan file 'erwin.jpg' di folder aplikasi untuk menampilkan foto.")
    with col2:
        st.write("""Bapak **Erwin Sinaga** adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Beliau memahami bahwa di era digital saat ini, integritas data dan keamanan aset adalah fondasi utama bagi setiap unit bisnis untuk dapat tumbuh secara berkelanjutan.

Melalui dedikasi yang tinggi terhadap transparansi, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan mendesak para pengusaha akan sistem perlindungan aset yang berbasis teknologi kecerdasan buatan mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif dan efisien. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit real-time yang mampu meminimalisir risiko kerugian modal secara signifikan bagi pelaku UMKM maupun korporasi.""")

elif nav == "2. 🎯 Visi, Misi & ROI":
    st.header("Strategi Perlindungan Aset")
    with st.expander("👁️ Visi Perusahaan", expanded=True):
        st.write("Menjadi pelopor global dalam penyediaan infrastruktur audit digital berbasis AI yang menjamin transparansi mutlak bagi pemilik bisnis.")
    with st.expander("🚀 Misi Perusahaan", expanded=True):
        st.write("1. Mengintegrasikan AI untuk deteksi fraud secara real-time.\n2. Memberdayakan UMKM dengan sistem keamanan setingkat korporasi.\n3. Menghilangkan kebocoran biaya operasional melalui audit otomatis.")
    
    st.write("---")
    st.subheader("📊 Simulasi ROI & Kerugian Klien")
    oz = st.number_input("Masukkan Total Omzet Bulanan Bisnis Anda (Rp):", value=100000000)
    leakage = oz * 0.07
    st.error(f"Potensi Kerugian Akibat Kebocoran (Estimasi 7%): Rp {leakage:,.0f}")
    st.success(f"Potensi Dana Diselamatkan dengan V-Guard: Rp {leakage * 0.9:,.0f} / Bulan")

elif nav == "3. 💎 Layanan & Produk":
    st.header("Paket Layanan Unggulan")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="service-card"><h3>📦 BASIC</h3><p><b>Rp 1.500.000</b></p><hr>• AI Monitor Dasar<br>• Laporan Bulanan<br>• Notifikasi Fraud SMS<br>• Support via Email</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="service-card" style="border: 2px solid #1e3a8a;"><h3>🚀 SMART</h3><p><b>Rp 2.500.000</b></p><hr>• Monitoring Pro Real-Time<br>• Integrasi VCS System<br>• Audit Harian Otomatis<br>• Konsultasi Strategis</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="service-card"><h3>🛡️ PRO</h3><p><b>Rp 5.000.000</b></p><hr>• Forensik Digital Full<br>• Multi-Cabang AI Sinkron<br>• CCTV AI Behavior Audit<br>• Support 24/7 Dedicated</div>', unsafe_allow_html=True)

elif nav == "4. 📝
