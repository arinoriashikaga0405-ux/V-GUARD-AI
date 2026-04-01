import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# === 1. KONFIGURASI ENGINE AI ===
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
    st.session_state.db_nasabah = [
        {
            "ID": 101, "Tgl": "2026-03-25", "Pelanggan": "Siska",
            "Bisnis": "Cafe Maju", "Usaha": "F&B", "Paket": "SMART", 
            "Harga": 2500000, "Jatuh_Tempo": "2026-04-25", "Status": "🟢 AKTIF"
        }
    ]

if 'akses_ad' not in st.session_state:
    st.session_state.akses_ad = False

# === 3. UI STYLE PREMIUM ===
st.markdown("""
<style>
    .alarm { background: #ff4b4b; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; border: 2px solid yellow; margin-bottom: 20px; }
    .notif { background: #fff3cd; padding: 10px; border-radius: 5px; border-left: 5px solid #ffc107; margin-bottom: 5px; color: black; }
</style>
""", unsafe_allow_html=True)

# === 4. SIDEBAR (RESTORED) ===
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg")
    st.markdown("**Erwin Sinaga**\nSenior Business Leader")
    st.write("---")
    m = st.radio("Navigasi Utama:", 
                 ["1. Profil Founder", 
                  "2. Visi, Misi & ROI", 
                  "3. Paket Unggulan", 
                  "4. Registrasi & Upload", 
                  "5. Operasional & Audit"])
    st.write("---")
    st.caption("© 2026 V-Guard AI Intelligence")

# === 5. LOGIKA HALAMAN ===

if m == "1. Profil Founder":
    st.header("Profil Kepemimpinan")
    st.write("""Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel.""")

elif m == "2. Visi, Misi & ROI":
    st.header("Strategi & Analisis ROI")
    st.info("**Visi:** Menjadi standar emas dunia dalam sistem audit real-time berbasis AI.")
    st.write("**Misi:** Mencegah kebocoran aset dan menjamin akuntabilitas finansial.")
    st.write("---")
    oz = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    bc = oz * 0.07
    st.error(f"Potensi Kebocoran (7%): Rp {bc:,.0f}")
    st.success(f"Penyelamatan Aset: Rp {bc - 2500000:,.0f}")

elif m == "3. Paket Unggulan":
    st.header("4 Produk Layanan V-Guard AI")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📦 BASIC (1.5jt)")
        st.write("1. Monitoring AI\n2. Report Mingguan\n3. Alarm\n4. Support")
        st.subheader("🚀 SMART (2.5jt)")
        st.write("1. Basic+\n2. Integrasi VCS\n3. Audit Real-time\n4. Notif WA")
    with c2:
        st.subheader("🛡️ PRO (5jt)")
        st.write("1. Smart+\n2. Forensik\n3. Konsul\n4. Proteksi Aset")
        st.subheader("👑 ENTERPRISE (10jt)")
        st.write("1. Pro+\n2. Custom AI\n3. Onsite Audit\n4. Fraud Ins.")

elif m == "4. Registrasi & Upload":
    st.header("Formulir Registrasi Klien (VCS)")
    with st.form("f_reg"):
        n = st.text_input("Nama Pelanggan")
        u = st.text_input("Nama Jenis Usaha")
        p = st.selectbox("Paket", ["BASIC", "SMART", "PRO", "ENTERPRISE"])
        st.file_uploader("Upload Data")
        if st.form_submit_button("Kirim Data VCS"):
            h = {"BASIC":1500000,"SMART":2500000,"PRO":5000000,"ENTERPRISE":10000000}[p]
            st.session_state.db_order.append({"Nama":n, "Usaha":u, "Paket":p, "Harga":h})
            st.success("Order Terkirim!")

elif m == "5. Operasional & Audit":
    if not st.session_state.akses_ad:
        pa = st.text_input("Security Pass:", type="password")
        if st.button("Authorize"):
            if pa == "w1nbju8282":
                st.session_state.akses_ad = True
                st.rerun()
    else:
        if st.button("🔒 Logout"):
            st.session_state.akses_ad = False
            st.rerun()
        
        st.header("Operasional V-Guard AI")
        st.markdown('<div class="alarm">🚨 FRAUD ALERT DETECTED!</div>', unsafe_allow_html=True)
        
        # Notif H-7
        td = datetime.now().date()
        for k in st.session_state.db_nasabah:
            jt = datetime.strptime(k['Jatuh_Tempo'], "%Y-%m-%d").date()
            if (jt - td).days <= 7:
                st.markdown(f'<div class="notif">⚠️ INVOICE H-7: {k["Bisnis"]}</div>', unsafe_allow_html=True)

        # TAB FIXED (Dipecah agar tidak terpotong)
        L_TABS = ["🛒 Order", "➕ Tambah", "📊 VCS", "📈 Laba", "🔍 AI"]
        t1, t2, t3, t4, t5 = st.tabs(L_TABS)
        
        with t1:
            st.table(pd.DataFrame(st.session_state.db_order))
        with t2:
            with st.form("f_add"):
                an, ab = st.text_input("Nama"), st.text_input("Bisnis")
                ah = st.number_input("Harga", value=2500000)
                at = st.date_input("Tempo")
                if st.form_submit_button("Simpan"):
                    st.session_state.db_nasabah.append({"ID":105, "Pelanggan":an, "Bisnis":ab, "Harga":ah, "Jatuh_Tempo":str(at)})
                    st.success("Tersimpan!")
        with t3:
            st.table(pd.DataFrame(st.session_state.db_nasabah))
        with t4:
            omzet = sum([x['Harga'] for x in st.session_state.db_nasabah])
            st.metric("Total Omzet", f"Rp {omzet:,.0f}")
            st.metric("Laba Bersih (60%)", f"Rp {omzet * 0.6:,.0f}")
        with t5:
            txt = st.text_area("Tempel Data:")
            if st.button("J
