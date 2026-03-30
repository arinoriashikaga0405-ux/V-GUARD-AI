import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

# Inisialisasi Database (Session State) agar data tidak hilang saat pindah menu
if 'db_transaksi' not in st.session_state:
    st.session_state.db_transaksi = [] # Untuk simpan file nota klien
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [] # Untuk simpan pendaftaran paket

# 2. CSS CUSTOM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 18px; }
    .footer-container { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #f8f9fa; text-align: center; padding: 15px 0px; font-weight: bold; border-top: 1px solid #dee2e6; z-index: 9999; }
    .stApp { margin-bottom: 100px; }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/628212190885"

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Folder Menu:", ["1. 👤 Profil & Filosofi", "2. 🎯 Visi & ROI", "3. 📦 Pendaftaran Klien", "4. 🔐 Admin Dashboard"])
    st.markdown('<p class="status-connected">● System Online</p>', unsafe_allow_html=True)
    st.link_button("📞 Konsultasi Langsung", wa_url, use_container_width=True)

# --- MENU 1 & 2 (PROFIL & ROI) ---
if menu == "1. 👤 Profil & Filosofi":
    st.header("👤 Strategic Leadership")
    st.write("Profil Bapak Erwin Sinaga (150+ Kata)...")
elif menu == "2. 🎯 Visi & ROI":
    st.header("🎯 Analisis ROI")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=500000000)
    st.success(f"Target Penyelamatan Aset: Rp {omzet * 0.05 * 0.9:,.0f}")

# --- MENU 3: PENDAFTARAN KLIEN ---
elif menu == "3. 📦 Pendaftaran Klien":
    st.header("📦 Registrasi Nasabah Baru")
    with st.form("form_reg"):
        n_bisnis = st.text_input("Nama Bisnis:")
        p_pilihan = st.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        sub_reg = st.form_submit_button("Kirim Data Pendaftaran")
        if sub_reg:
            st.session_state.db_nasabah.append({"Waktu": datetime.now().strftime("%H:%M"), "Nama": n_bisnis, "Paket": p_pilihan})
            st.success("Data pendaftaran terkirim ke Admin.")

# --- MENU 4: ADMIN DASHBOARD (Pusat Kendali Data) ---
elif menu == "4. 🔐 Admin Dashboard":
    st.header("🔐 Intelligence Center")
    u_id = st.text_input("Username:")
    p_id = st.text_input("Password:", type="password")
    
    # --- A. VIEW SUPER ADMIN (BAPAK ERWIN) ---
    if u_id == "erwin_admin" and p_id == "w1nbju8282": 
        st.success("Welcome, Super Admin Erwin.")
        t1, t2, t3, t4 = st.tabs(["📩 Pendaftaran", "🧾 Data Nota Klien", "🕒 Jadwal Server", "📊 Database"])
        
        with t1:
            st.subheader("Pendaftaran Nasabah Baru")
            st.table(pd.DataFrame(st.session_state.db_nasabah)) if st.session_state.db_nasabah else st.write("Belum ada pendaftaran.")
            
        with t2:
            st.subheader("Inspeksi Nota & Penjualan Klien")
            st.write("Di sini Bapak bisa melihat file transaksi yang sudah diunggah oleh klien.")
            if st.session_state.db_transaksi:
                df_nota = pd.DataFrame(st.session_state.db_transaksi)
                st.table(df_nota) # Menampilkan daftar file yang masuk
                st.info("Catatan: Klik nama file untuk melakukan audit AI (Simulasi).")
            else:
                st.write("Belum ada klien yang mengunggah nota hari ini.")
        
        with t3:
            st.subheader("Pengaturan Jadwal Anti-Overload")
            st.table(pd.DataFrame({"Usaha":["Retail","F&B","Corp"],"Jam Kirim":["21:00","23:00","Realtime"]}))
            
        with t4:
            st.subheader("Status Server")
            st.code("System Log: AI scan complete for Toko Jaya - No Fraud Detected.")

    # --- B. VIEW KLIEN (UNTUK DEMO KIRIM DATA) ---
    elif u_id == "klien001" and p_id == "owner123":
        st.success("Selamat Datang, Owner Toko Jaya.")
        st.subheader("📤 Unggah Nota Penjualan Hari Ini")
        file_nota = st.file_uploader("Pilih file Nota (Excel/CSV)", type=['csv', 'xlsx'])
        
        if file_nota is not None:
            if st.button("Kirim ke Admin"):
                # Simpan info file ke database agar Bapak bisa lihat di Admin
                info_nota = {
                    "Tanggal": datetime.now().strftime("%Y-%m-%d"),
                    "Nama Klien": "Toko Jaya",
                    "Nama File": file_nota.name,
                    "Ukuran": f"{file_nota.size / 1024:.1f} KB",
                    "Status Audit": "Menunggu Scan AI"
                }
                st.session_state.db_transaksi.append(info_nota)
                st.success(f"File {file_nota.name} berhasil terkirim ke server V-Guard.")

    elif p_id != "":
        st.error("Akses Ditolak.")

# 4. FOOTER
st.markdown('<div class="footer-container">© 2026 V-Guard AI Systems</div>', unsafe_allow_html=True)
