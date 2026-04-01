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

# No WhatsApp Founder
WA_NUMBER = "628212190885"

# Teks Profil Founder (Minimal 150 Kata)
profil_txt = (
    "Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang telah mengabdikan lebih dari satu dekade karir profesionalnya "
    "untuk mendalami seluk-beluk operasional bisnis dan efisiensi organisasi di skala nasional. Dengan latar belakang yang kuat "
    "dalam navigasi industri finansial, beliau memiliki kemampuan analitis yang tajam dalam mengidentifikasi titik-titik rawan "
    "kebocoran aset yang seringkali luput dari pengawasan manajemen konvensional. Dedikasi beliau terhadap prinsip integritas "
    "dan akuntabilitas menjadi pilar utama di balik berdirinya V-Guard AI, sebuah platform yang mengintegrasikan kecerdasan buatan "
    "untuk memberikan perlindungan berlapis bagi para pengusaha di Indonesia.\n\n"
    "Sebagai arsitek utama V-Guard AI, Bapak Erwin Sinaga fokus pada misi besar untuk mendemokrasikan fungsi audit internal. "
    "Beliau percaya bahwa setiap entitas bisnis, mulai dari skala UMKM hingga korporasi besar, harus memiliki akses terhadap "
    "teknologi pengawasan yang real-time dan akurat. Berdomisili di Tangerang, beliau aktif menjembatani kesenjangan antara "
    "teknologi digital dengan kebutuhan nyata di lapangan, memastikan bahwa setiap fitur yang dikembangkan dalam V-Guard AI "
    "mampu memberikan solusi konkret bagi efisiensi modal klien. Visi jangka panjang beliau adalah membangun ekosistem bisnis "
    "yang lebih sehat di Indonesia, di mana setiap rupiah investasi terjaga dengan aman dan setiap transaksi dapat dipertanggungjawabkan "
    "secara transparan, guna mendorong pertumbuhan ekonomi yang berkelanjutan bagi seluruh mitra yang bekerja sama dengannya."
)

# 2. CSS CUSTOM (Tampilan Kartu Produk & Animasi)
st.markdown(f"""
<style>
    .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; background: #ffffff; text-align: center; padding: 10px; font-weight: bold; border-top: 1px solid #ddd; z-index: 999; }}
    .fraud-alert {{ background: #f8d7da; color: #721c24; padding: 15px; border-radius: 10px; border-left: 10px solid #dc3545; font-weight: bold; animation: blinker 1s linear infinite; margin-bottom: 10px; }}
    .piutang-box {{ background: #fff3cd; color: #856404; padding: 15px; border-radius: 10px; border-left: 10px solid #ffc107; margin-bottom: 10px; font-weight: bold; }}
    .product-card {{ background: #f9f9f9; padding: 25px; border-radius: 15px; border: 1px solid #e0e0e0; min-height: 450px; transition: 0.3s; }}
    .product-card:hover {{ border-color: #1E3A8A; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); }}
    .price-tag {{ font-size: 24px; font-weight: bold; color: #1E3A8A; margin-bottom: 15px; }}
    @keyframes blinker {{ 50% {{ opacity: 0.2; }} }}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi:", ["1. 👤 Profil Founder", "2. 🎯 Visi, Misi & ROI", "3. 📦 Produk Unggulan", "4. 📝 Registrasi & Capture", "5. 🔐 Admin Control Center", "6. 📜 Laporan Audit Klien"])
    st.write("---")
    st.link_button("💬 Hubungi Bapak Erwin", f"https://wa.me/{WA_NUMBER}")

# --- MENU 1: PROFIL ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
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
    st.metric("Potensi Penyelamatan Fraud", f"Rp {save_val:,.0f}", "Hemat 7% Per Bulan")

# --- MENU 3: PRODUK UNGGULAN (TAMPILAN BARU) ---
elif menu == "3. 📦 Produk Unggulan":
    st.header("Paket Layanan V-Guard AI")
    p1, p2, p3, p4 = st.columns(4)
    
    with p1:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.subheader("BASIC")
        st.markdown('<p class="price-tag">Rp 1.5jt<small>/bln</small></p>', unsafe_allow_html=True)
        st.write("* Monitoring Transaksi Harian\n* Log Aktivitas Standar\n* Dashboard Desktop\n* Support Email")
        st.link_button("Pilih Paket", f"https://wa.me/{WA_NUMBER}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20BASIC")
        st.markdown('</div>', unsafe_allow_html=True)

    with p2:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.subheader("SMART")
        st.markdown('<p class="price-tag">Rp 2.5jt<small>/bln</small></p>', unsafe_allow_html=True)
        st.write("* Semua Fitur Basic\n* Deteksi Fraud AI Aktif\n* Notifikasi WA Real-time\n* Analisis Tren Mingguan")
        st.link_button("Pilih Paket", f"https://wa.me/{WA_NUMBER}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20SMART")
        st.markdown('</div>', unsafe_allow_html=True)

    with p3:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.subheader("PRO")
        st.markdown('<p class="price-tag">Rp 5jt<small>/bln</small></p>', unsafe_allow_html=True)
        st.write("* Semua Fitur Smart\n* Audit Finansial Mendalam\n* Laporan PDF Otomatis\n* Priority Support 24/7")
        st.link_button("Pilih Paket", f"https://wa.me/{WA_NUMBER}?text=Halo%20Pak%20Erwin,%20saya%20tertarik%20paket%20PRO")
        st.markdown('</div>', unsafe_allow_html=True)

    with p4:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.subheader("ELITE")
        st.markdown('<p class="price-tag">Hubungi Kami</p>', unsafe_allow_html=True)
        st.write("* Custom AI Integration\n* Pendampingan Strategis Founder\n* On-site Audit Visit\n* Multi-Business Control")
        st.link_button("Hubungi Founder", f"https://wa.me/{WA_NUMBER}?text=Halo%20Pak%20Erwin,%20saya%20ingin%20konsultasi%20paket%20ELITE")
        st.markdown('</div>', unsafe_allow_html=True)

# --- MENU 4: REGISTRASI ---
elif menu == "4. 📝 Registrasi & Capture":
    st.header("Registrasi & Capture Mandiri")
    with st.form("reg_form"):
        name = st.text_input("Nama PIC:")
        bisnis = st.text_input("Nama Bisnis:")
        st.file_uploader("Upload Capture Bukti Bayar / KTP", type=['jpg','png','jpeg'])
        if st.form_submit_button("Kirim Pendaftaran"):
            msg = f"Halo Pak Erwin, saya {name} dari {bisnis} sudah melakukan registrasi di sistem."
            st.success("Data diterima! Silakan klik tombol di bawah untuk konfirmasi ke WhatsApp.")
            st.link_button("Konfirmasi via WA", f"https://wa.me/{WA_NUMBER}?text={urllib.parse.quote(msg)}")

# --- MENU 5: ADMIN CONTROL CENTER ---
elif menu == "5. 🔐 Admin Control Center":
    st.header("🔐 Admin Dashboard")
    if not st.session_state.admin_auth:
        pw_input = st.text_input("Sandi Otoritas Admin:", type="password")
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
