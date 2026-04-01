import streamlit as st
import os
import pandas as pd

# 1. SETUP HALAMAN
st.set_page_config(page_title="V-Guard AI", layout="wide", page_icon="🛡️")

# Database & Auth
if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [{"ID": 101, "Bisnis": "Cafe Maju", "Paket": "MEDIUM", "Harga": 7500000, "Status": "🟢 AKTIF"}]
if 'admin_auth' not in st.session_state:
    st.session_state.admin_auth = False

WA_NUMBER = "628212190885"

# 2. CSS CUSTOM (KOTAK PAKET & FOOTER)
st.markdown(f"""
<style>
    .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; }}
    .product-card {{
        background-color: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 15px;
        padding: 20px; text-align: center; min-height: 380px; border-top: 8px solid #1E3A8A;
    }}
    .pkg-title {{ font-size: 24px; font-weight: bold; color: #1E3A8A; }}
    .pkg-price {{ font-size: 18px; font-weight: bold; color: #333; margin-bottom: 15px; }}
    .pkg-features {{ text-align: left; font-size: 13px; color: #555; min-height: 150px; }}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (SEMUA FOLDER)
with st.sidebar:
    if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    st.title("🛡️ V-Guard AI")
    menu = st.radio("Navigasi:", ["1. Profil Founder", "2. Visi & ROI", "3. Paket Unggulan", "4. Registrasi", "5. Admin Control", "6. Laporan Audit"])
    st.write("---")
    st.link_button("💬 Chat Support", f"https://wa.me/{WA_NUMBER}")

# --- LOGIKA MENU ---
if menu == "1. Profil Founder":
    st.header("Profil Kepemimpinan")
    st.write("""
    Bapak Erwin Sinaga adalah Senior Business Leader dengan pengalaman lebih dari 10 tahun di industri finansial nasional. 
    Beliau memiliki keahlian tajam dalam mengidentifikasi kebocoran aset yang sering luput dari pengawasan konvensional. 
    Sebagai arsitek V-Guard AI, beliau berkomitmen mendemokrasikan fungsi audit internal agar bisa diakses UMKM hingga korporasi. 
    Berdomisili di Tangerang, beliau menjembatani teknologi AI dengan kebutuhan riil lapangan untuk memastikan setiap rupiah 
    investasi klien terjaga aman. Visi beliau adalah menciptakan transparansi mutlak dalam setiap transaksi bisnis di Indonesia, 
    menjadikan V-Guard AI sebagai benteng pertahanan digital terpercaya bagi para pengusaha.
    """)

elif menu == "2. Visi & ROI":
    st.header("Visi & Analisis ROI")
    st.info("**Visi:** Menjadi benteng pertahanan digital utama di Indonesia.")
    st.success("**Misi:** Meminimalisir kebocoran transaksi hingga 0%.")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    st.metric("Potensi Hemat (7%)", f"Rp {omzet * 0.07:,.0f}")

elif menu == "3. Paket Unggulan":
    st.header("Layanan V-Guard AI")
    cols = st.columns(4)
    pkgs = [
        ("BASIC", "1.5jt", "● Monitor Harian<br>● Log Standar<br>● Dashboard Desktop"),
        ("SMART", "2.5jt", "● Fitur Basic+<br>● Deteksi Fraud AI<br>● Notif WA Real-time"),
        ("PRO", "5jt", "● Fitur Smart+<br>● Audit Mendalam<br>● Laporan PDF Otomatis"),
        ("ELITE", "Custom", "● Custom AI Integration<br>● Strategi Founder<br>● On-site Visit")
    ]
    for i, (name, price, feat) in enumerate(pkgs):
        with cols[i]:
            st.markdown(f'<div class="product-card"><div class="pkg-title">{name}</div><div class="pkg-price">Rp {price}/bln</div><div class="pkg-features">{feat}</div></div>', unsafe_allow_html=True)
            st.link_button("Pilih Paket", f"https://wa.me/{WA_NUMBER}?text=Saya%20pilih%20paket%20{name}")

elif menu == "4. Registrasi":
    st.header("Registrasi & Capture")
    with st.form("reg"):
        st.text_input("Nama Bisnis:")
        st.file_uploader("Upload Bukti/KTP", type=['jpg','png'])
        if st.form_submit_button("Kirim"): st.success("Data Terkirim!")

elif menu in ["5. Admin Control", "6. Laporan Audit"]:
    st.header("Akses Admin")
    pw = st.text_input("Sandi:", type="password")
    if pw == "w1nbju8282":
        st.dataframe(pd.DataFrame(st.session_state.db_nasabah), use_container_width=True)
    elif pw != "": st.error("Sandi Salah")

st.markdown('<div class="footer">© 2026 V-Guard AI | Secured by Erwin Sinaga</div>', unsafe_allow_html=True)
