import streamlit as st
import pandas as pd
import os

# --- 1. SETTING HALAMAN ---
st.set_page_config(page_title="V-Guard AI", layout="wide")

# --- 2. DATA KOMUNIKASI ---
HP = "628212190885"
LINK_WA = f"https://wa.me/{HP}"

# --- 3. DATABASE SESSION ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "Admin", "Paket": "MASTER"},
        {"User ID": "siska", "Password": "p", "Level": "Klien", "Paket": "SMART"}
    ]
if 'cl_in' not in st.session_state: st.session_state.cl_in = False

# --- 4. SIDEBAR (FOTO & IDENTITAS) ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    # Mencari foto di folder VGUARD_AI_APP
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    
    # Perbaikan tampilan teks agar rapi
    st.subheader("Erwin Sinaga")
    st.write("**Senior Business Leader**")
    st.write("---")
    
    nav = st.radio("Pilih Menu:", [
        "1. Profil Founder", 
        "2. Visi Misi ROI", 
        "3. Produk Layanan", 
        "4. Dashboard", 
        "5. Admin"
    ])
    st.write("---")
    st.link_button("💬 Hubungi WhatsApp", LINK_WA)

# --- 5. LOGIKA MENU ---

if nav == "1. Profil Founder":
    st.header("Profil Kepemimpinan")
    with st.container(border=True):
        st.write("""Bapak **Erwin Sinaga** adalah Senior Business Leader dengan pengalaman lebih dari 10 tahun. 
        Keahlian utama beliau terletak pada kemampuan analitis dalam mengidentifikasi celah kebocoran finansial bisnis. 
        V-Guard AI dibangun untuk menjamin transparansi mutlak bagi pemilik bisnis melalui audit real-time.""")

elif nav == "2. Visi Misi ROI":
    st.header("Visi, Misi & ROI")
    c1, c2 = st.columns(2)
    with c1: st.info("**Visi:** Menjadi pelopor audit digital berbasis AI.")
    with c2: st.success("**Misi:** Deteksi fraud real-time & proteksi aset UMKM.")
    st.write("---")
    oz = st.number_input("Input Omzet Bulanan (Rp):", value=100000000)
    st.error(f"Potensi Kerugian (7%): Rp {oz * 0.07:,.0f}")

elif nav == "3. Produk Layanan":
    st.header("Layanan & Pemesanan")
    ca, cb, cc = st.columns(3)
    with ca:
        with st.container(border=True):
            st.subheader("BASIC")
            st.write("Rp 1.500.000")
            st.link_button("Pesan BASIC", f"{LINK_WA}?text=Pesan%20BASIC")
    with cb:
        with st.container(border=True):
            st.subheader("SMART")
            st.write("Rp 2.500.000")
            st.link_button("Pesan SMART", f"{LINK_WA}?text=Pesan%20SMART")
    with cc:
        with st.container(border=True):
            st.subheader("PRO")
            st.write("Rp 5.000.000")
            st.link_button("Pesan PRO", f"{LINK_WA}?text=Pesan%20PRO")

elif nav == "4. Dashboard":
    tab1, tab2 = st.tabs(["📝 Registrasi", "🔑 Login"])
    with tab1:
        # Perbaikan form: Tombol submit ditambahkan agar tidak error
        with st.form("form_pendaftaran"):
            st.text_input("Nama:")
            st.text_input("Usaha:")
            st.selectbox("Paket:", ["BASIC", "SMART", "PRO"])
            st.text_input("Harga Kesepakatan:")
            if st.form_submit_button("KIRIM PENDAFTARAN"):
                st.success("Data berhasil terkirim!")

    with tab2:
        if not st.session_state.cl_in:
            u = st.text_input("User ID:")
            p = st.text_input("Password:", type="password")
            if st.button("MASUK"):
                user = next((c for c in st.session_state.user_creds if c["User ID"] == u and c["Password"] == p), None)
                if user:
                    st.session_state.cl_in = True
                    st.session_state.current_user = user
                    st.rerun()
                else: st.error("Login Gagal")
        else:
            st.info(f"Akun Aktif: {st.session_state.current_user['User ID']}")
            if st.button("Keluar"):
                st.session_state.cl_in = False
                st.rerun()

elif nav == "5. Admin":
    pw = st.text_input("Password Admin:", type="password")
    if st.button("BUKA PANEL"):
        if pw == "w1nbju8282":
            st.table(pd.DataFrame(st.session_state.user_creds))
        else: st.error("Akses Ditolak")

st.write("---")
st.caption("© 2026 V-Guard AI | Erwin Sinaga")
