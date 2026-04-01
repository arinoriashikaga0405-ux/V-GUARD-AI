import streamlit as st
import os
import pandas as pd
from datetime import datetime
import google.generativeai as genai

# 1. KONFIGURASI AI & HALAMAN
try:
    genai.configure(api_key="AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA")
    model = genai.GenerativeModel('gemini-pro')
    ai_ok = True
except:
    ai_ok = False

st.set_page_config(page_title="V-Guard AI", layout="wide")

if 'db' not in st.session_state:
    st.session_state.db = [
        {"ID": 101, "Nama": "Siska", "Bisnis": "Cafe Maju", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": 102, "Nama": "Jaya", "Bisnis": "Bengkel Berkah", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]

# 2. CSS CUSTOM
st.markdown("""
<style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; }
    .fraud { background: #f8d7da; color: #721c24; padding: 10px; border-radius: 8px; border-left: 8px solid #dc3545; font-weight: bold; margin-bottom: 5px; }
    .inv { background: #fff3cd; color: #856404; padding: 10px; border-radius: 8px; border-left: 8px solid #ffc107; margin-bottom: 5px; font-weight: bold; }
    .card { background: #f8f9fa; border: 1px solid #ddd; border-radius: 12px; padding: 15px; text-align: center; border-top: 6px solid #1E3A8A; min-height: 250px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGASI 1-6
with st.sidebar:
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    m = st.radio("Navigasi:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 📦 Paket Unggulan", "4. 📝 Registrasi & Capture", "5. 🔐 Admin Control Center", "6. 📜 Laporan Audit Klien"])
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- MENU 1: PROFIL ---
if m == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2])
    with c1: 
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang telah mengabdikan lebih dari satu dekade karir profesionalnya untuk mendalami seluk-beluk operasional bisnis dan efisiensi organisasi di skala nasional. Dengan keahlian mendalam dalam navigasi industri finansial, beliau memiliki kemampuan analitis yang tajam dalam mengidentifikasi titik-titik rawan kebocoran aset yang seringkali luput dari pengawasan manajemen konvensional. Dedikasi beliau terhadap prinsip integritas dan akuntabilitas menjadi pilar utama di balik berdirinya V-Guard AI, sebuah platform yang mengintegrasikan kecerdasan buatan untuk memberikan perlindungan berlapis bagi para pengusaha di Indonesia. Beliau fokus pada misi besar untuk mendemokrasikan fungsi audit internal agar dapat diakses oleh semua skala bisnis, mulai dari UMKM hingga korporasi besar. Berdomisili di Tangerang, beliau aktif menjembatani kesenjangan antara teknologi digital dengan kebutuhan nyata di lapangan.")

# --- MENU 2: ROI ---
elif m == "2. 🎯 Visi, Misi & ROI":
    st.info("Visi: Benteng pertahanan digital utama.")
    omzet = st.number_input("Omzet (Rp):", value=100000000)
    st.metric("Potensi Hemat", f"Rp {omzet * 0.07:,.0f}")

# --- MENU 3: PAKET ---
elif m == "3. 📦 Paket Unggulan":
    st.header("Layanan V-Guard AI")
    cols = st.columns(4)
    pkgs = [("BASIC", "1.5jt", "Audit Harian"), ("SMART", "2.5jt", "Fraud AI"), ("PRO", "5jt", "PDF Report"), ("ELITE", "Custom", "AI Khusus")]
    for i, (n, p, f) in enumerate(pkgs):
        with cols[i]:
            st.markdown(f'<div class="card"><h3>{n}</h3><p>Rp {p}</p><p>{f}</p></div>', unsafe_allow_html=True)
            st.link_button("Pilih", f"https://wa.me/628212190885?text=Paket%20{n}")

# --- MENU 4: REGISTRASI ---
elif m == "4. 📝 Registrasi & Capture":
    with st.form("reg"):
        st.text_input("Nama Pelanggan:")
        st.text_input("Bisnis:")
        if st.form_submit_button("Daftar"): st.success("Berhasil!")

# --- MENU 5: ADMIN ---
elif m == "5. 🔐 Admin Control Center":
    df = pd.DataFrame(st.session_state.db)
    for _, r in df[df['Harga'] > 1000000].iterrows():
        st.markdown(f'<div class="fraud">🚨 ALARM: {r["Bisnis"]} (Rp {r["Harga"]:,.0f})</div>', unsafe_allow_html=True)
    for _, r in df[df['Status'] == "🔴 Menunggu"].iterrows():
        st.markdown(f'<div class="inv">💰 PIUTANG: {r["Nama"]}</div>', unsafe_allow_html=True)
    st.download_button("📥 CSV", df.to_csv(index=False), "Laporan.csv")
    st.dataframe(df, use_container_width=True)

# --- MENU 6: LAPORAN ---
elif m == "6. 📜 Laporan Audit Klien":
    pw = st.text_input("Sandi Otoritas:", type="password")
    if pw == "w1nbju8282":
        st.table(pd.DataFrame(st.session_state.db))
        if st.button("🤖 Analisis Gemini AI"):
            if ai_ok:
                res = model.generate_content(f"Analisis data ini: {st.session_state.db}")
                st.info(res.text)
            else: st.error("AI Belum Terhubung")
