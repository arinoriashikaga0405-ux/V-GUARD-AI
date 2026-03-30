import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Systems", page_icon="🛡️", layout="wide")

# --- 2. CSS MODERN & CLEAN ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    .stApp { font-family: 'Poppins', sans-serif; background-color: white; }
    [data-testid="stSidebar"] { background-color: #0D47A1; }
    [data-testid="stSidebar"] * { color: white !important; }
    .card { background: #F8FAFC; padding: 20px; border-radius: 10px; border-left: 5px solid #00BCD4; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 4. LOGIKA NAVIGASI ---
if not st.session_state.auth:
    st.markdown("<div style='text-align:center; padding-top:100px;'>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/1004/1004666.png", width=80)
    st.title("V-GUARD AI SYSTEMS")
    st.write("Intelligence That Protects Profit | Founder: Erwin Sinaga")
    if st.button("🚀 MASUK KE COMMAND CENTER"):
        st.session_state.auth = True
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
    with st.sidebar:
        st.markdown("### 🛡️ V-Guard AI")
        st.markdown("---")
        menu = st.radio("Navigasi:", ["🏠 Overview", "👥 Manajemen User", "⚙️ Pengaturan AI"])
        st.markdown("---")
        if st.button("🔓 Logout"):
            st.session_state.auth = False
            st.rerun()

    st.header(f"💼 {menu}")
    
    if menu == "🏠 Overview":
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="card"><h4>Status Keamanan</h4><h2 style="color:#F44336;">HIGH RISK!</h2><p>2 Anomali Terdeteksi</p></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="card"><h4>Total Monitoring</h4><h2>Rp 1.42 M</h2><p>Asset under protection</p></div>', unsafe_allow_html=True)
        
        st.subheader("Proyeksi Cash Flow")
        chart_data = pd.DataFrame({'Actual': [10, 20, 15, 30], 'Target': [12, 18, 20, 35]})
        st.line_chart(chart_data)

    elif menu == "👥 Manajemen User":
        st.subheader("Daftar Pengguna Aktif")
        users = pd.DataFrame({
            "Nama": ["Erwin Sinaga", "Jaya", "Shafen"],
            "Role": ["CEO / Admin", "Manager", "Admin"],
            "Status": ["Aktif", "Aktif", "Aktif"]
        })
        st.table(users)

# --- 5. FOOTER (DIPERBAIKI AGAR TIDAK ERROR) ---
st.write("---")
st.caption("© 2026 V-Guard AI Systems | Developed for Erwin Sinaga")
