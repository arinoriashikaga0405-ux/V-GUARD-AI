import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="VGUARD AI Systems - Executive Platform", page_icon="🛡️", layout="wide")

# Inisialisasi State Navigasi
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- 2. CSS CUSTOM EKSEKUTIF ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .header-box { text-align: center; padding: 20px 0; }
    .main-title { font-size: 3rem !important; font-weight: 800; color: #1e3a8a; margin-bottom: 0; }
    .mission-box { 
        background-color: #ffffff; padding: 20px; border-radius: 12px; 
        border-left: 8px solid #1e3a8a; box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
        text-align: center; margin: 20px auto; max-width: 900px;
    }
    .card-paket {
        background-color: #ffffff; padding: 25px; border-radius: 15px; 
        border: 1px solid #e2e8f0; height: 420px; transition: 0.3s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02); text-align: center;
    }
    .card-paket:hover { transform: translateY(-5px); box-shadow: 0 10px 15px rgba(0,0,0,0.1); border-color: #ef4444; }
    .alarm-tag { 
        background-color: #fee2e2; color: #ef4444; padding: 5px 10px; 
        border-radius: 20px; font-size: 0.75rem; font-weight: bold; border: 1px solid #fecaca;
    }
    .feature-card {
        background-color: #ffffff; padding: 15px; border-radius: 10px;
        border-top: 4px solid #1e3a8a; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .roi-calc-box {
        background-color: #f1f5f9; padding: 25px; border-radius: 15px;
        border: 2px solid #1e3a8a; margin-top: 20px;
    }
    .stButton>button { background-color: #1e3a8a; color: white; border-radius: 8px; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    try:
        st.image("erwin.jpg", width=80) 
    except:
        st.write("👤 CEO PROFILE")
    st.markdown("### ERWIN")
    st.caption("Founder & CEO VGUARD AI")
    st.write("---")
    if st.button("🏠 Beranda Utama"):
        st.session_state.page = "Home"
    st.write("---")
    st.error("🚨 V-GUARD FIRE ALARM: ACTIVE")

# --- 4. LOGIKA NAVIGASI ---

if st.session_state.page == "Admin":
    st.title("💻 Command Center - Admin Audit")
    pwd = st.text_input("Kode Otoritas Admin", type="password")
    if pwd == "vguard2026":
        st.success("Akses Otoritas Diterima.")
        st.subheader("🔍 Scan Temuan Mencurigakan")
        st.warning("🚨 [ALARM] Deteksi Void Massal di Cabang Tangerang!")
        if st.button("🔔 Bunyikan Alarm Owner"):
            st.error("Notifikasi Fire Alarm Terkirim ke WhatsApp Owner!")
    elif pwd != "":
        st.error("Kode Salah!")

elif st.session_state.page == "Klien":
    st.title("📱 Owner Dashboard")
    st.metric("Total Profit Aman", "Rp 125M", "Protected")
    st.subheader("🔥 Log V-Guard Fire Alarm")
    st.info("Pesan: [02:15 AM] Alarm Berbunyi - Percobaan Manipulasi Stok di Store 01.")

else:
    st.markdown('<div class="header-box"><p class="main-title">🛡️ VGUARD AI SYSTEMS</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="mission-box"><p style="font-size:1.4rem; font-style:italic; color:#1e3a8a; margin:0;">"Digitizing Trust, Eliminating Leakage"</p></div>', unsafe_allow_html=True)

    # Profil (10 Tahun Bank)
    st.write("---")
    c_img, c_txt = st.columns([1, 4])
    with c_img:
        try: st.image("erwin.jpg", width=140)
        except: st.info("CEO Photo")
    with c_txt:
        st.markdown("### FOUNDER PROFILE & FILOSOFI")
        st.write("""
        Saya **Erwin**, Founder VGUARD AI Systems, mengintegrasikan standar keamanan **10 tahun pengalaman profesional di industri perbankan** ke dalam operasional bisnis Anda. Filosofi kami, **Perisai Digital**, dirancang untuk memberikan perlindungan aset mutlak melalui sistem **V-Guard Fire Alarm** yang mendeteksi setiap titik kebocoran secara instan.
        """)

    # Navigasi Ekosistem
    st.write("---")
    col_adm, col_cli = st.columns(2)
    with col_adm:
        st.markdown('<div class="feature-card"><b>ADMIN PORTAL</b><br>Audit & Monitoring Kebocoran.</div>', unsafe_allow_html=True)
        if st.button("Masuk Admin"): st.session_state.page = "Admin"; st.rerun()
    with col_cli:
        st.markdown('<div class="feature-card"><b>OWNER PORTAL</b><br>Terima Notifikasi Fire Alarm.</div>', unsafe_allow_html=True)
        if st.button("Masuk Klien"): st.session_state.page = "Klien"; st.rerun()

    # LAYANAN PRODUK & PAKET (UPDATE: FIRE ALARM INCLUDED)
    st.write("---")
    st.markdown("### 🏷️ LAYANAN PRODUK & PAKET")
    p1, p2, p3, p4 = st.columns(4)
    
    with p1:
