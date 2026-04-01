import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database (Session State)
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF", "Log": "System Initialized"},
        {"ID": 102, "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu", "Log": "Pending Payment"}
    ]

WA_NUMBER = "628212190885"

# 2. CSS CUSTOM (ALARM, INVOICE, & KOTAK LAYANAN)
st.markdown(f"""
<style>
    .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; }}
    .fraud-alert {{ background: #f8d7da; color: #721c24; padding: 15px; border-radius: 10px; border-left: 10px solid #dc3545; font-weight: bold; animation: blinker 1s linear infinite; margin-bottom: 10px; }}
    .invoice-box {{ background: #fff3cd; color: #856404; padding: 15px; border-radius: 10px; border-left: 10px solid #ffc107; margin-bottom: 10px; font-weight: bold; }}
    .product-card {{
        background-color: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 15px;
        padding: 25px; text-align: center; min-height: 400px; border-top: 8px solid #1E3A8A;
        display: flex; flex-direction: column;
    }}
    .pkg-title {{ font-size: 26px; font-weight: bold; color: #1E3A8A; margin-bottom: 5px; }}
    .pkg-price {{ font-size: 18px; font-weight: bold; color: #333; margin-bottom: 20px; }}
    .pkg-features {{ text-align: left; font-size: 14px; color: #555; line-height: 1.8; flex-grow: 1; }}
    @keyframes blinker {{ 50% {{ opacity: 0.2; }} }}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (NAVIGASI 1-6)
with st.sidebar:
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Capture", 
        "5. 🔐 Admin Control Center", 
        "6. 📜 Laporan Audit Klien"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", f"https://wa.me/{WA_NUMBER}")

# --- MENU 1: PROFIL FOUNDER (150 KATA, TANPA CEO/CSO) ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2.2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("""
        Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang telah mengabdikan lebih dari satu dekade karir profesionalnya untuk mendalami seluk-beluk operasional bisnis dan efisiensi organisasi di skala nasional. Dengan keahlian mendalam dalam navigasi industri finansial, beliau memiliki kemampuan analitis yang tajam dalam mengidentifikasi titik-titik rawan kebocoran aset yang seringkali luput dari pengawasan manajemen konvensional. Dedikasi beliau terhadap prinsip integritas dan akuntabilitas menjadi pilar utama di balik berdirinya V-Guard AI, sebuah platform yang mengintegrasikan kecerdasan buatan untuk memberikan perlindungan berlapis bagi para pengusaha di Indonesia.

        Beliau fokus pada misi besar untuk mendemokrasikan fungsi audit internal agar dapat diakses oleh semua skala bisnis, mulai dari UMKM hingga korporasi besar. Berdomisili di Tangerang, beliau aktif menjembatani kesenjangan antara teknologi digital dengan kebutuhan nyata di lapangan, memastikan bahwa setiap fitur yang dikembangkan dalam V-Guard AI mampu memberikan solusi konkret bagi efisiensi modal klien. Visi jangka panjang beliau adalah membangun ekosistem bisnis yang lebih sehat di Indonesia, di mana setiap rupiah investasi terjaga dengan aman dan setiap transaksi dapat dipertanggungjawabkan secara transparan, guna mendorong pertumbuhan ekonomi yang berkelanjutan bagi seluruh mitra yang bekerja sama dengannya.
        """)

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("Analisis Strategis")
    st.info("**Visi:** Benteng pertahanan digital utama bagi ekosistem bisnis Indonesia.")
    st.success("**Misi:** Meminimalisir kebocoran transaksi hingga 0%.")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    st.metric("Potensi Hemat (7%)", f"Rp {omzet * 0.07:,.0f}", "Audit Real-time")

# --- MENU 3: PAKET UNGGULAN (DENGAN DETAIL FITUR DI DALAM KOTAK) ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("Layanan V-Guard AI")
    cols = st.columns(4)
    pkgs = [
        ("BASIC", "1.5jt", "• Monitoring Transaksi Harian<br>• Log Aktivitas Standar<br>• Dashboard Desktop<br>• Support Email"),
        ("SMART", "2.5jt", "• Semua Fitur Basic<br>• Deteksi Fraud AI Aktif<br>• Notifikasi WA Real-time<br>• Analisis Tren Mingguan"),
        ("PRO", "5jt", "• Semua Fitur Smart<br>• Audit Finansial Mendalam<br>• Laporan PDF Otomatis<br>• Priority Support 24/7"),
        ("ELITE", "Custom", "• Custom AI Integration<br>• Pendampingan Founder<br>• On-site Audit Visit<br>• Multi-Business Control")
    ]
    for i, (name, price, feat) in enumerate(pkgs):
        with cols[i]:
            st.markdown(f"""
            <div class="product-card">
                <div class="pkg-title">{name}</div>
                <div class="pkg-price">Rp {price}/bln</div>
                <div class="pkg-features">{feat}</div>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("Pilih Paket", f"https://wa.me/{WA_NUMBER}?text=Saya%20tertarik%20paket%20{name}")

# --- MENU 4: REGISTRASI (ADA NAMA PELANGGAN) ---
elif menu == "4. 📝 Registrasi & Capture":
    st.header("Pendaftaran Klien Baru")
    with st.form("reg"):
        st.text_input("Nama Pelanggan (Pemilik):")
        st.text_input("Nama Bisnis / Perusahaan:")
        st.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO", "ELITE"])
        st.file_uploader("Upload Bukti Pembayaran / KTP", type=['jpg','png','jpeg'])
        if st.form_submit_button("Kirim Pendaftaran"):
            st.success("Data pendaftaran berhasil terkirim!")

# --- MENU 5: ADMIN CONTROL (LENGKAP: ALARM, INVOICE, TAMBAH KLIEN, CSV) ---
elif menu == "5. 🔐 Admin Control Center":
    st.header(" Dashboard Kendali Admin")
    df = pd.DataFrame(st.session_state.db_nasabah)
    
    # Alarm Fraud (> 1jt)
    fraud = df[df['Harga'] > 1000000]
    if not fraud.empty:
        for _, r in fraud.iterrows():
            st.markdown(f'<div class="fraud-alert">🚨 ALARM FRAUD: Bisnis "{r["Bisnis"]}" terdeteksi transaksi Rp {r["Harga"]:,.0f}</div>', unsafe_allow_html=True)

    # Status Piutang (Invoice)
    piutang = df[df['Status'] == "🔴 Menunggu"]
    if not piutang.empty:
        for _, r in piutang.iterrows():
            st.markdown(f'<div class="invoice-box">💰 INVOICE PENDING: {r["Pelanggan"]} - Rp {r["Harga"]:,.0f}</div>', unsafe_allow_html=True)

    # Tambah Menu Klien (Input Admin)
    with st.expander("➕ Tambah Klien Baru", expanded=False):
        with st.form("admin_add"):
            c1, c2 = st.columns(2)
            n_p = c1.text_input("Nama Pelanggan:")
            n_b = c1.text_input("Nama Bisnis:")
            n_h = c2.number_input("Harga Paket (Rp):", value=1500000)
            n_s = c2.selectbox("Status:", ["🟢 AKTIF", "🔴 Menunggu"])
            if st.form_submit_button("Simpan Klien"):
                st.session_state.db_nasabah.append({
                    "ID": 100 + len(st.session_state.db_nasabah) + 1, 
                    "Waktu": datetime.now().strftime("%Y-%m-%d"),
                    "Pelanggan": n_p, "Bisnis": n_b, "Paket": "ADMIN_ADD", 
                    "Harga": n_h, "Status": n_s, "Log": "Added by Admin"
                })
                st.rerun()
    
    st.download_button("📥 Download Laporan (CSV)", df.to_csv(index=False).encode('utf-8'), "Laporan_VGuard.csv", "text/csv")
    st.dataframe(df, use_container_width=True)

# --- MENU 6: LAPORAN AUDIT ---
elif menu == "6. 📜 Laporan Audit Klien":
    st.header("Laporan Audit")
    st.table(pd.DataFrame(st.session_state.db_nasabah)[["ID", "Waktu", "Bisnis", "Status"]])

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
