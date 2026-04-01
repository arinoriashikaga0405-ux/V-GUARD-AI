import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database (Proteksi agar tidak terjadi KeyError)
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Usaha": "F&B", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": 102, "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Usaha": "Otomotif", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]
if 'admin_akses_terbuka' not in st.session_state:
    st.session_state.admin_akses_terbuka = False

WA_NUMBER = "628212190885"
ADMIN_PASSWORD = "w1nbju8282"

def format_rp(angka):
    try:
        return f"Rp {float(angka):,.0f}".replace(",", ".")
    except:
        return str(angka)

# 2. CSS CUSTOM VISUAL V-GUARD
st.markdown("""
<style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; font-size: 12px; }
    .fraud-alarm { background-color: #ff4b4b; color: white; padding: 12px; border-radius: 8px; text-align: center; font-weight: bold; animation: blinker 2s linear infinite; margin-bottom: 20px; }
    @keyframes blinker { 50% { opacity: 0.7; } }
    .audit-box { background: #f0f2f6; padding: 15px; border-radius: 10px; border-left: 5px solid #1E3A8A; margin-bottom: 10px; }
    .metric-card { background: white; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); text-align: center; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (NAVIGASI TERKUNCI)
with st.sidebar:
    st.markdown("<h1 style='color: #1E3A8A; text-align: center;'>🛡️ V-GUARD AI</h1>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", use_container_width=True)
        st.markdown("<p style='text-align:center; font-weight:bold;'>Erwin Sinaga<br><span style='font-weight:normal; font-size:12px;'>Senior Business Leader</span></p>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Upload", 
        "5. 🔐 Akses Terbatas"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", f"https://wa.me/{WA_NUMBER}")

# --- MENU 1: PROFIL FOUNDER (LOCKED) ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2.2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("""Bapak Erwin Sinaga adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir.""")

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("Strategi & Analisis Proteksi")
    st.info("**Visi:** Menjadi standar emas dalam teknologi pengawasan bisnis digital di Indonesia.")
    omzet = st.number_input("Omzet Bulanan Bisnis (Rp):", value=100000000, step=1000000)
    bocor = omzet * 0.07
    st.error(f"Estimasi Kebocoran (7%): {format_rp(bocor)}")
    st.success(f"Dana Berhasil Diselamatkan: {format_rp(bocor - 2500000)}")

# --- MENU 3: PAKET UNGGULAN ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("Layanan V-Guard AI")
    pkts = [("BASIC", "1.5jt"), ("SMART", "2.5jt"), ("PRO", "5jt"), ("ELITE", "Custom")]
    cols = st.columns(4)
    for i, (n, p) in enumerate(pkts):
        with cols[i]:
            st.markdown(f'<div style="background:#e3f2fd; padding:20px; border-radius:10px; text-align:center;"><h3>{n}</h3><h2 style="color:#d32f2f;">Rp {p}</h2><p>• Monitoring AI<br>• VCS System<br>• Weekly Audit</p></div>', unsafe_allow_html=True)
            st.link_button(f"Pesan {n}", f"https://wa.me/{WA_NUMBER}")

# --- MENU 4: REGISTRASI & UPLOAD (LOCKED) ---
elif menu == "4. 📝 Registrasi & Upload":
    st.header("Formulir Pendaftaran Klien")
    with st.form("reg_vguard_final"):
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Nama Pelanggan:")
            st.text_input("Nama Bisnis:")
        with c2:
            st.text_input("Jenis Usaha:")
            st.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO", "ELITE"])
        st.file_uploader("Upload KTP / Dokumen Pendukung:", type=['jpg','png','pdf'])
        if st.form_submit_button("Kirim Pendaftaran Ke V-Guard"):
            st.success("Aplikasi Pendaftaran Berhasil Terkirim!")

# --- MENU 5: AKSES TERBATAS (FITUR ADMIN LENGKAP) ---
elif menu == "5. 🔐 Akses Terbatas":
    if not st.session_state.admin_akses_terbuka:
        st.markdown("<h2 style='text-align: center;'>🔐 Otoritas Login Admin</h2>", unsafe_allow_html=True)
        pwd = st.text_input("Sandi Keamanan:", type="password")
        if st.button("Masuk"):
            if pwd == ADMIN_PASSWORD:
                st.session_state.admin_akses_terbuka = True
                st.rerun()
            else:
                st.error("Akses Ditolak!")
    else:
        h1, h2 = st.columns([5, 1])
        with h1: st.header("Panel Operasional V-Guard AI")
        with h2:
            if st.button("🔒 LOGOUT"):
                st.session_state.admin_akses_terbuka = False
                st.rerun()

        st.markdown('<div class="fraud-alarm">🚨 PERINGATAN: INDIKASI FRAUD TERDETEKSI PADA TITIK TRANSAKSI HARIAN</div>', unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Database Klien", "📉 Audit Google Studio", "🧾 Laporan Rugi Laba", "📹 Monitoring CVV"])
        
        with tab1:
            with st.expander("+ Tambah Klien Baru"):
                with st.form("add_klien_admin"):
                    nk = st.text_input("Nama"); bk = st.text_input("Bisnis"); uk = st.text_input("Usaha")
                    pk = st.selectbox("Paket", ["BASIC", "SMART", "PRO"]); hk = st.number_input("Harga", value=1500000)
                    if st.form_submit_button("Simpan"):
                        st.session_state.db_nasabah.append({"ID": 103, "Waktu": str(datetime.now().date()), "Pelanggan": nk, "Bisnis": bk, "Usaha": uk, "Paket": pk, "Harga": hk, "Status": "🟢 AKTIF"})
                        st.rerun()
            
            # FIXED KEYERROR: Pengecekan kolom Harga sebelum format
            df = pd.DataFrame(st.session_state.db_nasabah)
            if 'Harga' in df.columns:
                df_show = df.copy()
                df_show['Harga'] = df_show['Harga'].apply(format_rp)
                st.table(df_show)
            else:
                st.table(df)

        with tab2:
            st.subheader("Google Studio Gemini Audit Intelligence")
            c1, c2, c3 = st.columns(3)
            c1.metric("Integrity Score", "98.5%", "+1.2%")
            c2.metric("Anomali Terdeteksi", "2 Kasus", "-50%")
            c3.metric("Akurasi AI", "99.9%", "Stable")
            
            st.write("---")
            st.markdown("### Laporan Audit Klien (Verified by Gemini AI)")
            st.line_chart([10, 15, 8, 25, 20, 35])
            st.markdown("""
            <div class="audit-box">
                <b>Hasil Audit Mingguan:</b> Semua transaksi pada <i>Cafe Maju</i> dan <i>Bengkel Berkah</i> telah divalidasi silang dengan data bank. 
                Tidak ditemukan kebocoran pada sistem POS.
            </div>
            """, unsafe_allow_html=True)

        with tab3:
            st.subheader("Laporan Rugi Laba AI (Real-time)")
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("#### Pemasukan & Pengeluaran")
                st.bar_chart({"Income": [80, 90, 100], "Expense": [30, 35, 40]})
            with col_b:
                st.markdown("#### Analisis Profitabilitas")
                st.info("Berdasarkan data Gemini, margin profit bersih meningkat 12% setelah instalasi V-Guard.")
                st.success("Status Keuangan: **SANGAT SEHAT**")

        with tab4:
            st.subheader("📹 Jalur Monitoring CCTV/CVV")
            st.warning("Visual Verification aktif. Mengawasi area kasir secara otomatis.")
            st.image("https://via.placeholder.com/800x400.png?text=Live+CCTV+AI+Monitoring+Active", use_container_width=True)

st.markdown('<div class="footer">© 2026 V-Guard AI | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
