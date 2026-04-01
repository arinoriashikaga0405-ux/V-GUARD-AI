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

# 2. CSS CUSTOM (Alarm Berkedip & Styling Notifikasi)
st.markdown("""
<style>
    .status-connected { color: #28a745; font-weight: bold; font-size: 14px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .fraud-alert { background: #f8d7da; color: #721c24; padding: 15px; border-radius: 10px; border-left: 10px solid #dc3545; font-weight: bold; animation: blinker 1s linear infinite; margin-bottom: 10px; }
    .piutang-box { background: #fff3cd; color: #856404; padding: 15px; border-radius: 10px; border-left: 10px solid #ffc107; margin-bottom: 10px; font-weight: bold; }
    .profile-box { text-align: justify; line-height: 1.6; padding: 20px; background: white; border-radius: 10px; border: 1px solid #eee; }
    @keyframes blinker { 50% { opacity: 0.2; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi:", [
        "1. 👤 Profil Founder", 
        "4. 📝 Registrasi & Capture", 
        "5. 🔐 Admin Control Center", 
        "6. 📜 Laporan Audit Klien"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- MENU 5: ADMIN CONTROL CENTER (SEMUA FITUR KEMBALI) ---
if menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Intelligence Control")

    # LOGIKA LOGIN SEKALI PAKAI
    if not st.session_state.admin_authenticated:
        pw = st.text_input("Sandi Otoritas:", type="password")
        if pw == "w1nbju8282":
            st.session_state.admin_authenticated = True
            st.rerun()
        elif pw != "":
            st.error("Sandi Salah!")
    
    else:
        # Dashboard Terbuka (Input Password Sudah Hilang)
        col_header, col_logout = st.columns([5, 1])
        col_header.subheader("Selamat Datang, Pak Erwin")
        if col_logout.button("🔒 Kunci Folder"):
            st.session_state.admin_authenticated = False
            st.rerun()

        df = pd.DataFrame(st.session_state.db_nasabah)

        # FITUR A: TAMBAH AKUN KLIEN BARU (Input Manual)
        with st.expander("➕ TAMBAH AKUN KLIEN BARU"):
            with st.form("admin_add_form"):
                c1, c2 = st.columns(2)
                adm_pic = c1.text_input("Nama PIC:")
                adm_bis = c1.text_input("Nama Bisnis:")
                adm_hrg = c2.number_input("Harga Investasi (Rp):", value=2500000)
                adm_pkt = c2.selectbox("Paket:", ["BASIC", "MEDIUM", "ENTERPRISE", "CORPORATE"])
                adm_wa = st.text_input("WhatsApp (Contoh: 62812...)")
                
                if st.form_submit_button("Daftarkan Klien Sekarang"):
                    if adm_pic and adm_bis:
                        new_id = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
                        st.session_state.db_nasabah.append({
                            "ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"),
                            "Pelanggan": adm_pic, "Bisnis": adm_bis, "Paket": adm_pkt, "Harga": adm_hrg,
                            "Status": "🔴 Menunggu", "Jatuh_Tempo": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
                            "Log": "Manual Input by Admin"
                        })
                        st.success(f"Akun {adm_bis} Berhasil Dibuat!")
                        st.rerun()

        # FITUR B: ALARM INDIKASI FRAUD (> 1 JUTA)
        st.write("---")
        st.subheader("🚨 Alarm Keamanan (Monitoring > Rp 1 Juta)")
        fraud_df = df[df['Harga'] > 1000000]
        if not fraud_df.empty:
            for _, r in fraud_df.iterrows():
                st.markdown(f'<div class="fraud-alert">⚠️ ALARM FRAUD: Transaksi {r["Bisnis"]} senilai Rp {r["Harga"]:,.0f} Terdeteksi!</div>', unsafe_allow_html=True)
        else:
            st.info("Tidak ada indikasi fraud saat ini.")

        # FITUR C: NOTIFIKASI INVOICE PIUTANG (Status Menunggu)
        st.subheader("📅 Notifikasi Piutang & Penagihan")
        piutang_df = df[df['Status'] == "🔴 Menunggu"]
        if not piutang_df.empty:
            for _, p in piutang_df.iterrows():
                st.markdown(f'<div class="piutang-box">📌 PIUTANG AKTIF: {p["Bisnis"]} (Rp {p["Harga"]:,.0f}) - JT: {p["Jatuh_Tempo"]}</div>', unsafe_allow_html=True)
                msg_wa = f"Halo {p['Pelanggan']}, mohon penyelesaian pembayaran V-Guard AI untuk {p['Bisnis']} sebesar Rp {p['Harga']:,.0f}. Terima kasih."
                st.link_button(f"📲 Hubungi {p['Pelanggan']}", f"https://wa.me/62?text={urllib.parse.quote(msg_wa)}")
        else:
            st.success("Semua tagihan lunas.")

        # FITUR D: EKSPOR CSV & DATABASE
        st.write("---")
        st.subheader("📋 Manajemen Database")
        col_s, col_csv = st.columns([3, 1])
        s_query = col_s.text_input("🔍 Cari Bisnis/PIC:")
        col_csv.download_button("📥 Export CSV", df.to_csv(index=False).encode('utf-8'), "Data_VGuard_Audit.csv", "text/csv")

        f_df = df[df['Pelanggan'].str.contains(s_query, case=False) | df['Bisnis'].str.contains(s_query, case=False)]
        for i, row in f_df.iterrows():
            with st.expander(f"{row['Status']} | {row['Bisnis']}"):
                col_btn1, col_btn2 = st.columns(2)
                if row['Status'] == "🔴 Menunggu":
                    if col_btn1.button("🟢 Aktifkan Akun", key=f"ac_{row['ID']}"):
                        for item in st.session_state.db_nasabah:
                            if item['ID'] == row['ID']: item['Status'] = "🟢 AKTIF"
                        st.rerun()
                if col_btn2.button("🗑️ Hapus Data", key=f"del_{row['ID']}"):
                    st.session_state.db_nasabah = [x for x in st.session_state.db_nasabah if x['ID'] != row['ID']]
                    st.rerun()

# --- MENU 6: LAPORAN AUDIT TRAIL (RAPI) ---
elif menu == "6. 📜 Laporan Audit Klien":
    st.header("📜 Laporan Audit Trail")
    st.info("Seluruh jejak pendaftaran dan aktivasi terekam secara otomatis di sini.")
    df_audit = pd.DataFrame(st.session_state.db_nasabah)
    for i, row in df_audit.iterrows():
        st.markdown(f"""<div style="background:white; padding:15px; border-radius:10px; border-left:5px solid #6c757d; margin-bottom:10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);">
        <b>ID: #{row['ID']} - {row['Bisnis']}</b><br>
        <small>Waktu: {row['Waktu']} | PIC: {row['Pelanggan']} | Log: {row['Log']}</small>
        </div>""", unsafe_allow_html=True)

# --- MENU PROFIL FOUNDER ---
elif menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c_img, c_txt = st.columns([1, 2.5])
    with c_img:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c_txt:
        st.markdown(f'<div class="profile-box"><b>Bapak Erwin Sinaga</b> adalah Senior Business Leader dengan pengalaman lebih dari 10 tahun di industri Perbankan dan Manajemen Aset. V-Guard AI merupakan visi beliau untuk menghadirkan transparansi dan keamanan aset tingkat tinggi bagi seluruh pengusaha di Indonesia.</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
