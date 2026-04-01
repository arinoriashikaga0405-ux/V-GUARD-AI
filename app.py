import streamlit as st
import pandas as pd

# 1. SETTING HALAMAN
st.set_page_config(page_title="V-Guard AI", layout="wide")

# 2. DATABASE (Admin Pass: w1nbju8282)
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "Eksekutif", "Paket": "MASTER"},
        {"User ID": "siska", "Password": "p", "Level": "Klien", "Paket": "SMART"}
    ]
if 'client_logged_in' not in st.session_state: st.session_state.client_logged_in = False
if 'auth_admin' not in st.session_state: st.session_state.auth_admin = False

# 3. SIDEBAR NAVIGASI 1-5
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    st.markdown("**Erwin Sinaga**\nSenior Business Leader")
    st.write("---")
    nav = st.radio("Menu:", ["1. Profil", "2. ROI", "3. Layanan", "4. Registrasi & Dashboard", "5. Akses Admin"])

# 4. LOGIKA MENU
if nav == "1. Profil":
    st.header("Profil Founder")
    st.write("Bapak Erwin Sinaga adalah Senior Business Leader dengan pengalaman 10+ tahun dalam manajemen aset dan perbankan.")

elif nav == "2. ROI":
    st.header("Analisis ROI")
    oz = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    st.error(f"Potensi Kebocoran (7%): Rp {oz * 0.07:,.0f}")

elif nav == "3. Layanan":
    st.header("Paket Layanan")
    st.write("BASIC (1.5jt), SMART (2.5jt), PRO (5jt)")

elif nav == "4. Registrasi & Dashboard":
    tab1, tab2 = st.tabs(["📝 Pendaftaran", "🔑 Login Klien"])
    with tab1:
        with st.form("reg_form"):
            st.text_input("Nama Pelanggan:")
            st.text_input("Jenis Usaha:")
            st.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO"])
            st.text_input("Harga Kesepakatan (Rp):")
            st.file_uploader("Upload Foto KTP:", type=["jpg", "png"])
            if st.form_submit_button("KIRIM PENDAFTARAN"):
                st.success("Data Berhasil Dikirim!")
    with tab2:
        if not st.session_state.client_logged_in:
            u = st.text_input("User ID:")
            p = st.text_input("Password:", type="password")
            if st.button("LOGIN KLIEN"):
                user = next((c for c in st.session_state.user_creds if c["User ID"] == u and c["Password"] == p), None)
                if user:
                    st.session_state.client_logged_in = True
                    st.session_state.current_user = user
                    st.rerun()
                else: st.error("ID atau Password Salah")
        else:
            st.info(f"Selamat Datang! Paket Anda: {st.session_state.current_user['Paket']}")
            if st.button("Keluar Dashboard"):
                st.session_state.client_logged_in = False
                st.rerun()

elif nav == "5. Akses Admin":
    if not st.session_state.auth_admin:
        ua = st.text_input("Admin ID:", value="admin")
        pa = st.text_input("Admin Password:", type="password")
        if st.button("BUKA PANEL"):
            if ua == "admin" and pa == "w1nbju8282":
                st.session_state.auth_admin = True
                st.rerun()
            else: st.error("Akses Ditolak")
    else:
        st.subheader("Panel Kontrol Eksekutif")
        st.table(pd.DataFrame(st.session_state.user_creds))
        if st.button("Logout Admin"):
            st.session_state.auth_admin = False
            st.rerun()

st.write("---")
st.caption("© 2026 V-Guard AI | Erwin Sinaga")
