import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE (Siska Dihapus) ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "CEO", "Paket": "MASTER"}
    ]
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 3. CSS UNTUK TEKS SEJAJAR & TAMPILAN ---
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    .ceo-text { font-size: 14px; color: #64748b; font-weight: 500; }
    .ceo-card { background-color: white; padding: 30px; border-radius: 15px; border-left: 5px solid #0f172a; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .price-card { background-color: white; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; text-align: center; }
    .wa-btn { background-color: #25d366; color: white !important; padding: 10px; border-radius: 8px; text-decoration: none; display: block; text-align: center; font-weight: bold; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    
    # TEKS SEJAJAR: Nama - Founder - CEO
    st.markdown('<p class="ceo-text">Erwin Sinaga — Founder — CEO</p>', unsafe_allow_html=True)
    
    st.write("---")
    menu = [
        "1. Profil Kepemimpinan",
        "2. Visi Misi & ROI",
        "3. Daftar Harga",
        "4. Register Pelanggan",
        "5. Produk Layanan",
        "6. Dashboard Login",
        "7. Panel Admin"
    ]
    nav = st.radio("Navigasi:", menu)
    st.write("---")
    st.markdown('<a href="https://wa.me/628212190885" class="wa-btn">💬 Hubungi CEO</a>', unsafe_allow_html=True)

# --- 5. LOGIKA MENU ---

if nav == "1. Profil Kepemimpinan":
    st.header("Profil Kepemimpinan")
    with st.container():
        st.markdown('<div class="ceo-card">', unsafe_allow_html=True)
        # Teks 200 Kata Profesional
        st.write("""
        Bapak **Erwin Sinaga** adalah **Founder sekaligus CEO V-Guard AI** yang memiliki visi besar dalam mentransformasi keamanan aset digital di Indonesia. Dengan pengalaman kepemimpinan lebih dari sepuluh tahun sebagai eksekutif senior di sektor perbankan dan manajemen aset, beliau telah mengasah kemampuan strategis dalam mendeteksi dan memitigasi risiko finansial yang kompleks. Keahlian beliau tidak hanya terbatas pada manajerial, tetapi juga pada pemahaman mendalam mengenai celah operasional yang sering menjadi titik lemah dalam bisnis skala menengah hingga korporasi besar.

        Di bawah kepemimpinan beliau, V-Guard AI dikembangkan sebagai platform berbasis kecerdasan buatan yang mengedepankan transparansi mutlak dan akurasi data real-time. Bapak Erwin percaya bahwa di tengah persaingan pasar yang agresif, perlindungan terhadap integritas modal adalah kunci keberlanjutan usaha. Beliau dikenal sebagai figur yang disiplin, inovatif, dan memiliki dedikasi tinggi dalam membantu para pengusaha UMKM agar memiliki sistem pengawasan kelas dunia tanpa harus menanggung biaya operasional yang membebani. Berbasis di Tangerang, beliau terus memimpin ekspansi teknologi V-Guard AI untuk memastikan setiap mitra bisnis mendapatkan jaminan rasa aman melalui solusi audit digital yang cerdas, aplikatif, dan terpercaya bagi masa depan industri nasional.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

elif nav == "2. Visi Misi & ROI":
    st.header("Visi, Misi & Analisis ROI")
    col1, col2 = st.columns(2)
    with col1: st.info("**Visi:** Pelopor audit digital AI global.")
    with col2: st.success("**Misi:** Deteksi fraud & proteksi aset UMKM.")
    st.write("---")
    oz = st.number_input("Input Omzet Bulanan Bisnis (Rp):", value=100000000)
    rugi = oz * 0.07
    st.metric("Potensi Kerugian (7%)", f"Rp {rugi:,.0f}")
    st.metric("Aset Terselamatkan AI", f"Rp {rugi*0.9:,.0f}", delta="ROI Positif")

elif nav == "3. Daftar Harga":
    st.header("Price List V-Guard AI")
    st.write("Rincian biaya investasi perlindungan bisnis Anda.")
    data_harga = {
        "Paket": ["BASIC", "SMART", "PRO", "MASTER (Custom)"],
        "Biaya Langganan": ["Rp 1.500.000 / bln", "Rp 2.500.000 / bln", "Rp 5.000.000 / bln", "Hubungi CEO"],
        "Target": ["UMKM Kecil", "Bisnis Menengah", "Korporasi", "Multi-Nasional"]
    }
    st.table(pd.DataFrame(data_harga))

elif nav == "4. Register Pelanggan":
    st.header("Formulir Pendaftaran Pelanggan Baru")
    with st.form("reg_form"):
        st.text_input("Nama Lengkap Pemilik:")
        st.text_input("Nama Usaha / Perusahaan:")
        st.selectbox("Pilih Paket Langganan:", ["BASIC", "SMART", "PRO"])
        st.text_input("Nomor WhatsApp Aktif:")
        if st.form_submit_button("Daftar Sekarang"):
            st.success("Data pendaftaran telah terkirim ke sistem V-Guard AI.")

elif nav == "5. Produk Layanan":
    st.header("Layanan Unggulan & Biaya")
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.subheader("BASIC")
            st.write("**Rp 1.500.000 / bln**")
            st.caption("Monitor Dasar & Laporan Bulanan")
    with c2:
        with st.container(border=True):
            st.subheader("SMART")
            st.write("**Rp 2.500.000 / bln**")
            st.caption("Real-Time Monitor & VCS System")
    with c3:
        with st.container(border=True):
            st.subheader("PRO")
            st.write("**Rp 5.000.000 / bln**")
            st.caption("Forensik Full & Multi-Cabang")

elif nav == "6. Dashboard Login":
    st.header("Akses Dashboard Klien")
    if not st.session_state.cl_in:
        u = st.text_input("User ID:")
        p = st.text_input("Password:", type="password")
        if st.button("Masuk"):
            user = next((c for c in st.session_state.user_creds if c["User ID"] == u and c["Password"] == p), None)
            if user:
                st.session_state.cl_in = True
                st.session_state.current_user = user
                st.rerun()
            else: st.error("Akses Ditolak")
    else:
        st.info(f"Selamat Datang di Portal {st.session_state.current_user['Level']}")
        if st.button("Logout"):
            st.session_state.cl_in = False
            st.rerun()

elif nav == "7. Panel Admin":
    st.header("CEO Executive Panel")
    pwd = st.text_input("Sandi Otoritas:", type="password")
    if st.button("Lihat Data"):
        if pwd == "w1nbju8282":
            st.subheader("Database Pengguna (Aktif)")
            st.table(pd.DataFrame(st.session_state.user_creds))
        else: st.error("Sandi Salah")

st.write("---")
st.caption("© 2026 V-Guard AI Intelligence | Erwin Sinaga — Founder — CEO")
