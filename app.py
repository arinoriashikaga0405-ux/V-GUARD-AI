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
    # Link WA dengan baris pendek agar tidak terputus
    wa_link = "https://wa.me/628212190885"
    st.markdown(f'<a href="{wa_link}" target="_blank" style="background-color:#25d366;color:white;padding:10px;border-radius:8px;text-decoration:none;display:block;text-align:center;font-weight:bold;">💬 Hubungi Admin</a>', unsafe_allow_html=True)

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

elif nav == "Visi dan Misi":
    st.header("Visi dan Misi Perusahaan")
    st.write("---")
    v1, v2 = st.columns(2)
    with v1:
        st.info("### 🎯 Visi")
        st.write("Menjadi pelopor global dalam teknologi audit digital berbasis AI yang menjamin transparansi dan keamanan aset mutlak bagi setiap pelaku bisnis.")
    with v2:
        st.success("### 🚀 Misi")
        st.write("""
        1. Memberikan proteksi aset melalui deteksi fraud real-time.
        2. Mendukung UMKM dan Korporasi dalam efisiensi operasional.
        3. Mewujudkan tata kelola bisnis yang bersih dan bebas dari kebocoran finansial.
        """)

elif nav == "Daftar Produk Utama":
    st.header("Daftar Produk Utama & Analisis ROI")
    
    # ROI Calculator
    with st.expander("📊 Simulasi ROI (Return on Investment)", expanded=True):
        oz = st.number_input("Omzet Bulanan (Rp):", value=100000000)
        rugi = oz * 0.07
        c_r1, c_r2 = st.columns(2)
        c_r1.metric("Potensi Rugi (7%)", f"Rp {rugi:,.0f}")
        c_r2.metric("Aset Aman V-Guard", f"Rp {rugi*0.9:,.0f}")

    st.write("---")
    wa_pesan = "https://wa.me/628212190885?text=Pesan%20"
    c1, c2 = st.columns(2)
    
    with c1:
        with st.container(border=True):
            st.subheader("📦 V-LITE (Basic)")
            st.write("- Alarm Fraud: Notif WA\n- Invoice: Digital Notif\n- Laba Rugi: Bulanan\n- Audit: Self-Audit")
            st.write("**Pasang: 1jt | Bulan: 1jt**")
            st.link_button("Pesan V-LITE", wa_pesan + "VLITE")

        with st.container(border=True):
            st.subheader("👁️ V-SIGHT (Visual)")
            st.write("- Alarm Fraud: Real-Time + Foto\n- Invoice: Sync Struk & Video\n- Laba Rugi: ROI Analisis\n- Audit: Perilaku Visual")
            st.write("**Pasang: 3.5jt | Bulan: 4.5jt**")
            st.link_button("Pesan V-SIGHT", wa_pesan + "VSIGHT")

    with c2:
        with st.container(border=True):
            st.subheader("🚀 V-PRO (Standard)")
            st.write("- Alarm Fraud: Real-Time Push\n- Invoice: Auto-Invoice & Stok\n- Laba Rugi: Harian (P&L)\n- Audit: Audit AI Otomatis")
            st.write("**Pasang: 2jt | Bulan: 2.5jt**")
            st.link_button("Pesan V-PRO", wa_pesan + "VPRO")

        with st.container(border=True):
            st.subheader("🏢 V-ENTERPRISE")
            st.write("- Alarm Fraud: Investigasi Tim\n- Invoice: Custom API\n- Laba Rugi: Konsolidasi Cabang\n- Audit: Forensik Digital")
            st.write("**Pasang: Custom | Bulan: 10jt++**")
            st.link_button("Hubungi Admin", wa_pesan + "ENTERPRISE")

elif nav == "Register Pelanggan":
    st.header("Pendaftaran Pelanggan Baru")
    with st.form("f_reg"):
        st.text_input("Nama Pemilik:")
        st.text_input("Nama Usaha:")
        st.selectbox("Menu Harga & Paket:", [
            "V-LITE (Pasang 1jt - Bulan 1jt)",
            "V-PRO (Pasang 2jt - Bulan 2.5jt)",
            "V-SIGHT (Pasang 3.5jt - Bulan 4.5jt)",
            "V-ENTERPRISE (Custom)"
        ])
        st.file_uploader("Upload KTP Pemilik:", type=["jpg", "png", "jpeg"])
        if st.form_submit_button("Kirim Pendaftaran"):
            st.success("Terkirim! Admin akan segera memproses.")

elif nav == "Dashboard Login":
    st.header("Portal Klien")
    st.text_input("User ID:")
    st.text_input("Password:", type="password")
    st.button("Masuk")

elif nav == "Admin Panel":
    st.header("Executive Control Panel")
    pwd = st.text_input("Sandi Otoritas:", type="password")
    if st.button("Buka Data"):
        if pwd == "w1nbju8282":
            st.success("Selamat Datang Founder Bapak Erwin Sinaga.")
        else: st.error("Akses Ditolak")

st.write("---")
st.caption("© 2026 V-Guard AI Intelligence | Erwin Sinaga — Founder")
