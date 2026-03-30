import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI & SESSION STATE (Penyimpanan Sementara)
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")

if 'db_aktivasi' not in st.session_state:
    st.session_state.db_aktivasi = []

# 2. CSS CUSTOM
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 18px; }
    .package-box { height: 500px; padding: 20px; border: 1px solid #e0e0e0; border-radius: 10px; background-color: #ffffff; margin-bottom: 10px; }
    .footer-container { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #f8f9fa; text-align: center; padding: 15px 0px; font-weight: bold; border-top: 1px solid #dee2e6; z-index: 9999; }
    .stApp { margin-bottom: 100px; }
</style>
""", unsafe_allow_html=True)

wa_url = "https://wa.me/628212190885"

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Menu Utama:", ["1. 👤 Profil", "2. 🎯 Strategi & ROI", "3. 📦 Pilih Paket Layanan", "4. 🔐 Admin Dashboard"])
    st.markdown('<p class="status-connected">● System Online</p>', unsafe_allow_html=True)

# --- MENU 1 & 2 (PROFIL & ROI TETAP SAMA) ---
if menu == "1. 👤 Profil":
    st.header("Strategic Leadership")
    st.write("Profil Senior Business Leader Erwin Sinaga...") 
elif menu == "2. 🎯 Strategi & ROI":
    st.header("Analisis ROI")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=500000000)
    st.success(f"Potensi Penyelamatan: Rp {omzet * 0.05 * 0.9:,.0f}")

# --- MENU 3: PILIH PAKET (FITUR PENERIMA DATA KLIEN) ---
elif menu == "3. 📦 Pilih Paket Layanan":
    st.header("📦 Registrasi Layanan V-Guard")
    st.write("Silakan pilih paket untuk mengirimkan permintaan aktivasi ke Admin.")
    
    with st.form("form_registrasi"):
        nama_bisnis = st.text_input("Nama Bisnis/Toko:")
        email_kontak = st.text_input("Email/WA:")
        paket_pilihan = st.selectbox("Pilih Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
        submit = st.form_submit_button("Kirim Permintaan Aktivasi")
        
        if submit:
            if nama_bisnis and email_kontak:
                # Menyimpan data ke 'database' admin sementara
                new_reg = {"Waktu": datetime.now().strftime("%H:%M"), "Bisnis": nama_bisnis, "Paket": paket_pilihan, "Status": "Pending"}
                st.session_state.db_aktivasi.append(new_reg)
                st.success(f"Permintaan paket {paket_pilihan} berhasil dikirim! Admin akan segera mengaktifkan akun Anda.")
            else:
                st.error("Mohon isi data dengan lengkap.")

# --- MENU 4: ADMIN DASHBOARD (FITUR MONITORING & AKTIVASI) ---
elif menu == "4. 🔐 Admin Dashboard":
    st.header("🔐 Intelligence Center")
    u_id = st.text_input("Username:")
    p_id = st.text_input("Password:", type="password")
    
    if u_id == "erwin_admin" and p_id == "w1nbju8282":
        st.success("Welcome, Super Admin.")
        t1, t2, t3 = st.tabs(["📩 Antrean Aktivasi", "🕒 Jadwal & Load", "📊 Database Klien"])
        
        with t1:
            st.subheader("Permintaan Aktivasi Masuk")
            if st.session_state.db_aktivasi:
                df_act = pd.DataFrame(st.session_state.db_aktivasi)
                st.table(df_act)
                st.info("Gunakan data di atas untuk mengaktifkan modul AI di server.")
            else:
                st.write("Belum ada permintaan aktivasi baru.")
        
        with t2:
            st.subheader("Jadwal Pengiriman Data (Anti-Overload)")
            df_j = pd.DataFrame({"Kategori":["Retail","F&B","Corporate"],"Slot":["21:00","23:00","Realtime"]})
            st.table(df_j)
            
        with t3:
            st.subheader("Klien Aktif")
            df_k = pd.DataFrame({"Nama":["Toko Jaya","Sentosa Corp"],"Paket":["BASIC","CORP"],"Aktif s/d":["Des 2026","Jan 2027"]})
            st.table(df_k)

    elif u_id == "klien001": # Simulasi akun yang sudah aktif
        st.header("Dashboard Toko Jaya")
        st.metric("Status Paket", "BASIC (Active)")
        st.file_uploader("Upload Transaksi Hari Ini")

# 4. FOOTER
st.markdown('<div class="footer-container">© 2026 V-Guard AI Systems</div>', unsafe_allow_html=True)
