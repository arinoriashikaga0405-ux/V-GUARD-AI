import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai
from streamlit_option_menu import option_menu

# === 1. KONFIGURASI ENGINE AI ===
# Menggunakan Key yang valid dari Bapak
K_V = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=K_V)
    v_ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# === 2. DATABASE SESSION ===
if 'db_order' not in st.session_state:
    st.session_state.db_order = []

if 'db_nasabah' not in st.session_state:
    skrg = datetime.now().date()
    # Data awal sesuai dashboard asli Bapak
    st.session_state.db_nasabah = [
        {
            "ID": 101, "Tgl": "2026-03-25", "Pelanggan": "Siska",
            "Bisnis": "Cafe Maju", "Usaha": "F&B", "Paket": "SMART", 
            "Harga": 2500000, "Jatuh_Tempo": "2026-04-25", "Status": "🟢 AKTIF"
        },
        {
            "ID": 102, "Tgl": "2026-03-28", "Pelanggan": "Jaya",
            "Bisnis": "Bengkel Berkah", "Usaha": "Otomotif", "Paket": "BASIC", 
            "Harga": 1500000, "Jatuh_Tempo": "2026-04-28", "Status": "🔴 Menunggu"
        }
    ]

if 'akses_ad' not in st.session_state:
    st.session_state.akses_ad = False

# === 3. UI STYLE PREMIUM ===
st.markdown("""
<style>
    .big-font { font-size: 24px !important; font-weight: bold; color: #1E3A8A; }
    .alarm { background: #ff4b4b; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; border: 2px solid yellow; margin-bottom: 20px; }
    .notif { background: #fff3cd; padding: 10px; border-radius: 5px; border-left: 5px solid #ffc107; margin-bottom: 5px; color: black; }
    .stTable { font-size: 14px; }
</style>
""", unsafe_allow_html=True)

# === 4. SIDEBAR (SESUAI FOTO) ===
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    else:
        st.warning("Unggah file erwin.jpg")
    st.markdown("**Erwin Sinaga**\nSenior Business Leader")
    st.write("---")
    
    # Navigasi Utama sesuai foto asli
    with st.container():
        m = option_menu(
            menu_title="Navigasi Utama:",
            options=["1. Profil Founder", "2. Visi, Misi & ROI", "3. Paket Unggulan", "4. Registrasi & Upload", "5. Operasional & Audit"],
            icons=["person-fill", "target", "box-seam", "cloud-upload", "cpu-fill"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#f8f9fa"},
                "icon": {"color": "#6c757d", "font-size": "16px"}, 
                "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#e9ecef"},
                "nav-link-selected": {"background-color": "#E0E7FF", "color":"#1E3A8A", "font-weight":"bold"},
            }
        )
    
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")
    st.caption("© 2026 V-Guard AI Intelligence")

# === 5. LOGIKA HALAMAN RESTORASI SOP ===

if m == "1. Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_column_width=True)
        else: st.info("Foto Founder")
    with c2:
        # SOP 150 Kata Murni
        st.write("""Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional.

Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel.""")

elif m == "2. Visi, Misi & ROI":
    st.header("Strategi & Analisis ROI")
    st.info("**Visi:** Menjadi standar emas dunia dalam sistem audit real-time berbasis AI.")
    st.write("**Misi:** Mencegah kebocoran aset, manipulasi data, dan menjamin akuntabilitas finansial.")
    st.write("---")
    oz = st.number_input("Masukkan Omzet Bulanan Bisnis Anda (Rp):", value=100000000)
    bc = oz * 0.07
    st.error(f"Potensi Kebocoran Finansial (SOP 7%): Rp {bc:,.0f}")
    st.success(f"Penyelamatan Aset via V-Guard: Rp {bc - 2500000:,.0f}")

elif m == "3. Paket Unggulan":
    st.header("4 Produk Layanan V-Guard AI")
    # Desain Card sesuai foto asli (Layanan 4 Produk)
    c1, c2 = st.columns(2)
    with c1:
        with st.container():
            st.subheader("📦 BASIC (1.5jt)")
            st.write("1. Monitoring AI\n2. Laporan Mingguan\n3. Alarm Dasar\n4. Support Email")
        with st.container():
            st.subheader("🚀 SMART (2.5jt)")
            st.write("1. Fitur Basic\n2. Integrasi VCS\n3. Audit Real-time\n4. Notif WA\n5. Dashboard")
    with c2:
        with st.container():
            st.subheader("🛡️ PRO (5jt)")
            st.write("1. Fitur Smart\n2. Forensik Digital\n3. Konsultasi\n4. Proteksi Aset\n5. Multi-User")
        with st.container():
            st.subheader("👑 ENTERPRISE (10jt)")
            st.write("1. Fitur Pro\n2. Custom AI\n3. Onsite Audit\n4. 24/7 Priority\n5. Risk Mgmt\n6. Fraud Ins.")

elif m == "4. Registrasi & Upload":
    st.header("Formulir Registrasi Klien Baru (VCS)")
    with st.form("f_reg"):
        n = st.text_input("Nama Pelanggan")
        u = st.text_input("Nama Jenis Usaha")
        p = st.selectbox("Pilih Paket", ["BASIC", "SMART", "PRO", "ENTERPRISE"])
        st.file_uploader("Upload Data Klien (CSV/Excel/KTP)")
        if st.form_submit_button("Kirim Data VCS"):
            # Harga otomatis
            h = {"BASIC":1500000,"SMART":2500000,"PRO":5000000,"ENTERPRISE":10000000}[p]
            st.session_state.db_order.append({"Nama":n, "Usaha":u, "Paket":p, "Harga":h, "Waktu":str(datetime.now().date())})
            st.success("Order Terkirim ke Admin!")

elif m == "5. Operasional & Audit":
    if not st.session_state.akses_ad:
        p_a = st.text_input("Security Pass:", type="password")
        if st.button("Authorize"):
            if p_a == "w1nbju8282":
                st.session_state.akses_ad = True
                st.rerun()
    else:
        # LOGOUT BUTTON (SESUAI FOTO)
        col_out1, col_out2 = st.columns([10, 1])
        with col_out2:
            if st.button("🔓 Logout"):
                st.session_state.akses_ad = False
                st.rerun()
        
        # OPERASIONAL V-GUARD AI (SESUAI FOTO)
        st.header("Operasional V-Guard AI")
        st.markdown('<div class="alarm">🚨 PERINGATAN: INDIKASI FRAUD TERDETEKSI PADA TITIK TRANSAKSI HARIAN!</div>', unsafe_allow_html=True)
        
        # Notifikasi H-7 (Invoice Reminder)
        td = datetime.now().date()
        for k in st.session_state.db_nasabah:
            jt_d = datetime.strptime(k['Jatuh_Tempo'], "%Y-%m-%d").date()
            if (jt_d - td).days <= 7:
                st.markdown(f'<div class="notif">⚠️ INVOICE H-7: {k["Bisnis"]} ({k["Jatuh_Tempo"]})</div>', unsafe_allow_html=True)

        # TAB OPERASIONAL SESUAI FOTO
        t1, t2, t3, t4, t5 = st.tabs(["🛒 Order Masuk", "➕ Tambah Nasabah (VCS)", "📊 Database Nasabah", "📈 Rugi Laba (60%)",
