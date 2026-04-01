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

# --- 3. SIDEBAR NAVIGASI ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    # FOTO FOUNDER
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    else:
        st.warning("Unggah file 'erwin.jpg' agar foto muncul.")
    
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
    # TOMBOL WHATSAPP (Link Sederhana agar tidak Error)
    wa_url = "https://wa.me/628212190885"
    st.link_button("💬 Chat WhatsApp", wa_url, use_container_width=True)

# --- 4. LOGIKA MENU ---

if nav == "👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    with st.container(border=True):
        st.write("""Bapak **Erwin Sinaga** adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Beliau memahami bahwa di era digital saat ini, integritas data dan keamanan aset adalah fondasi utama bagi setiap unit bisnis untuk dapat tumbuh secara berkelanjutan. Melalui dedikasi yang tinggi terhadap transparansi, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan mendesak para pengusaha akan sistem perlindungan aset yang berbasis teknologi kecerdasan buatan mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif dan efisien. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit real-time yang mampu meminimalisir risiko kerugian modal secara signifikan.""")

elif nav == "🎯 Visi, Misi & ROI":
    st.header("Strategi & Analisis ROI")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**👁️ Visi Kami**\n\nMenjadi pelopor global audit digital berbasis AI yang menjamin transparansi mutlak.")
    with col2:
        st.success("**🚀 Misi Kami**\n\nIntegrasi AI deteksi fraud real-time & pemberdayaan UMKM dengan sistem aman.")

    st.write("---")
    st.subheader("📊 Simulasi ROI Kerugian Klien")
    with st.container(border=True):
        oz = st.number_input("Masukkan Total Omzet Bulanan (Rp):", value=100000000)
        leakage = oz * 0.07
        st.error(f"Potensi Kerugian Akibat Kebocoran (7%): Rp {leakage:,.0f}")
        st.success(f"Penyelamatan Aset Bulanan Estimasi: Rp {leakage * 0.85:,.0f}")

elif nav == "💎 Produk & Layanan":
    st.header("Paket Layanan Unggulan")
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.subheader("📦 BASIC")
            st.write("**Rp 1.500.000**")
            st.write("- AI Monitor Dasar\n- Laporan Bulanan\n- Notifikasi Fraud SMS")
    with c2:
        with st.container(border=True):
            st.subheader("🚀 SMART")
            st.write("**Rp 2.500.000**")
            st.write("- Monitoring Real-Time\n- VCS System Integrasi\n- Audit Harian Otomatis")
    with c3:
        with st.container(border=True):
            st.subheader("🛡️ PRO")
            st.write("**Rp 5.000.000**")
            st.write("- Forensik Digital Full\n- Multi-Cabang Sinkron\n- CCTV AI Behavior")

elif nav == "📝 Register & Dashboard":
    t1, t2 = st.tabs(["📝 Form Pendaftaran", "🔑 Login Dashboard"])
    with t1:
        with st.form("reg_form"):
            st.text_input("Nama Pelanggan:")
            st.text_input("Jenis Usaha:")
            st.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO"])
            st.text_input("Harga Kesepakatan (Rp):")
            st.file_uploader("Upload Foto KTP:", type=["jpg", "png"])
            if st.form_submit_button("Kirim Pendaftaran"):
                st.success("Data berhasil terkirim ke sistem V-Guard!")
    with t2:
        if not st.session_state.cl_in:
            u = st.text_input("User ID:")
            p = st.text_input("Password:", type="password")
            if st.button("LOGIN KLIEN"):
                user = next((c for c in st.session_state.user_creds if c["User ID"] == u and c["Password"] == p), None)
                if user:
                    st.session_state.cl_in = True
                    st.session_state.current_user = user
                    st.rerun()
                else: st.error("ID atau Password Salah")
        else:
            st.info(f"Selamat Datang! Paket Anda: {st.session_state.current_user['Paket']}")
            if st.button("Logout"):
                st.session_state.cl_in = False
                st.rerun()

elif nav == "🔐 Akses Admin":
    st.header("Panel Kontrol Eksekutif")
    pa = st.text_input("Password Admin:", type="password")
    if st.button("Buka Panel"):
        if pa == "w1nbju8282":
            st.success("Halo, Pak Erwin!")
            st.table(pd.DataFrame(st.session_state.user_creds))
        else: st.error("Akses Ditolak")

st.write("---")
st.caption("© 2026 V-Guard AI Intelligence | Erwin Sinaga")
