import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. PENYIMPANAN STATUS (Agar Admin Tidak Ter-Logout Sendiri) ---
if 'admin_authed' not in st.session_state:
    st.session_state.admin_authed = False

# --- 3. SIDEBAR (URUTAN NAVIGASI STATIS) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    
    # Urutan Navigasi Sesuai SOP Bapak
    menu = [
        "Profil Kepemimpinan", 
        "Visi dan Misi",
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
            st.write("""
            Bapak **Erwin Sinaga** adalah sosok **Founder** di balik **V-Guard AI Intelligence**, sebuah platform inovatif yang lahir dari dedikasi mendalam terhadap keamanan aset dan transparansi bisnis. Beliau memiliki rekam jejak profesional yang prestisius selama lebih dari satu dekade, menempati berbagai posisi strategis dan manajerial senior di industri perbankan serta manajemen aset nasional. Pengalaman panjang tersebut telah membentuk ketajaman analitis beliau dalam mengidentifikasi berbagai pola risiko finansial dan celah operasional yang sering kali luput dari sistem pengawasan konvensional.

            Di bawah visi kepemimpinannya, V-Guard AI dikembangkan bukan sekadar sebagai alat audit, melainkan sebagai benteng pertahanan digital bagi para pengusaha. Beliau sangat memahami bahwa integritas data dan perlindungan modal adalah fondasi utama bagi keberlanjutan bisnis di era digital yang penuh tantangan. Berdomisili di Tangerang, beliau aktif menjembatani kebutuhan dunia usaha dengan solusi teknologi kecerdasan buatan yang aplikatif dan efisien. Fokus utama beliau adalah memberikan ketenangan pikiran bagi pemilik usaha melalui sistem audit real-time yang mampu meminimalisir potensi kerugian secara signifikan. Bapak Erwin dikenal sebagai pemimpin yang visioner, disiplin, dan memiliki komitmen tanpa kompromi dalam membantu UMKM hingga korporasi besar mencapai standar tata kelola bisnis yang bersih, aman, dan berkelanjutan.
            """)

elif nav == "Visi dan Misi":
    st.header("Visi dan Misi Perusahaan")
    v1, v2 = st.columns(2)
    with v1:
        st.info("### 🎯 Visi\nMenjadi pelopor global teknologi audit digital berbasis AI yang menjamin transparansi mutlak.")
    with v2:
        st.success("### 🚀 Misi\n1. Proteksi aset via Fraud Detection.\n2. Efisiensi operasional.\n3. Bisnis bebas kebocoran.")

elif nav == "Daftar Produk Utama":
    st.header("Daftar Produk & Analisis ROI")
    with st.expander("📊 Simulasi ROI (Return on Investment)", expanded=True):
        oz = st.number_input("Omzet Bulanan Bisnis (Rp):", value=100000000)
        rugi = oz * 0.07
        st.metric("Potensi Rugi Tanpa AI (7%)", f"Rp {rugi:,.0f}")
        st.metric("Aset Aman V-Guard AI", f"Rp {rugi*0.9:,.0f}")
    
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.subheader("📦 V-LITE")
            st.write("- **Alarm Fraud:** WA\n- **Invoice:** Digital\n- **Laba Rugi:** Bulanan\n- **Audit:** Self-Audit")
            st.write("**Pasang: 1jt | Bulan: 1jt**")
        with st.container(border=True):
            st.subheader("👁️ V-SIGHT")
            st.write("- **Alarm Fraud:** Real-Time + Foto\n- **Invoice:** Sync Video\n- **Laba Rugi:** ROI Analisis\n- **Audit:** Visual AI")
            st.write("**Pasang: 3.5jt | Bulan: 4.5jt**")
    with c2:
        with st.container(border=True):
            st.subheader("🚀 V-PRO")
            st.write("- **Alarm Fraud:** Real-Time Push\n- **Invoice:** Auto-Sync\n- **Laba Rugi:** Harian\n- **Audit:** AI Otomatis")
            st.write("**Pasang: 2jt | Bulan: 2.5jt**")
        with st.container(border=True):
            st.subheader("🏢 V-ENTERPRISE")
            st.write("- **Alarm Fraud:** Tim Investigasi\n- **Invoice:** Custom API\n- **Laba Rugi:** Multi-Cabang\n- **Audit:** Forensik")
            st.write("**Pasang: Custom | Bulan: 10jt++**")

elif nav == "Register Pelanggan":
    st.header("Pendaftaran Pelanggan Baru")
    with st.form("reg_form"):
        st.text_input("Nama Lengkap:")
        st.selectbox("Pilih Menu Harga & Paket:", ["V-LITE (1jt)", "V-PRO (2.5jt)", "V-SIGHT (4.5jt)", "V-ENTERPRISE"])
        st.file_uploader("Upload KTP:", type=["jpg", "png", "jpeg"])
        if st.form_submit_button("Kirim"):
            st.success("Terkirim!")

elif nav == "Dashboard Login":
    st.header("Portal Klien")
    st.text_input("User ID:")
    st.text_input("Password:", type="password")
    st.button("Masuk")

elif nav == "Admin Panel":
    st.header("🛡️ CEO Executive Panel")
    
    if not st.session_state.admin_authed:
        pwd = st.text_input("Sandi Otoritas:", type="password")
        if st.button("Buka Data"):
            if pwd == "w1nbju8282":
                st.session_state.admin_authed = True
                st.rerun()
            else: st.error("Sandi Salah!")
    else:
        st.success("Akses Diterima, Selamat Datang Bapak Erwin Sinaga.")
        if st.button("Logout Admin"):
            st.session_state.admin_authed = False
            st.rerun()
        
        st.write("---")
        # Dashboard Admin Aktif
        st.subheader("📈 Ringkasan Perusahaan")
        st.info("Total Pelanggan Aktif: 12 | Pendapatan: Rp 32.500.000")

st.write("---")
st.caption("© 2026 V-Guard AI Intelligence | Erwin Sinaga — Founder")
