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

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Database Sesi
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": 102, "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]

WA_NUMBER = "628212190885"

# 2. CSS CUSTOM
st.markdown(f"""
<style>
    .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; }}
    .fraud-alert {{ background: #f8d7da; color: #721c24; padding: 12px; border-radius: 10px; border-left: 10px solid #dc3545; font-weight: bold; margin-bottom: 8px; }}
    .invoice-box {{ background: #fff3cd; color: #856404; padding: 12px; border-radius: 10px; border-left: 10px solid #ffc107; margin-bottom: 8px; font-weight: bold; }}
    .product-card {{ background-color: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 15px; padding: 20px; text-align: center; min-height: 380px; border-top: 8px solid #1E3A8A; }}
    .pkg-title {{ font-size: 24px; font-weight: bold; color: #1E3A8A; }}
    .pkg-feat {{ text-align: left; font-size: 14px; margin-top: 15px; line-height: 1.6; color: #444; }}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (NAVIGASI 1-6)
with st.sidebar:
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 📦 Paket Unggulan", "4. 📝 Registrasi & Capture", "5. 🔐 Admin Control Center", "6. 📜 Laporan Audit Klien"])
    st.write("---")
    st.link_button("💬 Chat Support", f"https://wa.me/{WA_NUMBER}")

# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2.2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang telah mengabdikan lebih dari satu dekade karir profesionalnya untuk mendalami seluk-beluk operasional bisnis dan efisiensi organisasi di skala nasional. Dengan keahlian mendalam dalam navigasi industri finansial, beliau memiliki kemampuan analitis yang tajam dalam mengidentifikasi titik-titik rawan kebocoran aset yang seringkali luput dari pengawasan manajemen konvensional. Dedikasi beliau terhadap prinsip integritas dan akuntabilitas menjadi pilar utama di balik berdirinya V-Guard AI, sebuah platform yang mengintegrasikan kecerdasan buatan untuk memberikan perlindungan berlapis bagi para pengusaha di Indonesia. Beliau fokus pada misi besar untuk mendemokrasikan fungsi audit internal agar dapat diakses oleh semua skala bisnis, mulai dari UMKM hingga korporasi besar. Berdomisili di Tangerang, beliau aktif menjembatani kesenjangan antara teknologi digital dengan kebutuhan nyata di lapangan.")

# --- MENU 2: ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("Analisis Strategis")
    st.info("**Visi:** Benteng pertahanan digital utama bagi ekosistem bisnis Indonesia.")
    st.success("**Misi:** Meminimalisir kebocoran transaksi hingga 0%.")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    st.metric("Potensi Hemat (7%)", f"Rp {omzet * 0.07:,.0f}")

# --- MENU 3: PAKET UNGGULAN (KEMBALI DENGAN FITUR LENGKAP) ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("Layanan V-Guard AI")
    cols = st.columns(4)
    p_data = [
        ("BASIC", "1.5jt", "• Monitor Harian<br>• Log Standar<br>• Dashboard Desktop"),
        ("SMART", "2.5jt", "• Deteksi Fraud AI<br>• Notif WA Real-time<br>• Analisis Mingguan"),
        ("PRO", "5jt", "• Audit Mendalam<br>• Laporan PDF<br>• Support 24/7"),
        ("ELITE", "Custom", "• Custom AI Integration<br>• Pendampingan Founder<br>• On-site Audit")
    ]
    for i, (n, p, f) in enumerate(p_data):
        with cols[i]:
            st.markdown(f'<div class="product-card"><div class="pkg-title">{n}</div><p><b>Rp {p}/bln</b></p><div class="pkg-feat">{f}</div></div>', unsafe_allow_html=True)
            st.link_button("Pilih Paket", f"https://wa.me/{WA_NUMBER}?text=Paket%20{n}")

# --- MENU 4: REGISTRASI ---
elif menu == "4. 📝 Registrasi & Capture":
    st.header("Pendaftaran Klien Baru")
    with st.form("reg_form"):
        st.text_input("Nama Pelanggan (Pemilik):")
        st.text_input("Nama Bisnis:")
        st.selectbox("Paket:", ["BASIC", "SMART", "PRO", "ELITE"])
        if st.form_submit_button("Kirim Pendaftaran"): st.success("Data Terkirim!")

# --- MENU 5: ADMIN DASHBOARD (ALARM, INVOICE, CSV) ---
elif menu == "5. 🔐 Admin Control Center":
    st.header("📊 Dashboard Admin")
    df = pd.DataFrame(st.session_state.db_nasabah)
    for _, r in df[df['Harga'] > 1000000].iterrows():
        st.markdown(f'<div class="fraud-alert">🚨 ALARM FRAUD: {r["Bisnis"]} (Rp {r["Harga"]:,.0f})</div>', unsafe_allow_html=True)
    for _, r in df[df['Status'] == "🔴 Menunggu"].iterrows():
        st.markdown(f'<div class="invoice-box">💰 INVOICE PENDING: {r["Pelanggan"]}</div>', unsafe_allow_html=True)
    st.download_button("📥 Download Laporan CSV", df.to_csv(index=False).encode('utf-8'), "Laporan.csv", "text/csv")
    st.dataframe(df, use_container_width=True)

# --- MENU 6: LAPORAN AUDIT (PASSWORD + AI) ---
elif menu == "6. 📜 Laporan Audit Klien":
    st.header("📜 Laporan Audit Terenkripsi")
    pw = st.text_input("Masukkan Sandi Otoritas:", type="password")
    if pw == "w1nbju8282":
        st.success("Akses Diterima")
        st.table(pd.DataFrame(st.session_state.db_nasabah)[["ID", "Bisnis", "Status", "Pelanggan"]])
        if st.button("🤖 Jalankan Analisis Pakar Gemini"):
            if ai_ok:
                with st.spinner("Menganalisis..."):
                    res = model.generate_content(f"Berikan saran singkat untuk data audit: {st.session_state.db_nasabah}")
                    st.info(f"**Saran Strategis Gemini:**\n\n{res.text}")
            else: st.error("AI Belum Terhubung")
    elif pw != "": st.error("Sandi Salah!")

st.markdown('<div class="footer">© 2026 V-Guard AI | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
