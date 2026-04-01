import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. CONFIG & AI ENGINE ---
API_KEY = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=API_KEY)
    v_engine = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE SESSION ---
if 'db_order' not in st.session_state:
    st.session_state.db_order = []
if 'db_nasabah' not in st.session_state:
    skrg = datetime.now().date()
    st.session_state.db_nasabah = [{
        "ID": 101, "Tgl": str(skrg), "Pelanggan": "Siska",
        "Bisnis": "Cafe Maju", "Paket": "SMART", "Harga": 2500000, 
        "Jatuh_Tempo": str(skrg + timedelta(days=5)), "Status": "🟢 AKTIF"
    }]
if 'is_admin' not in st.session_state:
    st.session_state.is_admin = False

# --- 3. UI STYLE ---
st.markdown("""
<style>
    .alarm { background: #ff4b4b; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; border: 2px solid yellow; }
    .notif { background: #fff3cd; padding: 10px; border-radius: 5px; border-left: 5px solid #ffc107; margin-bottom: 5px; color: black; }
    .profil-box { line-height: 1.8; text-align: justify; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.markdown("**Erwin Sinaga**\nSenior Business Leader")
    st.write("---")
    menu = st.radio("Navigasi:", ["Profil Founder", "Visi, Misi & ROI", "Paket Layanan", "Order Pelanggan", "Admin Panel"])
    st.write("---")
    st.caption("© 2026 V-Guard AI Intelligence")

# --- 5. LOGIKA HALAMAN ---

# --- HALAMAN 1: PROFIL ---
if menu == "Profil Founder":
    st.header("Profil Kepemimpinan")
    st.markdown('<div class="profil-box">Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel.</div>', unsafe_allow_html=True)

# --- HALAMAN 2: VISI, MISI & ROI ---
elif menu == "Visi, Misi & ROI":
    st.header("Visi, Misi & Analisis ROI")
    st.info("**Visi:** Menjadi standar emas dunia dalam sistem audit real-time berbasis AI.\n\n**Misi:** Melindungi aset pengusaha dari kebocoran finansial dan manipulasi data.")
    st.write("---")
    oz = st.number_input("Masukkan Omzet Bulanan Bisnis Anda (Rp):", value=100000000)
    bc = oz * 0.07
    st.error(f"Potensi Kebocoran (Estimasi 7%): Rp {bc:,.0f}".replace(",", "."))
    st.success(f"Dana Yang Diselamatkan V-Guard: Rp {bc - 2500000:,.0f}".replace(",", "."))

# --- HALAMAN 3: PAKET LAYANAN ---
elif menu == "Paket Layanan":
    st.header("4 Produk Unggulan V-Guard")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📦 Paket BASIC")
        st.write("1. Monitoring AI Dasar\n2. Laporan Mingguan\n3. Alarm Anomali\n4. Support Email")
        st.subheader("🚀 Paket SMART")
        st.write("1. Fitur Basic\n2. Integrasi VCS\n3. Audit Real-time\n4. Notifikasi WA\n5. Dashboard Klien")
    with c2:
        st.subheader("🛡️ Paket PRO")
        st.write("1. Fitur Smart\n2. Forensic Digital\n3. Konsultasi Strategis\n4. Proteksi Asset\n5. Multi-User Access")
        st.subheader("👑 Paket ENTERPRISE")
        st.write("1. Fitur Pro\n2. Custom AI Training\n3. On-site Audit\n4. Prioritas 24/7\n5. Risk Management\n6. Fraud Insurance")

# --- HALAMAN 4: ORDER PELANGGAN ---
elif menu == "Order Pelanggan":
    st.header("Formulir Order Layanan")
    with st.form("order_form"):
        nama = st.text_input("Nama Lengkap")
        usaha = st.text_input("Nama Jenis Usaha")
        paket = st.selectbox("Pilih Jenis Paket", ["BASIC", "SMART", "PRO", "ENTERPRISE"])
        harga = {"BASIC": 1500000, "SMART": 2500000, "PRO": 5000000, "ENTERPRISE": 10000000}[paket]
        file_data = st.file_uploader("Upload Data Pendukung (Optional)")
        if st.form_submit_button("Kirim Order ke Admin"):
            new_ord = {"Nama": nama, "Usaha": usaha, "Paket": paket, "Harga": harga, "Status": "Baru"}
            st.session_state.db_order.append(new_ord)
            st.success("Order Berhasil Dikirim! Admin akan segera memproses.")

# --- HALAMAN 5: ADMIN PANEL ---
elif menu == "Admin Panel":
    if not st.session_state.is_admin:
        pwd = st.text_input("Security Code:", type="password")
        if st.button("Authorize"):
            if pwd == "w1nbju8282":
                st.session_state.is_admin = True
                st.rerun()
    else:
        if st.button("🔒 Logout"):
            st.session_state.is_admin = False
            st.rerun()
        
        st.markdown('<div class="alarm">🚨 FRAUD ALERT: ANOMALI TERDETEKSI!</div>', unsafe_allow_html=True)
        
        # Reminder Invoice H-7
        td = datetime.now().date()
        for k in st.session_state.db_nasabah:
            jt = datetime.strptime(k['Jatuh_Tempo'], "%Y-%m-%d").date()
            if (jt - td).days <= 7:
                st.markdown(f'<div class="notif">⚠️ REMINDER INVOICE H-7: {k["Bisnis"]} ({k["Jatuh_Tempo"]})</div>', unsafe_allow_html=True)

        t1, t2, t3, t4 = st.tabs(["🛒 Order Masuk", "📊 Database VCS", "📈 Laporan Rugi Laba", "🔍 Audit Gemini"])
        
        with t1:
            st.subheader("Daftar Order Baru")
            st.table(pd.DataFrame(st.session_state.db_order))
            
        with t2:
            st.subheader("Data VCS Pelanggan Aktif")
            st.dataframe(pd.DataFrame(st.session_state.db_nasabah))
            
        with t3:
            st.subheader("Laporan Rugi Laba (60% Margin)")
            total_inc = sum([x['Harga'] for x in st.session_state.db_nasabah])
            st.metric("Total Omzet Kontrak", f"Rp {total_inc:,.0f}".replace(",", "."))
            st.metric("Estimasi Laba Bersih", f"Rp {total_inc * 0.6:,.0f}".replace(",", "."))
            
        with t4:
            st.subheader("Audit Intelligence - Google Studio Connection")
            txt = st.text_area("Tempel Data Transaksi Klien untuk Diaudit AI:")
            if
