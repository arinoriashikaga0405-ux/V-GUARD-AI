import streamlit as st
import hashlib
from datetime import datetime
import os

# --- 1. CONFIG & KEAMANAN ---
WHATSAPP_NUMBER = "6282122190885" 
ADMIN_PWD_HASH = hashlib.sha256("w1nbju8282".encode()).hexdigest()

if 'auth_vguard' not in st.session_state:
    st.session_state['auth_vguard'] = False

# --- 2. PREMIUM UI DESIGN (CSS) ---
st.set_page_config(page_title="V-Guard AI | Erwin Sinaga", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #1e293b; border-right: 1px solid #334155; }
    
    .product-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 20px; border-radius: 20px; border: 1px solid #334155; height: 100%;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    
    /* Panel ROI di bawah tombol */
    .roi-panel-bottom {
        background-color: rgba(52, 211, 153, 0.05);
        border: 1px dashed #34d399; padding: 15px; border-radius: 12px; margin-top: 25px;
    }
    
    .price-tag { color: #34d399; font-size: 22px; font-weight: bold; }
    .wa-btn {
        display: block; text-align: center; background-color: #059669; color: white !important;
        padding: 10px; border-radius: 10px; text-decoration: none; font-weight: bold; margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("erwin.jpg"):
        st.image("erwin.jpg", use_column_width=True)
    st.markdown('<p style="text-align:center; font-weight:800; font-size:22px; color:white;">Erwin Sinaga</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#38bdf8; font-size:13px; margin-top:-10px;">Founder & CEO V-Guard AI</p>', unsafe_allow_html=True)
    st.divider()
    menu = st.radio("NAVIGASI:", ["🏠 Home", "📦 Produk & Investasi", "🔑 Portal Klien", "🔐 Admin Panel"])

# --- 📂 FOLDER 2: PRODUK & ANALISIS ROI ---
if menu == "📦 Produk & Investasi":
    st.title("🛡️ 4 Produk Utama & Analisis ROI")
    st.divider()
    
    p1, p2, p3, p4 = st.columns(4)
    products = [
        ("V-LITE", "1.5M", "250rb", "• AI Fraud Dasar<br>• Laporan PDF WA", "Rp 2jt - 5jt"),
        ("V-PRO", "3.5M", "750rb", "• Real-Time Monitor<br>• VCS Automate", "Rp 10jt - 25jt"),
        ("V-SIGHT", "5.0M", "1.2jt", "• Behavior Visual<br>• Video Audit Struk", "Rp 30
