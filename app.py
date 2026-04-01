import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import google.generativeai as genai

# --- 1. ENGINE AI ---
K_AI = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=K_AI)
    v_ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE SESSION ---
if 'db_order' not in st.session_state: st.session_state.db_order = []
if 'db_vcs' not in st.session_state:
    t = datetime.now().date()
    st.session_state.db_vcs = [{
        "ID": 101, "Nama": "Siska", "Bisnis": "Cafe Maju", 
        "Paket": "SMART", "Harga": 2500000, 
        "Tempo": str(t + timedelta(days=5))
    }]
if 'is_admin' not in st.session_state: st.session_state.is_admin = False

# --- 3. UI STYLE ---
st.markdown("""
<style>
    .alarm { background: #ff4b4b; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; border: 2px solid yellow; }
    .notif { background: #fff3cd; padding: 10px; border-radius: 5px; border-left: 10px solid #ffc107; margin-bottom: 5px; color: black; }
    .card { background: white; padding: 20px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Erwin Sinaga - Founder")
    st.markdown("### **Erwin Sinaga**\n*Senior Business Leader*")
    st.write("---")
    m = st.radio("Intelligence Navigasi:", 
                 ["Profil Founder", "Visi & Misi", "ROI & Layanan", "Order Pelanggan", "Admin Panel"])
    st.write("---")
    st.caption("© 2026 V-Guard AI")

# --- 5. HALAMAN ---

if m == "Profil Founder":
    st.header("Profil Kepemimpinan")
    st.write("""Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel.""")

elif m == "Visi & Misi":
    st.header("Visi & Misi Strategis")
    st.info("**Visi:** Menjadi standar emas dunia dalam sistem audit real-time berbasis AI.")
    st.write("**Misi:**")
    st.write("1. Transparansi finansial mutlak.\n2. Pencegahan manipulasi data.\n3. Perlindungan aset pengusaha.\n4. Akuntabilitas digital.")

elif m == "ROI & Layanan":
    st.header("ROI & 4 Produk Unggulan")
    oz = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    bc = oz * 0.07
    st.error(f"Potensi Kebocoran (7%): Rp {bc:,.0f}")
    st.success(f"Penyelamatan Aset V-Guard: Rp {bc - 2500000:,.0f}")
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📦 BASIC (1.5jt)")
        st.write("• AI Monitoring\n• Laporan Mingguan\n• Alarm Dasar\n• Support Email")
        st.subheader("🚀 SMART (2.5jt)")
        st.write("• Fitur Basic\n• VCS System\n• Audit Real-time\n• Notifikasi WA\n• Dashboard Klien")
    with c2:
        st.subheader("🛡️ PRO (5jt)")
        st.write("• Fitur Smart\n• Digital Forensic\n• Konsultasi Strategis\n• Proteksi Aset\n• Multi-User")
        st.subheader("👑 ENTERPRISE (10jt)")
        st.write("• Fitur Pro\n• Custom AI Training\n• On-site Audit\n• 24/7 Priority\n• Risk Management\n• Fraud Insurance")

elif m == "Order Pelanggan":
    st.header("Formulir Order VCS")
    with st.form("f_order"):
        n = st.text_input("Nama Lengkap")
        u = st.text_input("Nama Usaha")
        p = st.selectbox("Pilih Paket", ["BASIC", "SMART", "PRO", "ENTERPRISE"])
        st.file_uploader("Upload Data Transaksi")
        if st.form_submit_button("Kirim Order ke Admin"):
            st.session_state.db_order.append({"Nama":n, "Usaha":u, "Paket":p})
            st.success("Order Berhasil Dikirim!")

elif m == "Admin Panel":
    if not st.session_state.is_admin:
        pw = st.text_input("Security Code:", type="password")
        if st.button("Authorize"):
            if pw == "w1nbju8282":
                st.session_state.is_admin = True
                st.rerun()
    else:
        if st.button("🔒 Logout"):
            st.session_state.is_admin = False
            st.rerun()
        
        st.markdown('<div class="alarm">🚨 FRAUD ALERT DETECTED!</div>', unsafe_allow_html=True)
        
        # Notif H-7
        td = datetime.now().date()
        for k in st.session_state.db_vcs:
            jt = datetime.strptime(k['Tempo'], "%Y-%m-%d").date()
            if (jt - td).days <= 7:
                st.markdown(f'<div class="notif">⚠️ INVOICE H-7: {k["Bisnis"]} ({k["Tempo"]})</div>', unsafe_allow_html=True)

        t1, t2, t3, t4, t5 = st.tabs(["🛒 Order Masuk", "➕ Tambah Klien", "📊 Database VCS", "📈 Rugi Laba", "🔍 Audit Gemini"])
        
        with t1:
            st.table(pd.DataFrame(st.session_state.db_order))
        with t2:
            with st.form("f_add"):
                an, ab = st.text_input("Nama"), st.text_input("Bisnis")
                ah = st.number_input("Harga", value=2500000)
                at = st.date_input("Tempo")
                if st.form_submit_button("Sim
