import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI HALAMAN & STATE (LOCKED SOP)
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Usaha": "F&B", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": 102, "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Usaha": "Otomotif", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]
if 'admin_akses_terbuka' not in st.session_state:
    st.session_state.admin_akses_terbuka = False

WA_NUMBER = "628212190885"

def format_rp(angka):
    try:
        return f"Rp {float(angka):,.0f}".replace(",", ".")
    except:
        return str(angka)

# 2. CSS CUSTOM (STABIL)
st.markdown("""
<style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; }
    .product-card { 
        background-color: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 15px; 
        padding: 20px; text-align: center; min-height: 520px; border-top: 8px solid #1E3A8A; 
    }
    .pkg-title { font-size: 24px; font-weight: bold; color: #1E3A8A; margin-bottom: 10px; }
    .feature-text { text-align: left; font-size: 14px; line-height: 1.6; margin-top: 15px; color: #444; }
    .fraud-alarm { background-color: #ff4b4b; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; animation: blinker 1.5s linear infinite; margin-bottom: 20px; }
    @keyframes blinker { 50% { opacity: 0.5; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGASI (LOCK SOP 1-5)
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

# --- MENU 1: PROFIL (LOCKED) ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2.2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("""Bapak Erwin Sinaga adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel. Dengan visi besar untuk mendemokrasikan keamanan bisnis bagi semua kalangan, beliau terus berinovasi dalam mengembangkan instrumen pengawasan yang adaptif terhadap tantangan ekonomi masa depan.""")

# --- MENU 2: VISI, MISI & ROI (LOCKED) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("Strategi & Analisis Proteksi")
    st.info("**Visi:** Menjadi standar emas dalam teknologi pengawasan bisnis digital di Indonesia.")
    st.success("**Misi:** Menyediakan instrumen audit AI untuk mendeteksi indikasi kecurangan secara real-time.")
    st.write("---")
    omzet = st.number_input("Omzet Bulanan Bisnis (Rp):", value=100000000, step=1000000)
    pot_bocor = omzet * 0.07
    st.error(f"**Estimasi Kebocoran (7%):** {format_rp(pot_bocor)}")
    st.metric("Dana Berhasil Diselamatkan", format_rp(pot_bocor - 2500000), delta="ROI Positif")

# --- MENU 3: PAKET (LOCKED - LINK WA FOUNDER) ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("Layanan V-Guard AI")
    cols = st.columns(4)
    p_data = [("BASIC", "1.5jt"), ("SMART", "2.5jt"), ("PRO", "5jt"), ("ELITE", "Custom")]
    for i, (n, p) in enumerate(p_data):
        with cols[i]:
            st.markdown(f'<div class="product-card"><div class="pkg-title">{n}</div><p style="color: #d32f2f; font-size: 20px;"><b>Rp {p}</b></p>• Monitoring AI<br>• VCS System<br>• Weekly Audit</div>', unsafe_allow_html=True)
            st.link_button(f"Pesan {n}", f"https://wa.me/{WA_NUMBER}?text=Halo%20Pak%20Erwin,%20tertarik%20paket%20{n}")

# --- MENU 4: REGISTRASI (FIXED: BUTTON & JENIS USAHA) ---
elif menu == "4. 📝 Registrasi & Upload":
    st.header("Formulir Pendaftaran Klien")
    with st.form("reg_vguard_fixed"):
        col_a, col_b = st.columns(2)
        with col_a:
            st.text_input("Nama Pelanggan:")
            st.text_input("Nama Bisnis:")
        with col_b:
            st.text_input("Jenis Usaha (Contoh: Retail, F&B):")
            st.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO", "ELITE"])
        st.file_uploader("Upload KTP / Dokumen Pendukung:", type=['jpg', 'png', 'pdf'])
        submitted = st.form_submit_button("Kirim Pendaftaran Ke V-Guard")
        if submitted:
            st.success("Data Berhasil Dikirim. Tim kami akan segera menghubungi Bapak/Ibu.")

# --- MENU 5: AKSES TERBATAS (ALARM, RUGI LABA, AUDIT, CVV) ---
elif menu == "5. 🔐 Akses Terbatas":
    if not st.session_state.admin_akses_terbuka:
        cols_l = st.columns([1, 2, 1])
        with cols_l[1]:
            st.markdown("<h2 style='text-align: center;'>🔐 Login Admin</h2>", unsafe_allow_html=True)
            sandi = st.text_input("Sandi Keamanan:", type="password")
            if st.button("Buka Panel Admin"):
                if sandi == "w1nbju8282":
                    st.session_state.admin_akses_terbuka = True
                    st.rerun()
                else:
                    st.error("Akses Ditolak!")
    else:
        # HEADER & LOGOUT (SOP)
        h1, h2 = st.columns([5, 1])
        with h1: st.header("⚙️ Operasional V-Guard AI")
        with h2:
            if st.button("🔒 LOGOUT"):
                st.session_state.admin_akses_terbuka = False
                st.rerun()
        
        # ALARM FRAUD INDICATOR
        st.markdown('<div class="fraud-alarm">🚨 PERINGATAN: INDIKASI FRAUD TERDETEKSI PADA TITIK TRANSAKSI HARIAN</div>', unsafe_allow_html=True)
        
        t1, t2, t3, t4 = st.tabs(["📊 Database Klien", "📉 Laporan (Mingguan/Bulanan)", "📹 Monitoring CCTV/CVV", "🧾 Billing"])
        
        with t1:
            with st.expander("➕ Tambah Klien Baru"):
                with st.form("add_k"):
                    nk = st.text_input("Nama Pelanggan")
                    bk = st.text_input("Nama Bisnis")
                    uk = st.text_input("Jenis Usaha")
                    if st.form_submit_button("Simpan"):
                        st.session_state.db_nasabah.append({"ID": 103, "Waktu": "2026-04-01", "Pelanggan": nk, "Bisnis": bk, "Usaha": uk, "Paket": "Custom", "Harga": 0, "Status": "🟢 AKTIF"})
                        st.rerun()
            df = pd.DataFrame(st.session_state.db_nasabah)
            df['Harga'] = df['Harga'].apply(format_rp)
            st.table(df)

        with t2:
            st.subheader("Audit & Analisis Rugi Laba")
            sel_k = st.selectbox("Pilih Klien:", [d['Pelanggan'] for d in st.session_state.db_nasabah])
            c_l1, c_l2 = st.columns(2)
            with c_l1:
                st.info("**Laporan Mingguan**")
                st.write("- Penyelamatan Aset: Rp 750.000")
                st.write("- Status Audit: **Clear**")
            with c_l2:
                st.warning("**Audit Bulanan**")
                st.write("- Skor Integritas: 98%")
                st.write("- Indikasi Kerugian Bulanan: **0%**")
            st.button(f"Generate PDF Laporan untuk {sel_k}")

        with t3:
            st.subheader("📹 Jalur CVV (Client Visual Verification)")
            st.info("Sistem siap menerima transmisi data visual dari klien.")
            st.write("- Koneksi CCTV AI: **Stabil**")
            st.write("- Upload Data CVV Klien: **Aktif**")

        with t4:
            st.button("Kirim Invoice Ke WhatsApp")

st.markdown('<div class="footer">© 2026 V-Guard AI | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
