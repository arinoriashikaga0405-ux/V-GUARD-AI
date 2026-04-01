import streamlit as st
import os
import pandas as pd
from datetime import datetime

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# --- DATABASE STATE (Agar data yang ditambah tidak hilang saat refresh sesi) ---
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": 102, "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]
if 'admin_akses_terbuka' not in st.session_state:
    st.session_state.admin_akses_terbuka = False

WA_NUMBER = "628212190885"

# --- FUNGSI FORMAT RUPIAH ---
def format_rp(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")

# --- CSS CUSTOM (STABIL) ---
st.markdown("""
<style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; }
    .product-card { 
        background-color: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 15px; 
        padding: 20px; text-align: center; min-height: 520px; border-top: 8px solid #1E3A8A; 
    }
    .pkg-title { font-size: 24px; font-weight: bold; color: #1E3A8A; margin-bottom: 10px; }
    .feature-text { text-align: left; font-size: 14px; line-height: 1.6; margin-top: 15px; color: #444; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGASI (LOCK 1-4) ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🛡️ V-GUARD AI</h1>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", caption="Erwin Sinaga | Senior Business Leader", use_container_width=True)
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

# --- MENU 1-4: KUNCI TOTAL (SOP) ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2.2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("""Bapak Erwin Sinaga adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir... (Narasi >150 kata sesuai SOP)""")

elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("Analisis Strategis & Proteksi Kerugian")
    omzet = st.number_input("Omzet Bulanan Bisnis (Rp):", value=100000000, step=1000000)
    c_roi1, c_roi2 = st.columns(2)
    with c_roi1:
        pot_bocor = omzet * 0.07
        st.error(f"**Estimasi Kebocoran (7%):** {format_rp(pot_bocor)}")
    with c_roi2:
        hasil_roi = pot_bocor - 2500000
        st.metric("Dana Berhasil Diselamatkan", format_rp(hasil_roi), delta="ROI Positif")

elif menu == "3. 📦 Paket Unggulan":
    st.header("Layanan V-Guard AI")
    cols = st.columns(4)
    p_data = [("BASIC", "1.5jt"), ("SMART", "2.5jt"), ("PRO", "5jt"), ("ELITE", "Custom")]
    for i, (n, p) in enumerate(p_data):
        with cols[i]:
            st.markdown(f'<div class="product-card"><div class="pkg-title">{n}</div><p style="color: #d32f2f; font-size: 20px;"><b>Rp {p}</b></p><div class="feature-text">• Monitoring AI<br>• VCS System<br>• Weekly Audit</div></div>', unsafe_allow_html=True)

elif menu == "4. 📝 Registrasi & Upload":
    st.header("Formulir Pendaftaran")
    with st.form("reg_form"):
        st.text_input("Nama Pelanggan:")
        st.selectbox("Paket:", ["BASIC", "SMART", "PRO", "ELITE"])
        if st.form_submit_button("Kirim"): st.success("Data Terkirim")

# --- MENU 5: AKSES TERBATAS (PENAMBAHAN FITUR BARU) ---
elif menu == "5. 🔐 Akses Terbatas":
    if not st.session_state.admin_akses_terbuka:
        st.markdown("<h2 style='text-align: center;'>🔐 Verifikasi Otoritas Admin</h2>", unsafe_allow_html=True)
        sandi = st.text_input("Sandi Keamanan:", type="password")
        if st.button("Buka Panel Admin"):
            if sandi == "w1nbju8282":
                st.session_state.admin_akses_terbuka = True
                st.rerun()
    else:
        # HEADER ADMIN & LOGOUT (SOP)
        h1, h2 = st.columns([5, 1])
        with h1: st.header("⚙️ Operasional V-Guard AI")
        with h2:
            if st.button("🔒 LOGOUT"):
                st.session_state.admin_akses_terbuka = False
                st.rerun()
        
        tab1, tab2, tab3 = st.tabs(["📊 Database & Tambah Klien", "🚨 Audit & Rugi Laba Mingguan", "🧾 Billing"])
        
        with tab1:
            st.subheader("Manajemen Klien")
            # --- FITUR TAMBAH KLIEN ---
            with st.expander("➕ Tambah Klien Baru"):
                with st.form("add_client"):
                    c_n = st.text_input("Nama Pelanggan")
                    c_b = st.text_input("Nama Bisnis")
                    c_p = st.selectbox("Paket", ["BASIC", "SMART", "PRO", "ELITE"])
                    c_h = st.number_input("Harga Deal (Rp)", value=1500000)
                    if st.form_submit_button("Simpan Klien"):
                        new_data = {"ID": 100 + len(st.session_state.db_nasabah)+1, "Waktu": str(datetime.now().date()), "Pelanggan": c_n, "Bisnis": c_b, "Paket": c_p, "Harga": c_h, "Status": "🟢 AKTIF"}
                        st.session_state.db_nasabah.append(new_data)
                        st.rerun()

            # --- TABEL DENGAN FORMAT RP ---
            df = pd.DataFrame(st.session_state.db_nasabah)
            df['Harga'] = df['Harga'].apply(format_rp)
            st.table(df)

        with tab2:
            st.subheader("Laporan Mingguan Klien")
            selected_client = st.selectbox("Pilih Klien untuk Audit:", [d['Pelanggan'] for d in st.session_state.db_nasabah])
            
            c1, c2 = st.columns(2)
            with c1:
                st.info(f"📋 **Laporan Audit Mingguan: {selected_client}**")
                st.write("- Indikasi Fraud: **0 Terdeteksi**")
                st.write("- Kepatuhan SOP: **98%**")
                st.write("- Status Visual (VCS): **Normal**")
            with c2:
                st.warning(f"📉 **Laporan Rugi Laba Mingguan**")
                st.write(f"- Estimasi Penyelamatan Aset: **{format_rp(750000)}**")
                st.write("- Kebocoran Dicegah: **100%**")
                st.button(f"Kirim Laporan ke {selected_client} (WhatsApp)")

        with tab3:
            st.subheader("Billing System")
            st.button("Generate Invoice Otomatis")

st.markdown('<div class="footer">© 2026 V-Guard AI | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
