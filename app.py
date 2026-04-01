import streamlit as st
import pandas as pd
import os

# --- 1. INITIAL SETTINGS ---
st.set_page_config(page_title="V-Guard AI", layout="wide")

if 'admin_authed' not in st.session_state:
    st.session_state.admin_authed = False
if 'db_reg' not in st.session_state:
    st.session_state.db_reg = []

# --- 2. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.caption("Erwin Sinaga — Founder")
    st.write("---")
    menu = [
        "Profil Kepemimpinan", "Visi dan Misi", 
        "Daftar Produk Utama", "Register Pelanggan", 
        "Dashboard Login", "Admin Panel"
    ]
    nav = st.radio("Pilih Menu:", menu)
    st.write("---")
    st.markdown("[💬 Hubungi Admin](https://wa.me/628212190885)")

# --- 3. FUNGSI HALAMAN (MODULAR) ---

def show_profile():
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga")
    with col2:
        st.write("""
        Bapak **Erwin Sinaga** adalah **Founder** V-Guard AI Intelligence. 
        Dengan pengalaman lebih dari 10 tahun di perbankan dan aset manajemen, 
        beliau membangun V-Guard AI untuk memastikan transparansi mutlak bagi 
        pengusaha melalui audit real-time berbasis kecerdasan buatan. 
        Beliau berkomitmen membantu UMKM dan Korporasi mengamankan aset 
        dari risiko kebocoran finansial secara menyeluruh.
        """)

def show_products():
    st.header("Solusi V-Guard AI")
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.subheader("📦 V-LITE")
            st.write("Pasang: 1jt | Bulan: 1jt")
            st.write("- AI Fraud Dasar\n- Laporan Bulanan WA")
    with c2:
        with st.container(border=True):
            st.subheader("🚀 V-PRO")
            st.write("Pasang: 2jt | Bulan: 2.5jt")
            st.write("- VCS Integrasi Stok/Bank\n- Audit AI Harian")

def show_register():
    st.header("Pendaftaran Klien Baru")
    with st.form("f_reg"):
        n_p = st.text_input("Nama Pemilik:")
        n_u = st.text_input("Nama Usaha:")
        u_t = st.selectbox("Tipe Usaha:", ["Retail", "Resto", "Jasa"])
        if st.form_submit_button("Daftar Sekarang"):
            st.session_state.db_reg.append({"Nama": n_p, "Usaha": n_u, "Tipe": u_t})
            st.success("Terkirim! Mohon tunggu aktivasi Admin.")

def show_admin():
    if not st.session_state.admin_authed:
        st.header("🛡️ Restricted Access")
        pwd = st.text_input("Sandi Otoritas:", type="password")
        if st.button("Login Admin"):
            if pwd == "w1nbju8282":
                st.session_state.admin_authed = True
                st.rerun()
            else: st.error("Sandi Salah!")
    else:
        st.header("🛡️ Central Management")
        if st.button("Logout"):
            st.session_state.admin_authed = False
            st.rerun()
        
        tab1, tab2 = st.tabs(["✅ Aktivasi Klien", "📊 Monitor AI"])
        with tab1:
            if st.session_state.db_reg:
                df = pd.DataFrame(st.session_state.db_reg)
                st.table(df)
                if st.button("Aktifkan Semua"):
                    st.success("Klien Telah Diaktifkan!")
            else: st.write("Belum ada pendaftar.")
        with tab2:
            st.metric("Fraud Alert", "0", "Aman")
            st.metric("VCS Accuracy", "99.8%")

# --- 4. MAIN LOGIC (ROUTING) ---
if nav == "Profil Kepemimpinan": show_profile()
elif nav == "Visi dan Misi": st.header("Visi & Misi"); st.info("Menjadi pelopor audit AI global.")
elif nav == "Daftar Produk Utama": show_products()
elif nav == "Register Pelanggan": show_register()
elif nav == "Dashboard Login": st.header("Portal Klien"); st.text_input("ID:"); st.button("Masuk")
elif nav == "Admin Panel": show_admin()

st.write("---")
st.caption("© 2026 V-Guard AI Intelligence | Founder")
