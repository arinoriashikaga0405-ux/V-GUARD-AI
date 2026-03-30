import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Systems", page_icon="🛡️", layout="wide")

# --- 2. CSS MODERN (KEMBALI KE PUTIH BERSIH & RAPI) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    html { scroll-behavior: smooth; }
    .stApp { font-family: 'Poppins', sans-serif; background-color: white; }
    
    /* Sidebar Navigation */
    [data-testid="stSidebar"] { background-color: #0D47A1; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* Header Utama Sticky */
    .sticky-header {
        position: sticky; top: 0; background: white; padding: 15px 25px;
        display: flex; justify-content: space-between; align-items: center;
        border-bottom: 1px solid #f0f0f0; z-index: 99; margin-bottom: 25px;
    }
    
    /* Widget Card */
    .metric-card {
        background: white; padding: 25px; border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #f0f0f0;
        border-left: 5px solid #0D47A1;
    }
    .risk-alert { border-left-color: #F44336; background: #FFF5F5; }
</style>
""", unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'page' not in st.session_state: st.session_state.page = "Dashboard Overview"

# --- 4. LOGIKA HALAMAN ---
if not st.session_state.auth:
    # RE-LOGIN / LANDING
    st.markdown(f"<div style='text-align:center; padding:100px 0;'>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/1004/1004666.png", width=100)
    st.title("V-GUARD AI SYSTEMS")
    st.write("Intelligence That Protects Profit | Strategically Led by Erwin Sinaga")
    if st.button("🚀 MASUK KE COMMAND CENTER"):
        st.session_state.auth = True
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # --- DASHBOARD SIDEBAR ---
    with st.sidebar:
        st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
        st.markdown("---")
        st.write(f"👤 Admin: Erwin Sinaga")
        menu = st.radio("MAIN MENU", ["🏠 Overview", "👥 Users", "📑 Log Activity", "⚙️ Settings"])
        st.markdown("---")
        if st.button("🔓 Logout"):
            st.session_state.auth = False
            st.rerun()

    # --- HEADER UTAMA ---
    st.markdown(f"""
    <div class="sticky-header">
        <div style="font-weight:bold; font-size:1.4rem; color:#0D47A1;">{menu}</div>
        <div style="color:#666;">{datetime.now().strftime('%d %B %2026')}</div>
    </div>
    """, unsafe_allow_html=True)

    # --- CONTENT AREA ---
    if "Overview" in menu:
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown('<div class="metric-card risk-alert">', unsafe_allow_html=True)
            st.error("⚠️ HIGH RISK ALERT")
            st.write("2 Anomali Terdeteksi")
            st.markdown('</div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.info("💰 TOTAL SALDO")
            st.subheader("Rp 1.42 M")
            st.markdown('</div>', unsafe_allow_html=True)
        with c3:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.success("🛡️ PROFIT PROTECTED")
            st.subheader("Rp 45 JT")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("### 📊 Proyeksi Cash Flow Bulanan")
        # Menggunakan chart bawaan Streamlit agar tidak butuh Plotly
        chart_data = pd.DataFrame({'Actual': [100, 120, 115, 140], 'Forecast': [105, 125, 120, 160]})
        st.area_chart(chart_data)

        st.markdown("### 📑 Transaksi Terbaru (Flagged by AI)")
        df_fraud = pd.DataFrame({
            "Waktu": ["14:20", "11:05", "09:15"],
            "Vendor": ["Unknown Cloud", "Supplier B", "Retail X"],
            "Jumlah": ["Rp 25.000.000", "Rp 150.000.000", "Rp 2.500.000"],
            "Status": ["Critical", "Warning", "Critical"]
        })
        st.table(df_fraud)

    elif "Users" in menu:
        st.subheader("👥 Manajemen Pengguna Sistem")
        st.write("Halaman ini hanya dapat diakses oleh Level Direksi.")
        users = pd.DataFrame({
            "Nama": ["Erwin Sinaga", "Jaya", "Shafen"],
            "Role": ["CEO", "Manager", "Admin"],
            "Status": ["Aktif", "Aktif", "Aktif"]
        })
        st.dataframe(users, use_container_width=True)

st.write("---")
st.caption(f"© 2026 V-Guard AI Systems | Developed for Erwin Sinaga")
