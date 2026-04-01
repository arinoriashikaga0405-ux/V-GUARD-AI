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
    
    # Update Folder sesuai Instruksi Terbaru
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
    
    # Bagian ROI (Pindahan sesuai instruksi)
    with st.expander("📊 Cek Simulasi ROI (Return on Investment) Anda", expanded=True):
        st.write("Gunakan kalkulator ini untuk melihat potensi aset yang terselamatkan.")
        oz = st.number_input("Input Omzet Bulanan Bisnis (Rp):", value=100000000)
        rugi = oz * 0.07
        c_roi1, c_roi2 = st.columns(2)
        c_roi1.metric("Potensi Rugi Tanpa AI (7%)", f"Rp {rugi:,.0f}")
        c_roi2.metric("Aset Aman Dengan V-Guard", f"Rp {rugi*0.9:,.0f}")

    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.subheader("📦 V-LITE (Basic)")
            st.write("- **Alarm Fraud:** Notifikasi WA\n- **Invoice:** Digital Notif\n- **Laporan:** Rugi Laba Bulanan\n- **Audit:** Laporan Self-Audit")
            st.write("💰 **Pasang:** 1jt | **Bulan:** 1jt")
            st.link_button("Pesan V-LITE", "https://wa.me/628212190885?text=Pesan%20V-LITE")

        with st.container(border=True):
            st.subheader("👁️ V-SIGHT (Visual)")
            st.write("- **Alarm Fraud:** Real-Time + Foto\n- **Invoice:** Sync Struk & Video\n- **Laporan:** Analisis ROI & Laba Rugi\n- **Audit:** Audit Perilaku Visual")
            st.write("💰 **Pasang:** 3.5jt | **Bulan:** 4.5jt")
            st.link_button("Pesan V-SIGHT", "https://wa.me/628212190885?text=Pesan%20V-SIGHT")

    with c2:
        with st.container(border=True):
            st.subheader("🚀 V-PRO (Standard)")
            st.write("- **Alarm Fraud:** Real-Time Push\n- **Invoice:** Auto-Invoice & Stok\n- **Laporan:** Rugi Laba Harian\n- **Audit:** Audit AI Otomatis")
            st.write("💰 **Pasang:** 2jt | **Bulan:** 2.5jt")
            st.link_button("Pesan V-PRO", "https://wa.me/628212190885?text=Pesan%20V-PRO")

        with st.container(border=True):
            st.subheader("🏢 V-ENTERPRISE")
            st.write("- **Alarm Fraud:** Investigasi Tim\n- **Invoice:** Custom API & ERP\n- **Laporan:** Konsolidasi Cabang\n- **Audit:** Forensik Digital")
            st.write("💰 **Pasang:** Custom | **Bulan:** 10jt++")
            st.link_button("Hub
