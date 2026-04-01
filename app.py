import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database (Proteksi Struktur)
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Usaha": "F&B", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": 102, "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Usaha": "Otomotif", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]
if 'admin_akses_terbuka' not in st.session_state:
    st.session_state.admin_akses_terbuka = False

WA_NUMBER = "628212190885"
ADMIN_PASSWORD = "w1nbju8282"

def format_rp(angka):
    try:
        return f"Rp {float(angka):,.0f}".replace(",", ".")
    except:
        return str(angka)

# 2. CSS CUSTOM VISUAL V-GUARD
st.markdown("""
<style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; font-size: 12px; }
    .fraud-alarm { background-color: #ff4b4b; color: white; padding: 12px; border-radius: 8px; text-align: center; font-weight: bold; animation: blinker 2s linear infinite; margin-bottom: 20px; }
    @keyframes blinker { 50% { opacity: 0.7; } }
    .roi-card { background: #f8f9fa; padding: 25px; border-radius: 15px; border-left: 10px solid #1E3A8A; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (NAVIGASI TERKUNCI)
with st.sidebar:
    st.markdown("<h1 style='color: #1E3A8A; text-align: center;'>🛡️ V-GUARD AI</h1>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", use_container_width=True)
        st.markdown("<p style='text-align:center; font-weight:bold;'>Erwin Sinaga<br><span style='font-size:12px;'>Senior Business Leader</span></p>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Upload", 
        "5. 🔐 Akses Terbatas"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", f"https://wa.me/{WA_NUMBER}")

# --- MENU 1: PROFIL FOUNDER (LOCKED 150 WORDS) ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2.2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("""Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel dan adaptif terhadap tantangan ekonomi masa depan.""")

# --- MENU 2: VISI, MISI & ROI (DIKEMBALIKAN) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("Strategi & Analisis ROI")
    
    col_v, col_m = st.columns(2)
    with col_v:
        st.info("### 👁️ Visi\nMenjadi standar emas dalam teknologi pengawasan bisnis digital di Indonesia.")
    with col_m:
        st.success("### 🚀 Misi\nMenyediakan instrumen audit AI untuk mendeteksi indikasi kecurangan secara real-time.")
    
    st.write("---")
    st.subheader("📊 Kalkulator ROI V-Guard")
    
    with st.container():
        st.markdown('<div class="roi-card">', unsafe_allow_html=True)
        omzet = st.number_input("Masukkan Omzet Bulanan Bisnis (Rp):", value=100000000, step=1000000)
        pot_bocor = omzet * 0.07
        st.error(f"Estimasi Kebocoran Dana (Rata-rata 7%): {format_rp(pot_bocor)}")
        
        investasi = 2500000
        net_saved = pot_bocor - investasi
        
        st.markdown(f"### Dana Berhasil Diselamatkan (ROI): \n ## {format_rp(net_saved)}")
        st.caption("🟢 Analisis: Investasi V-Guard memberikan pengembalian positif sejak bulan pertama.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- MENU 3: PAKET UNGGULAN ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("Layanan V-Guard AI")
    pkts = [("BASIC", "1.5jt"), ("SMART", "2.5jt"), ("PRO", "5jt"), ("ELITE", "Custom")]
    cols = st.columns(4)
    for i, (n, p) in enumerate(pkts):
        with cols[i]:
            st.markdown(f'<div style="background:#f0f7ff; padding:20px; border-radius:15px; text-align:center; border:1px solid #1E3A8A;"><h3>{n}</h3><h2 style="color:#d32f2f;">Rp {p}</h2><p>• AI Monitoring<br>• VCS System<br>• Weekly Audit</p></div>', unsafe_allow_html=True)
            st.link_button(f"Pesan {n}", f"https://wa.me/{WA_NUMBER}")

# --- MENU 4: REGISTRASI & UPLOAD (LOCKED) ---
elif menu == "4. 📝 Registrasi & Upload":
    st.header("Formulir Pendaftaran Klien")
    with st.form("reg_vguard_final_fix"):
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Nama Pelanggan:")
            st.text_input("Nama Bisnis:")
        with c2:
            st.text_input("Jenis Usaha:")
            st.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO", "ELITE"])
        st.file_uploader("Upload Dokumen Pendukung (KTP/SKU):", type=['jpg','png','pdf'])
        if st.form_submit_button("Kirim Pendaftaran"):
            st.success("Aplikasi Berhasil Terkirim!")

# --- MENU 5: ADMIN (AUDIT & RUGI LABA) ---
elif menu == "5. 🔐 Akses Terbatas":
    if not st.session_state.admin_akses_terbuka:
        st.markdown("<h2 style='text-align: center;'>🔐 Otoritas Admin</h2>", unsafe_allow_html=True)
        pwd = st.text_input("Sandi Keamanan:", type="password")
        if st.button("Masuk"):
            if pwd == ADMIN_PASSWORD:
                st.session_state.admin_akses_terbuka = True
                st.rerun()
            else:
                st.error("Akses Ditolak!")
    else:
        h1, h2 = st.columns([5, 1])
        with h1: st.header("Panel Operasional Admin")
        with h2:
            if st.button("🔒 LOGOUT"):
                st.session_state.admin_akses_terbuka = False
                st.rerun()

        st.markdown('<div class="fraud-alarm">🚨 ALARM: INDIKASI FRAUD TERDETEKSI!</div>', unsafe_allow_html=True)
        
        t1, t2, t3 = st.tabs(["📊 Database", "📉 Audit Studio Gemini", "🧾 Laporan Rugi Laba"])
        
        with t1:
            df = pd.DataFrame(st.session_state.db_nasabah)
            if 'Harga' in df.columns:
                df_show = df.copy()
                df_show['Harga'] = df_show['Harga'].apply(format_rp)
                st.table(df_show)
            else: st.table(df)

        with t2:
            st.subheader("Audit Intelligence (Google Studio)")
            st.metric("Integrity Score", "98.5%", "+1.2%")
            st.line_chart([10, 20, 15, 35, 30, 50])
            st.success("Status Audit: VERIFIED ✅")

        with t3:
            st.subheader("Laporan Rugi Laba AI")
            st.area_chart({"Profit": [50, 65, 80, 75, 95]})
            st.table(pd.DataFrame({"Ket": ["Income", "Expense", "Profit"], "Total": [format_rp(120), format_rp(45), format_rp(75)]}))

st.markdown('<div class="footer">© 2026 V-Guard AI | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
