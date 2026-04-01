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

# 2. CSS CUSTOM (ALARM, INVOICE, & KOTAK)
st.markdown(f"""
<style>
    .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; }}
    .fraud-alert {{ 
        background: #f8d7da; color: #721c24; padding: 15px; border-radius: 10px; 
        border-left: 10px solid #dc3545; font-weight: bold; 
        animation: blinker 1s linear infinite; margin-bottom: 10px;
    }}
    .invoice-box {{
        background: #fff3cd; color: #856404; padding: 15px; border-radius: 10px;
        border-left: 10px solid #ffc107; margin-bottom: 10px; font-weight: bold;
    }}
    .product-card {{
        background-color: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 15px;
        padding: 20px; text-align: center; min-height: 380px; border-top: 8px solid #1E3A8A;
    }}
    .pkg-title {{ font-size: 24px; font-weight: bold; color: #1E3A8A; }}
    @keyframes blinker {{ 50% {{ opacity: 0.2; }} }}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
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

# --- MENU 1: PROFIL FOUNDER (DIPERTAHANKAN) ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with col_txt:
        st.subheader("Bapak Erwin Sinaga")
        st.write("""
        Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang telah mengabdikan lebih dari satu dekade karir profesionalnya 
        untuk mendalami seluk-beluk operasional bisnis dan efisiensi organisasi di skala nasional. Dengan keahlian mendalam 
        dalam navigasi industri finansial, beliau memiliki kemampuan analitis yang tajam dalam mengidentifikasi titik-titik rawan 
        kebocoran aset yang seringkali luput dari pengawasan manajemen konvensional. Dedikasi beliau terhadap prinsip integritas 
        dan akuntabilitas menjadi pilar utama di balik berdirinya V-Guard AI, sebuah platform yang mengintegrasikan kecerdasan buatan 
        untuk memberikan perlindungan berlapis bagi para pengusaha di Indonesia.
        
        Sebagai arsitek utama V-Guard AI, Bapak Erwin Sinaga fokus pada misi besar untuk mendemokrasikan fungsi audit internal. 
        Beliau percaya bahwa setiap entitas bisnis, mulai dari skala UMKM hingga korporasi besar, harus memiliki akses terhadap 
        teknologi pengawasan yang real-time dan akurat. Berdomisili di Tangerang, beliau aktif menjembatani kesenjangan antara 
        teknologi digital dengan kebutuhan nyata di lapangan, memastikan bahwa setiap fitur yang dikembangkan dalam V-Guard AI 
        mampu memberikan solusi konkret bagi efisiensi modal klien. Visi jangka panjang beliau adalah membangun ekosistem bisnis 
        yang lebih sehat di Indonesia, di mana setiap rupiah investasi terjaga dengan aman dan setiap transaksi dapat dipertanggungjawabkan 
        secara transparan, guna mendorong pertumbuhan ekonomi yang berkelanjutan bagi seluruh mitra yang bekerja sama dengannya.
        """)

# --- MENU 4: REGISTRASI (DENGAN NAMA PELANGGAN - DIPERTAHANKAN) ---
elif menu == "4. 📝 Registrasi & Capture":
    st.header("Pendaftaran Klien Baru")
    with st.form("reg_form"):
        st.text_input("Nama Pelanggan (Pemilik):")
        st.text_input("Nama Bisnis / Perusahaan:")
        st.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO", "ELITE"])
        st.file_uploader("Upload Bukti Pembayaran / KTP", type=['jpg','png','jpeg'])
        if st.form_submit_button("Kirim Pendaftaran"):
            st.success("Data berhasil terkirim!")

# --- MENU 5: ADMIN CONTROL CENTER (FITUR UTAMA KEMBALI & TANPA PASSWORD) ---
elif menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Dashboard Kendali Admin")
    
    df = pd.DataFrame(st.session_state.db_nasabah)
    
    # A. ALARM FRAUD (> 1 JUTA)
    st.subheader("🚨 Alarm Keamanan")
    fraud_list = df[df['Harga'] > 1000000]
    if not fraud_list.empty:
        for _, row in fraud_list.iterrows():
            st.markdown(f'<div class="fraud-alert">⚠️ ALARM FRAUD: Bisnis "{row["Bisnis"]}" terdeteksi transaksi Rp {row["Harga"]:,.0f}</div>', unsafe_allow_html=True)
    else:
        st.write("Tidak ada aktivitas fraud mencurigakan.")

    # B. NOTIFIKASI INVOICE / PIUTANG
    st.subheader("💰 Status Piutang (Invoice)")
    piutang_list = df[df['Status'] == "🔴 Menunggu"]
    if not piutang_list.empty:
        for _, row in piutang_list.iterrows():
            st.markdown(f'<div class="invoice-box">📌 INVOICE PENDING: {row["Pelanggan"]} - {row["Bisnis"]} (Rp {row["Harga"]:,.0f})</div>', unsafe_allow_html=True)
    
    # C. TAMBAH MENU KLIEN (INPUT ADMIN)
    with st.expander("➕ Tambah Data Klien Baru", expanded=False):
        with st.form("admin_add"):
            c1, c2 = st.columns(2)
            new_p = c1.text_input("Nama Pelanggan:")
            new_b = c1.text_input("Nama Bisnis:")
            new_h = c2.number_input("Harga Paket (Rp):", value=1500000)
            new_s = c2.selectbox("Status:", ["🟢 AKTIF", "🔴 Menunggu"])
            if st.form_submit_button("Simpan ke Database"):
                new_id = st.session_state.db_nasabah[-1]["ID"] + 1
                st.session_state.db_nasabah.append({
                    "ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d"),
                    "Pelanggan": new_p, "Bisnis": new_b, "Paket": "MANUAL", 
                    "Harga": new_h, "Status": new_s, "Log": "Admin Added"
                })
                st.rerun()

    # D. TABEL DATA & CSV EXPORT
    st.write("---")
    st.subheader("📊 Database Keseluruhan")
    st.download_button("📥 Download Laporan (CSV)", df.to_csv(index=False).encode('utf-8'), "Laporan_VGuard.csv", "text/csv")
    st.dataframe(df, use_container_width=True)

# --- MENU LAINNYA ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("Analisis Strategis")
    st.info("**Visi:** Benteng pertahanan digital utama.")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    st.metric("Potensi Hemat (7%)", f"Rp {omzet * 0.07:,.0f}")

elif menu == "3. 📦 Paket Unggulan":
    st.header("Layanan V-Guard AI")
    cols = st.columns(4)
    pkgs = [("BASIC", "1.5jt"), ("SMART", "2.5jt"), ("PRO", "5jt
