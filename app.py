import streamlit as st
import os
import pandas as pd
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide", page_icon="🛡️")

if 'db_nasabah' not in st.session_state:
    st.session_state.db_nasabah = [
        {"ID": 101, "Waktu": "2026-03-25", "Pelanggan": "Siska", "Bisnis": "Cafe Maju", "Usaha": "F&B", "Paket": "SMART", "Harga": 2500000, "Status": "🟢 AKTIF"},
        {"ID": 102, "Waktu": "2026-03-28", "Pelanggan": "Jaya", "Bisnis": "Bengkel Berkah", "Usaha": "Otomotif", "Paket": "BASIC", "Harga": 1500000, "Status": "🔴 Menunggu"}
    ]
if 'admin_akses_terbuka' not in st.session_state:
    st.session_state.admin_akses_terbuka = False

WA_NUMBER = "628212190885"
ADMIN_PASSWORD = "w1nbju8282"

def format_rp(angka):
    return f"Rp {float(angka):,.0f}".replace(",", ".")

# 2. CSS CUSTOM
st.markdown("""
<style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: white; text-align: center; padding: 10px; border-top: 1px solid #ddd; z-index: 999; }
    .product-card { background-color: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 15px; padding: 20px; text-align: center; min-height: 400px; border-top: 8px solid #1E3A8A; }
    .fraud-alarm { background-color: #ff4b4b; color: white; padding: 12px; border-radius: 8px; text-align: center; font-weight: bold; animation: blinker 2s linear infinite; margin-bottom: 20px; }
    @keyframes blinker { 50% { opacity: 0.7; } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown("<h1 style='color: #1E3A8A;'>🛡️ V-GUARD AI</h1>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"): 
        st.image("erwin.jpg", use_container_width=True)
        st.markdown("<p style='text-align:center;'><b>Erwin Sinaga</b><br>Senior Business Leader</p>", unsafe_allow_html=True)
    menu = st.radio("Menu:", ["1. 👤 Profil", "2. 🎯 Visi & ROI", "3. 📦 Paket", "4. 📝 Registrasi", "5. 🔐 Admin"])
    st.link_button("💬 Chat Support", f"https://wa.me/{WA_NUMBER}")

# --- MENU 1: PROFIL ---
if menu == "1. 👤 Profil":
    st.header("Profil Kepemimpinan")
    c1, c2 = st.columns([1, 2])
    with c1:
        if os.path.exists("erwin.jpg"): st.image("erwin.jpg", use_container_width=True)
    with c2:
        st.subheader("Bapak Erwin Sinaga")
        st.write("Beliau adalah Senior Business Leader dengan pengalaman lebih dari 10 tahun di industri perbankan dan asset management. Melalui V-Guard AI, beliau fokus pada pencegahan kebocoran finansial bisnis melalui audit berbasis AI.")

# --- MENU 2: ROI (FIXED BARIS 76) ---
elif menu == "2. 🎯 Visi & ROI":
    st.header("Strategi ROI")
    st.info("Visi: Menjadi standar emas pengawasan bisnis digital.")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=100000000, step=1000000)
    bocor = omzet * 0.07
    st.error(f"Potensi Kebocoran (7%): {format_rp(bocor)}")
    st.success(f"Dana Diselamatkan: {format_rp(bocor - 2500000)}")

# --- MENU 3: PAKET ---
elif menu == "3. 📦 Paket":
    st.header("Layanan V-Guard")
    cols = st.columns(4)
    pkts = [("BASIC", "1.5jt"), ("SMART", "2.5jt"), ("PRO", "5jt"), ("ELITE", "Custom")]
    for i, (n, p) in enumerate(pkts):
        with cols[i]:
            st.markdown(f'<div class="product-card"><h3>{n}</h3><h2 style="color:red;">{p}</h2><br>• AI Audit<br>• VCS System</div>', unsafe_allow_html=True)
            st.link_button(f"Pesan {n}", f"https://wa.me/{WA_NUMBER}?text=Order%20{n}")

# --- MENU 4: REGISTRASI ---
elif menu == "4. 📝 Registrasi":
    st.header("Pendaftaran Klien")
    with st.form("reg_form"):
        st.text_input("Nama Bisnis")
        st.text_input("Jenis Usaha")
        st.selectbox("Paket", ["BASIC", "SMART", "PRO", "ELITE"])
        if st.form_submit_button("Kirim Pendaftaran"):
            st.success("Terkirim!")

# --- MENU 5: ADMIN (LOCKED) ---
elif menu == "5. 🔐 Admin":
    if not st.session_state.admin_akses_terbuka:
        pwd = st.text_input("Sandi Keamanan:", type="password")
        if st.button("Login"):
            if pwd == ADMIN_PASSWORD:
                st.session_state.admin_akses_terbuka = True
                st.rerun()
            else:
                st.error("Sandi Salah!")
    else:
        st.header("⚙️ Operasional V-Guard")
        if st.button("🔒 Logout"):
            st.session_state.admin_akses_terbuka = False
            st.rerun()
        st.markdown('<div class="fraud-alarm">🚨 ALARM: INDIKASI FRAUD TERDETEKSI!</div>', unsafe_allow_html=True)
        t1, t2 = st.tabs(["📊 Database", "📉 Audit Studio"])
        with t1:
            st.table(pd.DataFrame(st.session_state.db_nasabah))
        with t2:
            st.subheader("Google Studio Gemini Audit")
            st.line_chart([10, 25, 15, 40, 30])

st.markdown('<div class="footer">© 2026 V-Guard AI | Erwin Sinaga</div>', unsafe_allow_html=True)
