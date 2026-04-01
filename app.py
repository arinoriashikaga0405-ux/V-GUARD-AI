import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database dengan struktur kolom yang konsisten (Pencegahan KeyError)
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

# 2. CSS CUSTOM (STANDARD VISUAL V-GUARD)
st.markdown("""
<style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; font-size: 12px; }
    .fraud-alarm { background-color: #ff4b4b; color: white; padding: 12px; border-radius: 8px; text-align: center; font-weight: bold; animation: blinker 2s linear infinite; margin-bottom: 20px; }
    @keyframes blinker { 50% { opacity: 0.7; } }
    .audit-card { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); padding: 20px; border-radius: 10px; border-left: 8px solid #1E3A8A; color: #333; }
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
    st.link_button("💬 Chat Support (WhatsApp)", f"https://wa.me/{WA_NUMBER}")

# --- MENU 1: PROFIL FOUNDER (LOCKED) ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2.2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("""Bapak Erwin Sinaga adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan. Beliau percaya bahwa ekosistem bisnis yang sehat hanya dapat tercipta melalui sistem yang akuntabel. Dengan visi besar untuk mendemokrasikan keamanan bisnis bagi semua kalangan, beliau terus berinovasi dalam mengembangkan instrumen pengawasan yang adaptif terhadap tantangan ekonomi masa depan.""")

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("Strategi & Analisis Proteksi")
    st.info("**Visi:** Menjadi standar emas dalam teknologi pengawasan bisnis digital di Indonesia.")
    st.success("**Misi:** Menyediakan instrumen audit AI untuk mendeteksi indikasi kecurangan secara real-time.")
    st.write("---")
    omzet = st.number_input("Omzet Bulanan Bisnis (Rp):", value=100000000, step=1000000)
    pot_bocor = omzet * 0.07
    st.error(f"Estimasi Kebocoran (7%): {format_rp(pot_bocor)}")
    st.markdown(f"### Dana Berhasil Diselamatkan \n ## {format_rp(pot_bocor - 2500000)}")

# --- MENU 3: PAKET UNGGULAN ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("Layanan V-Guard AI")
    pkts = [("BASIC", "1.5jt"), ("SMART", "2.5jt"), ("PRO", "5jt"), ("ELITE", "Custom")]
    cols = st.columns(4)
    for i, (n, p) in enumerate(pkts):
        with cols[i]:
            st.info(f"**{n}**\n\n**Rp {p}**")
            st.write("• Monitoring AI\n• VCS System\n• Weekly Audit")
            st.link_button(f"Pesan {n}", f"https://wa.me/{WA_NUMBER}")

# --- MENU 4: REGISTRASI & UPLOAD (LOCKED) ---
elif menu == "4. 📝 Registrasi & Upload":
    st.header("Formulir Pendaftaran Klien")
    with st.form("form_reg_vguard"):
        c1, c2 = st.columns(2)
        with c1:
            nama_p = st.text_input("Nama Pelanggan:")
            nama_b = st.text_input("Nama Bisnis:")
        with c2:
            usaha_p = st.text_input("Jenis Usaha (Retail, F&B, dll):")
            paket_p = st.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO", "ELITE"])
        st.file_uploader("Upload Dokumen Pendukung:", type=['jpg','png','pdf'])
        submit = st.form_submit_button("Kirim Pendaftaran Ke V-Guard")
        if submit:
            st.success("Data Berhasil Terkirim!")

# --- MENU 5: AKSES TERBATAS (FIXED KEYERROR) ---
elif menu == "5. 🔐 Akses Terbatas":
    if not st.session_state.admin_akses_terbuka:
        st.markdown("<h2 style='text-align: center;'>🔐 Login Admin</h2>", unsafe_allow_html=True)
        pwd = st.text_input("Sandi Keamanan:", type="password")
        if st.button("Masuk"):
            if pwd == ADMIN_PASSWORD:
                st.session_state.admin_akses_terbuka = True
                st.rerun()
            else:
                st.error("Sandi Salah!")
    else:
        h1, h2 = st.columns([5, 1])
        with h1: st.header("Panel Operasional V-Guard AI")
        with h2:
            if st.button("🔒 LOGOUT"):
                st.session_state.admin_akses_terbuka = False
                st.rerun()

        st.markdown('<div class="fraud-alarm">🚨 PERINGATAN: INDIKASI FRAUD TERDETEKSI PADA TITIK TRANSAKSI HARIAN</div>', unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Database Klien", "📉 Audit Google Studio", "📹 Monitoring CCTV/CVV", "🧾 Billing"])
        
        with tab1:
            with st.expander("+ Tambah Klien Baru"):
                with st.form("tambah_klien_fix"):
                    nk = st.text_input("Nama")
                    bk = st.text_input("Bisnis")
                    uk = st.text_input("Usaha")
                    pk = st.selectbox("Paket", ["BASIC", "SMART", "PRO"])
                    hk = st.number_input("Harga Paket (Angka)", value=1500000)
                    if st.form_submit_button("Simpan"):
                        new_data = {
                            "ID": 103, "Waktu": str(datetime.now().date()), 
                            "Pelanggan": nk, "Bisnis": bk, "Usaha": uk, 
                            "Paket": pk, "Harga": hk, "Status": "🟢 AKTIF"
                        }
                        st.session_state.db_nasabah.append(new_data)
                        st.rerun()
            
            # PROTEKSI KEYERROR: Pastikan DataFrame diformat dengan aman
            df = pd.DataFrame(st.session_state.db_nasabah)
            if 'Harga' in df.columns:
                df_display = df.copy()
                df_display['Harga'] = df_display['Harga'].apply(format_rp)
                st.table(df_display)
            else:
                st.table(df)

        with tab2:
            st.subheader("Audit Google Studio Gemini")
            st.markdown('<div class="audit-card"><b>Integrity Score: 98.5%</b><br>Audit AI Berjalan Normal</div>', unsafe_allow_html=True)
            st.line_chart([20, 40, 30, 60, 50])

        with tab3:
            st.info("Koneksi CVV (Client Visual Verification): Aktif")

        with tab4:
            st.button("Generate Billing")

st.markdown('<div class="footer">© 2026 V-Guard AI | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
