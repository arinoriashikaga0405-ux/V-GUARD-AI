import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database
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
    .fraud-alert {{ background: #f8d7da; color: #721c24; padding: 15px; border-radius: 10px; border-left: 10px solid #dc3545; font-weight: bold; animation: blinker 1s linear infinite; margin-bottom: 10px; }}
    .invoice-box {{ background: #fff3cd; color: #856404; padding: 15px; border-radius: 10px; border-left: 10px solid #ffc107; margin-bottom: 10px; font-weight: bold; }}
    .product-card {{ background-color: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 15px; padding: 20px; text-align: center; min-height: 380px; border-top: 8px solid #1E3A8A; }}
    .pkg-title {{ font-size: 24px; font-weight: bold; color: #1E3A8A; }}
    @keyframes blinker {{ 50% {{ opacity: 0.2; }} }}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 📦 Paket Unggulan", "4. 📝 Registrasi & Capture", "5. 🔐 Admin Control Center", "6. 📜 Laporan Audit Klien"])
    st.write("---")
    st.link_button("💬 Chat Support", f"https://wa.me/{WA_NUMBER}")

# --- MENU 1: PROFIL (150 KATA, TANPA CEO/CSO) ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang telah mengabdikan lebih dari satu dekade karir profesionalnya untuk mendalami seluk-beluk operasional bisnis dan efisiensi organisasi di skala nasional. Dengan keahlian mendalam dalam navigasi industri finansial, beliau memiliki kemampuan analitis yang tajam dalam mengidentifikasi titik-titik rawan kebocoran aset yang seringkali luput dari pengawasan manajemen konvensional. Dedikasi beliau terhadap prinsip integritas dan akuntabilitas menjadi pilar utama di balik berdirinya V-Guard AI, sebuah platform yang mengintegrasikan kecerdasan buatan untuk memberikan perlindungan berlapis bagi para pengusaha di Indonesia. Beliau fokus pada misi besar untuk mendemokrasikan fungsi audit internal agar dapat diakses oleh semua skala bisnis, mulai dari UMKM hingga korporasi besar. Berdomisili di Tangerang, beliau aktif menjembatani kesenjangan antara teknologi digital dengan kebutuhan nyata di lapangan, memastikan bahwa setiap fitur yang dikembangkan dalam V-Guard AI mampu memberikan solusi konkret bagi efisiensi modal klien. Visi jangka panjang beliau adalah membangun ekosistem bisnis yang lebih sehat di Indonesia.")

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("Analisis Strategis")
    st.info("**Visi:** Benteng pertahanan digital utama.")
    st.success("**Misi:** Meminimalisir kebocoran transaksi hingga 0%.")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    st.metric("Potensi Hemat (7%)", f"Rp {omzet * 0.07:,.0f}")

# --- MENU 3: PAKET UNGGULAN (DENGAN DETAIL FITUR) ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("Layanan V-Guard AI")
    cols = st.columns(4)
    pkgs = [
        ("BASIC", "1.5jt", "• Monitor Harian<br>• Log Standar<br>• Support Email"),
        ("SMART", "2.5jt", "• Fitur Basic+<br>• Deteksi Fraud AI<br>• Notif WA Real-time"),
        ("PRO", "5jt", "• Fitur Smart+<br>• Audit Mendalam<br>• Laporan PDF"),
        ("ELITE", "Custom", "• Custom AI<br>• Strategi Founder<br>• On-site Visit")
    ]
    for i, (n, p, f) in enumerate(pkgs):
        with cols[i]:
            st.markdown(f'<div class="product-card"><div class="pkg-title">{n}</div><p>Rp {p}/bln</p><div style="text-align:left; font-size:13px;">{f}</div></div>', unsafe_allow_html=True)
            st.link_button("Pilih Paket", f"https://wa.me/{WA_NUMBER}?text=Paket%20{n}")

# --- MENU 4: REGISTRASI ---
elif menu == "4. 📝 Registrasi & Capture":
    st.header("Pendaftaran Klien")
    with st.form("reg"):
        st.text_input("Nama Pelanggan (Pemilik):")
        st.text_input("Nama Bisnis:")
        st.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO", "ELITE"])
        if st.form_submit_button("Kirim"): st.success("Terkirim!")

# --- MENU 5: ADMIN (ALARM, INVOICE, CSV) ---
elif menu == "5. 🔐 Admin Control Center":
    st.header("Dashboard Admin")
    df = pd.DataFrame(st.session_state.db_nasabah)
    fraud = df[df['Harga'] > 1000000]
    if not fraud.empty:
        for _, r in fraud.iterrows(): st.markdown(f'<div class="fraud-alert">🚨 ALARM: {r["Bisnis"]} - Rp {r["Harga"]:,.0f}</div>', unsafe_allow_html=True)
    piutang = df[df['Status'] == "🔴 Menunggu"]
    if not piutang.empty:
        for _, r in piutang.iterrows(): st.markdown(f'<div class="invoice-box">💰 PIUTANG: {r["Pelanggan"]} - Rp {r["Harga"]:,.0f}</div>', unsafe_allow_html=True)
    st.download_button("📥 CSV", df.to_csv(index=False).encode('utf-8'), "Laporan.csv", "text/csv")
    st.dataframe(df, use_container_width=True)

# --- MENU 6: LAPORAN (DENGAN PASSWORD) ---
elif menu == "6. 📜 Laporan Audit Klien":
    st.header("Laporan Audit")
    pw = st.text_input("Sandi Laporan:", type="password")
    if pw == "w1nbju8282":
        st.table(pd.DataFrame(st.session_state.db_nasabah)[["ID", "Bisnis", "Status"]])
    elif pw != "": st.error("Sandi Salah")

st.markdown('<div class="footer">© 2026 V-Guard AI | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
