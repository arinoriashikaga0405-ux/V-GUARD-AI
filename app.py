import streamlit as st
import pandas as pd
import plotly.express as px
import os
import uuid
from datetime import datetime

# 1. SETTING HALAMAN AGAR TIDAK PECAH
st.set_page_config(page_title="V-Guard AI Systems", layout="wide", page_icon="🛡️")
wa_url = "https://wa.me/6282122190885"

# DATA PAKET (FORMAT RUPIAH RAPI)
pkgs = {
    "MIKRO": {"N": "Basic Guard", "S": "2.500.000", "M": "500.000"},
    "MENENGAH": {"N": "Premium Shield", "S": "7.500.000", "M": "1.500.000"},
    "ENTERPRISE": {"N": "Enterprise Vault", "S": "50.000.000", "M": "5.000.000"},
    "CORPORATE": {"N": "Elite Managed", "S": "85.000.000", "M": "10.000.000"}
}

# 2. SIDEBAR NAVIGASI
with st.sidebar:
    st.title("🛡️ V-Guard AI")
    menu = st.sidebar.radio("Pilih Menu:", ["🏠 Home & ROI", "📦 Paket Solusi", "👤 Profil Founder", "🔐 Admin Panel"])
    st.write("---")

# --- HOME & ROI ---
if menu == "🏠 Home & ROI":
    st.title("🛡️ ROI & Penyelamatan Kerugian")
    st.info("Kalkulator untuk mengukur potensi penghematan bisnis Anda.")
    
    num_trans = st.number_input("Total Transaksi/Bulan:", value=1000)
    avg_val = st.number_input("Rata-rata Nilai Transaksi (Rp):", value=500000)
    fraud_p = st.slider("Asumsi Fraud (%):", 0.0, 5.0, 1.2)
    
    pot_loss = (num_trans * avg_val) * (fraud_p / 100)
    
    st.error(f"### 🚩 Potensi Kerugian: Rp {pot_loss:,.0f}")
    st.success(f"### ✅ Penyelamatan V-Guard AI: Rp {pot_loss * 0.99:,.0f}")

# --- PAKET SOLUSI (2x2 LAYOUT AGAR TIDAK BERANTAKAN) ---
elif menu == "📦 Paket Solusi":
    st.title("📦 Paket Solusi & Pengiriman Data")
    
    # Baris 1
    c1, c2 = st.columns(2)
    with c1:
        st.warning("**MIKRO - Basic Guard**")
        st.write(f"Setup: Rp {pkgs['MIKRO']['S']}")
        st.write(f"Bulanan: Rp {pkgs['MIKRO']['M']}")
        st.link_button("Pesan via WA", wa_url, use_container_width=True)
    with c2:
        st.warning("**MENENGAH - Premium Shield**")
        st.write(f"Setup: Rp {pkgs['MENENGAH']['S']}")
        st.write(f"Bulanan: Rp {pkgs['MENENGAH']['M']}")
        st.link_button("Pesan via WA", wa_url, use_container_width=True)
    
    # Baris 2
    c3, c4 = st.columns(2)
    with c3:
        st.warning("**ENTERPRISE - Enterprise Vault**")
        st.write(f"Setup: Rp {pkgs['ENTERPRISE']['S']}")
        st.write(f"Bulanan: Rp {pkgs['ENTERPRISE']['M']}")
        st.link_button("Pesan via WA", wa_url, use_container_width=True)
    with c4:
        st.warning("**CORPORATE - Elite Managed**")
        st.write(f"Setup: Rp {pkgs['CORPORATE']['S']}")
        st.write(f"Bulanan: Rp {pkgs['CORPORATE']['M']}")
        st.link_button("Pesan via WA", wa_url, use_container_width=True)

    st.write("---")
    st.subheader("📲 Antrean Data AI (Server Control)")
    c_name = st.text_input("Nama Perusahaan:")
    if st.button("Kirim ke Antrean"):
        if c_name:
            tm = datetime.now().strftime("%H:%M:%S")
            st.success(f"Data {c_name} berhasil masuk antrean pada jam {tm}")
        else: st.warning("Mohon isi nama perusahaan.")

# --- PROFIL FOUNDER (WA SUDAH DIHAPUS TOTAL) ---
elif menu == "👤 Profil Founder":
    st.header("Strategic Leadership")
    l, r = st.columns([1, 2])
    with l:
        if os.path.exists("erwin.jpg"): 
            st.image("erwin.jpg", use_container_width=True)
        else: 
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=250)
    with r:
        st.subheader("Erwin Sinaga")
        st.markdown("#### *Founder & Chief Executive Officer*")
        st.write("""
        Bapak Erwin Sinaga adalah seorang Senior Business Leader visioner dengan rekam jejak impresif selama lebih dari 10 tahun 
        di posisi krusial sebagai CEO dan CSO dalam industri perbankan serta manajemen aset. Pengalaman mendalam beliau dalam 
        mengelola risiko operasional, memimpin transformasi digital, dan menjaga integritas aset bernilai tinggi menjadi pondasi 
        kuat di balik berdirinya V-Guard AI Systems. Beliau berdedikasi penuh untuk mendemokratisasi akses terhadap teknologi 
        keamanan finansial kelas dunia bagi UMKM maupun Korporat global di tahun 2026.
        """)

# --- ADMIN PANEL ---
elif menu == "🔐 Admin Panel":
    st.title("🔐 Admin Dashboard")
    if 'auth' not in st.session_state: st.session_state.auth = False
    
    if not st.session_state.auth:
        pwd = st.text_input("Masukkan Password Admin:", type="password")
        if st.button("Authorize"):
            if pwd == st.secrets["ADMIN_PASSWORD"]:
                st.session_state.auth = True
                st.rerun()
            else: st.error("Akses Ditolak!")
    else:
        st.success("Selamat Datang kembali, Pak Erwin.")
        if st.button("Logout Admin"):
            st.session_state.auth = False
            st.rerun()
        st.write("Monitoring Real-time dan Alarm Aktif tersedia di sini.")

st.write("---")
st.caption("© 2026 V-Guard AI Systems | Tangerang, Indonesia")
