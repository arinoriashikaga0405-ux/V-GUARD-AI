import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database & Login State
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25 08:00", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "MEDIUM", "Harga": 7500000, "Status": "🟢 AKTIF", "Jatuh_Tempo": "2026-04-25", "Log": "System Initialized"}
    ]

if 'admin_authenticated' not in st.session_state:
    st.session_state.admin_authenticated = False

# 2. CSS CUSTOM (Alarm Berkedip & Styling)
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .fraud-alert { background: #f8d7da; color: #721c24; padding: 20px; border-radius: 10px; border-left: 10px solid #dc3545; font-weight: bold; animation: blinker 1s linear infinite; margin-bottom: 15px; }
    .piutang-box { background: #fff3cd; color: #856404; padding: 20px; border-radius: 10px; border-left: 10px solid #ffc107; margin-bottom: 15px; font-weight: bold; }
    @keyframes blinker { 50% { opacity: 0.2; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi:", ["1. 👤 Profil Founder", "5. 🔐 Admin Control Center", "6. 📜 Laporan Audit Klien"])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- MENU 5: ADMIN CONTROL CENTER ---
if menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Control")

    # LOGIKA LOGIN: Input Password Hilang Jika Benar
    if not st.session_state.admin_authenticated:
        pw = st.text_input("Masukkan Sandi Otoritas:", type="password")
        if pw == "w1nbju8282":
            st.session_state.admin_authenticated = True
            st.rerun()
        elif pw != "":
            st.error("Sandi Salah!")
    
    else:
        # TAMPILAN SETELAH LOGIN (Sesuai Permintaan Bapak)
        st.success("Akses Diterima. Selamat Datang Pak Erwin.")
        if st.button("🔒 Logout & Kunci Dashboard"):
            st.session_state.admin_authenticated = False
            st.rerun()

        df = pd.DataFrame(st.session_state.db_nasabah)

        # FITUR 1: TAMBAH AKUN KLIEN BARU (FORM TERBUKA)
        st.write("---")
        st.subheader("➕ Menu Tambah Akun Klien")
        with st.form("tambah_akun_admin"):
            c1, c2 = st.columns(2)
            pic = c1.text_input("Nama PIC:")
            bisnis = c1.text_input("Nama Bisnis:")
            harga = c2.number_input("Nilai Investasi (Rp):", value=2500000)
            paket = c2.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
            if st.form_submit_button("Simpan & Daftarkan"):
                if pic and bisnis:
                    new_id = st.session_state.db_nasabah[-1]["ID"] + 1
                    st.session_state.db_nasabah.append({
                        "ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "Pelanggan": pic, "Bisnis": bisnis, "Paket": paket, "Harga": harga,
                        "Status": "🔴 Menunggu", "Jatuh_Tempo": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
                        "Log": "Manual Admin Input"
                    })
                    st.success("Klien Berhasil Ditambahkan!")
                    st.rerun()

        # FITUR 2: ALARM INDIKASI FRAUD (> 1 JUTA)
        st.write("---")
        st.subheader("🚨 Monitoring Fraud (Transaksi > Rp 1 Juta)")
        fraud_df = df[df['Harga'] > 1000000]
        if not fraud_df.empty:
            for _, r in fraud_df.iterrows():
                st.markdown(f'<div class="fraud-alert">⚠️ ALARM: Transaksi {r["Bisnis"]} (Rp {r["Harga"]:,.0f}) Melebihi Limit!</div>', unsafe_allow_html=True)
        else:
            st.info("Keamanan Terkendali.")

        # FITUR 3: NOTIFIKASI INVOICE PIUTANG
        st.write("---")
        st.subheader("📅 Notifikasi Piutang (Belum Bayar)")
        piutang_df = df[df['Status'] == "🔴 Menunggu"]
        if not piutang_df.empty:
            for _, p in piutang_df.iterrows():
                st.markdown(f'<div class="piutang-box">📌 TAGIHAN AKTIF: {p["Bisnis"]} | Rp {p["Harga"]:,.0f} | JT: {p["Jatuh_Tempo"]}</div>', unsafe_allow_html=True)
        else:
            st.success("Tidak ada piutang tertunggak.")

        # FITUR 4: DATABASE & EXPORT CSV
        st.write("---")
        st.subheader("📋 Database Klien & Export CSV")
        st.download_button("📥 Unduh Database (CSV)", df.to_csv(index=False).encode('utf-8'), "VGuard_Audit.csv", "text/csv")
        st.dataframe(df, use_container_width=True)

# --- MENU LAIN ---
elif menu == "1. 👤 Profil Founder":
    st.header("Profil Founder")
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", width=200)
    st.write("Bapak Erwin Sinaga - Senior Business Leader V-Guard AI.")

elif menu == "6. 📜 Laporan Audit Klien":
    st.header("📜 Laporan Audit Trail")
    st.table(pd.DataFrame(st.session_state.db_nasabah)[["ID", "Waktu", "Bisnis", "Log"]])

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
