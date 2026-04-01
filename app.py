import streamlit as st
import pandas as pd

# --- 1. CONFIG HALAMAN ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE USER (Password Admin: w1nbju8282) ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "Eksekutif", "Paket": "MASTER"},
        {"User ID": "siska", "Password": "p", "Level": "Klien", "Paket": "SMART"}
    ]

if 'client_logged_in' not in st.session_state: st.session_state.client_logged_in = False
if 'auth_admin' not in st.session_state: st.session_state.auth_admin = False

# --- 3. SIDEBAR NAVIGASI 1-5 ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    st.markdown("**Erwin Sinaga - Senior Business Leader**")
    st.write("---")
    nav = st.radio("Navigasi Utama:", ["1. Profil Founder", "2. Visi Misi ROI", "3. Layanan Produk", "4. Registrasi & Dashboard", "5. Akses Admin"])

# --- 4. LOGIKA MENU ---

if nav == "1. Profil Founder":
    st.header("Profil Kepemimpinan")
    st.write("Bapak Erwin Sinaga adalah Senior Business Leader dengan pengalaman 10+ tahun.")

elif nav == "2. Visi Misi ROI":
    st.header("Visi, Misi & ROI")
    oz = st.number_input("Input Omzet Bulanan (Rp):", value=100000000)
    st.error(f"Potensi Kerugian: Rp {oz * 0.07:,.0f}")

elif nav == "3. Layanan Produk":
    st.header("Paket Layanan")
    st.write("Tersedia Paket: BASIC (1.5jt), SMART (2.5jt), dan PRO (5jt).")

elif nav == "4. Registrasi & Dashboard":
    t1, t2 = st.tabs(["📝 Form Pendaftaran", "🔑 Login Klien"])
    
    with t1:
        st.subheader("Pendaftaran Pelanggan Baru")
        with st.form("form_reg"):
            st.text_input("Nama Pelanggan:")
            st.text_input("Jenis Usaha:")
            st.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO"])
            st.text_input("Harga Kesepakatan (Rp):")
            st.file_uploader("Upload Foto KTP:", type=["jpg", "png"])
            if st.form_submit_button("KIRIM DATA"):
                st.success("Data berhasil terkirim!")

    with t2:
        if not st.session_state.client_logged_in:
            u = st.text_input("User ID:")
            p = st.text_input("Password:", type="password")
            if st.button("LOGIN"):
                user = next((c for c in st.session_state.user_creds if c["User ID"] == u and c["Password"] == p), None)
                if user:
                    st.session_state.client_logged_in = True
                    st.session_state.current_user = user
                    st.rerun()
                else: st.error("Login Gagal")
        else:
            st.success(f"Paket Anda: {st.session_state.current_user['Paket']}")
            if st.button("Keluar"):
                st.session_state.client_logged_in = False
                st.rerun()

elif nav == "5. Akses Admin":
    if not st.session_state.
