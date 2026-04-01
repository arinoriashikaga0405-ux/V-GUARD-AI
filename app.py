import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [{"User ID": "admin", "Password": "w1nbju8282"}]
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    
    # Menu Navigasi Tanpa Angka
    menu = [
        "Profil Kepemimpinan & ROI", 
        "Daftar Harga Modern", 
        "Register Pelanggan", 
        "Dashboard Login", 
        "Admin Panel"
    ]
    nav = st.radio("Navigasi Utama:", menu)
    st.write("---")
    st.markdown('<a href="https://wa.me/628212190885" target="_blank" style="background-color:#25d366;color:white;padding:10px;border-radius:8px;text-decoration:none;display:block;text-align:center;font-weight:bold;">💬 Hubungi Admin</a>', unsafe_allow_html=True)

# --- 4. LOGIKA MENU ---

if nav == "Profil Kepemimpinan & ROI":
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga — Founder")
    with col2:
        with st.container(border=True):
            # Teks 200 Kata Profesional
            st.write("""
            Bapak **Erwin Sinaga** adalah sosok **Founder** di balik **V-Guard AI Intelligence**, sebuah platform inovatif yang lahir dari dedikasi mendalam terhadap keamanan aset dan transparansi bisnis. Beliau memiliki rekam jejak profesional yang prestisius selama lebih dari satu dekade, menempati berbagai posisi strategis dan manajerial senior di industri perbankan serta manajemen aset nasional. Pengalaman panjang tersebut telah membentuk ketajaman analitis beliau dalam mengidentifikasi berbagai pola risiko finansial dan celah operasional yang sering kali luput dari sistem pengawasan konvensional.

            Di bawah visi kepemimpinannya, V-Guard AI dikembangkan bukan sekadar sebagai alat audit, melainkan sebagai benteng pertahanan digital bagi para pengusaha. Beliau sangat memahami bahwa integritas data dan perlindungan modal adalah fondasi utama bagi keberlanjutan bisnis di era digital yang penuh tantangan. Berdomisili di Tangerang, beliau aktif menjembatani kebutuhan dunia usaha dengan solusi teknologi kecerdasan buatan yang aplikatif dan efisien. Fokus utama beliau adalah memberikan ketenangan pikiran bagi pemilik usaha melalui sistem audit real-time yang mampu meminimalisir potensi kerugian secara signifikan. Bapak Erwin dikenal sebagai pemimpin yang visioner, disiplin, dan memiliki komitmen tanpa kompromi dalam membantu UMKM hingga korporasi besar mencapai standar tata kelola bisnis yang bersih, aman, dan berkelanjutan.
            """)
    
    st.write("---")
    st.subheader("Strategi Visi, Misi & ROI")
    v1, v2 = st.columns(2)
    with v1: st.info("**Visi:** Pelopor audit digital AI global.")
    with v2: st.success("**Misi:** Proteksi aset UMKM & Fraud Detection.")
    
    oz = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    rugi = oz * 0.07
    st.metric("Potensi Rugi (7%)", f"Rp {rugi:,.0f}")
    st.metric("Aset Aman AI", f"Rp {rugi*0.9:,.0f}")

elif nav == "Daftar Harga Modern":
    st.header("Price List V-Guard AI")
    wa_adm = "https://wa.me/628212190885?text=Min,%20Paket%20"
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.subheader("BASIC")
            st.write("### Rp 1.5jt / bln")
            st.write("✓ Monitor Dasar\n\n✓ Laporan Bulanan")
            st.link_button("Pesan BASIC", wa_adm + "BASIC")
    with c2:
        with st.container(border=True):
            st.subheader("SMART")
            st.write("### Rp 2.5jt / bln")
            st.write("✓ Real-Time Monitor\n\n✓ VCS Integrasi")
            st.link_button("Pesan SMART", wa_adm + "SMART")
    with c3:
        with st.container(border=True):
            st.subheader("MASTER")
            st.write("### PRO / Custom")
            st.write("✓ Full Audit AI\n\n✓ Multi-Cabang")
            st.link_button("Hubungi Admin", wa_adm + "MASTER")

elif nav == "Register Pelanggan":
    st.header("Pendaftaran Pelanggan")
    with st.form("f_reg"):
        st.text_input("Nama Pemilik:")
        st.text_input("Nama Usaha:")
        st.selectbox("Pilih Paket & Harga:", ["BASIC (1.5jt)", "SMART (2.5jt)", "MASTER"])
        st.file_uploader("Upload Foto KTP:", type=["jpg", "png", "jpeg"])
        if st.form_submit_button("Daftar Sekarang"):
            st.success("Terkirim ke Admin!")

elif nav == "Dashboard Login":
    st.header("Portal Klien")
    if not st.session_state.cl_in:
        u = st.text_input("User ID:")
        p = st.text_input("Password:", type="password")
        if st.button("Masuk"):
            match = [c for c in st.session_state.user_creds if c["User ID"]==u and c["Password"]==p]
            if match:
                st.session_state.cl_in = True
                st.session_state.current_user = match[0]
                st.rerun()
            else: st.error("Akses Ditolak")
    else:
        st.info(f"Login: {st.session_state.current_user['User ID']}")
        if st.button("Logout"):
            st.session_state.cl_in = False
            st.rerun()

elif nav == "Admin Panel":
    st.header("Executive Control Panel")
    pwd = st.text_input("Sandi:", type="password")
    if st.button("Buka"):
        if pwd == "w1nbju8282":
            st.table(pd.DataFrame(st.session_state.user_creds))
        else: st.error("Salah")

st.write("---")
st.caption("© 2026 V-Guard AI Intelligence | Erwin Sinaga — Founder")
