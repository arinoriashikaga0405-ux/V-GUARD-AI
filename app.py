import streamlit as st
import pandas as pd
import os

# --- 1. CONFIG ---
st.set_page_config(page_title="V-Guard AI Intelligence", layout="wide")

# --- 2. DATABASE (Password Admin: w1nbju8282) ---
if 'user_creds' not in st.session_state:
    st.session_state.user_creds = [
        {"User ID": "admin", "Password": "w1nbju8282", "Level": "Eksekutif", "Paket": "MASTER"},
        {"User ID": "siska", "Password": "p", "Level": "Klien", "Paket": "SMART"},
        {"User ID": "jaya", "Password": "p", "Level": "Klien", "Paket": "BASIC"}
    ]

if 'client_logged_in' not in st.session_state: st.session_state.client_logged_in = False
if 'current_user' not in st.session_state: st.session_state.current_user = None
if 'auth_admin' not in st.session_state: st.session_state.auth_admin = False

# --- 3. CSS TAMPILAN ---
st.markdown("""
<style>
    .status-box { background-color: #e3f2fd; padding: 15px; border-radius: 8px; color: #1e3a8a; font-weight: bold; margin-bottom: 5px; }
    .package-box { background-color: #fff3e0; padding: 8px 15px; border-radius: 8px; color: #e65100; font-weight: bold; display: inline-block; margin-bottom: 20px; border: 1px solid #ffe0b2; }
    .service-card { background-color: #ffffff; padding: 15px; border-radius: 12px; border: 1px solid #e0e0e0; text-align: center; height: 350px; }
    .fraud-header { background-color: #ff7675; color: white; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR NAVIGASI 1-5 ---
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    st.markdown("**Erwin Sinaga - Senior Business Leader**")
    st.write("---")
    nav = st.radio("Navigasi Utama:", [
        "1. 👤 Profil Founder", 
        "2. 🎯 Visi, Misi & ROI", 
        "3. 💎 Layanan Produk", 
        "4. 📝 Registrasi & Dashboard", 
        "5. 🔐 Akses Terbatas"
    ])

# --- 5. LOGIKA HALAMAN ---

if nav == "1. 👤 Profil Founder":
    st.header("Profil Kepemimpinan")
    st.write("""Bapak **Erwin Sinaga** adalah seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Beliau membangun V-Guard AI untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif dan efisien.""")

elif nav == "2. 🎯 Visi, Misi & ROI":
    st.header("Visi, Misi & Analisis Kerugian")
    st.info("**Visi:** Menjadi pelopor global dalam infrastruktur audit digital berbasis AI.")
    oz = st.number_input("Input Omzet Bulanan (Rp):", value=100000000)
    leakage = oz * 0.07
    st.error(f"Potensi Kerugian (7%): Rp {leakage:,.0f}")

elif nav == "3. 💎 Layanan Produk":
    st.header("Paket Layanan V-Guard AI")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="service-card"><h3>BASIC</h3>Rp 1.5jt<br>Audit Dasar</div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="service-card"><h3>SMART</h3>Rp 2.5jt<br>Monitoring Pro</div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="service-card"><h3>PRO</h3>Rp 5.0jt<br>Multi-Cabang</div>', unsafe_allow_html=True)

elif nav == "4. 📝 Registrasi & Dashboard":
    if not st.session_state.client_logged_in:
        st.subheader("🔑 Login Dashboard Klien")
        u = st.text_input("User ID:")
        p = st.text_input("Password:", type="password")
        if st.button("LOGIN KLIEN"):
            user = next((c for c in st.session_state.user_creds if c["User ID"] == u and c["Password"] == p), None)
            if user:
                st.session_state.client_logged_in = True
                st.session_state.current_user = user
                st.rerun()
            else: st.error("User ID atau Password Salah!")
    else:
        pkg = st.session_state.current_user.get("Paket", "N/A")
        st.markdown('<div class="status-box">Status Akun: ✅ AKTIF</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="package-box">📦 Paket Layanan: {pkg}</div>', unsafe_allow_html=True)
        if st.button("Keluar"):
            st.session_state.client_logged_in = False
            st.rerun()

elif nav == "5. 🔐 Akses Terbatas":
    if not st.session_state.auth_admin:
        st.subheader("🔐 Akses Khusus Admin")
        u_adm = st.text_input("Username Admin:", value="admin")
        p_adm = st.text_input("Password Admin:", type="password")
        if st.button("BUKA PANEL ADMIN"):
            # PASSWORD SUDAH DIKUNCI KE w1nbju8282
            if u_adm == "admin" and p_adm == "w1nbju8282":
                st.session_state.auth_admin = True
                st.rerun()
            else: st.error("Password Admin Salah!")
    else:
        st.markdown('<div class="fraud-header">🚨 PANEL KONTROL EKSEKUTIF</div>')
        with st.form("add"):
            st.write("### Tambah Klien Baru")
            nu = st.text_input("ID Baru:")
            np = st.text_input("Pass Baru:")
            nk = st.selectbox("Pilih Paket:", ["BASIC", "SMART", "PRO"])
            if st.form_submit_button("AKTIFKAN"):
                st.session_state.user_creds.append({"User ID": nu, "Password": np, "Level": "Klien", "Paket": nk})
                st.rerun()
        st.table(pd.DataFrame(st.session_state.user_creds))
        if st.button("Tutup Panel Admin"):
            st.session_state.auth_admin = False
            st.rerun()

st.write("---")
st.caption("© 2026 V-Guard AI | Secured by Erwin Sinaga")
