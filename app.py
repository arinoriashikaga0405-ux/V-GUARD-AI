import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. STATUS LOGIN ---
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 3. SIDEBAR (Navigasi Bersih) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    
    # Update Nama Menu sesuai Instruksi
    menu = [
        "Profil Kepemimpinan", 
        "Daftar Produk Utama", 
        "Register Pelanggan", 
        "Dashboard Login", 
        "Admin Panel"
    ]
    nav = st.radio("Navigasi Utama:", menu)
    st.write("---")
    st.markdown('<a href="https://wa.me/628212190885" target="_blank" style="background-color:#25d366;color:white;padding:10px;border-radius:8px;text-decoration:none;display:block;text-align:center;font-weight:bold;">💬 Hubungi Admin</a>', unsafe_allow_html=True)

# --- 4. LOGIKA MENU ---

if nav == "Profil Kepemimpinan":
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga — Founder")
    with col2:
        with st.container(border=True):
            # Narasi 200 Kata Profesional
            st.write("""
            Bapak **Erwin Sinaga** adalah sosok **Founder** di balik **V-Guard AI Intelligence**, sebuah platform inovatif yang lahir dari dedikasi mendalam terhadap keamanan aset dan transparansi bisnis. Beliau memiliki rekam jejak profesional yang prestisius selama lebih dari satu dekade, menempati berbagai posisi strategis dan manajerial senior di industri perbankan serta manajemen aset nasional. Pengalaman panjang tersebut telah membentuk ketajaman analitis beliau dalam mengidentifikasi berbagai pola risiko finansial dan celah operasional yang sering kali luput dari sistem pengawasan konvensional.

            Di bawah visi kepemimpinannya, V-Guard AI dikembangkan bukan sekadar sebagai alat audit, melainkan sebagai benteng pertahanan digital bagi para pengusaha. Beliau sangat memahami bahwa integritas data dan perlindungan modal adalah fondasi utama bagi keberlanjutan bisnis di era digital yang penuh tantangan. Berdomisili di Tangerang, beliau aktif menjembatani kebutuhan dunia usaha dengan solusi teknologi kecerdasan buatan yang aplikatif dan efisien. Fokus utama beliau adalah memberikan ketenangan pikiran bagi pemilik usaha melalui sistem audit real-time yang mampu meminimalisir potensi kerugian secara signifikan. Bapak Erwin dikenal sebagai pemimpin yang visioner, disiplin, dan memiliki komitmen tanpa kompromi dalam membantu UMKM hingga korporasi besar mencapai standar tata kelola bisnis yang bersih, aman, dan berkelanjutan.
            """)

elif nav == "Daftar Produk Utama":
    st.header("Solusi Keamanan Aset V-Guard AI")
    st.info("Fitur Wajib: Alarm Fraud, Invoice Notif, Laporan Rugi Laba, & Laporan Audit")
    
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.subheader("📦 V-LITE (Basic)")
            st.write("""
            - **Alarm Fraud:** Notifikasi WA Berkala
            - **Invoice:** Digital Notifikasi Standar
            - **Laporan:** Rugi Laba Bulanan
            - **Audit:** Laporan Self-Audit (Bulanan)
            """)
            st.write("💰 **Pasang:** 1jt | **Bulan:** 1jt")
            st.link_button("Pesan V-LITE", "https://wa.me/628212190885?text=Pesan%20V-LITE")

        with st.container(border=True):
            st.subheader("👁️ V-SIGHT (Visual)")
            st.write("""
            - **Alarm Fraud:** Real-Time + Bukti Foto AI
            - **Invoice:** Sinkronisasi Struk & Video
            - **Laporan:** Analisis ROI Aset & Laba Rugi
            - **Audit:** Audit Perilaku Visual AI
            """)
            st.write("💰 **Pasang:** 3.5jt | **Bulan:** 4.5jt")
            st.link_button("Pesan V-SIGHT", "https://wa.me/628212190885?text=Pesan%20V-SIGHT")

    with c2:
        with st.container(border=True):
            st.subheader("🚀 V-PRO (Standard)")
            st.write("""
            - **Alarm Fraud:** Real-Time Push Notification
            - **Invoice:** Auto-Invoice & Update Stok
            - **Laporan:** Rugi Laba Harian (P&L)
            - **Audit:** Laporan Audit AI Otomatis
            """)
            st.write("💰 **Pasang:** 2jt | **Bulan:** 2.5jt")
            st.link_button("Pesan V-PRO", "https://wa.me/628212190885?text=Pesan%20V-PRO")

        with st.container(border=True):
            st.subheader("🏢 V-ENTERPRISE")
            st.write("""
            - **Alarm Fraud:** Investigasi Tim Khusus
            - **Invoice:** Custom Billing API & ERP
            - **Laporan:** Konsolidasi Multi-Cabang
            - **Audit:** Investigasi Forensik Digital
            """)
            st.write("💰 **Pasang:** Custom | **Bulan:** 10jt++")
            st.link_button("Hubungi Admin", "https://wa.me/628212190885?text=Pesan%20ENTERPRISE")

elif nav == "Register Pelanggan":
    st.header("Pendaftaran Pelanggan Baru")
    with st.form("f_reg"):
        st.text_input("Nama Lengkap Pemilik:")
        st.text_input("Nama Usaha / Perusahaan:")
        # Menambahkan Menu Harga/Paket sesuai instruksi
        st.selectbox("Pilih Menu Harga & Paket:", [
            "V-LITE (Pasang 1jt - Bulanan 1jt)",
            "V-PRO (Pasang 2jt - Bulanan 2.5jt)",
            "V-SIGHT (Pasang 3.5jt - Bulanan 4.5jt)",
            "V-ENTERPRISE (Project Based)"
        ])
        st.file_uploader("Upload Foto KTP Pemilik:", type=["jpg", "png", "jpeg"])
        if st.form_submit_button("Kirim Pendaftaran"):
            st.success("Data telah terkirim. Admin akan segera memproses verifikasi Bapak.")

elif nav == "Dashboard Login":
    st.header("Portal Klien V-Guard AI")
    st.text_input("User ID:")
    st.text_input("Password:", type="password")
    st.button("Masuk")

elif nav == "Admin Panel":
    st.header("Executive Control Panel")
    pwd = st.text_input("Sandi Otoritas:", type="password")
    if st.button("Buka Data"):
        if pwd == "w1nbju8282":
            st.success("Selamat Datang Bapak Erwin Sinaga.")
        else: st.error("Akses Ditolak")

st.write("---")
st.caption("© 2026 V-Guard AI Intelligence | Erwin Sinaga — Founder")
