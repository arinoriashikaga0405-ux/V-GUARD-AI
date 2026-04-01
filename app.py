import streamlit as st
import pandas as pd
import os

# --- 1. KONFIGURASI ---
st.set_page_config(page_title="V-Guard AI", layout="wide")

# --- 2. SESSION STATE ---
if 'admin_authed' not in st.session_state:
    st.session_state.admin_authed = False

# --- 3. SIDEBAR (Urutan Navigasi Statis) ---
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
    nav = st.radio("Navigasi Utama:", menu)
    st.write("---")
    st.markdown('<a href="https://wa.me/628212190885" target="_blank" style="background-color:#25d366;color:white;padding:10px;border-radius:8px;text-decoration:none;display:block;text-align:center;font-weight:bold;">💬 Hubungi Admin</a>', unsafe_allow_html=True)

# --- 4. LOGIKA MENU ---

if nav == "Profil Kepemimpinan":
    st.header("Profil Kepemimpinan")
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("erwin.jpg"):
            st.image("erwin.jpg", caption="Erwin Sinaga — Founder")
    with col2:
        with st.container(border=True):
            st.write("""
            Bapak **Erwin Sinaga** adalah sosok **Founder** V-Guard AI Intelligence. 
            Beliau memiliki pengalaman lebih dari 10 tahun di industri perbankan 
            dan manajemen aset. V-Guard AI lahir untuk memberikan transparansi 
            total bagi pemilik bisnis melalui sistem audit real-time berbasis AI 
            guna meminimalisir risiko kerugian dan kebocoran finansial.
            """)

elif nav == "Visi dan Misi":
    st.header("Visi dan Misi Perusahaan")
    v1, v2 = st.columns(2)
    with v1:
        st.info("### 🎯 Visi\nPelopor global teknologi audit digital berbasis AI.")
    with v2:
        st.success("### 🚀 Misi\n1. Proteksi aset via Fraud Detection.\n2. Efisiensi operasional.\n3. Tata kelola bebas bocor.")

elif nav == "Daftar Produk Utama":
    st.header("Produk & Analisis ROI")
    with st.expander("📊 Simulasi ROI", expanded=True):
        oz = st.number_input("Omzet Bulanan (Rp):", value=100000000)
        rugi = oz * 0.07
        st.metric("Potensi Rugi (7%)", f"Rp {rugi:,.0f}")
        st.metric("Aset Aman V-Guard", f"Rp {rugi*0.9:,.0f}")
    st.write("---")
    st.subheader("Fitur Utama: Alarm Fraud, VCS, CCTV & Audit")
    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.write("📦 **V-LITE**\n- Alarm WA\n- Invoice Digital\n- Laba Rugi Bulanan\n- **1jt / Bln**")
    with c2:
        with st.container(border=True):
            st.write("🚀 **V-PRO**\n- VCS (Stok Sync)\n- CCTV AI Behavior\n- Audit Otomatis\n- **2.5jt / Bln**")

elif nav == "Register Pelanggan":
    st.header("Pendaftaran Pelanggan Baru")
    with st.form("reg_form"):
        st.text_input("Nama Pemilik:")
        u_type = st.selectbox("Jenis Usaha:", ["Retail", "Resto", "Jasa"])
        st.selectbox("Paket:", ["V-LITE", "V-PRO", "V-SIGHT", "V-ENTERPRISE"])
        
        # Penjadwalan Anti-Overload
        jam = "22:00" if u_type == "Retail" else "23:00" if u_type == "Resto" else "00:00"
        st.warning(f"Jadwal Sinkronisasi Data: {jam} WIB (Mencegah Overload)")
        
        if st.form_submit_button("Daftar"):
            st.success(f"Berhasil! Slot upload Anda: {jam}")

elif nav == "Dashboard Login":
    st.header("Portal Klien")
