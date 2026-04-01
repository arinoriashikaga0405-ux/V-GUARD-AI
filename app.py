import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta

# 1. SETUP AWAL
st.set_page_config(page_title="V-Guard AI")

if 'db_nasabah' not in st.session_state:
    dt = datetime.now().date()
    jt_val = dt + timedelta(days=5)
    st.session_state.db_nasabah = [
        {
            "ID": 101, "Tgl": "2026-03-01", 
            "Pelanggan": "Siska", 
            "Bisnis": "Cafe Maju", 
            "Paket": "SMART", "Harga": 2500000, 
            "Jatuh_Tempo": str(jt_val),
            "Status": "🟢 AKTIF", "Score": 98
        }
    ]

if 'admin_in' not in st.session_state:
    st.session_state.admin_in = False

WA = "628212190885"
PWD = "w1nbju8282"

def format_rp(n):
    v = "{:,.0f}".format(float(n))
    return "Rp " + v.replace(",", ".")

# 2. STYLE & SIDEBAR
st.markdown("""
<style>
    .alarm { background: red; color: white; padding: 10px; border-radius: 5px; text-align: center; font-weight: bold; }
    .notif { background: orange; padding: 10px; border-radius: 5px; color: black; margin-bottom: 5px; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg")
    st.write("**Erwin Sinaga**")
    st.write("Senior Business Leader")
    st.write("---")
    m = st.radio("Menu:", ["Profil", "ROI", "Paket", "Admin"])
    st.link_button("Chat Support", "https://wa.me/" + WA)

# 3. LOGIKA HALAMAN
if m == "Profil":
    st.header("Profil Founder")
    st.write("Bapak Erwin Sinaga merupakan Senior Business Leader berpengalaman lebih dari satu dekade di industri perbankan dan aset manajemen. Beliau ahli dalam identifikasi celah kebocoran finansial. V-Guard AI dibangun untuk perlindungan aset yang transparan dan berbasis teknologi mutakhir bagi pemilik bisnis.")

elif m == "ROI":
    st.header("Analisis ROI")
    st.info("Visi: Audit AI Real-time.")
    oz = st.number_input("Omzet (Rp):", value=100000000)
    bc = oz * 0.07
    st.error("Bocor (7%): " + format_rp(bc))
    sv = bc - 2500000
    st.success("Save: " + format_rp(sv))

elif m == "Paket":
    st.header("Paket Layanan")
    c1, c2 = st.columns(2)
    c1.info("BASIC: 1.5jt")
    c2.success("SMART: 2.5jt")

elif m == "Admin":
    if not st.session_state.admin_in:
        p = st.text_input("Pass:", type="password")
        if st.button("Login"):
