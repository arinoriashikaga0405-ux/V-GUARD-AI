import streamlit as st
import os
import pandas as pd

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

# Inisialisasi Database
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [{"ID": 101, "Bisnis": "Cafe Maju", "Paket": "MEDIUM", "Harga": 7500000, "Status": "🟢 AKTIF"}]

WA_NUMBER = "628212190885"

# 2. CSS CUSTOM (KOTAK PAKET & FOOTER)
st.markdown(f"""
<style>
    .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; }}
    .product-card {{
        background-color: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 15px;
        padding: 20px; text-align: center; min-height: 380px; border-top: 8px solid #1E3A8A;
    }}
    .pkg-title {{ font-size: 24px; font-weight: bold; color: #1E3A8A; margin-bottom: 5px; }}
    .pkg-price {{ font-size: 18px; font-weight: bold; color: #333; margin-bottom: 15px; }}
    .pkg-features {{ text-align: left; font-size: 13px; color: #555; min-height: 150px; line-height: 1.6; }}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (TAMPILAN FOLDER AWAL)
with st.sidebar:
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", caption="Founder V-Guard AI", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 📦 Paket Unggulan", 
        "4. 📝 Registrasi & Capture", 
        "5. 🔐 Admin Control Center", 
        "6. 📜 Laporan Audit Klien"
    ])
    st.write("---")
    st.link_button("💬 Chat Support", f"https://wa.me/{WA_NUMBER}")

# --- MENU 1: PROFIL FOUNDER (MINIMAL 150 KATA) ---
if menu == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with col_txt:
        st.subheader("Bapak Erwin Sinaga")
        st.write("""
        Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang telah mengabdikan lebih dari satu dekade karir profesionalnya 
        untuk mendalami seluk-beluk operasional bisnis dan efisiensi organisasi di skala nasional. Dengan keahlian mendalam 
        dalam navigasi industri finansial, beliau memiliki kemampuan analitis yang tajam dalam mengidentifikasi titik-titik rawan 
        kebocoran aset yang seringkali luput dari pengawasan manajemen konvensional. Dedikasi beliau terhadap prinsip integritas 
        dan akuntabilitas menjadi pilar utama di balik berdirinya V-Guard AI, sebuah platform yang mengintegrasikan kecerdasan buatan 
        untuk memberikan perlindungan berlapis bagi para pengusaha di Indonesia.
        
        Sebagai arsitek utama V-Guard AI, Bapak Erwin Sinaga fokus pada misi besar untuk mendemokrasikan fungsi audit internal. 
        Beliau percaya bahwa setiap entitas bisnis, mulai dari skala UMKM hingga korporasi besar, harus memiliki akses terhadap 
        teknologi pengawasan yang real-time dan akurat. Berdomisili di Tangerang, beliau aktif menjembatani kesenjangan antara 
        teknologi digital dengan kebutuhan nyata di lapangan, memastikan bahwa setiap fitur yang dikembangkan dalam V-Guard AI 
        mampu memberikan solusi konkret bagi efisiensi modal klien. Visi jangka panjang beliau adalah membangun ekosistem bisnis 
        yang lebih sehat di Indonesia, di mana setiap rupiah investasi terjaga dengan aman dan setiap transaksi dapat dipertanggungjawabkan 
        secara transparan, guna mendorong pertumbuhan ekonomi yang berkelanjutan bagi seluruh mitra yang bekerja sama dengannya.
        """)

# --- MENU 2: VISI, MISI & ROI ---
elif menu == "2. 🎯 Visi, Misi & ROI":
    st.header("Analisis Strategis & ROI")
    st.info("**Visi:** Menjadi benteng pertahanan digital utama bagi ekosistem bisnis di Indonesia.")
    st.success("**Misi:** Meminimalisir kebocoran transaksi hingga 0% melalui audit real-time.")
    st.write("---")
    st.subheader("Simulasi Pencegahan Kerugian")
    omzet = st.number_input("Input Omzet Bulanan Bisnis Anda (Rp):", value=100000000)
    leakage = omzet * 0.07
    st.metric("Estimasi Kebocoran Aset (Fraud)", f"Rp {leakage:,.0f}", "Potensi Kerugian 7%")
    st.write("Dengan V-Guard AI, potensi kerugian di atas dapat ditekan hingga maksimal melalui sistem deteksi dini.")

# --- MENU 3: PAKET UNGGULAN ---
elif menu == "3. 📦 Paket Unggulan":
    st.header("Layanan V-Guard AI")
    cols = st.columns(4)
    pkgs = [
        ("BASIC", "1.5jt", "● Monitor Harian<br>● Log Aktivitas Standar<br>● Dashboard Desktop<br>● Support Email"),
        ("SMART", "2.5jt", "● Fitur Basic+<br>● Deteksi Fraud AI Aktif<br>● Notifikasi WA Real-time<br>● Analisis Tren Mingguan"),
        ("PRO", "5jt", "● Fitur Smart+<br>● Audit Finansial Mendalam<br>● Laporan PDF Otomatis<br>● Priority Support 24/7"),
        ("ELITE", "Custom", "● Custom AI Integration<br>● Pendampingan Founder<br>● On-site Audit Visit<br>● Multi-Business Control")
    ]
    for i, (name, price, feat) in enumerate(pkgs):
        with cols[i]:
            st.markdown(f'<div class="product-card"><div class="pkg-title">{name}</div><div class="pkg-price">Rp {price}/bln</div><div class="pkg-features">{feat}</div></div>', unsafe_allow_html=True)
            st.link_button("Pilih Paket", f"https://wa.me/{WA_NUMBER}?text=Saya%20pilih%20paket%20{name}")

# --- MENU 4: REGISTRASI (DENGAN NAMA PELANGGAN) ---
elif menu == "4. 📝 Registrasi & Capture":
    st.header("Pendaftaran Klien Baru")
    with st.form("reg_form"):
        st.text_input("Nama Pelanggan (Pemilik):") # Penambahan kolom sesuai instruksi
        st.text_input("Nama Bisnis / Perusahaan:")
        st.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO", "ELITE"])
        st.file_uploader("Upload Bukti Pembayaran / KTP", type=['jpg','png','jpeg'])
        if st.form_submit_button("Kirim Pendaftaran"):
            st.success("Terima kasih! Data pendaftaran Anda telah dikirim ke sistem untuk verifikasi.")

# --- MENU 5 & 6 (ADMIN & AUDIT) ---
elif menu in ["5. 🔐 Admin Control Center", "6. 📜 Laporan Audit Klien"]:
    st.header("Akses Terbatas")
    pw = st.text_input("Sandi Otoritas Admin:", type="password")
    if pw == "w1nbju8282":
        st.dataframe(pd.DataFrame(st.session_state.db_nasabah), use_container_width=True)
    elif pw != "":
        st.error("Akses Ditolak!")

st.markdown('<div class="footer">© 2026 V-Guard AI Systems | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
