"""
🛡️ V-GUARD AI INTELLIGENCE - ENTERPRISE EDITION
Optimasi Railway + Portal Klien Lengkap (Sesuai SOP)
Author: Erwin Sinaga - Founder & CEO
"""

import streamlit as st
import google.generativeai as genai
import pandas as pd
import numpy as np
import os
from datetime import datetime

# ============================================================================
# 1. KONFIGURASI ENGINE & SECURITY (SOP SECTION 1)
# ============================================================================

# Mengambil API Key dari Environment Variables Railway
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    st.warning("⚠️ API Key belum dikonfigurasi di Variables Railway.")

model_vguard = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    generation_config={"temperature": 0.2, "max_output_tokens": 50},
    system_instruction="Analisa transaksi: ALERT jika fraud, PASS jika aman."
)

# Konfigurasi Paket Produk (SOP SECTION 5)
PRODUCTS = {
    "V-LITE": {"install": "750.000", "monthly": "350.000", "desc": "Mikro / 1 Kasir"},
    "V-PRO": {"install": "1.500.000", "monthly": "850.000", "desc": "Retail & Kafe"},
    "V-SIGHT": {"install": "7.500.000", "monthly": "3.500.000", "desc": "Gudang & Toko"},
    "V-ENTERPRISE": {"install": "15.000.000", "monthly": "10.000.000", "desc": "Korporasi"}
}

# ============================================================================
# 2. DATABASE MOCKUP (SOP Section: Aktivasi Klien)
# ============================================================================

if "db_klien" not in st.session_state:
    # Simulasi database klien
    st.session_state.db_klien = pd.DataFrame(columns=[
        "Nama", "Usaha", "Paket", "Harga", "Username", "Password", "Status"
    ])

# ============================================================================
# 3. UI & NAVIGASI (SOP SECTION 4)
# ============================================================================

st.set_page_config(page_title="V-Guard AI Intelligence", page_icon="🛡️", layout="wide")

# Sidebar Navigation
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_container_width=True)
    st.markdown(f"<div style='text-align:center;'><p style='color:white; font-weight:bold;'>Erwin Sinaga</p><p style='color:gray;'>Founder & CEO</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    if "klien_auth" not in st.session_state:
        st.session_state.klien_auth = False

    if not st.session_state.klien_auth:
        menu = st.radio("NAVIGASI", ["Visi & Misi", "Produk & Layanan", "Portal Klien (Daftar/Login)"])
    else:
        menu = "Dashboard Klien"
        if st.button("🚪 Log Out"):
            st.session_state.klien_auth = False
            st.rerun()

# ============================================================================
# 4. LOGIKA MENU (SOP SECTION 5)
# ============================================================================

if menu == "Visi & Misi":
    st.header("🎯 Visi & Misi: Digitizing Trust")
    st.markdown("""
    **V-Guard AI Intelligence** hadir untuk mengeliminasi kebocoran, mengoptimalkan profitabilitas, 
    dan menjaga warisan bisnis Anda tetap utuh melalui inovasi teknologi.
    """)

elif menu == "Portal Klien (Daftar/Login)":
    tab1, tab2 = st.tabs(["📝 Daftar Klien Baru", "🔑 Login User Aktif"])
    
    with tab1:
        st.subheader("Form Order & Registrasi Baru")
        with st.container(border=True):
            c1, c2 = st.columns(2)
            with c1:
                nama_pel = st.text_input("Nama Pelanggan (Sesuai KTP)")
                nama_usa = st.text_input("Nama Usaha")
                ktp = st.file_uploader("Upload KTP", type=['jpg', 'png', 'pdf'])
            with c2:
                pkt = st.selectbox("Pilih Paket", list(PRODUCTS.keys()))
                harga_tampil = PRODUCTS[pkt]['install']
                st.info(f"Biaya Pemasangan: Rp {harga_tampil}")
                user_new = st.text_input("Buat Username")
                pass_new = st.text_input("Buat Password", type="password")
            
            if st.button("Kirim Registrasi"):
                new_data = {
                    "Nama": nama_pel, "Usaha": nama_usa, "Paket": pkt, 
                    "Harga": harga_tampil, "Username": user_new, 
                    "Password": pass_new, "Status": "Menunggu Aktivasi"
                }
                st.session_state.db_klien = pd.concat([st.session_state.db_klien, pd.DataFrame([new_data])], ignore_index=True)
                st.success("✅ Registrasi Terkirim! Mohon tunggu aktivasi dari Admin (Erwin Sinaga).")

    with tab2:
        st.subheader("Akses Dashboard Klien")
        with st.container(border=True):
            u_login = st.text_input("Username")
            p_login = st.text_input("Password ", type="password")
            if st.button("Masuk ke Dashboard"):
                # Cek di database
                db = st.session_state.db_klien
                user_match = db[(db['Username'] == u_login) & (db['Password'] == p_login)]
                
                if not user_match.empty:
                    if user_match.iloc[0]['Status'] == "Aktif":
                        st.session_state.klien_auth = True
                        st.session_state.current_klien = user_match.iloc[0].to_dict()
                        st.rerun()
                    else:
                        st.error("⚠️ Akun Anda ditemukan tetapi BELUM DIAKTIFASI oleh Admin.")
                else:
                    st.error("❌ Username atau Password salah.")

elif menu == "Dashboard Klien":
    klien = st.session_state.current_klien
    st.header(f"🛡️ Dashboard V-Guard: {klien['Usaha']}")
    st.subheader(f"Selamat Datang, {klien['Nama']}")
    
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Paket", klien['Paket'])
    col_b.metric("Status Sistem", "✅ SECURED")
    col_c.metric("Efisiensi AI", "88%")
    
    st.divider()
    st.markdown("### 🤖 V-Guard AI Squad Agents Monitoring")
    sq1, sq2 = st.columns(2)
    with sq1:
        st.info("**Agent: Sentinel** - Menganalisa anomali transaksi kasir.")
    with sq2:
        st.success("**Agent: Auditor** - Sinkronisasi mutasi bank & laporan POS.")
