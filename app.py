import streamlit as st
import os
import pandas as pd
from datetime import datetime
import google.generativeai as genai

# --- 1. CONFIG & ENGINE AI ---
K_V = "AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA"
try:
    genai.configure(api_key=K_V)
    v_ai = genai.GenerativeModel('gemini-1.5-flash')
except:
    pass

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE ---
if 'db_n' not in st.session_state:
    st.session_state.db_n = [
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Usaha": "F&B", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": 102, "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Usaha": "Otomotif", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 3. CSS CUSTOM (PREMIUM LOOK) ---
st.markdown("""
<style>
    .service-card {
        background-color: #ffffff; padding: 20px; border-radius: 15px;
        border: 1px solid #e0e0e0; box-shadow: 2px 2px 15px rgba(0,0,0,0.05);
        text-align: center; height: 100%; transition: 0.3s;
    }
    .service-card:hover { border: 1px solid #1e3a8a; transform: translateY(-5px); }
    .price-tag { font-size: 24px; font-weight: bold; color: #1e3a8a; margin: 10px 0; }
    .feature-list { text-align: left; font-size: 14px; margin-bottom: 20px; min-height: 180px; }
    .fraud-alert { background-color: #ff7675; color: white; padding: 15px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    else:
        st.info("Unggah erwin.jpg")
    st.markdown("**Erwin Sinaga**\nSenior Business Leader")
    st.write("---")
    nav = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 💎 Layanan Produk", 
        "4. 📝 Registrasi & Upload", 
        "5. 🔐 Akses Terbatas"
    ])
    st.write("---")
    st.caption("© 2026 V-Guard AI Intelligence")

# --- 5. LOGIKA HALAMAN ---

if nav == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.write("""Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel.""")

elif nav == "2. 🎯 Visi, Misi & ROI":
    st.header("Visi, Misi & ROI")
    st.info("**Visi:** Menjadi standar emas dalam audit AI.")
    st.write("**Misi:** Transparansi, Proteksi, Akuntabilitas.")
    st.write("---")
    oz = st.number_input("Masukkan Omzet (Rp):", value=100000000)
    bc = oz * 0.07
    st.error(f"Potensi Bocor (SOP 7%): Rp {bc:,.0f}")
    st.success(f"Penyelamatan Aset: Rp {bc - 2500000:,.0f}")

elif nav == "3. 💎 Layanan Produk":
    st.header("Paket Layanan Unggulan V-Guard AI")
    st.write("Pilih proteksi terbaik untuk keberlangsungan aset bisnis Anda.")
    
    c1, c2, c3 = st.columns(3)
    wa_link = "https://wa.me/628212190885?text=Halo%20V-Guard,%20saya%20tertarik%20paket%20"

    with c1:
        st.markdown(f"""<div class="service-card">
            <h3>📦 BASIC</h3>
            <div class="price-tag">Rp 1.500.000</div>
            <div class="feature-list">
                • AI Monitoring Dasar<br>
                • Laporan Mingguan (PDF)<br>
                • Alarm Indikasi Fraud<br>
                • Support Email & Chat
            </div>
        </div>""", unsafe_allow_html=True)
        st.link_button("🚀 Pesan Basic", wa_link + "BASIC")

    with c2:
        st.markdown(f"""<div class="service-card" style="border: 2px solid #1e3a8a;">
            <h3>🚀 SMART</h3>
            <div class="price-tag">Rp 2.500.000</div>
            <div class="feature-list">
                • Semua Fitur Paket Basic<br>
                • Integrasi VCS (Virtual Cloud)<br>
                • Audit AI Real-Time<br>
                • Notifikasi WhatsApp Instant<br>
                • Dashboard Monitoring Live
            </div>
        </div>""", unsafe_allow_html=True)
        st.link_button("🔥 Pesan Smart", wa_link + "SMART")

    with c3:
        st.markdown(f"""<div class="service-card">
            <h3>🛡️ PRO</h3>
            <div class="price-tag">Rp 5.000.000</div>
            <div class="feature-list">
                • Semua Fitur Paket Smart<br>
                • Forensik Data Digital<br>
                • Konsultasi Strategis Bulanan<br>
                • Sistem Proteksi Multi-Cabang<br>
                • Risk Management Analysis<br>
                • Prioritas Support 24/7
            </div>
        </div>""", unsafe_allow_html=True)
        st.link_button("💎 Pesan Pro", wa_link + "PRO")

elif nav == "4. 📝 Registrasi & Upload":
    st.header("Pendaftaran Klien Baru")
    with st.form("reg"):
        n, b = st.text_input("Nama Pelanggan:"), st.text_input("Nama Bisnis:")
        p = st.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO"])
        st.file_uploader("Upload Dokumen Pendukung:")
        if st.form_submit_button("Kirim Pendaftaran"):
            st.success("Data berhasil dikirim! Tim kami akan menghubungi Anda.")

elif nav == "5. 🔐 Akses Terbatas":
    if not st.session_state.auth:
        pw = st.text_input("Security Code:", type="password")
        if st.button("LOGIN"):
            if pw == "w1nbju8282":
                st.session_state.auth = True
                st.rerun()
    else:
        col_h1, col_h2 = st.columns([10, 1])
        col_h1.header("⚙️ Operasional V-Guard AI")
        if col_h2.button("OUT"):
            st.session_state.auth = False
            st.rerun()
        st.markdown('<div class="fraud-alert">🚨 PERINGATAN: INDIKASI FRAUD TERDETEKSI!</div>', unsafe_allow_html=True)
        t1, t2 = st.tabs(["📊 Database", "📈 Laba (60%)"])
        with t1: st.table(pd.DataFrame(st.session_state.db_n))
        with t2:
            total = sum([x['Harga'] for x in st.session_state.db_n])
            st.metric("Total Omzet", f"Rp {total:,.0f}")
            st.metric("Laba Bersih (60%)", f"Rp {total * 0.6:,.0f}")

st.write("---")
st.caption("© 2026 V-Guard AI | Secured by Erwin Sinaga")
