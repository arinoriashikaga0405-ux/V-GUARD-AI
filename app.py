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
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "MEDIUM", "Harga": 7500000, "Status": "🟢 AKTIF", "Log": "System Initialized"}
    ]

if 'admin_auth' not in st.session_state:
    st.session_state.admin_auth = False

# Teks Profil Founder
profil_txt = (
    "Bapak Erwin Sinaga adalah seorang Senior Business Leader yang memiliki rekam jejak profesional selama lebih dari 10 tahun "
    "di sektor Perbankan dan Manajemen Aset. Sebagai mantan CEO dan CSO, beliau memahami secara mendalam tantangan "
    "kebocoran finansial yang sering dihadapi oleh pemilik bisnis. Dedikasi beliau terhadap integritas dan transparansi "
    "melahirkan V-Guard AI, sebuah platform cerdas yang dirancang untuk melindungi aset pelaku usaha melalui teknologi "
    "kecerdasan buatan. Melalui kepemimpinannya, V-Guard AI tidak hanya menjadi alat monitor transaksi, tetapi menjadi "
    "mitra strategis dalam pengambilan keputusan bisnis berbasis data. Berdomisili di Tangerang, beliau aktif mengedukasi "
    "komunitas digital mengenai pentingnya pengawasan berlapis untuk mencegah fraud. Visi beliau adalah mendigitalisasi "
    "fungsi audit internal agar dapat diakses oleh semua skala bisnis, mulai dari UMKM hingga korporasi besar, guna "
    "memastikan setiap rupiah investasi klien terjaga dengan aman dan memberikan hasil maksimal bagi pertumbuhan ekonomi nasional."
)

# 2. CSS CUSTOM
st.markdown("""
<style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }
    .fraud-alert { background: #f8d7da; color: #721c24; padding: 15px; border-radius: 10px; border-left: 10px solid #dc3545; font-weight: bold; animation: blinker 1s linear infinite; margin-bottom: 10px; }
    .piutang-box { background: #fff3cd; color: #856404; padding: 15px; border-radius: 10px; border-left: 10px solid #ffc107; margin-bottom: 10px; font-weight: bold; }
    .card-box { background: white; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); border-top: 5px solid #1E3A8A; min-height: 120px; text-align: center; }
    @keyframes blinker { 50% { opacity: 0.2; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 📦 Produk Unggulan", "4. 📝 Registrasi & Capture", "5. 🔐 Admin Control Center", "6. 📜 Laporan Audit Klien"])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/628212190885")

# --- MENU 1: PROFIL ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Founder")
    c1, c2 = st.columns([1, 2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write(profil_txt)

# --- MENU 2: VISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("Visi, Misi & Analisis ROI")
    st.info("**Visi:** Menjadi benteng pertahanan digital utama bagi ekosistem bisnis di Indonesia.")
    st.success("**Misi:** Meminimalisir kebocoran transaksi hingga 0% melalui audit real-time.")
    st.write("---")
    omzet_input = st.number_input("Input Omzet Bulanan (Rp):", value=100000000)
    save_val = omzet_input * 0.07
    roi_val = ((save_val - 2500000) / 2500000) * 100
    st.metric("Estimasi ROI Bulanan", f"{roi_val:.1f}%", f"Efisiensi Rp {save_val:,.0f}")

# --- MENU 3: 4 PRODUK ---
elif menu == "3. 📦 Produk Unggulan":
    st.header("4 Layanan Unggulan V-Guard")
    p1, p2, p3, p4 = st.columns(4)
    p1.markdown('<div class="card-box"><b>V-Guard BASIC</b><br><small>Monitor Harian</small></div>', unsafe_allow_html=True)
    p2.markdown('<div class="card-box"><b>V-Guard SMART</b><br><small>Deteksi Fraud AI</small></div>', unsafe_allow_html=True)
    p3.markdown('<div class="card-box"><b>V-Guard PRO</b><br><small>Audit Mingguan</small></div>', unsafe_allow_html=True)
    p4.markdown('<div class="card-box"><b>V-Guard ELITE</b><br><small>Konsultasi Founder</small></div>', unsafe_allow_html=True)

# --- MENU 4: REGISTRASI ---
elif menu == "4. 📝 Registrasi & Capture":
    st.header("Registrasi & Capture Mandiri")
    with st.form("reg_form"):
        st.text_input("Nama PIC:")
        st.text_input("Nama Bisnis/Perusahaan:")
        st.file_uploader("Upload Capture Bukti Bayar / KTP", type=['jpg','png','jpeg'])
        if st.form_submit_button("Kirim Pendaftaran"):
            st.success("Terima kasih! Data telah kami terima untuk verifikasi Admin.")

# --- MENU 5: ADMIN CONTROL CENTER ---
elif menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Dashboard")
    if not st.session_state.admin_auth:
        pw_input = st.text_input("Sandi Otoritas:", type="password")
        if pw_input == "w1nbju8282":
            st.session_state.admin_auth = True
            st.rerun()
    else:
        if st.button("🔒 Logout Admin"):
            st.session_state.admin_auth = False
            st.rerun()
        
        df_admin = pd.DataFrame(st.session_state.db_nasabah)
        
        with st.expander("➕ TAMBAH AKUN KLIEN BARU", expanded=True):
            with st.form("add_new"):
                col_a, col_b = st.columns(2)
                a_pic = col_a.text_input("Nama PIC:")
                a_bis = col_a.text_input("Nama Bisnis:")
                a_hrg = col_b.number_input("Harga Investasi:", value=2500000)
                a_pkt = col_b.selectbox("Paket:", ["BASIC", "SMART", "PRO", "ELITE"])
                if st.form_submit_button("Simpan Data"):
                    new_id = st.session_state.db_nasabah[-1]["ID"] + 1 if st.session_state.db_nasabah else 101
                    st.session_state.db_nasabah.append({
                        "ID": new_id, "Waktu": datetime.now().strftime("%Y-%m-%d"),
                        "Pelanggan": a_pic, "Bisnis": a_bis, "Paket": a_pkt, "Harga": a_hrg,
                        "Status": "🔴 Menunggu", "Log": "Manual Input"
                    })
                    st.rerun()

        # Alarm Fraud
        fraud_chk = df_admin[df_admin['Harga'] > 1000000]
        for _, r in fraud_chk.iterrows():
            st.markdown(f'<div class="fraud-alert">⚠️ ALARM FRAUD: {r["Bisnis"]} (Rp {r["Harga"]:,.0f}) Terdeteksi!</div>', unsafe_allow_html=True)

        # Piutang
        piutang_chk = df_admin[df_admin['Status'] == "🔴 Menunggu"]
        for _, p in piutang_chk.iterrows():
            st.markdown(f'<div class="piutang-box">📌 PIUTANG: {p["Bisnis"]} (Rp {p["Harga"]:,.0f}) Belum Lunas.</div>', unsafe_allow_html=True)
        
        st.download_button("📥 Export CSV", df_admin.to_csv(index=False).encode('utf-8'), "Database.csv", "text/csv")
        st.dataframe(df_admin, use_container_width=True)

# --- MENU 6: AUDIT TERKUNCI ---
elif menu == "6. 📜 Laporan Audit Klien":
    st.header("Laporan Audit (Restricted)")
    pw_audit = st.text_input("Masukkan Sandi Audit:", type="password")
    if pw_audit == "w1nbju8282":
        st.table(pd.DataFrame(st.session_state.db_nasabah)[["ID", "Waktu", "Bisnis", "Status", "Log"]])
    elif pw_audit != "":
        st.error("Akses Ditolak!")

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
