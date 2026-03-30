import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="V-Guard AI", page_icon="🛡️", layout="wide")

# 2. SISTEM LOGIN
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🛡️ V-GUARD AI SECURE LOGIN")
    pwd_input = st.text_input("Masukkan Password Admin:", type="password")
    if st.button("Masuk Sekarang"):
        try:
            if pwd_input.strip() == st.secrets["ADMIN_PASSWORD"].strip():
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("❌ Password Salah.")
        except:
            st.error("⚠️ Password belum diatur di menu Secrets!")
    st.stop()

# 3. NAVIGASI SIDEBAR
st.sidebar.title("🛡️ V-Guard AI")
page = st.sidebar.radio("Navigasi:", ["🏠 Home", "📊 Dashboard", "📦 Products & Services", "👤 About Founder"])

if st.sidebar.button("🔒 Logout"):
    st.session_state.auth = False
    st.rerun()

# --- HALAMAN 3: PRODUCTS & SERVICES (DESAIN KEREN & HIDUP) ---
if page == "📦 Products & Services":
    st.markdown("<h1 style='text-align: center;'>🏷️ PAKET LAYANAN STRATEGIS</h1>", unsafe_allow_all_html=True)
    st.write("---")

    # CSS untuk membuat kartu terlihat "Hidup"
    st.markdown("""
        <style>
        .price-card {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            text-align: center;
            border-top: 5px solid #1E3A8A;
            height: 450px;
        }
        .price-header { color: #1E3A8A; font-weight: bold; font-size: 24px; margin-bottom: 5px; }
        .target-text { color: #6B7280; font-size: 14px; margin-bottom: 20px; }
        .price-value { color: #1E3A8A; font-size: 32px; font-weight: bold; margin: 20px 0; }
        .feature-list { text-align: left; font-size: 15px; color: #374151; min-height: 150px; }
        </style>
    """, unsafe_allow_all_html=True)

    wa_num = "6282122190885"
    
    col1, col2, col3, col4 = st.columns(4)

    # DATA PAKET
    packages = [
        {
            "col": col1, "name": "V-START", "target": "Target: UMKM", "price": "Rp 2.5 JT", 
            "features": ["Scan Harian", "Laporan Mingguan", "Support Desk", "Limit 1rb Transaksi"]
        },
        {
            "col": col2, "name": "V-GROW", "target": "Target: Multi-Cabang", "price": "Rp 7.5 JT", 
            "features": ["Real-time Scan", "Notifikasi WA Otomatis", "Priority Support", "Limit 5rb Transaksi"]
        },
        {
            "col": col3, "name": "V-PRIME", "target": "Target: Korporasi", "price": "Rp 50 JT", 
            "
