import streamlit as st
import os
import pandas as pd
from datetime import datetime
import google.generativeai as genai

# 1. KONFIGURASI AI & HALAMAN
# Menggunakan API Key resmi Bapak
try:
    genai.configure(api_key="AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA")
    model = genai.GenerativeModel('gemini-pro')
    ai_koneksi = True
except:
    ai_koneksi = False

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Database Sesi untuk menyimpan data klien baru
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": 102, "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]

WA_NUMBER = "628212190885"

# 2. CSS UNTUK TAMPILAN PAKET & FOOTER
st.markdown(f"""
<style>
    .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; }}
    .product-card {{ background-color: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 15px; padding: 20px; text-align: center; min-height: 380px; border-top: 8px solid #1E3A8A; }}
    .pkg-title {{ font-size: 24px; font-weight: bold; color: #1E3A8A; }}
    .pkg-feat {{ text-align: left; font-size: 14px; margin-top: 15px; line-height: 1.6; color: #444; }}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (LOGO & NAVIGASI 1-5)
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🛡️ V-GUARD AI</h1>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
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

# --- MENU 1: PROFIL FOUNDER (150+ KATA Tanpa CEO/CSO) ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2.2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("""
        Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang telah mengabdikan lebih dari satu dekade karir profesionalnya untuk mendalami seluk-beluk operasional bisnis dan efisiensi organisasi di skala nasional. Dengan keahlian mendalam dalam navigasi industri finansial, beliau memiliki kemampuan analitis yang tajam dalam mengidentifikasi titik-titik rawan kebocoran aset yang seringkali luput dari pengawasan manajemen konvensional. Dedikasi beliau terhadap prinsip integritas dan akuntabilitas menjadi pilar utama di balik berdirinya V-Guard AI, sebuah platform yang mengintegrasikan kecerdasan buatan untuk memberikan perlindungan berlapis bagi para pengusaha di Indonesia.

        Beliau fokus pada misi besar untuk mendemokrasikan fungsi audit internal agar dapat diakses oleh semua skala bisnis, mulai dari UMKM hingga korporasi besar. Berdomisili di Tangerang, beliau aktif menjembatani kesenjangan antara teknologi digital dengan kebutuhan nyata di lapangan, memastikan bahwa setiap fitur yang dikembangkan dalam V-Guard AI mampu memberikan solusi konkret bagi efisiensi modal klien. Visi jangka panjang beliau adalah membangun ekosistem bisnis yang lebih sehat di Indonesia, di mana setiap rupiah investasi terjaga dengan aman dan setiap transaksi dapat dipertanggungjawabkan secara transparan, guna mendorong pertumbuhan ekonomi yang berkelanjutan bagi seluruh mitra yang bekerja sama dengannya melalui pendekatan berbasis teknologi yang adaptif dan solutif bagi tantangan masa depan.
        """)

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("Analisis Strategis & ROI")
    st.info("**Visi:** Menjadi benteng pertahanan digital utama bagi ekosistem bisnis Indonesia.")
    st.success("**Misi:** Meminimalisir kebocoran transaksi bisnis hingga titik nol melalui audit AI.")
    omzet = st.number_input("Input Omzet Bulanan Bisnis Anda (Rp):", value=100000000)
    st.metric("Potensi Efisiensi Biaya (7%)", f"Rp {omzet * 0.07:,.0f}", "Audit Real-time")

# --- MENU 3: PAKET UNGGULAN ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("Layanan Unggulan V-Guard AI")
    cols = st.columns(4)
    p_data = [
        ("BASIC", "1.5jt", "• Monitor Harian<br>• Log Standar Bisnis<br>• Dashboard Desktop"),
        ("SMART", "2.5jt", "• Deteksi Fraud AI Aktif<br>• Notif WA Real-time<br>• Analisis Mingguan"),
        ("PRO", "5jt", "• Audit Mendalam AI<br>• Laporan PDF Otomatis<br>• Support Prioritas 24/7"),
        ("ELITE", "Custom", "• Custom AI Integration<br>• Pendampingan Founder<br>• On-site Audit Berkala")
    ]
    for i, (n, p, f) in enumerate(p_data):
        with cols[i]:
            st.markdown(f'<div class="product-card"><div class="pkg-title">{n}</div><p><b>Rp {p}/bln</b></p><div class="pkg-feat">{f}</div></div>', unsafe_allow_html=True)
            st.link_button("Pilih Paket", f"https://wa.me/{WA_NUMBER}?text=Halo%20V-Guard,%20saya%20ingin%20paket%20{n}")

# --- MENU 4: REGISTRASI & UPLOAD FOTO ---
elif menu == "4. 📝 Registrasi & Upload":
    st.header("Pendaftaran & Verifikasi Dokumen")
    with st.form("form_reg"):
        st.text_input("Nama Lengkap Pemilik Bisnis:")
        st.text_input("Nama Bisnis / Perusahaan:")
        st.selectbox("Pilih Paket Layanan:", ["BASIC", "SMART", "PRO", "ELITE"])
        st.file_uploader("Unggah Foto KTP / Identitas (JPG/PNG):", type=['jpg', 'png'])
        st.file_uploader("Unggah Bukti Transfer Aktivasi (JPG/PNG):", type=['jpg', 'png'])
        if st.form_submit_button("Kirim Data Registrasi"):
            st.success("Terima kasih! Data dan dokumen Anda telah berhasil diunggah untuk verifikasi.")

# --- MENU 5: AKSES TERBATAS (ADMIN & LAPORAN AUDIT) ---
elif menu == "5. 🔐 Akses Terbatas":
    st.header("🔐 Area Otoritas V-Guard AI")
    sandi_masuk = st.text_input("Masukkan Sandi Keamanan:", type="password")
    
    if sandi_masuk == "w1nbju8282":
        st.success("Otoritas Diterima.")
        t_admin, t_audit = st.tabs(["📊 Kelola Klien & Akun", "📜 Laporan Audit Pakar AI"])
        
        with t_admin:
            st.subheader("Manajemen Akun Klien")
            with st.expander("➕ Tambah / Buat Akun Klien Baru"):
                with st.form("tambah_klien"):
                    new_p = st.text_input("Nama Pelanggan:")
                    new_b = st.text_input("Nama Bisnis:")
                    new_pkg = st.selectbox("Paket:", ["BASIC", "SMART", "PRO", "ELITE"])
                    new_prc = st.number_input("Harga (Rp):", value=1500000)
                    if st.form_submit_button("Simpan & Aktifkan Akun"):
                        st.session_state.db_nasabah.append({
                            "ID": len(st.session_state.db_nasabah)+101, 
                            "Waktu": str(datetime.now().date()), 
                            "Pelanggan": new_p, "Bisnis": new_b, 
                            "Paket": new_pkg, "Harga": new_prc, "Status": "🟢 AKTIF"
                        })
                        st.success("Akun Klien Baru Berhasil Dibuat!")
                        st.rerun()
            
            df_admin = pd.DataFrame(st.session_state.db_nasabah)
            st.dataframe(df_admin, use_container_width=True)
            st.download_button("📥 Ekspor Database (CSV)", df_admin.to_csv(index=False).encode('utf-8'), "Database_VGuard.csv", "text/csv")

        with t_audit:
            st.subheader("Hasil Audit Kecerdasan Buatan")
            st.table(pd.DataFrame(st.session_state.db_nasabah)[["ID", "Bisnis", "Status", "Pelanggan"]])
            if st.button("🤖 Jalankan Analisis Pakar Gemini"):
                if ai_koneksi:
                    with st.spinner("Gemini sedang menganalisis database Bapak..."):
                        prompt_ai = f"Berikan analisis risiko singkat dan 3 saran efisiensi untuk data klien ini: {st.session_state.db_nasabah}"
                        response = model.generate_content(prompt_ai)
                        st.info(f"**Hasil Analisis Gemini AI:**\n\n{response.text}")
                else:
                    st.error("Koneksi AI Terputus. Periksa API Key.")
                
    elif sandi_masuk != "":
        st.error("Sandi Salah. Akses ditolak.")

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
