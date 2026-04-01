import streamlit as st
import os
import pandas as pd
from datetime import datetime, timedelta

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI", layout="wide")

# Inisialisasi Database
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
        return f"Rp {float(angka):,.0f}".replace(",", ".")
    except:
        return str(angka)

# 2. CSS CUSTOM
st.markdown("""
<style>
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; padding: 10px; font-size: 12px; }
    .alarm { background: #ff4b4b; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; animation: blink 1.5s linear infinite; }
    @keyframes blink { 50% { opacity: 0.6; } }
    .notif { background: #fff3cd; padding: 10px; border-radius: 5px; border-left: 5px solid #ffc107; margin-bottom: 5px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.title("🛡️ V-GUARD AI")
    # Baris pendek untuk mencegah SyntaxError terpotong
    foto_ada = os.path.exists("erwin.jpg")
    if foto_ada:
        st.image("erwin.jpg", use_container_width=True)
    
    st.markdown("**Erwin Sinaga**\nSenior Business Leader")
    st.write("---")
    menu = st.radio("Menu:", ["Profil", "Visi & ROI", "Paket", "Registrasi", "Admin"])
    st.link_button("💬 Chat Support", f"https://wa.me/{WA_NUMBER}")

# --- HALAMAN 1: PROFIL ---
if menu == "Profil":
    st.header("Profil Founder")
    st.write("""Bapak Erwin Sinaga merupakan seorang Senior Business Leader yang memiliki rekam jejak panjang selama lebih dari satu dekade dalam memimpin transformasi operasional dan strategi manajemen di industri perbankan serta manajemen aset nasional. Keahlian utama beliau terletak pada kemampuan analitis yang tajam dalam mengidentifikasi berbagai celah kebocoran finansial yang sering kali tidak terdeteksi oleh sistem pengawasan konvensional. 

Melalui dedikasi yang tinggi terhadap integritas bisnis, beliau membangun V-Guard AI sebagai jawaban atas kebutuhan para pengusaha akan sistem perlindungan aset yang transparan dan berbasis teknologi mutakhir. Berdomisili di Tangerang, beliau kini mendedikasikan seluruh kompetensinya untuk menjembatani kebutuhan dunia usaha dengan solusi digital yang aplikatif. Fokus utama beliau adalah memberikan rasa aman bagi pemilik bisnis melalui penerapan audit berbasis kecerdasan buatan yang mampu meminimalisir risiko kerugian modal secara signifikan.""")

# --- HALAMAN 2: VISI & ROI ---
elif menu == "Visi & ROI":
    st.header("Visi, Misi & ROI")
    st.info("**Visi:** Standar emas audit AI real-time.\n\n**Misi:** Mencegah kebocoran aset bisnis.")
    omzet = st.number_input("Omzet Bulanan (Rp):", value=100000000)
    bocor = omzet * 0.07
    st.error(f"Potensi Bocor (7%): {format_rp(bocor)}")
    st.success(f"P
