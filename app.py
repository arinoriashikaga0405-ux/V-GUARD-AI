import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database & Status Login
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25 08:00", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "MEDIUM", "Harga": 7500000, "Status": "🟢 AKTIF", "Jatuh_Tempo": "2026-04-25", "Log": "System Initialized"}
    ]

if 'admin_authenticated' not in st.session_state:
    st.session_state.admin_authenticated = False

# 2. CSS CUSTOM (Alarm Fraud & Styling)
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .fraud-alert { background: #f8d7da; color: #721c24; padding: 15px; border-radius: 10px; border-left: 10px solid #dc3545; font-weight: bold; animation: blinker 1s linear infinite; margin-bottom: 10px; }
    .piutang-box { background: #fff3cd; color: #856404; padding: 15px; border-radius: 10px; border-left: 10px solid #ffc107; margin-bottom: 10px; font-weight: bold; }
    @keyframes blinker { 50% { opacity: 0.2; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi:", ["1. 👤 Profil Founder", "4. 📝 Registrasi", "5. 🔐 Admin Control Center", "6. 📜 Laporan Audit"])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- MENU 5: ADMIN CONTROL CENTER ---
if menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Control")

    # Logika Login: Input password hilang jika sudah benar
    if not st.session_state.admin_authenticated:
        pw = st.text_input("Sandi Otoritas:", type="password")
        if pw == "w1nbju8282":
            st.session_state.admin_authenticated = True
            st.rerun()
        elif pw != "":
            st.error("Sandi Salah!")
    
    else:
        # Dashboard Admin Terbuka
        if st.button("🔒 Logout / Kunci Folder"):
            st.session_state.admin_authenticated = False
            st.rerun()

        df = pd.DataFrame(st.session_state.db_nasabah)

        # A. TAMBAH AKUN KLIEN BARU
        with st.expander("➕ TAMBAH AKUN KLIEN BARU"):
            with st.form("add_form"):
                c1, c2 = st.columns(2)
                p_pic = c1.text_input("Nama PIC:")
                p_bis = c1.text_input("Nama Bisnis:")
                p_hrg = c2.number_input("Harga (Rp):", value=2500000)
                p_pkt = c2.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE"])
                if st.form_submit_button("Simpan Akun"):
                    new_id = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
                    data_baru = {
                        "ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "Pelanggan": p_pic, "Bisnis": p_bis, "Paket": p_pkt, "Harga": p_hrg,
                        "Status": "🔴 Menunggu", "Jatuh_Tempo": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
                        "Log": "Manual Admin Input"
                    }
                    st.session_state.db_nasabah.append(data_baru)
                    st.success("Berhasil Ditambahkan!")
                    st.rerun()

        # B. ALARM FRAUD (> 1 JUTA)
        st.write("---")
        st.subheader("🚨 Alarm Keamanan")
        fraud = df[df['Harga'] > 1000000]
        if not fraud.empty:
            for _, r in fraud.iterrows():
                st.markdown(f'<div class="fraud-alert">⚠️ FRAUD DETECTED: {r["Bisnis"]} (Rp {r["Harga"]:,.0f})</div>', unsafe_allow_html=True)

        # C. NOTIFIKASI PIUTANG
        st.subheader("📅 Daftar Piutang")
        piutang = df[df['Status'] == "🔴 Menunggu"]
        for _, p in piutang.iterrows():
            st.markdown(f'<div class="piutang-box">📌 TAGIHAN: {p["Bisnis"]} - Rp {p["Harga"]:,.0f}</div>', unsafe_allow_html=True)

        # D. DATABASE & EXPORT
        st.write("---")
        st.download_button("📥 Export CSV", df.to_csv(index=False).encode('utf-8'), "Audit_VGuard.csv", "text/csv")
        st.dataframe(df, use_container_width=True)

# --- MENU LAINNYA ---
elif menu == "1. 👤 Profil Founder":
    st.header("Profil Founder")
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", width=200)
    st.write("Bapak Erwin Sinaga - Senior Business Leader V-Guard AI.")

elif menu == "6. 📜 Laporan Audit":
    st.header("📜 Laporan Audit Trail")
    st.table(pd.DataFrame(st.session_state.db_nasabah)[["Waktu", "Bisnis", "Log"]])

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
