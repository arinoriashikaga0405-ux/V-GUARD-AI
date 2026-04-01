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
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 3. CSS CUSTOM ---
st.markdown("""
<style>
    .status-box { background-color: #e3f2fd; padding: 15px; border-radius: 8px; color: #1e3a8a; font-weight: bold; }
    .wa-btn { background-color: #25d366; color: white; padding: 10px 20px; border-radius: 50px; text-decoration: none; font-weight: bold; display: inline-block; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.markdown("**Erwin Sinaga**\nSenior Business Leader")
    st.write("---")
    nav = st.radio("Menu:", ["1. Profil", "2. ROI", "3. Layanan", "4. Dashboard", "5. Admin"])
    st.write("---")
    st.markdown('<a href="https://wa.me/628212190885" class="wa-btn">💬 WhatsApp</a>', unsafe_allow_html=True)

# --- 5. LOGIKA MENU ---

if nav == "1. Profil":
    st.header("Profil Kepemimpinan")
    st.write("""Bapak **Erwin Sinaga** adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Beliau memahami bahwa di era digital saat ini, integritas data dan keamanan aset adalah fondasi utama bagi setiap unit bisnis untuk dapat tumbuh secara berkelanjutan. Melalui dedikasi yang tinggi terhadap transparansi, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan mendesak para pengusaha akan sistem perlindungan aset yang berbasis teknologi kecerdasan buatan mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif dan efisien. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit real-time yang mampu meminimalisir risiko kerugian modal secara signifikan.""")

elif nav == "2. ROI":
    st.header("Visi, Misi & ROI")
    st.info("**Visi:** Menjadi pelopor global audit digital berbasis AI.")
    # Teks Misi dibuat pendek agar tidak error
    st.write("**Misi:**")
    st.write("- Integrasi AI untuk deteksi fraud.")
    st.write("- Memberdayakan UMKM dengan sistem aman.")
    st.write("---")
    oz = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    st.error(f"Potensi Kerugian (7%): Rp {oz * 0.07:,.0f}")

elif nav == "3. Layanan":
    st.header("Layanan Unggulan")
    st.markdown("- **BASIC (1.5jt):** Monitor & Laporan.")
    st.markdown("- **SMART (2.5jt):** Real-Time & VCS System.")
    st.markdown("- **PRO (5.0jt):** Forensik & Multi-Cabang.")

elif nav == "4. Dashboard":
    t1, t2 = st.tabs(["📝 Registrasi", "🔑 Login"])
    with t1:
        with st.form("f1"):
            st.text_input("Nama:")
            st.text_input("Usaha:")
            st.selectbox("Paket:", ["BASIC", "SMART", "PRO"])
            st.text_input("Harga:")
            st.file_uploader("Upload KTP:", type=["jpg", "png"])
            if st.form_submit_button("KIRIM"):
                st.success("Data Terkirim!")
    with t2:
        if not st.session_state.cl_in:
            u = st.text_input("User ID:")
            p = st.text_input("Pass:", type="password")
            if st.button("LOGIN"):
                user = next((c for c in st.session_state.user_creds if c["User ID"] == u and c["Password"] == p), None)
                if user:
                    st.session_state.cl_in = True
                    st.session_state.current_user = user
                    st.rerun()
                else: st.error("Gagal Login")
        else:
            st.markdown(f'<div class="status-box">Paket: {st.session_state.current_user["Paket"]}</div>', unsafe_allow_html=True)
            if st.button("Keluar"):
                st.session_state.cl_in = False
                st.rerun()

elif nav == "5. Admin":
    pa = st.text_input("Pass Admin:", type="password")
    if st.button("MASUK"):
        if pa == "w1nbju8282":
            st.success("Halo Pak Erwin!")
            st.table(pd.DataFrame(st.session_state.user_creds))
        else: st.error("Ditolak")

st.write("---")
st.caption("© 2026 V-Guard AI | Secured by Erwin Sinaga")
