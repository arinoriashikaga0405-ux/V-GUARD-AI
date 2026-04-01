import streamlit as st
import os
import pandas as pd
from datetime import datetime
import google.generativeai as genai

# 1. KONFIGURASI AI
try:
    genai.configure(api_key="AIzaSyAcEAe31MPleCbfJCXOn51I_DmdCU0tKrA")
    model = genai.GenerativeModel('gemini-pro')
    ai_ok = True
except:
    ai_ok = False

st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Database Sesi & Login Session
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": 102, "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]
if 'admin_akses_terbuka' not in st.session_state:
    st.session_state.admin_akses_terbuka = False

WA_NUMBER = "628212190885"

# 2. CSS CUSTOM (STABIL)
st.markdown(f"""
<style>
    .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; }}
    .product-card {{ background-color: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 15px; padding: 20px; text-align: center; min-height: 380px; border-top: 8px solid #1E3A8A; }}
    .pkg-title {{ font-size: 24px; font-weight: bold; color: #1E3A8A; }}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGASI (DIPERTAHANKAN)
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

# --- MENU 1: PROFIL FOUNDER (KEMBALI KE TEKS LENGKAP) ---
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

# --- MENU 2: VISI, MISI & ROI (STABIL) ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("Analisis Strategis")
    st.info("**Visi:** Menjadi benteng pertahanan digital utama bagi ekosistem bisnis Indonesia.")
    st.success("**Misi:** Meminimalisir kebocoran transaksi bisnis hingga titik nol melalui audit AI.")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    st.metric("Potensi Efisiensi (7%)", f"Rp {omzet * 0.07:,.0f}")

# --- MENU 3: PAKET UNGGULAN (STABIL) ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("Layanan V-Guard AI")
    cols = st.columns(4)
    p_data = [
        ("BASIC", "1.5jt", "• Monitor Harian<br>• Log Standar Bisnis"), 
        ("SMART", "2.5jt", "• Fraud AI Aktif<br>• Notif WA Real-time"), 
        ("PRO", "5jt", "• Audit Mendalam AI<br>• Laporan PDF Otomatis"), 
        ("ELITE", "Custom", "• On-site Audit<br>• Pendampingan Founder")
    ]
    for i, (n, p, f) in enumerate(p_data):
        with cols[i]:
            st.markdown(f'<div class="product-card"><div class="pkg-title">{n}</div><p><b>Rp {p}</b></p><p>{f}</p></div>', unsafe_allow_html=True)
            st.link_button("Pilih", f"https://wa.me/{WA_NUMBER}?text=Paket%20{n}")

# --- MENU 4: REGISTRASI & UPLOAD (STABIL) ---
elif menu == "4. 📝 Registrasi & Upload":
    st.header("Pendaftaran Klien")
    with st.form("reg"):
        st.text_input("Nama Pemilik:")
        st.text_input("Nama Bisnis:")
        st.file_uploader("Upload KTP (JPG/PNG):", type=['jpg', 'png'])
        st.file_uploader("Upload Bukti Transfer (JPG/PNG):", type=['jpg', 'png'])
        if st.form_submit_button("Kirim Data"): st.success("Data Berhasil Terunggah!")

# --- MENU 5: AKSES TERBATAS (DENGAN LOGOUT POJOK KANAN ATAS) ---
elif menu == "5. 🔐 Akses Terbatas":
    if not st.session_state.admin_akses_terbuka:
        st.markdown("<h2 style='text-align: center;'>🔐 Verifikasi Otoritas Admin</h2>", unsafe_allow_html=True)
        cols_l = st.columns([1, 2, 1])
        with cols_l[1]:
            sandi = st.text_input("Masukkan Sandi Keamanan:", type="password", key="sandi_admin")
            if st.button("Buka Panel Admin"):
                if sandi == "w1nbju8282":
                    st.session_state.admin_akses_terbuka = True
                    st.rerun()
                else:
                    st.error("Sandi Salah!")
    else:
        # LOGOUT DI POJOK KANAN ATAS
        head_col1, head_col2 = st.columns([5, 1])
        with head_col1:
            st.header("⚙️ Control Center & Audit")
        with head_col2:
            if st.button("🔒 LOGOUT"):
                st.session_state.admin_akses_terbuka = False
                st.rerun()
        
        st.write("---") 
        tab_klien, tab_ai = st.tabs(["📊 Kelola Akun Klien", "🤖 Analisis Strategis Gemini"])
        
        with tab_klien:
            with st.expander("➕ Buat Akun Klien Baru secara Manual"):
                with st.form("add_manual"):
                    nama_c = st.text_input("Nama Pelanggan:")
                    bisnis_c = st.text_input("Nama Bisnis:")
                    if st.form_submit_button("Simpan Akun"):
                        st.session_state.db_nasabah.append({"ID": len(st.session_state.db_nasabah)+101, "Waktu": str(datetime.now().date()), "Pelanggan": nama_c, "Bisnis": bisnis_c, "Paket": "ADMIN", "Harga": 1500000, "Status": "🟢 AKTIF"})
                        st.rerun()
            st.dataframe(pd.DataFrame(st.session_state.db_nasabah), use_container_width=True)

        with tab_ai:
            st.table(pd.DataFrame(st.session_state.db_nasabah)[["ID", "Bisnis", "Status"]])
            if st.button("🤖 Jalankan Analisis Gemini AI"):
                if ai_ok:
                    with st.spinner("Menganalisis..."):
                        res = model.generate_content(f"Berikan analisis risiko singkat: {st.session_state.db_nasabah}")
                        st.info(res.text)
                else: st.error("AI Belum Terhubung")

st.markdown('<div class="footer">© 2026 V-Guard AI | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
