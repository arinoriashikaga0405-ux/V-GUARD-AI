import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="V-Guard AI Dashboard", page_icon="🛡️", layout="wide")

# --- 2. CSS MODERN DASHBOARD ---
st.markdown("""
<style>
    /* Sidebar Navigation Sticky */
    [data-testid="stSidebar"] { background-color: #0D47A1; border-right: 1px solid #e0e0e0; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* Header Utama Sticky Top */
    .sticky-header {
        position: sticky; top: 0; background: white; padding: 10px 20px;
        display: flex; justify-content: space-between; align-items: center;
        border-bottom: 1px solid #eee; z-index: 99; margin-bottom: 20px;
    }
    
    /* Widget & Card */
    .metric-card {
        background: white; padding: 20px; border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #f0f0f0;
    }
    .risk-high { border-left: 5px solid #F44336; background: #FFF5F5; }
    .risk-safe { border-left: 5px solid #4CAF50; background: #F6FFF6; }
</style>
""", unsafe_allow_html=True)

# --- 3. SESSION STATE (ROLE SIMULATION) ---
if 'role' not in st.session_state: st.session_state.role = "Admin" # Default Admin untuk Review Bapak
if 'page' not in st.session_state: st.session_state.page = "Dashboard Overview"

# --- 4. SIDEBAR NAVIGASI KIRI ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛡️ V-Guard AI</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # MENU UTAMA (Semua User)
    st.markdown("**MENU UTAMA**")
    if st.button("🏠 Dashboard Overview"): st.session_state.page = "Dashboard Overview"
    if st.button("📑 Transaksi"): st.session_state.page = "Transaksi"
    if st.button("🔔 Alarm & Notifikasi"): st.session_state.page = "Notifikasi"
    if st.button("📊 Laporan Keuangan"): st.session_state.page = "Laporan"
    if st.button("⚙️ Pengaturan Akun"): st.session_state.page = "Pengaturan"
    
    # MENU ADMIN (Hanya terlihat jika role == Admin)
    if st.session_state.role == "Admin":
        st.markdown("---")
        st.markdown("**ADMIN MENU**")
        if st.button("👥 Manajemen Pengguna"): st.session_state.page = "Manajemen Pengguna"
        if st.button("📜 Log Aktivitas"): st.session_state.page = "Log Aktivitas"
        if st.button("🤖 Konfigurasi AI/Rules"): st.session_state.page = "Rules"
        if st.button("🌍 Analisis Risiko Global"): st.session_state.page = "Global Risk"
    
    st.markdown("---")
    # User Profile/Logout di bagian bawah
    st.write(f"👤 {st.session_state.role}: Erwin Sinaga")
    if st.button("Logout"): st.stop()

# --- 5. HEADER UTAMA (STICKY TOP) ---
st.markdown(f"""
<div class="sticky-header">
    <div style="font-weight:bold; font-size:1.2rem; color:#0D47A1;">{st.session_state.page}</div>
    <div style="display:flex; gap:20px; align-items:center;">
        <input type="text" placeholder="Search transaksi/alert..." style="padding:5px 10px; border-radius:5px; border:1px solid #ddd;">
        <span>🔔</span> <span>❓</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. AREA KONTEN UTAMA ---

# A. DASHBOARD OVERVIEW
if st.session_state.page == "Dashboard Overview":
    c1, c2 = st.columns([1, 1])
    
    with c1:
        # Ringkasan Risiko
        st.markdown("""<div class="metric-card risk-high">
                    <h4 style="margin:0; color:#F44336;">Status Keamanan: HIGH RISK!</h4>
                    <p style="margin:0; font-size:0.9rem;">2 Alarm Aktif Memerlukan Verifikasi</p>
                    </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="metric-card">
                    <h4 style="margin:0; color:#0D47A1;">Ringkasan Akun</h4>
                    <p style="margin:0; font-size:1.2rem; font-weight:bold;">Total Saldo: Rp 1.420.000.000</p>
                    </div>""", unsafe_allow_html=True)

    st.markdown("### 📈 Proyeksi Cash Flow")
    df_flow = pd.DataFrame({'Bulan': ['Jan', 'Feb', 'Mar', 'Apr'], 'Actual': [100, 120, 115, 140], 'Projected': [100, 120, 115, 160]})
    fig = px.line(df_flow, x='Bulan', y=['Actual', 'Projected'], color_discrete_sequence=["#0D47A1", "#00BCD4"])
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### ⚠️ Transaksi Mencurigakan (AI Flagged)")
    data_fraud = {
        "Waktu": ["14:20", "11:05", "09:15"],
        "Vendor": ["Unknown Cloud", "Supplier B", "Retail X"],
        "Jumlah": ["Rp 25.000.000", "Rp 150.000.000", "Rp 2.500.000"],
        "Skor Risiko": ["High", "Medium", "High"]
    }
    st.table(pd.DataFrame(data_fraud))

# B. MANAJEMEN PENGGUNA (ADMIN ONLY)
elif st.session_state.page == "Manajemen Pengguna":
    st.subheader("👥 Daftar Pengguna Sistem")
    
    col_f1, col_f2 = st.columns([2, 1])
    with col_f1: st.text_input("Cari Nama atau Email...")
    with col_f2: st.selectbox("Filter Peran", ["Semua", "Admin", "User", "Viewer"])
    
    users = pd.DataFrame({
        "Nama": ["Erwin Sinaga", "Jaya", "Shafen", "Staff Keuangan"],
        "Email": ["erwin@vguard.com", "jaya@vguard.com", "shafen@vguard.com", "staff@vguard.com"],
        "Peran": ["Admin", "User", "Admin", "Viewer"],
        "Status": ["Aktif", "Aktif", "Aktif", "Non-Aktif"]
    })
    st.dataframe(users, use_container_width=True)
    
    st.markdown("---")
    c_btn1, c_btn2, c_btn3 = st.columns(3)
    with c_btn1: 
        if st.button("➕ Tambah Pengguna Baru"): st.info("Modal Form Pop-up Aktif")
    with c_btn2: st.button("✏️ Edit Role Selected")
    with c_btn3: st.button("🔑 Reset Password")

# Default untuk halaman lain yang sedang dikembangkan
else:
    st.info(f"Halaman {st.session_state.page} sedang dalam tahap integrasi data AI.")
