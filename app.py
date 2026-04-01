import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database & Login State agar tidak hilang saat pindah menu
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {
            "ID": 101, 
            "Waktu": "2026-03-25 08:00", 
            "Pelanggan": "Siska", 
            "Bisnis": "Cafe Maju", 
            "Paket": "MEDIUM", 
            "Harga": 7500000, 
            "Status": "🟢 AKTIF", 
            "Jatuh_Tempo": "2026-04-25",
            "Log": "System Initialized"
        }
    ]

if 'admin_authenticated' not in st.session_state:
    st.session_state.admin_authenticated = False

# 2. CSS CUSTOM (Alarm Fraud & Styling)
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .fraud-alert { background: #f8d7da; color: #721c24; padding: 20px; border-radius: 10px; border-left: 10px solid #dc3545; font-weight: bold; animation: blinker 1s linear infinite; margin-bottom: 15px; }
    .piutang-box { background: #fff3cd; color: #856404; padding: 20px; border-radius: 10px; border-left: 10px solid #ffc107; margin-bottom: 15px; font-weight: bold; }
    .roi-card { background: #e3f2fd; padding: 20px; border-radius: 10px; border-left: 5px solid #2196f3; }
    @keyframes blinker { 50% { opacity: 0.2; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi & ROI", 
        "3. 📦 Layanan Produk", 
        "4. 📝 Registrasi & Capture", 
        "5. 🔐 Admin Control Center", 
        "6. 📜 Laporan Audit Klien"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- MENU 1: PROFIL FOUNDER ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2.5])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("Senior Business Leader dengan 10+ tahun pengalaman di Perbankan & Asset Management. Founder V-Guard AI Intelligence.")

# --- MENU 2: VISI & ROI ---
elif menu == "2. 🎯 Visi & ROI":
    st.header("🎯 Visi & Analisis ROI")
    st.markdown('<div class="roi-card"><b>Visi:</b> Menjadi standar emas pengawasan AI untuk transparansi finansial UMKM di Indonesia.</div>', unsafe_allow_html=True)
    st.write("---")
    investasi = st.number_input("Estimasi Omzet Bulanan Bisnis (Rp):", value=100000000)
    fraud_save = investasi * 0.05
    st.metric("Potensi Penyelamatan Fraud (5%)", f"Rp {fraud_save:,.0f}")

# --- MENU 3: LAYANAN PRODUK ---
elif menu == "3. 📦 Layanan Produk":
    st.header("📦 Solusi V-Guard AI")
    colA, colB, colC = st.columns(3)
    colA.help("BASIC: Pengawasan Transaksi Dasar")
    colB.help("MEDIUM: Deteksi Fraud AI & Laporan Mingguan")
    colC.help("ENTERPRISE: Audit Full-Service & Pendampingan")

# --- MENU 5: ADMIN CONTROL CENTER (FITUR UTAMA) ---
elif menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Control")

    if not st.session_state.admin_authenticated:
        pw = st.text_input("Masukkan Sandi Otoritas:", type="password")
        if pw == "w1nbju8282":
            st.session_state.admin_authenticated = True
            st.rerun()
        elif pw != "": st.error("Sandi Salah!")
    
    else:
        st.success("Akses Diterima. Dashboard Aktif.")
        if st.button("🔒 Logout & Kunci"):
            st.session_state.admin_authenticated = False
            st.rerun()

        df = pd.DataFrame(st.session_state.db_nasabah)

        # FITUR: TAMBAH AKUN
        with st.expander("➕ TAMBAH AKUN KLIEN BARU", expanded=True):
            with st.form("admin_add"):
                c1, c2 = st.columns(2)
                pic = c1.text_input("Nama PIC:")
                bis = c1.text_input("Nama Bisnis:")
                hrg = c2.number_input("Harga (Rp):", value=2500000)
                pkt = c2.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE"])
                if st.form_submit_button("Daftarkan Klien"):
                    new_id = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
                    st.session_state.db_nasabah.append({
                        "ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "Pelanggan": pic, "Bisnis": bis, "Paket": pkt, "Harga": hrg,
                        "Status": "🔴 Menunggu", "Jatuh_Tempo": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
                        "Log": "Manual Input Admin"
                    })
                    st.rerun()

        # FITUR: ALARM FRAUD (> 1 JUTA)
        fraud_df = df[df['Harga'] > 1000000]
        if not fraud_df.empty:
            for _, r in fraud_df.iterrows():
                st.markdown(f'<div class="fraud-alert">⚠️ ALARM FRAUD: {r["Bisnis"]} (Rp {r["Harga"]:,.0f}) Melebihi Limit!</div>', unsafe_allow_html=True)

        # FITUR: NOTIFIKASI PIUTANG
        piutang_df = df[df['Status'] == "🔴 Menunggu"]
        if not piutang_df.empty:
            for _, p in piutang_df.iterrows():
                st.markdown(f'<div class="piutang-box">📌 PIUTANG: {p["Bisnis"]} - Rp {p["Harga"]:,.0f}</div>', unsafe_allow_html=True)

        # FITUR: EXPORT CSV
        st.download_button("📥 Export CSV", df.to_csv(index=False).encode('utf-8'), "Database_VGuard.csv", "text/csv")
        st.dataframe(df, use_container_width=True)

# --- MENU 6: LAPORAN AUDIT (PERBAIKAN KEYERROR) ---
elif menu == "6. 📜 Laporan Audit Klien":
    st.header("📜 Laporan Audit Trail")
    if st.session_state.db_nasabah:
        df_audit = pd.DataFrame(st.session_state.db_nasabah)
        # Pastikan kolom yang dipanggil ada untuk mencegah KeyError
        cols = ["ID", "Waktu", "Bisnis", "Log"]
        st.table(df_audit[cols])
    else:
        st.info("Belum ada data audit.")

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
