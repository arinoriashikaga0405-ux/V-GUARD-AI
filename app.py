import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta

# 1. SETUP
st.set_page_config(page_title="V-Guard AI", layout="wide")

if 'db_nasabah' not in st.session_state:
    today = datetime.now().date()
    st.session_state.db_nasabah = [
        {
            "ID": 101, "Tgl": "2026-03-01", "Pelanggan": "Siska", 
            "Bisnis": "Cafe Maju", "Paket": "SMART", "Harga": 2500000, 
            "Jatuh_Tempo": (today + timedelta(days=5)).strftime("%Y-%m-%d"),
            "Status": "🟢 AKTIF", "Audit_Score": 98
        }
    ]

if 'admin_akses' not in st.session_state:
    st.session_state.admin_akses = False

WA_NUMBER = "628212190885"
ADMIN_PWD = "w1nbju8282"

def format_rp(angka):
    try:
        val = "{:,.0f}".format(float(angka)).replace(",", ".")
        return "Rp " + val
    except:
        return str(angka)

# 2. UI STYLE
st.markdown("""
<style>
    .alarm { background: #ff4b4b; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; animation: blink 1.5s linear infinite; }
    @keyframes blink { 50% { opacity: 0.6; } }
    .notif { background: #fff3cd; padding: 10px; border-radius: 5px; border-left: 5px solid #ffc107; margin-bottom: 5px; color: black; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; padding: 10px; font-size: 10px; background: white; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.markdown("**Erwin Sinaga**\n\nSenior Business Leader")
    st.write("---")
    menu = st.radio("Navigasi:", ["Profil", "Visi & ROI", "Paket", "Registrasi", "Admin"])
    st.write("---")
    st.link_button("💬 Chat Support", "https://wa.me/" + WA_NUMBER)

# --- HALAMAN 1: PROFIL ---
if menu == "Profil":
    st.header("Profil Founder")
    st.write("""Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan.""")

# --- HALAMAN 2: VISI & ROI ---
elif menu == "Visi & ROI":
    st.header("Visi, Misi & ROI")
    st.info("Visi: Standar emas audit AI real-time.\nMisi: Mencegah kebocoran aset bisnis.")
    st.write("---")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    bocor = omzet * 0.07
    st.error("Potensi Kebocoran (7%): " + format_rp(bocor))
    save = bocor - 2500000
    st.success("Dana Diselamatkan V-Guard: " + format_rp(save))

# --- HALAMAN 3: PAKET ---
elif menu == "Paket":
    st.header("Paket Layanan")
    c1, c2, c3 = st.columns(3)
    c1.info("BASIC: 1.5jt\nMonitoring AI")
    c2.success("SMART: 2
